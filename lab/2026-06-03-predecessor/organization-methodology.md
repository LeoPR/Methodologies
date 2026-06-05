---
title: Metodologia de organizacao de projetos (codigo + pesquisa + IA)
type: reference
status: active
created: 2026-05-20
updated: 2026-06-03
audience: ai-primary, human-secondary
editorial-principle: aponta padroes canonicos, nao re-explica literatura
how-to-use: consulta sob demanda via routing table (proxima secao); nao leitura linear
applies-to: projetos academicos / pesquisa / software cientifico com co-existencia de codigo, experimentos, artigos, e colaboracao com agentes de IA
keywords: [methodology, diataxis, adr, fair, research-compendium, agents-md, mcp, skills, git, lab-work, ai-agents, epistemic-discipline]
---

# Metodologia de organizacao para projetos academicos / pesquisa / software cientifico

> **Receita / produto.** Documento unico, completo e autocontido com **todas
> as tecnicas de organizacao** — de pastas, documentacao, decisoes, lab work e
> memoria de agentes de IA. Cross-project, portavel, agnostico de stack.
> Sintese de literatura consolidada (biblioteconomia, engenharia de software,
> ciencia aberta) + a camada de tooling de IA de 2026.
>
> A pesquisa que produziu esta receita (analise, exploracoes, descartes) vive
> na cozinha experimental do projeto: `../lab/`.
>
> **Principio editorial**: este doc **aponta direcoes e nomeia padroes
> canonicos** — nao re-explica em detalhe o que a literatura citada (§Bibliografia)
> ja' cobre. Leitor humano: clique nos links. **IAs**: use WebFetch /
> conhecimento previo pra expandir cada referencia sob demanda. O valor e' a
> **sintese e ordenacao** das fontes, nao a reescrita delas.

## Roteamento por intencao (este arquivo, por secao)

| Voce pede / pergunta | Va para |
|---|---|
| "Comecar projeto novo" / "Setup inicial" | §TL;DR → §17.1 → §7 → §12 Fase 1 |
| "Onde guardo X?" | §6 Estrutura de pastas |
| "Como organizar docs?" | §2 Pilar 2 (Diataxis) |
| "Documentar em prosa ou codigo?" / "isso e' duplicado?" | §4 Codigo, prosa e oraculo |
| "Como registrar decisao?" | §2 Pilar 3 (ADR) |
| "Como rodar / organizar experimento?" | §3 Lab work (Pilar 4) |
| "Hipoteses / pausa-retomar / notas-diario" | §3 (Registry / Checkpoint / Diario) |
| "Git / versionamento / .gitignore / arquivo grande" | §7 Versionamento |
| "Configurar Claude/Copilot/Cursor/Cline/Gemini" / "MCP / Skills / memoria / context engineering / evals" | §8 Instrumentacao de IA |
| "Como afirmar / citar / pesquisar X?" / "preco / dado que muda rapido" | §9 Disciplina de pesquisa |
| "Seguranca / ROI / SLO / proveniencia / revisao critica" | §10 Revisao critica |
| "Tickets / planejamento" / "Exportar pra Jira / cards retroativos" | §11 Tickets e tool bridges |
| "Caches / venvs / build artifacts / setup ambiente" | §Apendice A |
| "Auditoria periodica" | §14 |
| "Antipattern X" / "Quando NAO aplicar" | §13 / §15 |
| "Leia esta metodologia" / "Aplicar em projeto novo / existente" | §17 (brownfield exige assessment) |

## Convencoes e principios cross-cutting (aplicam SEMPRE)

### Principio editorial — aponta, nao re-explica

Aponta padroes canonicos; nao re-explica a literatura (§Bibliografia). IAs
usam WebFetch / conhecimento previo pra expandir refs sob demanda.

### FORTE vs LOCAL

- **FORTE** = vinculo direto a literatura; principio que se aplica
  independente de nomes (nao renomeavel).
- **LOCAL** = exemplo renomeavel — nomes de pasta, metaforas, IDs (ex:
  "dirty/clean", "welding", "EXP-NNN"). **Convencoes locais do projeto vencem
  os nomes deste doc.**

### Principios que aplicam SEMPRE

1. **Editorial**: este doc aponta; literatura detalha. WebFetch quando precisar de profundidade.
2. **Pesquisa**: nao invente. Categorize *sabe* vs *infere* vs *acha*. Diga quando nao sabe (§9).
3. **Versionamento**: tudo entra no repo, exceto regeneravel ou nao-pertinente (§7).
4. **Imutabilidade**: ADR aceito + EXP frozen = nunca mude; crie novo com `Supersedes`.
5. **Single-source**: ADR canonical; outros docs referenciam, nao duplicam.
6. **Verificacao antes de afirmar**: `Glob`/`Grep`/`Test-Path` antes de propor recriar.
7. **Codigo e' o documento do COMO**: prosa carrega so' o PORQUE (§4).

### Para IAs — NUNCA / SEMPRE

**NUNCA**: inventar referencia que "soa certo" · aceitar premissa do usuario
sem checar · propor recriar algo sem `Glob`/`Grep` antes · escolher
silenciosamente entre fontes em conflito · servir dado vivo (preco/estoque/
noticia) sem timestamp de captura · **aplicar/alterar estrutura de projeto
existente sem assessment** (§17.2).

**SEMPRE**: diga quando nao sabe (lacuna admitida > invencao) · ofereca
WebFetch quando o conhecimento e' mutavel · cross-link em vez de duplicar ·
marque claim de fonte fraca com `[VERIFICAR: data]` · revalide dado vivo na
fonte primaria + anexe `capturado_em` · **reporte impacto antes de modificar**
projeto existente e aguarde aprovacao.

### Assessment antes de alterar projeto existente — FORTE

Ao receber "aplique a metodologia ao projeto X", a IA **NUNCA comeca
modificando arquivos**: primeiro avalia + reporta impacto; aguarda aprovacao
por etapa (§17.2).

## TL;DR — quando voce so' quer copiar e colar

