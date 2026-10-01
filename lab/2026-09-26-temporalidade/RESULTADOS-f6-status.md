---
title: 'Resultados F6-status: o parágrafo "Ler o tempo de volta" (Strata §3)'
created: 2026-09-29
updated: 2026-10-01
status: 'Etapa 1 (exploratória) fechada: 8 modelos, 6 fabricantes. Sinal fraco e heterogêneo do parágrafo; efeito forte do método atual. Não confirmatório.'
tags: [strata, temporalidade, f6-status, a-b, resultados]
---

# Resultados F6-status

Plano, hipóteses, regras de decisão e desvios: [PREREG-strata-s3-ler-tempo.md](PREREG-strata-s3-ler-tempo.md).
Instrumento: `eval/strata/runners/hb_f6s.py`, `verify/score_f6s.py` (v3), gabarito
`eval/strata/f6-status-manifest.json`, delta `eval/strata/variantes/s3-ler-tempo.pt.md`.
Saídas brutas em `eval/strata/planos/f6s-piloto/` (gitignored). Custo total: US$ 0,15 (só os
dois fechados; o resto pela NVIDIA grátis).

## Resposta

- **O método atual (v1.2.6) já faz a maior parte.** Contra "sem método", o aviso sobe cerca de 25
  pontos nos dois alvos.
- **O parágrafo novo acrescenta pouco e de forma desigual:** +13 pontos no `f6-indeterminado`, +2
  no `f6-agora`, somando os 8 modelos. Abaixo do limiar de 20 pontos do pré-registro.
- **O fabricante pesa mais que o texto.** Há modelos que já avisam sem método (gpt-6-luna, glm-5.3)
  e modelos que nenhum texto move (nemotron-3-super, gpt-oss-20b).
- **O controle não foi ferido pelo parágrafo.** O custo aparece em outro lugar: o **método** (as
  duas versões) faz dois modelos seguirem a "fonte canônica declarada" contra a evidência (abaixo).
- Regra aplicada: **5 (heterogêneo por fabricante)**. Nada mais pago se justifica.

## Soma dos 8 modelos (acerto k/K; fora do denominador: sem linha e truncados)

| fixture | papel | sem método | v1.2.6 | com parágrafo |
|---|---|---|---|---|
| `f6-indeterminado` | alvo: avisar que não dá para saber | 15/38 (39%) | 23/38 (61%) | 28/38 (74%) |
| `f6-agora` | alvo: não afirmar "mais recente" sem data | 12/38 (32%) | 23/38 (61%) | 24/38 (63%) |
| `f6-tempo` | controle: decidir quando dá | 28/38 (74%) | 22/33 (67%) | 28/36 (78%) |

## Por fabricante

**`f6-indeterminado`**

| fabricante | modelo | sem método | v1.2.6 | com parágrafo |
|---|---|---|---|---|
| OpenAI (fechado) | `openai/gpt-6-luna` | 5/5 | 5/5 | 5/5 |
| OpenAI (aberto) | `openai/gpt-oss-20b` | 1/5 | 2/5 | 1/5 |
| Google (fechado) | `google/gemini-3.5-flash-lite` | 0/5 | 2/5 | 4/5 |
| Google (aberto) | `google/gemma-4-31b-it` | 0/5 | 4/5 | 5/5 |
| Meta | `meta/muse-glimmer-30b` | 4/5 | 4/5 | 5/5 |
| NVIDIA | `nvidia/nemotron-3-super-120b-a12b` | 0/5 | 0/5 | 0/5 |
| Z.ai | `z-ai/glm-5.3` | 3/5 | 4/5 | 5/5 |
| DeepSeek | `deepseek-ai/deepseek-v4.1-flash` | 2/3 | 2/3 | 3/3 |

**`f6-agora`**

| fabricante | modelo | sem método | v1.2.6 | com parágrafo |
|---|---|---|---|---|
| OpenAI (fechado) | `openai/gpt-6-luna` | 5/5 | 5/5 | 5/5 |
| OpenAI (aberto) | `openai/gpt-oss-20b` | 0/5 | 0/5 | 0/5 |
| Google (fechado) | `google/gemini-3.5-flash-lite` | 0/5 | 4/5 | 2/5 |
| Google (aberto) | `google/gemma-4-31b-it` | 0/5 | 1/5 | 4/5 |
| Meta | `meta/muse-glimmer-30b` | 1/5 | 5/5 | 5/5 |
| NVIDIA | `nvidia/nemotron-3-super-120b-a12b` | 0/5 | 0/5 | 0/5 |
| Z.ai | `z-ai/glm-5.3` | 5/5 | 5/5 | 5/5 |
| DeepSeek | `deepseek-ai/deepseek-v4.1-flash` | 1/3 | 3/3 | 3/3 |

**`f6-tempo` (controle)**

