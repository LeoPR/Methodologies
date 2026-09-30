---
title: 'Resultados: acréscimo "Fonte declarada ≠ fonte usada" (Strata §5)'
created: 2026-09-30
updated: 2026-09-30
status: 'Etapa exploratória fechada: 8 modelos, 8 fabricantes. Regra 2 do pré-registro (alvo sobe, controles intactos): adotar com carimbo de testado. Decisão de aplicar ao canônico: dono.'
tags: [strata, s5, f6-fonte, a-b, resultados]
---

# Resultados: "Fonte declarada ≠ fonte usada" (Strata §5)

Plano, hipóteses, regras e red-team: [PREREG-strata-s5-fonte-declarada.md](PREREG-strata-s5-fonte-declarada.md).
Texto testado: [PROPOSTA-S5-fonte-declarada.md](PROPOSTA-S5-fonte-declarada.md) (delta
`eval/strata/variantes/s5-fonte-declarada.pt.md`). Instrumento: `runners/hb_f6s.py`, `verify/score_f6s.py`
v4.1, gabarito `f6-status-manifest.json`, `ops/run_f6s_fonte.sh`. Saídas brutas em
`eval/strata/planos/f6s-fonte/` (gitignored). Custo pago: US$ 1,86 (os demais pela NVIDIA grátis).

## Resposta

- **O acréscimo corrige o defeito que o motivou.** No alvo, o acerto sobe de 78% para 92%; os
  modelos que seguiam o arquivo declarado contra os resultados saem do erro.
- **Não gera desconfiança geral.** Nos três controles (declaração certa; nada contradiz a
  declaração; controle no outro domínio) o acerto fica dentro da margem pré-registrada.
- **O ponto fraco está no controle "vale por padrão".** Quando nada contradiz a declaração, 4 de 38
  respostas com o acréscimo falham (8 pontos abaixo do método atual, perto do limite de 10). Duas do
  gpt-6-luna declaram "indeterminado"; uma do gemma troca para a cópia sem traço; uma do muse declara
  conflito. É o risco que o red-team previu no ramo "se não casam com nenhuma, é indeterminada".
- **Regra aplicada: 2** (H1 sobe; H1b no teto; controles intactos; regressão estável): adotar no
  canônico com o carimbo de testado.

## Soma dos 8 modelos (acerto k/K; "fora" = sem as duas linhas, quase sempre truncamento)

| fixture | papel | sem método | v1.2.7 | com o acréscimo |
|---|---|---|---|---|
| `f6-tempo-s5` | alvo | 31/38 (82%) | 28/36 (78%) [2 fora] | **35/38 (92%)** |
| `f6-fonte-nova` | alvo fora da amostra | 38/38 (100%) | 37/38 (97%) | 36/38 (95%) (+1 parcial) |
| `f6-tempo-inverso` | controle | 37/37 (100%) [1 fora] | 38/38 (100%) | 38/38 (100%) |
| `f6-tempo-sem-traco` | controle "vale por padrão" | 38/38 (100%) | 37/38 (97%) (+1 parcial) | 34/38 (89%) |
| `f6-fonte-nova-inverso` | controle fora da amostra | 38/38 (100%) | 38/38 (100%) | 38/38 (100%) |
| `f6-sem-copia` | borda (descritiva) | 8/37 (22%) | 7/38 (18%) | 14/36 (39%) |
| `f6-indeterminado` | regressão | – | 28/38 (74%) | 27/37 (73%) |

## Hipóteses

| hipótese | resultado |
|---|---|
| H1: alvo sobe | **sim**: 0,78 → 0,92 (+0,14). muse 2/5 → 4/5; deepseek 0/3 → 3/3; gpt-6-luna 3/5 → 5/5 |
| H1b: fora da amostra +0,20 | **sem poder (teto)**: v1.2.7 já em 0,97 (regra de teto do pré-registro); com o acréscimo 0,95 |
| H2: controles −0,10 no máximo | **ok nos três**: inverso 1,00 → 1,00; sem traço 0,97 → 0,89 (−0,08); fora da amostra 1,00 → 1,00; parcial não sobe |
| H3: regressão | **ok**: 0,74 → 0,73 |

## Por fabricante (SEM · v1.2.7 · com o acréscimo)

