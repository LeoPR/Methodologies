#!/usr/bin/env bash
# F6-status: roda os 3 bracos (SEM, S126, S127) nas 3 fixtures, bracos intercalados por fixture.
# Uso: bash ops/run_f6s.sh <provider> <modelo> <K> <label>
set -u
P="$1"; M="$2"; K="$3"; L="$4"
cd "$(dirname "$0")/.."
export PYTHONIOENCODING=utf-8
for fx in f6-indeterminado f6-agora f6-tempo; do
  python runners/hb_f6s.py --provider "$P" --models "$M" --fixture "$fx" --arm sem --tag SEM --label "$L" --runs "$K"
  python runners/hb_f6s.py --provider "$P" --models "$M" --fixture "$fx" --arm strata --tag S126 --label "$L" --runs "$K"
  python runners/hb_f6s.py --provider "$P" --models "$M" --fixture "$fx" --arm strata --tag S127 \
      --insert variantes/s3-ler-tempo.pt.md --label "$L" --runs "$K"
done
