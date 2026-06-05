---
title: Analise de 5 lentes — sintese consolidada
status: frozen
created: 2026-06-03
updated: 2026-06-03
nota: saida bruta da analise multi-agente (em ingles); registro de pesquisa
---

# Analise de 5 lentes — sintese (registro de pesquisa)

> Saida consolidada de uma analise multi-agente do monolito
> `README.methodology.md` (~2035 linhas / 97KB), sob 5 lentes independentes
> com verificacao web: `concept-inventory`, `ai-2026-gaps`,
> `docorg-modernization`, `simplification-split`, `freshness-consistency`.
> Mantido em ingles (idioma da analise). Insumo do arquivo-produto.

## 1. Concept Inventory — Summary (~155 conceitos)

| Category | Count (approx) | Notes |
|---|---|---|
| framework | ~45 | Diataxis, ADR/MADR, Research Compendium, IMRaD, C4, Zettelkasten, PARA, evidence pyramid, JTBD |
| principle | ~40 | single-source, oracle-vs-prose, Rule of Three, Chesterton's fence, recency-vs-authority |
| convention | ~35 | FORTE/LOCAL, YAML frontmatter, dated-prefix, manifest fields, status enums, ID prefixes |
| antipattern | ~12 | lab graveyard, hot-edit frozen, manifest-sem-git_sha, prosa-espelho, manual `_v2` versioning |
| tool | ~25 | Claude Code, Copilot, Cursor, Cline, MLflow/W&B, DVC, git-cliff, Zenodo, jiracli |
| standard | ~15 | FAIR4RS, SemVer, Conventional Commits, CITATION.cff, NDJSON, XDG, WCAG 2.2, NIST CSF 2.0 |
| role-of-file | ~10 | CLAUDE/MAP/STATUS, vocabulary.md, checkpoint, narrativa, findings, report.md |
| pillar | 4 | Wayfinding, Diataxis docs, ADR, Lab/FAIR4RS |

**Durabilidade**: camada de tooling de IA (AGENTS.md status, tabelas de
ferramenta, env vars de cache, claims "2026") e' a que mais drifta; literatura
classica (Diataxis, ADR, IMRaD, FAIR4RS, property testing, Kolmogorov/MDL) e'
duravel. → isolar a camada de IA com data de re-verificacao.

## 2. AI-2026 Modernization — prioritizada (web-verificada)

| Pri | Finding | Source |
|---|---|---|
| HIGH | **AGENTS.md** virou padrao estabelecido (Agentic AI Foundation / Linux Foundation, ago 2025); nativo em Codex/Copilot/Cursor/Gemini CLI/Aider/Windsurf/Zed. Doc dizia "emergente". | openai.com/index/agentic-ai-foundation |
| HIGH | **MCP** totalmente ausente — padrao de conectividade de 2026 (97M+ downloads/mes, 10k+ servers). | blog.modelcontextprotocol.io/posts/2026-mcp-roadmap |
| HIGH | **Agent Skills (SKILL.md)** ausente — spec aberta (Anthropic, dez 2025), progressive disclosure, cross-tool. | code.claude.com/docs/en/skills |
| HIGH | **"IA nao lembra entre sessoes"** virou simplificacao — 4a camada: memoria filesystem (memory tool, /mnt/memory, contexto 1M) → drift opaco nao-versionado. | platform.claude.com/.../memory-tool |
| HIGH | **Tabela de ferramentas §5 desatualizada** — faltam Codex, Gemini CLI, Windsurf, Zed, Antigravity, Aider; convergencia em AGENTS.md. | dev.to (best AI IDEs 2026) |
| MED | **Context engineering / 1M / compaction** sub-desenvolvido — mais tokens piora (~65% das falhas = degradacao de contexto); valida roteamento via MAP.md. | platform.claude.com/cookbook |
| MED | **Prompt caching** — AGENTS.md estavel = prefixo cacheavel; volatil (STATUS.md) depois do estavel. | mager.co/blog (prompt caching 2026) |
| MED | **Subagents / fan-out** — corta trabalho multi-file 50-70%; §8 audit e §13.2 brownfield sao fan-outs. | code.claude.com/docs/en/agent-teams |
| MED | **Agent evals** — AGENTS.md/Skills/hooks regridem em silencio; evals em CI. | confident-ai.com (LLM agent eval) |
| MED | **Proveniencia / C2PA** — obrigatorio ago/2026 (EU AI Act Art. 50; CA SB 942; C2PA 2.1 = ISO/IEC 22144). | contentauthenticity.org |
| MED | **grep-first vs RAG** — top agentes usam grep/arvore, nao vector DB; Claude Code abandonou RAG vetorial. | mindstudio.ai (is RAG dead) |
| MED | **Structured output / schema-as-contract** — manifest/ticket/.tool-bridges ganham JSON Schema; MCP exige output schema. | collinwilkins.com (structured output) |
| LOW | **Observabilidade OTel GenAI** — complemento maquina do diario/manifest. | opentelemetry.io/blog/2026 |
| LOW | **AI-memory-abuse** + Cline memory-bank precisam atualizar (memoria filesystem autonoma; claude-mem). | github.com/thedotmack/claude-mem |

## 3. General Doc-Org Modernization (mapeada as 5 metas)

- **Busca (findability)**: SQLite FTS5 + sqlite-vec; **unifica** com grep-vs-RAG — grep agentico e' default; FTS5+sqlite-vec so' pra busca conceitual cross-doc em corpus grande. NAO indexar vetorialmente por reflexo.
- **Rastreabilidade**: proveniencia alem de `git_sha` — SLSA/Sigstore, RO-Crate/CodeMeta; **unifica** com C2PA/authored-by.
- **Versionamento de dados**: DVC esta datado → lakeFS / Quilt.
- **Espaco (umbrella)**: dedup `.7z`/`.zip`/`_bkp` com Borg/restic + `git gc`/`git bundle`.
- **Catalogo**: Backstage / codemeta pros ~60 subprojetos.
- **Render**: Quarto (MkDocs em maintenance-mode → Zensical).
- **Indice**: `index.py` manual → Dataview/backlinks (Logseq/SiYuan).

## 4. Simplification + Split Architecture (experimento)

Redundancias colapsaveis (~30-40% de reducao): Signal-vs-ruido (4+ lugares),
FORTE/LOCAL, "doc aponta nao re-explica" (5x), dados-vivos, assessment-antes-
de-alterar (4+), Apendice B re-tabula 8 SaaS trackers, sub-padroes de lab work,
§3.1-3.7. As linhas de corte naturais ja' eram os blocos "Quando aplicar" +
"Conexao com outros pilares" de cada secao.

Arquitetura testada (ver `experimento-split/`): README (indice) + 00-core +
lab-work + versioning + research-discipline + ai-instrumentation + doc-vs-code
+ tickets-and-tool-bridges + appendix-caches + bibliography.

**Decisao do produto**: consolidar de volta em **1 arquivo** (a receita); o
split fica como registro de pesquisa.

## 5. Freshness / Broken-Ref Fix List (aplicado)

- Links do umbrella (README/AGENTS/MAP) re-apontados para `Methodologies/`.
- Bug interno "cinco/seis secoes-tronco" (faltava "Codigo, prosa e oraculo") — resolvido na reescrita.
- **Achado**: caminhos `../../../dev-environment/` ficaram corretos no novo nivel `Methodologies/` (a mudanca os consertou) — nao adicionar 4o `../`.
- **Achado git critico**: `.gitignore` do umbrella e' allowlist (`/*`); `Methodologies/` estava sendo ignorado — corrigido com `!/Methodologies/`.
