#!/usr/bin/env python3
"""Agrega o R8 (projeto real) por braco. Uso: python aggregate_r8.py <real-key.json> <scores.json>"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
ARMS = ["real-pdf2md-baseline", "real-pdf2md-prose", "real-pdf2md-an"]

KEY = json.load(open(os.path.join(PLANOS, sys.argv[1]), encoding="utf-8"))
d = json.load(open(sys.argv[2], encoding="utf-8"))
r = d.get("result", d)
if isinstance(r, str):
    r = json.loads(r)
SC = {s["id"]: s for s in r["scores"]}


def rows(arm):
    return [SC[i] for i, m in KEY.items() if i in SC and m["arm"] == arm]


def rate(rs, k):
    return round(sum(1 for s in rs if s[k]) / len(rs), 2) if rs else None


def avg(rs, k):
    return round(sum(s[k] for s in rs) / len(rs), 2) if rs else None


o = []
o.append(f"{'braco':22} {'n':>2} {'RI1_dup':>7} {'RI2_ver':>7} {'genuino':>7} {'aluc':>5} {'crit.bom':>8} {'prior':>5}")
A = {}
for arm in ARMS:
    rs = rows(arm); A[arm] = rs
    o.append(f"{arm:22} {len(rs):>2} {rate(rs,'ri1_dupes'):>7} {rate(rs,'ri2_version'):>7} "
             f"{avg(rs,'genuine_other'):>7} {avg(rs,'hallucinated'):>5} {rate(rs,'false_criticism_good'):>8} {rate(rs,'prioritized_risk'):>5}")
o.append("\nLEGENDA: RI1=duplicatas -DESKTOP/fonte-unica (problema real central); RI2=versao inconsistente;")
o.append("  genuino=outros problemas reais (media); aluc=problemas FALSOS inventados (media); crit.bom=criticou DIARIO/CHANGELOG bons.")
o.append("\nLEITURA: o metodo (AN/prosa) faz achar RI1 mais que o baseline? gera mais ou menos alucinacao?")
print("\n".join(o))
open(r"C:\Users\leona\AppData\Local\Temp\agg_r8.txt", "w", encoding="utf-8").write("\n".join(o))
