---
name: auditoria-consolidacao-narrativa
type: registro
status: etapa 1 (rastreabilidade) e etapa 2 (tom) executadas 2026-08-02
created: 2026-08-02
updated: 2026-08-03
audience: ai-primary
---

# AUDITORIA: Consolidação narrativa (2026-08-02)

Registro datado da auditoria narrativa do corpus, disparada depois que o
reteste do L0 fechado (lab `2026-08-02-reteste-L0-fechado/`) moveu o estado da
evidência e deixou docs de superfície para trás.

## A régua do dono (4 linhas)

1. Sem tom de diário nos docs publicados: diário vive nas NOTAS dos labs.
2. Toda afirmação segue hipótese → teste → conclusão, com rastreabilidade.
3. Impessoal, mas Plain Language (ver `ESTILO-REDACAO.md`).
4. Rastreabilidade primeiro, tom depois: conserta-se o fato antes do estilo.

## Achados

| Documento | Problema | Tipo | Sev | Correção |
|---|---|---|---|---|
| ARQUITETURA-E-EVIDENCIAS.md | hub se declara fonte canônica mas sem entrada 2026-08-02; F3/F5/agente datados (l33,39-41,113,158-159) | RASTREABILIDADE | alta | entrada datada + recalibrar linhas |
| recipe/documentacao-multilingue.md:123-126 | fila diz recipe/README e o-que-voce-ganha "sem par" (falso hoje) | RASTREABILIDADE | alta | atualizar tabela |
| FECHAMENTO-avaliacao-strata.md:l70+passo9 | gaps já fechados (completion-only, s04) como abertos | RASTREABILIDADE | alta | entrada datada 2026-08-02 |
| recipe/strata-com-ia.pt-BR.md | tabela de decisão + SVG no roster jun/2026 | RASTREABILIDADE | alta | grade 2026-08 |
| lab/2026-08-02-reteste-L0-fechado/PLANO.md | status "shake-down em curso", já executado | RASTREABILIDADE | média | status executado |
| MAP.md | árvore sem lab/2026-08-02-reteste-L0-fechado; trilha "prova" só ao hub | RASTREABILIDADE | média | adicionar + apontar OPINIAO |

## Plano em etapas

- **Etapa 1: RASTREABILIDADE (esta).** Corrigir os 6 achados acima; cada doc
  ganha o fato datado, apontando à fonte (ADR-005), sem duplicar número
  volátil. Estado da evidência 2026-08: fonte única é a
  [`OPINIAO-DE-USO`](../2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md) +
  [`NOTAS-shakedown`](../2026-08-02-reteste-L0-fechado/NOTAS-shakedown.md).
- **Etapa 2: TOM (pendente).** Refinamento de estilo nos pontos mapeados
  (ex.: "como a gente" no MAP.md), sem mover fato.

## Etapa 2: TOM + convenção de nomes (executada 2026-08-02)

**Convenção de nomes (dono, 2026-08-02):** o `README.md` da raiz é sempre EN +
`README.pt-BR.md`; nas demais pastas, o par se dá só por sufixo (`README.en.md`
canônico + `README.pt-BR.md` derivado). Executada em 5 pacotes:

- **WP1 (recipe/):** `recipe/README.md` → `recipe/README.pt-BR.md` (git mv); links
  vivos corrigidos (`README.pt-BR.md` raiz, `MAP.md`, `OPINIAO-DE-USO.md`, seletor
  l10n do `recipe/README.en.md`); tabela de `recipe/documentacao-multilingue.md` e
  inventário do `AGENTS.md` atualizados. Par `strata-recipe-readme` segue válido.
