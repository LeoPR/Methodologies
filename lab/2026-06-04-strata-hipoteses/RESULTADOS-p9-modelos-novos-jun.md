---
title: 'P9 — spot-check dos modelos novos (jun/2026): a assinatura persiste; e o churn de L2 ao vivo'
created: 2026-06-14
updated: 2026-06-14
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

Para o gráfico `recipe/strata-com-ia-fronteira.svg` orientar o dev **por vendor e por gratuidade** (não por
nome, que churna), rodei 1 representante por vendor + 1 grátis no protocolo atual (s04 over-ação / s01
recall+segurança, K=5, temp 0,3). Reaproveitei 4 já medidos (P8/P9) e rodei os gaps (Anthropic, DeepSeek,
Z-ai, grátis). **Custo do gap ~US$1,79 (o Opus dominou) → saldo OpenRouter ~US$0,04: estouro da estimativa
de "~$1-1,5", registrado por honestidade.**

| vendor | modelo | custo | LIMPO over-ação (fabr.) | BAGUNÇADO recall · seg |
|---|---|---|---|---|
| Anthropic | claude-opus-4.8 | $$$ | **2,0** (1,4) ← o + calibrado | 2,8/4* · 4/5 |
| OpenAI | gpt-4.1 (forte) | $$ | 3,0 (**8,4**) | 4/4 · 5/5 |
| OpenAI | gpt-4o-mini (barato) | $ | 3,0 (3,4) | 2/4 · **~1/10 instável** |
| Google | gemini-2.5-flash | $ | 3,0 (6,6) | 4/4 · 5/5 |
| Google | gemini-3.1-flash-lite (nova) | $ | 3,0 (4,8 — < 2.5) | 4/4 · 5/5 |
| DeepSeek | deepseek-v3 | $ | 3,0 (4,8) | 3,6/4 · 3/5 |
| Z-ai | glm-4.6 | $ | **2,4** (2,8) | 4/4 · 5/5 |
| Grátis | llama-3.3-70b:free | 🆓 | **falhou** (rate-limit) | 1/10 rodou |

**Achados:**
1. **No projeto LIMPO, ninguém se abstém — nem o topo.** O Opus foi o **mais calibrado** (over-ação 2,0;
   1,4 fabricados, vs 3,0 e 3,4–8,4 dos outros), mas ainda levantou um falso-positivo (o §5 do parâmetro).
   Isso **revisa** o "só o Opus é confiável (abstém)" para **"o Opus é o mais calibrado, mas a abstenção
   total não acontece nem nele neste fixture"** — coerente com "capacidade oscila por fixture" (ADR-006).
   2º mais calibrado: glm-4.6 (2,4).
2. **No projeto BAGUNÇADO, a maioria pega o real (4/4) + segurança.** Falham o barato da OpenAI
   (gpt-4o-mini: recall 2/4, segurança **instável** ~1/10) e o deepseek-v3 (3/5).
3. **Grátis = instável:** llama-3.3-70b:free deu rate-limit (1 de 10). Confirma "sem opção grátis confiável".
4. **Caveats:** Opus **truncado** em 1500 tok (num-predict baixo) → recall s01 (2,8) provavelmente
   **subestimado**; K=5, temp 0,3, juiz único Claude. Sinais, não prova.
