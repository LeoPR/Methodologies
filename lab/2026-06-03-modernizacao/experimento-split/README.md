---
title: Suite de metodologia — indice e roteamento
type: index
status: active
created: 2026-05-20
updated: 2026-06-03
part-of: methodology-suite
audience: ai-primary, human-secondary
how-to-use: consulta sob demanda via routing table; nao leitura linear
applies-to: projetos academicos / pesquisa / software cientifico com codigo + experimentos + artigos + colaboracao com agentes de IA
keywords: [methodology, diataxis, adr, fair, research-compendium, agents-md, mcp, skills, git, lab-work, ai-agents, epistemic-discipline]
---

# Suite de metodologia para projetos academicos / pesquisa / software cientifico

> **Meta-suite**: como organizar pastas, documentacao, decisoes e memoria de
> agentes de IA. Cross-project, portavel, agnostico de stack. Sintese de
> literatura consolidada (biblioteconomia, engenharia de software, ciencia
> aberta) + a camada de tooling de IA de 2026.
>
> **Era um doc monolitico** (`README.methodology.md`, ~2k linhas); foi
> **dividido** numa suite de docs focados pra economizar tempo de leitura,
> reduzir duplicacao e permitir evoluir cada camada na sua cadencia. Este
> README e' o **indice + roteamento** — a propria camada de wayfinding.
>
> **Validado empiricamente** em projetos sob `Acadêmicos/` (TCF e outros): a
> Fase 1 fez o Claude Code parar de "se perder". Adesao **nao** e' universal
> entre os projetos-irmaos — parcial/zero e' comum e frequentemente
> intencional (ver [00-core](00-core.methodology.md) §8 e o `MAP.md` do umbrella).

## Os documentos da suite

