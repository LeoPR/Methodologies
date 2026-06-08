#!/usr/bin/env python3
"""P4 — Matriz CAPACIDADE POR SECAO x MODELO (sintetico, melhor caso = arm AN, N=3).
Responde: quais §/secoes (L0) os modelos ATENDEM, e qual modelo e' suficiente.
Uso: python aggregate_capability.py <cloud-key.json> <cloud-scores.json> [arm]"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
# P -> secao L0 (legenda)
SEC = {"P1": "§5 fonte-unica", "P2": "§3/§8 datas/historia", "P3": "§2 navegacao",
       "P4": "§3 traco/superficie", "P5": "§4 honestidade", "P6": "§6 sem-fonte",
       "P7": "§6-bis fail-open"}
PROBS = list(SEC)
ARM = sys.argv[3] if len(sys.argv) > 3 else "cloud-an"

KEY = json.load(open(os.path.join(PLANOS, sys.argv[1]), encoding="utf-8"))
d = json.load(open(sys.argv[2], encoding="utf-8"))
r = d.get("result", d)
if isinstance(r, str):
    r = json.loads(r)
SC = {s["id"]: s for s in r["scores"]}
models = sorted({m["model"] for m in KEY.values()})


def found_rate(model, prob):
    rs = [SC[i] for i, m in KEY.items() if i in SC and m["model"] == model and m["arm"] == ARM]
    if not rs:
        return None
    hit = sum(1 for s in rs for x in s["detected"] if x["problem"] == prob and x["found"])
    return hit / len(rs)


def cell(v):
    if v is None:
        return "  - "
    return f" {int(round(v*100)):>3}"  # %


o = []
o.append(f"# Capacidade por SECAO x MODELO — arm '{ARM}' (sintetico, % de runs que ACHARAM, N=3)\n")
short = [m.split("/")[-1].replace("-instruct", "")[:14] for m in models]
o.append("secao\\modelo".ljust(24) + "".join(f"{s:>15}" for s in short) + "   MEDIA")
for p in PROBS:
    rates = [found_rate(m, p) for m in models]
    valid = [x for x in rates if x is not None]
    avg = sum(valid) / len(valid) if valid else 0
    o.append(f"{(p+' '+SEC[p]):24}" + "".join(f"{cell(x):>15}" for x in rates) + f"   {int(round(avg*100)):>3}%")
# suficiencia por modelo: media de det_found
o.append("\n# Suficiencia por MODELO (det_found medio no arm, /7)")
for m, s in zip(models, short):
    rs = [SC[i] for i, k in KEY.items() if i in SC and k["model"] == m and k["arm"] == ARM]
    if rs:
        avg = round(sum(x["detection_found"] for x in rs) / len(rs), 2)
        o.append(f"  {s:16} {avg}/7")
o.append("\nNOTA: so a camada L0 (principios §1..§10) foi exercitada; L1 (padroes) e L2 (ferramentas)")
o.append("NAO foram testadas. E e' o MELHOR caso (sintetico, denso); em projeto REAL todos alucinam (ver R8).")
out = "\n".join(o)
print(out)
open(os.path.join(HERE, "..", "..", "lab", "2026-06-04-strata-hipoteses", "VIZ-capacidade-por-secao.md"), "w", encoding="utf-8").write(
    "---\ntitle: P4 — capacidade por secao x modelo (visualizacao)\ncreated: 2026-06-08\n---\n\n```\n" + out + "\n```\n")
