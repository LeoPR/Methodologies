---
title: Lab work / experimentos (Pilar 4 aprofundado)
type: reference
status: active
created: 2026-05-20
updated: 2026-06-03
part-of: methodology-suite
audience: ai-primary, human-secondary
see-also: [00-core.methodology.md, doc-vs-code.methodology.md, versioning-git-hygiene.methodology.md, bibliography.methodology.md]
---

# Lab work / experimentos — Pilar 4 (Compendium + FAIR4RS)

> **Quando aplicar**: projeto e' pesquisa / tem experimentos. Lab work
> e' a parte que vira arqueologia primeiro (60-90 dias). Vale camada
> extra de detalhe. Resolve "esse resultado e' reprodutivel?".
>
> **Convencoes**: principios sao consolidados; nomes ("dirty/clean",
> "welding", "EXP-NNN") sao exemplos LOCAIS — renomeaveis. Os rotulos
> **FORTE** (vinculo direto a literatura) e **LOCAL** (exemplo
> renomeavel) sao definidos em [00-core](00-core.methodology.md).

**Refs**: Marwick/Boettiger/Mullen 2018 (Research Compendium); Chue
Hong et al. 2022 (FAIR4RS). Ver [bibliography](bibliography.methodology.md).

**Estrutura minima** — modo exploratorio (bagunca permitida) vs
modo frozen (imutavel apos fechado):

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

Promocao exploratorio → frozen: refator formal (nomes locais: TCF
usa "welding"; literatura usa "harden", "productionize", "promote").

## Os dois modos de lab work

Toda pesquisa computacional opera em **dois modos** distintos. A
literatura reconhece isso com nomes variados — escolha o seu:

| Modo | Exemplo TCF (LOCAL) | Scrum/Agile | Pragmatic Prog. | Mineault | Brooks 1975 |
|---|---|---|---|---|---|
| Exploratorio, descartavel | "dirty" | spike | tracer bullet | research code | "throwaway prototype" |
| Frozen, reproduzivel | "clean" | story / PBI | production code | research software | "production code" |

**Principio FORTE**: separar fisicamente (pastas diferentes), regras
diferentes pra cada. Misturar = "lixo arqueologico".

**Nomenclatura LOCAL** (use qualquer): `exploratory/`+`frozen/`,
`dirty/`+`clean/`, `prototypes/`+`experiments/`, `spike/`+`studies/`,
`wip/`+`archive/`.

## Modo exploratorio — regras

**Permissivo em**: bagunca, codigo duplicado, dead code, hipoteses mudando.

**Estrito em**:
- **README curto** identificando pergunta + hipotese inicial — FORTE
- **Datado** com prefixo `YYYY-MM-DD-` — FORTE (tradicao de lab
  notebook fisico desde sec XIX: Faraday, Edison, Bell Labs)
- **Sub-experimentos numerados** (`01-`, `02-`, ...) — FORTE
- **Vocabulario disciplinado** — FORTE (ver "Praticas universais")
- **Imutavel apos fechado** — FORTE (codigo nao se modifica; pra
  continuar, fork novo)

**Estrutura sugerida** (TCF como exemplo; nomes sao LOCAL):
```
experiments/lab/dirty/2026-05-17-tema-do-macro/
├── README.md              <- frontmatter + pergunta/hipotese
├── notas/                 <- diario continuo, observacoes
├── 01-sub-experimento/    <- numerado sequencial
├── 02-...
└── 03-...
```

## Modo frozen — regras

**Imutavel apos fechado** — FORTE. Re-run gera nova versao
(`EXP-NNN-v2`). Mesma logica de **artefato citavel** — paper, Zenodo
DOI, software release nao mudam apos publicacao.

**Estrutura sugerida** — cada experimento e' um *research compendium*
(Marwick, Boettiger, Mullen 2018):

| Arquivo / convencao | Padrao subjacente | Forca |
|---|---|---|
| `README.md` em formato IMRaD | IMRaD (Sollaci & Pereira 2004) | FORTE |
| `run.py` executavel-em-uma-linha | Research Compendium | FORTE |
| `config.json` / `params.yaml` | Config over code | FORTE |
| `manifest.jsonl` (1 linha/run) | MLflow / W&B / Sacred run log | FORTE |
| `outputs/` | Cookiecutter DS `data/processed/` | FORTE |
| `report.md` (discussao final) | IMRaD Discussion | FORTE |
| Nome `EXP-NNN-tema/` | identificador estavel + slug | LOCAL — renomeavel pra `study-`, `experiment-`, etc. |

