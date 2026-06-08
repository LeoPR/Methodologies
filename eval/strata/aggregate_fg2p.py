#!/usr/bin/env python3
"""Agrega o R8-FG2P (projeto messy) por braco. Uso: python aggregate_fg2p.py <fg2p-key.json> <scores.json>"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
ARMS = ["real-fg2p-baseline", "real-fg2p-prose", "real-fg2p-an"]
KEY = json.load(open(os.path.join(PLANOS, sys.argv[1]), encoding="utf-8"))
d = json.load(open(sys.argv[2], encoding="utf-8"))
r = d.get("result", d)
if isinstance(r, str):
    r = json.loads(r)
SC = {s["id"]: s for s in r["scores"]}


def rows(arm):
    return [SC[i] for i, m in KEY.items() if i in SC and m["arm"] == arm]


o = []
o.append(f"{'braco':22} {'n':>2} {'genuino':>7} {'aluc':>5} {'crit.bom':>8} {'prior':>5}")
for arm in ARMS:
    rs = rows(arm); n = len(rs)
    o.append(f"{arm:22} {n:>2} {round(sum(s['genuine_found'] for s in rs)/n,2):>7} "
             f"{round(sum(s['hallucinated'] for s in rs)/n,2):>5} "
             f"{round(sum(1 for s in rs if s['false_criticism_good'])/n,2):>8} "
             f"{round(sum(1 for s in rs if s['prioritized_risk'])/n,2):>5}")
o.append("\nLEITURA: num projeto MESSY, o metodo (AN/prosa) acha mais GENUINOS que o baseline (= ajuda)?")
print("\n".join(o))
open(r"C:\Users\leona\AppData\Local\Temp\agg_fg2p.txt", "w", encoding="utf-8").write("\n".join(o))
