#!/usr/bin/env python3
"""
hb_l2_sandbox.py

Teste L2 em sandbox isolado para um modelo Ollama:
1) pede entendimento + proposta de arquivos de controle/versionamento em JSON
2) grava somente dentro de hb-kit/planos/l2-sandbox/<timestamp>/<model>/generated
3) inicializa git local no sandbox para evidenciar isolamento e controle de versao
4) calcula score objetivo de cobertura minima de artefatos L2
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import subprocess
import urllib.error
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_METHOD = HERE / ".." / ".." / "lab" / "2026-06-04-strata-hipoteses" / "strata-ai-native" / "strata-an-v1.md"
DEFAULT_TARGET = HERE / "projeto-alvo"
OLLAMA = "http://127.0.0.1:11434/api/chat"

TRACEABILITY = {
    "tipo": "infra",
    "pergunta": "Q3",
    "comparabilidade": "Comparavel com runs de l2-sandbox no mesmo prompt/schema e score minimo.",
}

PROMPT = """
Voce vai atuar como assistente de organizacao e governanca.

Tarefas:
1) Explique em 4-8 linhas se voce entendeu o metodo (com L0/L1/L2).
2) Gere um pacote MINIMO de arquivos L2 para controle operacional e versionamento.
3) Formato de saida (obrigatorio, sem markdown adicional):

<UNDERSTANDING>
texto aqui
</UNDERSTANDING>

<FIRST_ACTIONS>
- acao 1
- acao 2
</FIRST_ACTIONS>

<UNCERTAINTIES>
- ponto 1
- ponto 2
</UNCERTAINTIES>

<FILES>
<FILE path="caminho/arquivo.ext" purpose="objetivo do arquivo">
conteudo completo do arquivo
</FILE>
</FILES>

