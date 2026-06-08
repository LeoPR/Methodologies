---
title: Tier NUVEM LIMPO (R0-R3 nuvem) — 7 sabores via OpenRouter, fixture congelado
created: 2026-06-07
setup: OpenRouter (openai_compat) · fixture CONGELADO lumen-bugado (sha 22bf662f) · prompt prosa SEM enum · 3 braços (prosa/AN-v2/baseline) · N=3 · pontuação CEGA (ids opacos) · mesmo pipeline do local
status: SUPERSEDE o RESULTADOS-tier-nuvem.md (manual/contaminado/irreproduzível)
---

# Tier nuvem limpo — refaz o que a auditoria invalidou

7 sabores via OpenRouter, **paridade total com o local** (mesmo fixture/prompt/scorer/
cego). 63 planos, 0 erros. Corrige os furos da auditoria (fixture neutralizado, prompt
com enum, coleta manual N=1, sabor Anthropic quebrado, sem baseline).

## Por braço (det = achou/7) + comparação com o local

| Braço | LOCAL | **NUVEM** |
|---|---|---|
| baseline (sem método) | 2.25 | 3.43 |
| prosa (Strata v1.1.0) | 2.50 | **4.24** |
| AN-v2 (descontaminada) | 4.58 | **5.67** |

Nuvem (det_sec): baseline 0.0 · prosa 3.57 · AN 5.48. Priorização: baseline 0.24 ·
prosa 0.38 · **AN 0.90**. Armadilhas: baseline N1=5/N2=2; prosa N1=1; **AN N1=0,N2=0**.

## Correções honestas (a auditoria + teste limpo derrubaram 2 conclusões antigas)

1. **"A nuvem satura na prosa (7/7)" — FALSO.** No teste limpo a prosa-nuvem dá **4.24/7**,
   não satura. O "7/7" antigo veio de contaminação + enum vazado + scorer por âncora
   leniente. Só **1 sabor** (gemini-2.5-flash) satura na prosa.
2. **"A AN só serve pro tier fraco/local" — FALSO.** A AN ajuda a **nuvem também**
   (+1.43 sobre a prosa; det 4.24→5.67), sobretudo nos gates de julgamento.

## Onde a AN agrega na nuvem (found/21)

| | P1 | P2 | P3 | P4 | P5 | P6 | P7 |
|---|---|---|---|---|---|---|---|
| prosa | 16 | 16 | 15 | 13 | 12 | **4** | 13 |
| AN | 21 | 7 | 13 | 21 | **19** | **19** | **19** |

A AN resgata **P6 sem-fonte (4→19)**, P5 honestidade (12→19), P7 fail-open (13→19) — os
mesmos gates de julgamento/segurança do local. (P2 a AN piora: 16→7 — desvia o foco.)

## Falsa-inteligência — CONFIRMADA (det_found médio, N=3)

| sabor | prosa | AN | base |
|---|---|---|---|
| **google/gemini-2.5-flash** | **7.0** | **7.0** | 4.33 |
| openai/gpt-4.1-mini | 5.0 | 6.33 | 3.67 |
| anthropic/claude-3.5-haiku | 5.67 | 6.0 | 4.0 |
| deepseek/deepseek-chat-v3-0324 | 5.67 | 6.0 | 3.0 |
| meta-llama/llama-3.3-70b-instruct | 3.33 | 5.33 | 3.33 |
| meta-llama/llama-3.1-8b-instruct | **0.0** | 4.67 | 3.0 |
| qwen/qwen-2.5-7b-instruct | 3.0 | 4.33 | 2.67 |

- **Tamanho ≠ capacidade:** um *flash* barato (gemini-2.5-flash, 7/7) supera de longe um
  **70B** (llama-3.3-70b, 3.33 na prosa) e os 7-8B. A tese da "falsa inteligência" do dono
  está demonstrada: escolher modelo por porte/preço engana — para *esta* tarefa, o modelo
  importa mais que o tamanho.
- **Mesmo modelo, local vs nuvem:** llama-3.1-8b dá ~0 na prosa nos **dois** ambientes
  (drowna nos 17k tokens) e é resgatado pela AN (local 3.33 / nuvem 4.67). A fraqueza é do
  **modelo (8B)**, não do ambiente — bom controle.

## Veredito (claim recalibrado, agora reprodutível)

**Modelos de IA modernos aplicam o Strata** — em teste controlado e reprodutível (fixture
congelado, cego, baseline, N=3, desconfundido): vários sabores de nuvem (gemini-flash,
haiku, gpt-4.1-mini, deepseek-v3) detectam **5-7/7**; a **forma AI-nativa ajuda os dois
tiers** (local 4.58, nuvem 5.67) e é **necessária** para modelos pequenos (8B). A nuvem
**não satura** na prosa densa. **Ressalvas:** 1 documento, 1 projeto-alvo (validade
ecológica R8 pendente); N=3; juiz único Claude cego (R6 2º juiz pendente).
