# `eval/` — laboratório de PROVA (a "chave de fenda")

Ferramentas executáveis que **comprovam** se uma metodologia funciona. **Não** são a
metodologia nem o foco.

> **Princípio (não esquecer):** a ferramenta é **meio, não fim**. O fim é **provar que o
> Strata / Comporta funcionam em muitos ambientes** — não aperfeiçoar a chave de fenda.
> Melhore o harness só até onde ele comprova melhor; além disso é desvio.

## Os três territórios do projeto

| Território | É | Papel |
|---|---|---|
| `recipe/` | a **metodologia** (Strata, Comporta) | o **fim** |
| `lab/` | o laboratório de **ideias** | hipóteses + conclusões *sobre* a metodologia |
| `eval/` | os **executáveis de prova** (aqui) | a chave de fenda — reutilizável entre metodologias |

## Estrutura

- `strata/` — prova do Strata: runner multi-modelo, scorers, fixtures, cenários, `planos/`.
  Ver [`strata/README.md`](strata/README.md).
- `comporta/` — (futuro) prova do Comporta (ex.: `detect_env` + cenários de ambiente).

## Regra de classificação (de `strata/RASTREAMENTO-E-MELHORIA.md`)

Toda execução é **uma** categoria: `evidencia` (mede hipótese de produto) ·
`instrumento` (testa/corrige o harness) · `infra` (valida execução/isolamento). As
saídas brutas em `*/planos/` são **gitignored** (dados locais; projetos reais são privados).

> Status: "projeto no projeto" — calibrando a ferramenta até ela responder corretamente.
> Hipótese futura: pode virar um **spinoff** separado.
