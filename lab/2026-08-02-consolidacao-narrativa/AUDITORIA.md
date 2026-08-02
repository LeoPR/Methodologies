---
name: auditoria-consolidacao-narrativa
type: registro
status: etapa 1 (rastreabilidade) executada 2026-08-02; etapa 2 (tom) pendente
created: 2026-08-02
updated: 2026-08-02
audience: ai-primary
---

# AUDITORIA — Consolidação narrativa (2026-08-02)

Registro datado da auditoria narrativa do corpus, disparada depois que o
reteste do L0 fechado (lab `2026-08-02-reteste-L0-fechado/`) moveu o estado da
evidência e deixou docs de superfície para trás.

## A régua do dono (4 linhas)

1. Sem tom de diário nos docs publicados — diário vive nas NOTAS dos labs.
2. Toda afirmação segue hipótese → teste → conclusão, com rastreabilidade.
3. Impessoal, mas Plain Language (ver `ESTILO-REDACAO.md`).
4. Rastreabilidade primeiro, tom depois: conserta-se o fato antes do estilo.

## Achados

| Documento | Problema | Tipo | Sev | Correção |
|---|---|---|---|---|
| ARQUITETURA-E-EVIDENCIAS.md | hub se declara fonte canônica mas sem entrada 2026-08-02; F3/F5/agente datados (l33,39-41,113,158-159) | RASTREABILIDADE | alta | entrada datada + recalibrar linhas |
| recipe/documentacao-multilingue.md:123-126 | fila diz recipe/README e o-que-voce-ganha "sem par" — falso hoje | RASTREABILIDADE | alta | atualizar tabela |
| FECHAMENTO-avaliacao-strata.md:l70+passo9 | gaps já fechados (completion-only, s04) como abertos | RASTREABILIDADE | alta | entrada datada 2026-08-02 |
| recipe/strata-com-ia.md | tabela de decisão + SVG no roster jun/2026 | RASTREABILIDADE | alta | grade 2026-08 |
| lab/2026-08-02-reteste-L0-fechado/PLANO.md | status "shake-down em curso" — já executado | RASTREABILIDADE | média | status executado |
| MAP.md | árvore sem lab/2026-08-02-reteste-L0-fechado; trilha "prova" só ao hub | RASTREABILIDADE | média | adicionar + apontar OPINIAO |

## Plano em etapas

- **Etapa 1 — RASTREABILIDADE (esta):** corrigir os 6 achados acima; cada doc
  ganha o fato datado, apontando à fonte (ADR-005), sem duplicar número
  volátil. Estado da evidência 2026-08: fonte única é a
  [`OPINIAO-DE-USO`](../2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md) +
  [`NOTAS-shakedown`](../2026-08-02-reteste-L0-fechado/NOTAS-shakedown.md).
- **Etapa 2 — TOM (pendente):** refinamento de estilo nos pontos mapeados
  (ex.: "como a gente" no MAP.md), sem mover fato.
