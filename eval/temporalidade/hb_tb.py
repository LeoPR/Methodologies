#!/usr/bin/env python3
"""Bateria de temporalidade v1: o leitor reconstrói a ordem por dependência, nota a lacuna, o intruso e o
horário errado, e não inventa ordem onde não há?

Fixtures e gabarito em bateria-v1.json (cenas com letra interna; ordem de apresentação fixa por fixture).
O modelo vê as cenas rotuladas A, B, C... na ordem em que aparecem, não a letra interna (a letra denunciaria
a lacuna e o intruso); o cabeçalho grava mapa=<letras internas na ordem de apresentação>.
Braços (--arm): 'ingenuo' (só a tarefa), 'protocolo' (protocolo curto derivado da ONTOLOGIA v0) e, da v2 em diante,
'placebo' (orientações neutras de mesmo comprimento que o protocolo).
Bateria (--bateria, padrão bateria-v1.json): um rótulo usa uma bateria só; a escolha fica em planos/<label>/BATERIA.txt
(o pontuador a lê de lá) e, fora da v1, também no cabeçalho (bat=).
Reaproveita a chamada ao provedor de eval/strata/core (hb_runner.call_ex). Saída em
<raiz>/<label>/<fixture>/<braço>/p<apresentação>/<modelo>-r<run>.md, com cabeçalho rastreável. A raiz é a variável
TB_PLANOS (saídas de execução ficam fora de pasta sincronizada; ex.: Z:\\outputs\\Methodologies\\temporalidade);
sem ela, planos/ ao lado deste arquivo (o lugar da v1).
Teto de saída: --num-predict; sem ele, o 'num_predict' da bateria (v2: 32000) ou 8000. Fora da v1, o cabeçalho grava
max=<teto>.
Pontuação: score_tb.py. Pré-registros: lab/2026-09-26-temporalidade/PREREG-bateria-v1.md e PREREG-bateria-v2.md.

Uso:
  python hb_tb.py --provider openrouter --models openai/gpt-6-luna --label tb-v1 --runs 3
  python hb_tb.py ... --fixtures T3-P T3-O --arms protocolo
  python hb_tb.py ... --or-route '{"only":["deepinfra/fp8"],"allow_fallbacks":false}'   (rota fixa na OpenRouter)
O cabeçalho grava também a rota pedida (rota=), se a resposta veio do canal de raciocínio (ft=1) e os tokens
de raciocínio (rtok=), quando o provedor informa.
"""
import argparse
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "strata", "core"))
import hb_runner  # noqa: E402

BAT_PADRAO = "bateria-v1.json"
BAT = json.load(open(os.path.join(HERE, BAT_PADRAO), encoding="utf-8"))
ROTULOS = "ABCDEFGH"


