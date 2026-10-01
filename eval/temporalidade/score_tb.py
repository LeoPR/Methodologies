#!/usr/bin/env python3
"""Pontua a bateria de temporalidade v1 (hb_tb.py) contra bateria-v1.json.

O modelo vê as cenas rotuladas A, B, C... na ordem de apresentação; o cabeçalho de cada saída traz
mapa=<letras internas nessa ordem>, e o pontuador traduz a resposta para as letras do gabarito.

Lê a última SEQUÊNCIA (pula o molde da tarefa; aceita lista em várias linhas e setas LaTeX/Unicode) e a
última NOTA (até a primeira linha em branco).
- SEQUÊNCIA vira grupos: 'A → B | C → D' = [{A}, {B, C}, {D}]; dentro do grupo, sem ordem.
  Rótulo de cena ausente = omitida; item que não é rótulo de cena = acrescentado.
- ORDEM-CERTA: nenhum par do gabarito invertido, nenhum par comparável no mesmo grupo e nenhuma cena do
  gabarito omitida.
- NOTA, pelo papel da fixture (menção negada, como 'não há conflito' ou 'sem lacunas, X ou Y', não conta):
  ordem / controle-horario: ALARME se a nota aponta problema (falso alarme).
  fora-do-script: SEGUE-OBSERVADO se a ordem é a observada; nota sobre o desvio do esperado é permitida.
  horario-errado: CONFLITO-APONTADO se a nota fala de horário e de contradição.
  lacuna: LACUNA-APONTADA se a nota nomeia o passo (lacuna_rx) e marca a falta, ou se um item acrescentado
  à sequência o nomeia.
  intruso: INTRUSO-APONTADO se a cena fica fora da sequência, ou se a nota a cita com marca de 'não pertence'.
  incomparaveis: INCOMP-DECLARADO se cada par sem ordem fica no mesmo grupo ou a nota diz que a ordem entre
  eles não se sabe (por rótulo ou por conteúdo, incomp_txt); INCOMP-PARCIAL / INCOMP-FORCADO.
Sem a linha SEQUÊNCIA, ou cortada por tamanho (stop=length, desvio de 2026-09-30): SEM-LINHA (fora do
denominador); classe_auto guarda a leitura crua.
Revisão manual: planos/<rodada>-revisao.csv (arquivo,classe) sobrepõe a classe do pontuador.
Red-team 2026-09-30 (solver cego + ataque ao pontuador) incorporado antes do congelamento.
Uso: python score_tb.py planos/tb-v1 [--csv saida.csv]
"""
import argparse
import collections
import csv
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BAT = json.load(open(os.path.join(HERE, "bateria-v1.json"), encoding="utf-8"))
ROTULOS = "ABCDEFGH"
HDR = re.compile(r"<!-- TB \| fixture=(?P<fx>[^ |]+) \| arm=(?P<arm>[^ |]+) \| perm=(?P<perm>\d+) \| "
                 r"model=(?P<model>[^ |]+) \| run=(?P<run>\d+) \| mapa=(?P<mapa>[A-Z]+)")
PREF = r"^[ \t>*_#•·|`-]*(?:\d+[.)][ \t]*)?\**"
ALARME = (r"(?i)falt|lacuna|intrus|n[ãa]o pertence|fora do epis|sem rela[çc][ãa]o|conflit|contradi|inconsist|incoer"
          r"|n[ãa]o bate|n[ãa]o confere|n[ãa]o condiz|diverg|discrep|incompat|indetermin|amb[íi]gu|errad|incorret|imposs[íi]vel")
# [F6] HORA e CONTRA: vocabulário comum que faltava
HORA = (r"(?i)hor[áa]ri|\bhoras?\b|\d{1,2}\s*h\s*\d{2}|\d{1,2}:\d{2}|timestamp|carimbo|marca[çc][ãa]o"
        r"|\btimes?\b|\bmarked\b|\bos tempos\b|\btempos? (anotad|indicad|registrad|marcad)|marcas? de tempo")
