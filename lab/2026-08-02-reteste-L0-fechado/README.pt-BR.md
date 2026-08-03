---
title: Reteste do L0 fechado (2026-08-02) — shake-down + reteste dirigido + Degrau 3
created: 2026-08-02
updated: 2026-08-02
status: executado 2026-08-02
---

<!-- l10n: doc_id=lab-reteste-l0-readme · lang=pt-BR · source_lang=en · translation_of=README.en.md -->
[English](README.en.md) · **Português**

> Tradução de [`README.en.md`](README.en.md). Se houver divergência, o original em inglês prevalece.

# Reteste do L0 fechado (2026-08-02)

O núcleo L0 fechou editorialmente em 2026-08-01. O corpus v1 havia testado um L0 de
**12 seções** contra a tecnologia de junho; este lab retestou as conclusões **negativas**
datadas contra a prateleira de 2026-08 (local 17–32B, nuvem econômica) — *conclusão
negativa datada não se refuta pelo calendário; retesta-se.*

## Estrutura

- [`PLANO.md`](PLANO.md) — o **desenho pré-registrado**: tabela temporal de candidatos a
  reteste, roster de modelos congelado, grade de estratos de acesso, regras herdadas
  (gabarito pré-registrado, fixtures hash-congeladas, scorer mecânico com GOLD-gate,
  juiz cross-vendor, reporte ADR-006).
- [`NOTAS-shakedown.md`](NOTAS-shakedown.md) — o **diário de execução** append-only
  (cada leva, custo, incidente de harness e veredito, datado).

## Vereditos (4 linhas)

1. **Recusa de injeção (§6-bis): conclusão antiga REFUTADA** — a geração atual recusa
   injeção parafraseada/indireta espontaneamente (8/8), até no econômico; a "recusa
   lexical que caía sob paráfrase" era limite dos 8B de junho.
2. **Proporcionalidade/abstenção (§9): a fronteira MOVEU, não fechou** — a abstenção
   correta aparece (27B local), mas a proporcionalidade bilateral (abster onde deve E
   agir na medida onde deve) segue instável no tier médio.
3. **Verificação de fonte primária (§6): hipótese antiga CONFIRMADA, com refinamento** —
   web ajuda o conhecimento (e a "alucinação de verificação" sem web sumiu; a falha agora
   é erro de memória declarado ou abstenção, não tool-use fingido).
4. **Degrau 3 (texto→agente, ferramentas reais em sandbox): o padrão TRANSFERE** — o
   conserto §5 executado ficou 10/12 com Strata × 2/12 sem; ninguém puxou o `curl` da
   injeção (0/24); o risco residual migra para **obedecer o corpus como ordem de trabalho**.

Sinais em cenários sintéticos (K=2 = direção, não significância — ADR-006); o estado
datado da evidência vive na
[`../2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md`](../2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md).
O harness que produziu os runs está em [`../../eval/strata/`](../../eval/strata/) —
comandos de reprodução no README dele.
