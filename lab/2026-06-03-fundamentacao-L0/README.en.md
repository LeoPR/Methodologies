---
title: Grounding of the timeless core (L0) — literature review
status: closed
created: 2026-06-03
updated: 2026-08-02
tags: [knowledge-architecture, L0, literature-review, fontes-primarias, auto-revisao]
outcome: confirmed
---

<!-- l10n: doc_id=lab-fundamentacao-l0-readme · lang=en · canonical -->
[Português](README.pt-BR.md) · **English**

# Grounding of the timeless core (L0) — literature review

> **Self-review cycle**: applies the L0's own **§6 (source discipline)** and **§3
> (traceability)** to the **L0's claims**. For each principle: the **primary source**,
> the degree of evidence and the **verification status**. That the method holds up when
> applied to itself is, in itself, evidence that it works.

## Question

Do the claims of the timeless core (`recipe/knowledge-architecture.md`, Part I) have
support in verifiable **primary sources** — and is each one in fact *older* than AI/the
computer, as the layers thesis claims?

## Method

For each principle, find the **original source** (not third-party summaries — primary >
secondary discipline). Record the full citation, grade the evidence and honestly mark
the status:

- **`[WEB ✓ 2026-06-03]`** — citation and claim checked on the web in this round
  (primary source located). To re-verify: fetch the cited primary source and compare
  it against the L0 claim it grounds.
- **`[CANÔNICO]`** — established work, cited from knowledge; not re-verified in this
  round. *Known* with high confidence, but the label is honest (§6).
- **`[ANALOGIA]`** — the link is the lab's interpretation, not the author's term.

## Result — grounding per L0 section

### §1 — Three artifact types / physical separation

| L0 claim | Primary source | Status |
|---|---|---|
| Separating concerns/artifact types is the basic technique for ordering thought | Dijkstra, E. W. (1974). *On the role of scientific thought* (EWD447) — coined "separation of concerns" | `[WEB ✓]` |
| Decompose by what each part **hides** / by the decision likely to change | Parnas, D. L. (1972). "On the Criteria To Be Used in Decomposing Systems into Modules." *CACM* 15(12):1053–1058 | `[WEB ✓]` |
| Content organization/labeling/structure is a discipline of its own (findability) | Rosenfeld, L. & Morville, P. (1998). *Information Architecture for the World Wide Web*. O'Reilly | `[WEB ✓]` |

### §2 — The four questions / findability / documentation types

| L0 claim | Primary source | Status |
|---|---|---|
| "Where is X?": the reader follows **trails (information scent)** to the target; the cost of not finding is redoing | Pirolli, P. & Card, S. (1999). "Information Foraging." *Psychological Review* 106(4):643–675 | `[WEB ✓]` |
| Findability is a design problem, not a technical detail | Rosenfeld & Morville (1998); Morville, *Ambient Findability* (2005) | `[WEB ✓]` |
| 4 documentation types (learning/solving × practice/theory) | Procida, D. — Diataxis (**L1** formalization; the need is timeless) | `[CANÔNICO]` |

### §3 — Traceability (source + rationale + version; append-only)

| L0 claim | Primary source | Status |
|---|---|---|
| **Provenance**: where the data came from (the "why / where from") | Buneman, P., Khanna, S. & Tan, W.-C. (2001). "Why and Where: A Characterization of Data Provenance." *ICDT 2001*, LNCS 1973:316–330 | `[WEB ✓]` |
| Recording **who made the change, when, where and why** + version | Rochkind, M. J. (1975). "The Source Code Control System." *IEEE TSE* SE-1(4):364–370 (1st version control; literally records who/when/where/why) | `[WEB ✓]` |
| **Append-only, auditable** record that is not rewritten (corrections go forward) | Pacioli, L. (1494). *Summa de Arithmetica* — "Particularis de Computis et Scripturis" (double-entry bookkeeping; balanced, auditable ledger). As an **ancestor** of the immutable record | `[WEB ✓]` `[ANALOGIA]` |
| The **rationale** (why/alternatives) lives in documentation, not code | Parnas, D. L. & Clements, P. C. (1986). "A Rational Design Process: How and Why to Fake It." *IEEE TSE* 12(2):251–257 | `[WEB ✓]` |

