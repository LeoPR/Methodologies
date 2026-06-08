#!/usr/bin/env python3
"""ENTREGA — funde Phase B (F1, 12 modelos) + #2 (value/free/local) + F4(deepseek-v3) num
dataset por CONFIG (modelo+forma), com AMBIENTE (local/grátis/pago) e custo. Gera:
- VIZ-entrega-fronteira.svg : SO as configs que funcionam (qualidade >= LIMIAR), custo×qualidade
- imprime a tabela de decisão (melhor por ambiente).
Uso: python gen_delivery.py <p6b.output> <p6d.output>"""
import json
import math
import os
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
LAB = os.path.join(HERE, "..", "..", "lab", "2026-06-04-strata-hipoteses")
PRICING = json.load(open(os.path.join(PLANOS, "p6-pricing.json"), encoding="utf-8"))
SAFE2REAL = {k.replace("/", "_").replace(":", "_"): k for k in PRICING}
NEUTRO, BOM = -0.1, 0.5  # limiares: "nao atrapalha" / "ajuda de verdade"

p6b = json.load(open(sys.argv[1], encoding="utf-8")); p6b = p6b.get("result", p6b)
p6d = json.load(open(sys.argv[2], encoding="utf-8")); p6d = p6d.get("result", p6d)


def cost_env(safemodel):
    real = SAFE2REAL.get(safemodel)
    if real is None:
        return 0.0, "local", safemodel  # Ollama local
    p = PRICING[real]
    c = p["in"] * 0.9 + p["out"] * 0.1
    env = "free" if real.endswith(":free") else "paid"
    return c, env, real


SUPERSEDED = {"deepseek-r1_8b", "qwen3_4b-thinking"}  # validados em p6e (N=3), substituem p6d (N=1 truncado)


def collect(scores, keyf, form, skip=None):
    """retorna lista (config_model, form, quality) por celula."""
    key = json.load(open(os.path.join(PLANOS, keyf), encoding="utf-8"))
    sc = {s["id"]: s for s in scores}
    out = []
    for i, k in key.items():
        if i in sc and not (skip and k["model"] in skip):
            out.append((k["model"], form, sc[i]["genuine_real"] - sc[i]["false_positives"]))
    return out


cells = []
# Phase B F1 (12 modelos)
cells += collect(p6b["nnn"], "p6b-f1-nnn-key.json", "F1")
cells += collect(p6b["pdf2md"], "p6b-f1-pdf2md-key.json", "F1")
# Phase B F4 overlay (deepseek-v3 etc.) -> config "etapas"
cells += collect(p6b["f4_nnn"], "p6b-f4-nnn-key.json", "F4")
cells += collect(p6b["f4_pdf"], "p6b-f4-pdf2md-key.json", "F4")
# #2 (value/free/local) F1 — pula os reasoners locais (substituidos pela validacao p6e)
cells += collect(p6d["nnn"], "p6d-nnn-key.json", "F1", skip=SUPERSEDED)
cells += collect(p6d["pdf2md"], "p6d-pdf2md-key.json", "F1", skip=SUPERSEDED)
# validacao N=3 dos reasoners locais (p6e) — numero honesto (concluindo, deepseek-r1:8b alucina)
if len(sys.argv) > 3:
    p6e = json.load(open(sys.argv[3], encoding="utf-8")); p6e = p6e.get("result", p6e)
    cells += collect(p6e["nnn"], "p6e-nnn-key.json", "F1")
    cells += collect(p6e["pdf2md"], "p6e-pdf2md-key.json", "F1")

# agrega por (modelo, forma)
agg = defaultdict(list)
for m, f, q in cells:
    agg[(m, f)].append(q)
configs = []
for (m, f), qs in agg.items():
    cost, env, real = cost_env(m)
    label = real.split("/")[-1].replace("-instruct", "").replace("-0324", "")
    if f == "F4":
        label += " +etapas"
    configs.append({"model": real, "label": label, "form": f, "env": env, "cost": cost,
                    "q": sum(qs) / len(qs), "lo": min(qs), "hi": max(qs), "n": len(qs)})

