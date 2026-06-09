#!/usr/bin/env python3
"""Sonda: testa ENTENDER e APLICAR L1 (o que nunca foi testado), + auto-reporte de necessidade
de PESQUISA. 3 tiers: topo (Opus), medio (gpt-4.1-mini), pequeno local (deepseek-r1:8b).
Uso: python probe_l1.py"""
import os
import sys

import hb_runner

OUT = os.path.join(hb_runner.HERE, "planos", "probe-l1")
os.makedirs(OUT, exist_ok=True)

PROMPT = """Você conhece o método Strata (arquitetura do conhecimento em 3 camadas de durabilidade):
- L0 = núcleo atemporal: princípios (método científico, rastreabilidade, fonte única…), independentes de tecnologia.
- L1 = padrões consolidados: formalizações maduras que OPERACIONALIZAM o L0 (e são SUBSTITUÍVEIS sem tocar no L0).
- L2 = adaptação à era atual: como as ferramentas de hoje expressam L0/L1.

Responda exatamente 3 partes:

(1) EXPLIQUE, em 2-3 frases, a diferença entre L0, L1 e L2, e por que uma formalização L1 é "substituível".

(2) APLIQUE o L1 — para cada necessidade L0 abaixo, nomeie UMA formalização L1 madura, diga em 1 linha por que serve, e o que se trocaria sem tocar no L0:
   (a) registrar decisões de arquitetura com o porquê, de forma rastreável e imutável;
   (b) documentação que separa tutorial, how-to, referência e explicação;
   (c) declarar hipótese e método ANTES de coletar dados, para um experimento.

(3) HONESTIDADE: alguma dessas formalizações você NÃO conhece bem e precisaria PESQUISAR (web/fonte externa) para responder com segurança? Liste quais; se nenhuma, escreva "nenhuma — respondi do meu próprio conhecimento"."""

REMOTE = ["anthropic/claude-opus-4.8", "openai/gpt-4.1-mini"]
LOCAL = ["deepseek-r1:8b"]


def save(model, text, secs, tok):
    safe = model.replace(":", "_").replace("/", "_")
    with open(os.path.join(OUT, f"{safe}.md"), "w", encoding="utf-8") as f:
        f.write(f"<!-- probe-l1 | {model} | {secs:.0f}s | {tok} tok -->\n\n{text}")
    print(f"  OK {model} ({secs:.0f}s, {tok} tok)", flush=True)


if not os.environ.get("OPENROUTER_API_KEY"):
    print("sem OPENROUTER_API_KEY", file=sys.stderr); sys.exit(2)
for m in REMOTE:
    print(f"-> {m} ...", flush=True)
    try:
        txt, secs, tok = hb_runner.call_openrouter(m, PROMPT, num_predict=2200, seed=1)
        save(m, txt, secs, tok)
    except Exception as e:  # noqa
        print(f"  ERRO {m}: {e}", file=sys.stderr)
for m in LOCAL:
    print(f"-> {m} (local) ...", flush=True)
    try:
        txt, secs, tok = hb_runner.call_ollama(m, PROMPT, num_ctx=8192, num_predict=6000, seed=1)
        save(m, txt, secs, tok)
    except Exception as e:  # noqa
        print(f"  ERRO {m}: {e}", file=sys.stderr)
print("== fim probe-l1")
