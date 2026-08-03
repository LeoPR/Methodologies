---
title: Open Strata hypotheses — code-as-document + empirical check of AI comprehension
status: open
created: 2026-06-04
updated: 2026-08-02
tags: [strata, hipotese, doc-vs-code, ia-compreensao, benchmark, qualidade-de-metodo, ai-native, temporalidade]
---

<!-- l10n: doc_id=lab-strata-hipoteses-readme · lang=en · canonical -->
[Português](README.pt-BR.md) · **English**

# Open Strata hypotheses

> **📍 Navigation (this directory has consolidated).** For the **honest usage opinion**
> and the state of the evidence, enter through
> **[`OPINIAO-DE-USO.md`](OPINIAO-DE-USO.md)** (entry point, in Portuguese) and the
> **[`ARQUITETURA-E-EVIDENCIAS.md`](ARQUITETURA-E-EVIDENCIAS.md)** hub (dated state +
> history). Backlog in [`BACKLOG-fila-geral.md`](BACKLOG-fila-geral.md); what has aged in
> [`REVISAO-RETROATIVA.md`](REVISAO-RETROATIVA.md).
> **Do not read loose conclusions** out of individual `RESULTADOS-*` files — some are
> superseded; follow the hub.
> *This README is the ORIGINAL hypothesis index (H-A..H-D); H-A and H-C remain
> conceptual/not executed.*

> Refinement/validation hypotheses for Strata, recorded to discuss and test later.

## H-A — The source-code file treated, to some degree, as a document