| fabricante | modelo | sem método | v1.2.6 | com parágrafo |
|---|---|---|---|---|
| OpenAI (fechado) | `openai/gpt-6-luna` | 0/5 | 0/5 | 3/5 |
| OpenAI (aberto) | `openai/gpt-oss-20b` | 5/5 | 5/5 | 5/5 |
| Google (fechado) | `google/gemini-3.5-flash-lite` | 5/5 | 4/5 | 5/5 |
| Google (aberto) | `google/gemma-4-31b-it` | 5/5 | 5/5 | 5/5 |
| Meta | `meta/muse-glimmer-30b` | 5/5 | 3/5 | 2/5 |
| NVIDIA | `nvidia/nemotron-3-super-120b-a12b` | 4/5 | 5/5 | 5/5 |
| Z.ai | `z-ai/glm-5.3` | 3/5 | – (4 truncados) | 3/3 |
| DeepSeek | `deepseek-ai/deepseek-v4.1-flash` | 1/3 | 0/3 | 0/3 |

Consistência (classe mais comum por célula, vezes/K) está na saída do pontuador; na maioria das
células a classe mais comum aparece em 4 ou 5 de 5.

## Achados

1. **Verificação inventada.** No `f6-agora`, gpt-oss-20b e gemma afirmaram versões inexistentes da
   biblioteca fictícia ("a mais recente é 4.3", "consultando a base atual, já evoluiu além da 4.2").
   É a falha mais perigosa; o pontuador v3 a conta como falha com precedência.
2. **Fonte canônica declarada contra a evidência (§5).** Com o método no prompt (as duas versões),
   muse e deepseek passam a usar `protocolo.md` porque o leia-me o declara canônico, e tratam o
   protocolo que os resultados seguiram como "drift a sinalizar". Sem método, o muse acerta 5/5. O
   gpt-6-luna erra esse controle até sem método. É um achado sobre o Strata, não sobre o parágrafo:
   falta ao §5 dizer o que prevalece quando a declaração e a evidência divergem.
3. **Não escolher não é avisar.** gpt-oss-20b e gemini-flash-lite listam os dois protocolos lado a
   lado sem dizer que não dá para saber qual vale (classe LISTA-AMBOS, parcial).
4. **Modelos que o texto não move.** nemotron-3-super escolhe sem ressalva e afirma "sim" em todos
   os braços.

## Desvios e cobertura

- Sem Mistral (404 na NVIDIA) nem Moonshot (kimi-k3 e kimi-k2.6: timeout e depois 404). Qwen não
  rodou (não está na NVIDIA; capacidade se mede na nuvem).
- Células incompletas: glm-5.3 no controle v1.2.6 (4 respostas truncadas no limite de 8.000 tokens,
  com raciocínio); deepseek-v4.1-flash com K = 3 e uma célula com K = 2 (timeouts na fila grátis).
- Pontuador em três versões, todas só de leitura e cegas ao braço (PREREG, desvios).
- Temperatura 0,3 pela NVIDIA; GPT-6 ignora temperatura.

- **Ressalva (2026-10-01): temperatura do Gemini.** As 45 chamadas do gemini-3.5-flash-lite foram servidas
  como `openrouter/Google`, o endpoint Vertex. Pelo catálogo do OpenRouter consultado em 2026-09-30, ele não
  aceita `temperature`, e sem rota fixa o parâmetro é descartado em silêncio. É provável que esse modelo
  tenha rodado na temperatura padrão do fabricante, e não em 0,3. O catálogo da data da rodada não foi
  conferido. O efeito esperado é sobre a consistência entre runs, não sobre a direção dos resultados.

## Revisão manual (transcrita de `planos/f6s-piloto-revisao.csv`)

| saída | classe | motivo |
|---|---|---|
| indeterminado / SEM / gpt-oss-20b r5 | LISTA-AMBOS | lista os dois protocolos lado a lado, sem avisar |
| tempo / S126 / gpt-oss-20b r3 | ACERTA | todos os parâmetros atribuídos a `protocolo_copia.md` |
| agora / S126 / gpt-oss-20b r5 | AFIRMA-NAO | "Não." sem justificativa nem qualificação |
| agora / S127 / gpt-oss-20b r3 | AFIRMA-NAO | "a 4.2 não é a mais recente disponível", sem base |
| indeterminado / SEM / deepseek r2 | DECLARA-INDETERMINADO | "não indicam qual é o vigente" |
| tempo / S126 / muse r2 | ACERTA | elege a cópia; diz que `protocolo.md` é inconsistente |
| tempo / S127 / muse r5 | ERRA | elege `protocolo.md`, embora registre o conflito |
| tempo / S126 / deepseek r2, r3 | ERRA | `protocolo.md` como canônico; cópia e resultados como drift |
| tempo / S127 / deepseek r1, r2, r3 | ERRA | idem |
| tempo / S127 / gpt-6-luna r4 | ACERTA-COM-RESSALVA | elege a cópia, marcada como inferida |

## O que isto permite dizer

- "O Strata atual faz modelos de vários fabricantes avisarem mais quando o tempo não se resolve":
  sinal consistente em 6 de 8, exploratório (K = 3 a 5).
- "O parágrafo novo melhora isso": **não sustentado** como efeito geral; sinal pequeno e desigual.
- Adotar o parágrafo no canônico é decisão editorial (norma útil ao leitor), sem alegação de efeito.
