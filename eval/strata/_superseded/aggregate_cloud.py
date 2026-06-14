#!/usr/bin/env python3
"""Agrega a matriz NUVEM por braco e por SABOR (visao de falsa-inteligencia). Uso:
  python aggregate_cloud.py <cloud-key.json> <cloud-scores.json>"""
import json
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
PROBS = ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]
ARMS = ["cloud-baseline", "cloud-prose", "cloud-an"]

KEY = json.load(open(os.path.join(PLANOS, sys.argv[1]), encoding="utf-8"))
d = json.load(open(sys.argv[2], encoding="utf-8"))
r = d.get("result", d)
if isinstance(r, str):
    r = json.loads(r)
SC = {s["id"]: s for s in r["scores"]}


def rows(filt):
    return [SC[i] for i, m in KEY.items() if i in SC and filt(m)]


def df(rs):
    return round(sum(s["detection_found"] for s in rs) / len(rs), 2) if rs else None


def agg(rs):
    n = len(rs)
    found = {p: sum(1 for s in rs for x in s["detected"] if x["problem"] == p and x["found"]) for p in PROBS}
    return {"n": n, "df": round(sum(s["detection_found"] for s in rs) / n, 2),
            "ds": round(sum(s["detection_with_section"] for s in rs) / n, 2),
            "pr": round(sum(1 for s in rs if s["prioritized_risk"]) / n, 2),
            "n1": sum(1 for s in rs if s["traps"]["n1_delete"]),
            "n2": sum(1 for s in rs if s["traps"]["n2_apply_all"]),
            "coh": sum(1 for s in rs if s["coherent"]), "found": found}


o = []
o.append("=== POR BRACO (nuvem; 21 cada) ===")
o.append(f"{'braco':16} {'n':>2} {'det_found':>9} {'det_sec':>7} {'prior':>5} {'N1':>3} {'N2':>3} {'coer':>4}")
A = {}
for arm in ARMS:
    a = agg(rows(lambda m, arm=arm: m["arm"] == arm)); A[arm] = a
    o.append(f"{arm:16} {a['n']:>2} {a['df']:>9} {a['ds']:>7} {a['pr']:>5} {a['n1']:>3} {a['n2']:>3} {a['coh']:>4}")

o.append("\n=== DETECCAO POR PROBLEMA (found/21) ===")
o.append(f"{'braco':16} " + " ".join(f"{p:>4}" for p in PROBS))
for arm in ARMS:
    o.append(f"{arm:16} " + " ".join(f"{A[arm]['found'][p]:>4}" for p in PROBS))

models = sorted({m["model"] for m in KEY.values()})
o.append("\n=== POR SABOR x BRACO (det_found medio, N=3) — visao FALSA-INTELIGENCIA ===")
o.append(f"{'sabor':34} {'prose':>7} {'AN':>7} {'base':>7}")
for mdl in models:
    pr = df(rows(lambda m, mdl=mdl: m["model"] == mdl and m["arm"] == "cloud-prose"))
    an = df(rows(lambda m, mdl=mdl: m["model"] == mdl and m["arm"] == "cloud-an"))
    bl = df(rows(lambda m, mdl=mdl: m["model"] == mdl and m["arm"] == "cloud-baseline"))
    o.append(f"{mdl:34} {str(pr):>7} {str(an):>7} {str(bl):>7}")

o.append("\n=== vs LOCAL (det_found medio) ===")
o.append("  LOCAL : baseline 2.25 | prosa 2.50 | prosa-curta 3.92 | AN 4.58")
o.append(f"  NUVEM : baseline {A['cloud-baseline']['df']} | prosa {A['cloud-prose']['df']} | AN {A['cloud-an']['df']}")
print("\n".join(o))
open(r"C:\Users\leona\AppData\Local\Temp\agg_cloud.txt", "w", encoding="utf-8").write("\n".join(o))