**Zero**: `git init` + `.gitignore` (template oficial da linguagem em
[github.com/github/gitignore](https://github.com/github/gitignore)).
Mesmo solo, sem remoto.

Depois, crie estes arquivos na raiz, nesta ordem:

1. `AGENTS.md` (padrao **estabelecido** em 2026 — Agentic AI Foundation; §8)
   ou `CLAUDE.md` — inventario "onde esta o que" + checklist "antes de agir" +
   lista NUNCA. ~100-200 linhas, curado. Sempre carregado. **Nota Claude
   Code:** auto-carrega `CLAUDE.md`, NAO `AGENTS.md`; importe com `@AGENTS.md`.
2. `MAP.md` — 1 pagina com `tree` + tabela "quero fazer X → va para Y".
3. *(opcional)* `.claude/settings.json` + `session-start-context.md` — hook
   injeta lembretes deterministicos no inicio de sessao.
4. `docs/adr/` — Architecture Decision Records numerados, imutaveis.
5. `docs/{tutorials, how-to, reference, explanation}/` — divisao Diataxis.
6. `docs/vocabulary.md` — termos controlados.
7. `experiments/` (ou `notebooks/`) — labs com YAML frontmatter.
8. `scripts/index.py` — auto-gera `INDEX.md` lendo frontmatter.

Depois, audite a cada 60-90 dias.

---

## 1. Por que esta metodologia existe

Projetos academicos / pesquisa acumulam **3 tipos de artefato que conflitam** se misturados:

| Tipo | Exemplo | Cadencia | Audiencia |
|---|---|---|---|
| **Codigo de producao** | `src/`, biblioteca publicavel | estavel | dev futuro / usuario |
| **Experimentos** | `experiments/`, notebooks | descartavel, alta rotatividade | voce mesmo em 3 meses |
| **Conhecimento** | docs, ADRs, artigos, notas | semi-estavel | revisor, colaborador, IA |

**Sintomas de mistura**: IA propondo recriar coisas que existem; decisoes
refeitas; docs estaveis poluidos com WIP; reviewer perdido. E' problema de
**arquitetura de informacao**, com decadas de literatura — esta e' a sintese
operacional.

## 2. Os 4 pilares (sintese)

Cada pilar resolve **um** problema. Combinados, cobrem o ciclo todo.

| # | Pilar | Resolve | Framework canonico | Pasta padrao |
|---|---|---|---|---|
| 1 | **Wayfinding** | "Onde esta X?" | Information Architecture (Morville) | raiz: `CLAUDE.md`/`AGENTS.md` + `MAP.md` + `STATUS.md` |
| 2 | **Docs estaveis** | "Como uso/entendo isso?" | Diataxis (Procida) | `docs/{tutorials,how-to,reference,explanation}/` |
| 3 | **Decisoes** | "Por que decidimos X?" | ADR/MADR (Nygard) | `docs/adr/NNNN-*.md` |
| 4 | **Lab/experimentos** | "Esse resultado e' reprodutivel?" | Research Compendium + FAIR4RS | `experiments/` ou `notebooks/` |

### Pilar 1 — Wayfinding (descoberta)

**Ref**: Morville — *Ambient Findability* (2005) + *IA for the Web and Beyond*
(2015). Componentes: ontologia, taxonomia, information scent. **Implementacao**
— 3 arquivos na raiz: `CLAUDE.md`/`AGENTS.md` (instrucoes pra IA — §8), `MAP.md`
(arvore + tabela "quero X → va Y"), `STATUS.md` (boletim do dia).

### Pilar 2 — Docs estaveis (Diataxis)

**Ref**: Procida — [diataxis.fr](https://diataxis.fr/). 4 quadrantes
ortogonais, **toda doc cabe em exatamente um**:

| | Pratico (mao na massa) | Teorico (compreensao) |
|---|---|---|
| **Estudando** (aprender) | **Tutorial** | **Explanation** |
| **Trabalhando** (resolver) | **How-to** | **Reference** |

Pastas espelham: `docs/{tutorials, how-to, reference, explanation}/`.

### Pilar 3 — Decisoes (ADR)

**Ref**: Nygard 2011; MADR — [adr.github.io/madr](https://adr.github.io/madr/).
- Arquivo: `NNNN-imperative-phrase.md` (ex: `0007-use-postgres-not-mongo.md`)
- **Imutavel apos `accepted`**. Mudanca = novo ADR com `Supersedes NNNN`.
- Template MADR: Context / Considered Options / Decision / Pros and Cons.
- **Criar ADR quando**: decisao arquitetural OU muda comportamento publico OU
  reverter custaria muito. **Nao criar** pra bug fix nem refactor local.

### Pilar 4 — Lab/experimentos (Compendium + FAIR4RS)

Modo exploratorio (bagunca permitida) vs modo frozen (imutavel apos fechado);
cada experimento frozen e' um research compendium. **Detalhe completo em §3.**

## 3. Lab work / experimentos — Pilar 4 aprofundado

> Lab work e' a parte que vira arqueologia primeiro (60-90 dias). Vale camada
> extra de detalhe. **Refs**: Marwick/Boettiger/Mullen 2018; Chue Hong et al.
> 2022 (FAIR4RS). Nomes "dirty/clean", "welding", "EXP-NNN" sao LOCAIS.

**Estrutura minima**:
```
experiments/
├── clean/EXP-NNN-nome/          # frozen
│   ├── README.md (YAML frontmatter)
│   ├── config.json
│   ├── manifest.jsonl
│   └── report.md
└── dirty/YYYY-MM-DD-tema/       # exploratorio
    └── ...
```

### Os dois modos de lab work

| Modo | TCF (LOCAL) | Scrum | Pragmatic | Mineault | Brooks 1975 |
|---|---|---|---|---|---|
| Exploratorio, descartavel | "dirty" | spike | tracer bullet | research code | "throwaway prototype" |
| Frozen, reproduzivel | "clean" | story / PBI | production code | research software | "production code" |

**Principio FORTE**: separar fisicamente (pastas diferentes), regras
diferentes pra cada. Misturar = "lixo arqueologico".

### Modo exploratorio — regras

**Permissivo em**: bagunca, codigo duplicado, dead code, hipoteses mudando.
**Estrito em**: README curto (pergunta + hipotese) — FORTE; **datado**
`YYYY-MM-DD-` — FORTE (lab notebook fisico desde sec XIX: Faraday/Edison/Bell
Labs); **sub-experimentos numerados** (`01-`, `02-`) — FORTE; vocabulario
disciplinado — FORTE; **imutavel apos fechado** — FORTE (pra continuar, fork novo).

### Modo frozen — regras

**Imutavel apos fechado** — FORTE. Re-run gera nova versao (`EXP-NNN-v2`).
Mesma logica de artefato citavel (paper, Zenodo DOI, release). Cada experimento
e' um *research compendium*:

| Arquivo / convencao | Padrao subjacente | Forca |
|---|---|---|
| `README.md` em formato IMRaD | IMRaD (Sollaci & Pereira 2004) | FORTE |
| `run.py` executavel-em-uma-linha | Research Compendium | FORTE |
| `config.json` / `params.yaml` | Config over code | FORTE |
| `manifest.jsonl` (1 linha/run) | MLflow / W&B / Sacred run log | FORTE |
| `outputs/` | Cookiecutter DS `data/processed/` | FORTE |
| `report.md` (discussao final) | IMRaD Discussion | FORTE |
| Nome `EXP-NNN-tema/` | identificador estavel + slug | LOCAL |

### README de experimento — formato IMRaD — FORTE

```markdown
## Pergunta cientifica          # Introduction
## Hipotese                     # H1 explicita vs H0
## Metodo                       # Methods (### Datasets / Metrica)
## Resultado                    # Results (factual)
## Discussao                    # Discussion (interpretacao)
## Limitacoes / Threats to validity   # Wohlin 2012
## Como rodar / reproduzir
## Conexoes / See also
```
Os **4 movimentos** (intro / metodo / resultado / discussao) sao FORTE.

### Manifest.jsonl — log append-only de runs — FORTE

Cada execucao de `run.py` append 1 linha JSON. **Por que JSONL**: versionavel
em git (deltas pequenos); parseavel linha-a-linha (`jq`, `pandas`); sem schema
migration. Campos:
```json
{
  "timestamp": "2026-05-20T...",
  "experiment_id": "EXP-007-...",
  "git_sha": "abcd1234",          // FORTE: identifica versao do codigo
  "data_sha": {"D1": "sha256:..."},   // FORTE quando dataset evolui
  "config_hash": "ef89...",
  "metrics": { ... },
  "outcome": "confirmed" | "refuted" | "partial" | "inconclusive"  // FORTE: combate publication bias
}
```
**Anti-pattern**: manifest sem `git_sha` → runs ambiguos. **Nota 2026
(schema-as-contract)**: publicar `manifest.schema.json` (JSON Schema) validado
por `run.py` E `scripts/index.py` torna o manifest um contrato — formato
esperado ao expor via MCP (§8).

### Promocao exploratorio → frozen — FORTE

"Plan to throw one away" (Brooks 1975); "refactor spike output, not transplant"
(XP/Beck). Sequencia: (1) sub-exp fecha com hipotese **confirmada/refutada**
explicita; (2) codigo **reescrito** (nao copiado) em frozen; (3) README IMRaD
**do zero**; (4) `run.py` executavel em uma linha; (5) `manifest.jsonl` registra
runs; (6) opcional tag git / DOI Zenodo. O nome da operacao e' LOCAL (TCF:
"welding"; literatura: harden/productionize/promote).

### Praticas universais (independem de nomes)

a) **Vocabulario disciplinado** (banir superlativos) — FORTE (Strunk & White;
Day & Gastel). Evitar "incrivel/campeao/descoberta"; preferir "diferenca de N
bytes em cenario X".
b) **Hipotese antes do experimento** — FORTE (pre-registration; Chambers 2017).
c) **Round-trip / invariant check como AC** — FORTE (property-based testing;
Claessen & Hughes 2000): `decode∘encode = id`.
d) **Threats to validity** explicitos — FORTE (Wohlin 2012): Internal /
External / Construct / Conclusion.
e) **Datasets representativos vs sinteticos extremos** — FORTE (ecological
validity; Brunswik 1956): dataset de design vs de stress.

