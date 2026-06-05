---
name: agents-methodologies-project
type: ai-instructions
status: active
created: 2026-06-03
updated: 2026-06-03
audience: ai-primary
applies-to: agentes de IA operando no projeto Methodologies/
---

# Methodologies — instrucoes pra IA

Projeto de P&D de metodologia de organizacao. **3 cozinhas**: `lab/`
(experimental / pesquisa), `prototype/` (escala — futuro), `recipe/`
(produto). Este projeto **dogfooda** a metodologia que ele produz.

## Inventario — onde esta o que

- `recipe/knowledge-architecture.md` — **O PRODUTO**: arquitetura do conhecimento
  em camadas L0/L1/L2 (núcleo atemporal + padrões + ferramentas). **Single-source das técnicas.**
- `lab/` — pesquisa (modo exploratório). Subpastas datadas:
  - `2026-06-03-modernizacao/`: análise 5-lentes + `experimento-split/` (**FROZEN**)
  - `2026-06-03-fundamentacao-L0/`: 22 fontes primárias verificadas do L0
  - `2026-06-03-future-proof-sweep/`: varredura multi-lente (2 rodadas, 15 agentes)
  - `2026-06-03-predecessor/`: `organization-methodology.md` arquivado (**FROZEN**)
- `prototype/` — placeholder (testar a receita em escala; futuro).
- `MAP.md` / `STATUS.md` — mapa + foco atual.

## Antes de agir (checklist)

- Tecnica de organizacao **nova ou alterada** → vai pro PRODUTO
  (`recipe/knowledge-architecture.md`), nao espalhe em varios lugares.
- **Pesquisa / exploracao / descarte** de tecnica → `lab/` (pasta datada
  `YYYY-MM-DD-tema/`, modo exploratorio).
- `Glob`/`Grep`/`Test-Path` antes de propor recriar algo — a propria
  metodologia manda (verificacao antes de afirmar).

## Fronteira de cobertura (o que este projeto NAO cobre)

Strata cobre **como organizar, rastrear e gerar** conhecimento de trabalho. NAO cobre:

- **Gestao financeira / orcamento** do projeto — fora de escopo
- **Gestao de pessoas / RH** (contratacao, performance) — fora de escopo
- **Qualidade de codigo** (cobertura de testes, linting, metricas) — sao L2 de
  outro dominio; Strata registra *que* voce usa essas ferramentas, nao *como*
- **Conteudo do dominio** (como fazer estatistica, como escrever um artigo) —
  Strata organiza *o processo*, nao o conteudo substantivo
- **Adocao em times** (onboarding, gestao de mudanca) — pendente; pode virar
  Parte IV se recorrer (ADR-003, regra de tres)

## NUNCA

- **Editar `lab/.../experimento-split/`** — e' registro FROZEN de pesquisa
  (imutavel; "frozen = imutavel"). Pra continuar, novo experimento datado.
- **Editar `lab/.../predecessor/`** — FROZEN, registro historico do predecessor.
- Duplicar uma tecnica entre `recipe/` e `lab/` como se fossem dois produtos
  — o produto e' so' `recipe/` (single-source).
- Confundir com o umbrella `Acadêmicos/` (ver `../AGENTS.md`): la' e' umbrella,
  aqui e' um projeto.
