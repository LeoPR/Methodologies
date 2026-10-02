#!/usr/bin/env python3
"""
perfil_interativo.py: instrumento do M2a (ver M2A.md, desenho fixado antes dos números).

Lê os transcripts do Claude Code (~/.claude/projects/**/*.jsonl) READ-ONLY e, só com metadados
(modelo, tokens, nome de ferramenta, caminho de arquivo editado), monta:
  - turnos (pedido humano -> próximo pedido), com as chamadas da linha principal e as dos subagentes
    da mesma sessão no intervalo do turno;
  - a classe de cada turno (C1 pergunta, C2 investigação ou ação por shell, C3 edição pontual,
    C4 multi-arquivo);
  - o custo do mesmo perfil de tokens em cada rota (precos-2026-10-01.json).

Dedup por message.id para o uso (uma resposta aparece em várias linhas); os blocos tool_use são
lidos em todas as linhas (cada linha pode trazer um bloco diferente da mesma resposta).

Não faz chamada de API. Nenhum conteúdo de conversa é gravado: a saída por turno (CSV) tem só
números e o id da sessão. É derivada e regenerável, então fica fora do repositório (e do OneDrive): na
pasta de COMPORTA_SAIDA, ou na pasta temporária do sistema.

Uso:
    python perfil_interativo.py                      # janela até 2026-10-01T00:00Z
    python perfil_interativo.py --until 2026-11-01T00:00:00Z --out-dir <pasta fora do repositório>
"""
from __future__ import annotations

import argparse
import bisect
import csv
import glob
import json
import os
import re
import statistics
import tempfile
from collections import Counter, defaultdict

AQUI = os.path.dirname(os.path.abspath(__file__))
EDICAO = {"Edit", "Write", "MultiEdit", "NotebookEdit"}
SHELL = {"Bash", "PowerShell"}
CLASSES = ["C1", "C2", "C3", "C4"]
NOME_CLASSE = {"C1": "pergunta", "C2": "investigação ou ação por shell",
               "C3": "edição pontual", "C4": "multi-arquivo"}


def chave_modelo(m: str) -> str:
    return re.sub(r"-\d{8}$", "", m or "")


def campos(u: dict):
    """(entrada, leitura, escrita5m, escrita1h, saída) de um registro de uso."""
    cc = u.get("cache_creation") or {}
    w5 = cc.get("ephemeral_5m_input_tokens") or 0
    w1 = cc.get("ephemeral_1h_input_tokens") or 0
    tot = u.get("cache_creation_input_tokens") or 0
    if w5 + w1 < tot:  # split ausente ou incompleto: o resto conta como 5 min
        w5 += tot - w5 - w1
    return (u.get("input_tokens") or 0, u.get("cache_read_input_tokens") or 0, w5, w1,
            u.get("output_tokens") or 0)


def custo(f, p, w1_como_w5=False):
    i, r, w5, w1, o = f
    t1 = p["w5m"] if w1_como_w5 else p["w1h"]
    return (i * p["in"] + r * p["read"] + w5 * p["w5m"] + w1 * t1 + o * p["out"]) / 1e6


def eh_pedido(d: dict) -> bool:
    if d.get("type") != "user" or d.get("isMeta") or d.get("isCompactSummary") or d.get("isSidechain"):
        return False
    if d.get("toolUseResult") is not None:
        return False
    c = (d.get("message") or {}).get("content")
    if isinstance(c, str):
        s = c.lstrip()
        return bool(s) and not s.startswith("<local-command")
    if isinstance(c, list):
        tipos = {b.get("type") for b in c if isinstance(b, dict)}
        return bool(tipos) and "tool_result" not in tipos
    return False


def linhas(path):
    with open(path, encoding="utf-8", errors="replace") as fh:
        for ln in fh:
            ln = ln.strip()
            if not ln:
                continue
            try:
                yield json.loads(ln)
            except json.JSONDecodeError:
                continue


