<!-- l10n: doc_id=eval-readme · lang=en · canonical -->
[Português](README.pt-BR.md) · **English**

# `eval/`: the PROOF laboratory (the "screwdriver")

Executable tools that **prove** whether a methodology works. They are **not** the
methodology nor the focus.

> **Principle (do not forget):** the tool is a **means, not an end**. The end is
> **proving that Strata / Comporta work across many environments**, not perfecting
> the screwdriver. Improve the harness only as far as it proves better; beyond that
> it is scope creep.

## The project's three territories

| Territory | Is | Role |
|---|---|---|
| `recipe/` | the **methodology** (Strata, Comporta) | the **end** |
| `lab/` | the laboratory of **ideas** | hypotheses + conclusions *about* the methodology |
| `eval/` | the **proof executables** (here) | the screwdriver, reusable across methodologies |

## Structure

- `strata/` holds Strata's proof: multi-model runner, scorers (the programs that grade
  outputs), fixtures (controlled toy projects), scenarios, `planos/`.
  See [`strata/README.en.md`](strata/README.en.md).
- `comporta/`: (future) Comporta's proof (e.g.: `detect_env` + environment scenarios).

## Classification rule (from `strata/RASTREAMENTO-E-MELHORIA.md`)

Every run is **one** category: `evidencia` (measures a product hypothesis) ·
`instrumento` (tests/fixes the harness) · `infra` (validates execution/isolation). The
raw outputs in `*/planos/` are **gitignored** (local data; real projects are private).

> Status: "project within the project", calibrating the tool until it answers
> correctly. Future hypothesis: it may become a separate **spinoff**.
