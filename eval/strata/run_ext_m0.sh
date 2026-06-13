#!/usr/bin/env bash
# Braco EXTERNO (quebra circularidade) — probe de FALSO-POSITIVO no tier BEM-COMPORTADO.
# 3 repos open-source de terceiro, objetivamente organizados. M0 (abstencao-primeiro) vs AUDIT (controle
# 'ache problemas'). Num projeto organizado o certo e' JA-BOM/acao minima; over-detectar = falso-positivo (R8).
set -u
cd "$(dirname "$0")"
export OPENROUTER_API_KEY=$(tr -d '[:space:]' < .openrouter-key)
M="google/gemini-2.5-flash openai/gpt-4.1 openai/gpt-4o-mini"
for name in tomli humanize slugify; do
  PYTHONUTF8=1 python hb_m0.py --provider openrouter --form m0    --models $M --target external-fixtures/ext-$name --label extm0-$name    --runs 1
  PYTHONUTF8=1 python hb_m0.py --provider openrouter --form audit --models $M --target external-fixtures/ext-$name --label extaudit-$name --runs 1
done
echo "== EXT M0 (bem-comportado) CONCLUIDO =="