def montar(fx, arm, perm):
    f = BAT["fixtures"][fx]
    partes = []
    if arm in ("protocolo", "placebo"):
        partes.append(BAT[arm])
    regras = BAT["dominios"][f["dominio"]]["regras"]
    if regras:
        partes.append("Regras do processo:\n" + "\n".join(f"- {r}" for r in regras))
    ordem = f["apresentacao"][perm]
    partes.append("Cenas:\n" + "\n".join(f"{ROTULOS[i]}. {f['cenas'][k]}" for i, k in enumerate(ordem)))
    partes.append(BAT["tarefa"])
    return "\n\n".join(partes), "".join(ordem)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["ollama", "openrouter", "cerebras", "groq", "nvidia"], default="openrouter")
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--bateria", default=BAT_PADRAO, help="arquivo da bateria (ex.: bateria-v2.json)")
    ap.add_argument("--fixtures", nargs="+", default=None, help="padrão: todas as da bateria")
    ap.add_argument("--arms", nargs="+", default=["ingenuo", "protocolo"], choices=["ingenuo", "protocolo", "placebo"])
    ap.add_argument("--label", default="tb-v1")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--num-ctx", type=int, default=16384)
    ap.add_argument("--num-predict", type=int, default=None, help="padrão: o 'num_predict' da bateria, ou 8000")
    ap.add_argument("--reasoning", default=None, choices=["low", "medium", "high"], help="nível de raciocínio (OpenRouter); sem ele, padrão do modelo")
    ap.add_argument("--or-route", default=None, help='objeto "provider" da OpenRouter em JSON (rota fixa); sem ele, roteamento padrão')
    a = ap.parse_args()
    global BAT
    if a.bateria != BAT_PADRAO:
        BAT = json.load(open(os.path.join(HERE, a.bateria), encoding="utf-8"))
    if "placebo" in a.arms and "placebo" not in BAT:
        ap.error(f"{a.bateria} não tem braço placebo")
    if a.fixtures is None:
        a.fixtures = sorted(BAT["fixtures"])
    if a.num_predict is None:
        a.num_predict = BAT.get("num_predict", 8000)
    hb_runner.PROVIDER = a.provider
    if a.or_route:
        if a.provider != "openrouter":
            ap.error("--or-route só vale com --provider openrouter")
        obj = json.loads(a.or_route)
        if not isinstance(obj, dict) or not obj:
            ap.error("--or-route precisa ser um objeto JSON não vazio")
        hb_runner.OR_ROUTE = obj
    rota = json.dumps(hb_runner.OR_ROUTE, separators=(",", ":")) if hb_runner.OR_ROUTE else "-"
    base = os.path.join(os.environ.get("TB_PLANOS") or os.path.join(HERE, "planos"), a.label)
    print(f"saída em {base}", flush=True)
    # trava (PREREG v2): um rótulo usa uma bateria só. Rótulo sem marcador e com saídas é da v1.
    marcador = os.path.join(base, "BATERIA.txt")
    if os.path.exists(marcador):
        existente = open(marcador, encoding="utf-8").read().strip()
    else:
        existente = BAT_PADRAO if any(fn.endswith(".md") for _, _, fs in os.walk(base) for fn in fs) else None
    if existente and existente != a.bateria:
        sys.exit(f"RECUSADO: '{a.label}' usa {existente}; esta execução pede {a.bateria}. Use outro --label.")
    if existente is None and a.bateria != BAT_PADRAO:
        os.makedirs(base, exist_ok=True)
        open(marcador, "w", encoding="utf-8").write(a.bateria + "\n")
    bat_cab = "" if a.bateria == BAT_PADRAO else f" | bat={a.bateria} | max={a.num_predict}"
    # trava (PREREG §9, 2026-09-30): num rótulo, cada modelo tem uma rota e um provedor só; nunca se divide um modelo
    for m in a.models:
        safe = m.replace(":", "_").replace("/", "_")
        for raiz, _, arqs in os.walk(base):
            for fn in arqs:
                if fn.startswith(safe + "-r") and fn.endswith(".md"):
                    cab = open(os.path.join(raiz, fn), encoding="utf-8").readline()
                    r0 = re.search(r"\| rota=(.*?)(?= \| | -->)", cab)
                    p0 = re.search(r"\| provider=([^/ |]+)", cab)
                    r0, p0 = (r0.group(1) if r0 else "-"), (p0.group(1) if p0 else "")
                    if r0 != rota or p0 != a.provider:
                        sys.exit(f"RECUSADO: {m} já tem saídas em '{a.label}' com provider={p0} rota={r0}; "
                                 f"esta execução pede provider={a.provider} rota={rota}. Use outro --label.")
    for fx in a.fixtures:
        for arm in a.arms:
            for perm in range(len(BAT["fixtures"][fx]["apresentacao"])):
                prompt, mapa = montar(fx, arm, perm)
                out = os.path.join(base, fx, arm, f"p{perm}")
                os.makedirs(out, exist_ok=True)
                for m in a.models:
                    safe = m.replace(":", "_").replace("/", "_")
                    for run in range(1, a.runs + 1):
                        name = os.path.join(out, f"{safe}-r{run}.md")
                        if os.path.exists(name):
                            continue
                        stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
                        try:
                            content, secs, tok, stop, ft = hb_runner.call_ex(m, prompt, a.num_ctx, a.num_predict, seed=run,
                                                                          reasoning={"effort": a.reasoning} if a.reasoning else None)
                            meta = dict(hb_runner.LAST_META)
                            hdr = (f"<!-- TB | fixture={fx} | arm={arm} | perm={perm} | model={m} | run={run} | mapa={mapa} | {stamp} | "
                                   f"{secs:.0f}s | {tok} tok | stop={stop} | cost={meta.get('cost')} | "
                                   f"provider={a.provider}/{meta.get('provider')} | rota={rota} | ft={int(bool(ft))} | "
                                   f"rtok={meta.get('reasoning_tokens')} | reasoning={a.reasoning or 'default'}{bat_cab} -->\n\n")
                            open(name, "w", encoding="utf-8").write(hdr + (content or ""))
                            print(f"  {fx}/{arm}/p{perm} {m} r{run} OK {secs:.0f}s stop={stop}", flush=True)
                        except Exception as e:  # noqa: BLE001
                            open(name + ".ERROR.txt", "w", encoding="utf-8").write(f"ERRO: {e}")
                            print(f"  {fx}/{arm}/p{perm} {m} r{run} ERRO: {e}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
