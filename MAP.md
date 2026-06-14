---
name: map-methodologies-project
type: navigation
status: active
created: 2026-06-03
updated: 2026-06-14
---

# Methodologies — mapa

```
Methodologies/                        <- Oficina de metodologias (Strata pronto; Comporta no forno)
├── recipe/
│   ├── knowledge-architecture.md     <- PRODUTO Strata (L0/L1/L2; núcleo atemporal verificado)
│   └── README.md                     <- guia de uso do Strata (humano + IA; efêmero; pendências)
├── decisions/                        <- ADRs (registros de decisão imutáveis)
│   ├── ADR-001-formato-produto.md    <- 1 arquivo vs suíte de docs
│   ├── ADR-002-estrutura-L0-L1-L2.md <- camadas de durabilidade
│   ├── ADR-003-aposentadoria-predecessor.md <- opção 0b
│   ├── ADR-004-eval-separado-da-metodologia.md <- a ferramenta de prova não é a metodologia
│   ├── ADR-005-duplicacao-fonte-unica-proporcional.md <- apontar, não propagar (fonte única proporcional)
│   └── ADR-006-acuracia-precisao-mapear-distribuicao.md <- 2 eixos: acurácia × precisão (mapear a distribuição)
├── lab/                              <- cozinha experimental (pesquisa; FROZEN)
│   ├── 2026-06-03-modernizacao/      <- análise 5-lentes + experimento-split (FROZEN)
│   ├── 2026-06-03-fundamentacao-L0/  <- 22 fontes primárias do L0 verificadas
│   ├── 2026-06-03-future-proof-sweep/ <- varredura multi-lente (2 rodadas, 15 agentes)
│   ├── 2026-06-03-predecessor/       <- organization-methodology.md arquivado (FROZEN)
│   ├── 2026-06-04-aderencia-portabilidade/ <- aderencia/brownfield/IA/portabilidade (4 lentes)
│   ├── 2026-06-04-economia-ia-tokens/    <- COMPORTA (2ª metodologia): economia/roteamento de recursos de IA
│   ├── 2026-06-04-dev-environment-z/     <- metodologia Z:\ python/venv/cache (snapshot p/ estudo)
│   ├── 2026-06-04-strata-hipoteses/      <- IDEIAS + EVIDÊNCIA do Strata. ENTRADA: OPINIAO-DE-USO.md (opinião honesta) · hub ARQUITETURA-E-EVIDENCIAS.md · BACKLOG-fila-geral.md · REVISAO-RETROATIVA.md · RESULTADOS-*.md
│   └── 2026-06-06-comprovacao-forte-strata/ <- plano de comprovação (gates G1-G6) — SUPERSEDED pela consolidação em strata-hipoteses
├── eval/                             <- LABORATÓRIO DE PROVA (a "chave de fenda": comprova; NÃO é a metodologia, NÃO é o foco)
│   ├── README.md                     <- princípio (meio≠fim) + 3 territórios + regra evidencia/instrumento/infra
│   └── strata/                       <- harness do Strata: runner, scorers, fixtures, cenários + planos/ (gitignored)
├── prototype/                        <- cozinha prototipo (escala; futuro)
├── README.md                         <- entry humano (as 3 cozinhas)
├── AGENTS.md                         <- entry IA
├── MAP.md                            <- este arquivo
└── STATUS.md                         <- foco atual
```

## Quero... → vá para

| Quero | Va para |
|---|---|
| **Usar a metodologia** (produto) | [recipe/knowledge-architecture.md](recipe/knowledge-architecture.md) |
| **A opinião honesta de uso** (o que funciona, por tarefa/tier/custo) | [lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md](lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md) |
| Ver a **prova** de que o Strata funciona (a "chave de fenda") | hub [ARQUITETURA-E-EVIDENCIAS.md](lab/2026-06-04-strata-hipoteses/ARQUITETURA-E-EVIDENCIAS.md) · harness em [eval/strata/](eval/strata/) |
| Ver por que tomamos as decisoes que tomamos | [decisions/](decisions/) |
| Entender como a gente pesquisou | [lab/2026-06-03-modernizacao/README.md](lab/2026-06-03-modernizacao/README.md) |
| Ver a analise (inventario/gaps/sintese) | [lab/2026-06-03-modernizacao/analise-5-lentes.md](lab/2026-06-03-modernizacao/analise-5-lentes.md) |
| Ver o experimento de split (10 docs) | [lab/2026-06-03-modernizacao/experimento-split/](lab/2026-06-03-modernizacao/experimento-split/) |
| Saber o foco atual | [STATUS.md](STATUS.md) |
