#!/usr/bin/env bash
# Roda a bateria de temporalidade para UM modelo, com as fixtures divididas em N grupos disjuntos, um processo por grupo
# (nenhum arquivo é tocado por dois processos; o runner pula o que já existe, então relançar retoma).
# Nunca rode dois run_tb.sh do mesmo (label, modelo) ao mesmo tempo: os grupos se repetem e as chamadas se duplicam.
# Uso: bash run_tb.sh <provider> <modelo> <label> <K> [N=4] [rota JSON da OpenRouter]
#   ex.: bash run_tb.sh openrouter z-ai/glm-5.3 tb-v1 3 13 '{"only":["atlas-cloud/fp8"],"allow_fallbacks":false,"require_parameters":true}'
# Chave do OpenRouter lida de eval/strata/.openrouter-key (não é impressa). Logs em planos/<label>-<modelo>-g<i>.log.
set -u
P="$1"; M="$2"; L="$3"; K="$4"; N="${5:-4}"; ROTA="${6:-}"
cd "$(dirname "$0")"
export PYTHONIOENCODING=utf-8
if [ "$P" = "openrouter" ]; then
  export OPENROUTER_API_KEY=$(tr -d '[:space:]' < ../strata/.openrouter-key)
fi
FX=$(python -c "import json; print(' '.join(sorted(json.load(open('bateria-v1.json', encoding='utf-8'))['fixtures'])))")
SAFE=$(echo "$M" | tr '/:' '__')
mkdir -p planos
# logs de execuções anteriores do mesmo (label, modelo) vão para um arquivo de histórico, para não entrarem na conta
for f in planos/$L-$SAFE-g*.log; do [ -e "$f" ] && cat "$f" >> "planos/$L-$SAFE-anteriores.log" && rm -f "$f"; done
PIDS=(); LOGS=()
for g in $(seq 0 $((N - 1))); do
  GRUPO=$(echo $FX | tr ' ' '\n' | awk -v n="$N" -v g="$g" '(NR - 1) % n == g' | tr '\n' ' ')
  [ -z "$GRUPO" ] && continue
  LOG="planos/$L-$SAFE-g$g.log"
  if [ -n "$ROTA" ]; then
    python hb_tb.py --provider "$P" --models "$M" --label "$L" --runs "$K" --fixtures $GRUPO --or-route "$ROTA" > "$LOG" 2>&1 &
  else
    python hb_tb.py --provider "$P" --models "$M" --label "$L" --runs "$K" --fixtures $GRUPO > "$LOG" 2>&1 &
  fi
  PIDS+=($!); LOGS+=("$LOG")
done
FALHAS=0
for j in "${!PIDS[@]}"; do
  wait "${PIDS[$j]}" || { FALHAS=$((FALHAS + 1)); echo "processo ${LOGS[$j]} saiu com erro: $(tail -1 "${LOGS[$j]}")"; }
done
echo "$M: $(cat "${LOGS[@]}" | grep -c ' OK ') OK, $(cat "${LOGS[@]}" | grep -c 'ERRO') ERRO, ${#PIDS[@]} processos, $FALHAS saíram com erro"
