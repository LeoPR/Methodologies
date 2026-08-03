#!/usr/bin/env bash
# F4 — NUCLEO shake-down 2026-08 (OpenRouter). 4 modelos x 3 fixtures x [Strata,baseline] x K=2.
# num_predict 12000: reasoner-sujeito gasta tokens pensando (5000 trunca -> INDETERMINADO).
# Custo ~US$1 total; ~1-2 min/run. Requer OPENROUTER_API_KEY no ambiente.
set -u
cd "$(dirname "$0")/.."
M="qwen/qwen3.6-27b qwen/qwen3-14b qwen/qwen3-8b google/gemini-2.5-flash"
run(){ PYTHONUTF8=1 python runners/hb_f4.py --provider openrouter --models $M --runs 2 --num-ctx 20480 --num-predict 12000 "$@"; }
for fix in dup clean trap; do
  run --target cenarios/f4-$fix --label f4s-$fix-strata-mat
  run --target cenarios/f4-$fix --label f4s-$fix-base-mat --baseline
done
echo "== NUCLEO F4 2026-08 (nuvem) CONCLUIDO =="
