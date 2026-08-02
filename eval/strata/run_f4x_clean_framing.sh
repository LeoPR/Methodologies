#!/usr/bin/env bash
# F4X — fase seguinte: clean x framing (audit|hunt) x K=5 (flip-rate). 2026-08-02.
# Celulas decisivas: superagentes (haiku, v4-pro, 32b) + controles que calibram
# (gpt-4.1-mini, 27b) + sonda topo (opus-5 hunt).
set -u
cd "$(dirname "$0")"
run(){ PYTHONUTF8=1 python hb_f4.py --provider openrouter --runs 5 --num-ctx 20480 --num-predict 12000 "$@"; }

M="anthropic/claude-haiku-4.5 deepseek/deepseek-v4-pro qwen/qwen3-32b openai/gpt-4.1-mini qwen/qwen3.6-27b"
for fr in audit hunt; do
  run --models $M --target cenarios/f4-clean --label f4x-clean-strata-$fr --framing $fr
  run --models $M --target cenarios/f4-clean --label f4x-clean-base-$fr --framing $fr --baseline
done
run --models anthropic/claude-opus-5 --target cenarios/f4-clean --label f4x-clean-strata-hunt-topo --framing hunt

echo "== F4X CLEAN x FRAMING CONCLUIDA =="
