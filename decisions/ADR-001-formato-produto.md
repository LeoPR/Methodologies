---
status: accepted
date: 2026-06-03
deciders: [Leonardo Marques, Claude Code]
project: Strata
---

# ADR-001 — Formato do produto: 1 arquivo vs suíte de docs

## Contexto

A metodologia poderia ser expressa como (a) **1 arquivo único** com todas as
técnicas, ou (b) **suíte de 10 arquivos temáticos** (doc×code, lab work,
versioning, etc.), cada um menor e focado.

O experimento de split foi feito em `lab/2026-06-03-modernizacao/experimento-split/`
para avaliar a opção (b) antes de decidir.

## Decisão

**1 arquivo único** (`recipe/knowledge-architecture.md`).

## Razão

- §5 (fonte única): cada técnica tem uma fonte canônica — 10 arquivos criam 10
  pontos de divergência potencial e N versões de "o que fazer".
- §2 (achabilidade): para agentes de IA e humanos consultando sob demanda, 1
  arquivo é carregado no contexto inteiro; 10 exigem routing + coordenação.
- §9 (economia): a fragmentação acrescenta overhead de navegação sem ganho
  proporcional — o volume é gerenciável num monolito estruturado por camadas.
- A suíte de 10 revelou sobreposição inevitável entre os arquivos: impossível
  separar limpo sem duplicar.

## Consequências

- O arquivo cresce com as camadas; a organização interna (L0/L1/L2 + headers)
  substitui a organização de sistema de arquivos.
- A suíte de 10 ficou como registro FROZEN em `lab/` (dogfood de §3: não apagar,
  registrar).
- **Sinal de troca**: se o arquivo ultrapassar ~2000 linhas e a navegação interna
  degradar, reconsiderar split — mas preservar a unidade de §5.