| fabricante | alvo | fora da amostra | controle inverso | controle sem traço | controle fora | borda | regressão (v1.2.7 · acréscimo) |
|---|---|---|---|---|---|---|---|
| OpenAI (fechado) `gpt-6-luna` | 0/5 · 3/5 · 5/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · **3/5** | 5/5 · 5/5 · 5/5 | 0/5 · 1/5 · 5/5 | 5/5 · 5/5 |
| OpenAI (aberto) `gpt-oss-20b` | 5/5 · 5/5 · 4/5 | 5/5 · 5/5 · 4/5 | 4/4 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 0/4 · 0/5 · 0/5 | 0/5 · 0/5 |
| Google (fechado) `gemini-3.5-flash-lite` | 5/5 · 5/5 · 4/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 1/5 · 0/5 · 1/5 | 5/5 · 5/5 |
| Google (aberto) `gemma-4-31b-it` | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 4/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 4/5 | 5/5 · 5/5 |
| Meta `muse-glimmer-30b` | 5/5 · **2/5** · 4/5 | 5/5 · 5/5 · 4/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 4/5 | 5/5 · 5/5 · 5/5 | 0/5 · 0/5 · 0/5 | 5/5 · 5/5 |
| NVIDIA `nemotron-3-super` | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 2/5 · 1/5 · 0/5 | 0/5 · 0/5 |
| Z.ai `glm-5.3` | 5/5 · 3/3 · 5/5 | 5/5 · 4/5 · 5/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 5/5 · 5/5 · 5/5 | 0/5 · 0/5 · 3/3 | 5/5 · 4/4 |
| DeepSeek `deepseek-v4.1-flash` | 1/3 · **0/3** · 3/3 | 3/3 · 3/3 · 3/3 | 3/3 · 3/3 · 3/3 | 3/3 · 2/3 · 3/3 | 3/3 · 3/3 · 3/3 | 0/3 · 0/3 · 1/3 | 3/3 · 3/3 |

A classe mais comum por célula (consistência) está na saída do pontuador; na maioria das células ela
aparece em 4 ou 5 de 5.

**Alvo ∧ controle (o par que separa "siga os traços" de "o mais novo vence"):** com o acréscimo, 7 de 8
modelos acertam os dois em pelo menos 4 de 5; o muse fica em 4/5 ∧ 5/5; o gpt-6-luna, que errava o
alvo sem método (0/5), acerta os dois (5/5 ∧ 5/5).

## Achados

1. **O defeito era do método, e o acréscimo o desfaz.** No alvo, o método atual derruba o muse (5/5
   sem método → 2/5) e o deepseek segue errando (0/3); com o acréscimo, 4/5 e 3/3. O método atual
   ficava abaixo de "sem método" (78% × 82%); com o acréscimo, acima (92%).
2. **O ramo "indeterminado" dispara onde não devia.** No controle sem traço, "Se [os traços] não casam
   com nenhuma, ou se dividem, a resposta é indeterminada" é lido por alguns modelos como "não há traço,
   logo indeterminado". Candidato a ajuste de redação: restringir o ramo ao caso em que traços
   **contradizem** a declaração. Um texto ajustado exige novo teste antes de ser dito testado.
3. **Borda:** sem cópia, e com os resultados contradizendo o declarado, o acréscimo dobra o acerto
   (18% → 39%), puxado por gpt-6-luna (1/5 → 5/5) e glm (0/5 → 3/3). gpt-oss, muse e nemotron seguem
   apresentando o protocolo declarado.
4. **O domínio novo não discrimina**: todos acertam já sem método (teto). Ele não refuta nem confirma.

## Desvios e cobertura

- **Rota:** glm-5.3 e deepseek-v4.1-flash travaram na fila grátis da NVIDIA (timeouts, horas por
  chamada). O glm foi completado pelo OpenRouter nos mesmos pesos (as células já feitas na NVIDIA
  foram mantidas); o deepseek rodou a grade inteira pelo OpenRouter (K = 3), e as 25 saídas parciais
  da NVIDIA ficam só como descritivas (mesma direção: alvo 0/3 → 3/3).
- **Truncamento:** 8 saídas sem as duas linhas finais (quase todas do glm, que expõe o raciocínio na
  resposta e esgota o limite de 8.000 tokens). Fora do denominador, como pré-registrado.
- **Rótulo:** uma falha do muse no controle sem traço ("indeterminado – conflito entre ...") saiu ERRA
  quando a leitura é SUPER-AVISO. As duas classes são falha: o acerto não muda.
- **Temperatura:** 0,3 pela NVIDIA e no OpenRouter; GPT-6 ignora temperatura.

## Revisão manual (cega ao braço; de `planos/f6s-fonte-revisao.csv`)

| saída | classe | motivo |
|---|---|---|
| X1 (regressão, gpt-oss-20b) | LISTA-AMBOS | lista os dois protocolos lado a lado, sem avisar |
| X4, X5, X6, X7, X8 (glm-5.3) | SEM-LINHA | truncou no limite de tokens antes das duas linhas finais |

## O que isto permite dizer

- "O acréscimo ao §5 corrige o erro de seguir a fonte declarada contra a evidência de uso, sem
  gerar desconfiança geral": **sustentado** no exploratório (8 fabricantes, K = 3 a 5).
- "Ele não causa aviso à toa": **quase**; há sinal de excesso no caso sem traço, dentro da margem,
  concentrado no gpt-6-luna.