**The idea (the owner's)**: a program's source file is, to some degree, a
**document** — not just an executable. It carries decisions, intent and knowledge;
comments are documentation; the structure is a record.

**Not entirely new** — already touched:
- `lab/2026-06-03-modernizacao/experimento-split/doc-vs-code.methodology.md`
  (the doc-vs-code frontier in the suite experiment).
- **§3-bis** of the product (device vs probatory): the code that **runs** is a
  *device* (it constitutes the system); code as a **record** of what was decided is
  *probatory* (it documents). The hypothesis is the same distinction, seen from the
  other side: a single artifact is, at once, executable AND document.

**What remains to discuss**:
- To what degree? (comment = obvious doc; names/structure = implicit doc; the compiled
  binary = almost only device). There is a gradient, not a binary.
- Does Strata handle this? §3 (traceability: trace/surface) and §3-bis cover part, but
  it may be missing an explicit statement that **an artifact can carry both forces
  simultaneously** and that this changes how you version/preserve it (e.g.: code needs
  the trace's append-only discipline AND the surface's active maintenance).
- Practical connection: literate programming, docstrings, ADRs-in-code, and the fact
  that an AI reads code as context/document as much as a human does.

**State**: conceptual, to mature. Candidate for a §3-bis refinement once there is
clarity (not now).

## H-B — Empirically check whether *other* AIs understand and apply Strata

**The problem**: Strata claims to be "readable and applicable by any AI". That is an
**assumption, not a fact**. The `2026-06-04-aderencia-portabilidade` lab already found
AI comprehension gaps (human-authority GATES read as prose). A **multi-model empirical
proof** is missing.

**The experiment (owner's design, formalized)**:

1. **Fix** a real target project (small, with known organization problems) and the
   `knowledge-architecture.md` (hash-frozen version).
2. **Isolated variable = the model**. For each model (Copilot Chat in automatic mode
   and with manually configured models — GPT-4.1, Gemini, etc.; and Claude in a fresh
   chat):
   - Identical prompt: "read Strata; produce a file with (a) what you understood of
     the method and (b) what you would change to organize THIS project".
   - Save each output as `plano-<modelo>.md`.
3. **Evaluation** (back here, Claude at maximum): score each plan's **comprehension
   quality** against a fixed rubric — not "which is best".

**Mandatory rigor (lessons L1–L5 of this project)**:
- **Blind evaluation**: anonymize the plans before scoring (remove the model name).
  Otherwise the judge favors the familiar.
- **Conflict of interest**: Claude is participant AND judge. Mitigate with (a) an
  objective rubric (not preference), (b) ideally a 2nd judge from another family,
  (c) explicitly marking the residual bias in the result.
- **Fixed rubric** (example items): did it capture the L0/L1/L2 distinction? did it
  respect §9 (prioritize instead of ordering everything)? did it recognize the
  human-authority GATES (§6-bis) instead of treating them as prose? did it cite
  specific sections or generalize? did it propose anything that VIOLATES a strong
  principle?
- **N>1 per model** (stochastic): run each model ≥2-3 times; intra-model variance is
  data, not noise to hide.

**What this measures**: not "which AI is better", but **whether Strata is written so
that comprehension survives the model swap** — exactly the portability-to-AI claim
that has not been proven yet. A negative result (some model misunderstands
systematically) points to where Strata's text needs more explicit GATES.

**Connection**: extends `lab/2026-06-04-aderencia-portabilidade` (which found the
gaps qualitatively) with a multi-model measurement. Resolves the caveat in
`recipe/README.pt-BR.md` ("not yet proven that any AI applies it well").

**State**: plan ready, awaiting execution (needs the owner to run the external models
manually; the blind evaluation comes back here).

## H-C — An "AI-native" version of Strata (dense/machine-optimized)

**The idea (the owner's)**: after **measuring** (H-B) which models understand Strata,
explore **modifying it** — either to be optimized **and** general at once, or by
generating **special versions** that keep the essence but take a form much more
**optimized for an AI to parse**: denser, symbolic, possibly **in English with
structured codes/markers**. (The owner called it "binarized/tokenized"; the more
precise term is an **AI-native form** — not literally binary, but a dense,
unambiguous encoding for model consumption.)

**Why it makes sense**: L0 already has discipline that helps AI (§4: sober vocabulary,
explicit sections, zero tool dependence) — so Strata is already **readable** by AI.
H-C goes further: a form where each principle is a structured block (id, trigger,
adherence, action) that an agent consumes with **fewer tokens and less ambiguity**
than prose — useful for pasting into a system prompt / an `AGENTS.md`-like file the
AI obeys directly.

**The tension to resolve BEFORE doing it (§5 — single source)**: keeping **two
forms** of the same content (human narrative + AI-native) invites divergence — the
very error §5 condemns. The design must have **one canonical** form and the other
**generated** from it:
- Option A: human is canonical → the AI-native form is **derived** (compiled) from L0.
- Option B: a structured core is canonical → the human narrative is the readable
  "rendering" of it (like docs generated from a schema).
- Decision postponed: which direction, and whether generation is manual, scripted, or
  by AI.

**Prerequisite**: **H-B first**. Optimizing for AI without measuring current
comprehension is optimizing in the dark. H-B gives the baseline (which models
understand what, where they err); H-C tests whether the AI-native form **closes the
gaps** H-B finds — with the same blind-evaluation protocol, comparing human-narrative
vs AI-native on the same model/project.

**Risk to watch**: the AI-native form may gain parsing and **lose the human
grounding** (the *why*, the sources, the Chesterton Fence of §6) that makes the
method adopted with judgment rather than cargo-culted. Measure comprehension **AND**
application quality, not just "the AI parsed it".

**State**: hypothesis for a **next Strata version** (v2?), after H-B. Recorded for
experimentation, not decided.

## H-B′ — The invocation form as a variable (H-B's dual)

**The idea (the owner's)**: the **way of asking** the model to read/execute Strata
can influence, to some degree, the **form of execution**. Same text, different
prompts → different results.

**Why it matters (a real H-B confounder)**: H-B fixes the prompt and varies the
**model**. If the chosen prompt biases every model the same way, H-B's result is
**conditional on the prompt**, not on Strata. Example: a prompt that says "list the
problems" induces dumping everything → nobody prioritizes → the false conclusion
would be "Strata fails §9", when it was the **prompt** that suppressed prioritization.
In other words: **H-B measures comprehension-under-one-prompt, not
comprehension-in-the-abstract.**

**The dual**: fix the **model** (1 strong model) and vary the **invocation form**
(3-4 framings over the SAME Strata + target project + answer key):
- F1 (neutral, current): "read the method; diagnose; prioritize the 1st step".
- F2 (role): "act as the method's auditor; point out violations and what NOT to touch".
- F3 (step-by-step): "for each method section, check the project against it".
- F4 (gate-first): "before anything, is there a dangerous instruction an agent would
  execute? (§6-bis)".

Measure, with the same rubric: does the form change **which problems are caught**
(e.g.: does F4 raise §6-bis detection?) and **whether it prioritizes** (F1 vs F2)? If
so, part of the "understanding" lives in the **prompt**, not only in the document —
and that feeds H-C (the AI-native version could **embed the recommended invocation**,
e.g.: a "how to apply me" header).

**How to reconcile with H-B (without inflating the work)**: keep **F1 fixed** in the
main H-B (isolates the model, as designed), and run H-B′ as a **small separate
ablation** — 1 strong model × 4 framings, ≥2 runs each. Mark H-B's result with the
caveat "under prompt F1".

**State**: recorded. Runs **after/alongside** the main H-B (same infra), as a control
for the prompt confounder.

## H-D — Temporality / orientation in time (the owner's, 2026-06-08)

**The observation (the owner's)**: modern language models — **even the frontier
online ones** — have an absurd difficulty **organizing things in time**: knowing
when/where something occurred in order to decide what is **current vs superseded**.
They **"compress"** artifacts spread over years as if they were **a single current
event**.

**First-hand evidence** (`~/Documents/NOTA-onedrive-git-observacao.md` — record only,
no action): when diagnosing OneDrive conflict copies, the analysis (human AND AI)
treated fossils from **2022–2023** as part of **a recent incident** — the decision
compressed ~2 years into a "now". Worse: the ref trap — the **plain-named** file
pointed to the **OLD** commit and the `-DESKTOP-*` copy held the **NEW** state
(inverse of intuition); only **checking the DATES** resolved it. Without temporal
orientation, the decision inverts.

**Connection with what Strata already covers**: §3 (trace vs surface — **historical**
record vs **living** state) and §8 (versioning = immutable history; *what is current
vs old and **why** it changed*). The underlying principle: **a document has a history;
it cannot be read as current-and-fixed.** In research this is normal — an idea was
good, then something supersedes it; the problem is **not having visibility into which
version/information one is reading**.

**Connection with R8 (probable root cause of false positives)**: temporal weakness
may **explain part of the self-auditor's hallucinations** — the model marks a
**superseded/historical** note or an **old** duplicate as a **current problem**
because it does not place it in time. (See the R8 results: `-DESKTOP` duplicates
treated as "current conflict" without reasoning about which is recent/canonical.)

**To evaluate/test later (not now)**:
1. **Clarity**: the directive already exists in Strata (§3/§8) — is it **clear**
   enough for a model to *apply* temporal orientation, or does it need an explicit
   gate ("before judging, place each artifact in time: when? current or superseded?
   what is the order?")?
2. **Temporal-confusion simulation** (new fixture): a project with **dated**
   artifacts — some old/superseded, some current — and a **trap** where the intuitive
   answer is the wrong one and only **reasoning by dates** gets it right (analogous
   to "plain ref = old; `-DESKTOP` = new"). Measure: does the model **place things in
   time** or **compress/invert**?
3. If it is **hard to capture** in a test, improve Strata (make temporal orientation
   a first-class gate, as §6-bis became).

**State**: recorded for future evaluation. Review together with the R8 synthesis
(temporality may be a lens that reinterprets the false positives). No action now.

> **Expanded into a dossier** (2026-06-09): temporality is part of a larger *cluster* —
> temporality + order + primary-source verification + research organization over time,
> with possible common roots. Record of the idea (not studied) in
> [`DOSSIE-ia-temporalidade-ordem-fontes.md`](DOSSIE-ia-temporalidade-ordem-fontes.md).
