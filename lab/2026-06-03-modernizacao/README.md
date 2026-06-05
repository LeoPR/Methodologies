---
title: Modernizacao + reorganizacao da metodologia de organizacao
status: closed
created: 2026-06-03
updated: 2026-06-03
tags: [methodology, modernization, ai-2026, split-experiment]
outcome: partial
---

# Pesquisa: modernizar e reorganizar a metodologia de organizacao

## Pergunta cientifica

Como modernizar a metodologia de organizacao (originalmente 1 monolito de
~2k linhas) para os ambientes de IA de 2026 e para organizacao de documentos
em geral — e qual **estrutura de entrega** serve melhor (1 arquivo unico vs
suite multi-doc)?

## Hipoteses

- **H1**: o monolito esta desatualizado na camada de IA (faltam MCP, Agent
  Skills, memoria moderna, context engineering, evals, proveniencia).
  → **CONFIRMADA** (ver `analise-5-lentes.md`).
- **H2**: dividir em suite multi-doc melhora tempo de leitura / clareza /
  busca. → **PARCIAL**: melhora navegacao, mas o produto desejado e' **1
  arquivo**; o split vira artefato de pesquisa, nao o produto.

## Metodo

- **Analise multi-agente** (5 lentes, com verificacao web): inventario de
  conceitos · gaps IA-2026 · modernizacao doc-org · simplificacao/split ·
  freshness/consistencia. Saida em `analise-5-lentes.md`.
- **Experimento de estrutura**: split do monolito em 10 docs focados
  (`experimento-split/`).

## Resultado

- ~155 conceitos catalogados; ~15 gaps IA-2026 web-verificados; plano de
  simplificacao + arquitetura de split. Detalhe em `analise-5-lentes.md`.
- Suite de 10 docs em `experimento-split/` (**FROZEN**).

## Discussao / decisao

- **Produto final = 1 arquivo**: [`../../recipe/organization-methodology.md`](../../recipe/organization-methodology.md),
  consolidando todas as tecnicas + a modernizacao IA-2026. O split fica como
  registro de pesquisa (este experimento).
- A camada IA-2026 e' **alta cadencia** — re-verificar a cada auditoria.

## Limitacoes / notas

- `experimento-split/` e' **FROZEN** (nao editar — "frozen = imutavel").
- A subagent-workflow de extracao paralela falhou por "monthly spend limit";
  os 10 docs foram escritos diretamente.
- Os caminhos relativos `../../../dev-environment/` dentro de
  `experimento-split/` foram calculados pra profundidade do local original
  (raiz de `Methodologies/`) — ficam **stale** neste nivel mais profundo; nao
  corrigidos por serem registro congelado. No produto (`recipe/`) o caminho
  e' recalculado corretamente.
