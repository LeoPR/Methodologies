#!/usr/bin/env python3
"""Análise pré-registrada da bateria de temporalidade v1 (lab/2026-09-26-temporalidade/PREREG-bateria-v1.md §4-§5).

Lê as saídas pelo score_tb (com a revisão manual, se houver) e reporta, por família × braço:
acerto (k/K), consistência, efeito de apresentação, SEM-LINHA; H1 (protocolo − ingênuo na nota, IC 95%
por bootstrap de modelos) e H2 (alarme falso e ordem nos controles T1 + T2c).
Uso: python analise_tb.py planos/tb-v1 [--sensibilidade]   (sensibilidade: SEM-LINHA conta como falha)
"""
import argparse
import collections
import random
import sys

import score_tb as S

SEMENTE, REAMOSTRAS = 20260930, 2000
FAM_H1 = ["T2", "T3", "T4", "T5"]


def taxa(rs, ok):
    return (sum(ok(r) for r in rs), len(rs))


def fmt(k, n):
    return f"{k}/{n} ({k / n:.2f})" if n else "—"


def diff_boot(linhas, fam_filtro, ok, rng):
    """Diferença protocolo − ingênuo e IC 95% reamostrando modelos (cluster)."""
    por_modelo = collections.defaultdict(lambda: {"ingenuo": [0, 0], "protocolo": [0, 0]})
    for r in linhas:
        if fam_filtro(r):
            c = por_modelo[r["model"]][r["arm"]]
            c[0] += ok(r)
            c[1] += 1
    modelos = sorted(por_modelo)

    def d(ms):
        s = {a: [sum(por_modelo[m][a][0] for m in ms), sum(por_modelo[m][a][1] for m in ms)] for a in ("ingenuo", "protocolo")}
        if not s["ingenuo"][1] or not s["protocolo"][1]:
            return None
        return s["protocolo"][0] / s["protocolo"][1] - s["ingenuo"][0] / s["ingenuo"][1], s
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
    a = ap.parse_args()
    todas = S.carregar(a.indir)
    sem = [r for r in todas if r["classe"] == "SEM-LINHA"]
    linhas = todas if a.sensibilidade else [r for r in todas if r["classe"] != "SEM-LINHA"]
    acerto = lambda r: r["classe"] in S.ACERTO  # noqa: E731
    ordem = lambda r: r["ordem"] == "ORDEM-CERTA"  # noqa: E731
    # na sensibilidade, SEM-LINHA conta como falha em TODAS as métricas (no alarme falso, como alarme)
    alarme = lambda r: r["classe"] == "ALARME" or (a.sensibilidade and r["classe"] == "SEM-LINHA")  # noqa: E731
    rng = random.Random(SEMENTE)

    print(f"# Bateria v1: {a.indir} ({'sensibilidade: SEM-LINHA = falha' if a.sensibilidade else 'SEM-LINHA fora'})\n")
    print(f"Saídas: {len(todas)}; SEM-LINHA: {len(sem)} "
          f"(corte por tamanho {sum(r['stop'] == 'length' for r in sem)}; por braço "
          + ", ".join(f"{b} {sum(r['arm'] == b for r in sem)}" for b in ("ingenuo", "protocolo")) + ")")
    ft1 = [r for r in todas if r["ft"] == "1"]
    print(f"Resposta tirada do canal de raciocínio (ft=1): {len(ft1)}"
          + (" (" + ", ".join(f"{b} {sum(r['arm'] == b for r in ft1)}" for b in ("ingenuo", "protocolo")) + ")" if ft1 else ""))
    for m in sorted({r["model"] for r in todas}):
        rotas = {r["rota"] or "-" for r in todas if r["model"] == m}
        provs = {r["provedor"] for r in todas if r["model"] == m}
        if len(rotas) > 1 or len({p.split("/")[0] for p in provs}) > 1:
            print(f"AVISO: {m} mistura rotas {sorted(rotas)} ou provedores {sorted(provs)}")
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
    for fam in FAM_H1:
        x = diff_boot(linhas, lambda r, f=fam: r["familia"] == f, acerto, rng)
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
        print(f"| {fam} | {fmt(*s['ingenuo'])} | {fmt(*s['protocolo'])} | {dlt:+.2f} | [{lo:+.2f}, {hi:+.2f}] | "
              f"{'sim' if teto else 'não'} | {'cumpre' if crit else ('sem poder (teto)' if teto else 'não cumpre')} |")
    if avaliadas == 4:
        h1 = ok_fams >= 3
    else:
        h1 = avaliadas > 0 and ok_fams > avaliadas / 2
    print(f"\nH1: {ok_fams} de {avaliadas} famílias avaliáveis cumprem → {'VALE' if h1 else 'NÃO VALE'}\n")

    print("## H2: controles T1 + T2c (não inferioridade, margem 0,10)\n")
    ctrl = [r for r in linhas if r["familia"] in ("T1", "T2c")]
    res = {}
    for nome, ok, sinal in (("alarme falso", alarme, +1), ("ordem certa", ordem, -1)):
        x = diff_boot(ctrl, lambda r: True, ok, rng)
        dlt, lo, hi, s, _ = x
        viola = dlt > 0.10 if sinal > 0 else dlt < -0.10
        res[nome] = viola
        print(f"- {nome}: ingênuo {fmt(*s['ingenuo'])}, protocolo {fmt(*s['protocolo'])}, diferença {dlt:+.2f} "
              f"[{lo:+.2f}, {hi:+.2f}] → {'VIOLA' if viola else 'dentro da margem'}")
    print(f"\nH2: {'VIOLADA' if any(res.values()) else 'VALE'}\n")

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
