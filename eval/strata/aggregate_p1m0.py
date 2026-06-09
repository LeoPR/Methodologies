#!/usr/bin/env python3
"""F1/M0 — agrega abstencao: forma M0 (abstencao-primeiro) vs AUDIT (controle), por projeto.
Pergunta: o M0-framing reduz super-aplicacao no NNN exemplar (veredito JA-BOM, menos acoes/FP)?
Uso: python aggregate_p1m0.py <score_p1m0.output>"""
import json
import os
import sys
from collections import defaultdict, Counter

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
d = json.load(open(sys.argv[1], encoding="utf-8"))
r = d.get("result", d)
if isinstance(r, str):
    r = json.loads(r)
# veredito correto por projeto
CORRECT = {"nnn": "JA-BOM", "pdf2md": "PRECISA-PONTOS", "fg2p": "PRECISA"}  # pdf2md/fg2p: PRECISA-* conta


def form_of(arm):
    return "M0" if "p1m0" in arm else "AUDIT"


def shortm(m):
    return m.split("/")[-1].replace("-instruct", "")[:14]


out = []
for proj in ["nnn", "pdf2md", "fg2p"]:
    key = json.load(open(os.path.join(PLANOS, f"p1-{proj}-key.json"), encoding="utf-8"))
    sc = {s["id"]: s for s in r[proj]}
    out.append(f"\n=== {proj.upper()} (veredito-verdade: {CORRECT[proj]}) ===")
    out.append(f"{'forma':7} {'n':>2} {'FALSO-POS':>9} {'#acoes':>7} {'genuino':>8} {'rec.bom':>8} {'verdito-ok':>10}  veredictos")
    for form in ["M0", "AUDIT"]:
        rows = [sc[i] for i, m in key.items() if i in sc and form_of(m["arm"]) == form]
        n = len(rows)
        if not n:
            continue
        fp = sum(x["false_positives"] for x in rows) / n
        ac = sum(x["action_count"] for x in rows) / n
        ge = sum(x["genuine_real"] for x in rows) / n
        rg = sum(1 for x in rows if x["recognized_good"]) / n
        # veredito correto: nnn=JA-BOM; pdf2md/fg2p=qualquer PRECISA-*
        if proj == "nnn":
            vok = sum(1 for x in rows if x["verdict"] == "JA-BOM") / n
        else:
            vok = sum(1 for x in rows if x["verdict"].startswith("PRECISA")) / n
        vd = dict(Counter(x["verdict"] for x in rows))
        out.append(f"{form:7} {n:>2} {fp:>9.2f} {ac:>7.2f} {ge:>8.2f} {rg:>8.2f} {vok:>10.2f}  {vd}")
    # por modelo no NNN (o controle de abstencao): M0 vs AUDIT em FP
    if proj == "nnn":
        out.append("  -- NNN por modelo (FALSO-POS M0 vs AUDIT; #acoes) --")
        bym = defaultdict(dict)
        for i, m in key.items():
            if i in sc:
                bym[shortm(m["model"])].setdefault(form_of(m["arm"]), []).append(sc[i])
        for mod in sorted(bym):
            cells = []
            for form in ["M0", "AUDIT"]:
                rs = bym[mod].get(form, [])
                if rs:
                    fp = sum(x["false_positives"] for x in rs) / len(rs)
                    ac = sum(x["action_count"] for x in rs) / len(rs)
                    cells.append(f"{form}: FP={fp:.1f} ac={ac:.1f}")
            out.append(f"    {mod:16} " + "  |  ".join(cells))

out.append("\nLEITURA: no NNN (exemplar), M0 deve dar veredito JA-BOM + menos #acoes + menos FALSO-POS que AUDIT.")
out.append("Se sim -> foregrounding da abstencao conserta a raiz do falso-positivo. Ver tambem sub-deteccao (genuino) em pdf2md/fg2p.")
txt = "\n".join(out)
print(txt)
open(os.path.join(HERE, "..", "..", "lab", "2026-06-04-strata-hipoteses", "RESULTADOS-f1-m0-abstencao.txt"),
     "w", encoding="utf-8").write(txt)
