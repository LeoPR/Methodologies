---
title: Fechamento das camadas L0/L1/L2 — revisão fundamentada em partes
created: 2026-08-01
updated: 2026-08-01
status: **CICLO P1–P5 FECHADO (2026-08-01)** — L0 editorialmente fechado: §11
  enxuto no canônico (P1), P2 refutada, §6-bis expandido com autoridade-para-ver
  (P3), notas datadas resolvidas com persona declarada no lead (P4), âncoras do
  L1 mapeadas (P5). Flip EN-canônico formalizado (adendo ADR-008).
  Próximo passo declarado pelo dono: como TESTAR o L0 fechado.
origem: avaliação do repo (2026-08-01) — o usuário exigiu que cada achado fosse
  sustentado por lógica + literatura + evidência, uma parte por vez, antes de
  decidir qualquer mudança no canônico (recipe/)
---

# Fechamento das camadas — revisão fundamentada, em partes

Regra desta pasta (dogfood de §4/§7):

- **Uma parte por vez.** Cada parte declara hipótese antes, traz literatura
  web-verificada `[WEB ✓ 2026-08-01]`, evidência interna (o próprio repo) e
  ameaças à validade. **Só se fecha** quando a posição está sustentada.
- **Nada vai ao `recipe/`** enquanto a parte não fechar. O canônico é o produto;
  isto aqui é exploração (§1/§7).
- Se a conclusão for "**não mudar nada**", ela também é registrada — preservar
  o negativo (§4).

## Fila de partes

| Parte | Questão | Status |
|---|---|---|
| **P1 — Classificação** | o L0 tem princípio de *como agrupar/rotular* (eixo, divisão, facetas)? candidato a §11 | **FECHADA (2 ciclos):** §11 no canônico; 2º ciclo sob a régua axiomática **enxugou** o §11 (regras "eixo declarado" e "hipótese de domínio" eram teoremas deriváveis de §3/§4/§6 → viraram derivações declaradas) → [`P1-classificacao.md`](P1-classificacao.md) + [`P1-revisao.md`](P1-revisao.md) |
| **P2 — Identidade/granularidade** | o L0 diz o que é "*um* artefato" (atomicidade, fronteira de chunk, identidade estável)? | **FECHADA — REFUTADA (2026-08-01):** era pedido de apresentação, não axioma faltante; sem mudança no canônico → [`P2-identidade-grao.md`](P2-identidade-grao.md) §8 |
| **P3 — Sigilo / autoridade-para-ver** | o invariante simétrico ao §6-bis (agir) — compartimentalização, need-to-know — está no escopo do Eixo 5? | **FECHADA — APROVADA E APLICADA (2026-08-01):** §6-bis expandido no canônico EN-first (+ tradução PT derivada; linha L1 RBAC/ABAC ancorada nos dois atos); flip formal EN-canônico no mesmo ciclo (adendo ADR-008) → [`P3-sigilo-autoridade-ver.md`](P3-sigilo-autoridade-ver.md) §7 |
| **P4 — Notas datadas no L0** | as notas "Operacional (por que importa para IA)" em §3/§9 violam a regra da própria Parte I? extração ou reformulação | **FECHADA — APROVADA E APLICADA (2026-08-01):** notas saíram; persona declarada 1× no lead (formulação literal do dono); links datados viraram "Era instance" nos Groundings de §3/§9 → [`P4-notas-datadas-personas.md`](P4-notas-datadas-personas.md) §7 |
| **P5 — Âncoras do L1** | §1 e §9 sem mapeamento na Parte II; Cookiecutter sob §8 expressa §1; "gerar e priorizar" não ancorado | **FECHADA — APLICADA (2026-08-01):** Cookiecutter movido p/ nova âncora §1; "gerar e priorizar" re-ancorado como §7 (cont.); nova âncora §11 (3 formalizações); §9 fica sem tabela **por decisão declarada** (é regulador — sua expressão L1 são as notas de Adherence distribuídas) → [`P5-ancoras-L1.md`](P5-ancoras-L1.md) |

Ordem justificada: P1-P3 são **conceituais** (mudam o L0 se confirmadas —
precisam de literatura); P4 é **coerência interna** (a própria regra do
documento decide); P5 é **editorial**.

## A régua de revisão (surge da P2, 2026-08-01)

Critério discriminante para toda candidatura ao L0, fixado após a objeção do
dono (abstração não precisa de densidade/apresentação):

