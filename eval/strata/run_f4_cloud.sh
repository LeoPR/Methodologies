#!/usr/bin/env bash
# F4 — matriz NUVEM (execucao simulada). 3 modelos x 3 fixtures x [Strata, baseline] x 2 runs.
# f4-eco-pdf2md (digest real) roda a parte. Saida planos/<label>/ (gitignored). Chave via .openrouter-key.
set -u
cd "$(dirname "$0")"
export OPENROUTER_API_KEY=$(tr -d '[:space:]' < .openrouter-key)
M="openai/gpt-4o-mini google/gemini-2.5-flash openai/gpt-4.1"
run(){ PYTHONUTF8=1 python hb_f4.py --provider openrouter --models $M --runs 2 "$@"; }
for fix in f4-dup f4-clean f4-trap; do
  run --target cenarios/$fix --label f4-$fix-strata
  run --target cenarios/$fix --label f4-$fix-base --baseline
done
echo "== MATRIZ NUVEM F4 CONCLUIDA =="
