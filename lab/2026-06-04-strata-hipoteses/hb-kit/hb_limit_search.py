#!/usr/bin/env python3
"""
hb_limit_search.py

Auto-calibracao de limites para Strata em modelos locais (Ollama):
1) Para cada modelo, acha o maior num_ctx viavel por busca binaria.
2) Mede qualidade (pass_full) em cenarios-alvo nesse contexto.
3) Usa busca binaria na lista de modelos (forte -> fraco) para achar
   o menor modelo que ainda passa no criterio alvo.

Objetivo: evitar grade combinatoria e mapear fronteira possivel/impossivel.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import socket
import statistics
import time
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_METHOD_DOC = (HERE / "strata-an-v1.md").resolve()

TRACEABILITY = {
    "tipo": "evidencia",
    "pergunta": "Q1",
    "comparabilidade": "Comparavel com runs de limit-search anteriores no mesmo conjunto de cenarios/metodo.",
}

PROMPT_F1_JSON = (
    "Voce vai avaliar a organizacao de um projeto contra uma metodologia. "
    "Leia a METODOLOGIA e os ARQUIVOS DO PROJETO abaixo. "
    "Responda SOMENTE em JSON valido, sem markdown, com este schema: "
    '{"understanding": string, '
    '"findings": [{"id": "P1|P2|P3|P4|P5|P6|P7|OTHER", '
    '"section": string, "severity": "high|medium|low", '
    '"evidence": [string], "why": string}], '
    '"first_step": string, "uncertainties": [string]} . '
    "Priorize; nao mande aplicar tudo. Se algo nao da para saber, diga em uncertainties."
)

PROMPT_ANTI_N2_GUARD = (
    "Regra adicional de decisao: seja conservador contra falso-positivo. "
    "Se o cenario estiver bem estruturado, findings deve ficar vazio e first_step deve indicar manter como esta. "
    "Nunca recomende aplicar todas as secoes do Strata. "
    "Liste apenas achados com evidencia textual explicita."
)

EXTS = {
    ".md",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
    ".toml",
    ".ini",
    ".cfg",
    ".py",
    ".js",
    ".ts",
    ".csv",
}
SKIP_DIRS = {
    ".venv",
    "venv",
    "node_modules",
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    "dist",
    "build",
    "target",
    "out",
    ".next",
    "coverage",
    ".idea",
    ".vscode",
    "site-packages",
    ".tox",
    "vendor",
    "planos",
}

SECTION_EQUIV = {
    "§3/§8": ["§3", "§8", "secao 3", "secao 8", "section 3", "section 8"],
    "§6-bis": ["§6-bis", "§6 bis", "6-bis", "6 bis", "secao 6-bis", "section 6-bis"],
}

TRAP_N1 = [
    "apagar velho",
    "delete velho",
    "remover pasta velho",
    "rm -rf velho",
    "deletar historico",
]
TRAP_N2 = [
    "aplique as 12",
    "aplicar todas as secoes",
    "aplicar tudo",
    "todas as secoes do strata",
]


def _read_text(path: pathlib.Path, cap: int = 300_000) -> str | None:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:cap]
    except OSError:
        return None


def _collect_project_text(project_dir: pathlib.Path, cap_total: int = 180_000) -> str:
    parts: list[str] = []
    total = 0
    for p in sorted(project_dir.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(project_dir).as_posix()
        segs = set(rel.split("/"))
        if segs & SKIP_DIRS:
            continue
        if p.suffix.lower() not in EXTS:
            continue
        if p.stat().st_size > 80_000:
            continue
        txt = _read_text(p)
        if txt is None:
            continue
        block = f"\n===== {rel} =====\n{txt}\n"
        if total + len(block) > cap_total:
            parts.append(f"\n[... truncado: limite {cap_total} chars ...]\n")
            break
        parts.append(block)
        total += len(block)
    return "".join(parts)


def _norm(s: str) -> str:
    return " ".join(s.lower().split())


def _section_matches(expected: str, got: str) -> bool:
    got_n = _norm(got)
    if expected in got:
        return True
    if expected in SECTION_EQUIV:
        return any(token in got_n for token in SECTION_EQUIV[expected])
    return expected.lower() in got_n


def _extract_json(raw: str) -> dict:
    raw = raw.strip()
    if raw.startswith("{") and raw.endswith("}"):
        return json.loads(raw)
    i = raw.find("{")
    j = raw.rfind("}")
    if i >= 0 and j > i:
        return json.loads(raw[i : j + 1])
    raise ValueError("Sem JSON parseavel na resposta")


def _score_payload(payload: dict, scenario: dict, section_map: dict[str, str]) -> dict:
    findings = (
        payload.get("findings", [])
        if isinstance(payload.get("findings", []), list)
        else []
    )
    expected = scenario.get("expected_problems", [])
    expected_set = set(expected)

    by_id: dict[str, list[dict]] = {}
    for f in findings:
        if not isinstance(f, dict):
            continue
        pid = str(f.get("id", "")).strip().upper()
        if not pid:
            continue
        by_id.setdefault(pid, []).append(f)

    detection_correct = 0
    detection_partial = 0
    missed: list[str] = []

    for pid in expected:
        rows = by_id.get(pid, [])
        if not rows:
            missed.append(pid)
            continue
        expected_sec = section_map.get(pid, "")
        if any(_section_matches(expected_sec, str(r.get("section", ""))) for r in rows):
            detection_correct += 1
        else:
            detection_partial += 1

    hallucinated = 0
    for pid in by_id:
        if pid.startswith("P") and pid not in expected_set and pid != "OTHER":
            hallucinated += 1

    joined = _norm(json.dumps(payload, ensure_ascii=False))
    penalty_n1 = 2 if any(t in joined for t in TRAP_N1) else 0
    penalty_n2 = 2 if any(t in joined for t in TRAP_N2) else 0

    first_step = _norm(str(payload.get("first_step", "")))
    priority_score = 0
    if "P7" in expected_set and ("p7" in first_step or "6-bis" in first_step):
        priority_score += 1
    if "P1" in expected_set and (
        "p1" in first_step or "§5".lower() in first_step or "fonte unica" in first_step
    ):
        priority_score += 1

    max_h = int(scenario.get("max_hallucinated_problems", 0))
    pass_full = (
        detection_correct == len(expected)
        and penalty_n1 == 0
        and penalty_n2 == 0
        and hallucinated <= max_h
    )

    return {
        "pass_full": pass_full,
        "score_total": detection_correct
        + (0.5 * detection_partial)
        + priority_score
        - penalty_n1
        - penalty_n2,
        "detection_correct": detection_correct,
        "expected_count": len(expected),
        "hallucinated": hallucinated,
        "penalty_n1": penalty_n1,
        "penalty_n2": penalty_n2,
        "missed": missed,
    }


def _call_ollama(
    model: str,
    prompt: str,
    num_ctx: int | None,
    num_predict: int | None,
    seed: int,
    timeout_s: int,
    force_json_format: bool,
) -> tuple[str, dict, float]:
    url = "http://127.0.0.1:11434/api/chat"
    options = {
        "temperature": 0.2,
        "seed": seed,
    }
    if num_ctx is not None:
        options["num_ctx"] = int(num_ctx)
    if num_predict is not None:
        options["num_predict"] = int(num_predict)

    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": options,
    }
    if force_json_format:
        body["format"] = "json"
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    elapsed = time.time() - t0
    raw = data.get("message", {}).get("content", "")
    return raw, data, elapsed


def _probe_ctx(
    model_cfg: dict,
    method_text: str,
    scenario_text: str,
    ctx: int | None,
    timeout_s: int,
    num_predict_override: int | None,
    force_json_format: bool,
    prompt_suffix: str,
    use_catalog_num_predict: bool,
) -> tuple[bool, dict]:
    model_name = model_cfg["model"]
    num_predict = num_predict_override
    if num_predict is None and use_catalog_num_predict and "num_predict" in model_cfg:
        num_predict = int(model_cfg.get("num_predict", 2200))
    prompt = (
        f"## METODOLOGIA\n{method_text}\n\n## ARQUIVOS DO PROJETO\n{scenario_text}"
        f"\n\n## TAREFA\n{PROMPT_F1_JSON}\n{prompt_suffix}"
    )
    try:
        raw, meta, elapsed = _call_ollama(
            model_name,
            prompt,
            num_ctx=ctx,
            num_predict=num_predict,
            seed=7,
            timeout_s=timeout_s,
            force_json_format=force_json_format,
        )
        parse_ok = True
        parse_error = None
        try:
            _extract_json(raw)
        except (ValueError, json.JSONDecodeError) as exc:
            parse_ok = False
            parse_error = str(exc)[:300]

        if not str(raw).strip():
            return False, {
                "ctx": ctx,
                "num_predict": num_predict,
                "error_type": "EmptyResponse",
                "error": "Resposta vazia no probe de contexto",
            }

        eval_count = float(meta.get("eval_count", 0) or 0)
        eval_duration = float(meta.get("eval_duration", 0) or 0)
        tps = (eval_count / (eval_duration / 1e9)) if eval_duration else 0.0
        out = {
            "elapsed_s": elapsed,
            "decode_tps": tps,
            "eval_count": eval_count,
            "ctx": ctx,
            "num_predict": num_predict,
            "probe_json_ok": parse_ok,
        }
        if parse_error:
            out["probe_json_error"] = parse_error
        return True, out
    except (
        urllib.error.HTTPError,
        urllib.error.URLError,
        ValueError,
        json.JSONDecodeError,
        TimeoutError,
        socket.timeout,
        OSError,
    ) as exc:
        return False, {
            "ctx": ctx,
            "num_predict": num_predict,
            "error_type": type(exc).__name__,
            "error": str(exc)[:300],
        }


def _find_max_ctx(
    model_cfg: dict,
    method_text: str,
    scenario_text: str,
    lo: int,
    hi: int,
    timeout_s: int,
    force_json_format: bool,
    prompt_suffix: str,
    use_catalog_num_predict: bool,
    num_predict_override: int | None,
) -> tuple[int, list[dict]]:
    """Busca binaria do maior contexto viavel."""
    hist: list[dict] = []
    best = lo
    left, right = lo, hi

    ok, meta = _probe_ctx(
        model_cfg,
        method_text,
        scenario_text,
        lo,
        timeout_s,
        num_predict_override=num_predict_override,
        force_json_format=force_json_format,
        prompt_suffix=prompt_suffix,
        use_catalog_num_predict=use_catalog_num_predict,
    )
    hist.append({"ctx": lo, "ok": ok, **meta})
    if not ok:
        return 0, hist

    while left <= right:
        mid = (left + right) // 2
        ok, meta = _probe_ctx(
            model_cfg,
            method_text,
            scenario_text,
            mid,
            timeout_s,
            num_predict_override=num_predict_override,
            force_json_format=force_json_format,
            prompt_suffix=prompt_suffix,
            use_catalog_num_predict=use_catalog_num_predict,
        )
        hist.append({"ctx": mid, "ok": ok, **meta})
        if ok:
            best = mid
            left = mid + 1
        else:
            right = mid - 1
    return best, hist


def _evaluate_model(
    model_cfg: dict,
    scenarios: list[dict],
    scenario_texts: dict[str, str],
    method_text: str,
    section_map: dict[str, str],
    chosen_ctx: int,
    runs: int,
    eval_timeout_s: int,
    num_predict_override: int | None,
    verbose: bool,
    force_json_format: bool,
    prompt_suffix: str,
    use_catalog_num_predict: bool,
) -> dict:
    model_name = model_cfg["model"]
    num_predict = num_predict_override
    if num_predict is None and use_catalog_num_predict and "num_predict" in model_cfg:
        num_predict = int(model_cfg.get("num_predict", 2200))

    tests = 0
    full = 0
    scores: list[float] = []
    tps_list: list[float] = []
    elapsed_list: list[float] = []
    details: list[dict] = []

    for sc in scenarios:
        sid = sc["id"]
        stext = scenario_texts[sid]
        prompt = (
            f"## METODOLOGIA\n{method_text}\n\n## ARQUIVOS DO PROJETO\n{stext}"
            f"\n\n## TAREFA\n{PROMPT_F1_JSON}\n{prompt_suffix}"
        )
        for r in range(1, runs + 1):
            if verbose:
                print(
                    f"  RUN {model_cfg['id']} scenario={sid} r={r}/{runs} "
                    f"ctx={chosen_ctx if chosen_ctx is not None else 'default'} "
                    f"num_predict={num_predict if num_predict is not None else 'default'}",
                    flush=True,
                )
            tests += 1
            row = {"scenario_id": sid, "run": r, "status": "ok"}
            raw = None
            elapsed = None
            tps = None
            try:
                raw, meta, elapsed = _call_ollama(
                    model_name,
                    prompt,
                    num_ctx=chosen_ctx,
                    num_predict=num_predict,
                    seed=r,
                    timeout_s=eval_timeout_s,
                    force_json_format=force_json_format,
                )
                eval_count = float(meta.get("eval_count", 0) or 0)
                eval_duration = float(meta.get("eval_duration", 0) or 0)
                tps = (eval_count / (eval_duration / 1e9)) if eval_duration else 0.0

                payload = _extract_json(raw)
                scored = _score_payload(payload, sc, section_map)
                row.update(scored)
                row["elapsed_s"] = elapsed
                row["decode_tps"] = tps

                if scored["pass_full"]:
                    full += 1
                scores.append(float(scored["score_total"]))
                tps_list.append(tps)
                elapsed_list.append(elapsed)
            except Exception as exc:  # noqa
                row["status"] = "error"
                row["error_type"] = type(exc).__name__
                row["error"] = str(exc)[:300]
                if isinstance(raw, str) and raw.strip():
                    row["raw_preview"] = raw[:600]
                if elapsed is not None:
                    row["elapsed_s"] = elapsed
                if tps is not None:
                    row["decode_tps"] = tps
            details.append(row)

    pass_rate = (full / tests) if tests else 0.0
    return {
        "tests": tests,
        "pass_full_count": full,
        "pass_full_rate": pass_rate,
        "mean_score": statistics.mean(scores) if scores else 0.0,
        "median_decode_tps": statistics.median(tps_list) if tps_list else 0.0,
        "median_elapsed_s": statistics.median(elapsed_list) if elapsed_list else 0.0,
        "details": details,
    }


def _size_gb(model_name: str) -> float:
    # heuristica simples por prefixo nominal para desempate (cobertor curto)
    low = model_name.lower()
    if ":14b" in low:
        return 9.3
    if ":12b" in low:
        return 8.1
    if ":8b" in low:
        return 5.2
    if ":7b" in low:
        return 4.7
    if ":4b" in low:
        return 3.3
    if ":1.7b" in low:
        return 1.4
    if ":1b" in low:
        return 0.9
    if ":0.6b" in low:
        return 0.6
    return 99.0


def _model_quality_key(result: dict, model_cfg: dict) -> tuple:
    # Ordenacao para escolha "otima" dentro dos possiveis:
    # 1) pass_full_rate alto
    # 2) score medio alto
    # 3) tps alto
    # 4) tamanho baixo
    return (
        result["pass_full_rate"],
        result["mean_score"],
        result["median_decode_tps"],
        -_size_gb(model_cfg["model"]),
    )


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--models", default=str(HERE / "matrix_models.json"))
    p.add_argument("--scenarios", default=str(HERE / "scenario_manifest.json"))
    p.add_argument("--method", default=str(DEFAULT_METHOD_DOC))
    p.add_argument("--only-scenario", nargs="*", default=[])
    p.add_argument("--only-model", nargs="*", default=[])
    p.add_argument("--ctx-min", type=int, default=4096)
    p.add_argument("--ctx-max", type=int, default=32768)
    p.add_argument("--runs", type=int, default=1)
    p.add_argument("--target-pass-rate", type=float, default=1.0)
    p.add_argument("--timeout-s", type=int, default=240)
    p.add_argument(
        "--probe-timeout-s",
        type=int,
        default=None,
        help="Timeout para chamadas de probe de contexto (default: usa --timeout-s).",
    )
    p.add_argument(
        "--eval-timeout-s",
        type=int,
        default=None,
        help="Timeout para chamadas de avaliacao (default: usa --timeout-s).",
    )
    p.add_argument(
        "--use-model-default-context",
        action="store_true",
        help="Nao envia num_ctx; confia no contexto default do modelo no Ollama.",
    )
    p.add_argument(
        "--use-model-default-num-predict",
        action="store_true",
        help="Nao envia num_predict; confia no default do modelo no Ollama.",
    )
    p.add_argument(
        "--num-predict-override",
        type=int,
        default=None,
        help="Override explicito de num_predict (tem precedencia sobre config do catalogo).",
    )
    p.add_argument(
        "--verbose",
        action="store_true",
        help="Mostra parametros efetivos por run para execucao lenta e auditavel.",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Nao chama o modelo; apenas imprime parametros efetivos e tamanhos de prompt.",
    )
    p.add_argument(
        "--force-json-format",
        action="store_true",
        help="Envia format=json no payload do Ollama para reduzir quebra de JSON.",
    )
    p.add_argument(
        "--anti-n2-guard",
        action="store_true",
        help="Adiciona instrucoes conservadoras para reduzir N2 e falso-positivo antes de escalar.",
    )
    p.add_argument("--out", default=str(HERE / "planos" / "limit-search"))
    args = p.parse_args()

    method_path = pathlib.Path(args.method).resolve()
    method_text = _read_text(method_path)
    if not method_text:
        raise SystemExit(f"Metodo nao lido: {method_path}")

    with open(args.models, "r", encoding="utf-8") as f:
        mcat = json.load(f)
    with open(args.scenarios, "r", encoding="utf-8") as f:
        scen = json.load(f)

    models = [
        m for m in mcat["models"] if m.get("enabled") and m.get("provider") == "ollama"
    ]
    if args.only_model:
        allow_models = set(args.only_model)
        models = [m for m in models if m["id"] in allow_models]
    if not models:
        raise SystemExit("Sem modelos ollama enabled no catalogo")

    models.sort(key=lambda m: m.get("intelligence_rank", 0), reverse=True)

    scenarios = scen["scenarios"]
    if args.only_scenario:
        allow = set(args.only_scenario)
        scenarios = [s for s in scenarios if s["id"] in allow]
    if not scenarios:
        raise SystemExit("Sem cenarios selecionados")

    scenario_texts = {}
    for s in scenarios:
        txt = _collect_project_text((HERE / s["path"]).resolve())
        if not txt.strip():
            raise SystemExit(f"Cenario sem texto: {s['id']}")
        scenario_texts[s["id"]] = txt

    probe_timeout_s = (
        args.probe_timeout_s if args.probe_timeout_s is not None else args.timeout_s
    )
    eval_timeout_s = (
        args.eval_timeout_s if args.eval_timeout_s is not None else args.timeout_s
    )

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_root = pathlib.Path(args.out).resolve() / stamp
    out_root.mkdir(parents=True, exist_ok=True)

    # 1) Busca de contexto maximo por modelo (divisao sucessiva), exceto no modo default.
    ctx_results: dict[str, dict] = {}
    probe_scenario_text = scenario_texts[scenarios[0]["id"]]
    effective_num_predict = args.num_predict_override
    use_catalog_num_predict = not args.use_model_default_num_predict

    prompt_sizes = {
        sid: len(
            f"## METODOLOGIA\n{method_text}\n\n## ARQUIVOS DO PROJETO\n{scenario_texts[sid]}\n\n## TAREFA\n{PROMPT_F1_JSON}\n"
            f"{PROMPT_ANTI_N2_GUARD if args.anti_n2_guard else ''}"
        )
        for sid in scenario_texts
    }
    prompt_suffix = PROMPT_ANTI_N2_GUARD if args.anti_n2_guard else ""

    if args.dry_run:
        print("DRY-RUN limit-search", flush=True)
        print(f"  method={method_path}", flush=True)
        print(f"  method_chars={len(method_text)}", flush=True)
        print(f"  models={[m['id'] for m in models]}", flush=True)
        print(f"  scenarios={[s['id'] for s in scenarios]}", flush=True)
        print(
            "  effective_options: "
            f"num_ctx={'default' if args.use_model_default_context else f'{args.ctx_min}..{args.ctx_max}'} "
            f"num_predict={effective_num_predict if effective_num_predict is not None else 'default'} "
            f"probe_timeout_s={probe_timeout_s} eval_timeout_s={eval_timeout_s} runs={args.runs} "
            f"force_json_format={args.force_json_format} anti_n2_guard={args.anti_n2_guard}",
            flush=True,
        )
        for sid in sorted(prompt_sizes):
            print(
                f"  scenario={sid} scenario_chars={len(scenario_texts[sid])} prompt_chars={prompt_sizes[sid]}",
                flush=True,
            )

        dry = {
            "created": stamp,
            "mode": "dry-run",
            "method": str(method_path),
            "method_chars": len(method_text),
            "models": [m["id"] for m in models],
            "scenarios": [s["id"] for s in scenarios],
            "prompt_sizes": prompt_sizes,
            "use_model_default_context": args.use_model_default_context,
            "use_model_default_num_predict": args.use_model_default_num_predict,
            "num_predict_override": args.num_predict_override,
            "ctx_min": args.ctx_min,
            "ctx_max": args.ctx_max,
            "probe_timeout_s": probe_timeout_s,
            "eval_timeout_s": eval_timeout_s,
            "runs": args.runs,
            "force_json_format": args.force_json_format,
            "anti_n2_guard": args.anti_n2_guard,
        }
        (out_root / "limit-search-dry-run.json").write_text(
            json.dumps(dry, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"Dry-run salvo: {out_root}", flush=True)
        return 0

    for m in models:
        if args.use_model_default_context:
            print(
                f"CTX default -> {m['id']} ({m['model']}) "
                f"num_ctx=default num_predict="
                f"{effective_num_predict if effective_num_predict is not None else 'default'}",
                flush=True,
            )
            ok, meta = _probe_ctx(
                m,
                method_text,
                probe_scenario_text,
                None,
                probe_timeout_s,
                num_predict_override=effective_num_predict,
                force_json_format=args.force_json_format,
                prompt_suffix=prompt_suffix,
                use_catalog_num_predict=use_catalog_num_predict,
            )
            best_ctx = -1 if ok else 0
            ctx_results[m["id"]] = {
                "best_ctx": best_ctx,
                "history": [{"ctx": "default", "ok": ok, **meta}],
            }
        else:
            print(f"CTX search -> {m['id']} ({m['model']})", flush=True)
            best_ctx, hist = _find_max_ctx(
                m,
                method_text,
                probe_scenario_text,
                args.ctx_min,
                args.ctx_max,
                probe_timeout_s,
                force_json_format=args.force_json_format,
                prompt_suffix=prompt_suffix,
                use_catalog_num_predict=use_catalog_num_predict,
                num_predict_override=effective_num_predict,
            )
            print(f"  best_ctx={best_ctx}", flush=True)
            ctx_results[m["id"]] = {"best_ctx": best_ctx, "history": hist}

    # 2) Busca binaria no eixo de modelos (forte->fraco)
    # monotonia aproximada: se um modelo fraco passa, os mais fortes tendem a passar.
    eval_cache: dict[str, dict] = {}

    def eval_model_at(i: int) -> dict:
        m = models[i]
        mid = m["id"]
        if mid in eval_cache:
            return eval_cache[mid]
        print(f"EVAL -> {mid} ({m['model']})", flush=True)
        best_ctx = int(ctx_results[mid]["best_ctx"])
        chosen_ctx = None if best_ctx == -1 else best_ctx
        if best_ctx == 0:
            res = {
                "model_id": mid,
                "model": m["model"],
                "best_ctx": 0,
                "pass_full_rate": 0.0,
                "mean_score": 0.0,
                "median_decode_tps": 0.0,
                "tests": 0,
                "pass_full_count": 0,
                "details": [],
            }
        else:
            scored = _evaluate_model(
                m,
                scenarios=scenarios,
                scenario_texts=scenario_texts,
                method_text=method_text,
                section_map=scen.get("problem_sections", {}),
                chosen_ctx=chosen_ctx,
                runs=args.runs,
                eval_timeout_s=eval_timeout_s,
                num_predict_override=effective_num_predict,
                verbose=args.verbose,
                force_json_format=args.force_json_format,
                prompt_suffix=prompt_suffix,
                use_catalog_num_predict=use_catalog_num_predict,
            )
            res = {
                "model_id": mid,
                "model": m["model"],
                "best_ctx": chosen_ctx,
                **scored,
            }
        eval_cache[mid] = res
        return res

    n = len(models)
    lo, hi = 0, n - 1

    # avalia extremos primeiro (tatear possiveis/impossiveis)
    _ = eval_model_at(lo)
    _ = eval_model_at(hi)

    boundary = None
    while lo <= hi:
        mid = (lo + hi) // 2
        res = eval_model_at(mid)
        ok = res["pass_full_rate"] >= args.target_pass_rate
        if ok:
            boundary = mid
            lo = mid + 1  # tenta descer para mais fraco ainda
        else:
            hi = mid - 1

    # refino local para nao-monotonia: testa vizinhos da fronteira
    if boundary is not None:
        for j in [boundary - 1, boundary + 1]:
            if 0 <= j < n:
                _ = eval_model_at(j)

    # melhores "uteis" entre os que batem target
    candidates = []
    for i, m in enumerate(models):
        r = eval_model_at(i)
        if r["pass_full_rate"] >= args.target_pass_rate:
            candidates.append((i, m, r))

    chosen = None
    if candidates:
        chosen = max(candidates, key=lambda t: _model_quality_key(t[2], t[1]))

    report = {
        "created": stamp,
        "traceability": TRACEABILITY,
        "method": str(method_path),
        "ctx_search": {"ctx_min": args.ctx_min, "ctx_max": args.ctx_max},
        "scenarios": [s["id"] for s in scenarios],
        "runs": args.runs,
        "target_pass_rate": args.target_pass_rate,
        "use_model_default_context": args.use_model_default_context,
        "use_model_default_num_predict": args.use_model_default_num_predict,
        "num_predict_override": args.num_predict_override,
        "force_json_format": args.force_json_format,
        "anti_n2_guard": args.anti_n2_guard,
        "models_order": [m["id"] for m in models],
        "ctx_results": ctx_results,
        "evaluated": eval_cache,
        "boundary_index": boundary,
        "chosen": {
            "index": chosen[0],
            "model_id": chosen[1]["id"],
            "model": chosen[1]["model"],
            "result": chosen[2],
        }
        if chosen
        else None,
    }

    (out_root / "limit-search.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    md = [
        "# Limit Search Strata (offline)",
        "",
        "## Rastreabilidade",
        f"- tipo: {TRACEABILITY['tipo']}",
        f"- pergunta: {TRACEABILITY['pergunta']}",
        f"- comparabilidade: {TRACEABILITY['comparabilidade']}",
        "",
        "## Resumo",
        f"- Metodo: {method_path}",
        f"- Cenarios: {', '.join([s['id'] for s in scenarios])}",
        f"- Janela de contexto testada: {args.ctx_min}..{args.ctx_max}",
        f"- Timeout por chamada (s): {args.timeout_s}",
        f"- Probe timeout por chamada (s): {probe_timeout_s}",
        f"- Eval timeout por chamada (s): {eval_timeout_s}",
        f"- Runs por cenario: {args.runs}",
        f"- Target pass_full_rate: {args.target_pass_rate}",
        f"- Contexto: {'default do modelo' if args.use_model_default_context else f'{args.ctx_min}..{args.ctx_max}'}",
        f"- num_predict: {effective_num_predict if effective_num_predict is not None else 'default do modelo'}",
        "",
        "## Fronteira modelo",
        f"- Boundary index: {boundary}",
        "",
        "## Escolha recomendada",
    ]
    if chosen:
        _, m, r = chosen
        md.extend(
            [
                f"- Modelo: {m['id']} ({m['model']})",
                f"- Maior contexto viavel: {r['best_ctx']}",
                f"- pass_full_rate: {r['pass_full_rate']:.2f}",
                f"- mean_score: {r['mean_score']:.2f}",
                f"- median_decode_tps: {r['median_decode_tps']:.2f}",
            ]
        )
    else:
        md.append("- Nenhum modelo atingiu target_pass_rate.")

    md.extend(
        [
            "",
            "## Avaliado por modelo",
            "",
            "| Modelo | best_ctx | pass_full_rate | mean_score | tps |",
            "|---|---:|---:|---:|---:|",
        ]
    )

    for m in models:
        r = eval_cache[m["id"]]
        ctx_display = (
            "default" if r.get("best_ctx") is None else str(int(r.get("best_ctx", 0)))
        )
        md.append(
            f"| {m['id']} | {ctx_display} | {float(r['pass_full_rate']):.2f} | "
            f"{float(r['mean_score']):.2f} | {float(r['median_decode_tps']):.2f} |"
        )

    (out_root / "limit-search-summary.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Limit search concluido: {out_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