> **"Instanciado o método num corpus novo, sem computador, a operação existe no
> repertório do L0?"** Sim → candidatura válida (P1-§11: "formar o esquema" não
> existia). A "falta" só aparece como pedido de exemplo/definição do primitivo
> → **não é lacuna** (P2: "artefato" é primitivo de Hilbert — definido
> implicitamente pelas operações; exemplos ficam fora, mostrando que o fluxo
> funciona).

Fundamentação da régua: Hilbert 1899 (primitivos definidos implicitamente pelos
axiomas; "mesas, cadeiras, canecas"); Benacerraf 1965 (números não são objetos;
vale a estrutura); ADTs — Liskov & Zilles 1974 / Guttag & Horning 1978 (o tipo
é definido pelas operações, não pela representação). Completo em
[`P2-identidade-grao.md`](P2-identidade-grao.md) §8.

Corolário: a régua **reforça a P4** — notas "Operacional (por que importa para
IA)" na Parte I são apresentação dentro da abstração; o lugar delas é fora.

## Fluxo de idiomas (decisão do dono, 2026-08-01)

A partir da P3, trabalho é **EN-first**: o inglês (`knowledge-architecture.en.md`)
é o documento de trabalho; o PT é **tradução derivada** — não precisa ser lido
nem debatido, apenas traduzido com fidelidade para manter o mesmo conteúdo.

**Pendente (passo próprio, fora desta pasta):** ~~o flip *formal* de autoridade no
produto~~ — **FEITO 2026-08-01**: o par `strata-knowledge-architecture` inverteu
(EN canônico, PT derivado) por decisão explícita do dono; adendo datado no
ADR-008, cólofons trocados, `tools/check_l10n.py` inalterado (orientada a
marcadores). Resta da fila editorial da doc multilíngue: `recipe/README.md`,
`MAP.md`, `STATUS.md`, `o-que-voce-ganha.md` (sem par — ver tabela em
`recipe/documentacao-multilingue.md`).

## Série L1 (revisão de conteúdo da Parte II — a que havia ficado para trás)

| Parte | Questão | Status |
|---|---|---|
| **L1-1 — Conteúdo do L1** | camadas certas? mapeamentos pós-fechamento? `[CANONICAL]` basta? | **FECHADA — (a) aplicada EN-first (2026-08-01); (b) nada se move e (c) `[CANONICAL]`+verificar-ao-tocar decididos; PT pendente (fim do ciclo)** → [`L1-1-revisao-conteudo.md`](L1-1-revisao-conteudo.md) §7 |
| **L1-2 — Repesquisa de literatura** | as fontes da Parte II existem e sustentam as alegações? relação lógica L0↔L1 válida? lacunas canônicas? (**supera a política L1-1-(c)** por decisão do dono) | **APLICADA EN-first (2026-08-01)** — swarm 7 agentes, web-verificação integral: 0 fontes inexistentes, 0 relações quebradas; aplicados: 14 erros/precisões (A) + 9 reparos editoriais (B) + selos `[WEB ✓ 2026-08-01]` em toda a Parte II; PT pendente (fim do ciclo) → [`L1-2-repesquisa-literatura.md`](L1-2-repesquisa-literatura.md) |
| **L1-3 — Linhas novas (lacunas canônicas)** | as 8 candidatas da classe C da L1-2 entram? (RFC 2119/8174 §3-bis; FAIR-base e reporting guidelines §4; DRY §5; reference rot §6; capabilities/OAuth §6-bis; DOI/Zenodo publishing) | **PENDENTE** — decisão linha a linha (dono) |

## Série L2 (revisão da Parte III, pós-fechamento do L0)

| Parte | Questão | Status |
|---|---|---|
| **L2-1 — Alinhamento estrutural** | com o L0 fechado, o que a Parte III deve ao núcleo novo? (§6-bis-ver sem forma L2; §11 sem necessidade — negativo; fronteira Comporta) | **FECHADA — APLICADA EN-first (2026-08-01); PT derivado pendente (fim do ciclo)** → [`L2-1-alinhamento.md`](L2-1-alinhamento.md) §7 |

## Fluxo de trabalho desta fase (decisão do dono, 2026-08-01)

- **Traduções e reorganizações editoriais ficam PARA O FIM.** O que não pode
  esperar é o **traço do raciocínio**: cada parte registra hipótese, evidência,
  literatura e texto candidato **completos no doc da parte** — porque a tradução
  precisa seguir o contexto; ao traduzir, verifica-se a fidelidade contra este
  registro (§3: fonte + rationale rastreáveis).
- EN-first continua valendo para texto candidato ao canônico.