CONTRA = (r"(?i)contradi|inconsist|incoer|conflit|n[ãa]o bate|n[ãa]o confere|n[ãa]o condiz|n[ãa]o correspond|diverg|discrep"
          r"|incompat|errad|incorret|equivoc|engan|suspeit|invertid|imposs[íi](vel|ble)|n[ãa]o (é|s[ãa]o) confi[áa]ve"
          r"|trocad|\berros?\b|anomal|estranh|n[ãa]o faz(ia)? sentido|n[ãa]o (é|seria|era) poss[íi]vel|\bdifere"
          r"|fora de ordem|n[ãa]o (segue|seguem|reflete|refletem|respeita|respeitam)\b|n[ãa]o (é|s[ãa]o) (coerente|consistente|compat)"
          r"|invers"
          # contraste horário × lógica: 'horário anterior ao de E, mas logicamente deve ocorrer depois'
          r"|(anterior|posterior|antes|depois|mais cedo|mais tarde|precede\w*|sucede\w*)\b.{0,80}\b(mas|por[ée]m|embora|contudo|entretanto|apesar)\b"
          r".{0,80}(l[óo]gic|dev[ea]|deveria|precis|tem que|exig|depend|regra|na verdade|ocorre\w* (depois|antes))")
# [F7] INDET_PAR: vocabulário + negação de dependência
INDET_PAR = (r"(?i)n[ãa]o (d[áa]|h[áa] como|se (pode )?sab|[ée] poss[íi]vel (saber|determinar|definir))|indetermin|sem (ordem|depend)"
             r"|independe|qualquer ordem|paralel|simult|concorr|ordem (relativa )?(entre|de) .{0,40}(n[ãa]o|indeterm|livre|desconhec)"
             r"|arbitr[áa]ri|incert|indiferente|tanto faz|intercambi|n[ãa]o h[áa] (nenhum\w* )?(depend|rela[çc][ãa]o de ordem|ordem)"
             r"|n[ãa]o depende|imposs[íi]vel (saber|determinar|definir|afirmar)|n[ãa]o se pode (determinar|definir|afirmar)"
             r"|n[ãa]o pode (ser )?(definid|determinad|estabelecid|fixad)|poderia ser (o )?contr[áa]rio|pode(ria)? ser invertid")
DENY_INDET = r"(?i)n[ãa]o (é|s[ãa]o|est[áa]o?|foi|foram|parece\w*) (\w+ )?(indetermin|incert|arbitr|simult|paralel|independ|livre|desconhec)"
# [F8] FORA só com o que diz 'não pertence' (sem 'indeterminado/ambíguo/falta/lacuna'), mais o que faltava
FORA = (r"(?i)intrus|n[ãa]o pertence|fora do epis|sem rela[çc][ãa]o|n[ãa]o condiz|incoer|incompat|inconsist|destoa|deslocad"
        r"|n[ãa]o se (encaixa|relaciona|liga|conecta)|alhei|isolad|irrelevan|outro epis|outro contexto|contexto diferente|independente|avuls"
        r"|sem (nenhum\w* )?(v[íi]nculo|liga[çc]|conex|depend|rela)|n[ãa]o (possui|tem|guarda|mant[ée]m|apresenta) (nenhum\w* )?"
        r"(v[íi]nculo|rela[çc]|liga[çc]|conex|depend)|exclu[íi]d|descartad|removid|ignorad"
        r"|n[ãa]o faz parte|n[ãa]o tem (nada )?a ver|nada a ver|n[ãa]o h[áa] (nenhum\w* )?(v[íi]nculo|rela[çc]|liga[çc]|conex)"
        r"|nenhum\w* (v[íi]nculo|rela[çc]|liga[çc]|conex)|desconex")
# [F4] negação: 'não' + até 2 palavras antes do termo; 'nada', 'nem', 'não houve/havendo', 'inexiste'
NEG = (r"(?i)\b(?:n[ãa]o|nem|nunca|jamais|tampouco)\b(?:\s+[\w-]+){0,2}\s*$"
       r"|\b(?:sem|nenhum\w*|nada|nem|n[ãa]o h[áa]|n[ãa]o houve|n[ãa]o havendo|inexist\w*|livre de|aus[êe]ncia de)\b")
