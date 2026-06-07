---
title: Candidatos de modelos modernos locais via Ollama
created: 2026-06-07
status: pronto para triagem
scope: shortlist de modelos que cabem em setup local e podem ser avaliados no hb-kit
---

# Candidatos de modelos modernos locais via Ollama

Criticoes de selecao para shortlist local:
- porte nominal ate 14B (faixa mais realista para GPU de 12GB com quantizacoes usuais)
- foco em texto/raciocinio para protocolo Strata completion-only
- disponibilidade no ecossistema Ollama (instalado localmente ou catalogo publico)

## Ja instalados e prontos para teste

- `qwen3:8b` (5.2 GB)
- `deepseek-r1:8b` (5.2 GB)
- `granite3.3:8b` (4.9 GB)
- `qwen2.5-coder:7b` (4.7 GB)
- `llama3.1:8b` (4.9 GB)
- `gemma3:4b` (3.3 GB)
- `qwen3:4b` (2.5 GB)
- `qwen3:1.7b` (1.4 GB)
- `gemma3:1b` (815 MB)
- `qwen3:0.6b` (522 MB)
- `mistral-nemo:latest` (7.1 GB)
- `phi4:latest` (9.1 GB)
- `qwen3:14b` (9.3 GB)
- `deepseek-r1:14b` (9.0 GB)
- `gemma3:12b` (8.1 GB)
- `granite4.1:8b` (5.3 GB)
- `nemotron-3-nano:4b` (2.8 GB)

## Candidatos modernos do catalogo Ollama para baixar

Observacao: estes modelos apareceram no catalogo com atualizacoes recentes e
porte potencialmente compativel com a faixa local.

- `lfm2.5:8b`
- `gemma4:e4b`
- `gemma4:e2b`
- `qwen3.5:4b`
- `qwen3.5:9b`

## Comandos de pull (ollama-server)

```powershell
ollama pull lfm2.5:8b
ollama pull gemma4:e4b
ollama pull gemma4:e2b
ollama pull qwen3.5:4b
ollama pull qwen3.5:9b
```

## Sequencia sugerida de triagem (custo -> capacidade)

1. `qwen3:4b` e `gemma3:4b` (baseline leve)
2. `granite3.3:8b`, `qwen3:8b`, `deepseek-r1:8b`, `llama3.1:8b`
3. `mistral-nemo:latest`, `phi4:latest`, `qwen3:14b`, `deepseek-r1:14b`
4. novos baixados (`granite4.1:8b`, `nemotron-3-nano:4b`, `lfm2.5:8b`, `gemma4:*`, `qwen3.5:*`)

## Observacoes empiricas desta sessao

- `granite4.1:8b` e `nemotron-3-nano:4b` foram baixados com sucesso e estao no `ollama list`.
- triagem em lote largo ficou cara demais; para estes candidatos, o melhor proximo passo e'
	rodar **um modelo por vez**.
- smoke individual concluido:
	- `qwen3:0.6b`: probe estavel e muito rapido, mas `mean_score=0.00` e `pass_full=0.00`.
	- `gemma3:1b`: `mean_score=2.50`, porem com dois `JSONDecodeError` e `pass_full=0.00`.

Leitura pratica:
- para custo minimo, `qwen3:0.6b` serve como piso operacional, nao como candidato de fechamento.
- entre os sub-2B testados, `gemma3:1b` merece mais investigacao se houver mitigacao adicional
	de formato/JSON.

## Regra de comparabilidade para triagem

Usar sempre o mesmo protocolo minimo para comparacao inicial:

```powershell
python hb_limit_search.py --method strata-an-v1.md --only-model <model-id-no-catalogo> --only-scenario s03-simples s01-comum-brownfield s04-bem-formatado --runs 1 --target-pass-rate 0.0 --use-model-default-context --num-predict-override 1024 --probe-timeout-s 45 --eval-timeout-s 180 --force-json-format --anti-n2-guard
```

Antes de modelos >=4B, aplicar warm-up para reduzir falso timeout de probe:

```powershell
ollama run <modelo> "Responda apenas: ok"
```