### §4 — Scientific record (hypothesis-first, reproducible, honest)

| L0 claim | Primary source | Status |
|---|---|---|
| **Hypothesis declared BEFORE** the data (distinguishing prediction from postdiction) | Nosek, B. A. et al. (2018). "The preregistration revolution." *PNAS* 115(11):2600–2606 | `[WEB ✓]` |
| Registered Reports / preregistration as a practice | Chambers, C. (2017). *The Seven Deadly Sins of Psychology* | `[CANÔNICO]` |
| **Reproducibility**: redoing the result from the record | Claerbout, J. F. & Karrenbach, M. (1992). "Electronic documents give reproducible research a new meaning." *SEG Tech. Program Expanded Abstracts* (coined "reproducible research") | `[WEB ✓]` |
| **Threats to validity** (internal/external/construct/conclusion) | Campbell, D. T. & Stanley, J. C. (1963). *Experimental and Quasi-Experimental Designs for Research*. Rand McNally (origin of the typology) | `[WEB ✓]` |
| ... applied to software engineering | Wohlin, C. et al. (2012). *Experimentation in Software Engineering* | `[CANÔNICO]` |
| **Preserving the negative result** (fighting publication bias) | Rosenthal, R. (1979). "The file drawer problem and tolerance for null results." *Psychological Bulletin* 86(3):638–641 | `[WEB ✓]` |
| Intro → method → result → discussion structure | Sollaci, L. B. & Pereira, M. G. (2004). "The IMRAD structure: a fifty-year survey." *J Med Libr Assoc* 92(3):364–367 | `[WEB ✓]` |

### §5 — Single source per altitude (DRY, oracle, literate programming)

| L0 claim | Primary source | Status |
|---|---|---|
| Every piece of knowledge has **one** authoritative representation (knowledge DRY) | Hunt, A. & Thomas, D. (1999). *The Pragmatic Programmer* | `[CANÔNICO]` |
| **One source from which both derive** (weave = doc, tangle = code) | Knuth, D. E. (1984). "Literate Programming." *The Computer Journal* 27(2):97–111 | `[WEB ✓]` |
| The **oracle** must be an external artifact that decides correctness (code is not its own oracle) | Weyuker, E. J. (1982). "On Testing Non-testable Programs." *The Computer Journal* 25(4):465–470 (frames the "oracle problem") | `[WEB ✓]` |
| Code under-specifies intent; the doc is the medium of design | Parnas & Clements (1986) — see §3 | `[WEB ✓]` |
| Self-checkable contract (pre/post-conditions + invariants) | Meyer, B. (1997). *Object-Oriented Software Construction* (2nd ed.) — Design by Contract | `[CANÔNICO]` |

### §6 — Source discipline (epistemology)

| L0 claim | Primary source | Status |
|---|---|---|
| Using the **best available evidence** / evidence hierarchy | Sackett, D. L. et al. (1996). "Evidence based medicine: what it is and what it isn't." *BMJ* 312(7023):71–72 | `[WEB ✓]` |
| Tendency to seek/interpret evidence that confirms prior beliefs | Nickerson, R. S. (1998). "Confirmation Bias: A Ubiquitous Phenomenon in Many Guises." *Review of General Psychology* 2(2):175–220 | `[WEB ✓]` |
| Verifying laterally / going to the original source (stop, investigate, find, trace) | Caulfield, M. (2017/2019). *Web Literacy for Student Fact-Checkers*; "SIFT (The Four Moves)" | `[WEB ✓]` |
| Evaluating the source (currency/relevance/authority/accuracy/purpose) | Blakeslee, S. (2004). "The CRAAP Test." *LOEX Quarterly* | `[CANÔNICO]` |
| Triangulating with N independent sources | Denzin, N. K. (1978). *The Research Act* | `[CANÔNICO]` |
| Knowledge has a **half-life** (perishability of data) | Arbesman, S. (2012). *The Half-Life of Facts* | `[CANÔNICO]` |
| Not discarding what is not understood (find out why it exists) | Chesterton, G. K. (1929). *The Thing* ("Chesterton's fence") | `[CANÔNICO]` |