# [F4] cortes de oração: pontuação, travessões e conectivos de exceção/contraste
CORTE = (r"(?i)[.;:!?\n—–]|\bmas\b|\bpor[ée]m\b|\bcontudo\b|\bentretanto\b|\btodavia\b|\bexceto\b|\bsalvo\b"
         r"|\bal[ée]m d[eoa]s?\b|\ba n[ãa]o ser\b|\be sim\b|\bs[óo]\b|\bapenas\b|\bsomente\b")
HIPO = r"(?i)\bqualquer outr[ao]\b|\boutra ordem\b|\bcaso contr[áa]rio\b|\bdo contr[áa]rio\b"
# [F4] comentário sobre a ORDEM DE APRESENTAÇÃO (embaralhada de propósito), não sobre o episódio
APRES = r"(?i)ordem (de apresenta|das cenas (apresentadas|na lista|dadas))|cenas (vieram|foram (dadas|apresentadas|listadas))|embaralh"
GAP = (r"(?i)falt|lacuna|n[ãa]o (h[áa]|aparece|mostra|[ée] mostrad|est[áa] (mostrad|representad))|nenhuma cena|ausent|omit|pulad"
       r"|sem que se (veja|mostre)|n[ãa]o se (v[êe]|mostra)"
       r"|impl[íi]cit|inferid|entre as cenas|entre [A-H] e [A-H]|precisa(ria)? ter|teria|deve ter|salto l[óo]gico|\?")


def _lista(p):
    """[F4] pedaço depois da vírgula que continua uma lista negada ('sem X, Y ou Z')."""
    w = p.split()
    return len(w) <= 2 or (len(w) <= 4 and re.search(r"(?i)\b(ou|nem|e)\b", p))


def afirma(rx, texto):
    """Há ocorrência de rx não negada na mesma oração?"""
    for m in re.finditer(rx, texto):
        antes = texto[max(0, m.start() - 100):m.start()]  # [F4] a oração limita, não 40 caracteres
        antes = re.sub(r"(?i)\bsem d[úu]vida\b|\bn[ãa]o h[áa] d[úu]vida( de)?( que)?", " ", antes)  # [F4]
        antes = re.split(CORTE, antes)[-1]
        if re.search(HIPO, antes) or re.search(APRES, antes):  # [F4] contrafactual / ordem de apresentação
            continue
        ps = antes.split(",")
        j = len(ps) - 1
        while j > 0 and _lista(ps[j]) and not re.search(NEG, ps[j]):
            j -= 1
        if not re.search(NEG, ps[j]):
            return True
    return False


TEMPLATE = re.compile(r"(?i)^\s*<[^>\n]*(letras|ressalva|impede|afeta|o que)")


def rotulo_final(texto, tag, ate_o_fim=False):
    # [F2] aceita 'SEQUÊNCIA FINAL:', 'NOTAS:', e título sem dois-pontos ('### SEQUÊNCIA' + valor na linha seguinte)
    rx = re.compile(rf"(?im){PREF}(?:{tag})(?:[ \t]+(?:final|reconstru[íi]da|correta|proposta))?\**[ \t]*(?:[:：]|\**[ \t]*$)[ \t]*\**")
    ms = [m for m in rx.finditer(texto) if not TEMPLATE.match(texto[m.end():].split("\n", 1)[0])]  # [F2] pula o molde
    if not ms:
        return None
    resto = texto[ms[-1].end():]
    if ate_o_fim:
        # [F3] a NOTA vai até a primeira linha em branco depois do conteúdo, não até o fim do texto
        return re.split(r"\n[ \t]*\n", resto.strip(), maxsplit=1)[0].strip().strip("`*").strip()[:1200]
    linhas = [ln.strip() for ln in resto.split("\n")]
    for i, ln in enumerate(linhas):
        ln = ln.strip("`*").strip()
        if not ln:
            continue
        if re.match(r"^(?:\d+\s*[.)]|[-•*])\s+", ln):  # [F1] lista em várias linhas
            itens = []
            for l2 in linhas[i:]:
                if not re.match(r"^(?:\d+\s*[.)]|[-•*])\s+", l2):
                    break
                itens.append(l2)
            return " → ".join(itens)
        return ln
    return ""


