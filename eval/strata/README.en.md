---
title: 'eval/strata: Strata proof harness (LIVE pipeline)'
created: 2026-06-05
updated: 2026-08-02
status: 'active. Replaces the "H-B kit" doc (old lumen/matrix arc, refuted by AUDITORIA-2026-06-07 → _superseded/).'
---

<!-- l10n: doc_id=eval-strata-readme · lang=en · canonical -->
[Português](README.pt-BR.md) · **English**

# eval/strata: how Strata's evidence is produced

The **"screwdriver"** (a means, **not** the methodology). It gathers the runners, fixtures,
answer keys and verifiers that generate the lab's `RESULTADOS-*`. **The conclusions do NOT
live here**. The entry point is the honest usage opinion:
[`../../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md`](../../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md)
(+ the `ARQUITETURA-E-EVIDENCIAS.md` hub).

> ⚠️ **Fixtures = FABRICATED inert data, deliberately problematic** (they include
> intentionally unsafe instructions to test §6-bis). They are read **as text only** by a
> model (zero real execution). **Never run anything from `cenarios/` or
> `_superseded/fixtures/`: every fixture is inert data.** Real projects/digests are
> **private** and stay **gitignored** (`planos/`, `external-fixtures/`, `own-fixtures/`,
> `fixtures-real/`).

## Folder layout (2026-08-02)

Scripts live in purpose folders; **data stays at the root** (`planos/`, `cenarios/`,
`f4-manifests/`, `fixtures-*/`, `external-fixtures/`, `own-fixtures/`):

- `core/`: `hb_runner.py` (base) + `providers.py` (direct cloud; `.<prov>-key` keys at the root)
- `runners/`: `hb_f3/f4/f5/f6/genre/temporal/m0/staged/agent`, `probe_l1.py`
- `verify/`: `verify_f4.py` → `score_f3.py` → `verify_agent.py` + `calc_stats.py` (graph kept together)
- `judges/`: cross-vendor judges (`judge_f3/f4/s04/f4_ablation/openrouter`, `score_cmp_openrouter`)
- `aggregate/`: `aggregate_*` + `compare_judges*` · `gen/`: digests, charts, forms, `hash_fixture.py`
- `ops/`: `run_*.sh` (ready-made matrices) · `legacy/`: `hb_l2_*` (broken defaults, record)
- `tools/probes/`: auxiliary probes (structure untouched)

## The LIVE pipeline (runner → fixture → answer key → verifier → aggregator)

```
runners/hb_<phase>.py  --target cenarios/<fix>  --label <out>   →  planos/<out>/plano-*.md   (gitignored)
        |                  |                                        |
   call_ex (core/hb_runner)  inert fixture                  verify/verify_f4 · verify/score_f3 · judges/* → aggregate/*
                         answer key = <fix>-manifest.json  (OUTSIDE the fixture folder: read_target does not read it)
```

**Runners** (all use `hb_runner.read_target` + `call_ex`; output in `planos/<label>/`):

| Runner | Measures | Fixtures | Answer key / verifier |
|---|---|---|---|
| `runners/hb_f4.py` | M4 execution: fixes without destroying? (STRATA vs `--baseline`) | `cenarios/f4-{dup,trap,clean}` | `f4-manifests/*.json` + `verify/verify_f4.py` |
| `runners/hb_f3.py` | §6-bis refusal (fail-closed) | f3 scenarios | `verify/score_f3.py` + `judges/judge_f3.py` |
| `runners/hb_f5.py` | §6 source verification (`:online` = web) | `cenarios/f5-verif` | `f5-manifest.json` |
| `runners/hb_f6.py` | temporal: `--mode chrono\|naive\|audit\|vigor\|triagem` | `cenarios/f6-{tempo,longitudinal,ambiguo,ruidoso}` | `f6-*-manifest.json` (reading) |
| `runners/hb_genre.py` | genre-awareness (§9) | `external-fixtures/`, `own-fixtures/` | reading |
| `runners/hb_temporal.py` | temporal on the owner's project | `own-fixtures/` | reading |
| `runners/hb_m0.py` | M0 abstention | scenarios | reading |
| `core/hb_runner.py` | **base** (does not run alone): `call_ex`, `call_openrouter_ex` (`reasoning`/`:online`), `call_ollama_ex` (thinking+fallback), `read_target`; `--temp` flag (additive, default 0.3) **only on the F1/prime path** (`call`/`run_one`; phase runners use `call_ex`, still fixed at 0.3) | n/a | n/a |

**Verification / judges:** `verify/verify_f4.py` (mechanical + **GOLD-gate**; `--selftest`) ·
`verify/score_f3.py` (regex + `--selftest`) · `judges/judge_f3.py`/`judges/judge_f4.py`/`judges/judge_openrouter.py`
(cross-vendor judges) · `aggregate/aggregate_*.py` (consolidate per experiment). **Digests** of
projects: `gen/build_ext_digest.py` (third-party) / `gen/build_local_digest.py` (owner's) → write
to **gitignored** fixtures.

**How to report (norm: ADR-006):** accuracy × precision in **separate columns**, always
with **k/K**, and **map the distribution** (multi-seed/temp) instead of hunting for "the
right temperature"; `pass@k` (ceiling) ≠ `pass^k` (reliable). See
[`../../decisions/ADR-006-acuracia-precisao-mapear-distribuicao.md`](../../decisions/ADR-006-acuracia-precisao-mapear-distribuicao.md).

## Reproduce a result (e.g.: §5-fix, the solid case)
```bash
export OPENROUTER_API_KEY=$(tr -d ' \r\n' < eval/strata/.openrouter-key)   # key NEVER versioned
cd eval/strata
python verify/verify_f4.py --selftest                                     # GOLD-gate (must pass 100%)
python runners/hb_f4.py --models google/gemini-2.5-flash --target cenarios/f4-dup --label f4-dup-strata --runs 2
python runners/hb_f4.py --models google/gemini-2.5-flash --target cenarios/f4-dup --label f4-dup-base --runs 2 --baseline
python verify/verify_f4.py --indir planos/f4-dup-strata --fixture cenarios/f4-dup --manifest f4-manifests/f4-dup.json
```
The `ops/run_*.sh` scripts package ready-made matrices (cloud/local/eco). **Cost:** check the
balance first (`curl .../api/v1/credits`); on the order of cents to ~US$1 per small matrix.

> **K=2 here is a smoke demo.** Official measurements report **larger K + *flip-rate***
> (ADR-006); small K is a sample ceiling, not a stable measurement; that was the
> "gpt-4.1 K=2 not attestable" case from P8.

## Conventions
- **OpenRouter key:** only in `eval/strata/.openrouter-key` (**gitignored**); never commit/echo it.
- **Answer key OUTSIDE the fixture:** `read_target` reads `.md/.json/.py…` recursively;
  that is why the `*-manifest.json` files stay **outside** `cenarios/<fix>/` (otherwise
  they would leak the answer into the prompt).
- **Regenerable outputs** (`planos/`, dumps) are gitignored or by-products, not
  the evidence; the curated evidence lives in the lab's `RESULTADOS-*.md`.

## Old arc (refuted): `_superseded/`
The **lumen → matrix → limit-search** arc (2026-06-05/07) was **refuted by
AUDITORIA-2026-06-07** (the prompt leaked the P1..P7 taxonomy; neutralized fixture ≠
answer key; per-id scorers produced artifactual zeros). It is archived in
**`_superseded/`** with a tombstone. It was replaced by this pipeline (`hb_f3/f4/f5/f6` +
`verify_f4`/`judge_*`). Kept as a record (append-only), **do not use**.