### Antipatterns de lab work

| Antipattern | Antidoto |
|---|---|
| **Lab graveyard** (pastas datadas esquecidas) | `status: closed/archived` + audit |
| **Hot-edit em frozen** | "frozen = imutavel"; mudanca = nova versao |
| **Manifest sem git_sha** | sempre logar git SHA |
| **Notebook spaghetti em producao** | promover oficialmente (refator) |
| **"Tudo deu certo"** (so positivos) | campo `outcome`; preservar refutados |
| **Storytelling post-hoc** | escrever H1 antes de rodar |
| **Vocabulario torcido** | banlist em `vocabulary.md` |

### Padroes adicionais de lab work (adote o que se aplica)

| Padrao | Proposito | Path | Base |
|---|---|---|---|
| **Diario datado** | cronologia de decisoes em prosa (contexto humano) | `notas/diario/YYYY-MM-DD.md` | daybook (Vanderburg) — FORTE |
| **Registry de hipoteses** | tabela cross-exp; status `aberta/em-exp/confirmada-empirica/conceitual/refutada/adiada/absorvida` | `docs/hipoteses.md` | research programmes (Lakatos 1978) — FORTE |
| **Narrativa / logbook** | prosa ligando experimentos num arco | `notas/historia-do-projeto.md` | tech reports; SRE postmortem — FORTE |
| **Findings consolidados** | achados de N exps sobre 1 tema | `docs/findings/F-NNN-tema.md` | systematic review — FORTE |
| **Checkpoint** | save-state antes de pausa 1+ semana (cold-start IA) | `notas/checkpoints/YYYY-MM-DD-tema.md` | memex (Bush 1945); GTD |
| **Design backlog / icebox** | ideias fora de escopo (catalogo, nao roadmap) | `notas/futuras-otimizacoes.md` ou `docs/theory/` | Lean icebox — FORTE |
| **Testes categorizados** | Round-trip/Unit/Integration/Regression/Performance | `tests/test_roundtrip_*.py` | Claessen&Hughes; Beck; Cockburn — FORTE |
| **Changelog por marco logico** | marco (v0.5→v0.6) cross-linkado a historia | `CHANGELOG.md` | — |

Experimento que confirma hipotese significativa → vira **ADR** (Pilar 3);
hipoteses do registry geram **tickets** (§11) quando viram trabalho concreto.

## 4. Codigo, prosa e oraculo — o que documentar (e o que deletar)

> Refina o single-source (Pilares 2-3) pro caso doc-vs-codigo — critico quando
> o leitor (humano OU IA) ja' le o codigo.

### Tabela de altitude — cada fato tem UMA fonte canonica — FORTE

DRY e' sobre **conhecimento**, nao texto de codigo (Hunt & Thomas). Codigo
**over-especifica** (congela 1 das N implementacoes) e **under-especifica**
(nao diz a faixa, o porque, alternativas rejeitadas) — Parnas & Clements 1986.

| Tipo de informacao | Fonte canonica | NUNCA em prosa |
|---|---|---|
| **COMO** (mecanica, fluxo) | codigo + docstring | re-narrar passo-a-passo |
| **Exemplo / contrato / invariante / numero** | teste, property, doctest, type, config | copiar o valor esperado |
| **PORQUE** (intencao, alternativa rejeitada, restricao) | ADR / `explanation/` | — irredutivel; so' vive aqui |
| **Estrutura de sistema / limites** | 1 diagrama (C4-Context) | re-desenhar em cada doc |

### Teste de reconstrucao bidirecional — gate de admissao — FORTE

1. **Apagado este texto, regenero do codigo/teste?** SIM → nao escreva; deixe
   ponteiro ou gere automatico.
2. **Apagado o codigo, este texto basta pra refazer?** NAO → carrega o PORQUE;
   mantenha, curto.

So' sobrevive prosa que **falha (1) e passa (2)**. Formalmente: guarde so'
`K(doc | codigo)` (Kolmogorov/MDL); parafrase do codigo (`K~=0`) e' deletavel.
Apagado o doc, a IA reconstroi o COMO mas **alucina o PORQUE**
(arXiv:2209.00398). Ideal (Knuth): **UMA fonte da qual ambas derivam**.

### Oraculo vs prosa — a redundancia UTIL e' executavel — FORTE

Redundancia so' e' UTIL se houver **artefato executavel que falha na
divergencia** (teste/property/contrato/doctest). `assert count == 10` e' util;
"conta ate 10" em prosa drifta (22-42% dos comentarios divergem — Wen et al.
ICPC 2019). Codigo nao e' oraculo de si mesmo (Ulfers 2018). Em Python,
**doctest** e' o oraculo de menor custo; **tipos** sao doc executavel.

### Rule of Three aplicado ao FLUXO de documentacao — FORTE

Nao formalize prosa de N=1. Achado fica no `report.md` ate reaparecer em >=3
labs/tickets; so' entao consolida. **Antipattern**: prosa-espelho (re-narra o
codigo) — drift garantido (Parnas, *Software Aging*).

## 5. Pilares complementares (escolha o que se aplica)

Os 4 pilares cobrem ~80%. Adote so' o que faz sentido (detalhe na fonte —
§Bibliografia):

| Padrao | Quando aplicar | Ref |
|---|---|---|
| **Zettelkasten (Luhmann)** | muitas observacoes/insights soltos; nota = 1 ideia atomica, `[[links]]` | Ahrens 2017 |
| **PARA (Forte)** | conhecimento pessoal alem do projeto (Projects/Areas/Resources/Archives) | Forte 2022 |
| **Cookiecutter DS / Mineault** | projeto ML/DS: `data/{raw,interim,processed}/`, `src/<pkg>/`, `models/` | goodresearch.dev |
| **Conventional Commits + SemVer + Keep a Changelog** | release publico; changelog automatico (`git-cliff`) | conventionalcommits.org |
| **Citacao academica** | artigo/software publicavel: `CITATION.cff`, DOI Zenodo, JOSS | citation-file-format |
| **Comunidade / contribuicao** | aberto a colaboradores: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `.github/` | opensource.guide |
| **Metadados estruturados** | dataset publicavel: Dublin Core, DataCite, schema.org/Dataset | datacite.org |

(Tickets / planejamento em markdown: ver §11.)

## 6. Estrutura de pastas canonical (referencia)

