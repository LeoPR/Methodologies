#!/usr/bin/env python3
"""Bateria de temporalidade v1: o leitor reconstrói a ordem por dependência, nota a lacuna, o intruso e o
horário errado, e não inventa ordem onde não há?

Fixtures e gabarito em bateria-v1.json (cenas com letra interna; ordem de apresentação fixa por fixture).
O modelo vê as cenas rotuladas A, B, C... na ordem em que aparecem, não a letra interna (a letra denunciaria
a lacuna e o intruso); o cabeçalho grava mapa=<letras internas na ordem de apresentação>.
Braços (--arm): 'ingenuo' (só a tarefa) e 'protocolo' (protocolo curto derivado da ONTOLOGIA v0).
Reaproveita a chamada ao provedor de eval/strata/core (hb_runner.call_ex). Saída em
planos/<label>/<fixture>/<braço>/p<apresentação>/<modelo>-r<run>.md, com cabeçalho rastreável.
Pontuação: score_tb.py. Pré-registro: lab/2026-09-26-temporalidade/PREREG-bateria-v1.md.

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

BAT = json.load(open(os.path.join(HERE, "bateria-v1.json"), encoding="utf-8"))
ROTULOS = "ABCDEFGH"


def montar(fx, arm, perm):
    f = BAT["fixtures"][fx]
    partes = []
    if arm == "protocolo":
        partes.append(BAT["protocolo"])
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
    ap.add_argument("--fixtures", nargs="+", default=sorted(BAT["fixtures"]))
    ap.add_argument("--arms", nargs="+", default=["ingenuo", "protocolo"], choices=["ingenuo", "protocolo"])
    ap.add_argument("--label", default="tb-v1")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--num-ctx", type=int, default=16384)
    ap.add_argument("--num-predict", type=int, default=8000)
    ap.add_argument("--or-route", default=None, help='objeto "provider" da OpenRouter em JSON (rota fixa); sem ele, roteamento padrão')
    a = ap.parse_args()
    hb_runner.PROVIDER = a.provider
    if a.or_route:
        if a.provider != "openrouter":
            ap.error("--or-route só vale com --provider openrouter")
        obj = json.loads(a.or_route)
        if not isinstance(obj, dict) or not obj:
            ap.error("--or-route precisa ser um objeto JSON não vazio")
        hb_runner.OR_ROUTE = obj
    rota = json.dumps(hb_runner.OR_ROUTE, separators=(",", ":")) if hb_runner.OR_ROUTE else "-"
    base = os.path.join(HERE, "planos", a.label)
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
                            content, secs, tok, stop, ft = hb_runner.call_ex(m, prompt, a.num_ctx, a.num_predict, seed=run)
                            meta = dict(hb_runner.LAST_META)
                            hdr = (f"<!-- TB | fixture={fx} | arm={arm} | perm={perm} | model={m} | run={run} | mapa={mapa} | {stamp} | "
                                   f"{secs:.0f}s | {tok} tok | stop={stop} | cost={meta.get('cost')} | "
                                   f"provider={a.provider}/{meta.get('provider')} | rota={rota} | ft={int(bool(ft))} | "
                                   f"rtok={meta.get('reasoning_tokens')} -->\n\n")
                            open(name, "w", encoding="utf-8").write(hdr + (content or ""))
                            print(f"  {fx}/{arm}/p{perm} {m} r{run} OK {secs:.0f}s stop={stop}", flush=True)
                        except Exception as e:  # noqa: BLE001
                            open(name + ".ERROR.txt", "w", encoding="utf-8").write(f"ERRO: {e}")
                            print(f"  {fx}/{arm}/p{perm} {m} r{run} ERRO: {e}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
