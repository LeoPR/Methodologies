---
name: map-methodologies-project
type: navigation
status: active
created: 2026-06-03
updated: 2026-09-30
---

# Methodologies: mapa

> Camadas (L0/L1/L2), carimbos (FROZEN, SUPERSEDED) e códigos de experimento: vocabulário em [GLOSSARIO.md](GLOSSARIO.md).

```
Methodologies/                        <- Oficina de metodologias (Strata pronto; Comporta no forno)
├── recipe/                           <- PRODUTOS prontos (fonte única das técnicas)
│   ├── knowledge-architecture.en.md  <- PRODUTO Strata, FONTE CANÔNICA (L0/L1/L2; L0 fechado 2026-08-01; versão no frontmatter)
│   ├── knowledge-architecture.pt-BR.md     <- tradução pt-BR derivada do canônico EN
│   ├── README.en.md / README.pt-BR.md      <- guia de uso do Strata (humano + IA; efêmero; EN canônico)
│   ├── o-que-voce-ganha.en/.pt-BR.md       <- o que muda na prática (par EN/PT)
│   ├── strata-com-ia.en/.pt-BR.md          <- guia prático "funciona no meu ambiente? sai caro?"
│   ├── strata-idiomas.en/.pt-BR.md         <- manual de confiança PT × EN (o que funciona onde)
│   ├── documentacao-multilingue.md   <- método portável: docs de entrada em 2 línguas (fonte canônica + tradução rastreável)
│   └── *.en.svg / *.pt-BR.svg        <- diagramas (strata-modo; fronteira por contexto de acesso), par EN/PT
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
│   ├── 2026-06-04-strata-hipoteses/      <- IDEIAS + EVIDÊNCIA do Strata. ENTRADA: OPINIAO-DE-USO.md (opinião honesta)
│   │                                        hub ARQUITETURA-E-EVIDENCIAS.md · BACKLOG · REVISAO-RETROATIVA · RESULTADOS-* · variantes-ka/
│   └── 2026-08-01-fechamento-camadas/  <- CICLO P1–P5 que FECHOU o L0 (régua axiomática; §11, §6-bis+ver, persona, âncoras L1); decisões datadas por parte
│   └── 2026-08-02-reteste-L0-fechado/  <- RETESTE do L0 fechado (grade de estratos × capacidade; Degrau 3 agente): PLANO.md + NOTAS-shakedown.md (diário)
│   └── 2026-08-03-idioma-en/           <- IDIOMA PT×EN: sem diferença detectada; equivalência não demonstrada
│   └── 2026-08-03-prompt-ingenuo/      <- braço NAIVE ("uma IA precisa do Strata pra quê?"): PLANO pré-registrado · RESULTADOS (PT+EN) · PROPOSTA-S9 APLICADA (v1.2.2) e testada: inconclusiva, sem poder (RESULTADOS-verificacao-s9.md)
│   └── 2026-09-26-banco-modelos/       <- BANCO DE MODELOS 2026-09: faz tudo / mais barato / mais rápido / grátis / local; eixos pensamento e web
│   └── 2026-09-26-revisao-temporal/    <- revisão temporal: métodos de avaliação, roster, L1/L2, L0 teoria × texto
│   └── 2026-09-26-revisao-superficie/  <- revisão de superfície do Strata + AUDITORIA declarado × feito (destino por achado)
│   └── 2026-09-26-temporalidade/       <- TEMPORALIDADE (3ª frente): 8 mapas de literatura, ONTOLOGIA v0, protótipo, A/B F6-status
├── eval/                             <- LABORATÓRIO DE PROVA (a "chave de fenda": comprova; NÃO é a metodologia, NÃO é o foco)
│   ├── README.en.md / README.pt-BR.md <- princípio (meio≠fim) + 3 territórios + regra evidencia/instrumento/infra
│   ├── strata/                       <- harness do Strata: runner, scorers, fixtures, cenários + planos/ (gitignored)
│   └── temporalidade/                <- bateria de capacidade de temporalidade (fixtures, runner, pontuador, revisão, análise)
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
| Ver a **prova** de que o Strata funciona (a "chave de fenda") | [OPINIAO-DE-USO.md](lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md) (estado consolidado) · hub [ARQUITETURA-E-EVIDENCIAS.md](lab/2026-06-04-strata-hipoteses/ARQUITETURA-E-EVIDENCIAS.md) · rodadas mais recentes: [banco de modelos 2026-09](lab/2026-09-26-banco-modelos/), [F6-status (tempo no Strata)](lab/2026-09-26-temporalidade/RESULTADOS-f6-status.md) · harness em [eval/strata/](eval/strata/) |
| Ver por que tomamos as decisoes que tomamos | [decisions/](decisions/) |
| Saber **se o método agrega** sobre um pedido leigo (braço NAIVE) | [lab/2026-08-03-prompt-ingenuo/RESULTADOS.md](lab/2026-08-03-prompt-ingenuo/RESULTADOS.md) · §9 "quando não agir" aplicado e testado: **inconclusivo (sem poder)**: [RESULTADOS-verificacao-s9.md](lab/2026-08-03-prompt-ingenuo/RESULTADOS-verificacao-s9.md) |
| Ver o estado do momento | [STATUS.md](STATUS.md) |

