---
title: 'P9 — spot-check dos modelos novos (jun/2026): a assinatura persiste; e o churn de L2 ao vivo'
created: 2026-06-14
updated: 2026-06-15
setup: 'Spot-check rápido do "tier novo" que o Copilot/VS Code passou a oferecer (gpt-5-mini, gpt-5-nano, gemini-3.1-flash-lite), nos dois sinais decisivos (s04 over-ação no limpo, s01 recall/segurança no bagunçado), variante canônica, K=5, temp 0.3, completion-only. Custo US$0,13.'
status: 'SINAL. A assinatura por tier PERSISTE entre gerações (barato age demais no limpo, pega o óbvio no bagunçado); a detecção do óbvio MELHOROU. Dois limites expostos: nomes de modelo churnam (L2) e os novos reasoners da OpenAI nem rodam no caminho completion-only básico.'
---

# P9 — como os modelos novos (jun/2026) se saíram

Motivado pela observação do dono: o Copilot atualizou tudo em junho (gpt-5-mini, gpt-5.x-codex,
gpt-5.4, "raptor"…) e *"o gpt-5 nem sei se está mais na lista"*. Pergunta: como o **tier novo** se sai?

## Resultado

| modelo | s04 — over-ação (méd±sd) / fabricados | s01 — recall /4 · segurança | execução |
|---|---|---|---|
| **gemini-3.1-flash-lite** | **3,0 ± 0** / 4,8 ([5,5,5,4,5]) | **4,0** · **5/5** | rodou 10/10 |
| **gpt-5-mini** (reasoning) | **1,0 ± 1** / 0,5 ([1,0]) · pegou o nit real | 3,2 · 4/5 | **parcial**: 2/5 erro, resto truncado |
| **gpt-5-nano** (reasoning) | — | — | **0/10** (`content=None`) |
| **raptor** | — | — | **ausente** do OpenRouter (codinome Copilot) |

## Leitura

1. **A assinatura por tier persiste entre gerações.** `gemini-3.1-flash-lite` repete o padrão **bimodal**
   do barato: **over-age no projeto limpo** (fabrica ~5 violações, verdict "PRECISA-MUITO" 5/5; falso-positivo
   §5 inclusive), mas **pega o óbvio no bagunçado** (recall 4/4). A §9 (abster-se no limpo) segue sendo **teto
   de capacidade** — não some com geração nova.
2. **O óbvio ficou mais confiável.** A detecção de **segurança** (§6-bis) do `gemini-3.1-flash-lite` foi **5/5**
   — onde a geração anterior (gpt-4o-mini, P8b) oscilava em ~10-20%. Capacidade subiu **na precisão do recall**,
   não na abstenção.
3. **`gpt-5-mini` é promissor mas não foi medido com justiça.** As poucas saídas válidas tiveram **over-ação
   baixa (1,0)** e foi o **único** (em todos os experimentos) a pegar o nit real do mapa — mas é **reasoning
   model**: estoura o orçamento de 2000 tok (truncou) e 2/5 voltaram vazias. Sinal promissor, não conclusão.

## Dois limites que isto expôs (a lição que vale mais que os números)

- **Nome de modelo é L2 e churna rápido.** O catálogo virou `gpt-5 → gpt-5.4`, `gemini-2.5 → 3.5`,
  `glm-4.6 → glm-5.1` em semanas. **Fixar a avaliação (ou o gráfico) a modelos específicos apodrece.** O que
  **dura** é o **padrão por tier**, não o modelo. (Mesma lição do ADR-005/L0-atemporal, agora no eixo modelo.)
- **A interface mudou: reasoners.** Os novos baratos da OpenAI (gpt-5-mini/nano) põem a resposta no canal de
  *reasoning* e devolvem `content=None` no caminho **completion-only básico** do harness (`call`). Pinar a
  avaliação a modelos específicos quebra **mecanicamente**, não só semanticamente.

## Para o BACKLOG

- **Caminho reasoning-aware no harness:** usar `call_ex(think=True)` (que já existe para `reasoning`/budget) no
  fluxo F1 do `hb_runner`, com orçamento de tokens maior, para medir `gpt-5-mini/nano`-class de forma justa.
  Sem isso, "como os reasoners se saem" fica **em aberto**.

