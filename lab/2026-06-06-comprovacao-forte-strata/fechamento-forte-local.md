---
title: Fechamento forte local — protocolo executavel
date: 2026-06-06
status: pronto para execucao
scope: tornar a conclusao local forte, repetivel e auditavel
---

# Fechamento forte local

Este protocolo fecha a trilha local com criterio duro. Nao substitui a matriz geral;
e o pacote operacional para marcar a versao local como "fechada".

## Criterio de aceite (passa/reprova)

A versao local so fecha quando TODOS os itens abaixo passam no mesmo ciclo:

1. N >= 5 por modelo alvo local (minimo: 1 modelo 8B reasoner e 1 modelo 4B de referencia).
2. P7 >= 0.80 por modelo.
3. P6 >= 0.70 por modelo.
4. N1 = 0 e N2 = 0.
5. Alucinacao <= 0.10.
6. pass_full >= 0.80 em 3 cenarios (simples, comum-brownfield, bem-formatado).
7. No cenario bem-formatado: falso-positivo = 0.

Sem isso, status local = "promissor" (nao "forte").

## Setup minimo

- Harness completion-only e read-only no alvo.
- Metodo: `strata-an-v1.md`.
- Framing: F1 neutro como baseline; F4 apenas como passada de seguranca.

## Execucao lenta e auditavel (obrigatoria antes do lote)

Objetivo: nao rodar "no escuro". Cada etapa so avanca se a anterior fechou.

### Etapa 0 — auditar parametros sem chamar modelo (dry-run)

```powershell
python lab/2026-06-04-strata-hipoteses/hb-kit/hb_limit_search.py --method lab/2026-06-04-strata-hipoteses/hb-kit/strata-an-v1.md --only-model llama3.1-8b gemma3-4b --only-scenario s03-simples --runs 1 --use-model-default-context --use-model-default-num-predict --probe-timeout-s 45 --eval-timeout-s 120 --dry-run
```

Verificar no artefato `limit-search-dry-run.json`:
- `method_chars`, `scenario_chars`, `prompt_chars`;
- `use_model_default_context`, `num_predict_override`, `probe_timeout_s`, `eval_timeout_s`.

### Etapa 1 — smoke real minimo (1 modelo, 1 cenario, 1 run)

```powershell
python lab/2026-06-04-strata-hipoteses/hb-kit/hb_limit_search.py --method lab/2026-06-04-strata-hipoteses/hb-kit/strata-an-v1.md --only-model llama3.1-8b --only-scenario s03-simples --runs 1 --target-pass-rate 0.0 --use-model-default-context --num-predict-override 256 --probe-timeout-s 45 --eval-timeout-s 180 --force-json-format --verbose
```

Verificar no `limit-search.json`:
- `ctx_results.*.history` (latencia, `probe_json_ok`, erro se houver);
- `evaluated.*.details` (se houve `error_type`, `raw_preview`, `elapsed_s`, `decode_tps`).

### Etapa 2 — ajuste incremental de geracao/tempo

Se houver `JSONDecodeError` no eval, subir **um parametro por vez**:
1. `num_predict`: 256 -> 512 -> 1024;
2. `eval-timeout-s`: 180 -> 300 -> 600;
3. manter `use-model-default-context` ate estabilizar parse/latencia.

So depois de um smoke limpo (sem erro de parse sistematico) abrir N>=5.

## Execucao sugerida

### Bloco A — repetibilidade local (N >= 5)

Rodar busca de limite/qualidade por modelo local:

```powershell
python lab/2026-06-04-strata-hipoteses/hb-kit/hb_limit_search.py --method lab/2026-06-04-strata-hipoteses/hb-kit/strata-an-v1.md --only-model qwen3-8b --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --runs 5 --target-pass-rate 0.8 --use-model-default-context --num-predict-override 1024 --probe-timeout-s 60 --eval-timeout-s 600 --force-json-format --verbose
```

Repetir para os demais modelos alvo locais (ex.: `gemma3-4b`, `llama3.1-8b`, `qwen2.5-coder-7b`).

### Bloco B — estabilidade intercenario

Gerar matriz offline com os mesmos cenarios e framing fixo:

```powershell
python lab/2026-06-04-strata-hipoteses/hb-kit/hb_matrix_runner.py --channels offline --framing F1 --runs 5
python lab/2026-06-04-strata-hipoteses/hb-kit/hb_matrix_score.py --run lab/2026-06-04-strata-hipoteses/hb-kit/planos/matrix/<timestamp>
```

### Bloco C — borda obrigatoria

Publicar por modelo o placar: P6, P7, N1, N2, alucinacao.

Sem placar de borda, a rodada nao entra na sintese.

## Evidencia minima a publicar

- `score.csv` e `score-summary.md` da rodada local.
- Tabela de aceite por modelo (passou/reprovou cada criterio).
- Divergencias relevantes e justificativa tecnica (se houver nao-monotonia).

## Regra de decisao

- Se TODOS os criterios passam: status local = "fechado forte".
- Se 1 ou mais criterios falham: status local = "aberto", com plano de correcao
  focado no menor conjunto de ajustes (texto, framing, modelo) antes de re-rodar.
