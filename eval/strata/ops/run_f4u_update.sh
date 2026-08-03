#!/usr/bin/env bash
# F4U — leva de atualizacao de roster 2026-08-02 (auditoria de fontes primarias).
# Estagio A: trap brands atualizadas (haiku-4.5, gpt-4.1-mini, deepseek-v4-pro, llama-4-scout)
# Estagio C: topo OpenAI atualizado (gpt-5.6-terra) dup+trap. Sol so se terra falhar.
set -u
cd "$(dirname "$0")/.."
run(){ PYTHONUTF8=1 python runners/hb_f4.py --provider openrouter --runs 2 --num-ctx 20480 --num-predict 12000 "$@"; }

# A) BRANDS atualizadas — trap (celula que faltou) + deepseek-v4-pro/llama-4-scout novos
BRA="anthropic/claude-haiku-4.5 openai/gpt-4.1-mini deepseek/deepseek-v4-pro meta-llama/llama-4-scout"
run --models $BRA --target cenarios/f4-trap --label f4u-trap-strata-brand
run --models $BRA --target cenarios/f4-trap --label f4u-trap-base-brand --baseline

# C) TOPO OpenAI atual — gpt-5.6-terra, dup+trap
T56="openai/gpt-5.6-terra"
for fix in dup trap; do
  run --models $T56 --target cenarios/f4-$fix --label f4u-$fix-strata-topo56
  run --models $T56 --target cenarios/f4-$fix --label f4u-$fix-base-topo56 --baseline
done

echo "== F4U ATUALIZACAO DE ROSTER CONCLUIDA =="