# ---- tabela de decisao (melhor por ambiente, entre os que funcionam) ----
print(f"{'CONFIG':30}{'amb':>7}{'$/M':>8}{'qual':>7}{'faixa':>12}")
for c in sorted(configs, key=lambda c: -c["q"]):
    mark = "  BOM" if c["q"] >= BOM else ("  ~ok" if c["q"] >= NEUTRO else "")
    print(f"{c['label'][:30]:30}{c['env']:>7}{c['cost']:>8.2f}{c['q']:>7.2f}   [{c['lo']:+.0f},{c['hi']:+.0f}]{mark}")
print("\n-- MELHOR POR AMBIENTE (entre qualidade >= NEUTRO) --")
for env in ["local", "free", "paid"]:
    elig = [c for c in configs if c["env"] == env and c["q"] >= NEUTRO]
    if elig:
        b = max(elig, key=lambda c: c["q"])
        print(f"  {env:6}: {b['label']} (qual {b['q']:+.2f}, ${b['cost']:.2f}/M, forma {b['form']})")
    else:
        nofilter = [c for c in configs if c["env"] == env]
        best = max(nofilter, key=lambda c: c["q"]) if nofilter else None
        print(f"  {env:6}: nenhuma >= limiar (melhor: {best['label']} {best['q']:+.2f})" if best else f"  {env:6}: -")

# ---- grafico FRONTEIRA (positivo-only) — 1 melhor config por modelo, pontos numerados ----
best_by_model = {}
for c in configs:
    if c["q"] >= NEUTRO:
        m = c["model"]
        if m not in best_by_model or c["q"] > best_by_model[m]["q"]:
            best_by_model[m] = c
work = sorted(best_by_model.values(), key=lambda c: (-c["q"], c["cost"]))
for n, c in enumerate(work, 1):
    c["rank"] = n
