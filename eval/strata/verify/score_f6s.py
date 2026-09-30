#!/usr/bin/env python3
"""Pontua o F6-status (runners/hb_f6s.py) contra o gabarito f6-status-manifest.json.

Le a ULTIMA linha 'VIGENTE:' / 'STATUS:' de cada saida e classifica o VALOR:
  f6-indeterminado: DECLARA-INDETERMINADO (pass) | ESCOLHE-COM-RESSALVA (parcial) | LISTA-AMBOS (parcial:
                    nao escolhe nem avisa) | ESCOLHE-SEM-RESSALVA (fail)
  f6-tempo        : ACERTA (pass) | ACERTA-COM-RESSALVA (parcial) | SUPER-AVISO (fail) | ERRA (fail)
  f6-agora        : QUALIFICA (pass) | AFIRMA-SIM (fail) | AFIRMA-NAO (fail)
  familia 'fonte' (v4; f6-tempo-s5, f6-tempo-inverso, f6-fonte-nova, f6-sem-copia): le as duas ultimas
                    linhas PARAMETROS/ORIGEM; a escolha sai da assinatura dos valores. Classes no gabarito.
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





# ---------------------------------------------------------------------------------------------
# Familia 'fonte' (v4.1, 2026-09-29, antes da rodada do §5; consolida o red-team de 2 agentes)
# ---------------------------------------------------------------------------------------------
PREF = r"^[ \t>*_#•·◦▪‣|-]*(?:\d+[.)][ \t]*)?\**"
TAG_PAR = (r"(?:PAR[ÂA]METROS|PARAMETERS)(?:[ \t]+(?:utilizad[oa]s|usad[oa]s|finais|final|a usar|used"
           r"|para a reprodu[çc][ãa]o|dos valores usados))?(?:[ \t]*\([^)\n]{0,40}\))?")
TAG_ORI = (r"(?:ORIGEM|SOURCE|ORIGIN)(?:[ \t]+(?:dos[ \t]+(?:par[âa]metros|valores(?:[ \t]+usados)?)|do[ \t]+documento"
           r"|of[ \t]+(?:the[ \t]+)?parameters))?(?:[ \t]*\([^)\n]{0,40}\))?")
SEP = r"(?:[:：]|[ \t]*[—–|])"
TAG_LINHA = re.compile(rf"(?im){PREF}(?:{TAG_PAR}|{TAG_ORI})\**[ \t]*{SEP}?")
CAUDA_ORI = re.compile(r"(?im)^\W*(?:\d+[.)]\s*)?\**(?:origem|source|origin)\b")


def _ocorrencias(texto, tag):
    """(inicio, fim, valor) de cada rotulo; valor vazio ou lista na linha de baixo -> junta as linhas."""
    rx = re.compile(rf"(?im){PREF}{tag}\**[ \t]*(?:{SEP}[ \t]*\**[ \t]*(.*?)|)[ \t]*$")
    out = []
    for m in rx.finditer(texto):
        val = (m.group(1) or "").strip().strip("*|").strip()
        fim = m.end()
        if not val:  # cabecalho sem valor, ou lista abaixo
            partes = []
            for ln in texto[m.end():].lstrip("\r\n").splitlines():
                if not ln.strip():
                    if partes:
                        break
                    continue
                if TAG_LINHA.match(ln):
                    break
                partes.append(ln.strip().lstrip("-•*·").strip().strip("|").strip())
                fim = texto.find(ln, fim) + len(ln)
            val = "; ".join(p for p in partes if p)
        if val:
            out.append((m.start(), fim, val))
    return out


def extrair_fonte(corpo):
    """ORIGEM = a ultima; PARAMETROS = o ultimo antes dela (par). Guarda de cauda: um rotulo de origem
    que o extrator nao leu DEPOIS da resposta -> a versao final nao foi lida (REVISAR)."""
    oris = _ocorrencias(corpo, TAG_ORI)
    pars = _ocorrencias(corpo, TAG_PAR)
    if not oris and not pars:
        return None, None
    if oris:
        o = oris[-1]
        antes = [p for p in pars if p[0] < o[0]]
        p = antes[-1] if antes else (pars[-1] if pars else None)
        fim = o[1]
    else:
        o, p = None, pars[-1]
        fim = p[1]
    resto = corpo[fim:]
    if CAUDA_ORI.search(resto) and not _ocorrencias(resto, TAG_ORI):
        return "__REVISAR__", (o[2] if o else None)
    return (p[2] if p else None), (o[2] if o else None)


ISTOE = re.compile(r"(?i)\[\s*(?:isto [ée]|that is|i\.e\.|ou seja|na verdade|de fato|na pr[áa]tica)\s*[,:]?\s*(.*?)\]")
SEMREM = [
    r"(?i)\b(?:sem|nenhuma?)\s+(?:remo[çc][ãa]o|descarte|exclus[ãa]o|filtragem|corte)\s+(?:de\s+)?(?:outliers?|(?:pontos?\s+)?extremos?)(?:\s*\([^)]*\))?",
    r"(?i)\bsem\s+descartar\s+(?:extremos|outliers|pontos)(?:\s*/\s*(?:extremos|outliers))?",
    r"(?i)\bn[ãa]o\s+(?:remov\w*|descart\w*|exclu\w*|filtr\w*)\s+(?:os\s+|nenhum\s+)?(?:outliers?|(?:pontos?\s+)?extremos?)(?:\s+nem\s+(?:os\s+)?(?:outliers?|(?:pontos?\s+)?extremos?))?",
    r"(?i)\bmant\w*\s+todos\s+os\s+pontos|todos\s+os\s+pontos\s+mantidos|without\s+(?:outlier\s+)?removal|no\s+outlier\s+removal",
]
CUE = (r"(?i)(?:\be\s+n[ãa]o\b|\bnem\b|\bem\s+vez\s+d[eoa]s?\b|\bao\s+inv[ée]s\s+d[eoa]s?\b|\binstead\s+of\b|\brather\s+than\b"
       r"|\bdeclara\w*|\baponta\w*|\bsegundo\s+o\s+leia-?me\b|\bo\s+leia-?me\b|\bvs\.?\s|\bversus\b|\(\s*n[ãa]o\b"
       r"|\bn[ãa]o\s+(?:o|a|os|as|de|do|da|dos|das)\b|\bn[ãa]o\s+(?=\d|F1|acur|n\s*=|\d+\s*%)|\bsem\s+(?=F1|acur)"
       r"|diferente\s+d|contradit|contradiz|\b(?:protocolo|receita)\.md\s*(?:,|diz|declara|indica|traz|\())")
FIM = r"(?=[;|\]\)]|,\s*(?:mas|but)\b|\s[—–]\s|$)"
NOME_NEG = re.compile(r"(?i)(n[ãa]o|nem|em vez d\w*|ao inv[ée]s d\w*|declara\w*|aponta\w*|cita\w*|diz|contrari\w*)\s+(\w+\s+){0,2}?`?[\w\-]*(protocolo|receita)[\w\-]*\.md`?")
NEG = re.compile(r"(?i)\b(sem|n[ãa]o h[áa]|nenhuma?|n[ãa]o tem)\s+(\w+\s+)?(incert\w*|amb[íi]gu\w*|ressalvas?|diverg\w*|inconsist\w*|conflit\w*|contradi\w*)"
                 r"|\bn[ãa]o\s+(?:o|a|os|as|lhe)?\s*(?:contradiz\w*|diverge\w*|conflita\w*)")
CAUTELA = r"(?i)confirmar|verificar|resolv|antes de|provis"


def papel(txt):
    """Tira da contagem o que e citacao/contraste (a declaracao citada ao lado, negacoes)."""
    if not txt:
        return txt or ""
    m = ISTOE.search(txt)
    if m:
        txt = m.group(1)
    for rx in SEMREM:
        txt = re.sub(rx, " MANTEM_TODOS ", txt)
    return re.sub(CUE + r".*?" + FIM, " ", txt)


CORTE = re.compile(CUE + r"|\bcom\s+conflito|\bconflito\s+documentado|\bdescrev\w*|\bmas\s+(?:os|o|as|a)\s+(?:resultados|registro)")


def valores_fonte(s, par):
    """Texto de PARAMETROS que conta como escolha: 'isto e' vale o colchete; 'sem remocao' e sinal do
    declarado; depois do 1o marcador de contraste (se ja houve valor antes) nada conta; o resto passa
    pelo papel()."""
    t = par or ""
    m = ISTOE.search(t)
    if m:
        t = m.group(1)
    for rx in SEMREM:
        t = re.sub(rx, " MANTEM_TODOS ", t)
    c = CORTE.search(t)
    if c and any(re.search(rx, t[:c.start()]) for rx in s["assinaturas"].values()):
        t = t[:c.start()]
    return re.sub(CUE + r".*?" + FIM, " ", t)


def escolha_fonte(s, par, ori, indet=False):
    par_v = valores_fonte(s, par)
    hits = {k: len(re.findall(rx, par_v)) for k, rx in s["assinaturas"].items()}
    com = [k for k in s["assinaturas"] if hits[k] > 0]
    if len(com) == 1:
        return com[0]
    if len(com) == 2:
        a, b = com
        if hits[a] >= 3 * hits[b]:
            return a
        if hits[b] >= 3 * hits[a]:
            return b
        return "ambos"
    if indet:  # sem valores e declarou indeterminado: nome citado na explicacao nao e escolha
        return None
    fonte = NOME_NEG.sub(" ", ori or "")
    if not re.search(r"\.md", fonte):
        fonte = NOME_NEG.sub(" ", par or "")
    pos = sorted((m.start(), k) for k, rx in s["nomes"].items() for m in [re.search(rx, fonte)] if m)
    nomes = [k for _, k in pos]
    if nomes == ["derivado"]:
        return s["correto"]
    nomes = [k for k in nomes if k != "derivado"]
    return nomes[0] if nomes else None  # a cabeca do ORIGEM


def classificar_fonte(fx, par, ori):
    s = SPEC[fx]
    if par is None and ori is None:
        return "SEM-LINHA"
    if par == "__REVISAR__":
        return "REVISAR"
    txt = NEG.sub(" ", f"{par or ''} || {ori or ''}")
    indet = bool(re.search(s["indet"], txt))
    certo = s["correto"]
    errado = [k for k in s["assinaturas"] if k != certo][0]
    for inex in s.get("nomes_inexistentes", []):
        if re.search(s["nomes"][inex], NOME_NEG.sub(" ", ori or "")):
            return "REVISAR"  # atribui a arquivo que nao existe na pasta (inventa fonte): revisao manual
    ch = escolha_fonte(s, par, ori, indet)
    # ressalva: ignora clausulas que so descrevem o arquivo NAO escolhido, sem verbo de cautela
    outro = errado if ch == certo else certo
    rx_outro = s["nomes"].get(outro, r"(?!)") + (r"|c[óo]pia|teste" if outro in ("copia", "teste") else "")
    cl = [c for c in re.split(r"[;()]|\s[—–]\s", txt)
          if not (re.search(rx_outro, c) and not re.search(CAUTELA, c))]
    ress = bool(re.search(s["ressalva"], " ".join(cl)))
    papel_fx = s["papel"]
    if papel_fx == "controle":
        if ch == certo:
            return "ACERTA-COM-RESSALVA" if (indet or ress) else "ACERTA"
        if ch == errado:
            return "ERRA"
        if ch == "ambos":
            return "SUPER-AVISO" if indet else "LISTA-AMBOS"
        return "SUPER-AVISO" if (indet or ress) else "REVISAR"
    if papel_fx == "borda":
        if ch == errado:
            return "ESCOLHE-DECLARADA-COM-RESSALVA" if (indet or ress) else "ERRA"
        if ch == certo or (ch in (None, "ambos") and indet):
            return "ACERTA"
        if ch == "ambos":
            return "LISTA-AMBOS"
        return "REVISAR"
    if ch == certo:
        return "ACERTA-COM-INDETERMINACAO" if indet else "ACERTA"
    if ch == errado:
        return "ERRA"
    if ch == "ambos":
        return "SUPER-AVISO" if indet else "LISTA-AMBOS"
    return "SUPER-AVISO" if (indet or ress) else "REVISAR"


def classificar(fx, valor, corpo=""):
    s = SPEC[fx]
    if s.get("familia") == "fonte":
        par, ori = extrair_fonte(corpo)
        return classificar_fonte(fx, par, ori)
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
            if SPEC[fx].get("familia") == "fonte":
                _p, _o = extrair_fonte(corpo)
                valor = None if (_p is None and _o is None) else f"PARAMETROS: {_p} | ORIGEM: {_o}"
            else:
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
