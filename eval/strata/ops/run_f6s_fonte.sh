#!/usr/bin/env bash
# Teste do §5 (fonte declarada != fonte usada): 3 bracos (SEM, S127, S128) nas fixtures da familia 'fonte',
# bracos intercalados por fixture; regressao f6-indeterminado so em S127 x S128.
# Uso: bash ops/run_f6s_fonte.sh <provider> <modelo> <K> <label>
set -u
P="$1"; M="$2"; K="$3"; L="$4"
cd "$(dirname "$0")/.."
export PYTHONIOENCODING=utf-8
D5="variantes/s5-fonte-declarada.pt.md"
A5="> **Fundamentação**: fonte única (weave/tangle)"
for fx in f6-tempo-s5 f6-tempo-inverso f6-fonte-nova f6-tempo-sem-traco f6-fonte-nova-inverso f6-sem-copia; do
  python runners/hb_f6s.py --provider "$P" --models "$M" --fixture "$fx" --arm sem --tag SEM --label "$L" --runs "$K"
  python runners/hb_f6s.py --provider "$P" --models "$M" --fixture "$fx" --arm strata --tag S127 --label "$L" --runs "$K"
  python runners/hb_f6s.py --provider "$P" --models "$M" --fixture "$fx" --arm strata --tag S128 \
      --insert "$D5" --insert-before "$A5" --label "$L" --runs "$K"
done
python runners/hb_f6s.py --provider "$P" --models "$M" --fixture f6-indeterminado --arm strata --tag S127 --label "$L" --runs "$K"
python runners/hb_f6s.py --provider "$P" --models "$M" --fixture f6-indeterminado --arm strata --tag S128 \
    --insert "$D5" --insert-before "$A5" --label "$L" --runs "$K"