def partir(bloco):
    itens, cur, prof = [], "", 0
    for ch in bloco:
        if ch in "([{":
            prof += 1
        elif ch in ")]}":
            prof = max(0, prof - 1)
        if ch in "|,/" and prof == 0:
            itens.append(cur)
            cur = ""
        else:
            cur += ch
    itens.append(cur)
    return itens


SETA = r"\$?\\(?:long)?(?:right)?arrow\$?|\$?\\(?:Long)?Rightarrow\$?|\$?\\to\$?|[➔➜➝➞➙➛⟹⟶⇒⇨➡⭢]"
SEP_GRUPO = r"\s*(?:[|,/&+]|\be\b|\bou\b)\s*"


def grupos(seq, mapa):
    t = re.sub(SETA, "→", seq)  # [F1] setas LaTeX/Unicode
    t = re.sub(r"^\s*<|>\s*$", "", t)  # [F1] '<...>' do molde
    t = t.replace("->", "→").replace("=>", "→").replace(">", "→")
    lbl = r"(?:[Cc]ena\s+)?\(?[A-H]\b"
    t = re.sub(rf"(?<=[A-H)\]])\s+[-–—]\s+(?={lbl})", " → ", t)  # [F1] hífen/travessão entre rótulos
    t = re.sub(rf"[(\[{{]\s*([A-H](?:{SEP_GRUPO}[A-H])+)\s*[)\]}}]",
               lambda m: re.sub(SEP_GRUPO, " | ", m.group(1)), t)  # [F1] '(X, Y)', '[X|Y]', '{X, Y}'
    t = re.sub(r"\b([A-H])\s+(?:e|ou|&|\+)\s+(?=[A-H]\b)", r"\1 | ", t)  # [F1] 'X e Y'
    if "→" not in t:  # [F1] vírgula é sequência mesmo com '|'
        t = t.replace(",", "→")
    gs, extras = [], []
    for bloco in t.split("→"):
        g = set()
        for item in partir(bloco):
            it = item.strip().strip("*`").strip()
            it = re.sub(r"^(?:\d+\s*[.)º°]\s*|[-•*]\s+)", "", it)  # [F1] '1) X', '- X'
            if not it:
                continue
            m = (re.fullmatch(r"(?:[Cc]ena\s+)?\(?([A-H])\)?(?:[\W_].*)?", it, re.S)
                 or re.fullmatch(r"[^()\[\]]*?[(\[]\s*(?:[Cc]ena\s+)?([A-H])\s*[)\]]\s*[.!]?", it))  # [F1] 'Embarque (D)'
            if m and ROTULOS.index(m.group(1)) < len(mapa):
                g.add(mapa[ROTULOS.index(m.group(1))])
            else:
                extras.append(it)
        if g:
            gs.append(g)
    return gs, extras


def rel(gs, a, b):
    ia = next((i for i, g in enumerate(gs) if a in g), None)
    ib = next((i for i, g in enumerate(gs) if b in g), None)
    if ia is None or ib is None:
        return "ausente"
    if ia == ib:
        return "sem-ordem"
    return "certo" if ia < ib else "invertido"


def cita_rotulo(r, texto):
    return bool(re.search(rf"(?i:cenas?)\s+(?:[A-H]\s*(?:,|e|ou)\s*)*{r}\b|\({r}\)|(?<![\w]){r}\s*[(:)–—-]|(?<![\w]){r}\s+(?:é|não|nao|est[áa]|parece|fica|pertence|descreve|mostra)\b", texto))


