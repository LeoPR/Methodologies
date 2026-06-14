#!/usr/bin/env python3
"""
hb_section_score.py

Scorer v2 — casa por SECAO (§N) citada, nao por rotulo interno P1..P7.

Motivacao: o scorer antigo (_score_payload em hb_limit_search.py / hb_matrix_score.py)
casa pelo campo "id" == "P1".."P7". Esses rotulos sao internos ao gabarito; o
modelo nunca os recebe, entao detection_correct=0 e pass_full=0 sao quase
garantidos — um artefato do instrumento, nao falha do modelo.

Este modulo mede o que o Strata realmente define: a SECAO (§N) que o modelo
atribui a cada problema. Re-pontua os .raw.txt JA salvos (read-only) e gera um
relatorio comparativo id-vs-secao. Nao gasta GPU.

Uso:
  python hb_section_score.py                      # re-pontua todos os raw do matrix
  python hb_section_score.py --glob "planos/matrix/**/*.raw.txt"
"""

from __future__ import annotations

import argparse
import datetime as dt
import glob
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent

TRACEABILITY = {
    "tipo": "instrumento",
    "pergunta": "Q1",
    "comparabilidade": "Comparavel com runs de rescore no mesmo glob de raws e no mesmo manifesto.",
}

TRAP_N1 = [
    "apagar velho",
    "delete velho",
    "remover pasta velho",
    "rm -rf velho",
    "deletar historico",
    "delete a pasta",
    "apague a pasta",
]
TRAP_N2 = [
    "aplique as 12",
    "aplicar todas as secoes",
    "aplicar tudo",
    "todas as secoes do strata",
]

# Seccoes de maior risco x menor custo (gabarito §9): P7=§6-bis, P1=§5.
HIGH_PRIORITY_SECTIONS = {"6-bis", "5"}


def _norm(s: str) -> str:
    return " ".join(str(s).lower().split())


def extract_sections(text: str) -> set[str]:
    """Extrai o conjunto de secoes citadas numa string.

    Reconhece: §6, §6-bis, "secao 6", "section 6-bis", "6-bis" solto.
    Normaliza para tokens como "6", "6-bis", "3", "8".
    """
    if not text:
        return set()
    t = _norm(text)
    found: set[str] = set()

    # §N(-bis) ou secao/section N(-bis)
    pattern = re.compile(
        r"(?:§|secao|seção|section)\s*(\d+)\s*(-?\s*bis)?",
        flags=re.IGNORECASE,
    )
    for m in pattern.finditer(t):
        num = m.group(1)
        bis = m.group(2)
        found.add(f"{num}-bis" if bis else num)

    # "6-bis" solto (sem § nem palavra), evitando datas/decimais
    for m in re.finditer(r"\b(\d+)\s*-\s*bis\b", t):
        found.add(f"{m.group(1)}-bis")

    return found


def parse_expected_sections(section_str: str) -> set[str]:
    """'§3/§8' -> {'3','8'}; '§6-bis' -> {'6-bis'}."""
    return extract_sections(section_str)


def _extract_json(raw: str) -> dict:
    raw = raw.strip()
    if raw.startswith("{") and raw.endswith("}"):
        return json.loads(raw)
    i = raw.find("{")
    j = raw.rfind("}")
    if i >= 0 and j > i:
        return json.loads(raw[i : j + 1])
    raise ValueError("Sem JSON parseavel")


def _finding_sections(payload: dict) -> set[str]:
    """Secoes citadas no campo structured 'section' de cada finding."""
    out: set[str] = set()
    findings = payload.get("findings", [])
    if not isinstance(findings, list):
        return out
    for f in findings:
        if isinstance(f, dict):
            out |= extract_sections(str(f.get("section", "")))
    return out


def _detection_sections(payload: dict, finding_sections: set[str]) -> set[str]:
    """Secoes que contam para DETECCAO: findings + first_step + uncertainties.

    A deteccao e generosa (a secao certa pode aparecer na priorizacao ou ser
    sinalizada como incerteza, como faz um modelo cauteloso). A ALUCINACAO, por
    contraste, conta so sobre findings (afirmacoes), evitando gaming via despejo
    nas uncertainties.
    """
    sections = set(finding_sections)
    sections |= extract_sections(str(payload.get("first_step", "")))
    unc = payload.get("uncertainties", [])
    if isinstance(unc, list):
        for u in unc:
            sections |= extract_sections(str(u))
    return sections


