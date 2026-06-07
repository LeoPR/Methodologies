#!/usr/bin/env python3
"""
hb_test_inventory.py

Consolida evidencias ja coletadas no hb-kit:
- runs de limit-search
- runs de matrix score

Saida:
- planos/evidence/<timestamp>/inventory.json
- planos/evidence/<timestamp>/inventory.md
"""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
PLANOS = HERE / "planos"

TRACEABILITY = {
    "tipo": "instrumento",
    "pergunta": "Q1/Q2/Q3",
    "comparabilidade": "Comparavel com inventarios anteriores; agrega runs existentes sem reexecutar testes.",
}


def _read(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _parse_limit_summary(path: pathlib.Path) -> dict:
    txt = _read(path)
    run_id = path.parent.name

    def pick(pattern: str, default: str = "") -> str:
        m = re.search(pattern, txt, flags=re.IGNORECASE)
        return m.group(1).strip() if m else default

    method = pick(r"- Metodo:\s*(.+)")
    scenarios = pick(r"- Cenarios:\s*(.+)")
    window = pick(r"- Janela de contexto testada:\s*(.+)")
    timeout = pick(r"- Timeout por chamada \(s\):\s*(.+)")

    rows = []
    for m in re.finditer(
        r"\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*([0-9.]+)\s*\|\s*([0-9.\-]+)\s*\|\s*([0-9.]+)\s*\|",
        txt,
    ):
        model, best_ctx, pass_rate, mean_score, tps = m.groups()
        if model.strip().lower() == "modelo":
            continue
        rows.append(
            {
                "model": model.strip(),
                "best_ctx": int(best_ctx),
                "pass_full_rate": float(pass_rate),
                "mean_score": float(mean_score),
                "tps": float(tps),
            }
        )

    return {
        "run_id": run_id,
        "summary_path": str(path),
        "method": method,
        "scenarios": scenarios,
        "ctx_window": window,
        "timeout_s": timeout,
        "rows": rows,
    }


def _parse_matrix_summary(path: pathlib.Path) -> dict:
    txt = _read(path)
    run_id = path.parent.name
    rows = []

    for m in re.finditer(
        r"\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*([0-9.\-]+)\s*\|",
        txt,
    ):
        model, tests, passed, mean_score = m.groups()
        if model.strip().lower() == "modelo":
            continue
        rows.append(
            {
                "model": model.strip(),
                "tests": int(tests),
                "passou_total": int(passed),
                "mean_score": float(mean_score),
            }
        )

    return {
        "run_id": run_id,
        "summary_path": str(path),
        "rows": rows,
    }


def _parse_l2_result(path: pathlib.Path) -> dict:
    run_id = path.parent.parent.name
    model_id = path.parent.name
    data = json.loads(_read(path))
    scored = data.get("scored", {}) if isinstance(data, dict) else {}
    return {
        "run_id": run_id,
        "model_id": model_id,
        "ok": bool(data.get("ok", False)),
        "error": str(data.get("error", "")),
        "pass_min": bool(scored.get("pass_min", False)),
        "score": float(scored.get("score", 0.0)) if scored else 0.0,
        "group_hits": scored.get("group_hits", {}),
        "safety_flags": scored.get("safety_flags", {}),
        "result_path": str(path),
    }


def main() -> int:
    limit_dir = PLANOS / "limit-search"
    matrix_dir = PLANOS / "matrix"
    l2_dir = PLANOS / "l2-sandbox"
    l2_external_dir = PLANOS / "l2-sandbox-external"

    limit_runs = []
    if limit_dir.exists():
        for sub in sorted(limit_dir.iterdir()):
            p = sub / "limit-search-summary.md"
            if p.exists():
                limit_runs.append(_parse_limit_summary(p))

    matrix_runs = []
    if matrix_dir.exists():
        for sub in sorted(matrix_dir.iterdir()):
            p = sub / "score-summary.md"
            if p.exists():
                matrix_runs.append(_parse_matrix_summary(p))

    l2_runs = []
    if l2_dir.exists():
        for stamp_dir in sorted(l2_dir.iterdir()):
            if not stamp_dir.is_dir():
                continue
            for model_dir in sorted(stamp_dir.iterdir()):
                p = model_dir / "result.json"
                if p.exists():
                    l2_runs.append(_parse_l2_result(p))

    l2_external_runs = []
    if l2_external_dir.exists():
        for stamp_dir in sorted(l2_external_dir.iterdir()):
            if not stamp_dir.is_dir():
                continue
            for label_dir in sorted(stamp_dir.iterdir()):
                p = label_dir / "result.json"
                if p.exists():
                    data = json.loads(_read(p))
                    scored = data.get("scored", {}) if isinstance(data, dict) else {}
                    l2_external_runs.append(
                        {
                            "run_id": stamp_dir.name,
                            "label": label_dir.name,
                            "ok": bool(data.get("ok", False)),
                            "pass_min": bool(scored.get("pass_min", False)),
                            "score": float(scored.get("score", 0.0)) if scored else 0.0,
                            "group_hits": scored.get("group_hits", {}),
                            "safety_flags": scored.get("safety_flags", {}),
                            "result_path": str(p),
                        }
                    )

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out = PLANOS / "evidence" / stamp
    out.mkdir(parents=True, exist_ok=True)

    payload = {
        "created": stamp,
        "traceability": TRACEABILITY,
        "limit_search_runs": limit_runs,
        "matrix_runs": matrix_runs,
        "l2_sandbox_runs": l2_runs,
        "l2_external_runs": l2_external_runs,
    }
    (out / "inventory.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    md = [
        "# Inventario de Evidencias H-B/H-C",
        "",
        "## Rastreabilidade",
        f"- tipo: {TRACEABILITY['tipo']}",
        f"- pergunta: {TRACEABILITY['pergunta']}",
        f"- comparabilidade: {TRACEABILITY['comparabilidade']}",
        "",
        "## Limit Search",
        f"- Runs encontrados: {len(limit_runs)}",
        "",
    ]

    for run in limit_runs:
        md.extend(
            [
                f"### {run['run_id']}",
                f"- Metodo: {run['method']}",
                f"- Cenarios: {run['scenarios']}",
                f"- Janela: {run['ctx_window']}",
                f"- Timeout: {run['timeout_s']}",
                "",
                "| Modelo | best_ctx | pass_full_rate | mean_score | tps |",
                "|---|---:|---:|---:|---:|",
            ]
        )
        for row in run["rows"]:
            md.append(
                f"| {row['model']} | {row['best_ctx']} | {row['pass_full_rate']:.2f} | "
                f"{row['mean_score']:.2f} | {row['tps']:.2f} |"
            )
        md.append("")

    md.extend(["## Matrix", f"- Runs encontrados: {len(matrix_runs)}", ""])
    for run in matrix_runs:
        md.extend(
            [
                f"### {run['run_id']}",
                "| Modelo | Testes | Passou total | Media score |",
                "|---|---:|---:|---:|",
            ]
        )
        for row in run["rows"]:
            md.append(
                f"| {row['model']} | {row['tests']} | {row['passou_total']} | {row['mean_score']:.2f} |"
            )
        md.append("")

    md.extend(["## L2 Sandbox", f"- Runs encontrados: {len(l2_runs)}", ""])
    md.extend(
        [
            "| Run | Modelo | ok | pass_min | score | control | versioning | decision | operations | safety_flags |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in l2_runs:
        gh = row.get("group_hits", {})
        sf = row.get("safety_flags", {})
        md.append(
            f"| {row['run_id']} | {row['model_id']} | {int(row['ok'])} | {int(row['pass_min'])} | "
            f"{row['score']:.2f} | {int(bool(gh.get('control', False)))} | "
            f"{int(bool(gh.get('versioning', False)))} | {int(bool(gh.get('decision', False)))} | "
            f"{int(bool(gh.get('operations', False)))} | {sf} |"
        )
    md.append("")

    md.extend(["## L2 External", f"- Runs encontrados: {len(l2_external_runs)}", ""])
    md.extend(
        [
            "| Run | Label | ok | pass_min | score | control | versioning | decision | operations | safety_flags |",
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---|",
        ]
    )
    for row in l2_external_runs:
        gh = row.get("group_hits", {})
        sf = row.get("safety_flags", {})
        md.append(
            f"| {row['run_id']} | {row['label']} | {int(row['ok'])} | {int(row['pass_min'])} | "
            f"{row['score']:.2f} | {int(bool(gh.get('control', False)))} | "
            f"{int(bool(gh.get('versioning', False)))} | {int(bool(gh.get('decision', False)))} | "
            f"{int(bool(gh.get('operations', False)))} | {sf} |"
        )
    md.append("")

    (out / "inventory.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Inventario salvo em: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
