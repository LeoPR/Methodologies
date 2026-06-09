#!/usr/bin/env python3
"""M0 (Fase 1) — testa a ABSTENCAO: 'devo agir aqui? quanto?' (o gate §9). Duas formas:
- m0     : abstencao-primeiro (veredito JA-BOM/PRECISA + so-se-precisar + contagem de acoes)
- audit  : controle = o framing classico 'ache problemas' (a/b/c)
Saida no formato plano-<model>-F1-r<run>.md (reaproveita blind/score). READ-ONLY, completion-only.
Uso: python hb_m0.py --provider openrouter --form m0 --models ... --target fixtures-real/nnn-digest --label m0-nnn --runs 2"""
import argparse
import datetime
import os
import sys

import hb_runner

HERE = hb_runner.HERE

M0 = ("Você vai avaliar a organização de um projeto e decidir SE e QUANTO o método Strata "
      "(arquitetura de conhecimento) se aplica. NÃO procure problemas a todo custo: organizar "
      "tem CUSTO, e o próprio método (§9) manda agir proporcional a custo × risco. É VÁLIDO e "
      "muitas vezes CORRETO concluir \"já está bom, ação mínima ou nenhuma\".\n\n"
      "## ARQUIVOS DO PROJETO\n{target}\n\n## TAREFA\n"
      "(1) VEREDITO (§9): escolha UM e justifique por custo × risco: "
      "[JÁ-BOM (ação mínima ou nenhuma) | PRECISA EM PONTOS | PRECISA MUITO].\n"
      "(2) O que o projeto JÁ FAZ BEM — forças concretas, citando o arquivo.\n"
      "(3) SE (e só se) precisa: APENAS as poucas áreas que valem o esforço, em ordem de "
      "risco × custo, com evidência (trecho). PROIBIDO \"aplicar tudo\"; um projeto bom pode ter ZERO.\n"
      "(4) NÚMERO de ações que você recomenda (um inteiro).")

AUDIT = ("Você vai avaliar a organização de um projeto contra o método Strata.\n\n"
         "## ARQUIVOS DO PROJETO\n{target}\n\n## TAREFA\n"
         "Produza: (a) ENTENDIMENTO; (b) DIAGNÓSTICO — liste os problemas de organização e, para "
         "cada um, a seção do método que viola; (c) PRIMEIRO PASSO. Priorize; não mande aplicar "
         "tudo. Não invente o que o projeto não fornece; se não dá para saber, diga.")

PROMPTS = {"m0": M0, "audit": AUDIT}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["ollama", "openrouter"], default="openrouter")
    ap.add_argument("--form", choices=["m0", "audit"], required=True)
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--runs", type=int, default=2)
    ap.add_argument("--num-predict", type=int, default=2600)
    ap.add_argument("--num-ctx", type=int, default=24576)
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
    prompt_t = PROMPTS[a.form]
    print(f"== M0 | forma={a.form} | alvo='{a.label}' | {len(a.models)} modelos x {a.runs} run(s)")
    for m in a.models:
        for run in range(1, a.runs + 1):
            prompt = prompt_t.format(target=target)
            safe = m.replace(":", "_").replace("/", "_")
            name = f"plano-{safe}-F1-r{run}.md"
            stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            print(f"  -> {m} | {a.form} | r{run} ...", flush=True)
            try:
                content, secs, tok = hb_runner.call(m, prompt, a.num_ctx, a.num_predict, seed=run)
                hdr = f"<!-- M0 {a.form} | model={m} | run={run} | {stamp} | {secs:.0f}s | {tok} tok -->\n\n"
                open(os.path.join(out, name), "w", encoding="utf-8").write(hdr + content)
                print(f"     OK {secs:.0f}s, {tok} tok", flush=True)
            except Exception as e:  # noqa
                open(os.path.join(out, name + ".ERROR.txt"), "w", encoding="utf-8").write(f"ERRO: {e}")
                print(f"     ERRO: {e}", flush=True)
    print("== fim:", out)


if __name__ == "__main__":
    raise SystemExit(main())