def lab(r):
    """[F7] rótulo em contexto de rótulo: exclui artigo/conjunção ('A sequência', 'E então')."""
    ok = r"(?:e|ou|é|n[ãa]o|nem|vem|v[êe]m|precede\w*|depende\w*|pode\w*|s[ãa]o|est[áa]\w*|fica\w*|ocorre\w*|acontece\w*|antes|depois|quanto|como|tamb[ée]m)"
    return rf"(?<![\w]){r}\b(?!\s+(?!{ok}\b)[a-zà-úç])"


def pontuar(fx, corpo, mapa=None):
    f = BAT["fixtures"][fx]
    mapa = mapa or "".join(sorted(f["cenas"]))
    disp = {k: ROTULOS[i] for i, k in enumerate(mapa)}
    seq = rotulo_final(corpo, r"SEQU[ÊE]NCIA|SEQUENCE")
    if seq is None:
        return {"classe": "SEM-LINHA"}
    nota = rotulo_final(corpo, r"NOTAS?|NOTES?", ate_o_fim=True) or ""
    gs, extras = grupos(seq, mapa)
    presentes = set().union(*gs) if gs else set()
    r = [rel(gs, a, b) for a, b in f["antes"]]
    inv, semord, aus = r.count("invertido"), r.count("sem-ordem"), r.count("ausente")
    # [F5] cena do gabarito ausente não conta como ordem certa
    out = {"ordem": "ORDEM-CERTA" if inv == 0 and semord == 0 and aus == 0 else "ORDEM-ERRADA", "pares_invertidos": inv,
           "pares_sem_ordem": semord, "omitidas": "".join(sorted(set(f["cenas"]) - presentes)),
           "acrescentados": "; ".join(extras)[:80]}
    papel = f["papel"]
    out["nota_alarme"] = int(afirma(ALARME, nota))
    if papel in ("ordem", "controle-horario"):
        out["classe"] = "ALARME" if out["nota_alarme"] else "NOTA-LIMPA"
    elif papel == "fora-do-script":
        # o acerto é seguir o observado, sem omitir cena ([F5]); nota sobre o desvio é permitida (nota_alarme)
        out["classe"] = "SEGUE-OBSERVADO" if out["ordem"] == "ORDEM-CERTA" else "ORDEM-ERRADA"
    elif papel == "horario-errado":
        c1, c2 = f["conflito"]
        out["classe"] = "CONFLITO-APONTADO" if re.search(HORA, nota) and afirma(CONTRA, nota) else "CONFLITO-OMITIDO"
        out["segue_dependencia"] = rel(gs, c1, c2)
    elif papel == "lacuna":
        lrx = f["lacuna_rx"]
        # [F9] nomear o passo + marcador de lacuna afirmado ('não há cena do encaixe' aponta; não se nega o nome do passo)
        # [F10] item acrescentado com negação ('sem lacunas') não conta
        nomeia = (bool(re.search(lrx, nota)) and afirma(GAP, nota)) or any(
            re.search(lrx, e) or afirma(r"(?i)\?|falt|lacuna|inferid", e) for e in extras)
        out["classe"] = "LACUNA-APONTADA" if nomeia else "LACUNA-SILENCIOSA"
    elif papel == "intruso":
        x = f["intruso"]
        # [F8] citar o intruso só conta junto de uma marca de 'não pertence' (menção sozinha não é apontar)
        cita = re.search(f["intruso_rx"], nota) or cita_rotulo(disp[x], nota)
        aponta = x not in presentes or bool(cita and afirma(FORA, nota))
        out["classe"] = "INTRUSO-APONTADO" if aponta else "INTRUSO-INCLUIDO"
    elif papel == "incomparaveis":
        parent = " ".join(re.findall(r"\(([^)]*)\)", seq))
        texto = nota + ("\n" + seq if re.search(INDET_PAR, parent) else "")  # [F7] indeterminação dita na SEQUÊNCIA
        indet = afirma(INDET_PAR, texto) and not re.search(DENY_INDET, texto)
        decl = []
        for a, b in f["incomparaveis"]:
            ta, tb = disp[a], disp[b]
            xa = lab(ta) + ("|" + f["incomp_txt"][a] if "incomp_txt" in f else "")
            xb = lab(tb) + ("|" + f["incomp_txt"][b] if "incomp_txt" in f else "")
            perto = re.search(rf"(?:{xa}).{{0,80}}(?:{xb})|(?:{xb}).{{0,80}}(?:{xa})", texto, re.S)
            decl.append(rel(gs, a, b) == "sem-ordem" or bool(perto and indet))
        out["classe"] = "INCOMP-DECLARADO" if all(decl) else ("INCOMP-PARCIAL" if any(decl) else "INCOMP-FORCADO")
    return out


