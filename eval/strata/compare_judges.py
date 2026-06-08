#!/usr/bin/env python3
"""R6: compara juiz Claude (cego) vs 2o juiz nao-Claude (gpt-4.1-mini) nos planos nuvem.
Uso: python compare_judges.py <claude_scores.json> <gpt_judge.json> <cloud-key.json>"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
PROBS = ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]
ARMS = ["cloud-baseline", "cloud-prose", "cloud-an"]


def load(p):
    d = json.load(open(p, encoding="utf-8"))
    r = d.get("result", d)
    if isinstance(r, str):
        r = json.loads(r)
    return {s["id"]: s for s in r["scores"]}


C = load(sys.argv[1])          # juiz Claude
G = load(sys.argv[2])          # juiz gpt-4.1-mini
KEY = json.load(open(sys.argv[3] if len(sys.argv) > 3 else os.path.join(PLANOS, "cloud-key.json"), encoding="utf-8"))
ids = [i for i in KEY if i in C and i in G]


def arm_df(scores, arm):
    rs = [scores[i] for i in ids if KEY[i]["arm"] == arm]
    return round(sum(s["detection_found"] for s in rs) / len(rs), 2) if rs else None


o = []
o.append(f"Planos com ambos os juizes: {len(ids)}/{len(KEY)}")
o.append("\n=== det_found medio por braco, por JUIZ ===")
o.append(f"{'braco':16} {'Claude':>7} {'gpt-4.1-mini':>13} {'dif':>6}")
for arm in ARMS:
    c, g = arm_df(C, arm), arm_df(G, arm)
    o.append(f"{arm:16} {c:>7} {g:>13} {round(c-g,2):>6}")

# concordancia
diffs = [C[i]["detection_found"] - G[i]["detection_found"] for i in ids]
mae = round(sum(abs(x) for x in diffs) / len(diffs), 2)
bias = round(sum(diffs) / len(diffs), 2)
# concordancia por problema (found): % de planos em que os dois juizes concordam no found
pa = {}
for p in PROBS:
    agree = 0
    for i in ids:
        cf = next((x["found"] for x in C[i]["detected"] if x["problem"] == p), False)
        gf = next((x["found"] for x in G[i]["detected"] if x["problem"] == p), False)
        if cf == gf:
            agree += 1
    pa[p] = round(agree / len(ids), 2)
o.append(f"\n=== CONCORDANCIA ===")
o.append(f"MAE(det_found) Claude vs gpt = {mae}  | vies medio (Claude - gpt) = {bias}")
o.append("concordancia 'found' por problema (1.0 = sempre concordam):")
o.append("  " + " ".join(f"{p}={pa[p]}" for p in PROBS))

# teste de vies: Claude favorece modelos Claude?
def fam_bias(is_claude):
    sub = [C[i]["detection_found"] - G[i]["detection_found"] for i in ids if ("claude" in KEY[i]["model"]) == is_claude]
    return round(sum(sub) / len(sub), 2) if sub else None
o.append(f"\n=== VIES DE FAMILIA (Claude - gpt, por tipo de modelo avaliado) ===")
o.append(f"  modelos CLAUDE (haiku):   {fam_bias(True)}")
o.append(f"  modelos NAO-Claude:       {fam_bias(False)}")
o.append("  (se o de Claude for >> o de nao-Claude, ha indicio de Claude-favorece-Claude)")
print("\n".join(o))
open(r"C:\Users\leona\AppData\Local\Temp\judges.txt", "w", encoding="utf-8").write("\n".join(o))
