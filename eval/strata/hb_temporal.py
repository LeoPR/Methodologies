#!/usr/bin/env python3
"""Eixo TEMPORAL — o modelo SITUA artefatos no tempo (atual vs superado/historico) e reconhece
SUPERSESSAO/FUSAO/TOMBSTONE como ORGANIZACAO, nao como defeito? Testa o ponto-cego §3/§8 (datas/historia)
em projetos de acompanhamento-de-aula do proprio dono (que tem semanas fundidas, arquivamentos, DELETADO-recriavel).
NAO leva o gabarito no prompt (so a tarefa) — o gabarito pre-registrado fica em verify/RESULTADOS.
Uso: python hb_temporal.py --models google/gemini-2.5-flash openai/gpt-4.1 \\
       --target own-fixtures/own-aulaquantum --label temp-aulaquantum --runs 1
"""
import argparse
import datetime
import os
import sys

import hb_runner

HERE = hb_runner.HERE

TASK = ("Voce vai SITUAR NO TEMPO os artefatos deste projeto de acompanhamento de aula (§3/§8 — "
        "rastreabilidade e historia). Responda:\n"
        "(1) LINHA DO TEMPO: reconstrua a ordem/estado pelos artefatos — o que e ATUAL vs "
        "SUPERADO/HISTORICO. Use datas e nomes de pastas (semanas, capitulos, archive).\n"
        "(2) SUPERSESSAO / FUSAO / TOMBSTONE: ha artefatos FUNDIDOS, ARQUIVADOS ou marcados "
        "DELETADO/movido com ponteiro? Para CADA um, classifique: (a) ORGANIZACAO CORRETA "
        "(tombstone/arquivamento — preservar+marcar+apontar) ou (b) DEFEITO (perda, duplicata, lixo). Justifique.\n"
        "(3) VEREDITO TEMPORAL: a organizacao no tempo esta [COERENTE | TEM LACUNAS | CONFUSA]? "
        "Aponte APENAS o que de fato compromete situar no tempo — nao trate arquivamento/tombstone como defeito.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["ollama", "openrouter"], default="openrouter")
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--num-ctx", type=int, default=12288)
    ap.add_argument("--num-predict", type=int, default=2000)
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
    print(f"== TEMPORAL | alvo='{a.label}' | {len(a.models)} modelos x {a.runs} run(s)")
    for m in a.models:
        for run in range(1, a.runs + 1):
            safe = m.replace(":", "_").replace("/", "_")
            name = f"plano-{safe}-TEMP-r{run}.md"
            stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            print(f"  -> {m} | r{run} ...", flush=True)
            try:
                content, secs, tok, stop, ft = hb_runner.call_ex(m, prompt, a.num_ctx, a.num_predict, seed=run)
                hdr = f"<!-- TEMP | model={m} | run={run} | {stamp} | {secs:.0f}s | {tok} tok | target={a.label} -->\n\n"
                open(os.path.join(out, name), "w", encoding="utf-8").write(hdr + content)
                print(f"     OK {secs:.0f}s, {tok} tok", flush=True)
            except Exception as e:  # noqa
                open(os.path.join(out, name + ".ERROR.txt"), "w", encoding="utf-8").write(f"ERRO: {e}")
                print(f"     ERRO: {e}", flush=True)
    print("== fim:", out)


if __name__ == "__main__":
    raise SystemExit(main())