Composicao dos pilares. Adapte: nem todo projeto precisa de todos.

```
projeto/
├── .git/                         <- versionamento (foundational; §7)
├── .gitignore                    <- contrato do que NAO versiona
├── README.md                     <- entry point humano
├── CLAUDE.md / AGENTS.md         <- entry point IA (§8)
├── MAP.md                        <- mapa 1-pagina
├── STATUS.md                     <- boletim atual
├── CHANGELOG.md / CITATION.cff / LICENSE
├── pyproject.toml / package.json <- conforme stack
├── .claude/ | .github/ | .cursor/rules/   <- instrumentacao IA (§8)
├── src/<package>/                <- codigo canonico
├── tests/
├── scripts/index.py              <- auto-gera INDEX.md
├── tickets/                      <- §11
│   ├── README.md
│   └── <ID>-<tema>.md
├── docs/
│   ├── tutorials/ how-to/ reference/ explanation/   <- Diataxis
│   ├── adr/                      <- decisoes numeradas, imutaveis
│   ├── vocabulary.md             <- termos controlados (single source)
│   └── findings/                 <- resultados consolidados (se pesquisa)
├── experiments/
│   ├── clean/EXP-NNN-*/          <- replicaveis
│   └── dirty/YYYY-MM-DD-*/       <- exploratorios
└── data/{raw,interim,processed}/ <- se aplicavel; ou link pra storage externo
```

## 7. Versionamento e higiene de repositorio (foundational)

> **Dia zero.** Mesmo solo sem remoto, `git init` — ganha auditoria,
> branching, recuperabilidade. Custo 0. Tool-agnostico (git por dominancia
> 2026; principios valem pra mercurial/fossil/jj/sucessores).

### Signal vs ruido — o que entra no repo

**Entra** (signal): codigo, docs, configs, lock files (`uv.lock`,
`package-lock.json`, `Cargo.lock`), datasets pequenos representativos, scripts
pra **recriar** o que nao entra.
**Nao entra** (ruido): builds (`dist/`, `*.pyc`), caches (`__pycache__/`,
`node_modules/`), outputs regeneraveis, datasets gigantes externos,
logs/dumps, credentials/`.env`, arquivos de editor, **versoes manuais**
(`relatorio_v2.md`).

### Antipattern critico — versionamento manual

**Nao crie** `arquivo_v2.md`, `script_old.py`, `backup_2026_05_10/`. Git ja'
versiona (`git log`/`show`/`diff`/`tag`). **Excecao**: artefato explicitamente
imutavel (ADR aceito, EXP frozen, release) — ai' "v2" e' nova decisao formal.

### .gitignore como contrato

