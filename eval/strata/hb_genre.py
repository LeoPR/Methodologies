#!/usr/bin/env python3
"""Eixo GENERO — o modelo reconhece o GENERO do projeto e aplica o padrao CERTO para ele (§9: nao
exigir o que nao se aplica)? Confundidor que o tier messy externo levantou: baixa-conformidade != defeito
(uma lista/notas nao precisa de tests/CI). GENERO-CEGO = exigir padrao de software de um projeto de notas.
Uso: python hb_genre.py --provider openrouter --models google/gemini-2.5-flash openai/gpt-4.1 \\
       --target external-fixtures/ext-ml3months --label gen-ml3months --runs 1
"""
import argparse
import datetime
import os
import sys

import hb_runner

HERE = hb_runner.HERE

TASK = ("Voce vai avaliar a organizacao deste projeto APLICANDO O PADRAO CERTO PARA O GENERO dele "
        "(§9 — nao exija o que nao se aplica ao genero). Responda:\n"
        "(1) GENERO: que tipo de projeto e este? Escolha e justifique pelo CONTEUDO: "
        "[biblioteca/pacote | aplicacao/ferramenta | pesquisa/algoritmo | notas/aula/tutorial | "
        "lista/curadoria | outro].\n"
        "(2) PADRAO DO GENERO: para ESSE genero, o que REALMENTE importa organizar — e o que NAO se "
        "aplica (ex.: uma lista nao precisa de testes/CI; pesquisa nem sempre precisa de empacotamento).\n"
        "(3) VEREDITO (§9): [JA-BOM-PARA-O-GENERO | PRECISA EM PONTOS | PRECISA MUITO] + APENAS as poucas "
        "lacunas que importam PARA O GENERO (nao liste exigencias genericas que nao se aplicam).")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["ollama", "openrouter"], default="openrouter")
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--runs", type=int, default=1)
    ap.add_argument("--num-ctx", type=int, default=12288)
    ap.add_argument("--num-predict", type=int, default=1800)
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
    print(f"== GENERO | alvo='{a.label}' | {len(a.models)} modelos x {a.runs} run(s)")
    for m in a.models:
        for run in range(1, a.runs + 1):
            safe = m.replace(":", "_").replace("/", "_")
            name = f"plano-{safe}-GEN-r{run}.md"
            stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            print(f"  -> {m} | r{run} ...", flush=True)
            try:
                content, secs, tok, stop, ft = hb_runner.call_ex(m, prompt, a.num_ctx, a.num_predict, seed=run)
                hdr = f"<!-- GEN | model={m} | run={run} | {stamp} | {secs:.0f}s | {tok} tok | target={a.label} -->\n\n"
                open(os.path.join(out, name), "w", encoding="utf-8").write(hdr + content)
                print(f"     OK {secs:.0f}s, {tok} tok", flush=True)
            except Exception as e:  # noqa
                open(os.path.join(out, name + ".ERROR.txt"), "w", encoding="utf-8").write(f"ERRO: {e}")
                print(f"     ERRO: {e}", flush=True)
    print("== fim:", out)


if __name__ == "__main__":
    raise SystemExit(main())
