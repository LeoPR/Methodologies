#!/usr/bin/env python3
"""P6 — gera CANDLESTICK (faixa de variacao por modelo) + BUBBLE (custo×qualidade×inconsistencia)
a partir do grid Fase B (F1, 12 modelos × 2 projetos × N=2). SVG puro, sem deps.
Uso: python gen_charts.py <score_p6b.output>"""
import json
import math
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
LAB = os.path.join(HERE, "..", "..", "lab", "2026-06-04-strata-hipoteses")
PRICING = json.load(open(os.path.join(PLANOS, "p6-pricing.json"), encoding="utf-8"))
d = json.load(open(sys.argv[1], encoding="utf-8"))
r = d.get("result", d)
if isinstance(r, str):
    r = json.loads(r)
REASONERS = {"deepseek/deepseek-r1", "openai/o4-mini"}
CEILING = {"anthropic/claude-opus-4.8"}
OPCOLOR = {"openai": "#10a37f", "google": "#4285f4", "deepseek": "#7b3fe4",
           "meta-llama": "#f59e0b", "qwen": "#dc2626", "mistralai": "#e11d48", "anthropic": "#111111"}


def cost(m):
    p = PRICING.get(m)
    return p["in"] * 0.9 + p["out"] * 0.1 if p else None


def op(m):
    return m.split("/")[0]


def short(m):
    return m.split("/")[-1].replace("-instruct", "").replace("-0324", "")


# por modelo: lista de qualidade por celula + separado por projeto
cells = defaultdict(list)
byproj = defaultdict(lambda: defaultdict(list))
for proj, keyf in [("nnn", "p6b-f1-nnn-key.json"), ("pdf2md", "p6b-f1-pdf2md-key.json")]:
    key = json.load(open(os.path.join(PLANOS, keyf), encoding="utf-8"))
    sc = {s["id"]: s for s in r[proj]}
    for i, k in key.items():
        if i in sc:
            m = k["model"].replace("_", "/", 1)
            q = sc[i]["genuine_real"] - sc[i]["false_positives"]
            cells[m].append(q)
            byproj[m][proj].append(q)

rows = []
for m, vs in cells.items():
    c = cost(m)
    if c is None:
        continue
    rows.append({"m": m, "vals": vs, "mean": sum(vs) / len(vs), "lo": min(vs), "hi": max(vs),
                 "cost": c, "nnn": sum(byproj[m]["nnn"]) / max(1, len(byproj[m]["nnn"])),
                 "pdf": sum(byproj[m]["pdf2md"]) / max(1, len(byproj[m]["pdf2md"]))})
rows.sort(key=lambda x: x["cost"])

LXMIN = math.log10(min(x["cost"] for x in rows) * 0.8)
LXMAX = math.log10(max(x["cost"] for x in rows) * 1.2)
QLO = min(x["lo"] for x in rows) - 0.6
QHI = max(x["hi"] for x in rows) + 0.6


def svg_open(w, h):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" font-family="sans-serif">',
            f'<rect width="{w}" height="{h}" fill="white"/>']


def marker(svg, x, y, m, color, rr=6.5):
    if m in CEILING:
        svg.append(f'<polygon points="{x},{y-9} {x+2.6},{y-2.8} {x+8.6},{y-2.8} {x+3.8},{y+1.6} {x+5.6},{y+7.6} {x},{y+3.8} {x-5.6},{y+7.6} {x-3.8},{y+1.6} {x-8.6},{y-2.8} {x-2.6},{y-2.8}" fill="{color}" stroke="#000"/>')
    elif m in REASONERS:
        svg.append(f'<polygon points="{x},{y-8} {x+8},{y+7} {x-8},{y+7}" fill="{color}" stroke="#333"/>')
    else:
        svg.append(f'<circle cx="{x}" cy="{y}" r="{rr}" fill="{color}" stroke="#333"/>')


