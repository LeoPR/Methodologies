#!/usr/bin/env bash
# Reteste do §5 com o texto v2 (adendo §10 do PREREG): so o braco S128b, nas mesmas fixtures.
# Uso: bash ops/run_f6s_fonte_v2.sh <provider> <modelo> <K> <label>
set -u
P="$1"; M="$2"; K="$3"; L="$4"
cd "$(dirname "$0")/.."
export PYTHONIOENCODING=utf-8
for fx in f6-tempo-sem-traco f6-tempo-inverso f6-fonte-nova-inverso f6-tempo-s5 f6-sem-copia f6-fonte-nova f6-indeterminado; do
  python runners/hb_f6s.py --provider "$P" --models "$M" --fixture "$fx" --arm strata --tag S128b \
      --insert variantes/s5-fonte-declarada-v2.pt.md --insert-before "> **Fundamentação**: fonte única (weave/tangle)" \
      --label "$L" --runs "$K"
done
