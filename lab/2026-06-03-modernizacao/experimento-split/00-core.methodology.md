---
title: Nucleo da metodologia (core)
type: reference
status: active
created: 2026-05-20
updated: 2026-06-03
part-of: methodology-suite
audience: ai-primary, human-secondary
see-also: [README.md, lab-work.methodology.md, versioning-git-hygiene.methodology.md, research-discipline.methodology.md, ai-instrumentation.methodology.md, doc-vs-code.methodology.md, tickets-and-tool-bridges.methodology.md, appendix-caches-environments.methodology.md, bibliography.methodology.md]
---

# Nucleo da metodologia (core)

> **Documento-tronco** da suite de metodologia para projetos academicos /
> pesquisa / software cientifico com co-existencia de codigo, experimentos,
> artigos e colaboracao com agentes de IA. Cross-project, portavel,
> agnostico de stack. Os docs focados (lab-work, versionamento, disciplina
> de pesquisa, instrumentacao IA, etc.) aprofundam cada camada; este define
> o esqueleto e as convencoes comuns.
>
> **Como navegar**: entre pelo [README](README.md) (indice + routing).
> Este core e' consulta sob demanda, nao leitura linear.

## Convencoes e principios cross-cutting

> Definidos **uma vez** aqui; todos os docs da suite referenciam este bloco.

### Principio editorial — aponta, nao re-explica

Esta suite **aponta direcoes e nomeia padroes canonicos** — nao re-explica
em detalhe o que a literatura citada ja' cobre. Pra detalhe operacional,
consulte a [bibliography](bibliography.methodology.md) diretamente. O valor
e' a **sintese e ordenacao** das fontes, nao a reescrita delas. **IAs lendo**:
use WebFetch / conhecimento previo pra expandir cada referencia sob demanda.

### FORTE vs LOCAL

Marcadores de bindingness usados em toda a suite:
- **FORTE** = vinculo direto a literatura; principio que se aplica
  independente de nomes (nao renomeavel).
- **LOCAL** = exemplo renomeavel — nomes de pasta, metaforas, IDs (ex:
  "dirty/clean", "welding", "EXP-NNN"). Convencoes locais do projeto vencem
  os nomes desta suite.

### Principios que aplicam SEMPRE

1. **Editorial**: este doc aponta; literatura detalha. WebFetch quando precisar de profundidade.
2. **Pesquisa**: nao invente. Categorize *sabe* vs *infere* vs *acha*. Diga quando nao sabe. (ver [research-discipline](research-discipline.methodology.md))
3. **Versionamento**: tudo entra no repo, exceto regeneravel ou nao-pertinente. (ver [versioning-git-hygiene](versioning-git-hygiene.methodology.md))
4. **Imutabilidade**: ADR aceito + EXP frozen = nunca mude; crie novo com `Supersedes`.
5. **Single-source**: ADR canonical; outros docs referenciam, nao duplicam.
6. **Verificacao antes de afirmar**: `Glob`/`Grep`/`Test-Path` antes de propor recriar.
7. **Codigo e' o documento do COMO**: prosa carrega so' o PORQUE (intencao, restricao, alternativa rejeitada); o checavel vira teste, nao frase. (ver [doc-vs-code](doc-vs-code.methodology.md))

### Assessment antes de alterar projeto existente — FORTE

Ao receber "aplique a metodologia ao projeto X", a IA **NUNCA comeca
modificando arquivos**: primeiro avalia + reporta impacto; aguarda aprovacao
por etapa. Detalhe na secao "Como aplicar — projeto novo vs existente" abaixo.

---

## 1. Por que este documento existe

Projetos academicos / pesquisa acumulam **3 tipos de artefato que conflitam** se misturados:

| Tipo | Exemplo | Cadencia | Audiencia |
|---|---|---|---|
| **Codigo de producao** | `src/`, biblioteca publicavel | estavel | dev futuro / usuario |
| **Experimentos** | `experiments/`, notebooks | descartavel, alta rotatividade | voce mesmo em 3 meses |
| **Conhecimento** | docs, ADRs, artigos, notas | semi-estavel | revisor, colaborador, IA |

