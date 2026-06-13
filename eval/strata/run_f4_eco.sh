#!/usr/bin/env bash
# F4 ECOLOGICO — digest REAL (pdf2md, gitignored/privado). 3 modelos nuvem x [Strata,baseline] x 2.
# num_predict 12000: os arquivos reais sao grandes (re-emitir tombstone inteiro custa muitos tokens —
# achado: o formato 'emitir arquivo inteiro' estica em projeto real). Saida planos/ (gitignored).
set -u
cd "$(dirname "$0")"
export OPENROUTER_API_KEY=$(tr -d '[:space:]' < .openrouter-key)
M="openai/gpt-4o-mini google/gemini-2.5-flash openai/gpt-4.1"
run(){ PYTHONUTF8=1 python hb_f4.py --provider openrouter --models $M --runs 2 --num-predict 12000 --target fixtures-real/pdf2md-digest "$@"; }
run --label f4eco-strata
run --label f4eco-base --baseline
echo "== MATRIZ ECO F4 CONCLUIDA =="