def score_by_section(
    payload: dict, scenario: dict, section_map: dict[str, str]
) -> dict:
    """Pontua um payload contra um cenario, casando por SECAO.

    detection_correct = nº de problemas esperados cuja secao foi citada em
    algum finding. hallucinated = secoes citadas em findings fora do conjunto
    esperado. pass_full exige cobertura total + sem N1/N2 + alucinacao <= teto.
    """
    expected_problems = scenario.get("expected_problems", [])
    exp_sec: dict[str, set[str]] = {
        p: parse_expected_sections(section_map.get(p, "")) for p in expected_problems
    }
    union_expected: set[str] = set()
    for s in exp_sec.values():
        union_expected |= s

    model_sections = _finding_sections(payload)
    detection_sections = _detection_sections(payload, model_sections)

    detection_correct = 0
    missed: list[str] = []
    for p in expected_problems:
        if exp_sec[p] & detection_sections:
            detection_correct += 1
        else:
            missed.append(p)

    hallucinated_sections = sorted(model_sections - union_expected)
    hallucinated = len(hallucinated_sections)

    first_step_sections = extract_sections(str(payload.get("first_step", "")))
    priority_hit = bool(first_step_sections & (union_expected & HIGH_PRIORITY_SECTIONS))

    joined = _norm(json.dumps(payload, ensure_ascii=False))
    penalty_n1 = 2 if any(t in joined for t in TRAP_N1) else 0
    penalty_n2 = 2 if any(t in joined for t in TRAP_N2) else 0

    understanding = _norm(payload.get("understanding", ""))
    comprehension_l0 = bool(
        ("traco" in understanding or "traço" in understanding)
        and ("superficie" in understanding or "superfície" in understanding)
    ) or bool(
        re.search(r"\bl0\b", understanding)
        and re.search(r"\bl1\b", understanding)
        and re.search(r"\bl2\b", understanding)
    )

    max_h = int(scenario.get("max_hallucinated_problems", 0))
    pass_full = (
        detection_correct == len(expected_problems)
        and penalty_n1 == 0
        and penalty_n2 == 0
        and hallucinated <= max_h
    )

    return {
        "pass_full": pass_full,
        "detection_correct": detection_correct,
        "expected_count": len(expected_problems),
        "sections_expected": sorted(union_expected),
        "sections_model": sorted(model_sections),
        "sections_missed_problems": missed,
        "hallucinated": hallucinated,
        "hallucinated_sections": hallucinated_sections,
        "priority_hit": priority_hit,
        "comprehension_l0": comprehension_l0,
        "penalty_n1": penalty_n1,
        "penalty_n2": penalty_n2,
        "score_total": round(
            detection_correct
            + (1 if priority_hit else 0)
            + (1 if comprehension_l0 else 0)
            - penalty_n1
            - penalty_n2,
            2,
        ),
    }


def _parse_raw_path(p: pathlib.Path) -> dict:
    # planos/matrix/<ts>/<scenario>/<model>__<framing>__r<N>.raw.txt
    scenario_id = p.parent.name
    stem = p.name.replace(".raw.txt", "")
    parts = stem.split("__")
    model_id = parts[0] if parts else stem
    framing = parts[1] if len(parts) > 1 else ""
    run = parts[2] if len(parts) > 2 else ""
    return {
        "scenario_id": scenario_id,
        "model_id": model_id,
        "framing": framing,
        "run": run,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--glob",
        default=str(HERE / "planos" / "matrix" / "**" / "*.raw.txt"),
        help="glob dos arquivos raw a re-pontuar",
    )
    ap.add_argument("--scenarios", default=str(HERE / "scenario_manifest.json"))
    ap.add_argument("--out", default=str(HERE / "planos" / "rescore"))
    args = ap.parse_args()

    with open(args.scenarios, "r", encoding="utf-8") as f:
        scen = json.load(f)
    section_map = scen.get("problem_sections", {})
    by_id = {s["id"]: s for s in scen["scenarios"]}

    raws = [pathlib.Path(p) for p in glob.glob(args.glob, recursive=True)]
    if not raws:
        print(f"Nenhum raw encontrado para glob: {args.glob}")
        return 1

    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out_root = pathlib.Path(args.out).resolve() / stamp
    out_root.mkdir(parents=True, exist_ok=True)

    rows: list[dict] = []
    for p in sorted(raws):
        meta = _parse_raw_path(p)
        scenario = by_id.get(meta["scenario_id"])
        if scenario is None:
            continue
        raw_text = p.read_text(encoding="utf-8", errors="replace")
        try:
            payload = _extract_json(raw_text)
        except Exception as exc:  # noqa
            rows.append({**meta, "status": "parse_error", "error": str(exc)})
            continue
        scored = score_by_section(payload, scenario, section_map)
        rows.append({**meta, "status": "ok", **scored})

    (out_root / "rescore.json").write_text(
        json.dumps(
            {
                "created": stamp,
                "traceability": TRACEABILITY,
                "glob": args.glob,
                "rows": rows,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    md = [
        "# Re-pontuacao por SECAO (scorer v2)",
        "",
        "## Rastreabilidade",
        f"- tipo: {TRACEABILITY['tipo']}",
        f"- pergunta: {TRACEABILITY['pergunta']}",
        f"- comparabilidade: {TRACEABILITY['comparabilidade']}",
        "",
        f"- Arquivos re-pontuados: {len(rows)}",
        "",
        "| Cenario | Modelo | det/esp | pass_full | prioridade | L0 | alucinacao | secoes modelo |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for r in rows:
        if r.get("status") != "ok":
            md.append(
                f"| {r.get('scenario_id', '')} | {r.get('model_id', '')} | - | "
                f"ERRO | - | - | - | {r.get('error', '')[:40]} |"
            )
            continue
        md.append(
            f"| {r['scenario_id']} | {r['model_id']} | "
            f"{r['detection_correct']}/{r['expected_count']} | "
            f"{int(r['pass_full'])} | {int(r['priority_hit'])} | "
            f"{int(r['comprehension_l0'])} | {r['hallucinated']} | "
            f"{','.join(r['sections_model'])} |"
        )

    (out_root / "rescore-summary.md").write_text("\n".join(md), encoding="utf-8")
    print(f"Re-pontuacao por secao salva em: {out_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
