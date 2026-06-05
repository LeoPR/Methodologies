---
title: Tickets em markdown e tool bridges
type: reference
status: active
created: 2026-05-20
updated: 2026-06-03
part-of: methodology-suite
audience: ai-primary, human-secondary
see-also: [00-core.methodology.md, versioning-git-hygiene.methodology.md, ai-instrumentation.methodology.md, bibliography.methodology.md]
---

# Tickets em markdown e tool bridges

> **Quando aplicar**: projeto com unidades de trabalho discretas que
> precisam acompanhamento (tickets), e/ou voce precisa reportar/exportar
> esse trabalho pra uma ferramenta corp (Jira, Linear, Monday, etc.).
> O bridge so' faz sentido se os tickets ja' existem em formato canonical.

## Tickets em markdown — FORTE

**Quando**: projeto com unidades de trabalho discretas precisando
acompanhamento. Alternativa local-first a Jira / Linear / GitHub Issues.

**Por que markdown em git**: versiona, offline, IA le, sem
conta/login, sem custo. Trade-off conhecido (sem queries SQL-like).
Inspirado em **"files over apps"** (Steph Ango) + plain-text
accounting tradition.

**Padroes aplicaveis** (combine conforme escala):

| Padrao | Origem | Onde se aplica |
|---|---|---|
| Epic + Story | Scrum, Jira | Meta-ticket agrupando atomicos |
| Kanban states | Anderson 2010 | Workflow (open/wip/blocked/done) |
| Someday/Maybe | GTD (Allen) | Itens diferidos com razao |
| Definition of Done | Agile / Beck | Criterio de aceite explicito |
| MoSCoW | DSDM 1994 | Priorizacao Must/Should/Could/Won't |
| Now / Next / Later | ProductPlan | Roadmap visual sem datas duras |
| OKR | Doerr 2018 | Objetivos + Key Results mensuraveis |
| WSJF | SAFe | Weighted Shortest Job First |

**Estrutura sugerida**:
```
tickets/
├── README.md           <- index com tabela de tickets ativos
└── <ID>-<tema>.md      <- 1 arquivo por ticket
```

**Frontmatter sugerido** (este e' o **status enum canonical** da suite —
o bridge abaixo se refere a ele):
```yaml
---
status: open | in-progress | blocked | deferred | absorbed | closed | superseded
priority: P0 | P1 | P2 | P3        # opcional
created: YYYY-MM-DD
updated: YYYY-MM-DD
blocked-by: [TICKET-XYZ]            # opcional, gera grafo de dependencia
---
```

**Conteudo de ticket** (cubra estes movimentos; nomes livres):
contexto → hipotese/pergunta → plano → criterio de aceite (KR-style,
mensuravel) → riscos → conexoes → updates datados inline (preferivel
a thread porque versiona em git).

**Praticas FORTE**:
- IDs com prefixo taxonomico (`META-X` epic; `T-CODE-N`, `T-DOC-N`,
  `T-EXP-N` — logica PEP/RFC)
- Linkar ticket → commit no commit message
- Status enum **formal** (nao texto livre inline)
- AC **mensuravel** ("X% reducao", "RT 100%", nao "funciona")

## Tool bridges — canonical → ferramentas externas

> **Principio**: canonical e' **fonte da verdade** (markdown+git). Ferramenta
> corp e' **destino** (export). Bridge e' **unidirecional** por default —
> bidirecional gera dual source of truth e drift.

### O que e bridge

Bridge = funcao **`canonical → tool-specific format`** que:
1. Le artefatos versionados (`tickets/`, `experiments/`, ADRs, commits)
2. Aplica **regras de mapeamento** declaradas
3. Emite estrutura no formato que a ferramenta consome (CSV, JSON, API call, link copiavel)

Bridge **nao** modifica fonte. Saida bridge **nao** entra em git
canonical (e artefato efemero de uma exportacao especifica).

### Por que unidirecional

Bidirecional (sync) gera **drift** (edita no Jira, esquece de espelhar em
md), **dual source of truth** (qual vence em conflito?), e **custo de
manutencao** (sync robusto e projeto a parte). Excecao **rara**: pull
selectivo de comentarios em **snapshot** (nao sync continuo).

### Campos canonicos universais

Independente da ferramenta destino, ticket canonical tem:

| Campo canonical | Tipo | Onde guardar |
|---|---|---|
| `id` | string com prefixo taxonomico (`META-X`, `T-CODE-N`, etc.) | nome do arquivo `<ID>-<tema>.md` |
| `title` | string curta | `# titulo` do arquivo (H1) |
| `status` | enum canonical definido acima | frontmatter YAML |
| `priority` | enum: `P0 / P1 / P2 / P3` ou MoSCoW | frontmatter (opcional) |
| `created` / `updated` | ISO date | frontmatter |
| `assignee` | string ou lista | frontmatter (opcional) |
| `description` | markdown | corpo do arquivo |
| `acceptance_criteria` | lista mensuravel (KR-style) | secao no corpo |
| `blocked_by` / `blocks` | lista de IDs | frontmatter (grafo) |
| `tags` | lista | frontmatter |
| `commits` | lista de SHAs | secao "Commits relacionados" no corpo |
| `parent` (Epic→Story) | ID | frontmatter |
| `effort` | story points / horas / T-shirt | frontmatter (opcional) |
| `sprint` / `cycle` / `milestone` | string | frontmatter (opcional) |