**Sintomas de mistura**: IA propondo recriar coisas que existem;
decisoes refeitas; docs estaveis poluidos com WIP; reviewer perdido.

E' problema de **arquitetura de informacao**, com decadas de
literatura. Esta suite e' a **sintese operacional** dessa literatura.

## 2. Os 4 pilares (sintese)

Cada pilar resolve **um** problema. Combinados, cobrem o ciclo todo.

| # | Pilar | Resolve | Framework canonico | Pasta padrao |
|---|---|---|---|---|
| 1 | **Wayfinding** | "Onde esta X?" | Information Architecture (Morville) | raiz: `CLAUDE.md`/`AGENTS.md` + `MAP.md` + `STATUS.md` |
| 2 | **Docs estaveis** | "Como uso/entendo isso?" | Diataxis (Procida) | `docs/{tutorials,how-to,reference,explanation}/` |
| 3 | **Decisoes** | "Por que decidimos X?" | ADR/MADR (Nygard) | `docs/adr/NNNN-*.md` |
| 4 | **Lab/experimentos** | "Esse resultado e' reprodutivel?" | Research Compendium + FAIR4RS | `experiments/` ou `notebooks/` |

### Pilar 1 — Wayfinding (descoberta)

**Ref**: Morville — *Ambient Findability* (2005) + *Information
Architecture for the Web and Beyond* (2015). Tres componentes:
ontologia, taxonomia, information scent.

**Implementacao** — 3 arquivos na raiz com papeis distintos:
- `CLAUDE.md` / `AGENTS.md` → instrucoes operacionais pra IA (ver [ai-instrumentation](ai-instrumentation.methodology.md))
- `MAP.md` → mapa (arvore + tabela "quero X → va Y")
- `STATUS.md` → boletim do dia (foco atual, ultimo estado)

### Pilar 2 — Docs estaveis (Diataxis)

