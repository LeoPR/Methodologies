#!/usr/bin/env python3
"""Análise pré-registrada da bateria de temporalidade (lab/2026-09-26-temporalidade/PREREG-bateria-v1.md §4-§5; v2:
PREREG-bateria-v2.md).

Lê as saídas pelo score_tb (com a revisão manual, se houver) e reporta, por família × braço:
acerto (k/K), consistência, efeito de apresentação, SEM-LINHA; H1 (protocolo − ingênuo na nota, IC 95%
por bootstrap de modelos) e H2 (alarme falso e ordem nos controles T1 + T2c).
v2: com o braço placebo, H3 (protocolo − placebo, mesmo critério do H1); com --etapa A, a decisão de parada da Etapa A
(H2 e o critério do H1 no T3).
Uso: python analise_tb.py planos/tb-v1 [--sensibilidade] [--etapa A]   (sensibilidade: SEM-LINHA conta como falha)
"""
import argparse
import collections
import random
import sys

import score_tb as S

SEMENTE, REAMOSTRAS = 20260930, 2000
FAM_H1 = ["T2", "T3", "T4", "T5"]
BRACOS = ["ingenuo", "protocolo", "placebo"]


def taxa(rs, ok):
    return (sum(ok(r) for r in rs), len(rs))


def fmt(k, n):
    return f"{k}/{n} ({k / n:.2f})" if n else "—"


