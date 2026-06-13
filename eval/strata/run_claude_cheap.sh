#!/usr/bin/env bash
# Escada ANTHROPIC barata (Claude Code) como SUJEITO: Haiku + Sonnet, SEM thinking (minimo de flags).
# F3 (recusa) + F4 (execucao) nas fixtures discriminadoras. Opus fica para depois (custo).
set -u
cd "$(dirname "$0")"
export OPENROUTER_API_KEY=$(tr -d '[:space:]' < .openrouter-key)
M="anthropic/claude-3.5-haiku anthropic/claude-sonnet-4.5"
f3(){ PYTHONUTF8=1 python hb_f3.py --provider openrouter --task F5 --models $M --runs 2 "$@"; }
f4(){ PYTHONUTF8=1 python hb_f4.py --provider openrouter --models $M --runs 2 "$@"; }
# F3 — recusa de injecao (gate), paranoia (clean), parafrase (encoded)
f3 --target cenarios/s05-tarefas --label clf3-tarefas-strata
f3 --target cenarios/s05-tarefas --label clf3-tarefas-base --baseline
f3 --target cenarios/s05-clean   --label clf3-clean-strata
f3 --target cenarios/s05-clean   --label clf3-clean-base   --baseline
f3 --target cenarios/s05-encoded --label clf3-encoded-strata
# F4 — execucao: §5 (dup), tombstone+injecao (trap), abstencao (clean)
for fix in dup clean trap; do
  f4 --target cenarios/f4-$fix --label clf4-$fix-strata
  f4 --target cenarios/f4-$fix --label clf4-$fix-base --baseline
done
echo "== CLAUDE CHEAP (haiku+sonnet) CONCLUIDO =="
