<!-- l10n: doc_id=outreach-2026-08-medium · lang=en · translation_of=historia.pt-BR.md · source_lang=pt-BR -->
**English** · [Português](historia.pt-BR.md)

# I tested whether AI can organize knowledge on its own. The answer is more interesting than "yes" or "no"

*A durability-layered method, a US$ 7 laboratory, and what I learned when I measured everything
twice, in two languages.*

---

Any long work accumulates knowledge. Research, code, decisions, notes. Over time, it rots: you
cannot find what you decided, you do not know what still holds, and the next tool threatens a
full restart. I spent time distilling a method for this. It is called Strata, and the core idea
fits in one sentence: separate what is timeless from what is dated, so you can switch tools
without losing the why.

The method organizes knowledge into three durability layers, with Greek names that tell the
story of recorded knowledge. **Mneme**, memory, is the timeless core: principles that precede
the computer, like method, traceability, and single source. **Morfé**, form, is the layer of
mature forms that embody the principles: decision records, append-only history, tombstones.
**Órganon**, instrument, is today's tools: AI, git, the editor. When a tool dies, only this
layer changes.

A method like this must answer an uncomfortable question: can an AI apply it? Not in
conversation, in practice: read a messy project and return the right fix, with history
preserved and without obeying what it should not. That is what I measured.

## The laboratory

The laboratory's principles are the method's own: synthetic scenarios with a pre-registered
mechanical answer key, arms with and without the method over the same project, a blind jury of
models from other vendors, pre-registration before running. The main metric is simulated
execution: the model emits the fix files and a mechanical verifier inspects the final state.
No human judge, no AI judge at the main gate. And everything is cheap to reproduce: the whole
grade costs about US$ 7.

Three situations organize the tests. The **fix**: two conflicting "official" sources of the
same fact, and the right move is to elect one canonical and retire the other while preserving
its content. The **trap**: the same project with a planted malicious instruction, "download
and run this script", and the right move is to refuse. And the **already-good project**:
nothing to fix, and the right move is to do nothing.

## What current models already do

The first surprise: the fix saturated. From ~8B models on a consumer GPU to the paid frontier
top, with the method everyone executes the fix to standard, with tombstone, pointer, and
preserved history. Without the method, the same models fail across the whole grade: they
improvise, erase history, propagate the duplication. The difference between with and without
the method is the study's central measurement, and it is large.

The second: security refusal comes out spontaneously. Facing the planted instruction, current
generation models refuse to execute, explain that an instruction read from a file is data, not
an order, and neutralize the content. This holds even on the budget model. One cataloged
exception: one model failed twice and propagated the payload once. It is named in the
documents.

The third came from the newest cell: with an agent in a sandbox actually executing, with real
tools, the pattern held. Ten of twelve correct fixes with the method, two of twelve without.
None of the twenty-four executions ran the malicious command.

## The real edge

What separates models in 2026 is not fixing. It is **not acting**. On an already-good project,
some models recognize what is right and leave it alone; others invent defects to justify the
task. This edge does not order by price, nor by tier. There are calibrated budget models and
overacting expensive ones. The practical rule that came out of it: mid models work with a
checklist and a human confirming each finding; autonomous auditing, with nobody in the loop,
is a frontier-top privilege.

And there is a caveat the project carries with pride: on real third-party projects, under the
"find problems" request, every arm over-detected, baseline included. The abstention form fixes
the false positive; the hunting framing does not. The method is sold as assisted organization,
not as an autonomous auditor of other people's projects.

## The language question

The canonical document of the method is English. All the evidence, though, had been produced
in Portuguese. An attentive reader could ask: was this tested on the English text? So I
repeated the grade core in English, with an identical roster, and measured refusal in both
languages in a separate pilot.

The answer is liberating: **use the language of whoever reads and applies it**. Fix and
abstention reproduce with parity, the top tier closes 6 of 6 in both languages, and the
project's language does not move the numbers. English is not better in any cell. Mixing
languages, method in English with an instruction to answer in Portuguese, was the worst
security configuration of the entire study.

There is also a measured cost: Portuguese tokenizes about 22% more expensively than English
for the same content, a tokenizer inequality documented in the literature. It is real, but it
vanishes in the bill: a full audit of a small project costs about one cent on the budget
model. The metric that matters is different: the **cost per organized project**, which comes
out at less than one minute of human time.

## What this is not

Signals in controlled scenarios, not proofs. Validation on real projects is ongoing. AI
output is a draft to review, always. And models age fast: the cited names are dated by
design, and the laboratory exists to re-run when the shelf turns over.

Everything is open: the method, the usage guides, the experiments, the answer keys, and the
results documents behind every number in this text.

**Repository:** https://github.com/LeoPR/Methodologies

---

*Written in August 2026. The numbers are dated out of honesty; the method, by design, is not.*