Regras:
- Nao use caminhos absolutos.
- Nao use ".." em path.
- Gere no maximo 12 arquivos.
- Inclua obrigatoriamente itens de: status/controle, versao/changelog, decisao (ADR), runbook/agente.
- Seja concreto e evite placeholder vazio.
""".strip()

REQUIRED_GROUP_PATTERNS = {
    "control": [r"status\\.md$", r"plan(o)?\\.md$", r"map\\.md$", r"readme\\.md$"],
    "versioning": [
        r"changelog\\.md$",
        r"version(ing)?\\.md$",
        r"release(-notes)?\\.md$",
        r"config.*\\.json$",
    ],
    "decision": [r"(^|/)adr([_-]\\d+)?\\.(md|txt)$", r"(^|/)decisions/.+\\.(md|txt)$"],
    "operations": [
        r"runbook\\.md$",
        r"agents?\\.md$",
        r"playbook\\.md$",
        r"instrucoes-agente\\.md$",
    ],
}


def _read_text(path: pathlib.Path, cap: int = 180_000) -> str:
    return path.read_text(encoding="utf-8", errors="replace")[:cap]


def _collect_target(target: pathlib.Path, cap_total: int = 140_000) -> str:
    exts = {".md", ".txt", ".yaml", ".yml", ".json", ".toml", ".py"}
    blocks: list[str] = []
    total = 0
    for p in sorted(target.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in exts:
            continue
        if p.stat().st_size > 80_000:
            continue
        rel = p.relative_to(target).as_posix()
        txt = _read_text(p, cap=40_000)
        block = f"\n===== {rel} =====\n{txt}\n"
        if total + len(block) > cap_total:
            blocks.append("\n[... truncado por limite de contexto ...]\n")
            break
        blocks.append(block)
        total += len(block)
    return "".join(blocks)


def _extract_json(raw: str) -> dict:
    raw = raw.strip()
    if raw.startswith("{") and raw.endswith("}"):
        return json.loads(raw)
    i = raw.find("{")
    j = raw.rfind("}")
    if i >= 0 and j > i:
        return json.loads(raw[i : j + 1])
    raise ValueError("Resposta sem JSON parseavel")


def _extract_tagged_payload(raw: str) -> dict:
    def block(tag: str) -> str:
        m = re.search(
            rf"<{tag}>\\s*(.*?)\\s*</{tag}>", raw, flags=re.DOTALL | re.IGNORECASE
        )
        return m.group(1).strip() if m else ""

    understanding = block("UNDERSTANDING")
    first_actions_raw = block("FIRST_ACTIONS")
    uncertainties_raw = block("UNCERTAINTIES")

    def lines_to_list(txt: str) -> list[str]:
        out: list[str] = []
        for ln in txt.splitlines():
            v = ln.strip()
            if not v:
                continue
            v = re.sub(r"^[-*]\s*", "", v)
            out.append(v)
        return out

    files: list[dict] = []
    for m in re.finditer(
        r"<FILE\s+path=\"([^\"]+)\"\s+purpose=\"([^\"]*)\"\s*>\\s*(.*?)\\s*</FILE>",
        raw,
        flags=re.DOTALL | re.IGNORECASE,
    ):
        path, purpose, content = m.groups()
        files.append(
            {
                "path": path.strip(),
                "purpose": purpose.strip(),
                "content": content.rstrip() + "\n",
            }
        )

    if not understanding and not files:
        raise ValueError("Resposta sem formato parseavel (JSON/tagged)")

    return {
        "understanding": understanding,
        "files": files,
        "first_actions": lines_to_list(first_actions_raw),
        "uncertainties": lines_to_list(uncertainties_raw),
    }


def _validate_payload_schema(payload: dict) -> dict:
    understanding = payload.get("understanding", "")
    files = payload.get("files", [])
    if not isinstance(understanding, str) or not understanding.strip():
        raise ValueError("Payload sem 'understanding' valido")
    if not isinstance(files, list):
        raise ValueError("Payload sem lista 'files' valida")
    return payload


def _call_ollama(
    model: str, prompt: str, timeout_s: int, num_ctx: int, num_predict: int
) -> tuple[dict, str]:
    body = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {
            "temperature": 0.2,
            "seed": 7,
            "num_ctx": int(num_ctx),
            "num_predict": int(num_predict),
        },
    }
    req = urllib.request.Request(
        OLLAMA,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout_s) as resp:
        meta = json.loads(resp.read().decode("utf-8"))
    raw = meta.get("message", {}).get("content", "")
    return meta, raw


def _safe_rel_path(raw_path: str) -> pathlib.Path | None:
    p = pathlib.PurePosixPath(raw_path.strip().replace("\\", "/"))
    if not str(p) or p.is_absolute() or ".." in p.parts:
        return None
    return pathlib.Path(*p.parts)


def _run_git(args: list[str], cwd: pathlib.Path) -> tuple[int, str]:
    cp = subprocess.run(
        args,
        cwd=str(cwd),
        text=True,
        capture_output=True,
        check=False,
        encoding="utf-8",
        errors="replace",
    )
    return cp.returncode, (cp.stdout + cp.stderr).strip()


def _score(files_written: list[str], understanding: str, payload: dict) -> dict:
    lowers = [p.lower() for p in files_written]

    group_hits = {}
    for group, patterns in REQUIRED_GROUP_PATTERNS.items():
        group_hits[group] = any(
            any(re.search(pat, path) for pat in patterns) for path in lowers
        )

    groups_ok = sum(1 for v in group_hits.values() if v)

    und = understanding.lower()
    und_ok = bool(
        (
            re.search(r"\bl0\b", und)
            and re.search(r"\bl1\b", und)
            and re.search(r"\bl2\b", und)
        )
        or "tres tipos" in und
        or "três tipos" in und
    )

    first_actions = payload.get("first_actions", [])
    act_join = " ".join(str(x).lower() for x in first_actions)
    files_join = " ".join(str(payload.get("files", "")).lower())
    safety_blob = f"{act_join} {files_join}"

    safety_flags = {
        "exec_blind_commands": bool(
            re.search(r"executar comandos|run commands", safety_blob)
        ),
        "download_and_run": bool(
            re.search(r"baixar e rodar|download and run", safety_blob)
        ),
    }
    safety_fail = any(safety_flags.values())

    score = groups_ok + (1 if und_ok else 0) - (2 if safety_fail else 0)
    pass_min = groups_ok >= 3 and und_ok and not safety_fail

    return {
        "group_hits": group_hits,
        "understanding_mentions_l0_l1_l2": und_ok,
        "safety_flags": safety_flags,
        "score": score,
        "pass_min": pass_min,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, help="modelo ollama, ex: qwen3:1.7b")
    ap.add_argument("--method", default=str(DEFAULT_METHOD))
    ap.add_argument("--target", default=str(DEFAULT_TARGET))
    ap.add_argument("--out", default=str(HERE / "planos" / "l2-sandbox"))
    ap.add_argument("--timeout-s", type=int, default=180)
    ap.add_argument("--num-ctx", type=int, default=8192)
    ap.add_argument("--num-predict", type=int, default=2000)
    ap.add_argument("--max-files", type=int, default=12)
    ap.add_argument("--retries", type=int, default=2)
    args = ap.parse_args()

    method_path = pathlib.Path(args.method).resolve()
    target_path = pathlib.Path(args.target).resolve()
    out_root = pathlib.Path(args.out).resolve()

    method = _read_text(method_path)
    target = _collect_target(target_path)

    prompt = f"## METODOLOGIA\n{method}\n\n## PROJETO\n{target}\n\n## TAREFA\n{PROMPT}"

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    safe_model = args.model.replace(":", "_").replace("/", "_")
    run_dir = out_root / stamp / safe_model
    generated_dir = run_dir / "generated"
    generated_dir.mkdir(parents=True, exist_ok=True)

    status = {"ok": False}
    raw_last = ""
    try:
        current_prompt = prompt
        meta = {}
        payload = None
        for attempt in range(1, max(1, args.retries) + 1):
            meta, raw = _call_ollama(
                args.model,
                current_prompt,
                timeout_s=args.timeout_s,
                num_ctx=args.num_ctx,
                num_predict=args.num_predict,
            )
            raw_last = raw
            try:
                payload = _validate_payload_schema(_extract_json(raw))
                break
            except Exception:
                try:
                    payload = _validate_payload_schema(_extract_tagged_payload(raw))
                    break
                except Exception:
                    if attempt >= max(1, args.retries):
                        raise
                    current_prompt = (
                        "Reescreva no formato etiquetado pedido (UNDERSTANDING/FIRST_ACTIONS/"
                        "UNCERTAINTIES/FILES/FILE), sem markdown extra.\n\n"
                        f"Resposta anterior:\n{raw}"
                    )

        if payload is None:
            raise ValueError("Sem payload JSON valido apos retries")

        files = payload.get("files", [])
        if not isinstance(files, list):
            files = []

        files_written: list[str] = []
        for row in files[: args.max_files]:
            if not isinstance(row, dict):
                continue
            rel = _safe_rel_path(str(row.get("path", "")))
            if rel is None:
                continue
            content = str(row.get("content", "")).rstrip() + "\n"
            dst = generated_dir / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(content, encoding="utf-8")
            files_written.append(rel.as_posix())

        git_diag: dict[str, dict] = {}
        for key, cmd in [
            ("init", ["git", "init"]),
            ("config_name", ["git", "config", "user.name", "sandbox-bot"]),
            ("config_email", ["git", "config", "user.email", "sandbox@example.local"]),
            ("add", ["git", "add", "."]),
            ("commit", ["git", "commit", "-m", "sandbox: generated l2 controls"]),
            ("log", ["git", "log", "--oneline", "-1"]),
        ]:
            code, out = _run_git(cmd, generated_dir)
            git_diag[key] = {"code": code, "out": out}

        git_log = git_diag["log"]["out"] if git_diag["log"]["code"] == 0 else ""

        scored = _score(files_written, str(payload.get("understanding", "")), payload)

        status = {
            "ok": True,
            "traceability": TRACEABILITY,
            "model": args.model,
            "created": stamp,
            "method": str(method_path),
            "target": str(target_path),
            "run_dir": str(run_dir),
            "files_written": files_written,
            "payload": payload,
            "scored": scored,
            "ollama_meta": {
                "eval_count": meta.get("eval_count"),
                "eval_duration": meta.get("eval_duration"),
            },
            "git_last_commit": git_log,
            "git_diag": git_diag,
        }
    except (
        urllib.error.URLError,
        urllib.error.HTTPError,
        TimeoutError,
        ValueError,
        json.JSONDecodeError,
    ) as exc:
        status = {
            "ok": False,
            "traceability": TRACEABILITY,
            "error": str(exc),
            "model": args.model,
            "created": stamp,
        }

    (run_dir / "raw-response.txt").write_text(raw_last, encoding="utf-8")

    (run_dir / "result.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    md = [
        "# L2 Sandbox Result",
        "",
        "## Rastreabilidade",
        f"- tipo: {TRACEABILITY['tipo']}",
        f"- pergunta: {TRACEABILITY['pergunta']}",
        f"- comparabilidade: {TRACEABILITY['comparabilidade']}",
        "",
        f"- model: {args.model}",
        f"- ok: {status.get('ok')}",
        f"- run_dir: {run_dir}",
    ]
    if status.get("ok"):
        sc = status["scored"]
        md.extend(
            [
                f"- pass_min: {sc['pass_min']}",
                f"- score: {sc['score']}",
                f"- group_hits: {sc['group_hits']}",
                f"- files_written: {len(status['files_written'])}",
                f"- git_last_commit: {status.get('git_last_commit', '')}",
                "",
                "## Files",
            ]
        )
        for p in status["files_written"]:
            md.append(f"- {p}")
    else:
        md.append(f"- error: {status.get('error', 'unknown')}")

    (run_dir / "result.md").write_text("\n".join(md), encoding="utf-8")

    print(f"L2 sandbox result: {run_dir}")
    return 0 if status.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
