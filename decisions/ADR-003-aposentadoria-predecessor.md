---
status: accepted
date: 2026-06-03
deciders: [Leonardo Marques, Claude Code]
project: Strata
---

# ADR-003 — Aposentadoria do predecessor: opção 0b (sem migrar bloco operacional)

## Contexto

`recipe/organization-methodology.md` continha um **bloco operacional** (fases
de adoção, assessment brownfield, auditoria periódica) que não foi migrado para
`knowledge-architecture.md` durante a reestruturação em camadas L0/L1/L2.

Duas opções antes de aposentar:
- **0a**: migrar o bloco operacional como "Parte IV — Adoção e operação".
- **0b**: aposentar sem migrar — o bloco é coberto implicitamente por L1/L2.

## Decisão

**Opção 0b** — aposentadoria imediata sem migrar o bloco operacional.

## Razão

- O conteúdo do bloco (fases de adoção, checklist de auditoria) são
  instâncias de L1/L2 já cobertos — não adicionam princípio L0 novo.
- Migrar criaria uma "Parte IV" sem fundamento novo no L0 — viola §9 (organizar
  tem custo; não organizar o que não é necessário ainda).
- O bloco não foi necessário no uso real do projeto até hoje (regra de três —
  §7/L1: não formalizar o que ocorreu uma vez).

## Consequências

- O bloco operacional **não está perdido**: está preservado em
  `lab/2026-06-03-predecessor/` (FROZEN — dogfood de §3).
- Se o bloco se mostrar necessário (recorrência ≥ 3), volta como candidato a
  Parte IV — nesse momento ancorado em experiência real, não antecipado.
- `organization-methodology.md` movido para `lab/2026-06-03-predecessor/`
  (tombstone no arquivo de README do predecessor).
- **Sinal de troca**: ao aplicar Strata a 2+ subprojetos reais e o processo de
  adoção emergir como fricção comum, abrir ADR-004 para Parte IV.
