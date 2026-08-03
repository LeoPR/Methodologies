---
title: Strata in Portuguese or English (trust guide)
status: active
created: 2026-08-03
updated: 2026-08-03
purpose: answer, objectively, "which language should I run Strata in?". Only the conclusions; the why lives in the linked evidence
---

<!-- l10n: doc_id=strata-idiomas · lang=en · canonical -->
**English** · [Português](strata-idiomas.pt-BR.md)

# Strata in Portuguese or English: what works where

**Short answer: run Strata in the language of whoever reads and applies it.** Both versions
are first-class: `knowledge-architecture.en.md` is the canonical source and
`knowledge-architecture.pt-BR.md` is the derived translation, updated in the same commit
(ADR-008). The method was measured in both languages on 2026-08-03 with identical rosters;
the core behavior is the same.

## What holds in BOTH languages (measured)

- **Fixing a known defect (§5) saturates**: from affordable cloud models to the frontier top,
  every model executes the fix to standard with Strata, in PT and in EN alike (6/6 and 6/6).
  Without Strata, the same models fail across the whole grade in both languages.
- **Abstention (§9) is the edge, and it is a model property**: not price, not tier, not
  language. The same models over-act or stay calibrated in both languages.
- **The top tier closes both sides in both languages** (fix/trap/abstention, 6/6): the
  autonomous self-audit mode is safe in either language.
- **The language of your PROJECT does not matter**: method in EN × project in PT scored the
  same as method EN × project EN.

## What is language-sensitive (dated signals, 2026-08-03)

- **English is NOT better.** Switching the method to English hoping for a boost has no
  support: the refusal edge measured equal or slightly worse in EN (two independent
  instruments, same direction).
- **Mid/open models refuse injection a bit worse in EN** (payload propagated 5/8 in EN × 1/8
  in PT at the GPU tier; K=2 signal, dated). It does not change the recommendation, which is
  already "mid/affordable = checklist + human review" in **both** languages.
- **Do NOT mix languages.** The recipe "method in English, answer in Portuguese via an
  instruction" was tested and **rejected**: it had the worst obedience to the malicious
  payload in the whole study (4/6). One language end to end.

## Practical table

| Your situation | Do this |
|---|---|
| You read/work in Portuguese | Use `knowledge-architecture.pt-BR.md`. Full coverage; nothing lost. |
| You read/work in English | Use `knowledge-architecture.en.md`. Same proof coverage. |
| Mid/affordable or local model | Either language + **checklist + human confirming each finding** |
| Top model, autonomous self-audit | Either language (6/6 in both) |
| Project in a different language than the method | Fine as is; no need to translate the project |

## Why (pointers, not repetition)

- Language pilot, refusal (F3): [`lab/2026-08-03-idioma-en/RESULTADOS-idioma-f3.md`](../lab/2026-08-03-idioma-en/RESULTADOS-idioma-f3.md)
- Parity grade, fix/abstention/trap (F4): [`lab/2026-08-03-idioma-en/RESULTADOS-f4-en.md`](../lab/2026-08-03-idioma-en/RESULTADOS-f4-en.md)
- The full honest grade (which model for which task): [`OPINIAO-DE-USO`](../lab/2026-06-04-strata-hipoteses/OPINIAO-DE-USO.md)

*Signals are dated (2026-08-03) and model generations move fast. Re-check the linked evidence
before anchoring an expensive decision on this page.*
