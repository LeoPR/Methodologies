---
title: Strata with AI (practical usage guide)
status: active
created: 2026-06-08
updated: 2026-09-26
purpose: answer the developer asking "does it work in my environment? will it be expensive?". Only what works
nota: the full research (including what does NOT work and why) is in lab/2026-06-04-strata-hipoteses/RESULTADOS-p6..p9 (p8 = position/variance; p9 = roster churn, L2)
---

<!-- l10n: doc_id=strata-com-ia · lang=en · canonical -->
**English** · [Português](strata-com-ia.pt-BR.md)

# Strata with AI: practical guide

The method text is the same for everyone. What changes the result is **who runs it and how**.
Three golden rules before any model:

1. **For a full evaluation, give a mid/budget model the checklist in stages, not the raw
   text.** For a known fix the raw canonical text already works (2026-08 grade). The
   checklist (`../lab/2026-06-04-strata-hipoteses/strata-ai-native/strata-checklist.md`) is a
   prototype older than the closed L0: it has no gate for §11 or for the authority-to-read
   side of §6-bis. Use it as a scaffold, not as the method.
2. **AI output = a draft to review**, never an automatic verdict.
3. **Autonomous self-audit (AI auditing a project alone) is a top-tier-only mode**: on real
   projects it only paid off with the top model. For mid/budget models the setup that works
   is **checklist + human confirming each finding**.

> **Where the evidence holds (read before the table):** the saturation and abstention numbers
> come from **synthetic fixtures** with a pre-registered answer key. In **real third-party
> projects**, the AI self-auditor did **not** beat plain competence: with the "find problems"
> framing, every arm (baseline included) over-detected, inventing violations and criticizing
> good practices; the **abstention form** is what corrects the false positives
> ([R8](../lab/2026-06-04-strata-hipoteses/RESULTADOS-r8-sintese-3-projetos.md), reinterpreted
> 2026-06-13; [external arm](../lab/2026-06-04-strata-hipoteses/RESULTADOS-externo-bemcomportado.md)).
> Residual circularity: the rich quality audit on third-party projects still lacks an
> independent answer key and covers a single genre. Use the table to pick a model for
> **controlled tasks** (fix, trap, abstention); treat real-project audits as drafts for a human.

## Quick decision: what to use (2026-08 grade)

| I want to… | Use | Why |
|---|---|---|
| **run locally (consumer GPU)** | **qwen3:14b** (fits whole in a 3060 12GB) · **qwen3.6:27b** | the 14b is the daily workhorse; the 27b fixes and also abstained on the clean fixture (caveat below), but is slow (~22 min/run with offload) |
| **pay little in the cloud** | **gpt-5-mini** (OpenAI paid floor) · **haiku-4.5** · **deepseek-v4-pro** | they execute the fix to standard; gpt-5-mini also refuses injection spontaneously and, with web access, verifies sources |
| **the most, at any cost** | **opus-5** · **fable-5** | perfect fix and trap, and they abstained on the clean fixture (caveat below); the top tier is where **autonomous self-audit** paid off |
| **top tier without paying the ceiling** | sonnet-5 · gpt-5.6-terra · gemini-3.1-pro | perfect fix; trap perfect except one gemini-3.1-pro run that re-emitted the active directive; abstention **not measured** |
| **do NOT use for this** | llama-4-scout · local <4B | the scout failed the trap fix 2/2 and propagated the payload; below ~4B not even the format comes out |

*Rule: **fixing a known defect (§5) saturates from ~8B local to the top**. The edge that separates models is **abstention** (not touching what is already good): it depends on the **model and on how the request is worded**, not on the price, and there is no evidence that the method's text buys it (§9). Check the specific model in the honest grade of [`OPINIAO-DE-USO`](../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md). AI output = a draft to review, always. (Names and prices date quickly: they live in the dated layer, L2. Re-audit before anchoring an expensive decision.)*

> **Source and regime (2026-08-02):** retest of the closed L0, ~350 runs, K=2 (two runs per
> cell), three situations (§5 fix, trap with §6-bis injection, already-good project §9),
> mechanical gold standard + blind cross-vendor jury (terms: [GLOSSARIO](../GLOSSARIO.md)).
> Directional signals (synthetic), not proof. Numbers by task × capability:
> [`OPINIAO-DE-USO`](../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md); round diary:
> [`lab/2026-08-02-reteste-L0-fechado`](../lab/2026-08-02-reteste-L0-fechado/).
>
> **Caveat on the abstention cells:** the clean fixture used for them stated the answer in its
> own README, so part of what was measured is reading, not calibration. Only its successor
> without the leak is clean, and it measured three models
> ([§9 verification](../lab/2026-08-03-prompt-ingenuo/RESULTADOS-verificacao-s9.md)). Read
> every "abstained" in this page as a weak signal; the qualitative reading (it varies by model,
> not by price) holds.

