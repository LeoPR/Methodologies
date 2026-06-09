#!/usr/bin/env python3
"""Confronto de JUIZES (escada de tamanho) no MESMO conjunto cego P1+P2 (AN-v2 vs AN-v3).
Testa a hipotese 'maior = melhor juiz'. Discriminador: o NNN exemplar AN-v2 DEMONSTRAVELMENTE
gera falso-positivo (os planos criticam pratica boa / flagam os arquivos-IA) — um juiz que
reporta FP perto do real e' melhor; leniente demais (FP~0) e' pior.
Uso: python compare_judges_ladder.py <claude.output>   (glob automatico dos cmp-judge-*.json)"""
import glob
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PLANOS = os.path.join(HERE, "planos")
KEYS = {"nnn": json.load(open(os.path.join(PLANOS, "nnn-cmp-key.json"), encoding="utf-8")),
        "pdf2md": json.load(open(os.path.join(PLANOS, "pdf2md-cmp-key.json"), encoding="utf-8"))}
ARM = {"v2": {"nnn": "real-nnn-an", "pdf2md": "real-pdf2md-an"},
       "v3": {"nnn": "anv3-nnn", "pdf2md": "anv3-pdf2md"}}


def agg(result):
    """result = {nnn:[...], pdf2md:[...]} -> dict de metricas por arm."""
    out = {}
    for proj in ("nnn", "pdf2md"):
        sc = {s["id"]: s for s in result.get(proj, [])}
        for v in ("v2", "v3"):
            rows = [sc[i] for i, m in KEYS[proj].items() if i in sc and m["arm"] == ARM[v][proj]]
            if rows:
                out[(proj, v, "fp")] = sum(r["false_positives"] for r in rows) / len(rows)
                out[(proj, v, "gen")] = sum(r["genuine_real"] for r in rows) / len(rows)
                out[(proj, v, "rg")] = sum(1 for r in rows if r["recognized_good"]) / len(rows)
    return out


judges = {}
# Claude (workflow) passado por arg
if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
    d = json.load(open(sys.argv[1], encoding="utf-8")); r = d.get("result", d)
    if isinstance(r, str):
        r = json.loads(r)
    judges["claude-opus(wf)"] = agg(r)
# todos os cmp-judge-*.json
for f in sorted(glob.glob(os.path.join(PLANOS, "cmp-judge-*.json"))):
    name = os.path.basename(f)[len("cmp-judge-"):-len(".json")]
    d = json.load(open(f, encoding="utf-8"))
    judges[name] = agg(d.get("result", d))

# tamanho aproximado (so p/ ordenar a "escada"): nano<mini<4.1-mini<flash<5<codex<o3<5.5<pro<opus
RANK = ["openai_gpt-5-nano", "openai_gpt-5-mini", "openai_gpt-4.1-mini", "google_gemini-2.5-flash",
        "openai_gpt-5", "openai_gpt-5-codex", "openai_o3", "openai_gpt-5.5",
        "google_gemini-2.5-pro", "claude-opus(wf)"]
order = [j for j in RANK if j in judges] + [j for j in judges if j not in RANK]

print(f"{'JUIZ (menor->maior)':26}{'NNN v2 FP':>10}{'NNN v3 FP':>10}{'NNN recog v2/v3':>16}{'pdf gen v2/v3':>14}")
for j in order:
    m = judges[j]
    fp2 = m.get(("nnn", "v2", "fp")); fp3 = m.get(("nnn", "v3", "fp"))
    rg2 = m.get(("nnn", "v2", "rg")); rg3 = m.get(("nnn", "v3", "rg"))
    g2 = m.get(("pdf2md", "v2", "gen")); g3 = m.get(("pdf2md", "v3", "gen"))

    def s(x, f="{:.2f}"):
        return f.format(x) if x is not None else "-"
    print(f"{j:26}{s(fp2):>10}{s(fp3):>10}{(s(rg2)+'/'+s(rg3)):>16}{(s(g2)+'/'+s(g3)):>14}")
print("\nLEITURA: NNN v2 FP alto = juiz ENXERGA o falso-positivo (melhor); ~0 = leniente (pior).")
print("A escada testa 'maior=melhor juiz?'. Onde juizes DISCORDAM, adjudicar por fato objetivo do plano.")
