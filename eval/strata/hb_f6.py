#!/usr/bin/env python3
"""F6 — eixo TEMPORAL DURO: inferir a cronologia (atual vs superado) SEM marcadores explicitos
(sem datas, sem old/, sem 'DELETADO/SUBSTITUI') — so por referencia cruzada de conteudo, CONTRA nome de
arquivo/README enganosos. Prompt NEUTRO (nao dica 'ignore o nome'). Gabarito fica em f6-manifest.json, FORA
da pasta-alvo (read_target nao o le). Mede o ponto-cego do DOSSIE/H-D (inferir tempo sem ancoras).
Uso: python hb_f6.py --models google/gemini-2.5-flash openai/gpt-4.1 --target cenarios/f6-tempo --label f6 --runs 2
"""
import argparse
import datetime
import os
import sys

import hb_runner

HERE = hb_runner.HERE

# A) EXPLICITO — pede cronologia diretamente (testa CAPACIDADE de inferir tempo sem marcadores)
TASK_CHRONO = ("Estes documentos foram produzidos em momentos diferentes do mesmo estudo.\n"
               "(1) ORDEM: reconstrua a ordem temporal em que foram escritos.\n"
               "(2) ATUAL vs SUPERADO: qual e o protocolo EM VIGOR (operante hoje) e qual foi "
               "SUPERADO/historico?\n"
               "(3) EVIDENCIA: justifique citando a evidencia interna (do conteudo) que sustenta a ordem.")

# B) INGENUO — pergunta operacional SEM mencionar tempo (testa o COMPORTAMENTO-PADRAO: segue nome/README?)
TASK_NAIVE = ("Voce vai usar este estudo. Responda direto, sem rodeios:\n"
              "(1) Qual e o protocolo do estudo e quais os parametros EM VIGOR — amostra (n), "
              "metrica e limiar de decisao?\n"
              "(2) Em uma frase: o que voce rodaria para reproduzir o estudo?")

# AUDIT — longitudinal: rastrear evolucao de decisoes, achar a em-vigor e detectar drift (doc desatualizado)
TASK_AUDIT = ("Reauditoria do projeto:\n"
              "(1) Quais sao as decisoes registradas e qual esta EM VIGOR agora?\n"
              "(2) Os demais documentos (setup/config/etc.) estao CONSISTENTES com a decisao em vigor? "
              "Aponte qualquer documento DESATUALIZADO.\n"
              "(3) O que MUDOU por ultimo — a decisao mais recente alterou/reverteu alguma anterior?")

# VIGOR — pressiona por um veredito definitivo (testa ABSTENCAO quando a escolha esta pendente)
TASK_VIGOR = ("Responda direto:\n"
              "(1) Qual e a configuracao EM VIGOR deste estudo e seus parametros (amostra, limiar)?\n"
              "(2) Em uma frase: com que parametros voce rodaria?")

TASKS = {"chrono": TASK_CHRONO, "naive": TASK_NAIVE, "audit": TASK_AUDIT, "vigor": TASK_VIGOR}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--provider", choices=["ollama", "openrouter"], default="openrouter")
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--target", required=True)
    ap.add_argument("--label", default="f6")
    ap.add_argument("--mode", choices=["chrono", "naive", "audit", "vigor"], default="chrono")
    ap.add_argument("--runs", type=int, default=2)
    ap.add_argument("--num-ctx", type=int, default=8192)
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
    prompt = "## DOCUMENTOS\n" + target + "\n\n## TAREFA\n" + TASKS[a.mode]
    print(f"== F6/{a.mode} | alvo='{a.label}' | {len(a.models)} modelos x {a.runs} run(s)")
    for m in a.models:
        for run in range(1, a.runs + 1):
            safe = m.replace(":", "_").replace("/", "_")
            name = f"plano-{safe}-F6_{a.mode}-r{run}.md"
            stamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            print(f"  -> {m} | r{run} ...", flush=True)
            try:
                content, secs, tok, stop, ft = hb_runner.call_ex(m, prompt, a.num_ctx, a.num_predict, seed=run)
                hdr = f"<!-- F6/{a.mode} | model={m} | run={run} | {stamp} | {secs:.0f}s | {tok} tok | target={a.label} -->\n\n"
                open(os.path.join(out, name), "w", encoding="utf-8").write(hdr + content)
                print(f"     OK {secs:.0f}s, {tok} tok", flush=True)
            except Exception as e:  # noqa
                open(os.path.join(out, name + ".ERROR.txt"), "w", encoding="utf-8").write(f"ERRO: {e}")
                print(f"     ERRO: {e}", flush=True)
    print("== fim:", out)


if __name__ == "__main__":
    raise SystemExit(main())
