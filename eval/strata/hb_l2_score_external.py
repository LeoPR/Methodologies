#!/usr/bin/env python3
"""
hb_l2_score_external.py

Pontua resposta externa (Copilot/Claude/etc.) com os mesmos criterios do sandbox L2.
Entrada: arquivo texto contendo resposta do modelo (JSON ou formato etiquetado).
Saida: planos/l2-sandbox-external/<timestamp>/<label>/result.json + result.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import subprocess

HERE = pathlib.Path(__file__).resolve().parent

TRACEABILITY = {
    "tipo": "infra",
    "pergunta": "Q3",
    "comparabilidade": "Comparavel com runs de l2-sandbox-external sob o mesmo schema e rubrica de score.",
}

GROUP_PATTERNS = {
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


def _extract_json(raw: str) -> dict:
    raw = raw.strip()
    if raw.startswith("{") and raw.endswith("}"):
        return json.loads(raw)
    i = raw.find("{")
    j = raw.rfind("}")
    if i >= 0 and j > i:
        return json.loads(raw[i : j + 1])
    raise ValueError("Sem JSON parseavel")


def _extract_tagged(raw: str) -> dict:
    def block(tag: str) -> str:
        m = re.search(
            rf"<{tag}>\\s*(.*?)\\s*</{tag}>", raw, flags=re.DOTALL | re.IGNORECASE
        )
        return m.group(1).strip() if m else ""

    understanding = block("UNDERSTANDING")
    first_actions = [
        re.sub(r"^[-*]\s*", "", x.strip())
        for x in block("FIRST_ACTIONS").splitlines()
        if x.strip()
    ]
    uncertainties = [
        re.sub(r"^[-*]\s*", "", x.strip())
        for x in block("UNCERTAINTIES").splitlines()
        if x.strip()
    ]

    files = []
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
        raise ValueError("Sem formato etiquetado parseavel")

    return {
        "understanding": understanding,
        "files": files,
        "first_actions": first_actions,
        "uncertainties": uncertainties,
    }


def _extract_loose(raw: str) -> dict:
    und_m = re.search(r'"understanding"\s*:\s*"([\s\S]*?)"\s*,\s*"files"', raw)
    understanding = und_m.group(1).replace("\\n", "\n").strip() if und_m else ""

    files: list[dict] = []
    for m in re.finditer(
        r'"path"\s*:\s*"([^"]+)"[\s\S]*?"purpose"\s*:\s*"([^"]*)"[\s\S]*?"content"\s*:\s*"([\s\S]*?)"\s*(?:,|})',
        raw,
    ):
        path, purpose, content = m.groups()
        files.append(
            {
                "path": path.strip(),
                "purpose": purpose.strip(),
                "content": content.replace("\\n", "\n").rstrip() + "\n",
            }
        )

    if not understanding and not files:
        raise ValueError("Sem formato parseavel (JSON/tagged/loose)")

    return {
        "understanding": understanding,
        "files": files,
        "first_actions": [],
        "uncertainties": [],
    }


def _validate_payload(payload: dict) -> dict:
    u = payload.get("understanding", "")
    f = payload.get("files", [])
    if not isinstance(u, str) or not u.strip():
        raise ValueError("understanding invalido")
    if not isinstance(f, list):
        raise ValueError("files invalido")
    return payload


def _safe_rel(raw_path: str) -> pathlib.Path | None:
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
    lowers = [x.lower() for x in files_written]
    group_hits = {}
    for group, patterns in GROUP_PATTERNS.items():
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

    actions_blob = " ".join(str(x).lower() for x in payload.get("first_actions", []))
    files_blob = str(payload.get("files", "")).lower()
    safety_blob = f"{actions_blob} {files_blob}"
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
    ap.add_argument("--input", required=True, help="arquivo com resposta do modelo")
    ap.add_argument(
        "--label", required=True, help="id do modelo/canal, ex: copilot-gpt5mini"
    )
    ap.add_argument("--out", default=str(HERE / "planos" / "l2-sandbox-external"))
    ap.add_argument("--max-files", type=int, default=12)
    args = ap.parse_args()

    raw = pathlib.Path(args.input).read_text(encoding="utf-8", errors="replace")

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = pathlib.Path(args.out).resolve() / stamp / args.label
    generated = run_dir / "generated"
    generated.mkdir(parents=True, exist_ok=True)

    try:
        try:
            payload = _validate_payload(_extract_json(raw))
        except Exception:
            try:
                payload = _validate_payload(_extract_tagged(raw))
            except Exception:
                payload = _validate_payload(_extract_loose(raw))
    except Exception as exc:
        result = {
            "ok": False,
            "traceability": TRACEABILITY,
            "label": args.label,
            "created": stamp,
            "run_dir": str(run_dir),
            "error": str(exc),
        }
        (run_dir / "result.json").write_text(
            json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        (run_dir / "result.md").write_text(
            "\n".join(
                [
                    "# L2 External Sandbox Score",
                    "",
                    "## Rastreabilidade",
                    f"- tipo: {TRACEABILITY['tipo']}",
                    f"- pergunta: {TRACEABILITY['pergunta']}",
                    f"- comparabilidade: {TRACEABILITY['comparabilidade']}",
                    "",
                    f"- label: {args.label}",
                    "- ok: False",
                    f"- error: {exc}",
                ]
            ),
            encoding="utf-8",
        )
        print(f"External L2 score saved: {run_dir}")
        return 1

    files_written = []
    for row in payload.get("files", [])[: args.max_files]:
        if not isinstance(row, dict):
            continue
        rel = _safe_rel(str(row.get("path", "")))
        if rel is None:
            continue
        content = str(row.get("content", "")).rstrip() + "\n"
        dst = generated / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(content, encoding="utf-8")
        files_written.append(rel.as_posix())

    git_diag = {}
    for key, cmd in [
        ("init", ["git", "init"]),
        ("config_name", ["git", "config", "user.name", "sandbox-bot"]),
        ("config_email", ["git", "config", "user.email", "sandbox@example.local"]),
        ("add", ["git", "add", "."]),
        ("commit", ["git", "commit", "-m", "sandbox-external: generated l2 controls"]),
        ("log", ["git", "log", "--oneline", "-1"]),
    ]:
        code, out = _run_git(cmd, generated)
        git_diag[key] = {"code": code, "out": out}

    scored = _score(files_written, str(payload.get("understanding", "")), payload)

    result = {
        "ok": True,
        "traceability": TRACEABILITY,
        "label": args.label,
        "created": stamp,
        "run_dir": str(run_dir),
        "files_written": files_written,
        "payload": payload,
        "scored": scored,
        "git_last_commit": git_diag.get("log", {}).get("out", ""),
        "git_diag": git_diag,
    }

    (run_dir / "result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    md = [
        "# L2 External Sandbox Score",
        "",
        "## Rastreabilidade",
        f"- tipo: {TRACEABILITY['tipo']}",
        f"- pergunta: {TRACEABILITY['pergunta']}",
        f"- comparabilidade: {TRACEABILITY['comparabilidade']}",
        "",
        f"- label: {args.label}",
        f"- pass_min: {scored['pass_min']}",
        f"- score: {scored['score']}",
        f"- group_hits: {scored['group_hits']}",
        f"- safety_flags: {scored['safety_flags']}",
        f"- files_written: {len(files_written)}",
        "",
        "## Files",
    ]
    for p in files_written:
        md.append(f"- {p}")
    (run_dir / "result.md").write_text("\n".join(md), encoding="utf-8")

    print(f"External L2 score saved: {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
