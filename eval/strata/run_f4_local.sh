#!/usr/bin/env bash
# F4 — matriz LOCAL (Ollama, gratis, lenta). 4 modelos x 3 fixtures x [Strata,baseline] x 2 runs.
# Labels f4l-<fix>-<arm>. num_ctx 20480 (cabe no GPU 12GB), num_predict 5000 (emite arquivos inteiros).
set -u
cd "$(dirname "$0")"
M="deepseek-r1:8b qwen2.5-coder:7b gemma3:4b granite3.3:8b"
run(){ PYTHONUTF8=1 python hb_f4.py --provider ollama --models $M --runs 2 --num-ctx 20480 --num-predict 5000 "$@"; }
for fix in dup clean trap; do
  run --target cenarios/f4-$fix --label f4l-$fix-strata
  run --target cenarios/f4-$fix --label f4l-$fix-base --baseline
done
echo "== MATRIZ LOCAL F4 CONCLUIDA =="