### §7 — Knowledge generation and maturation pipeline

| L0 claim | Primary source | Status |
|---|---|---|
| Data → information → knowledge (maturation in levels) | Ackoff, R. L. (1989). "From Data to Wisdom." *Journal of Applied Systems Analysis* 16:3–9 (DIKW hierarchy) | `[WEB ✓]` |
| **Do not formalize N=1**; consolidate on recurrence (rule of three) | Fowler, M. (1999). *Refactoring* — "Rule of Three" (attrib. Don Roberts; cf. Roberts & Johnson 1996) | `[WEB ✓]` |
| Plan to **throw the first one away** (disposable exploration → production) | Brooks, F. P. (1975). *The Mythical Man-Month* — "plan to throw one away; you will, anyhow" | `[WEB ✓]` |

### §8 — Versioning as immutable history and provenance

| L0 claim | Primary source | Status |
|---|---|---|
| Recoverable history of who/when/why (version control as a concept) | Rochkind (1975) — see §3 | `[WEB ✓]` |
| Append-only auditable record | Pacioli (1494) — see §3 | `[WEB ✓]` `[ANALOGIA]` |
| Reproducibility as a test of the record | Claerbout & Karrenbach (1992) — see §4 | `[WEB ✓]` |
| Isolating what changes (kinship of "signal vs noise" with modularity) | Parnas (1972) — see §1 | `[WEB ✓]` |

### §9 — Effort economy (when to organize and when not to)

| L0 claim | Primary source | Status |
|---|---|---|
| Do not optimize (organize) too early; the overhead must pay off | Knuth, D. E. (1974). "Structured Programming with go to Statements." *ACM Computing Surveys* 6(4):261–301 (p. 268) | `[WEB ✓]` |
| Do not build what is not yet needed (YAGNI) | Beck, K. — Extreme Programming | `[CANÔNICO]` |

## Discussion

- **22 web-verified primary sources** in this round; the rest are canonical works
  (`[CANÔNICO]`) cited from knowledge.
- **The layers thesis holds up**: the sources range from **1494** (Pacioli) and the
  **scientific method** (Campbell & Stanley 1963; 19th-century laboratory notebooks)
  to 1972–1999 (software engineering) — **all older** than modern AI and the IDE.
  The L2 layer (today's tools) is, in fact, *form* over a core that already existed.

## Limitations / caveats (epistemic honesty — §6)

- **`[ANALOGIA]` Pacioli/double-entry → append-only record**: the link is the lab's;
  Pacioli did not speak of an "immutable ledger". It is a *conceptual ancestor* of the
  auditable record, not a literal citation of the modern concept.
- **IMRaD volume**: *J Med Libr Assoc* **92(3):364–367** is used (consistent with
  PubMed PMID 15243643); one web source spelled "95.3" — discarded by triangulation.
- **`[CANÔNICO]`**: items not re-verified in this round. If any becomes *load-bearing*
  in a dispute, re-verify first (mark `[VERIFICAR]`).
- **SIFT**: origin 2017 ("Four Moves and a Habit"); the "SIFT" name consolidated in
  2019 — both by Caulfield.

## Next step

Weave these citations back into `recipe/knowledge-architecture.md`: each L0 section
gets a **"Grounding"** line pointing to the primary source(s) — making the core itself
traceable (§3 dogfooding). Then proceed to Parts II (L1) and III (L2).
