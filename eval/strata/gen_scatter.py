#!/usr/bin/env python3
"""P6 Fase B — SCATTERPLOT (SVG puro, sem deps): custo × qualidade por modelo, forma F1.
X = custo (proxy $/M, log) ; Y = qualidade (genuino - falso-pos) ; cor = operadora ;
forma do marcador = reasoner(triangulo)/normal(circulo)/teto-Opus(estrela).
Uso: python gen_scatter.py <score_p6b.output>"""
import json
import math
import os
import re
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
PRICING = json.load(open(os.path.join(PLANOS, "p6-pricing.json"), encoding="utf-8"))
d = json.load(open(sys.argv[1], encoding="utf-8"))
r = d.get("result", d)
if isinstance(r, str):
    r = json.loads(r)

REASONERS = {"deepseek/deepseek-r1", "openai/o4-mini"}
CEILING = {"anthropic/claude-opus-4.8"}
OPCOLOR = {"openai": "#10a37f", "google": "#4285f4", "deepseek": "#7b3fe4",
           "meta-llama": "#f59e0b", "qwen": "#dc2626", "mistralai": "#e11d48",
           "anthropic": "#111111"}


def cost_proxy(model):
    p = PRICING.get(model)
    if not p:
        return None
    return p["in"] * 0.9 + p["out"] * 0.1  # prompt domina (~18k in : ~2k out)


# qualidade media por modelo (F1, 2 projetos, N runs)
qual = defaultdict(list)
for proj, keyf in [("nnn", "p6b-f1-nnn-key.json"), ("pdf2md", "p6b-f1-pdf2md-key.json")]:
    key = json.load(open(os.path.join(PLANOS, keyf), encoding="utf-8"))
    sc = {s["id"]: s for s in r[proj]}
    for i, k in key.items():
        if i in sc:
            model = k["model"].replace("_", "/", 1)  # blind grava org_modelo; pricing usa org/modelo
            qual[model].append(sc[i]["genuine_real"] - sc[i]["false_positives"])

pts = []
for model, qs in qual.items():
    c = cost_proxy(model)
    if c is None or not qs:
        continue
    pts.append({"model": model, "q": sum(qs) / len(qs), "cost": c, "n": len(qs)})
pts.sort(key=lambda p: p["cost"])

# F4 overlay (etapas): qualidade no subconjunto, p/ desenhar a "seta do ganho do guiado"
f4qual = defaultdict(list)
for keyf, group in [("p6b-f4-nnn-key.json", "f4_nnn"), ("p6b-f4-pdf2md-key.json", "f4_pdf")]:
    kp = os.path.join(PLANOS, keyf)
    if not os.path.exists(kp) or group not in r:
        continue
    key = json.load(open(kp, encoding="utf-8"))
    sc = {s["id"]: s for s in r[group]}
    for i, k in key.items():
        if i in sc:
            f4qual[k["model"].replace("_", "/", 1)].append(sc[i]["genuine_real"] - sc[i]["false_positives"])
f4 = {m: sum(v) / len(v) for m, v in f4qual.items() if v}

# --- escala ---
W, H = 960, 620
ML, MR, MT, MB = 80, 230, 60, 70
PW, PH = W - ML - MR, H - MT - MB
costs = [p["cost"] for p in pts]
allq = [p["q"] for p in pts] + list(f4.values())
qmin = min(allq) - 0.5
qmax = max(allq) + 0.5
lxmin, lxmax = math.log10(min(costs) * 0.8), math.log10(max(costs) * 1.2)


def px(c):
    return ML + (math.log10(c) - lxmin) / (lxmax - lxmin) * PW


def py(q):
    return MT + (qmax - q) / (qmax - qmin) * PH


def op(model):
    return model.split("/")[0]


def short(model):
    return model.split("/")[-1].replace("-instruct", "").replace("-0324", "")


svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="sans-serif">']
svg.append(f'<rect width="{W}" height="{H}" fill="white"/>')
svg.append(f'<text x="{ML}" y="30" font-size="18" font-weight="bold">P6 — Custo × Qualidade do Strata por modelo (forma F1-checklist, projetos reais)</text>')
svg.append(f'<text x="{ML}" y="48" font-size="12" fill="#666">Y = genuino - falso-positivo (maior=melhor) · X = custo proxy $/M (log) · △=reasoner ☆=teto(Opus)</text>')
# eixos
svg.append(f'<line x1="{ML}" y1="{py(0)}" x2="{ML+PW}" y2="{py(0)}" stroke="#999" stroke-dasharray="5,4"/>')
svg.append(f'<text x="{ML+PW}" y="{py(0)-5}" font-size="11" fill="#999" text-anchor="end">qualidade 0 (ruido=sinal)</text>')
svg.append(f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{MT+PH}" stroke="#333"/>')
svg.append(f'<line x1="{ML}" y1="{MT+PH}" x2="{ML+PW}" y2="{MT+PH}" stroke="#333"/>')
# ticks X (log)
for dec in [0.01, 0.1, 1, 10]:
    lx = math.log10(dec)
    if lxmin <= lx <= lxmax:
        x = px(dec)
        svg.append(f'<line x1="{x}" y1="{MT}" x2="{x}" y2="{MT+PH}" stroke="#eee"/>')
        svg.append(f'<text x="{x}" y="{MT+PH+18}" font-size="11" text-anchor="middle" fill="#555">${dec}</text>')
svg.append(f'<text x="{ML+PW/2}" y="{H-20}" font-size="13" text-anchor="middle">custo (proxy $/M tokens, escala log) →</text>')
# ticks Y
qy = int(math.floor(qmin))
while qy <= math.ceil(qmax):
    y = py(qy)
    svg.append(f'<text x="{ML-10}" y="{y+4}" font-size="11" text-anchor="end" fill="#555">{qy:+d}</text>')
    qy += 1
svg.append(f'<text x="20" y="{MT+PH/2}" font-size="13" text-anchor="middle" transform="rotate(-90 20 {MT+PH/2})">qualidade (genuino - falso-pos) →</text>')
# pontos
for p in pts:
    x, y = px(p["cost"]), py(p["q"])
    color = OPCOLOR.get(op(p["model"]), "#888")
    if p["model"] in CEILING:
        svg.append(f'<polygon points="{x},{y-9} {x+2.6},{y-2.8} {x+8.6},{y-2.8} {x+3.8},{y+1.6} {x+5.6},{y+7.6} {x},{y+3.8} {x-5.6},{y+7.6} {x-3.8},{y+1.6} {x-8.6},{y-2.8} {x-2.6},{y-2.8}" fill="{color}" stroke="#000"/>')
    elif p["model"] in REASONERS:
        svg.append(f'<polygon points="{x},{y-8} {x+8},{y+7} {x-8},{y+7}" fill="{color}" stroke="#333"/>')
    else:
        svg.append(f'<circle cx="{x}" cy="{y}" r="6.5" fill="{color}" stroke="#333"/>')
    svg.append(f'<text x="{x+11}" y="{y+4}" font-size="10.5" fill="#222">{short(p["model"])} ({p["q"]:+.1f})</text>')
# setas do ganho do guiado (F1 -> F4) no subconjunto
svg.append(f'<defs><marker id="ah" markerWidth="7" markerHeight="7" refX="5" refY="2.5" orient="auto"><path d="M0,0 L5,2.5 L0,5 z" fill="#16a34a"/></marker></defs>')
for p in pts:
    if p["model"] in f4:
        x = px(p["cost"])
        y1, y2 = py(p["q"]), py(f4[p["model"]])
        if abs(y2 - y1) > 3:
            svg.append(f'<line x1="{x-13}" y1="{y1}" x2="{x-13}" y2="{y2+ (4 if y2<y1 else -4)}" stroke="#16a34a" stroke-width="2" marker-end="url(#ah)" opacity="0.8"/>')
        svg.append(f'<circle cx="{x-13}" cy="{y2}" r="3.2" fill="none" stroke="#16a34a" stroke-width="1.6"/>')
svg.append(f'<text x="{ML+8}" y="{MT+PH-8}" font-size="10.5" fill="#16a34a">↑ verde = ganho da forma F4-etapas (guiado) sobre a F1-checklist</text>')
# legenda operadoras
ly = MT + 10
svg.append(f'<text x="{ML+PW+24}" y="{ly}" font-size="12" font-weight="bold">operadora</text>')
for i, (k, c) in enumerate(OPCOLOR.items()):
    yy = ly + 20 + i * 20
    svg.append(f'<circle cx="{ML+PW+34}" cy="{yy-4}" r="6" fill="{c}" stroke="#333"/>')
    svg.append(f'<text x="{ML+PW+48}" y="{yy}" font-size="11">{k}</text>')
svg.append('</svg>')
out = os.path.join(HERE, "..", "..", "lab", "2026-06-04-strata-hipoteses", "VIZ-p6-scatter.svg")
open(out, "w", encoding="utf-8").write("\n".join(svg))
print(f"-> {out} ({len(pts)} modelos plotados)")
for p in sorted(pts, key=lambda p: -p["q"]):
    tag = "☆teto" if p["model"] in CEILING else ("△reason" if p["model"] in REASONERS else "")
    print(f"  {short(p['model']):28} q={p['q']:+.2f}  custo≈${p['cost']:.2f}/M  {tag}")
