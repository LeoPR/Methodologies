---
name: agents-methodologies-project
type: ai-instructions
status: active
created: 2026-06-03
updated: 2026-06-16
audience: ai-primary
applies-to: agentes de IA operando no projeto Methodologies/
---

# Methodologies — instrucoes pra IA

Projeto de P&D de metodologia de organizacao. **3 cozinhas**: `lab/`
(experimental / pesquisa), `prototype/` (escala — futuro), `recipe/`
(produto). Este projeto **dogfooda** a metodologia que ele produz.

## Inventario — onde esta o que

Esta e' uma **oficina de metodologias** (ver `README.md`). 2 produtos: **Strata**
(nucleo consolidado; eixo seguranca §6-bis e Parte IV pendentes) e **Comporta** (economia de IA,
EM ANDAMENTO no `lab/`). **Tres territorios
por tipo de artefato**: `recipe/` = metodologia (o fim) · `lab/` = IDEIAS (hipoteses/
conclusoes) · `eval/` = EXECUTAVEIS de prova (a "chave de fenda"; meio, NAO a metodologia).

- `recipe/` — **produtos prontos** (single-source das tecnicas):
  - `knowledge-architecture.md` — **STRATA**: arquitetura do conhecimento em
    camadas L0/L1/L2. Pendente: eixo seguranca (§6-bis) e Parte IV (adocao/operacao).
  - `README.md` — guia de uso do Strata (humano + IA; o arquivo e' efemero).
- `decisions/` — **ADRs** (ADR-001..006): por que cada decisao de design. Imutaveis.
- `lab/` — pesquisa (modo exploratorio), subpastas datadas `YYYY-MM-DD-tema/`:
  - `2026-06-03-modernizacao/`: analise 5-lentes + `experimento-split/` (**FROZEN**)
  - `2026-06-03-fundamentacao-L0/`: 22 fontes primarias verificadas do L0
  - `2026-06-03-future-proof-sweep/`: varredura multi-lente (2 rodadas, 15 agentes)
  - `2026-06-03-predecessor/`: predecessor arquivado (**FROZEN**)
  - `2026-06-04-aderencia-portabilidade/`: aderencia/brownfield/IA/portabilidade
  - `2026-06-04-economia-ia-tokens/`: **COMPORTA** — a 2a metodologia (economia e
    roteamento de recursos de IA: compute/memoria/E-S/custo). Tem instrumentos medidos
    (`instrumento/`), arvore de decisao, `prototipo/detect_env.py` (classifica ambiente
    A1-A6). NAO destilado p/ recipe ainda (virara `recipe/comporta-*.md`).
  - `2026-06-04-dev-environment-z/`: metodologia Z:\ importada p/ estudo
    (`snapshot-fonte/` e' **gitignored** — nao publicar; so o README de estudo vai ao git)
  - `2026-06-04-strata-hipoteses/`: **IDEIAS + EVIDÊNCIA do Strata** (corpus v1 CONSOLIDADO).
    **ENTRE POR AQUI:** `OPINIAO-DE-USO.md` (opinião honesta por tarefa/tier/custo) e o hub
    `ARQUITETURA-E-EVIDENCIAS.md` (estado datado + histórico append-only); backlog em
    `BACKLOG-fila-geral.md`; auditoria do que envelheceu em `REVISAO-RETROATIVA.md`. Os `RESULTADOS-*.md`
    são os registros por fase (alguns superseded — siga o hub, não conclusões soltas). O HARNESS que gerou
    isso mora em `eval/strata/` (ver `eval/strata/README.md`). *Assinatura: econômico over-age / topo calibra /
    forma padroniza — sinal, não prova (sintético, completion-only).*
  - `2026-06-06-comprovacao-forte-strata/`: plano de comprovação (gates) — **SUPERSEDED** pela consolidação
    em `strata-hipoteses` (mantido como registro).
- `eval/` — **LABORATORIO DE PROVA** (a "chave de fenda": comprova; NAO e a metodologia
  nem o foco; reutilizavel entre metodologias). `strata/` = harness do Strata (runner
  multi-modelo, scorers, fixtures, cenarios, `RASTREAMENTO-E-MELHORIA.md`); `*/planos/` =
  saidas brutas **gitignored** (projetos reais sao PRIVADOS). Regra: toda execucao e'
  `evidencia|instrumento|infra`. Ver `eval/README.md`.
- `prototype/` — placeholder (testar a receita em escala; futuro).
- `divulgacao/` — **APOIO** (comunicacao/divulgacao: posts, imagens). Fora dos 3 territorios de
  artefato (e do `decisions/`); nao e produto, pesquisa nem ferramenta. Nao publica metrica nova.
- `README.md` (oficina) / `MAP.md` (mapa) / `STATUS.md` (foco atual) — wayfinding.

## Antes de agir (checklist)

- Tecnica de organizacao **nova ou alterada** → vai pro PRODUTO
  (`recipe/knowledge-architecture.md`), nao espalhe em varios lugares.
- **Pesquisa / exploracao / descarte** de tecnica → `lab/` (pasta datada
  `YYYY-MM-DD-tema/`, modo exploratorio).
- **Ferramenta/harness de prova** (runner, scorer, fixture, cenario) → `eval/`, NUNCA em
  `recipe/` (produto) nem misturado com as IDEIAS do `lab/`. A ferramenta e' **meio, nao
  fim**: nao gaste tempo aperfeicoando a chave de fenda; o fim e' **provar a metodologia**.
- `Glob`/`Grep`/`Test-Path` antes de propor recriar algo — a propria
  metodologia manda (verificacao antes de afirmar).
- **Editou QUALQUER `.md` com frontmatter** → **bumpe o `updated:`** p/ hoje (rastreabilidade
  §3/§8; o carimbo ja estagnou varias vezes — propagacao por memoria apodrece). Guarda mecanica:
  `python tools/check_stamps.py` (rode antes de commitar docs). P/ automatizar, chame-o do seu
  pre-commit — este repo ja usa um `core.hooksPath` global (`~/.githooks`), entao NAO sete um local
  (desligaria o hook global); adicione `python tools/check_stamps.py || exit 1` ao pre-commit de la.
- **Numero volatil** (linhas, KB, SHA) NAO vai inline na prosa — aponte para a fonte ou
  omita (regenera-se do artefato; §5). Estado de evidencias: aponte ao hub (secao 'Estado das
  fases — fonte unica'), nao copie o literal (ADR-005).
- **Mediu/reportou um modelo** aplicando a metodologia → reporte **acuracia × precisao em colunas
  separadas** (nao colapse num numero), publique **k e K**, e mapeie a distribuicao no regime de uso —
  NAO varra hiperparametros pra achar "a temp certa" (ADR-006). O `hb_runner` tem `--temp` (default 0.3).

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
