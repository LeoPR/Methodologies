---
title: ADR-007 — Narrativa de entrega = estado consolidado; o traço (evolução) mora à parte
status: aceito
date: 2026-06-16
scope: metodologia de documentação do repo (como escrevemos docs de entrega vs docs de traço); não é conteúdo da metodologia-produto, mas decorre do §3 do Strata
---

# ADR-007 — Narrativa de entrega = estado consolidado; o traço mora à parte

## Contexto

Os docs de **entrega** (README, recipe/README, strata-com-ia, GLOSSARIO, e a superfície ativa do STATUS)
escorregavam para dois vícios, apontados pelo dono:

- Narram a **evolução** no corpo: "agora com evidência", "K=5 derrubou o K=3", "removido", "enfraquecida",
  "(antes apelidado 'paranoia')", data de consolidação inline.
- Esse **"como mudou"** compete com o **"como é agora"** na mesma superfície de leitura — vira diário.

Falta uma regra única que separe o que o leitor encontra primeiro do registro de como chegamos aqui.

## Decisão

O **doc de entrega descreve só o ESTADO presente.** Austero, sempre reescrito para refletir o agora.

A **história** (antes→depois, rebaixamentos, renames, datas de consolidação) vive num **artefato à parte**:
changelog, decisão/ADR, STATUS histórico, `RESULTADOS-*`, BACKLOG.

- **Regra prática:** se a frase diz "antes era X, agora Y", o "antes" **desce ao traço**; fica o "Y".
- **Tracker (STATUS/MAP):** datados por natureza — datas e nomes de pasta são **identificadores**, não narrativa.
  O alvo é só o trecho que **narra a mudança** na superfície ativa.
- **História separada ≠ história descartada.** O log existe para recall e rationale; só não se lê como o estado de entrega.

## Fundamentação

### Padrões da indústria (L1)
- **Diátaxis:** *reference* é "neutral description… austere"; *explanation* é "understanding-oriented". Os quatro
  modos descrevem o produto **como ele é** — nenhum é log de evolução.
- **Keep a Changelog:** a evolução tem arquivo próprio (`CHANGELOG.md`), distinto até do git log ("full of
  noise"). Formaliza "história em artefato separado".
- **ADR (Nygard):** a decisão é **imutável após aceita** — "keep the old one around, but mark it as superseded".
  O log de decisões (append-only) é distinto da leitura do estado vigente (o conjunto de ADRs *accepted*).
- **SSOT / DRY:** "a single, unambiguous, authoritative representation". Estado e história não podem coabitar e
  divergir no mesmo doc — é integridade de fonte.
- **Evergreen / living docs:** o texto "reflects the most current state… does not become out of date" → exige
  externalizar o registro de mudanças.
- **Wikipedia NOTNEWS:** o corpo reflete o conhecimento vigente, "not written in news style"; o cronológico fica
  no *Page History*. (Apoio por analogia de governança.)

*Limite honesto:* Diátaxis não diz **textualmente** "nada de história de desenvolvimento" — é implicação do
"neutral description". Os apoios literais mais fortes são **Keep a Changelog** e o **ADR de Nygard**.

### Do próprio Strata (`recipe/knowledge-architecture.md`)
- **§3 (rastreabilidade):** três planos que o registro ingênuo confunde — o **traço** é append-only e
  recuperável; a **superfície** decai (ativo → superado-mas-visível → silenciado) e deve ser **rebaixada
  ativamente**; o **conhecimento vivo é re-narrável**. "Aplicar append-only à superfície é o erro que faz a
  leitura apodrecer." Ao silenciar, fica um **tombstone** (o quê/quando/por quê) — a lacuna é legível.
- **§5 (fonte única por altitude):** autoridade lógica única ≠ materialização única. O estado tem uma voz
  canônica; a re-narrativa é materialização derivada legítima, não segunda verdade.
- **§8 (versionamento):** história recuperável por estado — o mecanismo que torna o append-only do traço
  praticável (preserva a evolução sem poluir o vigente).
- **Camadas L0/L1/L2:** o estado durável não carrega a ferramenta datada — **datar exemplos, não o princípio**.

## Consequências

- Cada doc de entrega é corrigido para o presente; o "como mudou" é **movido** (não apagado) para o traço.
- **Vocabulário único:** capacidade = **topo / médio / econômico**; custo = **econômico / premium** em eixo
  separado. "Pequeno" como capacidade e "não-topo" saem (ver [GLOSSARIO](../GLOSSARIO.md)).
- O leitor para de tropeçar em diffs; o pesquisador recupera tudo no traço.
- **Custo:** disciplina ao editar (perguntar "isto é estado ou história?") e manter os artefatos de traço vivos.
