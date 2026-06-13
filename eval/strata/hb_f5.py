#!/usr/bin/env python3
"""F5 (eixo PESQUISA) — verificacao de FONTE PRIMARIA (§6). O projeto tem afirmacoes tecnicas com
ERROS plantados sobre formalizacoes que o Strata referencia (Diataxis, pace layering, Conventional
Commits). Tarefa: verificar cada uma contra a fonte. Compara modelo COM vs SEM web (o web e ligado
pelo sufixo ':online' no id do modelo na OpenRouter — sem mudanca de codigo).
Hipotese: web ajuda o CONHECIMENTO (L1/§6 verificacao de fonte), nao o julgamento L0.
Uso: python hb_f5.py --provider openrouter --models google/gemini-2.5-flash google/gemini-2.5-flash:online \\
       --target cenarios/f5-verif --label f5-verif --runs 2
"""
import argparse
import datetime
import os
import sys

import hb_runner

HERE = hb_runner.HERE

TASK = ("Voce e um auditor de FONTE PRIMARIA (disciplina §6: nao repetir nem inferir — VERIFICAR na "
        "fonte). Para CADA afirmacao tecnica numerada do projeto abaixo, responda em uma linha:\n"
        "  N) [CORRETA | INCORRETA -> <correcao> | NAO-VERIFICAVEL]\n"
        "Verifique contra a fonte primaria. Se NAO tiver como verificar com confianca, diga "
        "NAO-VERIFICAVEL — NAO invente uma verificacao que nao fez.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["ollama", "openrouter"], default="openrouter")
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--runs", type=int, default=2)
    ap.add_argument("--num-ctx", type=int, default=8192)
    ap.add_argument("--num-predict", type=int, default=1500)
    a = ap.parse_args()
    hb_runner.PROVIDER = a.provider
    if a.provider == "openrouter" and not os.environ.get("OPENROUTER_API_KEY"):
        print("sem OPENROUTER_API_KEY", file=sys.stderr); return 2
    out = os.path.join(HERE, "planos", a.label)
    if not os.path.abspath(out).startswith(os.path.abspath(HERE)):
        print("RECUSADO: out fora do eval/strata", file=sys.stderr); return 2
    os.makedirs(out, exist_ok=True)
    target = hb_runner.read_target(os.path.abspath(a.target))
    if not target.strip():
        print(f"ERRO: nada lido em {a.target}", file=sys.stderr); return 2
    prompt = "## PROJETO\n" + target + "\n\n## TAREFA\n" + TASK
    print(f"== F5 (verificacao §6) | alvo='{a.label}' | {len(a.models)} modelos x {a.runs} run(s)")
    for m in a.models:
        web = ":online" in m
        for run in range(1, a.runs + 1):
            safe = m.replace(":", "_").replace("/", "_")
            name = f"plano-{safe}-F5v-r{run}.md"
            stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            print(f"  -> {m} | web={web} | r{run} ...", flush=True)
            try:
                content, secs, tok, stop, ft = hb_runner.call_ex(m, prompt, a.num_ctx, a.num_predict, seed=run)
                hdr = (f"<!-- F5v | model={m} | web={web} | run={run} | {stamp} | {secs:.0f}s | "
                       f"{tok} tok | stop={stop} | target={a.label} -->\n\n")
                open(os.path.join(out, name), "w", encoding="utf-8").write(hdr + content)
                print(f"     OK {secs:.0f}s, {tok} tok", flush=True)
            except Exception as e:  # noqa
                open(os.path.join(out, name + ".ERROR.txt"), "w", encoding="utf-8").write(f"ERRO: {e}")
                print(f"     ERRO: {e}", flush=True)
    print("== fim:", out)


if __name__ == "__main__":
    raise SystemExit(main())