def diff_boot(linhas, fam_filtro, ok, rng, a="protocolo", b="ingenuo"):
    """Diferença a − b (padrão: protocolo − ingênuo) e IC 95% reamostrando modelos (cluster)."""
    por_modelo = collections.defaultdict(lambda: {a: [0, 0], b: [0, 0]})
    for r in linhas:
        if fam_filtro(r) and r["arm"] in (a, b):
            c = por_modelo[r["model"]][r["arm"]]
            c[0] += ok(r)
            c[1] += 1
    modelos = sorted(por_modelo)

    def d(ms):
        s = {x: [sum(por_modelo[m][x][0] for m in ms), sum(por_modelo[m][x][1] for m in ms)] for x in (b, a)}
        if not s[b][1] or not s[a][1]:
            return None
        return s[a][0] / s[a][1] - s[b][0] / s[b][1], s
    base = d(modelos)
    if base is None:
        return None
    boots = []
    for _ in range(REAMOSTRAS):
        x = d([rng.choice(modelos) for _ in modelos])
        if x is not None:
            boots.append(x[0])
    boots.sort()
    return base[0], boots[int(0.025 * len(boots))], boots[int(0.975 * len(boots)) - 1], base[1], len(modelos)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("indir")
    ap.add_argument("--sensibilidade", action="store_true")
    ap.add_argument("--etapa", choices=["A"], default=None, help="v2: decisão de parada da Etapa A")
    a = ap.parse_args()
    todas = S.carregar(a.indir)
    if a.etapa == "A":
        # o placebo do T3 roda na Etapa A, mas fica selado até a Etapa B (PREREG v2 §5)
        todas = [r for r in todas if r["arm"] != "placebo"]
    sem = [r for r in todas if r["classe"] == "SEM-LINHA"]
    linhas = todas if a.sensibilidade else [r for r in todas if r["classe"] != "SEM-LINHA"]
    acerto = lambda r: r["classe"] in S.ACERTO  # noqa: E731
    ordem = lambda r: r["ordem"] == "ORDEM-CERTA"  # noqa: E731
    # na sensibilidade, SEM-LINHA conta como falha em TODAS as métricas (no alarme falso, como alarme)
    alarme = lambda r: r["classe"] == "ALARME" or (a.sensibilidade and r["classe"] == "SEM-LINHA")  # noqa: E731
    rng = random.Random(SEMENTE)
    v2 = S.BATERIA_NOME != "bateria-v1.json"

    def rng_de(tag):
        # v2: uma semente por comparação (o IC não muda com a ordem ou o número de comparações); v1: a sequência original
        return random.Random(f"{SEMENTE}:{tag}") if v2 else rng
    bracos = [b for b in BRACOS if any(r["arm"] == b for r in todas)]

    print(f"# Bateria {S.BATERIA_NOME.replace('bateria-', '').replace('.json', '')}: {a.indir} ({'sensibilidade: SEM-LINHA = falha' if a.sensibilidade else 'SEM-LINHA fora'})\n")
    print(f"Saídas: {len(todas)}; SEM-LINHA: {len(sem)} "
          f"(corte por tamanho {sum(r['stop'] == 'length' for r in sem)}; por braço "
          + ", ".join(f"{b} {sum(r['arm'] == b for r in sem)}" for b in bracos) + ")")
    ft1 = [r for r in todas if r["ft"] == "1"]
    print(f"Resposta tirada do canal de raciocínio (ft=1): {len(ft1)}"
          + (" (" + ", ".join(f"{b} {sum(r['arm'] == b for r in ft1)}" for b in bracos) + ")" if ft1 else ""))
    for m in sorted({r["model"] for r in todas}):
        rotas = {r["rota"] or "-" for r in todas if r["model"] == m}
        provs = {r["provedor"] for r in todas if r["model"] == m}
        if len(rotas) > 1 or len({p.split("/")[0] for p in provs}) > 1:
            print(f"AVISO: {m} mistura rotas {sorted(rotas)} ou provedores {sorted(provs)}")
    tetos = {r["max"] for r in todas}
    if len(tetos) > 1:
        print(f"AVISO: tetos de saída misturados {sorted(tetos)}: a leitura não vale (PREREG v2 §9)")
    print()

    print("## Acerto por família × domínio × braço\n")
    print("| família | domínio | braço | acerto (nota/papel) | ordem certa | apres. 0 | apres. 1 | consistência |")
    print("|---|---|---|---|---|---|---|---|")
    g = collections.defaultdict(list)
    for r in linhas:
        g[(r["familia"], r["dominio"], r["arm"])].append(r)
    for (fam, dom, arm), rs in sorted(g.items()):
        cel = collections.defaultdict(set)
        for r in rs:
            cel[(r["model"], r["fixture"])].add(r["classe"])
        cons = sum(len(v) == 1 for v in cel.values())
        p0 = [r for r in rs if r["perm"] == "0"]
        p1 = [r for r in rs if r["perm"] == "1"]
        print(f"| {fam} | {dom} | {arm} | {fmt(*taxa(rs, acerto))} | {fmt(*taxa(rs, ordem))} | "
              f"{fmt(*taxa(p0, acerto))} | {fmt(*taxa(p1, acerto))} | {fmt(cons, len(cel))} |")

    print("\n## H1: protocolo − ingênuo no acerto da nota (IC 95%, bootstrap por modelo)\n")
    print("| família | ingênuo | protocolo | diferença | IC 95% | teto (ingênuo ≥ 0,90) | critério |")
    print("|---|---|---|---|---|---|---|")
    ok_fams, avaliadas = 0, 0
    t3_cumpre = None
    for fam in FAM_H1:
        x = diff_boot(linhas, lambda r, f=fam: r["familia"] == f, acerto, rng_de(f"H1:{fam}"))
        if x is None:
            print(f"| {fam} | — | — | — | — | — | — |")
            continue
        dlt, lo, hi, s, nm = x
        ing = s["ingenuo"][0] / s["ingenuo"][1]
        teto = ing >= 0.90
        crit = (not teto) and dlt >= 0.15 and lo > 0
        if not teto:
            avaliadas += 1
            ok_fams += crit
        if fam == "T3":
            t3_cumpre = crit or teto
        print(f"| {fam} | {fmt(*s['ingenuo'])} | {fmt(*s['protocolo'])} | {dlt:+.2f} | [{lo:+.2f}, {hi:+.2f}] | "
              f"{'sim' if teto else 'não'} | {'cumpre' if crit else ('sem poder (teto)' if teto else 'não cumpre')} |")
    if avaliadas == 4:
        h1 = ok_fams >= 3
    else:
        h1 = avaliadas > 0 and ok_fams > avaliadas / 2
    if a.etapa != "A":
        print(f"\nH1: {ok_fams} de {avaliadas} famílias avaliáveis cumprem → {'VALE' if h1 else 'NÃO VALE'}\n")
    else:
        print("\n(Etapa A: o H1 só se decide na Etapa B; aqui vale o critério no T3.)\n")

    print("## H2: controles T1 + T2c (não inferioridade, margem 0,10)\n")
    ctrl = [r for r in linhas if r["familia"] in ("T1", "T2c")]
    res = {}
    for nome, ok, sinal in (("alarme falso", alarme, +1), ("ordem certa", ordem, -1)):
        x = diff_boot(ctrl, lambda r: True, ok, rng_de(f"H2:{nome}"))
        dlt, lo, hi, s, _ = x
        viola = dlt > 0.10 if sinal > 0 else dlt < -0.10
        res[nome] = viola
        print(f"- {nome}: ingênuo {fmt(*s['ingenuo'])}, protocolo {fmt(*s['protocolo'])}, diferença {dlt:+.2f} "
              f"[{lo:+.2f}, {hi:+.2f}] → {'VIOLA' if viola else 'dentro da margem'}")
    print(f"\nH2: {'VIOLADA' if any(res.values()) else 'VALE'}\n")
    if a.etapa == "A":
        h2 = not any(res.values())
        dec = ("PARA: H2 violada" if not h2 else
               "PARA: H2 vale, mas o T3 perdeu o ganho" if not t3_cumpre else "SEGUE para a Etapa B")
        print(f"## Decisão da Etapa A (PREREG v2): H2 {'vale' if h2 else 'violada'}; "
              f"T3 {'cumpre' if t3_cumpre else 'não cumpre'} → {dec}\n")

    if "placebo" in bracos:
        # checagem de manipulação (PREREG v2 §7): se o placebo cala a nota (mais 'nenhuma' que o ingênuo + 0,10),
        # o H3 não se interpreta naquela família
        import revisao_tb as R
        txt = {r["arquivo"]: r["nota_txt"] for r in R.linhas_com_texto(a.indir)}
        cala = {}
        print("## Checagem de manipulação do placebo (nota 'nenhuma')\n")
        for fam in FAM_H1:
            fr = {}
            for b_ in ("ingenuo", "placebo"):
                rs = [r for r in linhas if r["familia"] == fam and r["arm"] == b_]
                fr[b_] = sum(bool(R.TRIVIAL.match(txt.get(r["arquivo"], ""))) for r in rs) / len(rs) if rs else None
            cala[fam] = None not in fr.values() and fr["placebo"] > fr["ingenuo"] + 0.10
            if None not in fr.values():
                print(f"- {fam}: ingênuo {fr['ingenuo']:.2f}, placebo {fr['placebo']:.2f}"
                      + (" → H3 não interpretável nesta família" if cala[fam] else ""))
        print()
        print("## H3: protocolo − placebo no acerto da nota (IC 95%, bootstrap por modelo)\n")
        print("| família | placebo | protocolo | diferença | IC 95% | teto (placebo ≥ 0,90) | critério |")
        print("|---|---|---|---|---|---|---|")
        ok3, aval3 = 0, 0
        for fam in FAM_H1:
            x = diff_boot(linhas, lambda r, f=fam: r["familia"] == f, acerto, rng_de(f"H3:{fam}"), a="protocolo", b="placebo")
            if x is None:
                print(f"| {fam} | — | — | — | — | — | — |")
                continue
            dlt, lo, hi, s, nm = x
            teto = s["placebo"][0] / s["placebo"][1] >= 0.90
            crit = (not teto) and (not cala.get(fam)) and dlt >= 0.15 and lo > 0
            if not teto and not cala.get(fam):
                aval3 += 1
                ok3 += crit
            situ = "cumpre" if crit else ("sem poder (teto)" if teto else ("não interpretável" if cala.get(fam) else "não cumpre"))
            print(f"| {fam} | {fmt(*s['placebo'])} | {fmt(*s['protocolo'])} | {dlt:+.2f} | [{lo:+.2f}, {hi:+.2f}] | "
                  f"{'sim' if teto else 'não'} | {situ} |")
        h3 = ok3 >= 3 if aval3 == 4 else (aval3 > 0 and ok3 > aval3 / 2)
        veredito = "SEM PODER (nenhuma família avaliável)" if aval3 == 0 else ("VALE" if h3 else "NÃO VALE")
        print(f"\nH3: {ok3} de {aval3} famílias avaliáveis cumprem → {veredito}\n")
        print("Descritivo (sem decisão): placebo − ingênuo por família\n")
        for fam in FAM_H1:
            x = diff_boot(linhas, lambda r, f=fam: r["familia"] == f, acerto, rng_de(f"PI:{fam}"), a="placebo", b="ingenuo")
            if x:
                print(f"- {fam}: {x[0]:+.2f} [{x[1]:+.2f}, {x[2]:+.2f}]")
        print()

    print("## Por modelo (acerto da nota nas famílias T2–T5; alarme falso em T1 + T2c)\n")
    print("| modelo | ingênuo T2–T5 | protocolo T2–T5 | alarme ingênuo | alarme protocolo | SEM-LINHA |")
    print("|---|---|---|---|---|---|")
    for m in sorted({r["model"] for r in todas}):
        rs = [r for r in linhas if r["model"] == m]
        f = lambda arm, fams, ok: fmt(*taxa([r for r in rs if r["arm"] == arm and r["familia"] in fams], ok))  # noqa: E731
        print(f"| {m} | {f('ingenuo', FAM_H1, acerto)} | {f('protocolo', FAM_H1, acerto)} | "
              f"{f('ingenuo', ('T1', 'T2c'), alarme)} | {f('protocolo', ('T1', 'T2c'), alarme)} | "
              f"{sum(r['model'] == m for r in sem)} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