def pct(xs, q):
    if not xs:
        return 0
    xs = sorted(xs)
    k = max(0, min(len(xs) - 1, int(round(q * (len(xs) - 1)))))
    return xs[k]


def main(argv=None):
    ap = argparse.ArgumentParser(description="Perfil de tokens do uso interativo (M2a).")
    ap.add_argument("--base", default=os.path.join(os.path.expanduser("~"), ".claude", "projects"))
    ap.add_argument("--until", default="2026-10-01T00:00:00Z")
    ap.add_argument("--precos", default=os.path.join(AQUI, "precos-2026-10-01.json"))
    ap.add_argument("--out-dir", default=os.environ.get("COMPORTA_SAIDA")
                    or os.path.join(tempfile.gettempdir(), "comporta-m2a"))
    a = ap.parse_args(argv)

    P = json.load(open(a.precos, encoding="utf-8"))
    PM, LOCAL = P["modelos"], P["local_rtx3060"]
    plano = P["planos"]["copilot_pro_plus"]

    vistos = set()            # message.id já contado
    blocos_vistos = set()     # tool_use.id já contado
    turnos = defaultdict(list)  # sessão -> [turno]
    sub_por_sessao = defaultdict(list)  # sessão -> [(ts, campos, modelo)]
    chamadas = []             # todas as chamadas deduplicadas: (ts, modelo, campos)
    desconhecidos = Counter()
    sinteticos = 0

    arquivos = glob.glob(os.path.join(a.base, "**", "*.jsonl"), recursive=True)
    principais = [f for f in arquivos if "/subagents/" not in f.replace("\\", "/")]
    subagentes = [f for f in arquivos if "/subagents/" in f.replace("\\", "/")]

    def registra(d, m):
        """Conta o uso uma vez por message.id. Devolve (ts, modelo, campos) ou None."""
        nonlocal sinteticos
        u, mid, ts = m.get("usage"), m.get("id"), d.get("timestamp")
        if not isinstance(u, dict) or not mid or not ts or ts >= a.until or mid in vistos:
            return None
        vistos.add(mid)
        mod = chave_modelo(m.get("model"))
        if mod == "<synthetic>":
            sinteticos += 1
            return None
        if mod not in PM:
            desconhecidos[mod] += 1
        c = (ts, mod, campos(u))
        chamadas.append(c)
        return c

    for path in principais:
        sid = os.path.splitext(os.path.basename(path))[0]
        atual = None
        for d in linhas(path):
            ts = d.get("timestamp")
            if eh_pedido(d):
                if ts and ts < a.until:
                    atual = dict(sid=sid, ini=ts, main=[], sub=[], tools=Counter(), arqs=set())
                    turnos[sid].append(atual)
                else:
                    atual = None
                continue
            m = d.get("message")
            if d.get("type") != "assistant" or not isinstance(m, dict):
                continue
            if d.get("isSidechain"):
                c = registra(d, m)
                if c:
                    sub_por_sessao[sid].append(c)
                continue
            c = registra(d, m)
            if atual is None:
                continue
            if c:
                atual["main"].append(c)
            for b in m.get("content") or []:
                if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("id") not in blocos_vistos:
                    blocos_vistos.add(b.get("id"))
                    nome = b.get("name")
                    atual["tools"][nome] += 1
                    if nome in EDICAO:
                        inp = b.get("input") or {}
                        fp = inp.get("file_path") or inp.get("notebook_path")
                        if fp:
                            atual["arqs"].add(fp.replace("\\", "/").lower())

    for path in subagentes:
        sid = path.replace("\\", "/").split("/")[-3]
        for d in linhas(path):
            m = d.get("message")
            if d.get("type") == "assistant" and isinstance(m, dict):
                c = registra(d, m)
                if c:
                    sub_por_sessao[sid].append(c)

    # subagente -> turno da mesma sessão pelo horário
    sem_turno = []
    for sid, subs in sub_por_sessao.items():
        ts_list = turnos.get(sid, [])
        inicios = [t["ini"] for t in ts_list]
        for c in subs:
            k = bisect.bisect_right(inicios, c[0]) - 1
            if k >= 0:
                ts_list[k]["sub"].append(c)
            else:
                sem_turno.append(c)

    def custo_de(cs, rota):
        tot = 0.0
        for _, mod, f in cs:
            if rota == "api":
                p = PM.get(mod)
                tot += custo(f, p) if p else 0.0
            elif rota == "copilot":
                p = PM.get(mod)
                tot += custo(f, p, w1_como_w5=True) if p else 0.0
            else:
                tot += custo(f, PM[rota], w1_como_w5=True)
        return tot

    # ---- por turno
    linhas_turno = []
    for sid, ts_list in turnos.items():
        for t in ts_list:
            todas = t["main"] + t["sub"]
            if not t["main"]:
                continue
            n_arq = len(t["arqs"])
            if n_arq >= 2:
                cls = "C4"
            elif n_arq == 1:
                cls = "C3"
            elif len(t["main"]) >= 3:
                cls = "C2"
            else:
                cls = "C1"
            ctx = max(f[0] + f[1] + f[2] + f[3] for _, _, f in todas)
            out = sum(f[4] for _, _, f in todas)
            mod = Counter(m for _, m, _ in t["main"]).most_common(1)[0][0]
            linhas_turno.append(dict(
                sessao=sid, mes=t["ini"][:7], inicio=t["ini"], classe=cls, modelo=mod,
                n_main=len(t["main"]), n_sub=len(t["sub"]), n_arquivos=n_arq,
                n_shell=sum(t["tools"][s] for s in SHELL), ctx_max=ctx, saida=out,
                custo_api=round(custo_de(todas, "api"), 6),
                custo_copilot=round(custo_de(todas, "copilot"), 6),
                custo_sonnet55=round(custo_de(todas, "claude-sonnet-5-5"), 6),
                custo_haiku45=round(custo_de(todas, "claude-haiku-4-5"), 6),
                cabe_8k=ctx <= 8192, cabe_32k=ctx <= LOCAL["cabe_ctx"]))

    os.makedirs(a.out_dir, exist_ok=True)
    with open(os.path.join(a.out_dir, "turnos.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(linhas_turno[0].keys()))
        w.writeheader()
        w.writerows(sorted(linhas_turno, key=lambda r: r["inicio"]))

    out = []
    pr = out.append
    pr(f"# M2a: resumo (janela até {a.until}; preços verificados em {P['verificado_em']})\n")
    pr(f"- Arquivos: {len(principais)} sessões principais, {len(subagentes)} de subagente.")
    pr(f"- Chamadas deduplicadas: {len(chamadas)}; sintéticas fora: {sinteticos}; "
       f"modelos sem preço: {dict(desconhecidos) or 'nenhum'}.")
    pr(f"- Turnos com chamada: {len(linhas_turno)}; chamadas de subagente sem turno (sessão sem "
       f"transcript principal ou antes do 1º pedido): {len(sem_turno)}, "
       f"custo API ${custo_de(sem_turno, 'api'):,.2f}.\n")

    # ---- por mês
    por_mes = defaultdict(list)
    for c in chamadas:
        por_mes[c[0][:7]].append(c)
    pr("## Por mês (todas as chamadas, inclusive subagentes)\n")
    pr("| mês | chamadas | entrada | leitura de cache | escrita de cache | saída | API (US$) | "
       "Copilot por token (US$) | plano Pro+ (US$) | mesmo perfil no Sonnet 5.5 (US$) | "
       "no Haiku 4.5 (US$) |")
    pr("|---|---|---|---|---|---|---|---|---|---|---|")
    for mes in sorted(por_mes):
        cs = por_mes[mes]
        soma = [sum(f[k] for _, _, f in cs) for k in range(5)]
        cop = custo_de(cs, "copilot")
        plano_custo = plano["preco_mes"] + max(0.0, cop - plano["creditos_inclusos_usd"])
        pr(f"| {mes} | {len(cs):,} | {soma[0]:,} | {soma[1]:,} | {soma[2] + soma[3]:,} | {soma[4]:,} | "
           f"{custo_de(cs, 'api'):,.0f} | {cop:,.0f} | {plano_custo:,.0f} | "
           f"{custo_de(cs, 'claude-sonnet-5-5'):,.0f} | {custo_de(cs, 'claude-haiku-4-5'):,.0f} |")

    # ---- composição do custo (API)
    comp = [0.0] * 5
    for _, mod, f in chamadas:
        p = PM.get(mod)
        if not p:
            continue
        comp[0] += f[0] * p["in"]; comp[1] += f[1] * p["read"]; comp[2] += f[2] * p["w5m"]
        comp[3] += f[3] * p["w1h"]; comp[4] += f[4] * p["out"]
    tot = sum(comp) or 1
    pr("\n## Composição do custo na API (janela inteira)\n")
    pr("| entrada | leitura de cache | escrita 5 min | escrita 1 h | saída |")
    pr("|---|---|---|---|---|")
    pr("| " + " | ".join(f"{100 * x / tot:.0f}%" for x in comp) + " |")

    # ---- por modelo
    pm = Counter()
    for c in chamadas:
        pm[c[1]] += custo_de([c], "api")
    tot_m = sum(pm.values()) or 1
    pr("\n## Parte do custo na API por modelo (janela inteira)\n")
    pr("| modelo | parte |")
    pr("|---|---|")
    for mod, v in pm.most_common():
        pr(f"| {mod} | {100 * v / tot_m:.1f}% |")

    # ---- por classe
    def bloco(titulo, rows):
        pr(f"\n## Por classe de turno: {titulo}\n")
        pr("| classe | turnos | chamadas (mediana / p90) | contexto máx. (mediana / p90) | "
           "saída (mediana / p90) | custo API por turno (mediana / p90 / média, US$) | "
           "parte do custo | com subagente | cabe em 8k | cabe em 32k |")
        pr("|---|---|---|---|---|---|---|---|---|---|")
        tot_c = sum(r["custo_api"] for r in rows) or 1
        for cls in CLASSES:
            rs = [r for r in rows if r["classe"] == cls]
            if not rs:
                continue
            n = len(rs)
            ch = [r["n_main"] + r["n_sub"] for r in rs]
            cx = [r["ctx_max"] for r in rs]
            sa = [r["saida"] for r in rs]
            cu = [r["custo_api"] for r in rs]
            pr(f"| {cls} {NOME_CLASSE[cls]} | {n} | {pct(ch, .5)} / {pct(ch, .9)} | "
               f"{pct(cx, .5):,} / {pct(cx, .9):,} | {pct(sa, .5):,} / {pct(sa, .9):,} | "
               f"{pct(cu, .5):.2f} / {pct(cu, .9):.2f} / {statistics.mean(cu):.2f} | "
               f"{100 * sum(cu) / tot_c:.0f}% | {100 * sum(r['n_sub'] > 0 for r in rs) / n:.0f}% | "
               f"{100 * sum(r['cabe_8k'] for r in rs) / n:.0f}% | "
               f"{100 * sum(r['cabe_32k'] for r in rs) / n:.0f}% |")

    bloco("janela inteira", linhas_turno)
    ref = [r for r in linhas_turno if r["mes"] == "2026-09"]
    if ref:
        bloco("setembro de 2026 (mês de referência)", ref)

    cabem = [r for r in linhas_turno if r["cabe_32k"]]
    if cabem:
        seg = [r["saida"] / LOCAL["decode_tps"] for r in cabem]
        pr(f"\nLocal ({LOCAL['modelo_ref']}, RTX 3060): {len(cabem)} turnos cabem em 32k; só o decode da "
           f"saída levaria, na mediana, {pct(seg, .5):.0f} s (p90 {pct(seg, .9):.0f} s), sem contar o prefill.")

    txt = "\n".join(out) + "\n"
    with open(os.path.join(a.out_dir, "resumo.md"), "w", encoding="utf-8") as fh:
        fh.write(txt)
    print(txt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