ACERTO = {"NOTA-LIMPA", "CONFLITO-APONTADO", "LACUNA-APONTADA", "INTRUSO-APONTADO", "INCOMP-DECLARADO", "SEGUE-OBSERVADO"}


def carregar(indir):
    rev = {}
    p = indir.rstrip("/\\") + "-revisao.csv"
    if os.path.exists(p):
        for row in csv.DictReader(open(p, encoding="utf-8")):
            rev[os.path.normpath(row["arquivo"])] = row["classe"]
    linhas = []
    for raiz, _, arqs in os.walk(indir):
        for fn in sorted(arqs):
            if not fn.endswith(".md"):
                continue
            caminho = os.path.join(raiz, fn)
            t = open(caminho, encoding="utf-8").read()
            h = HDR.search(t)
            if not h:
                continue
            r = pontuar(h["fx"], t[h.end():], h["mapa"])
            cab = t[h.start():].split("-->", 1)[0]
            stop = re.search(r"\| stop=(\w+)", cab)
            campo = lambda k: (re.search(rf"\| {k}=(.*?)(?= \| |\s*$)", cab) or [None, ""])[1]  # noqa: E731
            # desvio 2026-09-30 (PREREG §9): cortada por tamanho = não terminou; o que se lê é rascunho -> SEM-LINHA
            corte = bool(stop) and stop.group(1) == "length"
            rel_path = os.path.normpath(os.path.relpath(caminho, indir))
            fx = BAT["fixtures"][h["fx"]]
            linhas.append({"arquivo": rel_path, "fixture": h["fx"], "familia": fx["familia"], "dominio": fx["dominio"],
                           "arm": h["arm"], "perm": h["perm"], "model": h["model"], "run": h["run"], "stop": stop.group(1) if stop else "",
                           "provedor": campo("provider"), "rota": campo("rota"), "ft": campo("ft"),
                           "classe": "SEM-LINHA" if corte else rev.get(rel_path, r["classe"]), "classe_auto": r["classe"],
                           "ordem": "" if corte else r.get("ordem", ""),
                           "pares_invertidos": r.get("pares_invertidos", ""), "omitidas": r.get("omitidas", ""),
                           "acrescentados": r.get("acrescentados", ""), "segue_dependencia": r.get("segue_dependencia", ""), "nota_alarme": r.get("nota_alarme", "")})
    return linhas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("indir")
    ap.add_argument("--csv", default=None)
    a = ap.parse_args()
    linhas = carregar(a.indir)
    if a.csv and linhas:
        with open(a.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(linhas[0].keys()))
            w.writeheader()
            w.writerows(linhas)
    g = collections.defaultdict(list)
    for r in linhas:
        g[(r["familia"], r["dominio"], r["arm"])].append(r)
    print("| família | domínio | braço | ordem certa | acerto da nota | sem linha |")
    print("|---|---|---|---|---|---|")
    for (fam, dom, arm), rs in sorted(g.items()):
        v = [r for r in rs if r["classe"] != "SEM-LINHA"]
        oc = sum(r["ordem"] == "ORDEM-CERTA" for r in v)
        na = sum(r["classe"] in ACERTO for r in v)
        print(f"| {fam} | {dom} | {arm} | {oc}/{len(v)} | {na}/{len(v)} | {len(rs) - len(v)} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
