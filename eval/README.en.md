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
- `temporalidade/` holds the temporality capability battery: does a model order scenes by state
  dependency, notice a missing step, an intruder and a wrong timestamp, and leave unordered what
  the evidence does not order? The battery, runner, scorer, blind review and analysis are in the
  scripts' headers. It reuses `strata/core/`. The pre-registration is in
  `lab/2026-09-26-temporalidade/`.
- `comporta/`: (future) Comporta's proof (e.g.: `detect_env` + environment scenarios).

## Classification rule

Every run is **one** category: `evidencia` (measures a product hypothesis) ·
`instrumento` (tests/fixes the harness) · `infra` (validates execution/isolation). The
raw outputs in `*/planos/` are **gitignored** (local data; real projects are private).

> Status: "project within the project", calibrating the tool until it answers
> correctly. Future hypothesis: it may become a separate **spinoff**.
