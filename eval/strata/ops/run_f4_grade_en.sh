#!/usr/bin/env bash
# F4 — GRADE EN (repeticao de paridade do nucleo 2026-08 no idioma do canonico).
# Locks em lab/2026-08-03-idioma-en/PLANO-f4-en.md: roster IDENTICO a run_f4s_grade_or.sh,
# K=2, strata x baseline, framing audit apenas. Fixtures EN congeladas (gate A/D).
# Requer OPENROUTER_API_KEY no ambiente.
set -u
cd "$(dirname "$0")/.."
export OPENROUTER_API_KEY=$(tr -d '[:space:]' < .openrouter-key)

# Gates de instrumento: leitura do Strata PT+EN e GOLD mecanico (0 falso-neg grave).
PYTHONUTF8=1 python runners/hb_f4.py --selftest || { echo "selftest hb_f4 FALHOU; abortando"; exit 1; }
PYTHONUTF8=1 python verify/verify_f4.py --selftest | tail -2

run(){ PYTHONUTF8=1 python runners/hb_f4.py --provider openrouter --lang en --runs 2 --num-ctx 20480 --num-predict 12000 "$@"; }

# 1) PISO (<8b) — escada no dup ate quebrar
PISO="google/gemma-3-4b-it meta-llama/llama-3.2-3b-instruct meta-llama/llama-3.2-1b-instruct"
run --models $PISO --target cenarios/f4-dup-en --label f4e-dup-strata-piso
run --models $PISO --target cenarios/f4-dup-en --label f4e-dup-base-piso --baseline

# 2) CLASSES GPU — dup/clean/trap
GPU="openai/gpt-oss-20b qwen/qwen3-32b qwen/qwen3.6-35b-a3b openai/gpt-oss-120b"
for fix in dup clean trap; do
  run --models $GPU --target cenarios/f4-$fix-en --label f4e-$fix-strata-gpu
  run --models $GPU --target cenarios/f4-$fix-en --label f4e-$fix-base-gpu --baseline
done

# 3) BRANDS economicos — dup/clean
BR="anthropic/claude-haiku-4.5 openai/gpt-4.1-mini deepseek/deepseek-v3.2"
for fix in dup clean; do
  run --models $BR --target cenarios/f4-$fix-en --label f4e-$fix-strata-brand
  run --models $BR --target cenarios/f4-$fix-en --label f4e-$fix-base-brand --baseline
done

# 4) TOPOS-controle — dup/trap
TP="anthropic/claude-sonnet-5 openai/gpt-5 google/gemini-3.1-pro-preview"
for fix in dup trap; do
  run --models $TP --target cenarios/f4-$fix-en --label f4e-$fix-strata-topo
  run --models $TP --target cenarios/f4-$fix-en --label f4e-$fix-base-topo --baseline
done

echo "== GRADE EN F4 (paridade) CONCLUIDA =="
