#!/usr/bin/env bash
# F4V — leva de catalogo 2026-08-02: kimi-k3 (brand nova, Moonshot) + opus-5/fable-5
# no trap (2 bracos) e clean (Strata) — "ver alem" = borda de abstencao.
set -u
cd "$(dirname "$0")/.."
run(){ PYTHONUTF8=1 python runners/hb_f4.py --provider openrouter --runs 2 --num-ctx 20480 --num-predict 12000 "$@"; }

# 1) KIMI-K3 — brand nova: dup + trap, 2 bracos
K="moonshotai/kimi-k3"
for fix in dup trap; do
  run --models $K --target cenarios/f4-$fix --label f4v-$fix-strata-kimi
  run --models $K --target cenarios/f4-$fix --label f4v-$fix-base-kimi --baseline
done

# 2) OPUS-5 / FABLE-5 — trap (2 bracos) + clean (Strata)
for M in anthropic/claude-opus-5 anthropic/claude-fable-5; do
  short=$(echo $M | cut -d/ -f2)
  run --models $M --target cenarios/f4-trap --label f4v-trap-strata-${short}
  run --models $M --target cenarios/f4-trap --label f4v-trap-base-${short} --baseline
  run --models $M --target cenarios/f4-clean --label f4v-clean-strata-${short}
done

echo "== F4V CATALOGO CONCLUIDA =="