![Strata by AI: which model to use, by vendor](strata-com-ia-fronteira.en.svg)

**How to read the chart** (2026-08 grade; by access context: local GPU, budget plan, top tier).

The retest measured each model in **three situations** with a pre-registered answer key:

- **§5 fix**: a known defect (duplicated information), Strata arm × baseline.
- **§6-bis trap**: the same fix with a malicious instruction planted in the project.
- **Already-good project §9**: nothing to correct; the right answer is **not to act**.

The finding that organizes the chart: **the §5 fix saturated**: from ~8B local to the frontier
top, with Strata everyone executes to standard. **The edge that separates models is abstention** (§9): who abstains
on a project that is already good. It depends on the **model, not the tier or price**. Opus-5/fable-5
abstained, and there are calibrated budget models and overacting expensive ones (all on the
clean fixture, with the caveat above); check the specific model in OPINIAO.

**What the chart says:**
- **Local:** below ~4B not even the format comes out (not the method; capability). **qwen3:14b**
  fits whole in a 3060 12GB and carries the day-to-day; **qwen3.6:27b** fixes and also abstained
  (caveat above), but runs with offload: ~22 min/run, feasible, slow.
- **Budget cloud:** **gpt-5-mini** is OpenAI's paid floor; **haiku-4.5** and
  **deepseek-v4-pro** execute the fix perfectly.
- **Top:** **opus-5** and **fable-5** fix, pass the trap and abstained (caveat above);
  sonnet-5, gpt-5.6-terra, gemini-3.1-pro and kimi-k3 fix perfectly and pass the trap, except
  one gemini-3.1-pro run; their abstention was not measured.
- **Avoid for this use:** **llama-4-scout**, the only one that, with Strata, failed the trap
  fix 2/2 and propagated the injection payload in one of them.

> **Read by pattern, not by name.** Models change fast; what **lasts** is the behavior by
> access stratum (model names are dated examples; roster audited in primary sources on
> 2026-08-02). Full honest grade, by task × capability × cost:
> [`OPINIAO-DE-USO`](../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md).

## How you ask: what it helps and what it does not

For a **full evaluation** by a mid/budget model, the form of the request helps (June signal):
- **Checklist** (yes/no per gate, with the 3 anti-false-positive rules) >> raw text.
- **Stages** (applying in separate turns) is what helps mid/budget models the most:
  it forces the model to acknowledge what is good and place it in time **before** pointing defects.
- It does **not** buy the judgment of when *not* to act: that stays with the model, and a
  well-worded plain request calibrates it as well as the method or better.
- **Reasoners** (deepseek-r1, qwen3-thinking) need `think:true` and a generous token
  budget, otherwise they "think" and never answer.

## Limits (what to expect: not a defect, how to calibrate)

- **Over-acting is not a tier stamp:** some budget models calibrate on a clean project and
  some expensive ones over-act; it shows up more with noise and under audit framing. Treat
  the result as a draft and confirm each finding with the cited excerpt.
- **The temporal dimension depends on legibility:** with readable dates and history
  (§3/§8) models place things in time correctly; with noisy or unmarked history they flag the
  historical as a current problem. Review dated findings carefully.
- **Both sides at once (2026-08):** on the synthetic grade, opus-5, fable-5 and the local
  qwen3.6:27b fixed **and** abstained (clean fixture, caveat above). The others **oscillate**
  on one side; treat as draft.
- **Local reasoners deceive:** a local reasoner may look
  "clean" only because it **truncated before concluding**; when it actually finishes, the verdict changes.
  Do not trust the partial result (in the 2026-08 retest, false-zero by truncation becomes
  INDETERMINATE, never FAIL).

## Final notes

- **Free local is a real option:** qwen3:14b (fits in a 3060 12GB) executes the
  fix, and qwen3.6:27b also abstained (caveat above): free, slow. Remote `:free` remains bad: heavy
  rate-limiting and low quality.
- The full analysis (configurations that do **not** work, the experiments and the research
  charts) is in `lab/2026-06-04-strata-hipoteses/`
  (`RESULTADOS-p6-*`).
