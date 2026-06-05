---
title: Instrumentacao para agentes de IA
type: reference
status: active
created: 2026-05-20
updated: 2026-06-03
part-of: methodology-suite
audience: ai-primary, human-secondary
cadence: high
re-verify-by: 2026-09-01
see-also: [00-core.methodology.md, research-discipline.methodology.md, lab-work.methodology.md, tickets-and-tool-bridges.methodology.md, bibliography.methodology.md]
---

# Instrumentacao para agentes de IA

> **Quando aplicar**: configurar Claude / Codex / Copilot / Cursor / Cline /
> Gemini CLI / etc. num projeto, ou decidir como a IA "lembra" e age.
>
> **CAMADA DE ALTA CADENCIA.** Tooling de IA muda em meses. Os fatos de
> ferramenta abaixo carregam captura `[2026-06-03]` e devem ser
> **re-verificados a cada auditoria** (ver [00-core](00-core.methodology.md) §7).
> Os **principios** (single-source, memoria em camadas, doc versionada >
> memoria, contexto curado > volume) sao estaveis; os **produtos** nao.

## Principio chave — memoria em camadas

IA **nao tem memoria implicita continua** entre sessoes. O que parece
memoria sao **mecanismos explicitos**, de durabilidade e auditabilidade
diferentes. Em 2026 sao **quatro** (a versao antiga deste doc listava tres —
faltava o (4)):

| # | Camada | Onde | Versionado / auditavel? | Conteudo | Durabilidade |
|---|---|---|---|---|---|
| 1 | **Arquivos sempre carregados** | `CLAUDE.md` / `AGENTS.md` (raiz do projeto) | SIM (git) | operacional do projeto, estavel | alta |
| 2 | **Hook deterministico** | `.claude/settings.json` + `session-start-context.md` | depende (alguns gitignore `.claude/`) | primer ephemero, 5-15 linhas | media |
| 3 | **Memoria explicita do agente (user-scope)** | `~/.claude/.../memory/` (Claude Code); `memory-bank/` (Cline) | NAO (user-scope) | preferencias do usuario, cross-projeto | media |
| 4 | **Memoria persistida em filesystem (NOVO 2026)** | memory tool / Managed Agents (`/mnt/memory`); contexto ate 1M tokens | **NAO por default — risco** | o agente **escreve e le memorias sozinho** durante execucao | alta mas **opaca** |

