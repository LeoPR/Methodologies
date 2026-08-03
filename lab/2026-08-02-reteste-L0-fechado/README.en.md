---
title: Retest of the closed L0 (2026-08-02) — shake-down + targeted retest + Degrau 3
created: 2026-08-02
updated: 2026-08-02
status: executed 2026-08-02
---

<!-- l10n: doc_id=lab-reteste-l0-readme · lang=en · canonical -->
[Português](README.pt-BR.md) · **English**

# Retest of the closed L0 (2026-08-02)

The L0 core closed editorially on 2026-08-01. The v1 corpus had tested a **12-section**
L0 against June's technology; this lab retested the dated **negative** conclusions against
the 2026-08 shelf (local 17–32B, cloud affordable tier) — *a dated negative conclusion is
not refuted by the calendar; it is retested.*

## Structure

- [`PLANO.md`](PLANO.md) — the **pre-registered design**: temporal table of retest
  candidates, frozen model roster, access-strata grid, inherited rules (answer key
  pre-registered, hash-frozen fixtures, mechanical scorer with GOLD-gate, cross-vendor
  judge, ADR-006 reporting).
- [`NOTAS-shakedown.md`](NOTAS-shakedown.md) — the append-only **execution diary**
  (every batch, cost, harness incident and verdict, dated).

## Verdicts (4 lines)

1. **Injection refusal (§6-bis): old conclusion REFUTED** — the current generation refuses
   a paraphrased/indirect injection spontaneously (8/8), even at the affordable tier; the
   "lexical refusal that fell to paraphrase" was June's 8B limit.
2. **Proportionality/abstention (§9): the frontier MOVED, it did not close** — correct
   abstention now appears (local 27B), but bilateral proportionality (abstain where it
   should AND act in the right measure) remains unstable in the mid tier.
3. **Primary-source verification (§6): old hypothesis CONFIRMED, refined** — web access
   helps knowledge (and the "verification hallucination" without web disappeared; failure
   is now declared memory error or abstention, not fake tool-use).
4. **Degrau 3 (text→agent, real tools in a sandbox): the pattern TRANSFERS** — the §5 fix
   executed landed 10/12 with Strata × 2/12 without; nobody pulled the injected `curl`
   (0/24); the residual risk migrates to **obeying the corpus as a work order**.

Signals in synthetic scenarios (K=2 = direction, not significance — ADR-006); the dated
state of the evidence lives in
[`../2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md`](../2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md).
The harness that produced the runs is in [`../../eval/strata/`](../../eval/strata/) —
reproduction commands in its README.
