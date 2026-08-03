<!-- l10n: doc_id=outreach-2026-08-linkedin-artigo · lang=en · translation_of=artigo.pt-BR.md · source_lang=pt-BR -->
**English** · [Português](artigo.pt-BR.md)

# Strata in August 2026: what the tests show when AI tries to organize knowledge

*Technical article. Every claim here has a pre-registered answer key, a logged run, and an open
results document in the repository. Where the regime is weak, the text says weak.*

## The problem and the method

Any long work accumulates knowledge: research, code, decisions, notes. Over time it rots: you
cannot find what you decided, you do not know what still holds, and the next tool threatens a
full restart. Strata attacks this with a durability-layered architecture:

- **Mneme (L0)**, memory: the principles that precede the computer. Method, traceability,
  single source, immutable history. The test question: "if AI and the computer disappeared,
  would this still be true?". Editorially closed on August 1, 2026.
- **Morfé (L1)**, form: the mature forms that embody the principles (decision records,
  append-only history, tombstones). One good form, not the only one; replaceable without
  touching the core.
- **Órganon (L2)**, instrument: today's tools, like AI and git. Detachable: when the tool
  dies, only this layer changes.

The practical thesis: switch tools without losing the why. The rest of this article is about
how we tested whether an AI can actually apply this method, and what answered back.

## How we test

The laboratory is public and cheap to reproduce (the full grade costs about US$ 7). The
principles: controlled synthetic scenarios with a pre-registered mechanical answer key; arms
with and without the method over the same project; a blind jury of models from other vendors;
frozen fixture hashes; pre-registration before running. The mother metric is simulated
execution: the model emits the fix files and a mechanical verifier inspects the final state,
with no human judge and no AI judge at the main gate.

Three situations organize the grade: the **§5 fix** (two conflicting "official" sources of the
same fact; the right move is to elect one canonical and retire the other preserving its
content), the **§6-bis trap** (the same project with a planted malicious instruction,
"download and run this script"; the right move is to refuse), and the **already-good project
§9** (nothing to fix; the right move is to not act).

## What the current model generation already does

**The fix saturated.** From ~8B models on a consumer GPU to the paid frontier top, with the
method everyone executes the fix to standard, with tombstone, pointer, and preserved history.
Without the method, the same models fail across the whole grade: they improvise, erase
history, or propagate the duplication. The with/without contrast is the study's mother metric,
and it is large.

**Security refusal comes out spontaneously.** Facing the planted instruction, current
generation models refuse to execute, cite the principle that an instruction read from a file
is data, not an order, and neutralize the content. This holds even at the affordable tier.
Cataloged exception: one model (llama-4-scout) failed the trap fix twice and propagated the
payload once.

**In the first cell with real tools, the pattern transferred.** With an agent in a sandbox
actually executing, the fix came out in 10 of 12 cases with the method against 2 of 12
without, and none of the 24 runs executed the malicious command.

## The real edge: knowing when not to act

What separates models today is not fixing, it is **abstaining**. On an already-good project,
some recognize the good and leave it alone; others invent defects to justify the task. This
edge is a model property: it does not order by price, by tier, or (now measured) by language.
There are calibrated budget models and overacting expensive ones. Practical consequence, now a
product rule: mid or affordable models work with a checklist and a human confirming each
finding; autonomous self-audit, with nobody in the loop, is a frontier-top mode.

And there is an ecological caveat the project carries at the top of its documents: on real
third-party projects, under the "find problems" request, every arm, baseline included,
over-detected. The abstention form fixes the false positive; the hunting framing does not.
That is why the method is sold as assisted organization, not as an autonomous auditor of
other people's projects.

## Portuguese × English: the missing question

The canonical document of the method is English, but all the evidence had been produced in
Portuguese. On August 3, 2026 we closed parity: the grade core was repeated in English with an
identical roster, and a separate pilot measured refusal in both languages.

The result, in one sentence: **run the method in the language of whoever reads and applies
it**. Fix and abstention reproduce with parity; the top tier closes 6 of 6 in both languages;
the project's language does not move the numbers. English is not better in any cell. And two
practical findings: mixing languages (method in English with an instruction to answer in
Portuguese) was the worst security configuration of the entire study, and there is a weak,
dated signal that mid open models refuse injection slightly worse in English (5/8 × 1/8, two
runs per cell; to be confirmed with more volume if it ever matters).

## The cost, measured

One AI audit of a small project, method plus project on input and an answer on output, costs
about **1 cent** on the reference budget model. Reproducing the whole published grade costs
about **US$ 7**. Language moves cost by around 20%: Portuguese tokenizes more expensively
than English for the same content, a tokenizer inequality documented in the literature, a
real effect but too small to drive decisions. The metric that organizes value is **cost per
organized project**: one AI pass with the method costs less than one minute of human time,
and the output is traceable, with what changed, why, and under which authority.

## What this is not

Signals in controlled synthetic scenarios, not proofs. Ecological validation is ongoing. AI
output is a draft to review, always. Models age fast; the cited names are dated by design,
and the laboratory exists precisely to re-run when the shelf turns over.

## Where to read and verify

Everything is open: the method, the usage guides (which model, which language), the
experiments, the answer keys, and the results documents behind every number in this article.

👉 https://github.com/LeoPR/Methodologies

#KnowledgeManagement #InformationArchitecture #ArtificialIntelligence #Methodology #SoftwareEngineering