| Doc | Cobre | Cadencia |
|---|---|---|
| **[00-core](00-core.methodology.md)** | Esqueleto: 4 pilares, estrutura de pastas canonical, fases de implementacao, antipatterns, auditoria, quando-NAO-aplicar, como-aplicar (greenfield/brownfield) **+ convencoes cross-cutting (FORTE/LOCAL, editorial, assessment-antes-de-alterar)** | estavel |
| **[lab-work](lab-work.methodology.md)** | Pilar 4: experimentos exploratorio/frozen, README IMRaD, `manifest.jsonl`, promocao, registry de hipoteses, checkpoints, diario | estavel |
| **[versioning-git-hygiene](versioning-git-hygiene.methodology.md)** | Signal vs ruido (fonte unica), `.gitignore` como contrato, arquivos grandes, commits, branching, solo-git | estavel |
| **[research-discipline](research-discipline.methodology.md)** | Hierarquia de fontes, dados vivos vs consolidados, marcacao de claims, revisao critica (seguranca/ROI/SLO/proveniencia) | estavel |
| **[ai-instrumentation](ai-instrumentation.methodology.md)** | `CLAUDE.md`/`AGENTS.md`, **MCP, Agent Skills, memoria em camadas, context engineering, prompt caching, subagents, evals, proveniencia** | **ALTA — re-verificar** |
| **[doc-vs-code](doc-vs-code.methodology.md)** | O que documentar e o que deletar: oraculo executavel, teste de reconstrucao bidirecional, Rule of Three pra prosa | estavel |
| **[tickets-and-tool-bridges](tickets-and-tool-bridges.methodology.md)** | Tickets em markdown + export unidirecional pra trackers corp (Jira/Linear/etc.) | estavel |
| **[appendix-caches-environments](appendix-caches-environments.methodology.md)** | Caches/ambientes por OS/tool em pasta dedicada (`Z:\caches\`, XDG, etc.) | estavel |
| **[bibliography](bibliography.methodology.md)** | Lista de referencias compartilhada — todos os docs linkam aqui | estavel |

## Roteamento por intencao do usuario

| Usuario pede / pergunta | Va para |
|---|---|
| "Comecar projeto novo" / "Setup inicial" | TL;DR (abaixo) → [00-core](00-core.methodology.md) §11.1 → [versioning](versioning-git-hygiene.methodology.md) → core Fase 1 |
| "Onde guardo X?" | [00-core](00-core.methodology.md) §4 (estrutura de pastas) |
| "Como organizar docs?" | [00-core](00-core.methodology.md) Pilar 2 (Diataxis) |
| "Documentar em prosa ou codigo?" / "isso e' duplicado?" / "apago o doc e reconstruo?" | [doc-vs-code](doc-vs-code.methodology.md) |
| "Como registrar decisao?" | [00-core](00-core.methodology.md) Pilar 3 (ADR) |
| "Como rodar / organizar experimento?" | [lab-work](lab-work.methodology.md) |
| "Hipoteses / pausa-retomar / notas-diario" | [lab-work](lab-work.methodology.md) (Registry / Checkpoint / Diario) |
| "Git / versionamento / .gitignore / arquivo grande" | [versioning-git-hygiene](versioning-git-hygiene.methodology.md) |
| "Como afirmar / citar / pesquisar X?" | [research-discipline](research-discipline.methodology.md) |
| "Preco / noticia / dado que muda rapido" / "busca achou coisa obsoleta" | [research-discipline](research-discipline.methodology.md) → Dados vivos vs consolidados |
| "Seguranca / ROI / SLO / proveniencia / revisao critica do projeto" | [research-discipline](research-discipline.methodology.md) → Revisao critica |
| "Configurar Claude / Copilot / Cursor / Cline / Gemini" | [ai-instrumentation](ai-instrumentation.methodology.md) |
| "MCP / Skills / subagents / context engineering / evals / memoria de agente" | [ai-instrumentation](ai-instrumentation.methodology.md) |
| "Tickets / planejamento" / "Exportar pra Jira / cards retroativos" | [tickets-and-tool-bridges](tickets-and-tool-bridges.methodology.md) |
| "Caches / venvs / build artifacts / setup ambiente Python-LaTeX-GCC" | [appendix-caches-environments](appendix-caches-environments.methodology.md) |
| "Auditoria periodica" | [00-core](00-core.methodology.md) §7 |
| "Antipattern X" / "Quando NAO aplicar" | [00-core](00-core.methodology.md) §6 / §8 |
| "Leia esta metodologia" / "Avalie aplicabilidade" | [00-core](00-core.methodology.md) §11.3 (protocolo IA — **reportar, NAO alterar**) |
| "Aplicar em projeto novo / existente" | [00-core](00-core.methodology.md) §11.1 / §11.2 (brownfield exige assessment) |

## Principios cross-cutting (aplicam SEMPRE)

Definidos em [00-core](00-core.methodology.md) → "Convencoes e principios
cross-cutting". Resumo: **editorial** (aponta, nao re-explica) · **pesquisa**
(nao invente; *sabe* vs *infere* vs *acha*) · **versionamento** (tudo entra,
exceto regeneravel) · **imutabilidade** (ADR/EXP frozen nunca mudam) ·
**single-source** (referencia, nao duplica) · **verificacao antes de
afirmar** (`Glob`/`Grep` antes de recriar) · **codigo e' o documento do
COMO** (prosa so' carrega o PORQUE).

### Para IAs — NUNCA / SEMPRE

**NUNCA**: inventar referencia que "soa certo" · aceitar premissa do usuario
sem checar · propor recriar algo sem `Glob`/`Grep` antes · escolher
silenciosamente entre fontes em conflito · servir dado vivo (preco/estoque/
noticia) sem timestamp de captura · **aplicar/alterar estrutura de projeto
existente sem assessment** (ver [00-core](00-core.methodology.md) §11.2).

**SEMPRE**: diga quando nao sabe (lacuna admitida > invencao) · ofereca
WebFetch quando o conhecimento e' mutavel · cross-link em vez de duplicar ·
marque claim de fonte fraca com `[VERIFICAR: data]` · revalide dado vivo na
fonte primaria + anexe `capturado_em` · **reporte impacto antes de
modificar** projeto existente e aguarde aprovacao.

## TL;DR — quando voce so' quer copiar e colar

**Zero**: `git init` + `.gitignore` (template oficial da linguagem em
[github.com/github/gitignore](https://github.com/github/gitignore)).
Mesmo solo, sem remoto.

Depois, crie estes arquivos na raiz, nesta ordem:

1. `AGENTS.md` (padrao **estabelecido** em 2026 — Agentic AI Foundation; ver
   [ai-instrumentation](ai-instrumentation.methodology.md)) ou `CLAUDE.md` —
   inventario "onde esta o que" + checklist "antes de agir" + lista NUNCA.
   ~100-200 linhas, curado. Sempre carregado. **Nota Claude Code:** ele
   auto-carrega `CLAUDE.md`, NAO `AGENTS.md`; importe com `@AGENTS.md`.
2. `MAP.md` — 1 pagina com `tree` + tabela "quero fazer X → va para Y".
3. *(opcional)* `.claude/settings.json` + `session-start-context.md` — hook
   injeta lembretes deterministicos no inicio de sessao. Pular se `CLAUDE.md`
   ja' cobre o operacional.
4. `docs/adr/` — Architecture Decision Records numerados, imutaveis.
5. `docs/{tutorials, how-to, reference, explanation}/` — divisao Diataxis.
6. `docs/vocabulary.md` — termos controlados.
7. `experiments/` (ou `notebooks/`) — labs com YAML frontmatter
   (`status`, `tags`, `created`, `updated`).
8. `scripts/index.py` — auto-gera `INDEX.md` lendo frontmatter.

Depois, audite a cada 60-90 dias. Detalhes em [00-core](00-core.methodology.md).
