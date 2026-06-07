#!/usr/bin/env python3
"""Agrega varios braços (pares chave+scores) por braço/problema. Uso:
  python aggregate_all.py <key1.json> <scores1.json> [<key2.json> <scores2.json> ...]"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
PROBS = ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]

KEY, SCORES = {}, {}
args = sys.argv[1:]
for i in range(0, len(args), 2):
    KEY.update(json.load(open(os.path.join(PLANOS, args[i]), encoding="utf-8")))
    d = json.load(open(args[i + 1], encoding="utf-8"))
    r = d.get("result", d)
    if isinstance(r, str):
        r = json.loads(r)
    for s in r["scores"]:
        SCORES[s["id"]] = s

ARMS = ["clean-baseline", "clean-prose", "clean-curta", "clean-an"]
ARMS = [a for a in ARMS if any(m["arm"] == a for m in KEY.values())]


def rows(arm):
    return [SCORES[i] for i, m in KEY.items() if i in SCORES and m["arm"] == arm]


def agg(rs):
    n = len(rs)
    found = {p: sum(1 for s in rs for d in s["detected"] if d["problem"] == p and d["found"]) for p in PROBS}
    sect = {p: sum(1 for s in rs for d in s["detected"] if d["problem"] == p and d.get("section_cited_correct")) for p in PROBS}
    return {"n": n,
            "df": round(sum(s["detection_found"] for s in rs) / n, 2),
            "ds": round(sum(s["detection_with_section"] for s in rs) / n, 2),
            "pr": round(sum(1 for s in rs if s["prioritized_risk"]) / n, 2),
            "n1": sum(1 for s in rs if s["traps"]["n1_delete"]),
            "n2": sum(1 for s in rs if s["traps"]["n2_apply_all"]),
            "found": found, "sect": sect}


o = []
o.append(f"{'braco':16} {'n':>2} {'det_found':>9} {'det_sec':>7} {'prior':>5} {'N1':>3} {'N2':>3}")
A = {}
for arm in ARMS:
    a = agg(rows(arm)); A[arm] = a
    o.append(f"{arm:16} {a['n']:>2} {a['df']:>9} {a['ds']:>7} {a['pr']:>5} {a['n1']:>3} {a['n2']:>3}")
o.append("\nDETECCAO POR PROBLEMA (found / n):")
o.append(f"{'braco':16} " + " ".join(f"{p:>4}" for p in PROBS))
for arm in ARMS:
    o.append(f"{arm:16} " + " ".join(f"{A[arm]['found'][p]:>4}" for p in PROBS))
o.append("\nCHAVE comprimento x gate:")
if all(k in A for k in ("clean-baseline", "clean-curta", "clean-an", "clean-prose")):
    o.append(f"  det_found: baseline {A['clean-baseline']['df']} | prosa-longa {A['clean-prose']['df']} | "
             f"prosa-CURTA {A['clean-curta']['df']} | AN {A['clean-an']['df']}")
    o.append(f"  AN - curta = {round(A['clean-an']['df'] - A['clean-curta']['df'], 2)}  "
             f"(curta tem ~mesmo tamanho da AN, SEM gates)")
    o.append(f"  curta - baseline = {round(A['clean-curta']['df'] - A['clean-baseline']['df'], 2)}")
    o.append(f"  P7 fail-open found: baseline {A['clean-baseline']['found']['P7']} | prosa {A['clean-prose']['found']['P7']} | "
             f"curta {A['clean-curta']['found']['P7']} | AN {A['clean-an']['found']['P7']}")
print("\n".join(o))
open(r"C:\Users\leona\AppData\Local\Temp\agg_all.txt", "w", encoding="utf-8").write("\n".join(o))
