---
title: P1 — Classificação como candidata a princípio L0 (por que, teoria, literatura)
created: 2026-08-01
updated: 2026-08-01
status: FECHADA — §11 aprovado pelo dono e aplicado ao canônico (recipe/knowledge-architecture.md
  + espelho .en.md, 2026-08-01). Enumerações externas atualizadas (recipe/README, hub).
  REVISADA no 2º ciclo sob a régua axiomática — ver [`P1-revisao.md`](P1-revisao.md)
  (§11 enxugado: 2 regras novas + derivações declaradas). Este doc permanece como traço (§3).
---

# P1 — Classificação: o L0 sabe *que* separar, mas não *como* agrupar

## 1. Hipótese (declarada antes, §4)

> **H:** O núcleo L0 cobre separação (§1), achabilidade (§2), rastreio (§3),
> geração (§4/§7), fontes (§6), história (§8), economia (§9) e portador (§10) —
> mas **não cobre o ato de agrupar e rotular** (formar categorias). Se essa
> lacuna é real e se a teoria de classificação é **anterior à IA e atemporal**,
> então falta um princípio no L0 (candidato a §11). **Refutaria H:** mostrar que
> §1+§2 já implicam a teoria de agrupamento, ou que a teoria de classificação é
> datada/contestada a ponto de não passar no teste do L0 ("se a IA e o computador
> sumissem, continua verdadeiro?").

## 2. O argumento lógico (por quê)

O L0 é um sistema fechado de necessidades: separar (§1), encontrar (§2),
rastrear (§3), gerar (§4/§7), validar fontes (§6), versionar (§8), economizar
(§9), preservar (§10). Mas toda essa cadeia **pressupõe um esquema já formado**:

- §2 ("Onde está X?") prescreve ponto de entrada, mapa e sinais de trilha — mas
  o mapa é um **índice sobre um agrupamento prévio**. O *scent* (Pirolli & Card)
  só orienta se os rótulos foram bem formados; o problema anterior ao scent é o
  **rótulo e o eixo** que o geraram.
- §1 prescreve separação física por **um eixo** (cadência × audiência) sem dizer
  por que esse eixo, quando um eixo basta, e o que fazer quando um objeto não
  cabe em nenhuma categoria do eixo. Ou seja: §1 **usa** classificação sem
  **fundamentá-la**.

Logo há um degrau conceitual anterior a §1/§2 que o L0 não nomeia: **formar o
esquema** — decidir o eixo, dividir sem sobreposição, e saber quando um eixo só
não dá conta. É o que a biblioteconomia chama de *teoria da classificação*, e
ela existe, formalizada, desde antes do computador.

## 3. Evidência interna (o próprio repo como caso)

- **O repo dogfooda o eixo de §1** (`recipe/` produto, `lab/` exploração,
  `eval/` ferramenta) e o próprio dogfooding **estica a tipologia**: `eval/` não
  é produto (é meio), não é exploração (tem regras de estável) e não é
  conhecimento — a ADR-004 resolve organizacionalmente, mas o L0 não dá o
  conceito de onde a ferramenta cabe. Sintoma clássico de **esquema enumerativo
  rígido**: objeto novo não cabe nas classes listadas.
- A Parte II mapeia **Arquitetura da Informação** (Rosenfeld & Morville 1998)
  sob §2 — mas R&M é em grande parte um livro **sobre esquemas de organização e
  rotulação** (capítulos de *organization schemes* e *labeling*). O L0 cita a
  fonte e **não extrai o princípio** — o conhecimento está na bibliografia, não
  no núcleo.
- O AGENTS.md da oficina já pratica informalmente a regra candidata ("**Tres
  territorios por tipo de artefato**" = eixo declarado) — o que sugere que a
  necessidade é real no uso, só não está formalizada.

## 4. Literatura (web-verificada 2026-08-01)

A teoria de classificação é **mais antiga que a IA, o computador e o VSCode** —
passa no teste do L0:

- **Aristóteles (~séc. IV a.C.)** — *Categorias* e a regra da definição
  *per genus proximum et differentiam specificam*: uma classe se forma por
  gênero próximo + diferença específica. É a raiz da regra de divisão (dividir
  por um fundamento declarado). `[CANÔNICO]`
- **Dewey 1876** — *Decimal Classification*: esquema **enumerativo** (lista
  fechada de classes); domina a prática e mostra, pelo seu defeito conhecido
  (classe nova não cabe na enumeração), a tensão que a teoria posterior resolve.
  `[WEB ✓ 2026-08-01]`
- **Bliss 1929** — *The Organization of Knowledge and the System of the
  Sciences*: o consenso científico/educacional como critério de ordem das
  classes (o esquema como **hipótese sobre o domínio**). `[WEB ✓ 2026-08-01]`
- **Ranganathan 1933** — *Colon Classification* (Madras Library Association):
  o primeiro esquema **analítico-sintético facetado** — em vez de enumerar todos
  os assuntos, fornece facetas-padrão (PMEST: Personality, Matter, Energy,
  Space, Time) e regras de **síntese**. É a resposta canônica ao "quando um eixo
  não basta". `[WEB ✓ 2026-08-01]`
- **Ranganathan 1937** — *Prolegomena to Library Classification*: formaliza os
  **cânones da divisão** — entre eles o **Canon of Exhaustiveness** (a divisão
  deve cobrir todo o universo) e o **Canon of Exclusiveness** (uma entidade
  pertence a uma só classe do mesmo array) — mais os de sequência útil e
  consistente. É a formalização biblioteconômica da regra lógica de divisão.
  `[WEB ✓ 2026-08-01]` (cânones listados na ISKO/encyclopedia e no índice do
  Prolegomena)
- **Classification Research Group / Vickery 1960** — *Faceted Classification:
  A Guide to Construction and Use of Special Schemes* (Aslib): leva a faceta da
  biblioteca geral para **esquemas especiais por domínio** — o uso prático para
  projetos. `[CANÔNICO]`
- **Svenonius 2000** — *The Intellectual Foundation of Information
  Organization* (MIT Press): sistematiza a organização da informação como
  disciplina com princípios (incl. *literary warrant*: o vocabulário/eixo se
  justifica **pela literatura/corpus real**, não por a priori). `[WEB ✓
  2026-08-01]` (MIT Press, xviii+255 p., ISBN 0262194333)
- **Hjørland & Albrechtsen 1995** — "Toward a New Horizon in Information
  Science: Domain Analysis" (*JASIS* 46(6)): o esquema bom é **relativo ao
  domínio** — não existe taxonomia neutra; classificar é tomar posição
  epistêmica sobre o corpus. `[WEB ✓ 2026-08-01]`

## 5. Ameaças à validade (honestidade de resultado, §4)

- **Contra-argumento forte — classificação é situada, não universal.** Bowker &
  Star 1999 (*Sorting Things Out: Classification and Its Consequences*, MIT
  Press) mostram que todo esquema é parcial, político e **apega-se a casos**;
  esquemas universais falham ao encontrar o caso real. `[CANÔNICO]` **Resposta:**
  isso não derruba H — derruba a *ambição universalista*. O princípio L0
  resultante deve ser **procedural** ("declare o eixo; divida sem sobreposição;
  revise quando o caso não couber"), não **substancial** ("estas são as
  categorias certas"). Hjørland e o *literary warrant* de Svenonius apontam o
  mesmo: o eixo é hipótese de domínio — o que é compatível com §6 (honestidade
  epistêmica) e com a regra de três (§7).
- **"§1+§2 já implicam isso."** Não: §1 dá *um* eixo resolvido; §2 pressupõe o
  esquema. Nenhum dos dois diz como formar um eixo novo — que é o caso comum de
  quem adota o método num projeto novo (o público-alvo do produto).
- **Risco de inchar o L0.** Real (§9). A defesa é o tamanho: o princípio cabe em
  ~1 seção curta; a fundamentação é anterior à IA; e a necessidade apareceu no
  dogfooding sem ser procurada.

## 6. Posição (o que proponho, se o dono aprovar)

**H confirmada com escopo procedural.** Candidato a **§11 — Classificação:
formar o esquema antes de organizar**, em 4 regras atemporais:

1. **Eixo declarado** — todo agrupamento responde "por que característica estas
   classes?" (Aristóteles; regra da divisão).
2. **Divisão limpa** — no mesmo eixo, as classes são mutuamente exclusivas e,
   juntas, exaustivas (Ranganathan 1937: Exclusiveness + Exhaustiveness).
3. **Um eixo não basta → facetas** — sintetizar por facetas em vez de inflar a
   árvore enumerativa (Ranganathan 1933; Vickery 1960).
4. **O esquema é hipótese de domínio** — justificado pelo corpus real (literary
   warrant; Bliss; Hjørland), revisável quando o caso não couber (Bowker &
   Star); proporcional à vida do projeto (§9).

Nada disto depende de software: bibliotecários fazem há 2.400 anos
(Aristóteles → Dewey → Ranganathan → Svenonius).

## 7. Decisão

- [x] **Dono aprovou §11 (2026-08-01)** — aplicado ao canônico + espelho `.en.md`
  (ADR-008); enumerações "12 princípios" → 13 em `recipe/README.md` e no hub.
- [ ] L1: mapeamento "Para §11" (candidatos naturais: facetas/CRG; taxonomias de
  domínio; *controlled vocabulary*) — fica para a **Parte 5** (âncoras do L1).
