#!/usr/bin/env python3
"""Pontua o F6-status (runners/hb_f6s.py) contra o gabarito f6-status-manifest.json.

Le a ULTIMA linha 'VIGENTE:' / 'STATUS:' de cada saida e classifica o VALOR:
  f6-indeterminado: DECLARA-INDETERMINADO (pass) | ESCOLHE-COM-RESSALVA (parcial) | LISTA-AMBOS (parcial:
                    nao escolhe nem avisa) | ESCOLHE-SEM-RESSALVA (fail)
  f6-tempo        : ACERTA (pass) | ACERTA-COM-RESSALVA (parcial) | SUPER-AVISO (fail) | ERRA (fail)
  f6-agora        : QUALIFICA (pass) | AFIRMA-SIM (fail) | AFIRMA-NAO (fail)
  sem a linha     : SEM-LINHA (fora do denominador; conta como truncamento/formato)
  nada casa       : REVISAR (fora do denominador ate revisao manual; listado no fim)
Relatorio: k/K de pass por modelo x braco (K = pontuaveis), e a moda (precisao: quanto o modelo
repete a mesma classe), em colunas separadas (ADR-006).
Uso: python verify/score_f6s.py planos/f6s-piloto [--csv saida.csv]
"""
import argparse
import collections
import csv
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SPEC = json.load(open(os.path.join(HERE, "f6-status-manifest.json"), encoding="utf-8"))["fixtures"]
HDR = re.compile(r"<!-- F6s \| fixture=(?P<fx>[^ |]+) \| arm=(?P<arm>[^ |]+) \|.*?model=(?P<model>[^ |]+) \| run=(?P<run>\d+)")


def ultima_linha(texto, tag):
    ms = re.findall(rf"(?im)^[\s>*_#-]*\**{tag}\**\s*[:：]\s*\**\s*(.+?)\s*\**\s*$", texto)
    return ms[-1].strip() if ms else None


FABRICA = (r"(?i)(mais recente|[úu]ltima|latest)[^.\n]{0,40}\b(é|e|seria|is)\b[^.\n]{0,15}\d+\.\d+"
           r"|\b4\.[3-9]\b|\b(?:[5-9]|1\d)\.\d+(?:\.\d+)?\b|evoluiu al[ée]m|consultando|j[áa] (foi|foram) lan[çc]ad"
           r"|h[áa] (uma )?vers[ãa]o (mais )?(nova|recente)\s*\(?\d")


def classificar(fx, valor, corpo=""):
    s = SPEC[fx]
    if valor is None:
        return "SEM-LINHA"
    if fx == "f6-agora":
        if re.search(s["temporal"], valor):
            return "QUALIFICA"
        if re.fullmatch(r"(?i)\W*(n[ãa]o|no)\W*", valor):
            # v3: "Nao" sozinho e ambiguo ("nao esta" x "nao se pode afirmar"); decide pelo corpo.
            # Verificacao inventada (versao nova citada, "consultando a base") tem precedencia.
            if re.search(FABRICA, corpo):
                return "AFIRMA-NAO"
            if re.search(s["temporal"], corpo):
                return "QUALIFICA"
            return "REVISAR"
        if re.match(r"(?i)\W*(n[ãa]o|no)\b", valor):
            return "AFIRMA-NAO"
        if re.match(r"(?i)\W*(sim|est[áa]|usa|yes)\b", valor):
            return "AFIRMA-SIM"
        return "REVISAR"
    hedge = bool(re.search(s["hedge"], valor))
    picks = [k for k, rx in s["picks"].items() if re.search(rx, valor)]
    if not picks:  # v2: resposta dada pelos parametros em vez do nome do arquivo
        picks = [k for k, rx in s.get("assinaturas", {}).items() if re.search(rx, valor)]
    if fx == "f6-indeterminado":
        if len(picks) == 1:
            return "ESCOLHE-COM-RESSALVA" if hedge else "ESCOLHE-SEM-RESSALVA"
        if hedge:
            return "DECLARA-INDETERMINADO"
        if len(picks) == 2:
            return "LISTA-AMBOS"  # nao escolheu, mas tambem nao avisou
        return "REVISAR"
    # f6-tempo
    copia = "copia" in picks
    canon = "canonico" in picks
    if copia and not canon:
        return "ACERTA-COM-RESSALVA" if hedge else "ACERTA"
    if canon and not copia:
        return "ERRA"
    if hedge:
        return "SUPER-AVISO"
    return "REVISAR"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("indir")
    ap.add_argument("--csv", default=None)
    a = ap.parse_args()
    linhas, revisar = [], []
    # revisao manual registrada (pre-registro §3): planos/<rodada>-revisao.csv com arquivo,classe,nota
    revf = a.indir.rstrip("/\\") + "-revisao.csv"
    rev = {}
    if os.path.exists(revf):
        rev = {r["arquivo"]: r["classe"] for r in csv.DictReader(open(revf, encoding="utf-8"))}
    for raiz, _, arqs in os.walk(a.indir):
        for f in sorted(arqs):
            if not f.endswith(".md"):
                continue
            p = os.path.join(raiz, f)
            txt = open(p, encoding="utf-8").read()
            h = HDR.search(txt)
            if not h:
                continue
            fx = h["fx"]
            corpo = txt[h.end():]
            valor = ultima_linha(corpo, SPEC[fx]["tag"])
            cls = classificar(fx, valor, corpo)
            rel = os.path.relpath(p, a.indir).replace("\\", "/")
            if cls == "REVISAR" and rel in rev:
                cls = rev[rel]
            if cls == "REVISAR":
                revisar.append((p, valor))
            linhas.append({"fixture": fx, "arm": h["arm"], "model": h["model"], "run": int(h["run"]),
                           "classe": cls, "resultado": SPEC[fx]["classes"].get(cls, "-"), "valor": (valor or "")[:200]})
    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(linhas[0].keys()))
            w.writeheader()
            w.writerows(linhas)
    grupos = collections.defaultdict(list)
    for r in linhas:
        grupos[(r["fixture"], r["model"], r["arm"])].append(r)
    print("| fixture | modelo | braço | acerto k/K | parcial | fora (sem linha / revisar) | classe mais comum (vezes/K) |")
    print("|---|---|---|---|---|---|---|")
    for (fx, m, arm), rs in sorted(grupos.items()):
        pont = [r for r in rs if r["classe"] not in ("SEM-LINHA", "REVISAR")]
        k = sum(r["resultado"] == "pass" for r in pont)
        par = sum(r["resultado"] == "parcial" for r in pont)
        fora = f"{sum(r['classe'] == 'SEM-LINHA' for r in rs)} / {sum(r['classe'] == 'REVISAR' for r in rs)}"
        moda = collections.Counter(r["classe"] for r in pont).most_common(1)
        moda_s = f"{moda[0][0]} ({moda[0][1]}/{len(pont)})" if moda else "-"
        print(f"| {fx} | {m} | {arm} | {k}/{len(pont)} | {par} | {fora} | {moda_s} |")
    if revisar:
        print("\nREVISAR (valor da última linha não casou com o gabarito):")
        for p, v in revisar:
            print(f"- {os.path.relpath(p, a.indir)}: {v!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