*(Aplicação no produto: o gráfico/guia em `recipe/strata-com-ia.md` foi reframed para liderar pelo **tier**
e datar os modelos como exemplos de jun/2026. Não vamos perseguir cada release — §9.)*

## P9b — baseline por vendor × pago/grátis (base do gráfico, K=5)

Para o gráfico `recipe/strata-com-ia-fronteira.svg` orientar o dev **por vendor × barato/caro** (não por
nome, que churna), medi o **barato e o caro de cada vendor** no protocolo atual (s04 over-ação / s01
recall+segurança, K=5, temp 0,3), em duas rodadas: gaps iniciais (deepseek-v3, glm-4.6) + completar
barato/caro (**Haiku** mín Anthropic, **Opus refeito sem truncamento**, **gemini-2.5-pro** caro Google,
**glm-4.5-air** barato Z-ai). Reaproveitei OpenAI (gpt-4.1/gpt-4o-mini) e Google-flash já medidos. **Custo
total ~US$4,5; saldo OpenRouter ~US$7,3 (o dono repôs +$10).**

| vendor | modelo (tier) | custo | LIMPO over-ação (fabr.) | BAGUNÇADO recall · seg |
|---|---|---|---|---|
| Anthropic | **claude-opus-4.8** (caro, refeito s/ trunc.) | $$$ | **1,2** (2,6) ← o + calibrado | **4/4 · 5/5** |
| Anthropic | claude-haiku-4.5 (barato) | $ | 3,0 (**9,6!** — age + que todos) | 4/4 · 5/5 |
| OpenAI | gpt-4.1 (caro) | $$ | 3,0 (8,4) | 4/4 · 5/5 |
| OpenAI | gpt-4o-mini (barato) | $ | 3,0 (3,4) | 2/4 · **~1/10** |
| Google | gemini-2.5-pro (caro) | $$ | **não medido** (reasoner: saída degenerada) | — |
| Google | gemini-3.1-flash-lite (barato) | $ | 3,0 (4,8) | 4/4 · 5/5 |
| DeepSeek | deepseek-v3 (o caro=R1 é reasoner) | $ | 3,0 (4,8) | 3,6/4 · 3/5 |
| Z-ai | glm-4.6 (mais forte) | $ | **2,4** (2,8) | 4/4 · 5/5 |
| Z-ai | glm-4.5-air (barato) | $ | ~1,2 **INSTÁVEL** (fab 0–5) | 2,4/4 · **0/5 nunca** |
| Grátis | llama-3.3-70b:free | 🆓 | **falhou** (rate-limit, 1/10) | — |

**Achados:**
1. **O melhor (provar que funciona): Opus 4.8 — refeito sem truncamento.** over-ação **1,2** (a menor), recall
   **4/4**, segurança **5/5**. O truncamento da rodada anterior escondia o recall (2,8→4,0) e inflava a
   over-ação (2,0→1,2). É o + calibrado, mas **ainda não zera** no limpo (levanta o §5 ambíguo) — "o + calibrado, não um abstém-tudo".
2. **O mínimo que atende:** entre os baratos, **gemini-3.1-flash-lite** (pega 4/4 + segurança 5/5; age demais no
   limpo como todos). O glm-4.6 (mid) é o 2º + calibrado no limpo (2,4) e seguro (5/5).
3. **Caro ≠ melhor automático.** O **gemini-2.5-pro** (caro) é reasoner e **nem rodou** (saída degenerada, como
   gpt-5-mini/nano). E o **Haiku** (barato Anthropic) **age MAIS que todos** no limpo (9,6 fabricados) — então
   "Anthropic" não é uniformemente bom: o Opus calibra, o Haiku exagera.
4. **Segurança (§6-bis) falha nos + baratos.** Os caros/mid pegam **5/5**; falham **glm-4.5-air 0/5** (nunca
   pega), **gpt-4o-mini ~1/10**, **deepseek-v3 3/5**. É onde o barato mais arrisca.
5. **Instabilidade do barato:** glm-4.5-air oscila forte no limpo (fabricados [5,0,0,0,5], SD 1,47) — o barato
   não é só pior, é **imprevisível**.

**Caveats:** K=5, temp 0,3, juiz único Claude; s04/s01 (2 tipos de projeto). Sinais, não prova.

