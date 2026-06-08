#!/usr/bin/env python3
"""P1+P2 — agrega AN-v2 (real-*-an) vs AN-v3 (anv3-*) por projeto, contra gabarito corrigido.
Uso: python aggregate_p1p2.py <score_cmp.output>"""
import json
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
d = json.load(open(sys.argv[1], encoding="utf-8"))
r = d.get("result", d)
if isinstance(r, str):
    r = json.loads(r)

PROJ = {"nnn": ("nnn-cmp-key.json", "real-nnn-an", "anv3-nnn"),
        "pdf2md": ("pdf2md-cmp-key.json", "real-pdf2md-an", "anv3-pdf2md")}
out = []


def shortmodel(m):
    return m.split("/")[-1].replace("-instruct", "").replace("deepseek-", "")[:16]


for proj, (keyf, arm_v2, arm_v3) in PROJ.items():
    key = json.load(open(os.path.join(PLANOS, keyf), encoding="utf-8"))
    sc = {s["id"]: s for s in r[proj]}
    out.append(f"\n=== {proj.upper()} — AN-v2 (R8) vs AN-v3 (P1+P2) — gabarito corrigido ===")
    out.append(f"{'forma':10} {'n':>2} {'FALSO-POS':>9} {'genuino':>8} {'reconh.bom':>10} {'flag_extra':>10}")
    agg = {}
    for label, arm in [("AN-v2", arm_v2), ("AN-v3", arm_v3)]:
        rs = [sc[i] for i, m in key.items() if i in sc and m["arm"] == arm]
        n = len(rs)
        fp = sum(s["false_positives"] for s in rs) / n
        ge = sum(s["genuine_real"] for s in rs) / n
        rg = sum(1 for s in rs if s["recognized_good"]) / n
        fx = sum(1 for s in rs if s["flag_extra"]) / n
        agg[label] = (fp, ge, rg, fx)
        out.append(f"{label:10} {n:>2} {fp:>9.2f} {ge:>8.2f} {rg:>10.2f} {fx:>10.2f}")
    (fp2, ge2, rg2, fx2) = agg["AN-v2"]
    (fp3, ge3, rg3, fx3) = agg["AN-v3"]
    out.append(f"{'Δ(v3-v2)':10} {'':>2} {fp3-fp2:>+9.2f} {ge3-ge2:>+8.2f} {rg3-rg2:>+10.2f} {fx3-fx2:>+10.2f}")
    # por modelo (so falso-pos e genuino)
    out.append(f"  -- por modelo (FP / genuino) --")
    bymodel = defaultdict(dict)
    for i, m in key.items():
        if i not in sc:
            continue
        lab = "v2" if m["arm"] == arm_v2 else "v3"
        bymodel[shortmodel(m["model"])].setdefault(lab, []).append(sc[i])
    for mod in sorted(bymodel):
        cell = []
        for lab in ["v2", "v3"]:
            rs = bymodel[mod].get(lab, [])
            if rs:
                fp = sum(s["false_positives"] for s in rs) / len(rs)
                ge = sum(s["genuine_real"] for s in rs) / len(rs)
                cell.append(f"{lab}: FP={fp:.1f} gen={ge:.1f}")
        out.append(f"    {mod:16} " + "  |  ".join(cell))

out.append("\nLEITURA: AN-v3 (anti-FP + etapas) baixa o FALSO-POSITIVO e sobe reconh.bom?")
out.append("Custo: pode baixar 'genuino' (modelo medio passa a dizer 'tudo ok' e perde os reais sutis)?")
txt = "\n".join(out)
print(txt)
open(os.path.join(HERE, "..", "..", "lab", "2026-06-04-strata-hipoteses", "RESULTADOS-p1p2-anv3.txt"),
     "w", encoding="utf-8").write(txt)