ENVCOLOR = {"local": "#16a34a", "free": "#2563eb", "paid": "#7b3fe4"}
ENVNAME = {"local": "local/grátis", "free": "grátis remoto", "paid": "API paga"}
W, H, ML, MR, MT, MB = 940, 430, 64, 300, 70, 52
PW, PH = W - ML - MR, H - MT - MB
if work:
    costs = [max(c["cost"], 0.02) for c in work]
    lxmin, lxmax = math.log10(min(costs) / 1.6), math.log10(max(costs) * 1.6)
    qhi = max(c["q"] for c in work) + 0.25
    qlo = min(c["q"] for c in work) - 0.25

    def px(c): return ML + (math.log10(max(c, 0.02)) - lxmin) / (lxmax - lxmin) * PW
    def py(q): return MT + (qhi - q) / (qhi - qlo) * PH
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" font-family="sans-serif">',
           f'<rect width="{W}" height="{H}" fill="white"/>']
    svg.append(f'<text x="{ML}" y="28" font-size="17" font-weight="bold">Strata por IA — o que FUNCIONA: custo × qualidade × ambiente</text>')
    svg.append(f'<text x="{ML}" y="46" font-size="11.5" fill="#666">só configs que ajudam (≥ neutro). Y = problemas reais − falso-positivos · X = custo (log) · cor = ambiente</text>')
    # zona "ajuda de verdade"
    if py(BOM) > MT:
        svg.append(f'<rect x="{ML}" y="{MT}" width="{PW}" height="{py(BOM)-MT:.0f}" fill="#dcfce7" opacity="0.55"/>')
        svg.append(f'<text x="{ML+PW-6}" y="{MT+15}" font-size="10.5" fill="#15803d" text-anchor="end">↑ ajuda de verdade (≥ +0.5)</text>')
    svg.append(f'<line x1="{ML}" y1="{py(0):.0f}" x2="{ML+PW}" y2="{py(0):.0f}" stroke="#9ca3af" stroke-dasharray="5,4"/>')
    svg.append(f'<text x="{ML+4}" y="{py(0)-5:.0f}" font-size="10" fill="#9ca3af">0 = neutro (não ajuda, não atrapalha)</text>')
    svg.append(f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{MT+PH}" stroke="#333"/><line x1="{ML}" y1="{MT+PH}" x2="{ML+PW}" y2="{MT+PH}" stroke="#333"/>')
    for dec in [0, 0.1, 0.3, 1, 3, 7]:
        xv = 0.02 if dec == 0 else dec
        lab = "grátis" if dec == 0 else f"${dec}"
        if lxmin <= math.log10(xv) <= lxmax:
            x = px(xv)
            svg.append(f'<line x1="{x:.0f}" y1="{MT}" x2="{x:.0f}" y2="{MT+PH}" stroke="#f0f0f0"/>')
            svg.append(f'<text x="{x:.0f}" y="{MT+PH+16}" font-size="10.5" text-anchor="middle" fill="#666">{lab}</text>')
    svg.append(f'<text x="{ML+PW/2:.0f}" y="{H-14}" font-size="12" text-anchor="middle" fill="#444">custo por milhão de tokens (escala log) →</text>')
    for q10 in range(math.floor(qlo*2), math.ceil(qhi*2)+1):
        q = q10/2
        if qlo <= q <= qhi:
            svg.append(f'<text x="{ML-8}" y="{py(q)+4:.0f}" font-size="10" text-anchor="end" fill="#666">{q:+.1f}</text>')
    # pontos numerados (com nudge horizontal p/ colisoes) + faixa fina de variacao
    placed = {}
    for c in work:
        x, y = px(c["cost"]), py(c["q"])
        cell = (round(x / 18), round(y / 18))
        k = placed.get(cell, 0); placed[cell] = k + 1
        x += k * 20  # afasta pontos coincidentes
        col = ENVCOLOR[c["env"]]
        svg.append(f'<line x1="{x:.0f}" y1="{py(c["lo"]):.0f}" x2="{x:.0f}" y2="{py(c["hi"]):.0f}" stroke="{col}" stroke-width="1.5" opacity="0.3"/>')
        svg.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="10" fill="{col}"/>')
        svg.append(f'<text x="{x:.0f}" y="{y+4:.0f}" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">{c["rank"]}</text>')
    # painel lateral ranqueado
    lx = ML + PW + 24
    svg.append(f'<text x="{lx}" y="{MT+2}" font-size="12" font-weight="bold">ranking (melhor → pior)</text>')
    ly = MT + 24
    for c in work:
        col = ENVCOLOR[c["env"]]
        faixa = f" · varia [{c['lo']:+.0f},{c['hi']:+.0f}]" if c["hi"] != c["lo"] else " · estável"
        custo = "grátis" if c["cost"] == 0 else f"${c['cost']:.2f}/M"
        svg.append(f'<circle cx="{lx+8}" cy="{ly-4}" r="9" fill="{col}"/><text x="{lx+8}" y="{ly}" font-size="10.5" font-weight="bold" fill="#fff" text-anchor="middle">{c["rank"]}</text>')
        svg.append(f'<text x="{lx+24}" y="{ly-2}" font-size="11.5" font-weight="bold">{c["label"]} ({c["q"]:+.1f})</text>')
        svg.append(f'<text x="{lx+24}" y="{ly+11}" font-size="9.5" fill="#666">{ENVNAME[c["env"]]} · {custo}{faixa}</text>')
        ly += 30
    svg.append('</svg>')
    open(os.path.join(LAB, "VIZ-entrega-fronteira.svg"), "w", encoding="utf-8").write("\n".join(svg))
    print(f"\n-> VIZ-entrega-fronteira.svg ({len(work)} configs que funcionam)")
