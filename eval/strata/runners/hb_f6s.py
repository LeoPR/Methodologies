#!/usr/bin/env python3
"""F6-status: o leitor AVISA quando o tempo nao se resolve? (A/B de um delta no metodo)

Mede tres coisas com a MESMA tarefa por fixture (texto no gabarito f6-status-manifest.json):
  f6-indeterminado (alvo)   : nada decide qual protocolo vale -> declarar indeterminado
  f6-agora         (alvo)   : "mais recente" dito em 2025 -> nao afirmar status de hoje sem verificar
  f6-tempo         (controle): a evidencia decide -> decidir, sem avisar a toa (§9)

Bracos (--arm):
  sem    : sem metodologia (referencia; e o que o F6 de junho mediu)
  strata : com o documento do metodo (canonico), opcionalmente com um DELTA inserido em tempo de
           execucao (--insert FILE --insert-before ANCORA). O recipe/ nao muda antes do resultado.
O cabecalho de cada saida registra braco, method_sha, provedor, custo e tokens.
Pontuacao: verify/score_f6s.py. Aditivo: nao altera hb_f6.py (serie de regressao).

Uso:
  python runners/hb_f6s.py --provider nvidia --models moonshotai/kimi-k3 --fixture f6-indeterminado \
      --arm strata --label f6s-piloto --runs 5
  python runners/hb_f6s.py ... --arm strata --insert variantes/s3-ler-tempo.pt.md \
      --insert-before "> **Fundamentação**: proveniência de dados" --tag S127
"""
import argparse
import datetime
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "core"))
import hb_runner  # noqa: E402

HERE = hb_runner.HERE

PRE_STRATA = ("Você vai trabalhar com os documentos de um projeto seguindo uma metodologia. "
              "Leia a METODOLOGIA e os DOCUMENTOS abaixo e execute a TAREFA.\n")
PRE_SEM = "Você vai trabalhar com os documentos de um projeto. Leia os DOCUMENTOS abaixo e execute a TAREFA.\n"


def sha(texto):
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()[:12]


def montar_metodo(path, insert, before):
    txt = open(path, encoding="utf-8").read()
    if insert:
        delta = open(insert, encoding="utf-8").read()
        if txt.count(before) != 1:
            raise SystemExit(f"ancora nao encontrada exatamente 1x: {before!r}")
        txt = txt.replace(before, delta + before)
    return txt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["ollama", "openrouter", "cerebras", "groq", "nvidia"], default="openrouter")
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--fixture", required=True, choices=["f6-indeterminado", "f6-agora", "f6-tempo"])
    ap.add_argument("--arm", choices=["sem", "strata"], required=True)
    ap.add_argument("--method-path", default=hb_runner.STRATA)
    ap.add_argument("--insert", default=None)
    ap.add_argument("--insert-before", default="> **Fundamentação**: proveniência de dados")
    ap.add_argument("--tag", default=None, help="rotulo do braco na saida (ex.: SEM, S126, S127)")
    ap.add_argument("--label", default="f6s")
    ap.add_argument("--runs", type=int, default=5)
    ap.add_argument("--num-ctx", type=int, default=32768)
    ap.add_argument("--num-predict", type=int, default=8000)
    ap.add_argument("--reasoning", choices=["default", "off", "low"], default="default")
    a = ap.parse_args()

    hb_runner.PROVIDER = a.provider
    spec = json.load(open(os.path.join(HERE, "f6-status-manifest.json"), encoding="utf-8"))["fixtures"][a.fixture]
    target = hb_runner.read_target(os.path.join(HERE, "cenarios", a.fixture))
    if not target.strip():
        print("ERRO: fixture vazia", file=sys.stderr)
        return 2
    if a.arm == "strata":
        metodo = montar_metodo(a.method_path, a.insert, a.insert_before)
        msha = sha(metodo)
        prompt = PRE_STRATA + "\n## METODOLOGIA (Strata)\n" + metodo + "\n\n## DOCUMENTOS\n" + target + "\n\n## TAREFA\n" + spec["task"]
        tag = a.tag or ("S+delta" if a.insert else "STRATA")
    else:
        msha = "-"
        prompt = PRE_SEM + "\n## DOCUMENTOS\n" + target + "\n\n## TAREFA\n" + spec["task"]
        tag = a.tag or "SEM"
    reasoning = {"off": {"enabled": False}, "low": {"effort": "low"}}.get(a.reasoning)

    out = os.path.join(HERE, "planos", a.label, a.fixture, tag)
    os.makedirs(out, exist_ok=True)
    print(f"== F6s | {a.fixture} | braco={tag} | method_sha={msha} | {len(a.models)} modelo(s) x {a.runs}", flush=True)
    for m in a.models:
        safe = m.replace(":", "_").replace("/", "_")
        for run in range(1, a.runs + 1):
            name = os.path.join(out, f"{safe}-r{run}.md")
            if os.path.exists(name):
                print(f"  = {m} r{run} ja existe", flush=True)
                continue
            stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            try:
                content, secs, tok, stop, ft = hb_runner.call_ex(m, prompt, a.num_ctx, a.num_predict, seed=run,
                                                                 reasoning=reasoning)
                meta = dict(hb_runner.LAST_META)
                hdr = (f"<!-- F6s | fixture={a.fixture} | arm={tag} | method_sha={msha} | model={m} | run={run} | {stamp} | "
                       f"{secs:.0f}s | {tok} tok | stop={stop} | cost={meta.get('cost')} | "
                       f"provider={a.provider}/{meta.get('provider')} | reasoning={a.reasoning} -->\n\n")
                open(name, "w", encoding="utf-8").write(hdr + (content or ""))
                print(f"  -> {m} r{run} OK {secs:.0f}s {tok} tok stop={stop}", flush=True)
            except Exception as e:  # noqa: BLE001
                open(name + ".ERROR.txt", "w", encoding="utf-8").write(f"ERRO: {e}")
                print(f"  -> {m} r{run} ERRO: {e}", flush=True)
    print("== fim:", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