Esse vocabulario universal e o **lado canonical** da bridge. Cada
ferramenta tem **nomes diferentes** pros mesmos campos — bridge traduz.
**Nao re-tabular as ferramentas aqui** — UI/nomes de campo de SaaS mudam e a
doc oficial de cada uma cobre melhor; mapeie de la' (ex: Jira `id`->Key,
`status`->Status workflow, `parent`->Epic, `effort`->Story Points; Linear /
GitHub Projects integram commits automaticamente; Trello nao tem `parent` nativo).

### Formato de exportacao

**Bulk CSV** e' o padrao mais robusto (Jira / Monday / Asana / Linear /
ClickUp aceitam); 1 linha por ticket, cabecalhos da doc da ferramenta:

```csv
ID,Title,Status,Priority,Assignee,Description,Acceptance Criteria,Labels,Created,Updated,Parent
T-CODE-1,"Welding alg16 -> src/tcf",in-progress,P0,leonardo,"Mover online.py...","RT 100%; bytes identico",welding;canonical,2026-05-18,2026-05-19,META-NAMING
```

**API direta** (Jira REST v3, Linear/Monday GraphQL, Asana REST) so' quando
CSV nao expressa (issue links/dependencies) ou ha' volume continuo — use
ferramenta dedicada (`jiracli`, `linear-cli`), nao integracao amadora.
**Copy-paste manual** vale ate ~3 cards/mes; acima, CSV.

### Workflows comuns (resumo)

- **Sprint planning**: filtre tickets `status: open` + `priority <= P1` +
  soma `effort` <= capacidade; respeite `blocked-by`; emita CSV com
  `sprint:` preenchido.
- **Reporting periodico (PMO)**: agregue tickets fechados + commits + EXPs
  welded + ADRs do periodo num relatorio markdown orientado a stakeholder.
- **Retroactive cards** (backfill pro corp tracker): o trabalho ja'
  aconteceu — voce **tem a resposta** (commits, tickets fechados, EXPs). Os
  cards retroativos sao "perguntas pra resposta que ja temos": formato de
  ticket pre-trabalho (pergunta + AC) mas ja' preenchendo os campos de
  fechamento. Estrutura:

```
Title: <id canonical> — <titulo do ticket>
Status: Closed
Created: <data inicio real do trabalho>
Closed: <data fim real>
Description:
  [Como se fosse antes:]
  Pergunta: <recriada a partir do contexto>
  Hipotese: <recriada>
  Plano: <recriado>

  [Resolucao (ja conhecida):]
  Feito: <resumo do que aconteceu>
  Commits: <SHAs>
  Decisoes registradas: <ADRs derivados>
```

  Util pra compliance, onboarding, auditoria, sync inicial com tracker
  recem-imposto. **Sempre linke evidencia versionada** (commit SHA, ADR ID,
  EXP ID) — sem isso, vira ficcao.

### Anti-patterns

| Antipattern | Sintoma | Antidoto |
|---|---|---|
| **Dual source of truth** | Jira e md divergem | canonical e md; export unidirecional |
| **Sync continuo amador** | webhook quebra; conflito de timestamp | snapshot periodico; ou ferramenta dedicada se necessario |
| **Card vazio** | criado em Jira sem AC nem description | preencher canonical primeiro; depois exportar |
| **Retroactive sem evidencia** | card claims trabalho mas nao linka commit/ADR/EXP | linkar sempre; senao e ficcao |
| **CSV manualmente editado** | export gerado, depois editado a mao | edite canonical; re-export |
| **Bridge bidirecional fragil** | sync quebra a cada release nova da ferramenta | unidirecional sempre que possivel |
| **Workflow corp diferente do canonical** | status enum diferente entre md e Jira | mapeie no bridge; nao force canonical a copiar workflow corp |
| **Login do colaborador no card** | bridge cria card como "system user" | configurar bridge com user que tem contexto |

### IA orchestration — quando e util

| Tarefa | Como |
|---|---|
| Gerar CSV de bulk export | Le `tickets/`, parseia frontmatter, emite CSV no formato da ferramenta destino |
| Retroactive cards | Le commits + ADRs + EXPs do periodo; reconstroi pergunta/hipotese/plano "como se fosse antes" |
| Sugestao de sprint | Filtra `status: open` + `priority` + soma effort vs capacidade; respeita `blocked-by` |
| Reporting periodico | Agrega tickets fechados + commits + ADRs do periodo; emite relatorio markdown |
| Identificar drift Jira ↔ md | Compara snapshot Jira vs md; lista divergencias pra resolucao manual |

IA **nao** deve: criar cards no Jira sem aprovacao explicita (side-effect
externo); modificar canonical pra "casar" com Jira; inventar
campos/status/commits sem evidencia.

### Configuracao por projeto — onde declarar bridges

Em `.tool-bridges.yaml` (ou similar) na raiz do projeto:

```yaml
bridges:
  jira:
    project_key: TCF
    user: leonardo
    field_mapping:
      acceptance_criteria: "Acceptance Criteria"   # custom field
      effort: "Story Points"
    status_mapping:
      open: "To Do"
      in-progress: "In Progress"
      blocked: "Blocked"
      closed: "Done"
      superseded: "Won't Do"
    export_path: ./bridges/jira-export.csv
```

`.tool-bridges.yaml` e canonical-side, mas **gitignored** porque
contem identificadores per-dev (project_key, user, custom field IDs do
tenant) que variam por colaborador / instancia. Versione
`.tool-bridges.example.yaml` como template sem valores reais; cada dev copia
+ ajusta localmente. (Ruido vs signal — ver
[versioning-git-hygiene](versioning-git-hygiene.methodology.md#signal-vs-ruido).)

## Referencias

Ver [bibliography](bibliography.methodology.md) → "Project management /
agile / kanban" e "Tool bridges (trackers externos)".