## README de experimento — formato IMRaD — FORTE

**Ref**: Sollaci & Pereira 2004 (survey IMRaD 50 anos). Estrutura
canonica de paper cientifico, aplicavel a UM experimento:

```markdown
## Pergunta cientifica          # Introduction
## Hipotese                     # H1 explicita vs H0
## Metodo                       # Methods
  ### Datasets / Metrica
## Resultado                    # Results (factual)
## Discussao                    # Discussion (interpretacao)
## Limitacoes / Threats to validity   # Wohlin 2012
## Como rodar / reproduzir
## Conexoes / See also
```

Rotulos sao LOCAL; os **4 movimentos** (intro / metodo / resultado /
discussao) sao FORTE.

## Manifest.jsonl — log append-only de runs — FORTE

**Padrao**: cada execucao de `run.py` append 1 linha JSON com
timestamp, parametros, metricas, hashes. Inspirado em MLflow / W&B /
Sacred / syslog / NDJSON.

**Por que JSONL append-only**: versionavel em git (deltas pequenos);
parseavel linha-a-linha (`jq`, `pandas.read_json(lines=True)`); sem
schema migration (campos novos aparecem em runs novos).

**Campos sugeridos**:
```json
{
  "timestamp": "2026-05-20T...",
  "experiment_id": "EXP-007-...",
  "git_sha": "abcd1234",          // FORTE: identifica versao do codigo
  "data_sha": {"D1": "sha256:..."},   // FORTE quando dataset evolui
  "config_hash": "ef89...",       // FORTE quando config evolui
  "metrics": { ... },
  "outcome": "confirmed" | "refuted" | "partial" | "inconclusive"
                                  // FORTE: combate publication bias
}
```

**Anti-pattern**: manifest sem `git_sha` → runs identicos com
timestamps diferentes sao ambiguos (mesmo codigo? mudou e ratio
ficou identico por sorte?).

> **Nota 2026 (schema-as-contract)**: publicar um `manifest.schema.json`
> (JSON Schema) validado tanto pelo `run.py` quanto pelo `scripts/index.py`
> torna o manifest um contrato — e e' o formato esperado ao expor o log
> via MCP. Ver [ai-instrumentation](ai-instrumentation.methodology.md).

## Promocao exploratorio → frozen

**O que a literatura ensina**:
- "Plan to throw one away" — Brooks 1975, *The Mythical Man-Month*
- "Refactor spike output, not transplant" — XP / Kent Beck
- Notebook → module refactor — Jupyter Best Practices

**Sequencia sugerida** — FORTE:
1. Sub-experimento exploratorio fecha com hipotese **confirmada**
   ou **refutada** (decisao explicita, nao "deixar pra depois")
2. Codigo relevante e' **reescrito** (nao copiado) em frozen
3. README IMRaD redigido **do zero** (nao reciclado das notas)
4. `run.py` deve ser **executavel em uma linha** (`python run.py`)
5. `manifest.jsonl` registra runs reproduzindo o resultado prometido
6. Opcional: tag git (`exp-NNN`); DOI Zenodo se publicavel

**O nome dessa operacao e LOCAL**. TCF usa "welding". Literatura
usa "refactor", "harden", "productionize", "promote", "land in
master", "land in src/". Escolha a metafora que cabe no seu time.

## Praticas universais (independente de nomes)

5 praticas que **sempre se aplicam**. Refs inline em cada pratica; pratica em 1 linha.

#### a) Vocabulario disciplinado (banir superlativos) — FORTE

Refs: Strunk & White; Day & Gastel; APA / Nature / ACS style guides.

- **Evitar**: "incrivel", "muito melhor", "vencedor", "campeao",
  "descoberta", "surpreendente", superlativos absolutos sem cenario
- **Preferir**: "diferenca de N bytes em cenario X", "menor em A vs B",
  "comportamento observado", "consistente com hipotese"

#### b) Hipotese **antes** do experimento — FORTE

Pre-registration / Registered Reports (Chambers 2017). Cada
sub-experimento abre com `H1: [...]` antes de codar — mesmo informal.

#### c) Round-trip / invariant check como criterio de aceite — FORTE

Property-based testing (Claessen & Hughes 2000). Se ha' invariante
natural (`decode∘encode = id`, `parse∘print = id`), use como AC.

#### d) Threats to validity explicitos — FORTE

Wohlin et al. 2012. 4 ameacas a enderecar em 3-5 linhas por
experimento: **Internal** (causalidade?), **External** (generaliza?),
**Construct** (mediu o que pretendia?), **Conclusion** (estatistica OK?).

