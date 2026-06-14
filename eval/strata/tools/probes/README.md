# tools/probes — diagnósticos one-off (NÃO fazem parte do pipeline)

Sondas/smoke-tests pontuais, fora do pipeline de evidência (`hb_f*` → `verify_f4`/`judge_*` → `aggregate_*`):

- `openrouter_probe.py` — lista modelos OpenRouter (ex.: `:free`) / sanidade da chave.
- `price_probe.py` — preço $/M por modelo (planejar custo antes de rodar).
- `probe_judges.py` — achar/comparar juízes fortes.
- `probe2.py` — smoke genérico.
- `diag_ollama.py` — diagnostica thinking/`done_reason` do Ollama local.

> `probe_l1.py` ficou em `eval/strata/` (importa a base viva `hb_runner`). Estes aqui não importam nada local.
