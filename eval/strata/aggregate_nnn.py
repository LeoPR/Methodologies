#!/usr/bin/env python3
"""Agrega o R8-NNN (projeto exemplar) por braco — foco falso-positivo.
Uso: python aggregate_nnn.py <nnn-key.json> <scores.json>"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
ARMS = ["real-nnn-baseline", "real-nnn-prose", "real-nnn-an"]
KEY = json.load(open(os.path.join(PLANOS, sys.argv[1]), encoding="utf-8"))
d = json.load(open(sys.argv[2], encoding="utf-8"))
r = d.get("result", d)
if isinstance(r, str):
    r = json.loads(r)
SC = {s["id"]: s for s in r["scores"]}


def rows(arm):
    return [SC[i] for i, m in KEY.items() if i in SC and m["arm"] == arm]


o = []
o.append(f"{'braco':20} {'n':>2} {'reconh.bom':>10} {'FALSO-POS':>9} {'flag-IA-dup':>11} {'genuino':>7}")
for arm in ARMS:
    rs = rows(arm); n = len(rs)
    rg = round(sum(1 for s in rs if s["recognized_good"]) / n, 2)
    fp = round(sum(s["false_positives"] for s in rs) / n, 2)
    fa = round(sum(1 for s in rs if s["flagged_ai_files_as_dup"]) / n, 2)
    gm = round(sum(s["genuine_micro"] for s in rs) / n, 2)
    o.append(f"{arm:20} {n:>2} {rg:>10} {fp:>9} {fa:>11} {gm:>7}")
o.append("\nreconh.bom=fracao que reconheceu o projeto como bem-organizado; FALSO-POS=violacoes inventadas (media);")
o.append("flag-IA-dup=fracao que flagou erroneamente os 3 arq-IA como §5; genuino=problemas reais triviais (media).")
o.append("LEITURA: o metodo (AN/prosa) gera mais FALSO-POSITIVO que o baseline num projeto exemplar?")
print("\n".join(o))
open(r"C:\Users\leona\AppData\Local\Temp\agg_nnn.txt", "w", encoding="utf-8").write("\n".join(o))