- **WP2 (pares EN/PT):** `eval/`, `eval/strata/`, `lab/2026-06-04-strata-hipoteses/`
  e `lab/2026-06-03-fundamentacao-L0/` renomeados para `README.pt-BR.md` + canônico
  `README.en.md` novo (tradução fiel; colofões l10n próprios). Par novo em
  `lab/2026-08-02-reteste-L0-fechado/` (superfície: PLANO = desenho pré-registrado,
  NOTAS = diário, vereditos em 4 linhas, ponteiro à OPINIAO). Reprodutibilidade no
  README do harness: pipeline (runner → fixture hash-congelada → gabarito
  pré-registrado → verificador mecânico GOLD-gate → juiz cross-vendor), comandos
  exatos de entrada e o que NÃO mora ali (conclusões → OPINIAO). Links do repo
  corrigidos (`AGENTS.md`, `eval/README*`, `ARQUITETURA-E-EVIDENCIAS.md`,
  `eval/strata/RASTREAMENTO-E-MELHORIA.md`).
- **WP3 (tom impessoal, só as frases mapeadas):** `STATUS.md` (P0: "o gabarito
  humano perdeu/estava incompleto; o modelo superou o gabarito"; fix "identificado
  em revisão humana"), `MAP.md` ("como a pesquisa foi feita"), `GLOSSARIO.md`
  (frontmatter mínimo; mede-se/usam-se/testado/repetido; linha datada Degrau 3),
  `ARQUITETURA-E-EVIDENCIAS.md` (4 frases: linhas 29, 72, 98, 303),
  `OPINIAO-DE-USO.md` ("contrato de ferramentas do laboratório"; âncora não é
  célula Claude-julga-Claude; "a Fase B deste corpus"), `REVISAO-RETROATIVA.md`
  (aperfeiçoada/mantém-se; `updated:` adicionado). Extras da reavaliação: raiz
  `README.md`/`README.pt-BR.md` ("casos medidos"). Snapshots históricos (labs
  datados, `RESULTADOS-*`) mantidos como registro, não reescritos.
- **WP4 (outreach):** `LINKEDIN-post.md`/`.pt-BR.md` ao estado 2026-08 (conserto §5
  e recusa saturam do econômico ao topo; piso local ~8B executa / ~20–27B satura;
  primeira célula agente em sandbox 10/12 × 2/12; evitar llama-4-scout; "sinais,
  não provas" mantido). `outreach/README*` sem claim datado: inalterado. SVGs
  verificados: conteúdo conceitual (camadas), sem roster, sem correção factual.
- **WP5 (reavaliação, esta seção):** varredura de primeira pessoa nas superfícies
  tocadas + relêitura contra a régua.

### Veredito da reavaliação

- **Impessoal:** ok nas superfícies publicadas. Restos conhecidos (registrados, não
  corrigidos por escopo): o hub `ARQUITETURA-E-EVIDENCIAS.md` ainda tem 1ª pessoa
  fora das 4 frases mapeadas (linhas ~82, ~88, ~111, ~120: "Como medimos", "nós
  gastamos"); o mapeamento mandou tocar só as 4.
- **Hipótese → teste → conclusão:** ok; as superfícies apontam a
  ADR/PLANO/NOTAS/OPINIAO para o detalhe; micro-detalhe de harness ficou em
  `eval/strata/README*` e nas NOTAS, não nas superfícies.
- **Reprodutível:** ok; comandos exatos de entrada e convenções no README do
  harness; lab de fundamentação diz como re-verificar (fonte primária citada).

### Pendências registradas

- Tradução EN de `recipe/strata-com-ia.pt-BR.md` (canônico pendente; já constava na fila
  de `documentacao-multilingue.md`).
- Hub `ARQUITETURA-E-EVIDENCIAS.md`: 1ª pessoa residual fora do mapeado (acima).
- PNGs de outreach: renderizar novamente se o texto dos SVGs mudar (não mudou).

### Registro: decisão anti-travessão (2026-08-02)

- **Decisão do dono:** eliminar o travessão (U+2014) dos textos publicados.
  Justificativa: preferência editorial; o sinal não tem função semântica que
  outro não cumpra, para leitor humano ou IA, e o excesso dele é marca
  conhecida de texto gerado por LLM.
- **Régua nova:** `ESTILO-REDACAO.md` (passo 6) agora proíbe o travessão.
  Apartes vão entre parênteses ou aspas; continuidade com ponto final,
  dois-pontos ou ponto-e-vírgula, o que ler melhor em Linguagem Simples.
- **Escopo aplicado:** raiz, `recipe/` (Strata bumpado para v1.2.1, só
  pontuação), READMEs de `eval/` e `eval/strata/`, `outreach/` e as
  superfícies vivas do `lab/`.
- **Exclusões por regra:** `decisions/` (ADRs imutáveis), pastas FROZEN
  (`experimento-split/`, `predecessor/`), fixtures/cenários/manifests de
  `eval/` (hash-congelados), `RESULTADOS-*`/`PLANO.md`/`NOTAS-shakedown.md`
  (registros datados), `_superseded/`, `recipe/_variants/`. Travessões em
  blocos de código (prompts prontos para copiar) foram preservados.
- **Complemento SVG (2026-08-02):** a primeira varredura cobriu `.md`; varredura
  corretiva cobriu os 8 SVGs publicados (outreach 2, recipe 2, VIZ-p6 4).
  Rótulos no padrão "·"; prosa com vírgula/dois-pontos/ponto-e-vírgula. XML
  validado. Os PNGs de outreach (`strata-linkedin*.png`) foram re-renderizados
  dos SVGs corrigidos com playwright+Chromium, tudo dentro do `.venv`
  (navegador em `.venv/pw-browsers`; fidelidade de browser, verificação visual
  feita; a tentativa svglib+rlPyCairo degradou fontes/resolução e foi revertida).
  Caminho registrado em `outreach/README*`; script `tools/render_svg_png.py`.

---

## Reorganização de eval/strata em subpastas por propósito (2026-08-02)

Os ~50 scripts soltos de `eval/strata/` foram reorganizados em subpastas por
propósito, com `git mv` (histórico preservado) e **sem quebrar o pipeline**:
`core/` (hb_runner + providers), `runners/` (hb_f3/f4/f5/f6/genre/temporal/m0/
staged/agent + probe_l1), `verify/` (verify_f4 → score_f3 → verify_agent +
calc_stats, grafo junto), `judges/` (juízes cross-vendor), `aggregate/`
(aggregate_* + compare_judges*), `gen/` (digests/charts/forms/blind/hash),
`ops/` (run_*.sh), `legacy/` (hb_l2_*, defaults já quebrados). **Dados ficaram
na raiz** (planos/, cenarios/, f4-manifests/, fixtures-*/, external-fixtures/,
own-fixtures/, manifests f5/f6, README/RUNBOOK/RASTREAMENTO/AUDITORIA);
`tools/probes/` intacto.

**Receita de shim aplicada:** (1) todo `.py` movido que computa o próprio HERE
subiu UM nível (`dirname(dirname(...))` / `parents[1]`); (2) imports internos
flat ganharam `sys.path.insert` antes do import — `core/` para runners e judges
(hb_runner/providers), `verify/` para aggregate_f4, mesma pasta dentro de
verify/; (3) `core/hb_runner.py`: STRATA subiu um nível (`../../../recipe/...`);
(4) `core/providers.py`: chaves `.<prov>-key` seguem na raiz (HERE ajustado);
(5) paths `../../lab/...` de aggregate/gen não tocados (corretos com o HERE
na raiz); (6) `ops/*.sh`: `cd "$(dirname "$0")/.."` + invocação
`python runners/hb_*.py` (antes era basename); (7) bug latente corrigido:
`tools/probes/price_probe.py` gravava em `tools/probes/planos/` (fora do
gitignore) — HERE subiu 2 níveis, grava em `eval/strata/planos/`.

**Gates pós-mover (todos 100%):** `verify/verify_f4.py --selftest` (GOLD=8, 0
erros) · `verify/verify_agent.py --selftest` (GOLD=10, 0 erros) ·
`verify/score_f3.py --selftest` (gold=86, 0 falso-neg/pos) · `calc_stats`
(selftest() True — o script não tem flag `--selftest`; o self-test roda sempre
no main() e foi invocado direto) · `runners/hb_f4.py --help` (import chain viva)
· `compileall` em core/runners/verify/judges/aggregate/gen/ops/legacy/tools sem
erros. Smoke extra: imports cruzados (hb_agent, aggregate_f4, judge_f3) com
HERE consistente.

**Docs vivos atualizados:** `eval/strata/README.pt-BR.md` + `README.en.md`
(nova seção "Layout das pastas", bloco de comandos com prefixos), RUNBOOK-nuvem,
`cenarios/README.md`, `RASTREAMENTO-E-MELHORIA.md` (hb_l2_* → legacy/),
`tools/probes/README.md`, `AGENTS.md` (inventário). Lab e ADRs não tocados
(registros citam caminhos antigos — ficam como histórico).

**Pendência:** nenhuma funcional. `_superseded/` segue congelado com os HEREs
da época (não roda mais por basename — registro, não usar).

## Etapa 3 (2026-08-02): superfície não cita erro antigo + sufixo pt-BR

Duas regras editoriais novas aplicadas às superfícies publicadas:

1. **Superfície não cita erro antigo.** Documento de superfície afirma o que é
   verdade hoje, direto; nunca escreve o correto e depois "(antes estava errado
   assim)". Quem lê desconhece o passado do texto e não deve adivinhá-lo; as
   formas erradas são infinitas e não se citam. A evolução vive no histórico do
   git. Varredura e correção em: `recipe/strata-com-ia.pt-BR.md` +
   `.en.md` (2 pontos), `recipe/README.pt-BR.md` + `README.en.md` (2 linhas de
   tabela), `recipe/o-que-voce-ganha.pt-BR.md` + `.en.md` (1 ponto),
   `recipe/strata-com-ia-fronteira.svg` (2 linhas; a linha da grade anterior
   virou "A evolução das medições fica no histórico do git."). Datação legítima
   de método (ex.: "roster auditado em fonte primária em 2026-08-02", bloco
   "Fonte e regime") permanece: datar o método não é citar erro.
2. **Sufixo de idioma em todo par não-README.** Só o README da raiz usa
   `README.md` (EN) + `README.pt-BR.md`. Nos demais pares o PT não fica sem
   sufixo: `X.en.md` (canônico) + `X.pt-BR.md`. Renomeados com `git mv`:
   `recipe/knowledge-architecture.md` → `.pt-BR.md`, `recipe/o-que-voce-ganha.md`
   → `.pt-BR.md`, `recipe/strata-com-ia.md` → `.pt-BR.md`. Referências
   atualizadas em todos os docs vivos (raiz, recipe/, eval/ código e RUNBOOK,
   READMEs e hubs do lab); registros datados e imutáveis (ADRs, RESULTADOS-*,
   FROZEN, planos/) ficaram com os caminhos da época, como histórico.
   `recipe/documentacao-multilingue.md` registra a convenção.

**Gates:** `check_stamps.py` ok · `check_l10n.py --working` ok ·
`verify/verify_f4.py --selftest` GOLD 100% (o harness passou a ler
`recipe/knowledge-architecture.pt-BR.md`, mesmo conteúdo PT de sempre).

## Etapa 4 (2026-08-02): siglas legíveis na primeira leitura

Regra editorial aplicada: todo código/sigla de superfície se resolve na primeira
leitura, seja abrindo no primeiro uso (modo fluido, preferido quando são poucas),
seja com uma chave de leitura no topo (quando a densidade é alta), seja com um
ponteiro explícito para o `GLOSSARIO.md`.

- **DOSSIÊs do lab** (densidade alta): `DOSSIE-judge-justificativa-cientifica.md`
  ganhou bloco "Como ler os códigos" (F0/F3/F4/R6, P1..P7, NNN, AN-v2/v3, GOLD) e
  abriu no primeiro uso: SEP, NLG, BLEU/ROUGE, GUM, ECE, RLHF, PoLL, κ de Cohen,
  MAE, IAA, pass@k/pass^k. `DOSSIE-ia-temporalidade-ordem-fontes.md` (densidade
  baixa): modo fluido (H-D, F5/F6, fase P4 abertos na frase).
- **GLOSSARIO.md** ganhou as entradas que faltavam: §N, framing/framing-dependente,
  FROZEN/SUPERSEDED, K, flip-rate.
- **Superfícies:** README raiz EN/PT (ADR, TDD, frontmatter, Krippendorff, fixtures),
  recipe/README EN/PT (§N, TDD, Krippendorff, fixtures, flip-rate em prosa),
  strata-com-ia EN/PT ("isso é L2" virou "camada datada, L2"; K=2 aberto; gold
  mecânico; ponteiro pro glossário), MAP.md e STATUS.md (ponteiro no topo; o
  histórico datado do STATUS fica coberto pelo aviso), knowledge-architecture
  EN/PT (EXP aberto, N=1 em prosa), eval/README EN/PT (scorers, fixtures).
- Registros datados de lab (`RESULTADOS-*`, histórico do STATUS) não foram
  reescritos: são histórico; o ponteiro para o glossário cobre o leitor.

**Gates:** `check_stamps.py` ok · `check_l10n.py --working` ok.

## Etapa 5 (2026-08-03): recipe enxuto + diagramas em par EN/PT

- **`recipe/_variants/` morava no território errado:** os braços âncora/placebo
  (ka-B, ka-C, v1.1.0) são material de experimento datado, não produto. Movidos
  para `lab/2026-06-04-strata-hipoteses/variantes-ka/` (eram gitignored e
  seguem; o README da pasta, tracked, explica a proveniência). BACKLOG
  atualizado (o item (b) da autoauditoria pedia esse movimento).
- **Diagramas em par EN/PT**, mesma convenção dos textos: `strata-modo.svg` →
  `strata-modo.pt-BR.svg` + `strata-modo.en.svg` (novo, canônico);
  `strata-com-ia-fronteira.svg` → `.pt-BR.svg` + `.en.svg` (novo). Cada
  documento aponta o diagrama do próprio idioma. Renders conferidos em PNG
  (Chromium do venv), sem overflow.
- **Bloco recipe do MAP.md reescrito** para o estado real (README pair,
  o-que-voce-ganha pair, sufixos .en/.pt-BR, variantes-ka no lab); README raiz
  EN/PT sincronizado (nome do arquivo pt-BR).
- Resultado: no GitHub, `recipe/` lista só produto e guias; o canônico
  (`knowledge-architecture.en.md`) é o 2º nome na listagem alfabética e o
  primeiro citado em README raiz, MAP e AGENTS.

**Gates:** `check_stamps.py` ok · `check_l10n.py --working` ok.

## Etapa 6 (2026-08-03): enumeração em lista, não inline

Regra de higiene de formatação: série de 3+ itens com conteúdo (vereditos, modos,
passos) vai em **lista**, não encadeada em parágrafo com "·" ("receita de bolo
inline"). Fundamentação: NN/g, *7 Tips for Presenting Bulleted Lists* (2017);
BC/Yukon, *Technical Writing Essentials* §3.3 (listas simplificam frases longas);
*Technical Communication Fundamentals* (3+ itens relacionados pedem lista).
Aplicado: GLOSSARIO.md (escada M0–M4 e vereditos F3/F4 viraram sub-bullets; a
escada também ficou global, executor = humano ou ferramenta, com a IA como caso
comentado) e MAP.md (inventário da pasta strata-hipoteses em duas linhas).
Varredura nas demais superfícies: sem outros casos em prosa.

**Gates:** `check_stamps.py` ok.