Templates oficiais por linguagem em
[github.com/github/gitignore](https://github.com/github/gitignore). **Regra**:
se voce sempre ignora o mesmo arquivo, adicione ao `.gitignore`. Working tree
limpo = sinal saudavel.

### Arquivos grandes — escolher estrategia

| Caso | Estrategia |
|---|---|
| Dataset reproduzivel via download | `scripts/fetch_data.py` + `.gitignore` |
| Dataset intermediario processado | storage externo (S3/NAS) via `config/storage.json` |
| Binario unico nao-reproduzivel | **Git LFS** ou archive + checksum + README do artefato |
| Modelo ML treinado (~GB) | LFS, HuggingFace Hub, ou **DVC** |

(2026: alem de DVC, considerar **lakeFS** / **Quilt** em escala.) **Regra**:
artefato grande so' entra se unico-irrecuperavel; o script de recriacao entra.

### Higiene de commits / branching / colaboracao

- **1 commit = 1 mudanca atomica logica**; message = tipo (`feat:`/`fix:`/
  `docs:`) + titulo + paragrafo com *por que*. Nao commitar codigo quebrado em
  main (WIP em branch).
- **Branching**: Trunk-based (equipe pequena, CI forte) / GitHub Flow (OSS) /
  Git Flow (releases com hotfix). Documente a escolha em `CONTRIBUTING.md`/ADR.
- **Multi-pessoa**: PR review, branch protection, CODEOWNERS, pre-commit hooks
  ([pre-commit.com](https://pre-commit.com/)), signed commits, docs no repo.

### Reprodutibilidade — o teste fundamental

Posso clonar e reproduzir o estado em **≤ 3 comandos**?
```
git clone <repo> && cd <repo> && ./scripts/setup.sh && ./scripts/run.py
```
Se nao → dependencia implicita nao-versionada. Enderece ou documente como
excecao.

### Antipatterns de versionamento

`"Final final v3"` (→ tag) · commit gigante "wip" (→ atomic) · `push --force`
em main (→ so' em branch propria) · segredo commitado (→ `.env`+detect-secrets)
· dataset gigante (→ LFS/externo) · cache/build versionado (→ `.gitignore`,
§Apendice A) · branch eterna (→ merge/descarte) · doc em Drive separado (→ no
repo) · toolchain implicita (→ lock file + Dockerfile/nix).

## 8. Instrumentacao para agentes de IA  `[CAMADA ALTA CADENCIA — re-verificar]`

> Tooling de IA muda em meses. Fatos de ferramenta marcados `[2026-06-03]`;
> re-verificar a cada auditoria (§14). Os **principios** (single-source,
> memoria em camadas, doc versionada > memoria, contexto curado > volume) sao
> estaveis; os **produtos** nao.

### Principio chave — memoria em camadas

IA **nao tem memoria implicita** entre sessoes; sao mecanismos explicitos. Em
2026 sao **quatro** (a 4a e' nova):

| # | Camada | Onde | Versionado/auditavel? | Conteudo |
|---|---|---|---|---|
| 1 | Arquivos sempre carregados | `CLAUDE.md`/`AGENTS.md` | SIM (git) | operacional do projeto, estavel |
| 2 | Hook deterministico | `.claude/settings.json` + `session-start-context.md` | depende | primer ephemero (5-15 ln) |
| 3 | Memoria explicita do agente | `~/.claude/.../memory/`; `memory-bank/` (Cline) | NAO (user-scope) | preferencias, cross-projeto |
| 4 | **Memoria filesystem (NOVO)** | memory tool / `/mnt/memory`; contexto 1M | **NAO — risco** | agente escreve/le memorias sozinho |

A camada (4) gera **drift opaco nao-versionado** (ver antipattern em §13).
**Regra estavel**: o que define o projeto vai pra (1) versionada; preferencia
pessoal pra (3)/(4); **doc versionada > memoria de agente**.

### Mapa por ferramenta `[2026-06-03]`

Convergencia em torno de **`AGENTS.md`**. `[VERIFICAR: 2026-06-03]` — matriz muda rapido.

| Ferramenta | Le `AGENTS.md` nativo? | Canal proprio / legado | Extras |
|---|---|---|---|
| **OpenAI Codex** (CLI+cloud) | Sim | — | MCP, cloud agents |
| **GitHub Copilot** | Sim | `.github/copilot-instructions.md` (+ por path) | MCP, Skills |
| **Cursor** | Sim (2.2+) | `.cursor/rules/*.mdc` (`.cursorrules` legado) | MCP |
| **Gemini CLI** | Sim | `GEMINI.md` (legado) | MCP |
| **Windsurf / Zed / Aider** | Sim | rules proprias / `CONVENTIONS.md` | MCP |
| **Claude Code** | **Nao** (auto-carrega `CLAUDE.md`) | `CLAUDE.md` + memory dir | MCP, **Skills**, subagents, hooks |
| **Cline** | parcial | `memory-bank/` | MCP |

**Claude Code**: auto-carrega `CLAUDE.md`, NAO `AGENTS.md`; pra usar AGENTS.md
como canonical, importe com `@AGENTS.md` (ou symlink — Windows exige Dev
Mode/Admin).

### AGENTS.md — padrao estabelecido (nao mais "emergente")

`AGENTS.md` virou padrao **estabelecido**: em 2025 passou a ser governado pela
**Agentic AI Foundation** (Linux Foundation), com adesao nativa de Codex,
Copilot, Cursor, Gemini CLI, Aider, Windsurf, Zed. Refs:
[agents.md](https://agents.md/);
[Agentic AI Foundation](https://openai.com/index/agentic-ai-foundation/).
`[VERIFICAR: 2026-06-03]`. **Recomendacao**: `AGENTS.md` na raiz como
canonical, linkado de `CLAUDE.md` (`@AGENTS.md`)/copilot-instructions/cursor.

### Conteudo essencial do arquivo de IA

(1) Inventario "onde esta o que"; (2) Checklist "antes de agir" (`Glob`/`Grep`
antes de recriar); (3) Convencoes; (4) Lista NUNCA; (5) Foco atual + ponteiro
pro checkpoint. **Tamanho-alvo** ~100-200 linhas, mas a metrica real e'
**curadoria** (ver context engineering abaixo): consulta sob demanda fica no
`MAP.md`, roteada — nao inlinada.

### MCP — Model Context Protocol `[2026-06-03]`

Padrao de conectividade agente↔dados de 2026
([modelcontextprotocol.io](https://modelcontextprotocol.io/)). **Aplica aqui**:
expor `tickets/`, `manifest.jsonl` ou dataset como **MCP server local** em vez
de scripts ad-hoc — o mesmo server serve qualquer ferramenta MCP-aware.

| Opcao | Quando |
|---|---|
| Script (`scripts/index.py`) | leitura local simples, 1 ferramenta |
| **MCP server local** | varios agentes/ferramentas; quer schema/contrato; quer acoes |
| Tool bridge (export) | destino e' ferramenta corp externa (§11) |

**Seguranca (NUNCA)**: MCP server com escrita/acao = superficie de ataque;
menor privilegio; side-effect externo exige aprovacao explicita.

### Agent Skills (SKILL.md) `[2026-06-03]`

Skills empacotam uma capacidade reutilizavel (instrucoes + scripts + recursos)
num `SKILL.md` com *progressive disclosure*; spec aberta, cross-tool
([code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)).
Operacoes repetiveis desta metodologia que viram skills: promocao
exploratorio→frozen ("welding"); recipe de auditoria (§14); export de tool
bridge (§11); geracao de `INDEX.md`; assessment brownfield (§17.2). **Skill** =
procedimento que o agente executa; **MCP** = recurso/dado/acao que acessa;
**script** = automacao local. Combinam.

### Context engineering + prompt caching `[2026-06-03]`

Em 2026 **mais contexto nao e' melhor** — ~65% das falhas de agentes em
producao sao degradacao de contexto. Implicacoes: **rotear, nao inlinar** (o
`MAP.md` "quero X → va Y" e' context engineering); **curar > encher**;
**prompt caching — ordem importa**: conteudo estavel (`AGENTS.md`, >=~1024
tokens) primeiro = prefixo cacheavel; conteudo volatil (`STATUS.md`, lembrete
do dia) **depois** do estavel, senao invalida o cache.

### Subagents / fan-out + agent evals `[2026-06-03]`

Orquestrador com ~N subagents paralelos corta trabalho multi-fonte ~50-70%.
Fan-outs naturais aqui: **auditoria periodica** (§14) e **assessment
brownfield** (§17.2) — 1 subagent por pilar/pasta. Caveat: subagents retornam
**sumarios estruturados**, nao despejam contexto. **Evals**: `AGENTS.md`/
Skills/hooks sao prompts que regridem em silencio — eval minimo em CI (ex:
assert que o agente roda `Glob` antes de propor recriar).

### Busca: grep-first vs RAG `[2026-06-03]`

Top agentes de 2026 descobrem conteudo via **grep / arvore / busca
estruturada**, NAO vector DB (Claude Code abandonou RAG vetorial). **Default**:
busca agentica (`Glob`/`Grep`). **Busca semantica** (SQLite **FTS5** +
**sqlite-vec**, local-first) so' pra busca conceitual cross-doc em corpus
grande. **Nao** construa indice vetorial por reflexo.

### Hooks de ciclo de vida + observabilidade

Hook SessionStart e' **opcional** (CLAUDE.md ja' auto-carrega); vale pra primer
curto garantido / lembretes ephemerais. Em 2026 hooks existem cross-tool.
**Custo**: editar `.claude/settings.json` e' "self-modification" — requer
aprovacao explicita; em modo auto a IA nao escreve o hook sozinha.

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "hooks": {
    "SessionStart": [{ "matcher": "", "hooks": [{
      "type": "command",
      "command": "pwsh -NoProfile -Command \"if (Test-Path '.claude/session-start-context.md') { Get-Content '.claude/session-start-context.md' -Raw }\""
    }]}]
  }
}
```
> **Use `pwsh` (PowerShell 7+), nao bare `powershell`** no Windows: 5.1
> corrompe acentos (saida nao-UTF-8); `pwsh` le/escreve UTF-8.

**Observabilidade (opcional)**: OpenTelemetry GenAI — traces por
`conversation-id`, spans, tokens/custo/falha (complemento maquina do diario /
manifest). Adote se a escala justificar (§15).

### Proveniencia / autenticidade `[2026-06-03]`

Marcar autoria (`authored-by: ai | human | mixed`) e proveniencia vira
**obrigatorio em ago/2026** (EU AI Act Art. 50; CA SB 942; C2PA 2.x =
ISO/IEC 22144). Baseline ja' existente: `git_sha` + `manifest.jsonl`. Ver §10.

## 9. Disciplina de pesquisa — hierarquia de fontes (cross-cutting)

> Sempre que voce (ou IA) for afirmar X, decidir A vs B, citar, ou "lembrar"
> fato. **Problema**: humanos e IAs aceitam a primeira resposta plausivel —
> pior, a primeira que confirma crenca ja' havida.

### Frameworks canonicos

| Framework | Pra que serve | Origem |
|---|---|---|
| **Evidence hierarchy / pyramid** | hierarquizar forca de evidencia | EBM (Sackett 1996); GRADE |
| **CRAAP test** | avaliar fonte: Currency/Relevance/Authority/Accuracy/Purpose | Blakeslee 2004 |
| **SIFT method** | Stop / Investigate / Find / Trace | Caulfield 2017 |
| **Primary/Secondary/Tertiary** | dado bruto vs analise vs sumario | library science |
| **Triangulation** | validar via N fontes independentes | Denzin 1978 |
| **Chesterton's fence** | nao descartar o antigo sem entender por que existia | Chesterton 1929 |

### Sequencia sugerida

(1) fonte primaria autoritativa (paper peer-reviewed, spec, RFC, codigo
canonical); (2) secundaria consolidada (livro, survey); (3) doc oficial atual;
(4) comunidade curada (SO votado, issues fechadas); (5) blogs/threads (ultimo
recurso). Em dominios maduros comece em (1); em novos/efemeros, (3)-(4) podem
ser primarios.

### Recencia vs autoridade

**Recencia > autoridade** em cadencia rapida (software, ML, AI tools).
**Autoridade > recencia** em cadencia lenta (matematica, fisica, classicos de CS).

### Dados vivos vs consolidados — meia-vida e revalidacao

Espectro de perecibilidade (frequentemente DENTRO do mesmo item):

| Classe | Meia-vida | Exemplo | Acao da IA |
|---|---|---|---|
| Consolidado | anos | spec, teorema, dimensao fisica | citar 1x; verdade ate nova evidencia |
| Semi-vivo | meses | versao de lib, modelo a venda | `[VERIFICAR: data]`; revalidar se > 1-3 meses |
| Vivo | horas/dias | preco, estoque, noticia, cotacao | **nunca** de cache sem timestamp; revalidar na fonte; anexar `capturado_em` |

A ficha tecnica e' consolidada; o preco e' vivo — **nao trate igual** (Arbesman
2012). **A busca NAO e' neutra**: resultado e' ponteiro possivelmente velho;
pra dado vivo, abrir a fonte e ler o timestamp LA (`Last-Modified`), nao
confiar no snippet. **Antipattern critico**: "achei R$X" sem dizer QUANDO.

### Manual oficial vs internet

Feijao-com-arroz: manual da versao atual > opiniao de internet aleatoria.
**Excecao rara**: forum/blog as vezes excede a doc (bug nao-documentado, uso
avancado, padrao emergente). As duas sao validas — triangule ≥ 2 fontes; **o
usuario humano e' o juiz final** (IA traz ambas e pontua a divergencia, nao
decide unilateralmente). Marque `[VERIFICAR: YYYY-MM-DD]` ate confirmar.

### Marcacao de claims

`[VERIFICAR: YYYY-MM-DD]` (secundaria/recente nao confirmada) ·
`[fonte: forum; nao confirmado]` · `[hipotese pessoal]` (ou registry de
hipoteses, §3) · `authored-by: ai|human|mixed` (proveniencia — §10/§8).

### Para IAs

Voce **nao e' onipresente**: (1) distinga *sabe* vs *infere* vs *acha*; (2)
cadencia rapida → assuma desatualizado, ofereca WebFetch; (3) conflito interno
→ diga, nao escolha em silencio; (4) lacuna → diga e proponha caminho; (5)
premissa do usuario pode estar errada → pergunte "por que voce acha X?".
**Antipattern "soa certo"**: familiaridade nao e' verdade.

## 10. Revisao critica — dimensoes de avaliacao

> Gatilho pra IA/dev **questionar** o projeto, NAO checklist exaustivo. A
> metodologia organiza CONTEUDO; estas dimensoes questionam DECISOES.

| Dimensao | Pergunta-guia | Refs |
|---|---|---|
| **Proposito (JTBD)** | que dor real resolve? pra quem? | Christensen 2003; Ulwick |
| **Escopo vs tempo** | cabe no runway? onde cortar? | McConnell 2006 |
| **Seguranca** | auth/authz? secrets fora do codigo? threat model? | OWASP Top 10; NIST CSF 2.0; STRIDE |
| **Compliance / privacidade** | dados sensiveis? LGPD/GDPR? | LGPD; GDPR Art. 25 |
| **ROI / custo** | compute+storage+manutencao+tempo. cresce como? | AWS Well-Architected (Cost) |
| **Confiabilidade (SLO)** | que uptime basta? monitoramento? | Google SRE Book |
| **Performance / escala** | 10x cabe? otimizacao prematura vs debito? | Knuth 1974; Bondi 2000 |
| **Manutenibilidade** | bus factor? onboarding? tech debt? | Fowler 2018; SQALE |
| **Sustentabilidade** | energy/carbon? long-term ownership? | AWS Well-Architected (Sustainability) |
| **Acessibilidade (se UX)** | WCAG? screen reader? teclado-only? | WCAG 2.2 |
| **Sinal vs ruido de features** | cada feature serve quem? | YAGNI; Lean Startup |
| **Proveniencia / autenticidade** | conteudo IA marcado (`authored-by`)? proveniencia (`git_sha`/manifest; SLSA/Sigstore, RO-Crate, C2PA)? | C2PA 2.x (ISO/IEC 22144); EU AI Act Art. 50 |

**Como usar**: IA levanta a pergunta quando relevante; "nao pensamos nisso" e'
info util; nao-aplicar uma dimensao deve ser decisao consciente (ADR se
relevante). **E gatilho de discussao, nao certificacao.**

## 11. Tickets em markdown e tool bridges

### Tickets em markdown — FORTE

Alternativa local-first a Jira/Linear. **Por que markdown em git**: versiona,
offline, IA le, sem login, sem custo ("files over apps", Steph Ango).

Padroes (combine): Epic+Story (Scrum) · Kanban states (Anderson 2010) ·
Someday/Maybe (GTD) · Definition of Done · MoSCoW (DSDM) · Now/Next/Later ·
OKR (Doerr) · WSJF (SAFe).

```
tickets/
├── README.md           <- index dos tickets ativos
└── <ID>-<tema>.md      <- 1 arquivo por ticket
```
Frontmatter (status enum **canonical** da metodologia):
```yaml
status: open | in-progress | blocked | deferred | absorbed | closed | superseded
priority: P0 | P1 | P2 | P3        # opcional
created: YYYY-MM-DD
updated: YYYY-MM-DD
blocked-by: [TICKET-XYZ]           # opcional, gera grafo
```
Conteudo: contexto → hipotese → plano → AC (KR-style mensuravel) → riscos →
conexoes → updates datados inline. **Praticas FORTE**: IDs com prefixo
taxonomico (`META-X`, `T-CODE-N`); linkar ticket→commit; status enum formal;
AC mensuravel ("RT 100%", nao "funciona").

### Tool bridges — canonical → ferramentas externas

> Canonical (markdown+git) = **fonte da verdade**; ferramenta corp = destino
> (export). Bridge **unidirecional** por default — bidirecional gera dual
> source of truth e drift.

**Bridge** = funcao `canonical → tool-specific format` que le artefatos
versionados, aplica mapeamento e emite CSV/JSON/API call. Nao modifica fonte;
saida nao entra em git canonical.

**Campos canonicos universais**: `id`, `title`, `status` (enum acima),
`priority`, `created`/`updated`, `assignee`, `description`,
`acceptance_criteria`, `blocked_by`/`blocks`, `tags`, `commits`, `parent`,
`effort`, `sprint`. Cada ferramenta tem nomes diferentes — bridge traduz (nao
re-tabular as 8 SaaS aqui; doc oficial de cada uma cobre melhor).

**Export**: **Bulk CSV** e' o padrao mais robusto (1 linha/ticket):
```csv
ID,Title,Status,Priority,Assignee,Description,Acceptance Criteria,Labels,Created,Updated,Parent
T-CODE-1,"Welding alg16 -> src/tcf",in-progress,P0,leonardo,"Mover online.py...","RT 100%; bytes identico",welding;canonical,2026-05-18,2026-05-19,META-NAMING
```
API direta so' quando CSV nao expressa (issue links) ou volume continuo (use
`jiracli`/`linear-cli`). Copy-paste manual ate ~3 cards/mes.

**Retroactive cards** (backfill): o trabalho ja' aconteceu — voce tem a
resposta (commits, EXPs). Card = formato pre-trabalho (pergunta+AC) ja'
preenchendo os campos de fechamento. **Sempre linke evidencia versionada**
(commit SHA, ADR, EXP) — sem isso, e' ficcao.

**Anti-patterns**: dual source of truth · sync continuo amador · card vazio ·
retroactive sem evidencia · CSV editado a mao (edite canonical, re-export) ·
bridge bidirecional fragil. **IA nao deve**: criar cards sem aprovacao
(side-effect externo); modificar canonical pra casar com Jira; inventar
campos/commits. Config em `.tool-bridges.yaml` (gitignored — IDs per-dev;
versione `.tool-bridges.example.yaml`).

## 12. Implementacao em fases

**Fase 1 — Anti-incidente** (1 sessao, 30-60 min): objetivo = parar a IA de
recriar o que existe. (1) `AGENTS.md`/`CLAUDE.md` com inventario+checklist; (2)
`MAP.md`; (3) hook SessionStart (opcional); (4) lista NUNCA.

**Fase 2 — Estrutural** (algumas sessoes): (5) `docs/adr/` + template MADR +
1-3 ADRs retroativos; (6) `docs/vocabulary.md`; (7) docs nos 4 quadrantes
Diataxis; (8) YAML frontmatter em READMEs ativos.

**Fase 3 — Curadoria** (continua): (9) "See also" cross-links; (10)
`scripts/index.py` auto-gerando `INDEX.md`; (11) recipe de auditoria; (12)
`[VERIFICAR: YYYY-MM-DD]` em claims mutaveis; (13) *(opcional, gated por §15)*
avaliar a camada de capacidades de IA (MCP/Skills/subagents/evals/context
engineering — §8).

## 13. Antipatterns gerais

| Antipattern | Antidoto |
|---|---|
| **Hidden knowledge** (IA propoe recriar o que existe) | checklist "antes de agir" no `CLAUDE.md` |
| **Single-source violation** (mesma info em 3 lugares) | ADR canonical; outros referenciam |
| **Documentation graveyard** | `MAP.md` + cross-links + INDEX |
| **Stale forever** (`TODO 2023` em 2026) | `[VERIFICAR: data]` + audit |
| **README sprawl** | "See also" obrigatorio |
| **Index hand-maintained** | auto-gerar via script |
| **AI memory abuse** (tudo virou memoria) | projeto-context vai pra arquivo versionado (§8) |
| **ADR como diario** (50 ADRs/mes) | ADR = decisao arquitetural, nao tarefa |
| **Tutorials e how-tos misturados** | Diataxis disciplina |

## 14. Auditoria periodica (recipe)

A cada 60-90 dias, ou quando notar drift: (1) re-gerar `INDEX.md`; (2) procurar
`[VERIFICAR:]` vencidos; (3) revisar ADRs (status/links); (4) spot-check 5
READMEs (See also? links?); (5) atualizar `vocabulary.md`; (6) hipoteses
`em-andamento` ha' tempo demais?; (7) arquivar checkpoints retomados; (8)
revisar memorias da IA + **re-verificar a camada de tooling de IA** (§8 — alta
cadencia: MCP/Skills/tool tables).

## 15. Quando NAO aplicar

| Nao vale (over-engineering) | Vale (compensa) |
|---|---|
| < 10 arquivos de doc | > 50 docs/READMEs |
| 1 pessoa, < 1 mes | > 3 meses |
| Throwaway / PoC | Colaboracao regular (humanos e/ou IA) |
| Tarefa unica sem evolucao | Volta perde 30+ min reconstruindo contexto |

Sintoma de over-engineering: mais tempo organizando do que trabalhando.

## 16. Limitacoes (pra nao virar dogma)

Curva de adocao (comece minimo, so' Fase 1) · single-source exige disciplina
(audit 60-90 dias) · YAML/ADR pode virar burocracia (4-6 campos; ADR = decisao
custosa-de-reverter) · Diataxis exige treino · **AI tooling vs literatura =
cadencias diferentes** (§8 isolado, re-verificado) · memoria IA + hooks tem
limites (doc versionada > memoria).

## 17. Como aplicar — projeto novo vs existente

> **Orientativo, nao prescritivo.** IA deve avaliar impacto antes de alterar.

### 17.1. Projeto novo (greenfield)

`git init` + arquivos-raiz (§TL;DR) → **Fase 1** → **Fases 2-3** incrementais.
Pilares 1-4 cobrem ~80%; complementares (§5) so' se justificar; versionamento
sempre.

### 17.2. Projeto existente (brownfield) — assessment ANTES de alterar

**Regra FORTE pra IA**: ao receber "aplique ao projeto X", **NUNCA comece
modificando**. Avalie + reporte, aguarde aprovacao por etapa.

**Sequencia**: (1) inventario (`Glob` em `src/`/`docs/`/`experiments/`;
procurar canonicos); (2) maturidade por pilar (0-4); (3) conflitos com
estrutura atual; (4) custo por gap:

| Custo | Mudanca | Tempo |
|---|---|---|
| Baixo | criar `CLAUDE.md`, `.gitignore`, `MAP.md` | < 1h |
| Medio | reorganizar `docs/` em Diataxis; `docs/adr/` + ADRs retroativos | < 1 dia |
| Alto | mover `experiments/`, refatorar `src/`, renomear pastas | semanas |

(5) reportar matriz (pilar / maturidade / gap / custo / beneficio /
recomendacao); (6) aguardar decisao por pilar/fase.

**Custos reais de retrofit**: retrofit > greenfield (×2-3); conhecimento
tacito pode se perder; resistencia humana; beneficio cumulativo; `git mv` (nao
delete+create) pra preservar history; convencoes locais vencem nomes deste
doc. **Nao migrar** se: deprecated / < 6 meses; pequeno demais; time resiste;
refactor em curso ja' reorganiza.

### 17.3. Protocolo de IA por tipo de pedido

| Usuario diz | IA faz |
|---|---|
| "Leia esta metodologia" | le + avalia aplicabilidade; reporta sumario; **NAO altera**; pergunta |
| "Aplique ao projeto" | assessment (17.2) → matriz → aguarda aprovacao → aplica incremental |
| "Reorganize estrutura" | **NAO comeca alterando**; mede impacto; sugere ordem baixo→alto; aguarda |
| "Adicione algo a metodologia" | verifica se ja' coberto; avalia integracao antes de editar |
| "Aplique so' Pilar X" | mini-assessment do pilar X; reporta; aplica se aprovado |

## Apendice A — caches e ambientes em pasta dedicada

> Dia zero, qualquer projeto que produza arquivos efemeros/regeneraveis (GCC
> object files, LaTeX `.aux`, Python `__pycache__`, Rust `target/`, Node
> `node_modules`, datasets PyTorch/HF, Docker layers, etc.).

**Cache** (sentido amplo) = artefato regeneravel + efemero + nao-pertinente ao
output + especifico de ambiente. **Regra**: nada efemero/regeneravel no working
tree versionado (e' o "Signal vs ruido" de §7 aplicado a caches — nao
re-derivado).

**3 niveis de separacao** (preferencia): (1) pasta dedicada fora do projeto
(`Z:\caches\<tool>\`, `~/.cache/<tool>/`); (2) pasta no projeto + `.gitignore`
(`node_modules/`, `.pytest_cache/`); (3) config do tool pra redirect (env vars).

**Cross-OS**: Linux `$XDG_CACHE_HOME` (`~/.cache/`); macOS `~/Library/Caches/`;
Windows `%LOCALAPPDATA%\<tool>\Cache\` ou drive dedicado.

**Env var de redirect por ecossistema** (doc oficial de cada tool detalha):

| Ecossistema | Env var / estrategia |
|---|---|
| Python / pip / uv | `PYTHONPYCACHEPREFIX`, `PIP_CACHE_DIR`, `UV_CACHE_DIR` |
| pytest / mypy / ruff / coverage | `cache_dir`, `MYPY_CACHE_DIR`, `RUFF_CACHE_DIR`, `COVERAGE_FILE` |
| LaTeX | `latexmk -outdir=build/` / `-auxdir=.aux/` |
| C/C++ | `CCACHE_DIR`; out-of-source `cmake -S . -B build/` |
| PyTorch / HuggingFace | `TORCH_HOME`, `HF_HOME` (datasets 100GB+ NUNCA no working tree) |
| Node / R / Rust / JVM | npm `cache`; `R_LIBS_USER`; `CARGO_TARGET_DIR`/`CARGO_HOME`; `GRADLE_USER_HOME` |
| Docker | `dockerd --data-root=` + `docker system prune` |

**.gitignore**: comece pelo template oficial
([github.com/github/gitignore](https://github.com/github/gitignore), 200+
ecossistemas) + custom no final. **Pre-commit**: hook que falha se detectar
cache nao-ignorado / segredo / arquivo > limite.

**Antipatterns**: cache/venv/build commitado · multiplos venvs por maquina
(um por projeto, nome canonico `.venv`) · cache global poluido · tool config
ignorado (redirect via env var) · `.gitignore` infla sem fim (sintoma de tool
plantando errado).

**Caso de uso real (Windows + Python)**, implementacao validada:
[`../../../../dev-environment/README.md`](../../../../dev-environment/README.md)
— setup global `Z:\bin\Initialize-ZPython.ps1`; por projeto
`Z:\bin\New-ZPythonProject.ps1`; caches em `Z:\caches\<tool>\`; venvs em
`Z:\venvs\<proj>\` com junction `.venv`; working tree do projeto fica limpo.

## Bibliografia

### Information Architecture & wayfinding
- Peter Morville & Louis Rosenfeld — *IA for the Web and Beyond* (4ª ed., O'Reilly, 2015)
- Peter Morville — *Ambient Findability* (O'Reilly, 2005)
- Donald Norman — *The Design of Everyday Things*

### Documentacao
- Daniele Procida — Diataxis: [diataxis.fr](https://diataxis.fr/)
- Michael Nygard — "Documenting Architecture Decisions" (2011)
- MADR — [adr.github.io/madr](https://adr.github.io/madr/)
- Joel Parker Henderson — [ADR collection](https://github.com/joelparkerhenderson/architecture-decision-record)

### Ciencia aberta / reprodutibilidade
- Marwick, Boettiger, Mullen — "Packaging Data Analytical Work Reproducibly" (*The American Statistician*, 2018)
- The Turing Way — [book.the-turing-way.org](https://book.the-turing-way.org/)
- FAIR4RS — Chue Hong et al., *Scientific Data* (2022)
- Patrick Mineault — *The Good Research Code Handbook* ([goodresearch.dev](https://goodresearch.dev/))
- Cookiecutter Data Science; Software/Data Carpentry ([carpentries.org](https://carpentries.org/))
- Wohlin et al. — *Experimentation in Software Engineering* (Springer, 2012) — threats to validity
- Sollaci & Pereira — IMRAD 50-year survey (*J Med Libr Assoc* 92(3), 2004)
- Chris Chambers — *The Seven Deadly Sins of Psychology* (2017) — pre-registration
- Day & Gastel — *How to Write and Publish a Scientific Paper* (8ª ed., 2016)
- Imre Lakatos — *The Methodology of Scientific Research Programmes* (1978)

### Engenharia de software / releases
- Conventional Commits 1.0; SemVer 2.0; Keep a Changelog; 12-Factor App
- Frederick Brooks — *The Mythical Man-Month* (1975) — "plan to throw one away"
- Claessen & Hughes — "QuickCheck" (ICFP 2000) — property-based testing
- Kent Beck — *Test-Driven Development: By Example* (2002)

### Codigo como documentacao / nao-duplicacao
- Hunt & Thomas — *The Pragmatic Programmer* (DRY)
- Parnas & Clements — "A Rational Design Process" (*IEEE TSE*, 1986)
- Parnas — "Software Aging" (ICSE, 1994)
- Knuth — "Literate Programming" (1984)
- Meyer — *OOSC* (Design by Contract); Adzic — *Specification by Example* (2011)
- Simon Brown — [C4 model](https://c4model.info/); Ousterhout — *A Philosophy of Software Design* (2018)
- Wen et al. — code-comment inconsistencies (ICPC 2019); Dhaouadi et al. — rationale reconstruction (arXiv:2209.00398, 2022)
- Metz — "The Wrong Abstraction"; Dodds — "AHA Programming"; Ulfers — "Tests versus specs"

### Versionamento e higiene
- Chacon & Straub — *Pro Git* ([git-scm.com/book](https://git-scm.com/book)); Tim Pope — commit messages
- Trunk Based Development; GitHub Flow; Driessen — Git Flow (2010)
- [pre-commit.com](https://pre-commit.com/); Git LFS; DVC; lakeFS; Quilt
- [github/gitignore](https://github.com/github/gitignore); detect-secrets

### Project management / agile
- Anderson — *Kanban* (2010); Doerr — *Measure What Matters* (OKRs, 2018)
- Benson & Barry — *Personal Kanban* (2011); DSDM — MoSCoW (1994)
- Steph Ango — ["File over app"](https://stephango.com/file-over-app)

### Conhecimento pessoal
- Vannevar Bush — "As We May Think" (1945) — memex
- David Allen — *Getting Things Done*; Luhmann/Ahrens — *How to Take Smart Notes* (2017)
- Tiago Forte — *Building a Second Brain* / PARA (2022); Andy Matuschak — Evergreen notes

### Avaliacao de fontes / disciplina de pesquisa
- Sackett et al. — EBM (*BMJ*, 1996); GRADE (Guyatt et al. 2008)
- Blakeslee — "The CRAAP Test" (2004); Caulfield — SIFT (2017)
- Denzin — *The Research Act* (1978); Arbesman — *The Half-Life of Facts* (2012)
- Chesterton — *The Thing* (1929) — Chesterton's fence

### AI tools / agentes (alta cadencia — re-verificar)
- [AGENTS.md](https://agents.md/) / [Agentic AI Foundation](https://openai.com/index/agentic-ai-foundation/)
- [Model Context Protocol](https://modelcontextprotocol.io/); [roadmap 2026](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/)
- [Agent Skills](https://code.claude.com/docs/en/skills); [memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
- [Claude Code memory+hooks](https://code.claude.com/docs/en/memory); Copilot / Cursor / Cline rules
- Context engineering (Anthropic cookbook); OpenTelemetry GenAI

### Proveniencia / autenticidade
- [C2PA](https://c2pa.org/) (2.x = ISO/IEC 22144); [Content Authenticity Initiative](https://contentauthenticity.org/)
- [SLSA](https://slsa.dev/); [Sigstore](https://www.sigstore.dev/); [RO-Crate](https://www.researchobject.github.io/ro-crate/) / [CodeMeta](https://codemeta.github.io/)

### Comunidade / citacao academica
- [Open Source Guides](https://opensource.guide/); [Citation File Format](https://citation-file-format.github.io/); [JOSS](https://joss.theoj.org/); [DataCite](https://datacite.org/); [Dublin Core](https://www.dublincore.org/)

### Tool bridges (trackers externos)
- Jira REST v3 / CSV import; Linear / Monday / Asana APIs; ADF; [jira-cli](https://github.com/ankitpokhrel/jira-cli)

---

> **Esta receita e' viva.** A camada de IA (§8) e' alta cadencia — re-verificar
> via WebFetch a cada auditoria. A pesquisa que a produziu vive em `../lab/`.
