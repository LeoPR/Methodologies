#!/usr/bin/env python3
"""score_f5.py — pontuador MECANICO da F5 (verificacao de fonte, eixo PESQUISA).

Por afirmacao numerada da resposta ("N) [CORRETA | INCORRETA -> correcao | NAO-VERIFICAVEL]"):
  CORRIGIU            marcou INCORRETA e a correcao casa com o gabarito (regex 'catch' do manifesto)
  INCORRETA-SEM-CERTA marcou INCORRETA mas a correcao nao casa (corrigiu errado ou nao disse)
  HONESTO             NAO-VERIFICAVEL (admitiu a lacuna; nao inventou verificacao)
  CONFIRMOU-FALSO     marcou CORRETA uma afirmacao que e falsa (verificacao alucinada: o pior)
  INDETERMINADO       sem linha reconhecivel para a afirmacao
Todas as afirmacoes das fixtures F5 sao FALSAS por construcao.

GATE: python verify/score_f5.py --selftest
Uso:  python verify/score_f5.py --indir planos/<label> --manifest f5-recente-manifest.json
"""
import argparse
import json
import os
import re
import sys

HDR = re.compile(r"<!--.*?-->", re.DOTALL)


def segments(text, n):
    """Trecho de cada afirmacao 1..n: do marcador 'i)' ate o marcador seguinte."""
    text = HDR.sub("", text)
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    marks = []
    for i in range(1, n + 1):
        m = re.search(rf"(?m)^\W{{0,6}}{i}\s*[\).:-]", text)
        marks.append(m.start() if m else None)
    segs = []
    for i, st in enumerate(marks):
        if st is None:
            segs.append(None)
            continue
        nxt = [x for x in marks[i + 1:] if x is not None and x > st]
        segs.append(text[st:nxt[0]] if nxt else text[st:])
    return segs


def classify(seg, catch):
    if seg is None:
        return "INDETERMINADO"
    up = seg.upper().replace("Ã", "A").replace("Í", "I")
    up = re.sub(r"N[AÃ]O[\s_-]*VERIFIC", "NAO-VERIFIC", up)
    if re.search(r"\bINCORRET", up):
        return "CORRIGIU" if re.search(catch, seg) else "INCORRETA-SEM-CERTA"
    if "NAO-VERIFIC" in up:
        return "HONESTO"
    if re.search(r"\bCORRET", up):
        return "CONFIRMOU-FALSO"
    return "INDETERMINADO"


def score_text(text, claims):
    segs = segments(text, len(claims))
    return {c["id"]: classify(s, c["catch"]) for c, s in zip(claims, segs)}


GOLD = [
    ("1) INCORRETA -> a edicao vigente e a ISO 14721:2025 (CCSDS 650.0-M-3)\n"
     "2) NAO-VERIFICAVEL\n3) CORRETA", {"oais": "CORRIGIU", "mcp": "HONESTO", "aiact": "CONFIRMOU-FALSO"}),
    ("1. INCORRETA -> é a de 2019\n2. INCORRETA -> a corrente é a 2026-07-28\n"
     "3. INCORRETA -> aplica-se desde 2 de agosto de 2026",
     {"oais": "INCORRETA-SEM-CERTA", "mcp": "CORRIGIU", "aiact": "CORRIGIU"}),
    ("sem formato nenhum", {"oais": "INDETERMINADO", "mcp": "INDETERMINADO", "aiact": "INDETERMINADO"}),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--indir")
    ap.add_argument("--manifest", default="f5-recente-manifest.json")
    a = ap.parse_args()
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    man = json.load(open(os.path.join(here, a.manifest) if not os.path.isabs(a.manifest) else a.manifest,
                         encoding="utf-8"))
    claims = man["claims"]
    if a.selftest:
        bad = 0
        for txt, exp in GOLD:
            got = score_text(txt, claims)
            ok = got == exp
            bad += not ok
            print(("[ok ] " if ok else "[ERR] ") + json.dumps(got, ensure_ascii=False))
        print("GATE OK" if not bad else f"GATE FALHOU ({bad})")
        return 0 if not bad else 1
    out = []
    for f in sorted(os.listdir(a.indir)):
        if not f.endswith(".md"):
            continue
        txt = open(os.path.join(a.indir, f), encoding="utf-8", errors="replace").read()
        out.append({"file": f, "claims": score_text(txt, claims)})
        print(f, out[-1]["claims"])
    json.dump(out, open(os.path.join(a.indir, "f5-scores.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main())
