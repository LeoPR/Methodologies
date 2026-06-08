---
title: R6 — 2º juiz independente (não-Claude) sobre o tier nuvem
created: 2026-06-07
setup: gpt-4.1-mini (via OpenRouter) re-pontua CEGO os 63 planos nuvem; compara com o juiz Claude
status: viés de juiz endereçado — conclusão robusta; absolutos dependem do juiz
---

# R6 — o 2º juiz valida a conclusão (e mede o viés)

Fecha o último caveat metodológico grande (juiz único Claude, com participante da
família Claude no set). Um juiz **não-Claude** (gpt-4.1-mini) re-pontua **cego** os
mesmos 63 planos da nuvem, contra o mesmo gabarito.

## det_found médio por braço, por juiz

| braço | juiz Claude | juiz gpt-4.1-mini |
|---|---|---|
| baseline | 3.43 | 4.62 |
| prosa | 4.24 | 5.43 |
| **AN-v2** | **5.67** | **6.52** |

**AN > prosa > baseline vale com os dois juízes.** Deltas quase idênticos:
AN−prosa +1.43 (Claude) / +1.09 (gpt); prosa−baseline +0.81 em ambos. **A descoberta
do H-C é robusta à escolha do juiz** — o que importava (ordenação + deltas) se mantém.

## Concordância

- **MAE(det_found) = 1.14** (escala 0-7); o gpt-4.1-mini é **~1 ponto mais leniente**
  (viés médio Claude−gpt = −1.08). **Lição:** reportar **deltas e ordenação**, não
  números absolutos como verdade — o nível depende do juiz.
- **Concordância "found" por problema:** P1 0.94 · P7 0.90 · P4 0.89 · P5 0.86 ·
  P6 0.76 · P3 0.71 · **P2 0.56**. Os gates **críticos** (conflito, fail-open,
  honestidade) têm alta concordância; os **"moles"** (P2 datas, P3 readme) é onde os
  juízes divergem.

## Teste de viés — o juiz Claude favorece modelos Claude?

| modelos avaliados | Claude − gpt (det_found) |
|---|---|
| **Claude (haiku)** | **−0.33** |
| não-Claude | −1.20 |

O juiz Claude foi **~0.87 ponto relativamente mais generoso** com o haiku do que o juiz
neutro foi. **Indício LEVE de favoritismo de família** — coerente com a preocupação da
auditoria. **Ressalvas:** n minúsculo (1 modelo Claude, 9 planos), poder estatístico
baixo; e **não altera a conclusão** (o "AN ajuda os dois tiers" não depende da célula
Claude — ver `RESULTADOS-tier-nuvem-limpo.md`).

## Veredito
Caveat de juiz **endereçado**: a conclusão central (AN > prosa > baseline; AN resgata os
gates de julgamento) **sobrevive a um 2º juiz de outra família**. Recomendações
operacionais: (1) reportar deltas, não absolutos; (2) **não** usar célula Claude-julga-
Claude como âncora de claim (o que já não fazemos); (3) para decisão de promoção, manter
2 juízes nas células decisivas. Pendentes do plano: R5 (N≥5), R8 (projetos reais), R7 (sandbox).
