---
title: Strata with AI (practical usage guide)
status: active
created: 2026-06-08
updated: 2026-09-30
purpose: answer the developer asking "does it work in my environment? will it be expensive?". Only what works
nota: the model bank behind this page, with the reasoning and web axes and every caveat, is in lab/2026-09-26-banco-modelos/; older research (what does NOT work and why) in lab/2026-06-04-strata-hipoteses/RESULTADOS-p6..p9
---

<!-- l10n: doc_id=strata-com-ia · lang=en · canonical -->
**English** · [Português](strata-com-ia.pt-BR.md)

# Strata with AI: practical guide

The method text is the same for everyone. What changes the result is **who runs it and how**.
Five rules before any model:

1. **AI output = a draft to review**, never an automatic verdict.
2. **Autonomous self-audit (AI auditing a real project alone) is a top-tier-only mode**: on real
   projects it only paid off with the top model. For every other model the setup that works is
   **checklist + human confirming each finding**.
3. **Reasoning effort: leave it at the model's default or `low`. Never `high`** for judgment
   tasks. (It is the API parameter that sets how much the model "thinks" before answering: `off`,
   `low`, `medium`, `high`; it changes neither model size nor answer length.) More thinking did not
   improve any cell, cost more, and sometimes made the model act on a project that was already
   good or run out of budget before answering.
4. **Source verification (§6) needs web search on.** Without it, even top models confirm
   outdated facts with confidence. Without web, read "correct" as "not verified".
5. **For a full evaluation by a mid or budget model, give it the checklist in stages, not the
   raw text.** For a known fix the raw canonical text already works. The checklist
   (`../lab/2026-06-04-strata-hipoteses/strata-ai-native/strata-checklist.md`) is a prototype
   older than the closed L0 (no gate for §11 or for the authority-to-read side of §6-bis): use
   it as a scaffold, not as the method.

> **Where the evidence holds (read before the table):** the numbers come from **synthetic
> fixtures** with a pre-registered answer key and a mechanical scorer. In **real third-party
> projects**, the AI self-auditor did **not** beat plain competence: with the "find problems"
> framing, every arm (baseline included) over-detected; the **abstention form** is what corrects
> the false positives
> ([R8](../lab/2026-06-04-strata-hipoteses/RESULTADOS-r8-sintese-3-projetos.md);
> [external arm](../lab/2026-06-04-strata-hipoteses/RESULTADOS-externo-bemcomportado.md)).
> Use the table to pick a model for **controlled tasks** (fix, trap, abstention); treat
> real-project audits as drafts for a human.

## Quick decision: what to use (2026-09 bank)

"Does everything" = fixes the known defect (§5), refuses the planted malicious instruction
(§6-bis) **and** abstains on a project that is already good (§9), in the majority of three runs
each.

| I want… | Use | Why |
|---|---|---|
| **the cheapest that does everything** | **gpt-6-luna** · mimo-v2.6-flash · glm-5.3-flash (effort `low`) | a fraction of a cent per run; luna answers in seconds |
| **the fastest that does everything** | **gemini-3.5-flash-lite** | answers in seconds, at a fraction of a cent per run |
| **open weights that do everything** | **qwen3.8-27b** (27B dense, Apache 2.0) | does everything at every reasoning-effort level; with reasoning `off` it is 5× cheaper and faster |
| **the top** (autonomous audit of a real project) | **opus-5.5** · **gpt-6-sol** · **gemini-3.8-flash** · sonnet-5 · grok-4.7 | all do everything; gpt-6-sol and gemini-3.8-flash cost about 5× less than opus-5.5 |
| **free, and does everything** | **kimi-k3** · **deepseek-v4.1-flash**, both on NVIDIA NIM | zero cost; kimi-k3 takes tens of seconds per run, deepseek-v4.1-flash minutes. Other free routes cap tokens per minute below one method prompt (Groq's free plan, for instance); dated limits are in the bank |
| **on your own machine, 24 GB GPU** (3090, 4090) | **qwen3.8:27b** | the weights do everything; with the whole method in the prompt it fits a 24 GB card (measured), decoding tens of tokens per second (projected) |
| **on your own machine, 12 GB GPU** | **qwen3.6:35b-a3b** (MoE, expert offload) with reasoning **`off`** | fixes and is safe (refuses the injection), but does **not** abstain: pair it with a human who decides when not to touch; tens of tokens per second with offload (measured). Only up to ~12B dense fits whole with the method in the prompt; qwen3.8:27b also runs here with offload, but slowly (minutes per run, reasoning `off`) |
| **on a unified-memory box** (NVIDIA GB10 / DGX Spark, AMD Ryzen AI Max+ 395) | large MoE models; **deepseek-v4.1-flash** on 2+ linked GB10 | lots of memory, little bandwidth (273 GB/s on GB10, 256 GB/s on the Ryzen): dense models decode slowly, MoE fits better. DeepSeek V4.1-Flash (does everything) runs on linked GB10s with vLLM ≥ v0.30.0 (third-party measurement on 2 units: tens of tokens per second); not on llama.cpp or local Ollama yet ([fit by GPU](../lab/2026-06-04-economia-ia-tokens/instrumento/STAGE5.md)) |
| **fix + trap only, very cheap** | gemma-4-26b-a4b · gemma-4-31b | they fix and refuse, but do **not** abstain: pair them with a human who decides when not to touch |
| **do NOT use for autonomous action** | **gpt-oss-120b** · **claude-haiku-4.5** · gemma4:12b · llama-4-scout · local below ~4B | all propagated the planted injection at least once (gpt-oss-120b 3/3); haiku-4.5 also never abstained; gemma4:12b has no cloud host, so its result holds for the local Q4 only; below ~4B not even the format comes out |

*Cost and time are **bands**, not prices of the day: cost per run in a fraction of a cent (below
US$ 0.01), cents (up to US$ 0.10) or tenths of a dollar; time per run in seconds (under 15 s),
tens of seconds or minutes. The exact values, dated and returned by the provider, are in the
[bank](../lab/2026-09-26-banco-modelos/); today's catalog prices are on the provider's page.*

*Rule: the edge that separates models is **abstention** (not touching what is already good). It
depends on the **model and on how the request is worded**, not on price, and there is no
evidence that the method's text buys it (§9). (Names and prices date quickly: they live in the
dated layer, L2. Re-audit before anchoring an expensive decision.)*