# ================= CANDLESTICK =================
W, H, ML, MR, MT, MB = 980, 620, 80, 220, 64, 70
PW, PH = W - ML - MR, H - MT - MB
def px(c): return ML + (math.log10(c) - LXMIN) / (LXMAX - LXMIN) * PW
def py(q): return MT + (QHI - q) / (QHI - QLO) * PH
svg = svg_open(W, H)
svg.append(f'<text x="{ML}" y="30" font-size="18" font-weight="bold">P6 — Qualidade do Strata por modelo: FAIXA de variação (candlestick)</text>')
svg.append(f'<text x="{ML}" y="48" font-size="12" fill="#666">barra = min..max nas 4 células (2 projetos × 2 runs) · ▬ = média · azul=projeto messy(pdf2md) vermelho=exemplar(NNN) · △reasoner ☆Opus</text>')
svg.append(f'<line x1="{ML}" y1="{py(0)}" x2="{ML+PW}" y2="{py(0)}" stroke="#999" stroke-dasharray="5,4"/>')
svg.append(f'<text x="{ML+PW}" y="{py(0)-5}" font-size="11" fill="#999" text-anchor="end">qualidade 0 (ruído=sinal)</text>')
svg.append(f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{MT+PH}" stroke="#333"/><line x1="{ML}" y1="{MT+PH}" x2="{ML+PW}" y2="{MT+PH}" stroke="#333"/>')
for dec in [0.01, 0.1, 1, 10]:
    lx = math.log10(dec)
    if LXMIN <= lx <= LXMAX:
        x = px(dec); svg.append(f'<line x1="{x}" y1="{MT}" x2="{x}" y2="{MT+PH}" stroke="#eee"/><text x="{x}" y="{MT+PH+18}" font-size="11" text-anchor="middle" fill="#555">${dec}</text>')
svg.append(f'<text x="{ML+PW/2}" y="{H-18}" font-size="13" text-anchor="middle">custo (proxy $/M, log) →</text>')
qy = int(math.floor(QLO))
while qy <= math.ceil(QHI):
    y = py(qy); svg.append(f'<text x="{ML-10}" y="{y+4}" font-size="11" text-anchor="end" fill="#555">{qy:+d}</text>'); qy += 1
for x in rows:
    cx = px(x["cost"])
    svg.append(f'<line x1="{cx}" y1="{py(x["lo"])}" x2="{cx}" y2="{py(x["hi"])}" stroke="#bbb" stroke-width="7" stroke-linecap="round"/>')
    # marcadores por projeto (mostra a bimodalidade)
    svg.append(f'<circle cx="{cx}" cy="{py(x["nnn"])}" r="3.6" fill="#dc2626"/>')
    svg.append(f'<circle cx="{cx}" cy="{py(x["pdf"])}" r="3.6" fill="#2563eb"/>')
    svg.append(f'<line x1="{cx-7}" y1="{py(x["mean"])}" x2="{cx+7}" y2="{py(x["mean"])}" stroke="{OPCOLOR.get(op(x["m"]),"#000")}" stroke-width="2.5"/>')
    svg.append(f'<text x="{cx+10}" y="{py(x["mean"])+4}" font-size="10" fill="#222">{short(x["m"])}</text>')
svg.append('</svg>')
open(os.path.join(LAB, "VIZ-p6-candle.svg"), "w", encoding="utf-8").write("\n".join(svg))

# ================= BUBBLE =================
W2, H2 = 980, 620
svg = svg_open(W2, H2)
def px2(c): return ML + (math.log10(c) - LXMIN) / (LXMAX - LXMIN) * PW
QLO2 = min(x["mean"] for x in rows) - 0.6
QHI2 = max(x["mean"] for x in rows) + 0.6
def py2(q): return MT + (QHI2 - q) / (QHI2 - QLO2) * PH
svg.append(f'<text x="{ML}" y="30" font-size="18" font-weight="bold">P6 — Bubble: custo × qualidade × INCONSISTÊNCIA × operadora</text>')
svg.append(f'<text x="{ML}" y="48" font-size="12" fill="#666">X=custo(log) · Y=qualidade média · tamanho da bolha = amplitude(max−min) = inconsistência/risco · cor=operadora · △reasoner ☆Opus</text>')
svg.append(f'<line x1="{ML}" y1="{py2(0)}" x2="{ML+PW}" y2="{py2(0)}" stroke="#999" stroke-dasharray="5,4"/>')
svg.append(f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{MT+PH}" stroke="#333"/><line x1="{ML}" y1="{MT+PH}" x2="{ML+PW}" y2="{MT+PH}" stroke="#333"/>')
for dec in [0.01, 0.1, 1, 10]:
    lx = math.log10(dec)
    if LXMIN <= lx <= LXMAX:
        x = px2(dec); svg.append(f'<line x1="{x}" y1="{MT}" x2="{x}" y2="{MT+PH}" stroke="#eee"/><text x="{x}" y="{MT+PH+18}" font-size="11" text-anchor="middle" fill="#555">${dec}</text>')
svg.append(f'<text x="{ML+PW/2}" y="{H2-18}" font-size="13" text-anchor="middle">custo (proxy $/M, log) →</text>')
qy = int(math.floor(QLO2))
while qy <= math.ceil(QHI2):
    y = py2(qy); svg.append(f'<text x="{ML-10}" y="{y+4}" font-size="11" text-anchor="end" fill="#555">{qy:+d}</text>'); qy += 1
for x in rows:
    cx, cy = px2(x["cost"]), py2(x["mean"])
    spread = x["hi"] - x["lo"]
    rr = 6 + spread * 3.2
    color = OPCOLOR.get(op(x["m"]), "#888")
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="{color}" fill-opacity="0.32" stroke="{color}" stroke-width="1.5"/>')
    if x["m"] in REASONERS:
        svg.append(f'<polygon points="{cx},{cy-5} {cx+5},{cy+4} {cx-5},{cy+4}" fill="{color}"/>')
    elif x["m"] in CEILING:
        svg.append(f'<text x="{cx}" y="{cy+4}" font-size="13" text-anchor="middle">★</text>')
    svg.append(f'<text x="{cx}" y="{cy-rr-3}" font-size="9.5" text-anchor="middle" fill="#222">{short(x["m"])}</text>')
# legenda tamanho
svg.append(f'<text x="{ML+PW+24}" y="{MT+10}" font-size="12" font-weight="bold">bolha = inconsistência</text>')
for i, s in enumerate([1, 3, 6]):
    yy = MT + 50 + i * 60; rr = 6 + s * 3.2
    svg.append(f'<circle cx="{ML+PW+50}" cy="{yy}" r="{rr}" fill="#888" fill-opacity="0.3" stroke="#888"/><text x="{ML+PW+95}" y="{yy+4}" font-size="11">amplitude {s}</text>')
svg.append('</svg>')
open(os.path.join(LAB, "VIZ-p6-bubble.svg"), "w", encoding="utf-8").write("\n".join(svg))

print("-> VIZ-p6-candle.svg + VIZ-p6-bubble.svg")
print(f"{'modelo':26}{'media':>7}{'min':>6}{'max':>6}{'NNN':>7}{'pdf2md':>8}{'amplit':>8}")
for x in sorted(rows, key=lambda x: -x["mean"]):
    print(f"{short(x['m']):26}{x['mean']:>7.2f}{x['lo']:>6.1f}{x['hi']:>6.1f}{x['nnn']:>7.1f}{x['pdf']:>8.1f}{x['hi']-x['lo']:>8.1f}")