A camada (4) e' poderosa e perigosa: o agente acumula estado duravel **fora
do git**, gerando **drift opaco nao-versionado** (ver antipattern "AI memory
abuse" abaixo). Refs:
[memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool).

**Regra que nao muda**: o que define o projeto vai pra camada (1)
(versionada); preferencia pessoal vai pra (3)/(4); **doc versionada > memoria
de agente** sempre que houver duvida. Cada ferramenta tem canal proprio, mas
o **conteudo canonical e' o mesmo** (single-source, evitar drift).

## Mapa por ferramenta `[2026-06-03]`

Em 2026 a convergencia e' em torno de **`AGENTS.md`** (ver proxima secao). A
tabela gira em torno de "le AGENTS.md nativamente?"; os arquivos
tool-especificos viram canal legado/complementar. `[VERIFICAR: 2026-06-03]`
— matriz de suporte muda rapido.

| Ferramenta | Le `AGENTS.md` nativo? | Canal proprio / legado | Capacidades extras |
|---|---|---|---|
| **OpenAI Codex** (CLI + cloud) | Sim | — | MCP, cloud agents |
| **GitHub Copilot** | Sim | `.github/copilot-instructions.md`, `.github/instructions/*.md` por path | MCP, Skills |
| **Cursor** | Sim (2.2+) | `.cursor/rules/*.mdc` (regra por glob; `.cursorrules` legado) | MCP |
| **Gemini CLI** | Sim | `GEMINI.md` (legado) | MCP |
| **Windsurf** | Sim | rules proprias | MCP |
| **Zed** | Sim | — | MCP |
| **Aider** | Sim | `CONVENTIONS.md` (legado) | — |
| **Claude Code** | **Nao** (auto-carrega `CLAUDE.md`) | `CLAUDE.md` + `~/.claude/.../memory/` | MCP, **Skills**, subagents, hooks |
| **Cline** | parcial | `memory-bank/` (workaround pre-memory-tool) | MCP |

**Nota Claude Code**: ele auto-carrega `CLAUDE.md`, **nao** `AGENTS.md`. Pra
usar `AGENTS.md` como canonical, importe-o de dentro do `CLAUDE.md` com
`@AGENTS.md` (ou symlink — no Windows exige Dev Mode/Admin). Em projeto
so'-Claude, `CLAUDE.md` sozinho basta.

## AGENTS.md — padrao estabelecido (nao mais "emergente")

`AGENTS.md` deixou de ser proposta e virou **padrao estabelecido**: em 2025
passou a ser governado pela **Agentic AI Foundation** (sob a Linux
Foundation), com adesao nativa de Codex, Copilot, Cursor, Gemini CLI, Aider,
Windsurf, Zed e outros. Refs: [agents.md](https://agents.md/);
[Agentic AI Foundation](https://openai.com/index/agentic-ai-foundation/).
`[VERIFICAR: 2026-06-03]`.

**Recomendacao 2026**: usar `AGENTS.md` na raiz como canonical e linkar pra
ele a partir de `CLAUDE.md` (`@AGENTS.md`) /
`.github/copilot-instructions.md` / `.cursor/rules/`. Reduz duplicacao; o
link mantem compatibilidade onde a ferramenta nao le `AGENTS.md`.

## Conteudo essencial do arquivo de IA

Independente do nome do arquivo, deve conter:

1. **Inventario "onde esta o que"** — `src/`, `docs/`, `experiments/`, `data/` (incluindo storage externo: `Z:\`, S3, etc.)
2. **Checklist "antes de agir"** — `Glob`/`Grep` em pastas X antes de propor recriar
3. **Convencoes** — naming, formato de status, idioma de docs
4. **Lista NUNCA** — comandos destrutivos proibidos, codigo intocavel, acoes que exigem confirmacao
5. **Foco atual + ponteiro pro checkpoint** — onde retomar

**Tamanho-alvo**: ~100-200 linhas, mas a metrica real nao e' contagem de
linhas e sim **curadoria** (ver "Context engineering" abaixo): so' o que a IA
precisa SEMPRE. O que e' consulta sob demanda fica no `MAP.md` e nos docs
focados, roteado — nao inlinado.

## Context engineering + prompt caching `[2026-06-03]`

Em 2026, **mais contexto nao e' melhor** — degrada o agente. Estima-se que
~65% das falhas de agentes em producao sao degradacao de contexto
("context rot"): o sinal se dilui em tokens irrelevantes. Refs:
[Anthropic — context engineering](https://platform.claude.com/cookbook/).

Implicacoes pra esta metodologia (varias ja' eram feitas sem nome):
- **Rotear, nao inlinar**: o `MAP.md` ("quero X → va Y") e' context
  engineering — carrega o trecho relevante sob demanda em vez de despejar
  tudo. Mantenha.
- **Curar > encher**: prefira `AGENTS.md` enxuto + ponteiros a um arquivo de
  500 linhas que a IA ignora no meio.
- **Prompt caching — ordem importa**: conteudo **estavel** primeiro
  (`AGENTS.md`/`CLAUDE.md`, >=~1024 tokens) e' prefixo cacheavel — cache hit
  corta latencia/custo drasticamente. Conteudo **volatil** (`STATUS.md`,
  lembretes do dia, hook ephemero) vem **depois** do estavel, senao invalida
  o cache a cada sessao. Refs: doc de prompt caching da plataforma.

## MCP — Model Context Protocol `[2026-06-03]`

**Ausente na versao antiga; e' o padrao de conectividade agente↔dados de
2026.** MCP padroniza como um agente acessa ferramentas, dados e recursos via
servidores ("MCP servers"). Refs:
[modelcontextprotocol.io](https://modelcontextprotocol.io/).

**Como se aplica aqui**: em vez de scripts ad-hoc, voce pode expor artefatos
canonicais do projeto como um **MCP server local** — ex: um server que serve
`tickets/` (status, dependencias), o `manifest.jsonl` (runs/metricas), ou um
dataset. O agente consome via protocolo padrao, e o mesmo server serve
qualquer ferramenta MCP-aware.

| Opcao | Quando |
|---|---|
| Script `scripts/index.py` etc. | leitura local simples, 1 ferramenta, sem necessidade de protocolo |
| **MCP server local** | varios agentes/ferramentas consomem o mesmo recurso; quer schema/contrato; quer acoes (nao so' leitura) |
| Tool bridge (export) | destino e' ferramenta corp externa (ver [tickets-and-tool-bridges](tickets-and-tool-bridges.methodology.md)) |

**Seguranca (NUNCA)**: MCP server com permissao de escrita/acao = superficie
de ataque. Principio de menor privilegio; acao com side-effect externo exige
aprovacao explicita do usuario (mesma regra dos tool bridges).

## Agent Skills (SKILL.md) `[2026-06-03]`

**Ausente na versao antiga.** Skills empacotam uma capacidade reutilizavel
(instrucoes + scripts + recursos) num `SKILL.md` com *progressive disclosure*
(o agente carrega o detalhe so' quando aciona a skill — economiza contexto).
Spec aberta, portavel entre ferramentas. Refs:
[code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills).

As **operacoes repetiveis** desta metodologia sao candidatas obvias a Skills:

| Operacao da metodologia | Vira skill que... |
|---|---|
| Promocao exploratorio→frozen ("welding") | reescreve codigo de lab em frozen + gera README IMRaD + valida `run.py` em 1 linha |
| Auditoria periodica (§7 do core) | roda o recipe de audit (re-gera INDEX, procura `[VERIFICAR:]` vencidos, revisa ADRs) |
| Export de tool bridge | le `tickets/` + frontmatter e emite CSV no formato da ferramenta destino |
| Geracao de `INDEX.md` | parseia frontmatter e gera o indice |
| Assessment brownfield (§11.2) | inventario + maturidade por pilar + matriz de custo |

Skill vs MCP vs script: **skill** = procedimento que o agente executa;
**MCP** = recurso/dado/acao que o agente acessa; **script** = automacao local
simples. Combinam.

## Subagents e fan-out paralelo `[2026-06-03]`

Um orquestrador que distribui ~N subagents em paralelo corta trabalho
multi-file/multi-fonte (~50-70% em tarefas grandes). Duas operacoes desta
metodologia sao **fan-outs embaracosamente paralelos**:
- **Auditoria periodica** (§7 do core) — um subagent por pilar/pasta.
- **Assessment brownfield** (§11.2) — um subagent por pilar medindo maturidade + custo.

**Caveat**: subagents devem retornar **sumarios estruturados**, nao despejar
o contexto inteiro de volta (senao anula o ganho de context engineering).
Refs: docs de agent teams / subagents da ferramenta.

## Agent evals — testar comportamento de agente `[2026-06-03]`

`AGENTS.md`, Skills e hooks sao **prompts** — e prompts regridem em silencio
quando editados. Isso e' um ponto cego dado que a metodologia insiste que "o
fato checavel vira teste" (ver [doc-vs-code](doc-vs-code.methodology.md)).

Pratica 2026: **evals em CI** quando um PR toca prompts (~60%
deterministico / ~30% LLM-as-judge / ~10% humano). Eval minimo pra esta
metodologia: *assert que o agente roda `Glob`/`Grep` antes de propor recriar
algo* (o incidente-fundador do TCF). Encaixa em "Testes categorizados" (ver
[lab-work](lab-work.methodology.md)) e na auditoria periodica.

## Busca: grep-first vs RAG / busca semantica `[2026-06-03]`

Os melhores agentes de codigo de 2026 (Claude Code, Cursor, etc.) descobrem
conteudo via **grep / arvore de arquivos / busca estruturada**, **nao** via
vector DB — Claude Code chegou a abandonar RAG com vector-DB. Um leitor
"ai-primary" pode erroneamente assumir que precisa de um indice de embeddings.

**Stance da metodologia**:
- **Default**: busca agentica (`Glob`/`Grep`) sobre o repo. E' o que o
  checklist "antes de agir" ja' pressupoe.
- **Busca semantica** (ex: SQLite **FTS5** + **sqlite-vec**, local-first) so'
  quando ha' **busca conceitual cross-doc** num corpus grande (ex: uma
  `findings/` extensa, ou a bibliografia) onde lexical nao basta.
- **Nao** construa indice vetorial por reflexo. Refs:
  [is RAG dead?](https://www.mindstudio.ai/blog/is-rag-dead-what-ai-agents-use-instead).

## Structured output / schema como contrato `[2026-06-03]`

`manifest.jsonl`, frontmatter de ticket e `.tool-bridges.yaml` sao
contratos implicitos — formalize-os com **JSON Schema** validado **tanto pelo
agente quanto pelo `scripts/index.py`**. A partir de fim-2025, MCP espera
resultados conformes a um output schema, entao expor esses artefatos via MCP
ja' pede schema. Sugestao: `manifest.schema.json`, `ticket.schema.json` no
repo.

## Hooks de ciclo de vida (cross-tool) — deterministico, opcional

`CLAUDE.md` ja' e' auto-carregado pelo Claude Code, entao o hook
**SessionStart e opcional**. Vale quando: voce quer um primer **muito curto**
(5-15 linhas) garantido a cada sessao; lembretes **ephemerais** que mudam
toda semana; ou **garantia deterministica** de que algo foi visto. Pule se o
`CLAUDE.md` ja' cobre os 5 itens essenciais. Em 2026 hooks de ciclo de vida
existem cross-tool (nao so' Claude Code) — generalize a ideia.

**Custo de instalar o hook**: editar `.claude/settings.json` e' classificado
como "self-modification of agent configuration" — requer aprovacao explicita
do usuario; em modo auto a IA **nao escreve o hook sozinha**, precisa pedir.

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "hooks": {
    "SessionStart": [{
      "matcher": "",
      "hooks": [{
        "type": "command",
        "command": "pwsh -NoProfile -Command \"if (Test-Path '.claude/session-start-context.md') { Get-Content '.claude/session-start-context.md' -Raw }\""
      }]
    }]
  }
}
```

> **Use `pwsh` (PowerShell 7+), nao bare `powershell`.** No Windows o
> `powershell` 5.1 corrompe acentos (saida nao-UTF-8) do contexto injetado —
> `inicio`/`sessao` viram mojibake. `pwsh` le/escreve UTF-8 por default.
> (Fallback com 5.1: `Get-Content ... -Raw -Encoding UTF8` +
> `[Console]::OutputEncoding=[Text.Encoding]::UTF8`.)

Conteudo de `session-start-context.md`: 5-15 linhas de lembrete operacional.
**Nao depende de LLM lembrar — e injetado a cada sessao.**

## Observabilidade de agentes (OTel GenAI) — opcional `[2026-06-03]`

Complemento **maquina** do diario datado / `manifest.jsonl`: traces por
`conversation-id`, spans por chamada, captura de tokens/custo/falha. Claude
Code / Codex / Copilot exportam **OpenTelemetry** (semantic conventions de
GenAI). Adote so' se a escala justificar (ver §8 do core). Refs:
[OpenTelemetry GenAI](https://opentelemetry.io/).

## Proveniencia / autenticidade `[2026-06-03]`

Marcar autoria (`authored-by: ai | human | mixed`) e proveniencia de
artefatos vira **obrigatorio em ago/2026** (EU AI Act Art. 50; California
SB 942; C2PA 2.x = ISO/IEC 22144). Para software publicavel
(`CITATION.cff`/Zenodo/JOSS) e' integridade de pesquisa. Baseline ja'
existente: `git_sha` + `manifest.jsonl`. Detalhe e a dimensao de revisao
critica em [research-discipline](research-discipline.methodology.md).

## Antipattern — AI memory abuse (modernizado)

| Antipattern | Sintoma | Antidoto |
|---|---|---|
| **Tudo virou memoria de agente** | contexto-de-projeto na camada (3)/(4), indexavel zero, nao-versionado | projeto-context vai pra `CLAUDE.md`/`AGENTS.md` versionado, nao memoria |
| **Drift opaco de memoria filesystem** | agente acumulou estado duravel fora do git; ninguem sabe o que ele "lembra" | limitar camada (4) a preferencias genuinas; auditar o dir de memoria (§7 do core); ferramentas tipo `claude-mem` auto-capturam sessoes — revisar o que entra |
| **memory-bank como single-source** | `memory-bank/` (Cline) tratado como canonical em vez de workaround | e' UMA convencao pre-memory-tool; canonical e' a camada (1) versionada |

## Referencias

Ver [bibliography](bibliography.methodology.md) → "AI tools / agentes" e
"Proveniencia / autenticidade de conteudo". **Toda essa secao e' alta
cadencia** — confirme via WebFetch antes de tratar como verdade.
