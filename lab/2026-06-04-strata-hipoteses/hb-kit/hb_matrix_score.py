#!/usr/bin/env python3
"""
hb_matrix_score.py

Score automatico da matriz gerada por hb_matrix_runner.py.
Criterio central para "resolve totalmente":
- encontrou todos os problemas esperados do cenario
- sem penalidade N1/N2
- dentro do teto de alucinacao permitido
"""

from __future__ import annotations

import argparse
import csv
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent

TRACEABILITY = {
    "tipo": "evidencia",
    "pergunta": "Q1",
    "comparabilidade": "Comparavel com runs da matrix no mesmo manifesto de cenarios e rubrica.",
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


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()


def _section_matches(expected: str, got: str) -> bool:
    got_n = _norm(got)
    if expected in got:
        return True
    if expected in SECTION_EQUIV:
        return any(token in got_n for token in SECTION_EQUIV[expected])
    return expected.lower() in got_n


def _collect_foundings(payload: dict) -> list[dict]:
    findings = payload.get("findings", [])
    if isinstance(findings, list):
        return [f for f in findings if isinstance(f, dict)]
    return []


def _score_one(payload: dict, scenario: dict, section_map: dict) -> dict:
    findings = _collect_foundings(payload)
    expected = scenario.get("expected_problems", [])
    expected_set = set(expected)

    found_by_id: dict[str, list[dict]] = {}
    for f in findings:
        pid = str(f.get("id", "")).strip().upper()
        if not pid:
            continue
        found_by_id.setdefault(pid, []).append(f)

    detection_correct = 0
    detection_partial = 0
    missed: list[str] = []
    for pid in expected:
        rows = found_by_id.get(pid, [])
        if not rows:
            missed.append(pid)
            continue
        expected_sec = section_map.get(pid, "")
        if any(_section_matches(expected_sec, str(r.get("section", ""))) for r in rows):
            detection_correct += 1
        else:
            detection_partial += 1

    hallucinated = 0
    for pid in found_by_id:
        if pid.startswith("P") and pid not in expected_set and pid != "OTHER":
            hallucinated += 1

    joined = _norm(json.dumps(payload, ensure_ascii=False))
    penalty_n1 = 2 if any(token in joined for token in TRAP_N1) else 0
    penalty_n2 = 2 if any(token in joined for token in TRAP_N2) else 0

    first_step = _norm(str(payload.get("first_step", "")))
    priority_score = 0
    if "P7" in expected_set and (
        "p7" in first_step or "§6-bis".lower() in first_step or "6-bis" in first_step
    ):
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

    score_total = (
        detection_correct
        + (0.5 * detection_partial)
        + priority_score
        - penalty_n1
        - penalty_n2
    )

    return {
        "expected_count": len(expected),
        "detection_correct": detection_correct,
        "detection_partial": detection_partial,
        "missed": missed,
        "hallucinated": hallucinated,
        "priority_score": priority_score,
        "penalty_n1": penalty_n1,
        "penalty_n2": penalty_n2,
        "pass_full": pass_full,
        "score_total": score_total,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--run",
        required=True,
        help="Pasta de run criada por hb_matrix_runner (contendo index.json)",
    )
    parser.add_argument("--scenarios", default=str(HERE / "scenario_manifest.json"))
    args = parser.parse_args()

    run_dir = pathlib.Path(args.run).resolve()
    index_file = run_dir / "index.json"
    if not index_file.exists():
        raise SystemExit(f"index.json nao encontrado em: {run_dir}")

    with open(index_file, "r", encoding="utf-8") as f:
        index = json.load(f)
    with open(args.scenarios, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    scenario_map = {s["id"]: s for s in manifest["scenarios"]}
    section_map = manifest.get("problem_sections", {})

    rows = []
    summary_by_model: dict[str, dict] = {}

    for item in index.get("results", []):
        scenario_id = item["scenario_id"]
        model_id = item["model_id"]
        status = item.get("status", "error")

        row = {
            "test_id": item.get("test_id", ""),
            "scenario_id": scenario_id,
            "model_id": model_id,
            "framing": item.get("framing", ""),
            "run": item.get("run", 0),
            "status": status,
            "score_total": 0.0,
            "pass_full": False,
            "detection_correct": 0,
            "expected_count": 0,
            "hallucinated": 0,
            "priority_score": 0,
            "penalty_n1": 0,
            "penalty_n2": 0,
            "missed": "",
        }

        if status == "ok":
            json_rel = item.get("json_file", "")
            payload = json.loads((run_dir / json_rel).read_text(encoding="utf-8"))
            scenario = scenario_map[scenario_id]
            scored = _score_one(payload, scenario, section_map)
            row.update(
                {
                    "score_total": scored["score_total"],
                    "pass_full": scored["pass_full"],
                    "detection_correct": scored["detection_correct"],
                    "expected_count": scored["expected_count"],
                    "hallucinated": scored["hallucinated"],
                    "priority_score": scored["priority_score"],
                    "penalty_n1": scored["penalty_n1"],
                    "penalty_n2": scored["penalty_n2"],
                    "missed": ",".join(scored["missed"]),
                }
            )

        rows.append(row)
        key = f"{model_id}"
        stats = summary_by_model.setdefault(
            key, {"tests": 0, "pass_full": 0, "sum_score": 0.0}
        )
        stats["tests"] += 1
        stats["sum_score"] += float(row["score_total"])
        if row["pass_full"]:
            stats["pass_full"] += 1

    csv_file = run_dir / "score.csv"
    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "test_id",
                "scenario_id",
                "model_id",
                "framing",
                "run",
                "status",
                "score_total",
                "pass_full",
                "detection_correct",
                "expected_count",
                "hallucinated",
                "priority_score",
                "penalty_n1",
                "penalty_n2",
                "missed",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    (run_dir / "score.json").write_text(
        json.dumps(
            {
                "traceability": TRACEABILITY,
                "run_dir": run_dir.as_posix(),
                "rows": rows,
                "summary_by_model": summary_by_model,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    summary_md = [
        "# Score matriz H-B/H-C",
        "",
        "## Rastreabilidade",
        f"- tipo: {TRACEABILITY['tipo']}",
        f"- pergunta: {TRACEABILITY['pergunta']}",
        f"- comparabilidade: {TRACEABILITY['comparabilidade']}",
        "",
        "## Criterio de resolucao total",
        "- detection_correct == expected_count",
        "- sem N1/N2",
        "- hallucinated <= teto do cenario",
        "",
        "## Resultado por modelo",
        "",
        "| Modelo | Testes | Passou total | Media score |",
        "|---|---:|---:|---:|",
    ]
    for model_id, stats in sorted(summary_by_model.items()):
        avg = stats["sum_score"] / max(stats["tests"], 1)
        summary_md.append(
            f"| {model_id} | {stats['tests']} | {stats['pass_full']} | {avg:.2f} |"
        )

    summary_md.extend(
        [
            "",
            f"Arquivos: score.csv e score-summary.md em {run_dir.as_posix()}",
        ]
    )

    (run_dir / "score-summary.md").write_text("\n".join(summary_md), encoding="utf-8")
    print(f"Score concluido: {run_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
