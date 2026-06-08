---
title: P6 Fase A — shootout de FORMAS (F0/F1/F2/F4) — qual tutoria mínima rende no modelo barato?
created: 2026-06-08
setup: F0-bare (Strata canônico 53KB) / F1-checklist (2KB) / F2-AN-v3 (denso) / F4-etapas (multi-turn) × 4 modelos baratos (gpt-4.1-mini, gemini-2.5-flash, deepseek-v3, llama-3.3-70b) × NNN+pdf2md × N=1 · pontuação CEGA (juiz Claude) contra gabarito corrigido · qualidade = genuíno − falso-positivo
status: a TUTORIA importa monotonicamente — dar o texto CRU a um modelo barato é o pior; andaime ajuda; etapas (F4) é o único net-positivo; checklist (F1) é o melhor custo-benefício portátil
---

# P6-A — a forma é tudo (para o modelo barato)

Pergunta do dono: *o texto-base é auto-contido; o desafio é a FORMA que a IA executa. Qual a
tutoria MÍNIMA que faz um modelo barato/grátis aplicar bem, sendo o mais portátil possível?*

## Ranking das formas (qualidade média = genuíno − falso-positivo, 8 células cada)

| forma (tutoria crescente →) | qualidade | portabilidade |
|---|---|---|
| **F0 — bare** (Strata canônico cru, 53KB) | **−3.25** (pior) | máxima |
| F1 — checklist (2KB, gates sim/não) | −1.62 | **máxima** (1 prompt) |
| F2 — AN-v3 (denso, gates+etapas num prompt) | −1.38 | alta |
| **F4 — etapas** (multi-turn guiado) | **+0.12** (único positivo) | baixa (orquestrador) |

**O ranking é monotônico com a tutoria.** Confirma e **afia** a tese do dono: o texto *é*
auto-contido — **para um executor capaz**. Para um executor **barato**, entregá-lo **cru (F0)
é a PIOR opção** (mais ruído); cada grau de andaime melhora; só as **etapas (F4)** levam o
barato ao net-positivo.

## O trade-off que decide a estratégia: portátil × confiável

| forma | NNN (controle FP) | pdf2md (detecção real) | papel |
|---|---|---|---|
| **F4 etapas** | melhor (corta FP: −0.25) | +0.50 | **mais confiável**, menos portátil (4 chamadas + orquestrador) |
| **F1 checklist** | −3.00 | **−0.25, e VENCE nos bons**: gemini **+2**, deepseek **+1** | **mais portátil** (1 prompt 2KB), positivo na detecção |
| F2 AN-v3 | −2.75 | 0.00 | meio-termo denso |
| F0 bare | −3.50 | −3.00 | não usar com barato |

- Para **suprimir falso-positivo** (projeto exemplar), **F4** ganha — o passo-a-passo segura a
  alucinação (deepseek/llama/gpt zeram o FP com F4).
- Para **achar o real** (pdf2md), o **F1-checklist** já é positivo nos melhores baratos
  (gemini +2, deepseek +1) — com **um único prompt de 2KB**.

## Por modelo (quem responde a quê)
- **gemini-2.5-flash**: responde bem à forma; F1-checklist o deixa **+2** no pdf2md. Bom barato.
- **deepseek-v3**: idem (F1 +1 / F4 +1) — o mais consistente sob orientação.
- **gpt-4.1-mini**: fica **mudo** (0) em quase tudo — não alucina, mas também não acha.
- **llama-3.3-70b**: o mais difícil (negativo em quase tudo); **só o F4** o tira do vermelho.

## Veredito da Fase A
1. **Não entregue o Strata cru a um modelo barato (F0).** É o pior. A forma de invocação
   domina o resultado — exatamente a tese do dono.
2. **Duas formas valem para "tutorar com o mínimo":**
   - **F1-checklist** = a aposta de **reach/portabilidade**: 1 prompt de 2KB, positivo na
     detecção com gemini/deepseek. Para "máximo de pessoas, mais portátil" → esta.
   - **F4-etapas** = a aposta de **confiabilidade**: a única net-positiva, corta FP em todos;
     custo = multi-turn + orquestrador (menos portátil, mais chamadas).
3. **Leva para a Fase B (scatterplot):** **F1 + F4** (portátil vs confiável), no grid largo
   (baratos/grátis + reasoners + Opus de teto), para ver quais modelos chegam a "bom o
   bastante" com a forma portátil vs precisando da forma guiada.

## Caveats
- **N=1 por célula** — as células individuais (ex. gemini F1 +2) são sugestivas; o **ranking
  das formas** (média de 8 células) é o sinal robusto. A Fase B sobe o N nas vencedoras.
- Qualidade = genuíno − falso-positivo (gabarito corrigido pós-P0). 2 projetos.
