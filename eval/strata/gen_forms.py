#!/usr/bin/env python3
"""P6 — grafico do VETOR ORIENTACAO: qualidade vs FORMA (F0..F4) por modelo. Mostra quanto a
tutoria compra e onde cada modelo cruza 0. SVG puro.
Uso: python gen_forms.py <faseA.output> <f15.output>"""
import json
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
LAB = os.path.join(HERE, "..", "..", "lab", "2026-06-04-strata-hipoteses")
A = json.load(open(sys.argv[1], encoding="utf-8")); A = A.get("result", A)
F = json.load(open(sys.argv[2], encoding="utf-8")); F = F.get("result", F)
ORDER = ["F0", "F1", "F1.5", "F2", "F4"]
LABEL = {"F0": "F0 cru", "F1": "F1 check", "F1.5": "F1.5 check+", "F2": "F2 AN-v3", "F4": "F4 etapas"}
ARM2FORM = {"p6f0": "F0", "p6f1": "F1", "p6f2": "F2", "p6f4": "F4"}
COL = {"openai/gpt-4.1-mini": "#10a37f", "google/gemini-2.5-flash": "#4285f4",
       "deepseek/deepseek-chat-v3-0324": "#7b3fe4"}


def add(dst, scores, keyf, formmap=None, fixed=None):
    key = json.load(open(os.path.join(PLANOS, keyf), encoding="utf-8"))
    sc = {s["id"]: s for s in scores}
    for i, k in key.items():
        if i not in sc:
            continue
        model = k["model"].replace("_", "/", 1)
        if fixed:
            form = fixed
        else:
            arm = k["arm"].rsplit("-", 1)[0]  # p6f0-nnn -> p6f0
            form = formmap.get(arm)
        if form:
            dst[(form, model)].append(sc[i]["genuine_real"] - sc[i]["false_positives"])


q = defaultdict(list)
add(q, A["nnn"], "p6-nnn-key.json", ARM2FORM)
add(q, A["pdf2md"], "p6-pdf2md-key.json", ARM2FORM)
add(q, F["nnn"], "p6c-f15-nnn-key.json", fixed="F1.5")
add(q, F["pdf2md"], "p6c-f15-pdf2md-key.json", fixed="F1.5")
qm = {k: sum(v) / len(v) for k, v in q.items()}
models = [m for m in COL if any((f, m) in qm for f in ORDER)]

W, H, ML, MR, MT, MB = 820, 540, 70, 200, 64, 60
PW, PH = W - ML - MR, H - MT - MB
allv = list(qm.values())
ymin, ymax = min(allv) - 0.6, max(allv) + 0.6
def fx(i): return ML + i / (len(ORDER) - 1) * PW
def fy(v): return MT + (ymax - v) / (ymax - ymin) * PH
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="sans-serif">',
       f'<rect width="{W}" height="{H}" fill="white"/>']
svg.append(f'<text x="{ML}" y="30" font-size="18" font-weight="bold">P6 — Vetor ORIENTAÇÃO: qualidade × forma (tutoria crescente →)</text>')
svg.append(f'<text x="{ML}" y="48" font-size="12" fill="#666">Y = genuíno − falso-positivo (média 2 projetos) · cada linha = um modelo barato · mais à direita = mais tutoria</text>')
svg.append(f'<line x1="{ML}" y1="{fy(0)}" x2="{ML+PW}" y2="{fy(0)}" stroke="#999" stroke-dasharray="5,4"/>')
svg.append(f'<text x="{ML+PW}" y="{fy(0)-5}" font-size="11" fill="#999" text-anchor="end">0 (ruído=sinal)</text>')
svg.append(f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{MT+PH}" stroke="#333"/><line x1="{ML}" y1="{MT+PH}" x2="{ML+PW}" y2="{MT+PH}" stroke="#333"/>')
yy = int(__import__("math").floor(ymin))
while yy <= ymax:
    y = fy(yy); svg.append(f'<text x="{ML-10}" y="{y+4}" font-size="11" text-anchor="end" fill="#555">{yy:+d}</text>'); yy += 1
for i, f in enumerate(ORDER):
    x = fx(i)
    svg.append(f'<line x1="{x}" y1="{MT}" x2="{x}" y2="{MT+PH}" stroke="#eee"/>')
    svg.append(f'<text x="{x}" y="{MT+PH+20}" font-size="11" text-anchor="middle" fill="#333">{LABEL[f]}</text>')
for m in models:
    color = COL[m]
    pts = [(i, qm[(f, m)]) for i, f in enumerate(ORDER) if (f, m) in qm]
    path = " ".join(f"{'M' if j == 0 else 'L'}{fx(i):.0f},{fy(v):.0f}" for j, (i, v) in enumerate(pts))
    svg.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="2.5"/>')
    for i, v in pts:
        svg.append(f'<circle cx="{fx(i)}" cy="{fy(v)}" r="5" fill="{color}" stroke="#fff"/>')
    lx, lv = pts[-1]
    svg.append(f'<text x="{fx(lx)+10}" y="{fy(lv)+4}" font-size="11" fill="{color}">{m.split("/")[-1].replace("-0324","")[:16]}</text>')
svg.append('</svg>')
open(os.path.join(LAB, "VIZ-p6-forms.svg"), "w", encoding="utf-8").write("\n".join(svg))
print("-> VIZ-p6-forms.svg")
print(f"{'modelo':24}" + "".join(f"{f:>9}" for f in ORDER))
for m in models:
    print(f"{m.split('/')[-1][:22]:24}" + "".join((f"{qm[(f,m)]:>9.2f}" if (f, m) in qm else f"{'-':>9}") for f in ORDER))