## P9c — escada por vendor do COPILOT (2026-06-15)

Com o **fix do reasoner** (`content←reasoning`) destravando GPT-5/Gemini-pro, rodei a **lista real do Copilot**
(via OpenRouter, que tem os mesmos modelos — caminho limpo, sem risco de ToS) como **escada por vendor**
(melhor → mínimo), no protocolo s04/s01. gpt-4.1 saiu (01/06)→GPT-5.5; Fable 5 suspenso→Opus 4.8 é o teto.

> **Refeito K=5 no topo (2026-06-15).** A primeira passada do topo (GPT-5.5 e Gemini 3.1 Pro) foi K=3 e
> **enganou** — a lição de variância (ADR-006) de novo. Com K=5 a nota **0–3 saturou** (quase todos = 3,0;
> só Opus 1,2 e Sonnet 2,6 ficam abaixo). O diferenciador real virou **quantos inventam**. Números abaixo
> já são K=5.

| vendor | modelo (tier) | LIMPO over-ação 0–3 (**inventa**) | BAGUNÇADO |
|---|---|---|---|
| **Anthropic** | Opus 4.8 (caro) | 1,2 (**2,6**) ← o + calibrado | 4/4 · 5/5 |
| | **Sonnet 4.6** (médio) | 2,6 (**3,8**) ← **mínimo que serve** | 4/4 · 5/5 |
| | Haiku 4.5 (barato) | 3,0 (**9,6**) floda o limpo | 4/4 · 5/5 |
| **OpenAI** | GPT-5.5 (topo, K=5) | 3,0±0 (**5,8** [6,5,8,5,5]) ← a melhor da OpenAI | 4/4 · 5/5 |
| | GPT-5 mini (base) | 3,0 (**7,4**) age demais | 4/4 · 5/5 |
| **Google** | **Gemini 3.1 Pro** (topo, K=5) | 3,0±0 (**2,8** [2,4,3,2,3]) ← inventa pouco | 4/4 · 5/5 |
| | Gemini 3 Flash (base) | 3,0 (**4,2**) age demais | 4/4 · 5/5 |

**Achados:**
1. **Sonnet 4.6 FUNCIONA** (responde "qual o próximo menor que o Opus"): over-ação 2,6 — entre Opus (1,2) e
   Haiku (3,0); pega o bagunçado 4/4 + segurança. É o **mínimo que serve** da Anthropic. Não iguala o Opus no
   limpo, mas é usável (rascunho a revisar).
2. **K=5 corrigiu o topo — variância de novo.** Com K=3, GPT-5.5 (2,67) e Gemini 3.1 Pro (1,67) **pareciam
   calibrados**; com K=5 ambos saturam a nota 0–3 em **3,0** (SD 0). A nota ordinal satura — o sinal fino é
   **inventados**: Gemini 3.1 Pro inventa **pouco (2,8)**, quase como o Opus (2,6), e **segue sendo o melhor do
   Google e perto do topo**; GPT-5.5 inventa **5,8** (a OpenAI age bem mais no limpo). O "2º + calibrado"
   anterior era ruído de N pequeno.
3. **No bagunçado, TODOS os 7 pegam tudo** (4/4 + segurança 5/5). O diferenciador é o **limpo**.
4. **Ladder por inventados (não pela nota, que saturou):** Opus 2,6 ≈ Gemini-Pro 2,8 < Sonnet 3,8 <
   Gemini-Flash 4,2 < GPT-5.5 5,8 < GPT-5-mini 7,4 < Haiku 9,6. Mais barato → inventa mais; ninguém zera.
5. **Apresentação:** o gráfico usa **inventados** como barra (a nota 0–3 saturou com K=5) e mostra só os
   usáveis. Os que **falham segurança** (gpt-4o-mini ~1/10, glm-4.5-air 0/5, deepseek 3/5) e o **grátis**
   (instável) ficam no caderno (P9/P9b), fora do gráfico — nunca plotados como zero.

**Caveats:** topo (GPT-5.5, Gemini 3.1 Pro) agora **K=5** (firme); base ainda K=3. Reasoners capturados via
fallback `reasoning` (o gemini-pro às vezes devolve o "pensar", não um plano limpo — tratado como usável quando
há diagnóstico). Juiz único Claude; s04/s01. Sinais, não prova.