#### e) Datasets representativos vs sinteticos extremos — FORTE

Ecological validity (Brunswik 1956). Separe **dataset de design**
(realistico, guia evolucao) de **dataset de stress** (artificial,
dimensiona limites).

## Antipatterns especificos de lab work

| Antipattern | Sintoma | Antidoto |
|---|---|---|
| **Lab graveyard** | pastas datadas que ninguem lembra | `status: closed/archived` no frontmatter + audit periodico |
| **Hot-edit em frozen** | experimento "imutavel" foi alterado pos-fecho | regra "frozen = imutavel"; mudanca = nova versao |
| **Manifest sem git_sha** | runs identicos, qual codigo rodou? | sempre logar git SHA |
| **Notebook spaghetti em producao** | exp exploratorio virou dep de outro | promover oficialmente (refator) ou nao depender |
| **"Tudo deu certo"** | so positivos registrados | campo `outcome` explicito; preservar refutados |
| **Storytelling post-hoc** | hipotese se ajusta ao resultado | escrever H1 antes de rodar |
| **Vocabulario torcido** | "incrivel resultado!" em log | banlist em `vocabulary.md` |

## Padroes adicionais de lab work

Sub-padroes que complementam o modo exploratorio. Adote o que se aplica.
(Colapsado em tabela; cada linha aponta a tradicao/ref — detalhe na
fonte primaria via [bibliography](bibliography.methodology.md).)

| Padrao | Proposito (1 linha) | Path sugerido | Base / forca |
|---|---|---|---|
| **Diario datado** | Cronologia de decisoes em prosa; contexto humano (distinto do manifest, que loga runs maquinaveis) | `notas/diario/YYYY-MM-DD.md` | bound notebooks (Faraday/Edison/Bell Labs); daybook (Vanderburg) — FORTE |
| **Registry de hipoteses** | Tabela central rastreando hipoteses cross-experimento; status `aberta/em-exp/confirmada-empirica/confirmada-conceitual/refutada/refutada-parcial/adiada/absorvida` (empirica vs conceitual importa) | `docs/hipoteses.md` | research programmes (Lakatos 1978) — FORTE |
| **Narrativa / project logbook** | Prosa longa ligando experimentos num arco (nao duplica detalhe tecnico; narra o arco) | `notas/historia-do-projeto.md` | tech reports (DARPA/IBM); postmortem aplicado a sucesso (Google SRE) — FORTE |
| **Findings consolidados** | Achados de N experimentos sobre UM tema, apos fechamento de fase (diferente de `report.md` de 1 exp) | `docs/findings/F-NNN-tema.md` | systematic review / meta-analysis — FORTE |
| **Checkpoint** | "Save-state" antes de pausa 1+ semana: o que fazia + por que pausou + o que NAO mudar + como retomar. Critico pra cold-start com IA | `notas/checkpoints/YYYY-MM-DD-tema.md` | memex (Bush 1945); Tickler file (GTD) |
| **Design backlog / icebox** | Ideias fora de escopo, vale registrar. Catalogo (ideia+justificativa), NAO roadmap (sem prazo) | `notas/futuras-otimizacoes.md` ou `docs/theory/` | Lean icebox (Pivotal); product backlog (Scrum) — FORTE |
| **Testes categorizados** | Round-trip / Unit / Integration / Regression / Performance; organize por nome ou subdir | `tests/test_roundtrip_*.py` | Claessen&Hughes 2000; Beck; Cockburn; snapshot — FORTE |
| **Changelog por marco logico** | Alternativa a Keep a Changelog: marco logico (v0.5→v0.6) cross-linkado a historia (apropriado quando "release" nao e' o marco) | `CHANGELOG.md` | ambos validos |

## Onde lab work conecta com outros pilares

Experimento que confirma hipotese significativa → vira **ADR** (Pilar 3,
ver [00-core](00-core.methodology.md)); `MAP.md` / `STATUS.md` listam
experimentos ativos (Pilar 1); `CLAUDE.md`/`AGENTS.md` deve referenciar a
regra "frozen e' imutavel" pra IA respeitar (ver
[ai-instrumentation](ai-instrumentation.methodology.md)); hipoteses do
registry geram **tickets** (ver
[tickets-and-tool-bridges](tickets-and-tool-bridges.methodology.md)) quando
viram trabalho concreto.

## Referencias

Ver [bibliography](bibliography.methodology.md) → "Ciencia aberta /
reprodutibilidade".
