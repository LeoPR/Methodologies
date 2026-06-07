#!/usr/bin/env python3
"""
hb_matrix_runner.py

Executa uma matriz automatica de avaliacao do Strata:
- modelos online/offline (catalogo matrix_models.json)
- cenarios sinteticos e fixture oficial (scenario_manifest.json)
- framing F1/F4

Seguranca:
- completion-only (sem tools)
- leitura de cenarios em modo read-only
- saida apenas dentro de hb-kit/planos/matrix/
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import re
import socket
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_METHOD_DOC = (
    HERE / ".." / ".." / ".." / "recipe" / "knowledge-architecture.md"
).resolve()
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

PROMPTS = {
    "F1": (
        "Voce vai avaliar a organizacao de um projeto contra uma metodologia. "
        "Leia a METODOLOGIA e os ARQUIVOS DO PROJETO abaixo. "
        "Responda SOMENTE em JSON valido, sem markdown, com este schema: "
        '{"understanding": string, '
        '"findings": [{"id": "P1|P2|P3|P4|P5|P6|P7|OTHER", '
        '"section": string, "severity": "high|medium|low", '
        '"evidence": [string], "why": string}], '
        '"first_step": string, "uncertainties": [string]} . '
        "Priorize; nao mande aplicar tudo. Se algo nao da para saber, diga em uncertainties."
    ),
    "F4": (
        "Voce vai avaliar a organizacao de um projeto contra uma metodologia. "
        "ANTES de qualquer outra coisa, cheque risco fail-open para agente (secao §6-bis). "
        "Depois continue o diagnostico completo. "
        "Responda SOMENTE em JSON valido, sem markdown, com este schema: "
        '{"understanding": string, '
        '"findings": [{"id": "P1|P2|P3|P4|P5|P6|P7|OTHER", '
        '"section": string, "severity": "high|medium|low", '
        '"evidence": [string], "why": string}], '
        '"first_step": string, "uncertainties": [string]} . '
        "Priorize; nao mande aplicar tudo."
    ),
}


def _read_text(path: pathlib.Path, cap: int = 250_000) -> str | None:
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
        text = _read_text(p)
        if text is None:
            continue
        block = f"\n===== {rel} =====\n{text}\n"
        if total + len(block) > cap_total:
            parts.append(f"\n[... truncado: limite {cap_total} chars ...]\n")
            break
        parts.append(block)
        total += len(block)
    return "".join(parts)


def _extract_json_object(raw: str) -> dict:
    raw = raw.strip()
    if raw.startswith("{") and raw.endswith("}"):
        return json.loads(raw)
    match = re.search(r"\{.*\}", raw, flags=re.S)
    if not match:
        raise ValueError("Resposta nao contem JSON parseavel")
    return json.loads(match.group(0))


def _call_ollama(model_cfg: dict, prompt: str, seed: int) -> str:
    url = "http://127.0.0.1:11434/api/chat"
    body = {
        "model": model_cfg["model"],
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {
            "temperature": 0.2,
            "seed": seed,
            "num_ctx": int(model_cfg.get("num_ctx", 20480)),
            "num_predict": int(model_cfg.get("num_predict", 2200)),
        },
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=1200) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data.get("message", {}).get("content", "")


def _call_openai_compat(model_cfg: dict, prompt: str) -> str:
    api_key = os.environ.get(model_cfg.get("api_key_env", ""), "")
    if not api_key:
        raise RuntimeError(f"API key ausente em {model_cfg.get('api_key_env')}")

    base = model_cfg["base_url"].rstrip("/")
    url = f"{base}/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    if "openrouter.ai" in base:
        headers["HTTP-Referer"] = "https://local.strata-hb"
        headers["X-Title"] = "strata-hb-matrix"

    body = {
        "model": model_cfg["model"],
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers=headers,
    )
    with urllib.request.urlopen(req, timeout=1200) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def _is_ollama_up() -> bool:
    try:
        sock = socket.create_connection(("127.0.0.1", 11434), timeout=1.5)
        sock.close()
        return True
    except OSError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", default=str(HERE / "matrix_models.json"))
    parser.add_argument("--scenarios", default=str(HERE / "scenario_manifest.json"))
    parser.add_argument("--method", default=str(DEFAULT_METHOD_DOC))
    parser.add_argument("--framing", nargs="*", default=["F1"])
    parser.add_argument("--runs", type=int, default=1)
    parser.add_argument("--channels", nargs="*", default=["offline", "online"])
    parser.add_argument("--only-model", nargs="*", default=[])
    parser.add_argument("--only-scenario", nargs="*", default=[])
    parser.add_argument("--out", default=str(HERE / "planos" / "matrix"))
    args = parser.parse_args()

    method_doc = pathlib.Path(args.method).resolve()
    method_txt = _read_text(method_doc)
    if not method_txt:
        raise SystemExit(f"Metodo nao lido: {method_doc}")

    with open(args.models, "r", encoding="utf-8") as f:
        model_catalog = json.load(f)
    with open(args.scenarios, "r", encoding="utf-8") as f:
        scenario_manifest = json.load(f)

    models = [m for m in model_catalog["models"] if m.get("enabled", False)]
    models = [m for m in models if m.get("channel") in set(args.channels)]
    if args.only_model:
        allowed = set(args.only_model)
        models = [m for m in models if m["id"] in allowed]

    scenarios = scenario_manifest["scenarios"]
    if args.only_scenario:
        allowed = set(args.only_scenario)
        scenarios = [s for s in scenarios if s["id"] in allowed]

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_root = pathlib.Path(args.out).resolve() / stamp
    guard_root = HERE.resolve()
    if guard_root not in out_root.parents:
        raise SystemExit("Recusado: --out fora de hb-kit")
    out_root.mkdir(parents=True, exist_ok=True)

    if any(m["provider"] == "ollama" for m in models) and not _is_ollama_up():
        print("AVISO: Ollama nao parece ativo em 127.0.0.1:11434")

    index: dict = {
        "created": stamp,
        "method": str(method_doc),
        "models": [m["id"] for m in models],
        "scenarios": [s["id"] for s in scenarios],
        "framing": args.framing,
        "runs": args.runs,
        "results": [],
    }

    for scenario in scenarios:
        scenario_dir = (HERE / scenario["path"]).resolve()
        scenario_text = _collect_project_text(scenario_dir)
        if not scenario_text.strip():
            print(f"SKIP scenario sem texto: {scenario['id']}")
            continue

        for model in models:
            for frame in args.framing:
                if frame not in PROMPTS:
                    continue
                for run in range(1, args.runs + 1):
                    test_id = f"{scenario['id']}__{model['id']}__{frame}__r{run}"
                    prompt = (
                        f"## METODOLOGIA\n{method_txt}\n\n"
                        f"## ARQUIVOS DO PROJETO\n{scenario_text}\n\n"
                        f"## TAREFA\n{PROMPTS[frame]}"
                    )
                    result_entry = {
                        "test_id": test_id,
                        "scenario_id": scenario["id"],
                        "model_id": model["id"],
                        "provider": model["provider"],
                        "channel": model["channel"],
                        "framing": frame,
                        "run": run,
                        "status": "ok",
                        "raw_file": "",
                        "json_file": "",
                        "error": "",
                    }

                    out_dir = out_root / scenario["id"]
                    out_dir.mkdir(parents=True, exist_ok=True)
                    raw_file = out_dir / f"{model['id']}__{frame}__r{run}.raw.txt"
                    json_file = out_dir / f"{model['id']}__{frame}__r{run}.json"

                    try:
                        if model["provider"] == "ollama":
                            raw = _call_ollama(model, prompt, seed=run)
                        elif model["provider"] == "openai_compat":
                            raw = _call_openai_compat(model, prompt)
                        else:
                            raise RuntimeError(
                                f"Provider nao suportado: {model['provider']}"
                            )

                        parsed = _extract_json_object(raw)
                        raw_file.write_text(raw, encoding="utf-8")
                        json_file.write_text(
                            json.dumps(parsed, ensure_ascii=False, indent=2),
                            encoding="utf-8",
                        )
                        result_entry["raw_file"] = str(
                            raw_file.relative_to(out_root).as_posix()
                        )
                        result_entry["json_file"] = str(
                            json_file.relative_to(out_root).as_posix()
                        )
                        print(f"OK {test_id}")
                    except (
                        urllib.error.HTTPError,
                        urllib.error.URLError,
                        RuntimeError,
                        ValueError,
                        KeyError,
                    ) as exc:
                        raw_file.write_text(f"ERRO: {exc}", encoding="utf-8")
                        result_entry["status"] = "error"
                        result_entry["error"] = str(exc)
                        result_entry["raw_file"] = str(
                            raw_file.relative_to(out_root).as_posix()
                        )
                        print(f"ERRO {test_id}: {exc}")

                    index["results"].append(result_entry)

    (out_root / "index.json").write_text(
        json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Matriz concluida. Saida: {out_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
