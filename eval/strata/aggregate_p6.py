#!/usr/bin/env python3
"""P6 Fase A — shootout de FORMAS: matriz (forma × modelo) de QUALIDADE (genuino - falso-pos)
por projeto, contra os gabaritos corrigidos. Identifica a forma vencedora por modelo.
Uso: python aggregate_p6.py <score_p6.output>"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
FORMS = {"f0": "F0-bare", "f1": "F1-check", "f2": "F2-ANv3", "f4": "F4-etapas"}
d = json.load(open(sys.argv[1], encoding="utf-8"))
r = d.get("result", d)
if isinstance(r, str):
    r = json.loads(r)


def shortmodel(m):
    return m.split("/")[-1].replace("-instruct", "").replace("deepseek-", "").replace("-chat-v3-0324", "-v3")[:14]


def form_of(arm):
    m = re.search(r"p6(f[0-4])-", arm)
    return FORMS.get(m.group(1)) if m else arm


out = []
overall = {f: [] for f in FORMS.values()}
for proj, keyf in [("nnn", "p6-nnn-key.json"), ("pdf2md", "p6-pdf2md-key.json")]:
    key = json.load(open(os.path.join(PLANOS, keyf), encoding="utf-8"))
    sc = {s["id"]: s for s in r[proj]}
    models = sorted({shortmodel(m["model"]) for m in key.values()})
    out.append(f"\n=== {proj.upper()} — QUALIDADE (genuino - falso-pos) por forma × modelo ===")
    out.append(f"{'forma':10}" + "".join(f"{m:>14}" for m in models) + f"{'MEDIA':>8}")
    for fkey, fname in FORMS.items():
        row = []
        allq = []
        for mod in models:
            rs = [sc[i] for i, k in key.items()
                  if i in sc and form_of(k["arm"]) == fname and shortmodel(k["model"]) == mod]
            if rs:
                q = sum(s["genuine_real"] - s["false_positives"] for s in rs) / len(rs)
                row.append(f"{q:>14.2f}")
                allq.append(q)
                overall[fname].append(q)
            else:
                row.append(f"{'-':>14}")
        avg = sum(allq) / len(allq) if allq else 0
        out.append(f"{fname:10}" + "".join(row) + f"{avg:>8.2f}")
    # vencedora por modelo
    out.append("  vencedora/modelo:")
    for mod in models:
        best, bestq = None, -99
        for fname in FORMS.values():
            rs = [sc[i] for i, k in key.items()
                  if i in sc and form_of(k["arm"]) == fname and shortmodel(k["model"]) == mod]
            if rs:
                q = sum(s["genuine_real"] - s["false_positives"] for s in rs) / len(rs)
                if q > bestq:
                    best, bestq = fname, q
        out.append(f"    {mod:16} -> {best} ({bestq:+.2f})")

out.append("\n=== RANKING GERAL das formas (media de qualidade nos 2 projetos, modelos baratos) ===")
for f, qs in sorted(overall.items(), key=lambda kv: -(sum(kv[1]) / len(kv[1]) if kv[1] else -99)):
    if qs:
        out.append(f"  {f:10} {sum(qs)/len(qs):+.2f}  (n={len(qs)})")
out.append("\nqualidade = genuino(reais achados) - falso-positivo. Maior = melhor. Custo de tutoria: F0<F1<F2<F4.")
txt = "\n".join(out)
print(txt)
open(os.path.join(HERE, "..", "..", "lab", "2026-06-04-strata-hipoteses", "RESULTADOS-p6-shootout.txt"),
     "w", encoding="utf-8").write(txt)
