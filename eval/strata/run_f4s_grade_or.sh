#!/usr/bin/env bash
# F4 — GRADE incremental 2026-08 (OpenRouter). Completa a grade de estratos (PLANO §3.2).
# num_predict 12000 (reasoner-budget). Requer OPENROUTER_API_KEY no ambiente.
# Levas: piso (<8b, dup) · classes GPU (dup/clean/trap) · brands (dup/clean) · topos (dup/trap).
set -u
cd "$(dirname "$0")"
run(){ PYTHONUTF8=1 python hb_f4.py --provider openrouter --runs 2 --num-ctx 20480 --num-predict 12000 "$@"; }

# 1) PISO (<8b) — escada no dup até quebrar
run --models "google/gemma-3-4b-it meta-llama/llama-3.2-3b-instruct meta-llama/llama-3.2-1b-instruct" \
    --target cenarios/f4-dup --label f4g-dup-strata-piso
run --models "google/gemma-3-4b-it meta-llama/llama-3.2-3b-instruct meta-llama/llama-3.2-1b-instruct" \
    --target cenarios/f4-dup --label f4g-dup-base-piso --baseline

# 2) CLASSES GPU — dup/clean/trap
GPU="openai/gpt-oss-20b qwen/qwen3-32b qwen/qwen3.6-35b-a3b openai/gpt-oss-120b"
for fix in dup clean trap; do
  run --models "$GPU" --target cenarios/f4-$fix --label f4g-$fix-strata-gpu
  run --models "$GPU" --target cenarios/f4-$fix --label f4g-$fix-base-gpu --baseline
done

# 3) BRANDS econômicos — dup/clean
BR="anthropic/claude-haiku-4.5 openai/gpt-4.1-mini deepseek/deepseek-v3.2"
for fix in dup clean; do
  run --models "$BR" --target cenarios/f4-$fix --label f4g-$fix-strata-brand
  run --models "$BR" --target cenarios/f4-$fix --label f4g-$fix-base-brand --baseline
done

# 4) TOPOS-controle — dup/trap
TP="anthropic/claude-sonnet-5 openai/gpt-5 google/gemini-3.1-pro-preview"
for fix in dup trap; do
  run --models "$TP" --target cenarios/f4-$fix --label f4g-$fix-strata-topo
  run --models "$TP" --target cenarios/f4-$fix --label f4g-$fix-base-topo --baseline
done

echo "== GRADE INCREMENTAL F4 2026-08 CONCLUIDA =="
