---
title: ADR-004 — Separar o laboratório de PROVA (eval/) do produto e das ideias
status: aceito
date: 2026-06-07
scope: estrutura do projeto (oficina), não conteúdo de uma metodologia
---

# ADR-004 — `eval/` separado: a ferramenta de prova não é a metodologia

## Contexto

Uma hipótese focada (H-B: *"uma IA consegue ler e aplicar o Strata?"*) cresceu até
virar um **harness de benchmarking** (runners, scorers, fixtures, cenários, dezenas de
execuções), misturado dentro de `lab/`. Isso feria:
- o alinhamento original do dono — *"os experimentos são alheios ao projeto"* e *"a
  missão não é criar métricas e enfiar tudo no arquivo da metodologia"*;
- o próprio **Strata** — §1 (três tipos de artefato: confundir apodrece) e §5 (fonte única).

Sintoma concreto da mistura: um fixture **deliberadamente inseguro** (instrução
*fail-open* mandando um agente baixar-e-rodar de URL) vivia como arquivo "real" num
repo público e precisou ser **neutralizado** — quebrando o gabarito no caminho.

## Decisão

Três territórios por **tipo de artefato**:

| Território | É | Papel |
|---|---|---|
| `recipe/` | a **metodologia** (Strata, Comporta) | o **fim** |
| `lab/` | o laboratório de **ideias** | hipóteses + conclusões *sobre* a metodologia |
| `eval/` | os **executáveis de prova** | a *chave de fenda* — meio; reutilizável entre metodologias |

**Princípio operacional:** a ferramenta é **meio, não fim**. Melhorá-la só até onde ela
**comprova melhor**; além disso é desvio. O fim é **provar que a metodologia funciona em
muitos ambientes**.

## Consequências

- `lab/.../hb-kit/` → `eval/strata/` (runner, scorers, fixtures, cenários).
- Variantes AI-nativas (AN) → `lab/.../strata-ai-native/`; `RESULTADOS-*.md` → `lab/.../`
  (conclusões = ideias, não ferramenta).
- `eval/*/planos/` (saídas brutas) **gitignored**; avaliações de projetos reais são privadas.
- **Comporta** seguirá o mesmo: o **manual** (instruções de montar o ambiente) = `recipe/`
  (metodologia); a **ferramenta** (ex.: `detect_env`) = `eval/` (prova + auxílio), **não**
  o manual. Linha cinzenta reconhecida e resolvida assim.
- A ferramenta pode virar um **spinoff** separado no futuro (hipótese aberta).

## Pendências (ajuste de núcleo, depois)

- Tornar os fixtures **inertes/seguros** sem entregar a resposta ao modelo testado.
- Reconciliar `projeto-alvo` (neutralizado) com `scenario_manifest.json` (que ainda
  espera P1–P7) — ou restaurar de forma segura, ou migrar de vez para `cenarios/`.

## Alternativas consideradas

- **Repositório separado** (`strata-eval`): separação máxima, mas custo de 2 repos e da
  ponte entre eles — adiado (pode virar o spinoff).
- **Arrumar dentro de `lab/` sem mover**: mínima, mas mantém a mistura conceitual — rejeitado.