**Ref**: Procida — [diataxis.fr](https://diataxis.fr/).

4 quadrantes ortogonais, **toda doc cabe em exatamente um**:

| | Pratico (mao na massa) | Teorico (compreensao) |
|---|---|---|
| **Estudando** (aprender) | **Tutorial** | **Explanation** |
| **Trabalhando** (resolver) | **How-to** | **Reference** |

Pastas espelham: `docs/{tutorials, how-to, reference, explanation}/`.

### Pilar 3 — Decisoes (ADR)

**Ref**: Nygard 2011; MADR — [adr.github.io/madr](https://adr.github.io/madr/).

**Regras**:
- Arquivo: `NNNN-imperative-phrase.md` (ex: `0007-use-postgres-not-mongo.md`)
- **Imutavel apos `accepted`**. Mudanca = novo ADR com `Supersedes NNNN`.
- Template MADR: Context / Considered Options / Decision / Pros and Cons.

**Criar ADR quando**: decisao arquitetural (afeta multiplos
componentes / versoes futuras) **OU** muda comportamento publico
**OU** reverter custaria muito. **Nao criar** pra bug fix nem
refactor local.

### Pilar 4 — Lab/experimentos (Compendium + FAIR4RS)

Modo exploratorio (bagunca permitida) vs modo frozen (imutavel apos
fechado); cada experimento frozen e' um research compendium. **Detalhe
completo em [lab-work](lab-work.methodology.md)** — esta e' a parte que
vira arqueologia primeiro, entao tem doc proprio.

## 3. Pilares complementares (escolha o que se aplica)

Os 4 pilares cobrem ~80% dos casos. Estes complementos cobrem nichos
especificos. **Adote so' o que faz sentido pro seu projeto** (colapsado em
tabela; detalhe na fonte via [bibliography](bibliography.methodology.md)):

| Padrao | Quando aplicar | Ref |
|---|---|---|
| **Atomic notes + linking (Zettelkasten — Luhmann)** | muitas observacoes/insights soltos; cada nota = 1 ideia atomica, nome estavel, pasta plana, `[[links]]` | Ahrens 2017 |
| **PARA (Tiago Forte)** | organizar conhecimento pessoal alem do projeto (Projects/Areas/Resources/Archives) | Forte 2022 |
| **Cookiecutter DS / Mineault** | projeto ML/DS: `data/{raw,interim,processed}/`, `notebooks/`, `src/<pkg>/`, `models/`, `reports/` | [goodresearch.dev](https://goodresearch.dev/) |
| **Conventional Commits + SemVer + Keep a Changelog** | release publico / usuarios externos; commits convencionais → changelog automatico (`git-cliff`, `release-please`) | conventionalcommits.org / semver.org |
| **Citacao academica** | vira artigo / software publicavel: `CITATION.cff`, DOI Zenodo, JOSS | citation-file-format |
| **Comunidade / contribuicao** | aberto a colaboradores: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE`, templates `.github/` | opensource.guide |
| **Metadados estruturados (biblioteconomia)** | dataset publicavel: Dublin Core, DataCite, schema.org/Dataset; YAML frontmatter | datacite.org |
| **Tickets / planejamento em markdown** | unidades de trabalho discretas com acompanhamento | ver [tickets-and-tool-bridges](tickets-and-tool-bridges.methodology.md) |

## 4. Estrutura de pastas canonical (referencia)

Composicao dos pilares. Adapte: nem todo projeto precisa de todos.

```
projeto/
├── .git/                         <- versionamento (foundational; ver versioning-git-hygiene)
├── .gitignore                    <- contrato do que NAO versiona
├── .gitattributes                <- opcional: LFS, line endings, diff de binarios
├── README.md                     <- entry point humano
├── CLAUDE.md                     <- entry point IA (ver ai-instrumentation pra variantes)
├── MAP.md                        <- mapa 1-pagina
├── STATUS.md                     <- boletim atual
├── CHANGELOG.md                  <- se versionado publicamente
├── CITATION.cff                  <- se academico publicavel
├── LICENSE
├── pyproject.toml / package.json <- conforme stack
│
├── .claude/                      <- Claude Code: settings + hooks
│   ├── settings.json
│   └── session-start-context.md
├── .github/                      <- se GitHub: copilot-instructions, workflows, templates
│   └── copilot-instructions.md
├── .cursor/rules/                <- se Cursor (regras por glob)
│
├── src/<package>/                <- codigo canonico
├── tests/
├── scripts/                      <- ferramentas de suporte (nao e' o produto)
│   └── index.py                  <- auto-gera INDEX.md
│
├── tickets/                      <- se planejamento em markdown (ver tickets-and-tool-bridges)
│   ├── README.md                 <- index dos tickets ativos
│   └── <ID>-<tema>.md            <- 1 arquivo por ticket
│
├── docs/
│   ├── tutorials/                <- Diataxis: aprender fazendo
│   ├── how-to/                   <- Diataxis: receitas pra problemas
│   ├── reference/                <- Diataxis: especificacao API/formato
│   ├── explanation/              <- Diataxis: porque/conceitos
│   ├── adr/                      <- decisoes numeradas, imutaveis
│   ├── vocabulary.md             <- termos controlados (single source)
│   └── findings/                 <- resultados consolidados (se pesquisa)
│
├── experiments/                  <- se projeto e' pesquisa
│   ├── clean/EXP-NNN-*/          <- replicaveis
│   └── dirty/YYYY-MM-DD-*/       <- exploratorios
│
└── data/                         <- se aplicavel; ou link pra storage externo
    ├── raw/
    ├── interim/
    └── processed/
```

## 5. Implementacao em fases

### Fase 1 — Anti-incidente (1 sessao, 30-60 min)

Objetivo: parar a IA de propor recriar coisas que existem.

1. Criar `AGENTS.md` (preferido — ver [ai-instrumentation](ai-instrumentation.methodology.md)) ou `CLAUDE.md` com inventario + checklist
2. Criar `MAP.md` com tree comentado + tabela "quero X → va Y"
3. Configurar hook SessionStart (Claude Code) ou equivalente
4. Adicionar lista NUNCA ao arquivo de IA

**Resultado esperado**: reducao drastica de propostas absurdas da IA.

### Fase 2 — Estrutural (algumas sessoes)

5. Criar `docs/adr/` com README + template MADR + 1-3 ADRs retroativos
6. Criar `docs/vocabulary.md` com termos canonicos do projeto
7. Mover docs existentes pros 4 quadrantes Diataxis (renomeando se necessario)
8. Adicionar YAML frontmatter (`status`, `tags`, `created`, `updated`) em READMEs ativos

### Fase 3 — Curadoria (continua)

9. Adicionar "See also" cross-links em READMEs (information scent)
10. Implementar `scripts/index.py` auto-gerando `INDEX.md` lendo frontmatter (sem dep externa — parse manual basta)
11. Criar `docs/how-to/audit-memorias-e-documentacao.md` com recipe de auditoria (rodar a cada 60-90 dias)
12. Adotar `[VERIFICAR: YYYY-MM-DD]` em claims mutaveis
13. *(opcional, gated por §8 "Quando NAO aplicar")* Avaliar a **camada de capacidades de IA** — MCP / Skills / subagents / evals / context engineering — ver [ai-instrumentation](ai-instrumentation.methodology.md).

## 6. Antipatterns (evitar)

| Antipattern | Sintoma | Antidoto |
|---|---|---|
| **Hidden knowledge** | infra/tool existe, IA propoe recriar | checklist "antes de agir" no `CLAUDE.md` |
| **Single-source violation** | mesma info em 3 lugares, drift | ADR canonical; outros docs referenciam |
| **Documentation graveyard** | docs existem, ninguem acha | `MAP.md` + cross-links + INDEX |
| **Stale forever** | `TODO 2023` ainda la' em 2026 | `[VERIFICAR: data]` + audit |
| **README sprawl** | dir com README sem cross-link | "See also" obrigatorio em README ativo |
| **Index hand-maintained** | sempre desatualizado | auto-gerar via script |
| **AI memory abuse** | tudo virou memoria, indexavel zero | projeto-context vai pra arquivo versionado, nao memoria (ver [ai-instrumentation](ai-instrumentation.methodology.md)) |
| **ADR como diario** | 50 ADRs por mes | ADR = decisao **arquitetural**, nao tarefa |
| **Tutorials e how-tos misturados** | usuario tenta aprender com receita avancada | Diataxis disciplina |

## 7. Auditoria periodica (recipe)

A cada 60-90 dias, ou quando notar drift:

1. **Re-gerar `INDEX.md`** e revisar entradas sem frontmatter
2. **Procurar `[VERIFICAR:]`** vencidos — confirmar/atualizar/deletar
3. **Revisar ADRs** — status correto? links externos vivos?
4. **Spot-check 5 READMEs aleatorios** — tem `See also`? links funcionam?
5. **Atualizar `vocabulary.md`** — termos novos? deprecated ainda usados?
6. **Roadmap de hipoteses/pesquisa** — entradas `em-andamento` ha' tempo demais?
7. **Checkpoints antigos** — arquivar os ja' retomados
8. **Memorias da IA** — review pra entradas obsoletas ou conflitantes; **e a camada de tooling de IA** (alta cadencia: MCP/Skills/tool tables) — re-verificar (ver [ai-instrumentation](ai-instrumentation.methodology.md))

## 8. Quando NAO aplicar

Esta metodologia tem overhead nao-trivial. Vale **apenas** quando os
ganhos compensam.

| Nao vale (over-engineering) | Vale (compensa) |
|---|---|
| < 10 arquivos de doc | > 50 docs/READMEs |
| 1 pessoa, < 1 mes | > 3 meses de duracao |
| Throwaway / proof of concept | Colaboracao regular (humanos e/ou IA) |
| Tarefa unica sem evolucao | Volta perde 30+ min reconstruindo contexto |

Sintoma de over-engineering: mais tempo organizando do que trabalhando.

## 9. Limitacoes (pra nao virar dogma)

| Limitacao | Mitigacao |
|---|---|
| **Curva de adocao**: Fase 1 = 30-60 min; Fases 2-3 = semanas | Comece minimo (so' Fase 1) |
| **Single-source exige disciplina**: drift volta sem audit | Audit 60-90 dias (§7) |
| **YAML/ADR pode virar burocracia** | 4-6 campos no frontmatter; ADR = decisao reversivel-custosa, nao tarefa |
| **Diataxis exige treino**: tutorial vs how-to e' sutil | Ler [diataxis.fr](https://diataxis.fr/) antes de aplicar |
| **AI tooling vs padroes academicos — cadencias diferentes** | Conteudo estavel no core; camada de IA isolada em [ai-instrumentation](ai-instrumentation.methodology.md), re-verificada a cada audit |
| **Memoria IA + hooks tem limites** | Doc versionada > memoria; mantenha session-start-context curto (5-15 linhas) |

## 10. Caso de uso real — TCF

Metodologia sintetizada durante incidente em projeto TCF (2026-05-18)
— IA propos recriar dataset/scripts que ja' existiam. Causa raiz:
falta de wayfinding na raiz. Pos-Fase 1, problema cessou. 3 outros
projetos sob `Acadêmicos/` adotaram subconjuntos com resultados similares.

**Artefatos de referencia** em TCF (consultar como exemplo concreto,
nao copiar literalmente — adaptar): `CLAUDE.md`, `MAP.md`, `STATUS.md`,
`.claude/`, `docs/adr/`, `docs/vocabulary.md`,
`docs/how-to/audit-memorias-e-documentacao.md`, `scripts/index.py`,
`tickets/`, `experiments/lab/{clean,dirty}/`.

## 11. Como aplicar — projeto novo vs existente

Esta suite e' **orientativa**, nao prescritiva. **IA deve avaliar
impacto antes de alterar** estrutura existente. Dois cenarios:

### 11.1. Projeto novo (greenfield)

Greenfield = `git init` + arquivos-raiz (ver [README](README.md) →
TL;DR) -> **Fase 1** (anti-incidente) -> **Fases 2-3** incrementais.
Pilares 1-4 cobrem ~80%; complementares (§3) so' se justificar;
versionamento sempre.

### 11.2. Projeto existente (brownfield) — assessment ANTES de alterar

**Regra FORTE pra IA**: ao receber "aplique a metodologia ao projeto X",
**NUNCA comece modificando arquivos**. Primeiro avalie + reporte
impacto. Aguarde aprovacao por etapa.

#### Sequencia de assessment

1. **Inventario** — `Glob` em pastas (`src/`, `docs/`, `experiments/`,
   `tests/`, `.github/`, `.claude/`); procurar canonicos (`README.md`,
   `CLAUDE.md`, `AGENTS.md`, `STATUS.md`, `MAP.md`, `CHANGELOG.md`, ADRs).
2. **Maturidade por pilar** — escala 0-4 (0 ausente; 2 parcial; 4 completo).
3. **Conflitos com estrutura atual** — convencoes ja' estabelecidas
   que diferem desta metodologia; renomes custam (links, imports, git
   history, workflows do time).
4. **Custo de migracao por gap**:

| Custo | Tipo de mudanca | Tempo |
|---|---|---|
| **Baixo** | criar `CLAUDE.md`, `.gitignore`, `MAP.md` | < 1h |
| **Medio** | reorganizar `docs/` em Diataxis; criar `docs/adr/` + ADRs retroativos | < 1 dia |
| **Alto** | mover `experiments/`, refatorar `src/`, migrar tickets, renomear pastas | semanas |

5. **Reportar matriz** ao usuario. Exemplo de formato:

| Pilar | Maturidade atual | Gap | Custo migracao | Beneficio esperado | Recomendacao |
|---|---|---|---|---|---|
| 1 Wayfinding | 1/4 | falta CLAUDE.md, MAP.md | Baixo | Alto (IA para de errar) | Aplicar Fase 1 |
| 2 Diataxis | 3/4 | docs/explanation ausente | Baixo | Medio | Aplicar oportunisticamente |
| 3 ADR | 0/4 | inexistente | Medio | Alto (decisoes futuras) | Aplicar; ADRs retroativos so' pras 3 mais criticas |
| 4 Lab | 4/4 | OK | — | — | Nao mexer |

6. **Aguardar decisao** por pilar/fase. Nao modifica nada sem aprovacao explicita.

#### Avaliacao honesta — custos reais de retrofit

- **Retrofit > greenfield em custo** sempre. Estimativa otimista multiplique por 2-3.
- **Conhecimento tacito do time pode se perder** se reorganizacao quebra convencoes ergonomicas nao-documentadas.
- **Resistencia humana** — colaboradores acostumados resistem mesmo com beneficio objetivo. Mude no minimo viavel, prove valor, depois expanda.
- **Beneficio cumulativo, nao imediato** — IA parar de errar em Pilar 1 da retorno em dias; ADRs retroativos so' geram valor quando proxima decisao similar surgir.
- **Git history fica confuso** se renomeacoes em massa — use `git mv` e commits separados pra mudancas estruturais vs conteudo.
- **Custo de aprendizado da IA** — IA precisa re-internalizar o layout em sessoes futuras; primeiros dias podem ter regressoes.

#### Principios pra retrofit

- **Fase 1 primeiro** — custo baixo, valor imediato. Provar antes de continuar.
- **Nao reorganizar tudo de uma vez** — disrupcao vs ganho.
- **Preservar `git history`** — `git mv` em vez de delete+create; commits separados.
- **ADRs retroativos** documentam decisoes ja' tomadas; nao reabrem.
- **Convencoes locais vencem nomes deste doc** — se projeto ja' tem termo proprio, preserve (logica FORTE/LOCAL).

#### Quando NAO migrar projeto existente

- Deprecated ou < 6 meses ate' fechar
- Pequeno demais (over-engineering — ver §8)
- Time resiste fortemente; beneficio incerto
- Refactor em curso ja' vai reorganizar tudo

### 11.3. Protocolo de IA por tipo de pedido

| Usuario diz | IA faz |
|---|---|
| "Leia esta metodologia" | Le indice + pilares; avalia aplicabilidade ao projeto atual; reporta sumario (pilares cobertos, gaps); **NAO altera**; pergunta se aplica algo especifico |
| "Aplique ao projeto" / "Organize com esta metodologia" | Faz assessment (§11.2 passos 1-5); reporta matriz pilar/custo/beneficio; aguarda aprovacao; aplica incrementalmente |
| "Reorganize estrutura conforme metodologia" | **NAO comeca alterando**; mede impacto (custo + ruptura + risco); sugere ordem (baixo→alto); aguarda aprovacao por etapa |
| "Adicione algo a metodologia" | Verifica se ja' coberto; se sim, aponta o doc/secao; se nao, avalia integracao + qual doc da suite e' o home antes de editar |
| "Aplique so' Pilar X" | Faz mini-assessment so' do pilar X; reporta; aplica se aprovado |

## 12. Atualizacao desta suite

- A suite e' **canonical mas viva**. Atualizar quando:
  - Novo framework relevante consolidar (ex: substituto do Diataxis)
  - AI tooling tiver mudanca de paradigma (camada de alta cadencia — ver [ai-instrumentation](ai-instrumentation.methodology.md))
  - Aprender algo novo aplicando em projeto
- Mudancas significativas: aumentar `updated:` no frontmatter do doc afetado
  e registrar no commit message (ou `CHANGELOG.md` do mono-repo Acadêmicos, se existir).

## Referencias

Lista completa em [bibliography](bibliography.methodology.md).
