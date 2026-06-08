---
title: P6 Fase B — scatterplot custo × qualidade (grid de 12 modelos) + overlay de etapas
created: 2026-06-08
setup: forma F1-checklist × 12 modelos ($0.02 a $7/M) × NNN+pdf2md × N=2 · F4-etapas overlay em 5 baratos · pontuação CEGA (juiz Claude, gabarito corrigido) · qualidade = genuíno − falso-positivo
status: cheap+portátil+bom = ESCOLHA DOIS. Só o teto (Opus) é claramente positivo com a forma portátil; etapas levantam os baratos ao custo da portabilidade
artifact: VIZ-p6-scatter.svg
---

# P6-B — a fronteira: custo × qualidade × portabilidade

Gráfico: [VIZ-p6-scatter.svg](VIZ-p6-scatter.svg) (X=custo log, Y=qualidade, △=reasoner,
☆=Opus, setas verdes = ganho das etapas F4 sobre a checklist F1).

## O scatter (forma F1-checklist portátil, 12 modelos, projetos reais)

| modelo | qualidade | custo≈$/M | nota |
|---|---|---|---|
| **claude-opus-4.8** ☆ | **+1.75** | 7.00 | único claramente positivo (teto) |
| o4-mini △ | +0.25 | 1.43 | melhor não-Opus (reasoner) |
| gpt-4.1-mini | 0.00 | 0.52 | break-even |
| gemini-2.5-flash | −0.25 | 0.52 | break-even |
| gemini-2.5-flash-lite | −1.00 | 0.13 | |
| deepseek-r1 △ | −1.00 | 0.88 | reasoner não salva |
| deepseek-chat-v3 | −2.25 | 0.26 | |
| qwen-2.5-72b | −2.75 | 0.36 | |
| gpt-4.1-nano | −3.25 | 0.13 | |
| llama-3.3-70b | −3.50 | 0.12 | |
| llama-3.1-8b | −5.25 | 0.02 | mais barato = pior |
| mistral-small-24b | −5.50 | 0.09 | |

**Três leituras do gráfico:**
1. **Custo NÃO compra qualidade entre os baratos.** Os mais baratos (llama-8b $0.02, mistral
   $0.09) são os PIORES (−5.25, −5.5). A qualidade só aparece no patamar ~$0.5 (gpt-4.1-mini,
   gemini-flash empatam em 0) e claramente no teto (Opus, $7). Não há almoço grátis.
2. **Só o teto é positivo com a forma portátil.** Re-confirma o P0: capacidade domina. Com
   um único prompt (F1), os baratos no máximo empatam (não pioram, mas quase não ajudam).
3. **Raciocínio (think) ajuda DESIGUAL:** o4-mini (+0.25) é o melhor não-Opus; mas deepseek-r1
   (−1.00) é medíocre. "Pensar" não é garantia.

## O overlay de etapas (F4) — as setas verdes

Onde a forma portátil falha, as **etapas (F4, multi-turn guiado) levantam os baratos**:

| modelo | F1 (portátil) | F4 (etapas) | ganho |
|---|---|---|---|
| **deepseek-v3** | −2.25 | **+0.50** | **+2.75** (vira positivo, a $0.26/M!) |
| mistral-small | −5.50 | −0.50 | +5.00 |
| gemini-2.5-flash | −0.25 | 0.00 | +0.25 |
| gpt-4.1-mini | 0.00 | 0.00 | +0.00 |
| llama-3.1-8b | −5.25 | −4.50 | +0.75 (o mais fraco resiste) |

Média do subconjunto: **F1 −2.65 → F4 −0.90** (+1.75 só pela forma). **deepseek-v3 + etapas
(+0.50 a $0.26/M)** fica competitivo com o o4-mini (+0.25 a $1.43) — mais barato e positivo.

## A resposta à pergunta do dono: cheap + portátil + bom = **ESCOLHA DOIS**

Não dá para ter os três num projeto real difícil. A fronteira tem três pontos úteis:

1. **Máxima qualidade (qualquer custo):** **Opus + F1** (+1.75). Capacidade resolve.
2. **Barato + portátil (aceitando neutro):** **gpt-4.1-mini ou gemini-2.5-flash + F1-checklist**
   (~0 a ~$0.5/M). O "piso portátil seguro": 1 prompt de 2KB, não adiciona ruído — mas também
   quase não adiciona sinal. Bom como **filtro** do que está claramente mal.
3. **Barato + bom (sacrificando portabilidade):** **deepseek-v3 + F4-etapas** (+0.50 a $0.26/M).
   O melhor ponto "acessível e realmente útil" — mas precisa do orquestrador multi-turn.

## Nuance importante (por tipo de projeto)
As médias acima incluem o **NNN exemplar**, onde QUALQUER achado é falso-positivo — isso
puxa todos para baixo. Na Fase A, no **pdf2md (com problemas reais)**, os baratos com F1 já
eram positivos (gemini +2, deepseek +1). Ou seja: **o barato acha problema óbvio, mas peca na
RESTRIÇÃO** (não consegue dizer "está limpo"). As etapas (F4) adicionam essa restrição. O
ponto cego continua sendo o §3/§8 temporal (H-D) e o §5 sutil.

## Caveats
- Qualidade = genuíno − falso-positivo (gabarito corrigido). 2 projetos, N=2 (F1) / N=1 (F4).
- Custo = proxy $/M (in×0.9 + out×0.1, prompt domina). Não inclui o custo extra de 4× chamadas do F4.
- Juiz Claude cego; padrão consistente com Fase A e com o 2º juiz do P1+P2.
