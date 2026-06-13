---
title: 'Fila geral — ideias/planos/hipóteses em aberto (a consolidar/defrag)'
created: 2026-06-13
status: 'INDEX vivo das pendencias NAO executadas. Proxima META: defrag/compress -> 1 plano objetivo priorizado.'
---

# Fila geral — o que está em aberto (para consolidar)

> **Lugar único** (§5) das **ideias/planos/hipóteses não-executados**, para depois **consolidar** num
> plano objetivo. Itens grandes têm doc próprio (linkado); itens novos/menores ficam aqui até a
> consolidação. O **estado do que já foi FEITO** vive no [hub de evidências](ARQUITETURA-E-EVIDENCIAS.md).

## Aberto — testes / evidência
- **Expansão de cenários e gêneros** (PatchCraft; AulaQuantum/DeepLearning; amostragem externa; viés do
  projeto-próprio): [`PLANO-evidencia-cenarios-e-narrativa.md`](PLANO-evidencia-cenarios-e-narrativa.md).
- **F5** (com/sem ferramentas) · **F6** (temporalidade): [`PLANO-geral-modos-fechar-lacunas.md`](PLANO-geral-modos-fechar-lacunas.md).
- **Dossiê** temporalidade/ordem/fonte (estudar): [`DOSSIE-ia-temporalidade-ordem-fontes.md`](DOSSIE-ia-temporalidade-ordem-fontes.md).

## Aberto — design do método
- **Exportação/tradução p/ normas externas (o "L3"?):** [`IDEIA-exportacao-traducao.md`](IDEIA-exportacao-traducao.md).
- **Setup operacional p/ agentes (Claude Code / Copilot) — área cinzenta** *(canônico vs spinoff vs Comporta)*.
  **Reflexão:** é **L2 (Órganon — ferramentas datadas)**. O **princípio** ("organize o projeto para os agentes
  da era atual agirem; datado/revalidável") **já cabe** no L2 do Strata; as **receitas específicas** (AGENTS.md,
  CLAUDE.md, config Copilot) **não** devem inchar o **arquivo canônico** — vão para um **satélite** (estender
  [`strata-com-ia.md`](../../recipe/strata-com-ia.md) ou um `strata-agentes.md` novo). **Fronteira com Comporta:**
  *organizar para o agente AGIR = Strata; escolher/custear/rotear o agente = Comporta.* (Pensar depois.)
- **Organização de artefatos de ambiente (caches/temp/venvs) — `Z:\caches\README.md`:** liga ao lab
  [`2026-06-04-dev-environment-z`](../2026-06-04-dev-environment-z/). **Reflexão:** é um **princípio L0/L1** —
  *classifique cada artefato por **canônico × regenerável × efêmero × vínculo-com-o-projeto** e o coloque por
  isso* — expresso por **L2** (junction p/ Z:, env vars, `.gitignore`, `%TEMP%`). Espectro a destilar:
  - **efêmero de execução** (temp) → `%TEMP%/%TMP%` (some no reboot; só p/ descartável; **se a ferramenta
    respeita é tool-dependente** — algumas têm cache próprio e ignoram TMP);
  - **regenerável caro** (cache do pip/uv) → dir de cache (mantém entre runs, mas **apagável** — regenera);
  - **regenerável mas VINCULADO ao projeto** (ex.: cache de palavras p/ acelerar um dicionário local) →
    cache **com escopo de projeto** (gitignored, mas atado aos dados do projeto — **não** é `%TEMP%`);
  - **canônico** (a fonte) → versionado.
  **Overlap com Comporta** (cache que poupa recompute = economia de recurso). Perguntas a fechar depois:
  TMP é o mesmo entre ferramentas? quão "vinculado" cada cache é? regenerável-de-projeto mora onde?

## Próxima META — defrag / compress (consolidar)
**Revisitar** todos os itens acima e **fundir** num **plano objetivo priorizado** (o que fazer, em ordem),
cortando sobreposição (ex.: a fronteira **Strata × Comporta** aparece nos caches **e** no setup-de-agente —
resolver uma vez). Hoje são ideias dispersas; a consolidação as torna acionáveis.
> ⚠️ **LEMBRETE:** fazer este **defrag antes de disparar mais testes** — para não acumular dívida de ideias.
> *(Quando for feito: bom candidato a um **workflow** de síntese — ler todos os docs de ideia em paralelo →
> 1 plano priorizado.)*

## Índice dos docs de ideia/plano
[dossiê](DOSSIE-ia-temporalidade-ordem-fontes.md) · [plano-evidência](PLANO-evidencia-cenarios-e-narrativa.md) ·
[IDEIA-exportação](IDEIA-exportacao-traducao.md) · [roadmap-modos](PLANO-geral-modos-fechar-lacunas.md) ·
[hub de evidências](ARQUITETURA-E-EVIDENCIAS.md) · (este backlog).