> **Source and regime (2026-09-26):** model bank, three cells (§5 fix on `f4-dup`, §6-bis trap
> on `f4-trap`, §9 abstention on `f4-clean-v2`, the fixture without the answer leak), K=3,
> mechanical gold scorer, real cost returned by the provider. Directional signals, not proof.
> Full table, reasoning and web axes, and caveats:
> [`lab/2026-09-26-banco-modelos/`](../lab/2026-09-26-banco-modelos/).
>
> **Local = the same weights.** A model's capability belongs to its weights: it is measured in the
> cloud on the same weights, and it holds on your machine. Your machine answers a different
> question: does it fit, and how fast. That is measured on a few points and projected for other
> cards ([fit by GPU](../lab/2026-06-04-economia-ia-tokens/instrumento/STAGE5.md)). A cloud × local
> bridge on the same cells checks that quantization does not change the conclusion.

![Strata by AI: which model to use, by access context](strata-com-ia-fronteira.en.svg)

## Reasoning and web: how to set them

| Parameter | Set it to | What was measured |
|---|---|---|
| **reasoning effort** | model default or `low` (locally: `off`) | `high` never improved a cell; it cut gpt-6-luna's abstention from 3/3 to 1/3 and made gemini-3.8-flash fail the trap; deepseek and glm ran out of budget. Off helps only models that stay robust (qwen3.8-27b) and can hurt abstention in others |
| **models whose reasoning cannot be turned off** | use the lowest accepted level (`low`) | glm-5.3-flash rejects "off" (HTTP 400); gemini-3.8-flash rejects "minimal"; opus-5.5 always thinks |
| **token budget** | generous (≥12k output) for thinking models | truncation is the most common failure of thinking models; a truncated answer is not a verdict. Locally, thinking plus the whole method overflowed a 32k context: run local models with reasoning `off` |
| **web search** (`:online` or the vendor's search tool) | on, for source verification (§6) | without web, gemini-3.8-flash and deepseek-v4.1-flash confirmed outdated facts; with web, gemini and gpt-6-luna corrected 6/6. Without web, qwen3.8 is the most honest (it says "not verifiable") |
| **temperature** | do not rely on it | the GPT-6 line and sonnet-5 do not accept it (the router drops it silently); DeepSeek ignores it while thinking |

## How you ask: what it helps and what it does not

For a **full evaluation** by a mid or budget model, the form of the request helps:
- **Checklist** (yes/no per gate, with the 3 anti-false-positive rules) >> raw text.
- **Stages** (applying in separate turns): the model acknowledges what is good and places it in
  time **before** pointing defects.
- It does **not** buy the judgment of when *not* to act: that stays with the model, and a
  well-worded plain request calibrates it as well as the method or better.

## Limits (what to expect: not a defect, how to calibrate)

- **Over-acting is not a tier stamp:** cheap models do everything here, and some mid models
  (gemma 4) fix and refuse but do not abstain. Check the specific model.
- **The temporal dimension depends on legibility:** with readable dates and history (§3/§8)
  models place things in time correctly; with noisy or unmarked history they flag the historical
  as a current problem. Review dated findings carefully.
- **The route changes without notice:** the same model name is served by different providers, and
  vendors swap what answers to a name (since 2026-09-14 DeepSeek's API serves V4.1-Flash when
  V4-Pro is requested). The plan header records who served each run.
- **Truncation deceives:** a thinking model may look "clean" only because it ran out of tokens
  before concluding. A truncated answer is INDETERMINATE, never a pass or a fail.
