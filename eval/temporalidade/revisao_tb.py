#!/usr/bin/env python3
"""Revisão manual cega da bateria de temporalidade v1 (PREREG-bateria-v1.md §4).

  amostra <indir>        sorteia por família × braço (nota não trivial: 25%, mín. 20; nota 'nenhuma': 5%),
                         semente 20260930, e escreve <indir>-revisao-lista.md (cega a braço e modelo: só as
                         cenas rotuladas, o gabarito em rótulos de exibição e as linhas SEQUÊNCIA/NOTA) e
                         <indir>-revisao-chave.json (id -> arquivo).
  ampliar <indir> <fam>  acrescenta à lista todas as notas não triviais da família (concordância < 0,90).
  aplicar <indir>        lê <indir>-revisao-ids.csv (id,classe), grava <indir>-revisao.csv (arquivo,classe)
                         e reporta a concordância pontuador × revisão por família (fração e kappa de Cohen).
"""
import collections
import csv
import json
import os
import random
import re
import sys

import score_tb as S

SEMENTE = 20260930
TRIVIAL = re.compile(r"(?i)^\W*(nenhuma|nenhum|none|n/?a|-+)\W*$")


def nota_de(texto):
    return (S.rotulo_final(texto, r"NOTAS?|NOTES?", ate_o_fim=True) or "").strip()


def linhas_com_texto(indir):
    out = []
    for r in S.carregar(indir):
        t = open(os.path.join(indir, r["arquivo"]), encoding="utf-8").read()
        h = S.HDR.search(t)
        corpo = t[h.end():]
        r["nota_txt"] = nota_de(corpo)
        r["seq_txt"] = S.rotulo_final(corpo, r"SEQU[ÊE]NCIA|SEQUENCE") or ""
        r["mapa"] = h["mapa"]
        out.append(r)
    return out


def bloco(i, r):
    f = S.BAT["fixtures"][r["fixture"]]
    disp = {k: S.ROTULOS[j] for j, k in enumerate(r["mapa"])}
    cenas = "\n".join(f"  {disp[k]}. {f['cenas'][k]}" for k in r["mapa"])
    regras = S.BAT["dominios"][f["dominio"]]["regras"]
    gab = [f"papel: {f['papel']}", "antes: " + ", ".join(f"{disp[a]}<{disp[b]}" for a, b in f["antes"])]
    if f.get("incomparaveis"):
        gab.append("sem ordem: " + ", ".join(f"{disp[a]}|{disp[b]}" for a, b in f["incomparaveis"]))
    if f.get("conflito"):
        gab.append("conflito: " + " × ".join(disp[x] for x in f["conflito"]))
    if f.get("intruso"):
        gab.append(f"intruso: {disp[f['intruso']]}")
    if f["papel"] == "lacuna":
        gab.append("lacuna: o estado que falta entre as cenas (ver bateria-v1.json)")
    return (f"### {i}\n\n" + (("Regras: " + " / ".join(regras) + "\n\n") if regras else "") + f"Cenas:\n{cenas}\n\n"
            f"Gabarito: {'; '.join(gab)}\n\nSEQUÊNCIA: {r['seq_txt']}\nNOTA: {r['nota_txt'] or '(vazia)'}\n\n"
            f"Classe: \n\n")


def amostra(indir):
    rng = random.Random(SEMENTE)
    ls = [r for r in linhas_com_texto(indir) if r["classe_auto"] != "SEM-LINHA" and r["stop"] != "length"]
    est = collections.defaultdict(lambda: {"nt": [], "triv": []})
    for r in ls:
        est[(r["familia"], r["arm"])]["triv" if TRIVIAL.match(r["nota_txt"]) else "nt"].append(r)
    escolhidas = []
    for k in sorted(est):
        nt, tv = est[k]["nt"], est[k]["triv"]
        n_nt = len(nt) if len(nt) <= 20 else max(20, round(0.25 * len(nt)))
        escolhidas += rng.sample(nt, n_nt) + rng.sample(tv, max(1, round(0.05 * len(tv))) if tv else 0)
    # resposta tirada do canal de raciocínio (ft=1, terminou com stop=stop): todas entram (PREREG §9, 2026-09-30)
    ja = {r["arquivo"] for r in escolhidas}
    escolhidas += [r for r in ls if r["ft"] == "1" and r["arquivo"] not in ja]
    escrever(indir, escolhidas, rng)


def escrever(indir, escolhidas, rng, anexar=False):
    ch_p = indir.rstrip("/\\") + "-revisao-chave.json"
    chave = json.load(open(ch_p, encoding="utf-8")) if anexar and os.path.exists(ch_p) else {}
    ja = set(chave.values())
    novas = [r for r in escolhidas if r["arquivo"] not in ja]
    rng.shuffle(novas)
    ini = len(chave) + 1
    modo = "a" if anexar else "w"
    with open(indir.rstrip("/\\") + "-revisao-lista.md", modo, encoding="utf-8") as fh:
        if not anexar:
            fh.write("# Revisão cega (sem braço nem modelo). Classe com o nome do pontuador.\n\n")
        for i, r in enumerate(novas, ini):
            chave[str(i)] = r["arquivo"]
            fh.write(bloco(i, r))
    json.dump(chave, open(ch_p, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(f"{len(novas)} saídas na lista (total {len(chave)})")


def ampliar(indir, fam):
    ls = [r for r in linhas_com_texto(indir) if r["familia"] == fam and r["classe_auto"] != "SEM-LINHA" and r["stop"] != "length"
          and not TRIVIAL.match(r["nota_txt"])]
    escrever(indir, ls, random.Random(SEMENTE + 1), anexar=True)


def kappa(pares):
    n = len(pares)
    if not n:
        return None, None
    po = sum(a == b for a, b in pares) / n
    ca, cb = collections.Counter(a for a, _ in pares), collections.Counter(b for _, b in pares)
    pe = sum(ca[k] * cb[k] for k in set(ca) | set(cb)) / n / n
    return po, (po - pe) / (1 - pe) if pe < 1 else 1.0


def aplicar(indir):
    base = indir.rstrip("/\\")
    chave = json.load(open(base + "-revisao-chave.json", encoding="utf-8"))
    ids = {row["id"]: row["classe"].strip() for row in csv.DictReader(open(base + "-revisao-ids.csv", encoding="utf-8")) if row["classe"].strip()}
    auto = {r["arquivo"]: r for r in S.carregar(indir)}
    with open(base + "-revisao.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["arquivo", "classe"])
        for i, c in sorted(ids.items(), key=lambda x: int(x[0])):
            w.writerow([chave[i], c])
    por_fam = collections.defaultdict(list)
    for i, c in ids.items():
        r = auto[os.path.normpath(chave[i])]
        por_fam[r["familia"]].append((r["classe_auto"], c))
    print("| família | revisadas | concordância | kappa |")
    print("|---|---|---|---|")
    for fam, ps in sorted(por_fam.items()):
        po, k = kappa(ps)
        print(f"| {fam} | {len(ps)} | {po:.2f} | {k:.2f} |")


if __name__ == "__main__":
    cmd, indir = sys.argv[1], sys.argv[2]
    {"amostra": lambda: amostra(indir), "aplicar": lambda: aplicar(indir),
     "ampliar": lambda: ampliar(indir, sys.argv[3])}[cmd]()
