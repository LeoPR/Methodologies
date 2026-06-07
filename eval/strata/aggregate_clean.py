#!/usr/bin/env python3
"""Junta os scores cegos com a chave e agrega por braco/modelo. Uso:
  python aggregate_clean.py <workflow_output.json>"""
import json
import sys
from collections import defaultdict

HERE = __import__("os").path.dirname(__import__("os").path.abspath(__file__))
KEY = json.load(open(f"{HERE}/planos/clean-key.json", encoding="utf-8"))

d = json.load(open(sys.argv[1], encoding="utf-8"))
r = d.get("result", d)
if isinstance(r, str):
    r = json.loads(r)
scores = {s["id"]: s for s in r["scores"]}

ARMS = ["clean-prose", "clean-an", "clean-baseline"]
PROBS = ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]


def rows_for(filt):
    return [scores[oid] for oid, meta in KEY.items() if oid in scores and filt(meta)]


def agg(rows):
    n = len(rows)
    if not n:
        return None
    found = {p: 0 for p in PROBS}
    sect = {p: 0 for p in PROBS}
    for s in rows:
        for det in s["detected"]:
            if det["found"]:
                found[det["problem"]] += 1
            if det.get("section_cited_correct"):
                sect[det["problem"]] += 1
    return {
        "n": n,
        "det_found": round(sum(s["detection_found"] for s in rows) / n, 2),
        "det_sec": round(sum(s["detection_with_section"] for s in rows) / n, 2),
        "coher": round(sum(1 for s in rows if s["coherent"]) / n, 2),
        "prior": round(sum(1 for s in rows if s["prioritized_risk"]) / n, 2),
        "n1": sum(1 for s in rows if s["traps"]["n1_delete"]),
        "n2": sum(1 for s in rows if s["traps"]["n2_apply_all"]),
        "found": found, "sect": sect,
    }


out = []
out.append("===== POR BRACO (12 planos cada: 4 modelos x N=3) =====")
out.append(f"{'braco':16} {'n':>2} {'det_found':>9} {'det_sec':>7} {'coer':>5} {'prior':>5} {'N1':>3} {'N2':>3}")
A = {}
for arm in ARMS:
    a = agg(rows_for(lambda m, arm=arm: m["arm"] == arm))
    A[arm] = a
    out.append(f"{arm:16} {a['n']:>2} {a['det_found']:>9} {a['det_sec']:>7} {a['coher']:>5} {a['prior']:>5} {a['n1']:>3} {a['n2']:>3}")

out.append("\n===== DETECCAO POR PROBLEMA (found / 12) =====")
out.append(f"{'braco':16} " + " ".join(f"{p:>4}" for p in PROBS))
for arm in ARMS:
    a = A[arm]
    out.append(f"{arm:16} " + " ".join(f"{a['found'][p]:>4}" for p in PROBS))
out.append("\n  (P7=§6-bis fail-open ; P6=§6 sem-fonte — os gates mais criticos)")

out.append("\n===== COM SECAO CERTA POR PROBLEMA (/ 12; baseline nao recebe metodo) =====")
out.append(f"{'braco':16} " + " ".join(f"{p:>4}" for p in PROBS))
for arm in ARMS:
    a = A[arm]
    out.append(f"{arm:16} " + " ".join(f"{a['sect'][p]:>4}" for p in PROBS))

out.append("\n===== POR MODELO x BRACO (det_found medio, N=3) =====")
models = sorted({m["model"] for m in KEY.values()})
out.append(f"{'modelo':20} " + " ".join(f"{arm.replace('clean-',''):>9}" for arm in ARMS))
for mdl in models:
    cells = []
    for arm in ARMS:
        a = agg(rows_for(lambda m, arm=arm, mdl=mdl: m["arm"] == arm and m["model"] == mdl))
        cells.append(f"{a['det_found']:>9}" if a else f"{'-':>9}")
    out.append(f"{mdl:20} " + " ".join(cells))

# deltas
out.append("\n===== DELTAS (det_found medio) =====")
out.append(f"AN - baseline : {round(A['clean-an']['det_found'] - A['clean-baseline']['det_found'], 2)}")
out.append(f"prosa - baseline: {round(A['clean-prose']['det_found'] - A['clean-baseline']['det_found'], 2)}")
out.append(f"AN - prosa    : {round(A['clean-an']['det_found'] - A['clean-prose']['det_found'], 2)}")
out.append(f"P7 found: prosa={A['clean-prose']['found']['P7']}/12 AN={A['clean-an']['found']['P7']}/12 baseline={A['clean-baseline']['found']['P7']}/12")
out.append(f"P6 found: prosa={A['clean-prose']['found']['P6']}/12 AN={A['clean-an']['found']['P6']}/12 baseline={A['clean-baseline']['found']['P6']}/12")

open(r"C:\Users\leona\AppData\Local\Temp\clean_agg.txt", "w", encoding="utf-8").write("\n".join(out))
print("\n".join(out))
