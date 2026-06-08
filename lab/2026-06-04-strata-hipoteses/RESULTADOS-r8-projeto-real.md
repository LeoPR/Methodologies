---
title: R8 — validade ecológica num projeto REAL (pdf2md) — o método PIOROU
created: 2026-06-08
setup: digest da camada de organização do pdf2md (real, privado) · AN-v2/prosa/baseline × 4 sabores nuvem × N=2 · pontuação CEGA contra base-de-verdade real
status: DISCONFIRMAÇÃO importante — o ganho do sintético NÃO generaliza p/ projeto real bem-organizado
---

# R8 — o teste ecológico que tempera tudo

Primeiro teste num **projeto real** (pdf2md), não no fixture sintético. Base-de-verdade
real: RI1 = duplicatas `-DESKTOP-SG30VJF` conflitantes (§5 fonte-única + §3 superfície);
RI2 = versão inconsistente (pyproject `0.1.0-dev` vs `0.7.0`). Controles positivos: o
`DIARIO.md` (datas+rationale) e o `CHANGELOG.md` (SemVer) são **bons** — criticá-los = alucinação.

## Resultado (4 sabores nuvem × N=2; pontuação cega)

| braço | RI1 dupes | RI2 versão | genuínos (méd) | **alucinação (méd)** | criticou-o-bom | priorizou |
|---|---|---|---|---|---|---|
| **baseline** (sem método) | **1.00** | **1.00** | 1.5 | **0.00** | 0.38 | **1.00** |
| prosa (Strata) | 0.75 | 0.38 | 1.38 | 0.75 | 0.62 | 0.50 |
| AN-v2 | 0.88 | 0.38 | 1.12 | **1.00** | 0.38 | 0.50 |

## A descoberta (contra-intuitiva e honesta)

**No projeto real, a competência pura (baseline) GANHOU do método.** O baseline achou os
dois problemas reais (100%), **não alucinou nada** e priorizou. Dar o Strata ao modelo
(prosa ou AN) **piorou**: achou o problema óbvio **menos** (distraído aplicando o
framework), **alucinou mais** (inventou ADR faltando; criticou o DIÁRIO/CHANGELOG que são
bons como se violassem §3/§4/§8) e priorizou pior.

**Por quê:** o fixture sintético era **denso em problemas plantados** (cada arquivo tinha
um) → os gates do método ajudavam a varrer. Um projeto real **bem-organizado** tem
problemas **esparsos** + boas práticas; aí o método **prima o modelo a "caçar
violações"** → falso-positivo. **Os modelos violaram o §9 (economia/proporcionalidade)**
do próprio Strata ao super-aplicá-lo. Ironia que valida o §9 como o gate mais importante —
e que os modelos são os primeiros a furar.

## O que isto faz com as conclusões anteriores

- **Não invalida** o sintético (lá a AN realmente ajuda a achar problemas densos), mas
  **mostra que NÃO generaliza** para projeto real bem-organizado.
- **Recoloca o uso do Strata**: melhor como **checklist que um humano aplica com
  julgamento** do que como **auto-auditor de IA** que sai marcando violações. Como
  auto-auditor em projeto decente, ele **gera ruído** (falso-positivo).
- O **baseline** (competência genérica) é forte E honesto em dado real — a "competência
  vs método" pende para competência quando o projeto já é bom.

## Caveats
- **1 projeto real**, e **bem-organizado** (DIÁRIO/CHANGELOG bons). Num projeto real
  **bagunçado** (denso em problemas reais) o método pode ajudar — como no sintético.
  Próximo R8 deveria incluir um projeto real **messy** (ex.: NNN/TCF) p/ ver o outro extremo.
- N=2 por célula; 4 sabores; digest = só a camada de organização (curada por mim).
- Pontuação cega ao modelo, mas o juiz (Claude) conhece a base-de-verdade que EU defini.

## Veredito
**Validade ecológica MISTA, com um alerta forte:** num projeto real bem-organizado, o
Strata como prompt de auto-auditoria **induz alucinação e perde para a competência pura**.
A hipótese provável: **o método ajuda onde há problemas densos; atrapalha (falso-positivo)
onde o projeto já é bom.** Isso é o achado mais importante do reteste para a maturidade do
produto — e exige decidir o **modo de uso** (humano-com-julgamento vs auto-auditor) antes
de qualquer claim de produto.
