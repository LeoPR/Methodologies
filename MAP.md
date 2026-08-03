---
name: map-methodologies-project
type: navigation
status: active
created: 2026-06-03
updated: 2026-08-02
---

# Methodologies: mapa

```
Methodologies/                        <- Oficina de metodologias (Strata pronto; Comporta no forno)
├── recipe/
│   ├── knowledge-architecture.en.md  <- PRODUTO Strata, FONTE CANÔNICA (L0/L1/L2; L0 fechado 2026-08-01, v1.2.1)
│   ├── knowledge-architecture.pt-BR.md     <- tradução pt-BR derivada do canônico EN
│   ├── README.md                     <- guia de uso do Strata (humano + IA; efêmero; pendências)
│   ├── strata-com-ia{,.en}.md          <- guia prático "funciona no meu ambiente? sai caro?"
│   ├── documentacao-multilingue.md   <- método portável: docs de entrada em 2 línguas (fonte canônica + tradução rastreável)
│   └── *.svg                         <- diagramas (strata-modo; custo×qualidade×ambiente)
├── decisions/                        <- ADRs (registros de decisão imutáveis)
│   ├── ADR-001-formato-produto.md    <- 1 arquivo vs suíte de docs
│   ├── ADR-002-estrutura-L0-L1-L2.md <- camadas de durabilidade
│   ├── ADR-003-aposentadoria-predecessor.md <- opção 0b
│   ├── ADR-004-eval-separado-da-metodologia.md <- a ferramenta de prova não é a metodologia
│   ├── ADR-005-duplicacao-fonte-unica-proporcional.md <- apontar, não propagar (fonte única proporcional)
│   ├── ADR-006-acuracia-precisao-mapear-distribuicao.md <- 2 eixos: acurácia × precisão (mapear a distribuição)
│   ├── ADR-007-narrativa-entrega-estado-consolidado.md <- narrativa de entrega separada do histórico
│   └── ADR-008-documentacao-multilingue-fonte-canonica.md <- fonte canônica + tradução rastreável
├── lab/                              <- cozinha experimental (pesquisa; registros podem ser FROZEN)
│   ├── 2026-06-03-modernizacao/      <- análise 5-lentes + experimento-split (FROZEN)
│   ├── 2026-06-03-fundamentacao-L0/  <- 22 fontes primárias do L0 verificadas
│   ├── 2026-06-03-future-proof-sweep/ <- varredura multi-lente (2 rodadas, 15 agentes)
│   ├── 2026-06-03-predecessor/       <- organization-methodology.md arquivado (FROZEN)
│   ├── 2026-06-04-aderencia-portabilidade/ <- aderencia/brownfield/IA/portabilidade (4 lentes)
│   ├── 2026-06-04-economia-ia-tokens/    <- COMPORTA (2ª metodologia): economia/roteamento de recursos de IA
│   ├── 2026-06-04-dev-environment-z/     <- metodologia Z:\ python/venv/cache (snapshot p/ estudo)
│   ├── 2026-06-04-strata-hipoteses/      <- IDEIAS + EVIDÊNCIA do Strata. ENTRADA: OPINIAO-DE-USO.md (opinião honesta) · hub ARQUITETURA-E-EVIDENCIAS.md · BACKLOG-fila-geral.md · REVISAO-RETROATIVA.md · RESULTADOS-*.md
│   └── 2026-06-06-comprovacao-forte-strata/ <- plano de comprovação (gates G1-G6); SUPERSEDED pela consolidação em strata-hipoteses
│   └── 2026-08-01-fechamento-camadas/  <- CICLO P1–P5 que FECHOU o L0 (régua axiomática; §11, §6-bis+ver, persona, âncoras L1); decisões datadas por parte
│   └── 2026-08-02-reteste-L0-fechado/  <- RETESTE do L0 fechado (grade de estratos × capacidade; Degrau 3 agente): PLANO.md + NOTAS-shakedown.md (diário)
├── eval/                             <- LABORATÓRIO DE PROVA (a "chave de fenda": comprova; NÃO é a metodologia, NÃO é o foco)
│   ├── README.md                     <- princípio (meio≠fim) + 3 territórios + regra evidencia/instrumento/infra
│   └── strata/                       <- harness do Strata: runner, scorers, fixtures, cenários + planos/ (gitignored)
├── prototype/                        <- cozinha prototipo (escala; futuro)
├── outreach/                         <- APOIO: comunicação/divulgação (posts, imagens); fora dos 3 territórios de artefato
├── README.md                         <- entry humano (as 3 cozinhas)
├── AGENTS.md                         <- entry IA
├── MAP.md                            <- este arquivo
└── STATUS.md                         <- foco atual
```

## Quero... → vá para

| Quero | Va para |
|---|---|
| **Começar do zero (onboarding de superfície)** | [`README.md`](README.md) → [`recipe/o-que-voce-ganha.pt-BR.md`](recipe/o-que-voce-ganha.pt-BR.md) → [`recipe/README.pt-BR.md`](recipe/README.pt-BR.md) → [`recipe/knowledge-architecture.pt-BR.md`](recipe/knowledge-architecture.pt-BR.md) |
| **Usar a metodologia** (produto) | [recipe/knowledge-architecture.en.md](recipe/knowledge-architecture.en.md) (canônico EN; pt-BR: `knowledge-architecture.pt-BR.md`) |
| **Organizar docs de entrada em 2 línguas** (aplicável a outro projeto) | [recipe/documentacao-multilingue.md](recipe/documentacao-multilingue.md) |
| **A opinião honesta de uso** (o que funciona, por tarefa/tier/custo) | [lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md](lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md) |
| Ver a **prova** de que o Strata funciona (a "chave de fenda") | [OPINIAO-DE-USO.md](lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md) (estado consolidado) · hub [ARQUITETURA-E-EVIDENCIAS.md](lab/2026-06-04-strata-hipoteses/ARQUITETURA-E-EVIDENCIAS.md) · rodada atual [lab/2026-08-02-reteste-L0-fechado/](lab/2026-08-02-reteste-L0-fechado/) · harness em [eval/strata/](eval/strata/) |
| Ver por que tomamos as decisoes que tomamos | [decisions/](decisions/) |
| Ver o estado do momento | [STATUS.md](STATUS.md) |

## Pesquisa histórica (não é trilha de entrada)

Os links abaixo são importantes como evidência e memória de projeto, mas não fazem
parte da leitura inicial de superfície:

| Quero | Va para |
|---|---|
| Entender como a pesquisa foi feita | [lab/2026-06-03-modernizacao/README.md](lab/2026-06-03-modernizacao/README.md) |
| Ver a analise (inventario/gaps/sintese) | [lab/2026-06-03-modernizacao/analise-5-lentes.md](lab/2026-06-03-modernizacao/analise-5-lentes.md) |
| Ver o experimento de split (10 docs) | [lab/2026-06-03-modernizacao/experimento-split/](lab/2026-06-03-modernizacao/experimento-split/) |
