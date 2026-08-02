---
title: Knowledge architecture — organize, track, and generate
project: Strata
version: 1.2.0
type: reference
status: active
created: 2026-05-20
updated: 2026-08-01
lang: en
canonical-source: Acadêmicos/Methodologies/recipe/knowledge-architecture.en.md (Strata project). This English file is the canonical source (authority migrated 2026-08-01 by explicit decision — see ADR-008, addendum); the Portuguese file is a derived translation.
license: CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/)
audience: knowledge workers (researchers, engineers) and AI agents — neutral
layers: L0 timeless core · L1 consolidated patterns · L2 adaptation to the current era
supersedes: organization-methodology.md (archived in lab/2026-06-03-predecessor/)
how-to-use: on-demand reference; Part I is self-contained and independent of any tool
decisions: decisions/
---

<!-- l10n: doc_id=strata-knowledge-architecture · lang=en · canonical -->
<!-- Freshness ruler = git history (see recipe/documentacao-multilingue.md), not a hand-written stamp.
     Translate prose only, never the § refs, code, paths, the Greek layer names (Mneme/Morfé/Órganon),
     or the grounding citations. -->
[Português](knowledge-architecture.md) · **English**

# Knowledge architecture — organize, track, and generate

> A method to **organize, track, and generate** knowledge and information across
> the life of a project — research, scientific software, or any intellectual work
> that accumulates artifacts. The problem is **older than** the computer, the
> internet, and AI: librarians, scientists, and engineers have faced it for
> centuries. The tools of each era (today: AI agents, editors, version control)
> are **forms** that express this method — they shape it, but do not found it.
>
> The applier this method assumes is timeless: anyone with the time and
> patience to organize **any library that ever existed or will exist**. In the
> current era that reader is, often, an AI agent — an instance, not an
> exception (§6-bis applies the same pattern to prompt injection).

## How to read — the three durability layers

Everything here is classified by **durability**. That decides what is stable and
what you should expect to replace.

| Layer | What it is | Cadence | Test |
|---|---|---|---|
| **Mneme** · L0 — Timeless core | scientific method, information architecture, epistemology, traceability | decades/centuries | "if AI and the computer vanished, would it still be true?" |
| **Morfé** · L1 — Consolidated patterns | named, mature, but replaceable formalizations (Diataxis, ADR, FAIR, IMRaD, Conventional Commits) | ~decades | "it is *one* good way to do the L0, not the only one" |
| **Órganon** · L2 — Adaptation to the current era | how today's tools express L0/L1 (AI agents, IDE/VSCode, git, caches) | months | "swappable without touching the L0" |

> **The layer names** (Greek; `L0/L1/L2` remains the technical nickname): **Mneme** (μνήμη,
> *memory* — what endures and is transmitted without being lost), **Morfé** (μορφή, *form* — how
> knowledge is encoded), and **Órganon** (ὄργανον, *instrument* — the dated tool that carries it).
> Stratifying by **durability** (the slow layer constrains the fast one) has a named precedent:
> *pace layering* (Brand, 1999). Etymology and grounding in the [glossary](../GLOSSARIO.md).

- **Part I** (this document, below) is the **L0** — complete and self-contained. It
  reads on its own, without naming any tool.
- **Part II** maps **L1** patterns to each L0 need.
- **Part III** is the **L2** layer: dated, with a revalidation deadline,
  detachable. When a tool dies, only Part III changes.

> **STRONG / LOCAL convention** (used throughout): **STRONG** = tied to L0/L1
> (a principle, not renameable); **LOCAL** = an example from the L2 layer (a folder
> name, tool, metaphor — swap it freely). Your project's local conventions
> override the names here.

---

# PART I — TIMELESS CORE (L0)

> Principles that precede and outlive any tool. No product name, no date. If a
> passage here depends on a specific tool, it is in the wrong place — it belongs
> to Part III.
>
> **Grounding**: each section lists its primary sources. In the source repository
> (`Strata/lab/2026-06-03-fundamentacao-L0/`), 22 web-verified sources
> (2026-06-03) — **all predating AI and VSCode** (from Pacioli, 1494, to classical
> software engineering), which confirms the layers thesis. The sections added
> later (§3-bis, §6-bis, §10 and the refinements to §3/§5/§6/§7/§9) had their
> grounding verified in a second cycle `[WEB ✓ 2026-06-03]`
> (`Strata/lab/2026-06-03-future-proof-sweep/`). §11 had its grounding verified
> in a third cycle `[WEB ✓ 2026-08-01]` (`lab/2026-08-01-fechamento-camadas/`).

## 1. The invariant problem: three kinds of artifact that conflict

Every project that lasts accumulates **three kinds of artifact** with different
cadences and audiences. Mixing them generates entropy — it is the root cause of
most symptoms of disorganization.

| Kind | Nature | Cadence | For whom |
|---|---|---|---|
| **Product** | the stable, publishable result | changes slowly, carefully | the user / the future |
| **Exploration** | attempts, drafts, experiments | high turnover, disposable | yourself, months from now |
| **Knowledge** | what was learned, decided, concluded | semi-stable | reviewer, collaborator, successor |

**STRONG principle — physical separation**: each kind lives in its own place,
with its own rules. The stable result is not polluted by drafts; the draft is not
frozen under the rules of the stable; the knowledge is not lost between the two.
This is applied information architecture — older than any medium.

**Symptoms of mixing** (universal): redoing what already exists; redoing
decisions already made; a stable document polluted with work-in-progress;
whoever arrives later gets lost.

> **Grounding**: separation of concerns — Dijkstra 1974 (EWD447); modularity /
> *information hiding* — Parnas 1972 (*CACM*); information architecture —
> Rosenfeld & Morville 1998.

## 2. The four questions every knowledge base must answer

Regardless of medium or tool, a body of work must answer, to whoever arrives
(human or machine), four questions. These are the **needs** — the formalizations
that meet them (in Part II) are replaceable.

| Question | L0 need | (L1 formalization → Part II) |
|---|---|---|
| **"Where is X?"** | findability: an entry point, a map, trail signs (*scent*) that guide to the target | information architecture; maps/indexes |
| **"How do I use / understand this?"** | documentation that distinguishes *learning* from *solving*, and *practice* from *theory* | Diataxis (4 quadrants) |
| **"Why did we decide X?"** | a decision record with the *why*, immutable, supersedable but not erasable | ADR / decision records |
| **"Is this reliable / reproducible?"** | validation: the result can be redone and was obtained honestly | scientific method, reproducible compendium |

Findability deserves a note: the cost of **not finding** is redoing. That is why
the entry point and the map are not a luxury — they are what keeps work from
being recreated out of ignorance that it already exists. **STRONG**: before
creating, check whether it already exists.

> **Grounding**: *information scent* — Pirolli & Card 1999 (*Psychological
> Review*); findability as a design problem — Rosenfeld & Morville 1998 /
> Morville 2005.

## 3. Traceability — the first-class principle

> You named this as a central goal ("organization **and** tracking"). It is an L0
> principle in its own right, not a detail scattered around.

**Every artifact, claim, and decision must be traceable to three things:**

1. **Source** — where it came from (who / which evidence / which origin data).
2. **Rationale** — why it exists / why it was decided this way (the intent, the
   rejected alternatives).
3. **Version** — in what state this was true (which moment, which revision).

From this derive several mechanisms that are, at bottom, the same principle:
**provenance** of a datum, **supersession** of a decision (the new one points to
the one it replaces), **stable identity** of an artifact (a name/ID that does not
change), **authorship** (who — or what — produced it), and **chain of custody**
(history is not rewritten; it is corrected going forward).

**STRONG principle — the trace is append-only**: you correct by adding, not by
erasing. A refuted result **remains** (refutation is knowledge). A revoked
decision **remains**, marked as superseded. Quietly erasing the past destroys
traceability. (The mechanism that makes this practicable — state-recoverable
history — is in §8.)

But *append-only* governs the **trace**, not the **reading surface**. Three planes
that naive recording collapses into one:

- **Trace** (what happened) — **immutable and recoverable**; never destroyed.
- **Surface** (what the reader encounters first) — **decays through disuse and
  obsolescence**: `active → superseded-but-visible → silenced` (retained,
  recoverable, off the default reading path) `→ disposed`. Demoting **access** is
  not destroying the **trace**. Without this distinction, every dead claim weighs
  on the surface as much as a live one and auditability turns into noise: the
  reader pays to sweep what no longer holds (§9).
- **Living knowledge** (the narrative taught going forward) — **re-narratable** to
  each new reader, with the previous version **chained**. Re-expressing with
  provenance ≠ furtive editing.

**Two opposing rules, not one**: to the **trace**, you only add (never erase or
edit — it is the history, the accepted decisions); on the **surface**, **actively**
demote what has died (silence it, leaving a tombstone). Applying *append-only* to
the surface is the error that makes reading rot under the weight of what no longer
holds.

**The end of the cycle is governed, not absent.** The real opposition is not
erase-vs-never-erase; it is **furtive editing** (always forbidden — it corrupts
history in silence) vs **authorized disposal** (legitimate and itself a record).
Disposal **leaves a tombstone**: what, when, why, under whose authority — the gap
stays **legible**, not silent. Retaining everything forever, undifferentiated, is
a failure mode, not the supreme virtue.

**Two times, not one.** Distinguish *when something was true/in force in the world*
(valid time) from *when the record captured it* (transaction time): reconstructing
"which rule held **when** the fact occurred" is different from recovering "the
state of the file on that date" (§8). Amending ≠ revoking ≠ correcting what was
always so.

**Marking the confidence next to the claim** is part of traceability: a
strong-source claim ≠ a claim to be confirmed ≠ a personal hypothesis ≠ content
generated by an agent. Each carries its label (the form of the label is L2).

> **Grounding**: data provenance — Buneman, Khanna & Tan 2001 (ICDT); recording
> who/when/where/why + version — Rochkind 1975 (SCCS, *IEEE TSE*; the first
> version control); append-only auditable record — Pacioli 1494 (double-entry
> bookkeeping; ancestral analogy); rationale in documentation — Parnas & Clements
> 1986.
>
> Additions (trace/surface gradient, disposal, bitemporal) `[WEB ✓ 2026-06-03]`:
> access decays but the trace remains (retrieval strength ≠ storage strength) —
> Bjork & Bjork 1992 (*From Learning Processes to Cognitive Processes*, vol. 2,
> pp. 35–67); disposal and retention schedule as a governed act — Schellenberg
> 1956 (*Modern Archives: Principles and Techniques*); bitemporality (valid time
> ≠ transaction time) — Snodgrass 1999 (*Developing Time-Oriented Database
> Applications in SQL*, Morgan Kaufmann).
>
> Era instance `[2026-06]` — legible traceability lets an AI reader locate time
> (signal, N=1): `lab/2026-06-04-strata-hipoteses/RESULTADOS-f6-temporal-sem-marcadores.md`.

## 3-bis. Force of the artifact: what act this is

Alongside *where it came from* and *how reliable it is* (§3), every artifact
carries a third mark — **orthogonal** to the other two: **what act it performs**.
"I think X" and "do X" can have the **same** confidence and the **same** provenance
and demand **opposite** actions from the reader. Confusing them is a reading error,
not a matter of degree.

The cut with the most practical weight:

- **Dispositive** — the artifact **constitutes** what it says: a decision, a
  definition, a commitment, a directive. There is no external source to check —
  it **is** the source. Undoing it is a **new act**, not an edit (this, and not
  the cost of re-creation, is why an accepted decision is immutable — a distinction
  §8 today conflates).
- **Probative** — the artifact **records** something true elsewhere: a
  measurement, an observation, a chronicle. It has an external source — and so it
  **revalidates at the source** (§6). Marking this as dispositive would be
  pretending the artifact creates the fact it merely witnesses.

> **STRONG**: mark the type of act. A reader — human or agent — who ingests a
> corpus without knowing what is a directive, what is a disposable hypothesis, and
> what is a record of fact reads it all on the same plane and errs.

**Declare the frame of reference, not just the instant.** §3 stamps *when*
something was true; what is missing is the spatial-metric twin: **against what
origin / unit / reference frame** a value reads. "3 measures", "coordinate Y",
"cost Z" only mean anything against a declared standard — a number without a unit
is noise with the appearance of signal. (The *Mars Climate Orbiter* probe, 1999,
was lost because pound-force was read as newton.)

**Declare the decoding key too — and make it redundant.** Even before *reading*
the content, the receiver needs to know *in what language / schema / codec* it is
and *where the dictionary is*. That key (vocabulary, unit, format) is itself a
first-class artifact. **Unlike the content** (§5, which minimizes repetition), the
key **must** be redundant and co-located: a legend that lives only in a distant
source is a single point of decoding failure. A record whose key has been lost is
as mute as a cuneiform tablet without a dictionary — and the Rosetta Stone is the
famous counterexample: it carries its own key.

> **Grounding** `[WEB ✓ 2026-06-03]`: the **dispositive / probative** boundary is
> terminology from medieval diplomatics — `charta` (the document *is* the act:
> first person, present tense) vs `notitia` (the document *proves* an act
> consummated elsewhere: third person, perfect), the dispositive clause opened by
> a performative (`notum sit` / `sciatis`). Formalized by Brunner 1880 (*Zur
> Rechtsgeschichte der römischen und germanischen Urkunde*, Berlin) — ~80 years
> before Austin 1962 (*How to Do Things with Words*) and Searle 1969, who merely
> **name** it (= L1). Declared unit/origin: weights-and-measures physically
> deposited in temples (antiquity); the modern canonical failure — *Mars Climate
> Orbiter* 1999 (pound-force read as newton). Decoding key / codec redundancy:
> Rosetta Stone (196 BC), deciphered via an external anchor — Champollion 1822.

## 4. Scientific recording: generating reliable knowledge

The way to turn exploration into reliable knowledge is the **scientific method** —
from Faraday and the 19th-century laboratory notebooks, not from computing.
Applied to a unit of work:

- **Hypothesis first** — declare what you expect (and what would refute it)
  **before** running. Otherwise the narrative adjusts to the result (post-hoc
  *storytelling*).
- **Immutable and reproducible record** — what was done can be redone by another
  from the record; once closed, it is not altered (redoing produces a new version,
  not an edit).
- **Honesty of result** — record what confirmed **and** what refuted; preserving
  the negative fights publication bias.
- **Explicit threats to validity** — does the result generalize? did it measure
  what it intended? does causality hold? does the statistic close?
- **Sober vocabulary** — describe what was observed ("lower by N in scenario X"),
  not the superlative ("amazing result"). A superlative is noise.

The canonical structure of a report (introduction → method → result → discussion)
is a **movement**, not a format: it serves an experiment as much as an article.
(The formalization — IMRaD — is in Part II.)

> **Adherence** (proportional to the axis of work — §9): the **core** is universal —
> honesty of result (recording also what refuted), sober vocabulary, and demarcating
> what is not known hold for any intellectual work. The **apparatus** — formal
> hypothesis-first, reproducible record, threats-to-validity, "does the statistic
> close?" — is conditional on **generating empirical/reproducible claims**; outside
> that axis, §4 holds by analogy, without guilt over hypotheses you do not have.

> **Grounding**: hypothesis declared beforehand / pre-registration — Nosek et al.
> 2018 (*PNAS*); reproducibility — Claerbout & Karrenbach 1992 (coins the term);
> threats to validity — Campbell & Stanley 1963; preserving the negative /
> publication bias — Rosenthal 1979 ("file drawer"); IMRaD structure — Sollaci &
> Pereira 2004. Tradition: laboratory notebooks (19th century).

## 5. Single source by altitude: knowledge, code, and data

**Every fact has a single canonical source.** The principle is not "do not repeat
text" — it is "all knowledge has a single authoritative representation". And there
is a division by **altitude**:

- The **how** (mechanics, flow) is best expressed in the doing itself (code,
  protocol, procedure) — it is not re-narrated in prose.
- The **example / contract / number / observation** lives in a **verifiable
  artifact that signals divergence** (a test, a measurement, a check) — you do not
  copy the expected value into prose, where it rots in silence.
- The **why** (intent, constraint, rejected alternative) is the **irreducible** —
  it lives only in prose, and is the only thing that justifies writing it.

**Admission test for any document** (STRONG): *if I delete this text, can I
regenerate it from the verifiable artifact?* If yes, do not write it — leave a
pointer. *And: if I delete the artifact, does this text suffice to remake it?* If
yes, it carries the why — keep it, short. Only prose that **fails** the first and
**passes** the second survives. The rest is drift waiting to happen.

**Single authority ≠ single instance** — the cut that avoids this section's most
common misunderstanding. The rule is about **logical authority**: a single
canonical voice per fact, which resolves **divergence** (two sources disagreeing →
drift). It does **not** forbid multiple **materializations** of the same truth:

- a **replica** verifiable-against-the-origin is not drift — it is what protects
  against *loss* (§10);
- a derived **re-expression** (summary, translation, formalization for another
  audience) is legitimate **if** it points to the canonical source and does **not**
  become a second authority.

The antipattern is only the copy that **pretends to be the source**. That is why
the admission test above measures duplication of **authority**, not of **content**.
It is the same cut (canonical voice ⊥ materialization) that reappears in access
(§3), in versioning (§8), and in the carrier (§10). **This is the parent principle
of the durability axis.**

> **Grounding**: single source (weave/tangle) — Knuth 1984 (*The Computer
> Journal*); the artifact does not contain its own correctness criterion (the
> oracle problem) — Weyuker 1982 (instantiated in software; the principle
> generalizes to all formal verification); intent under-specified by the procedure
> — Parnas & Clements 1986; DRY of knowledge — Hunt & Thomas 1999. Work ≠
> expression ≠ manifestation (derived re-expression ≠ authority duplication) —
> FRBR (*Functional Requirements for Bibliographic Records*), IFLA 1998 `[WEB ✓ 2026-06-03]`.

## 6. Source discipline: the epistemology of what you claim

Whoever works with knowledge — person or machine — tends to accept the first
plausible answer, worse still the one that confirms what was already believed.
Against this, principles older than any search engine:

- **Hierarchy of evidence** — strong evidence (replicated, primary) weighs more
  than opinion. Know which rung what you cite is on.
- **Primary > secondary > tertiary** — raw data / original source beats
  third-party analysis beats summary of a summary.
- **Recency vs authority** — in a fast-changing domain, the recent source beats
  the old; in a stable domain (mathematics, principles), the old remains
  canonical. Know which you are in.
- **Perishability of the datum** — every datum has a half-life. A principle lasts
  years; a price, hours. Do not treat them alike: a perishable datum requires
  **revalidation at the source** and a **stamp of when it was captured**.
- **Triangulation** — an important claim rests on independent sources.
- **Epistemic honesty** — distinguish what you **know**, **infer**, and **think**;
  **admitting a gap is worth more than inventing**; familiarity ("sounds right")
  is not truth.
- **Chesterton's fence** — do not discard what you do not understand: find out why
  it exists before removing it.

**Demarcating your own ignorance** is part of the discipline, not its opposite. A
mature body of knowledge draws the **boundary of what it covers** — silence
*outside* it is not denial, it is "not raised". And every void carries its **type**:
confirmed-absent ("I swept, it does not exist") ≠ pending ≠ unreadable ≠
out-of-scope. Treating all four as the same blank cell leads the reader — human or
agent — to **fill by assumption**. (Distinct from "admitting a gap" above: there it
is the confidence level *of a claim*; here it is the contour of what the corpus
deliberately *does not* cover.)

> **Adherence** (proportional to the exposure of the claim — §9): epistemic honesty
> (know/infer/think) and Chesterton's fence hold **always**, even solo. Hierarchy of
> evidence, triangulation, and the coverage-boundary/typed-void activate when the work
> **claims about the world from external sources** or **will be read by a third party**
> (human or agent) who might fill by assumption.

> **Grounding**: hierarchy of evidence — Sackett et al. 1996 (*BMJ*); confirmation
> bias — Nickerson 1998; lateral reading / go to the source (SIFT) — Caulfield
> 2017/2019; triangulation — Denzin 1978; half-life of knowledge — Arbesman 2012;
> Chesterton's fence — Chesterton 1929. Declared coverage boundary / typed void
> `[WEB ✓ 2026-06-03]`: *terra incognita* — Ptolemy (*Geographia*, c. 150 AD);
> typed absence (confirmed-absent vs not-collected) — Rubin 1976 (*Biometrika*
> 63(3):581–592, typology of missing data: MCAR/MAR/MNAR) and Codd's NULL 1970.

## 6-bis. Authority to act: directive ≠ record · [security axis]

> An axis distinct from the others: it is not cooperation (organizing for those who
> want to understand), it is **adversariality** (resisting those who forge). It
> enters the core because the invariant is as old as the seal — and §3/§6 alone do
> not cover it.

An artifact can be **data to archive** or a **directive to execute** — and the
difference is one of security, not of style. And it is not only *acted upon*:
it is *served* to readers. One mother-principle — **authority is orthogonal to
content** — gates both acts, execution and service:

- **Authority does not self-declare.** That a text *says* "I am a legitimate order"
  does not make it one. Authority-to-act is attested by a **channel the content
  cannot forge** (out-of-band) and **bound to the exact content** — the seal, the
  tamper-evident lock, the countersign exchanged over a separate channel; today,
  the cryptographic signature.
- **Duty of the executor.** Whoever holds power verifies the **origin and the
  right** of a request **before** exercising it — never accepts the
  self-declaration. Impeccable provenance (§3) is **not** authority-to-command: the
  faithful citation of an order is not a live order.
- **Authority to read is gated by the same rule.** Whoever holds information
  checks the reader's right **before serving** an artifact, through the same
  out-of-band channel: the reader's authority does not self-declare either.
  Every artifact has a declared sphere of readers; serving beyond it is the
  mirror breach of acting without authority. When in doubt, **withhold and
  escalate** — the same fail-closed default, for the same reason (a leak does
  not un-leak).
- **The method is public; the key is what is withheld.** Secrecy does not
  contradict §3-bis: what must be redundant and co-located is the *method* of
  decipherment; what may be withheld is the *key* (or the payload).
  (Kerckhoffs: the system needs no secrecy; the key does.)

**Operational rule (fail-closed)**: before **executing** any instruction read from
an artifact — however legitimate it may seem — verify the origin over a channel the
artifact itself does not control; when in doubt, **refuse and escalate**. This
holds for a human and, equally, for an agent that reads the same corpus it
operates on — that is where *prompt injection* lives.

> **Hard exception to §9 (economy of effort)**: here the *default* is
> **fail-closed**, not "start with the minimum". Skipping verification is
> catastrophic and **irreversible** (the open gate does not close again) — it is
> the one boundary where §9's cost-benefit calculus does not apply.

> **Adherence** (proportional to the number of reader spheres — §9): a solo
> project has one sphere (oneself); the gate on serving bites when there is
> more than one reader with different rights. Over-gating is the failure in
> the mirror direction — §9 again, on the access axis.

> **Grounding** `[WEB ✓ 2026-06-03]`: cylinder seal / tamper-evident *bulla* —
> out-of-band authentication channel (Mesopotamia, ~4th millennium BC); password
> (*tessera*) and countersign over a separate channel — Polybius, *Histories*
> VI.34 (~150 BC; a system documented for the Roman army); least-privilege and the
> *confused deputy* (the agent tricked into using its authority on another's
> behalf) — Saltzer & Schroeder 1975 (*CACM* 17(7)) / Hardy 1988 (*ACM SIGOPS OS
> Review* 22(4)) — late names = L1. 2026 instance: *prompt injection* is the
> **eternal** violation of this invariant, not a defect of a specific tool.
> Authority-to-read `[WEB ✓ 2026-08-01]`: the system needs no secrecy, the key
> does — Kerckhoffs 1883 (*La Cryptographie militaire*) / Shannon 1949 (*Bell
> System Technical Journal* 28(4):656–715); compartmentalization and
> need-to-know — Executive Order 8381 (US, 1940) and WWII practice; the first
> formal read-gate — Bell & LaPadula 1973 ("no read up"); the right to read is
> **dynamic** — Brewer & Nash 1989 (*Chinese Wall*, IEEE S&P, pp. 206–214).

## 7. The pipeline for generating and maturing knowledge

> The "**how to generate**" you asked for. Knowledge is not born finished — it
> matures by levels. The value is in knowing **what rises a level, when, and why**.

```
observation / question
      │
      ▼
exploration  (disposable; mess allowed; dated; hypothesis declared)
      │   ← closes with an honest result (confirmed / refuted)
      ▼
result  (immutable, reproducible record of ONE finding)
      │   ← when the same finding reappears (rule of three)
      ▼
consolidation  (findings from N explorations on a theme; stable knowledge)
      │   ← when it becomes a choice that affects the future
      ▼
decision  (immutable record + rationale; traceable; supersedable)
      │
      ▼
narrative  (the arc: links decisions and findings into a story that is understood)
```

**Maturation rules** (STRONG):
- Do not formalize what happened **once** — it is what drifts most. Leave it at
  the disposable level until it **recurs** (rule of three). Only then promote it.
- Rising a level is **rewriting**, not copying — the mature record is born clean,
  it does not inherit the mess of the exploration.
- What rises to the immutable level (a closed result, an accepted decision) **does
  not change again**: to continue, open a new one at the exploration level.
- **Collate the mature version against the source before closing.** Rewriting to
  clean up is right — but rewriting is the **noisiest** transmission (it passes
  through a mind that reinterprets). Check that the irreducible (the number, the
  claim, the why) survived, not just the style. Promoting without checking is
  copying without reviewing — the error enters in the *transfer*, not in the
  record at rest.

> **Adherence** (proportional to recurrence and to the life of the project — §9): the
> **rule of three** is itself the regulator — nothing rises a level without recurring
> (N≥3) and without the project lasting long enough for maturation to pay off. A
> one-off task, without evolution, legitimately lives only at the **exploration**
> level: not consolidating is the right behavior, not laziness.

> **Grounding**: rule of three (do not formalize at N=1) — Fowler 1999 (attrib.
> Don Roberts) `[WEB ✓]`; "throw the first one away" (exploration ≠ product) —
> Brooks 1975 (*Mythical Man-Month*). Ackoff 1989 (DIKW: data → information →
> knowledge → wisdom) provides analogical vocabulary, but DIKW is contested in
> information science (Frické 2009) and the pipeline above is not derived directly
> from it `[ANALOGY]`. Fidelity-re-reading on promotion `[WEB ✓ 2026-06-03]`:
> collation / textual criticism — Lachmann (1793–1851, stemmatic method, 19th
> century); high-fidelity proofreading in replication (DNA mismatch repair) —
> Modrich (Nobel in Chemistry 2015).

## 8. Versioning as immutable history and provenance

Versioning is a **principle**, not a tool: keeping an **auditable and recoverable
history** of the work — the mechanism that makes append-only (§3) practicable
across the whole workspace. (The tool that does it today is L2.)

- **State-recoverable history** — every past state can be recovered, compared, and
  marked (the physical implementation of append-only, §3). This **eliminates
  manual versioning**: never `report_v2`, `old_script`, `backup_of_the_date` — the
  history already does that, and manual copies pollute and drift. (Exception: an
  artifact that is declaredly immutable — an accepted decision, a closed
  experiment, a published version — where "v2" is a new formal record, not an
  informal backup.)
- **Signal vs noise** — what **defines** the work enters the record (the essence:
  sources, decisions, the irrecoverable); what is **regenerable** or
  **non-pertinent** stays out (what can be reconstructed from what entered). When
  something regenerable must exist, version **the way to recreate it**, not the
  product.
- **Separate the ephemeral from the canonical** — transient by-products (cache,
  environment, build) do not contaminate the record of the work. The same
  signal-vs-noise principle applied to the workspace.
- **Reproducibility as a test** — the proving question: *does another person, on
  another machine, reconstruct the work state in a few steps?* If not, there is an
  unrecorded implicit dependency — find and record it, or document it as a
  legitimate exception.

> **Adherence** (proportional to third-party reproduction and to the life of the work
> — §9): the proving question ("does another person, on another machine,
> reconstruct?") **is** the trigger — versioning bites when another needs to
> reconstruct the state or when the history has audit value. Solo-and-short does not
> require it in principle; applying it early is only because today it costs almost
> nothing (L2), not because of universality.

> **Grounding**: mechanism for a who/when/why history — Rochkind 1975 (see §3 for
> the append-only principle this §8 implements); reproducibility as a test —
> Claerbout & Karrenbach 1992; isolate what changes (kinship with modularity) —
> Parnas 1972.

## 9. Economy of effort: when to organize and when not to

Organizing has a **cost**. It is worth it when the gain compensates — and not
before.

| Not worth it (excess) | Worth it (pays off) |
|---|---|
| few artifacts, short life | many artifacts, long life |
| one person, days | collaboration (humans and/or machines) |
| disposable / proof of concept | months of duration; resuming is expensive |
| one-off task, no evolution | coming back wastes time reconstructing context |

**Symptom of excess**: spending more time organizing than working. Start with the
minimum that stops the immediate pain; grow only when you feel the lack.

**The regulator is the distance to the anticipated reader.** How much to declare,
how much to organize, how much to replicate — all scale with the **distance (in
time, space, context) of whoever will read**. An ephemeral note that only you read
today leaves the context implicit and does not pay for redundancy. But what a
successor (human or agent) will read in months declares the frame and disperses
copies. There it stops being overhead and becomes a condition for the artifact to
still **mean** (§3-bis) and **exist** (§10). It is the same shape as perishability
(§6) and durability (§10): organize **in proportion** to a variable, not in the
absolute. (The only exception: the security boundary §6-bis, where the *default* is
*fail-closed*, not "the minimum".)

**The other regulator is the genre of the work.** Proportionality is not only *how
much* to organize — it is *which standard* to demand. What counts as
"well-organized" depends on the **kind** of artifact: a **library** calls for
tests, packaging, and CI; a **lecture notebook, list, curation, or research
project** does not — demanding of them the software apparatus is the **same §9
excess along another axis** (low software-conformance ≠ defect). Before auditing or
acting, **name the genre and apply its standard**; do not demand what does not
apply. It is the same proportionality-to-relevance of Grice / Sperber-Wilson, here
about the *kind of work* rather than the distance to the reader.

> **Grounding**: organizing/optimizing too early does not pay off — Knuth 1974
> (*ACM Computing Surveys*, "premature optimization…"); not building what is not
> yet needed (YAGNI) — Beck (Extreme Programming); declaring/organizing in
> proportion to the distance to the receiver (relevance/proportionality) — Grice
> 1975 (*Logic and Conversation*, in Cole & Morgan eds.) / Sperber & Wilson 1986
> (*Relevance: Communication and Cognition*) `[WEB ✓ 2026-06-03]`.
>
> Era instance `[2026-06]` — asked the genre explicitly, AI readers apply the
> right standard and stop over-demanding (strong but circular signal):
> `lab/2026-06-04-strata-hipoteses/RESULTADOS-genero.md`.

## 10. Durability of the carrier: redundancy and dispersion

§8 teaches how to survive **editing** (recoverable history). What is missing is
the symmetric pair: surviving **loss**. These are orthogonal dangers — an authority
that drifts (two voices disagreeing) vs a carrier that dies (the only one there
was, gone).

**Single source ≠ single copy.** §5 mandates a single **logical authority** per
fact — to resolve **divergence**. This does **not** imply a single **physical
carrier**. Against **loss**, the invariant is the opposite: **N copies, dispersed
across substrates with independent failure modes**. Read literally, "do not copy"
would push toward a single point of failure — exactly what consumed the Library of
Alexandria and nearly erased Lucretius (who survived by **one** manuscript); and
what life has avoided for billions of years (multi-copy, redundancy).

The reconciliation is clean: redundancy never creates a second **truth**, only a
second **carrier of the same truth**. A replica that **knows itself derived** and
**verifies against the origin** (same content, same checksum) is a legitimate
*backup*, not the "copy that drifts" condemned in §8. Only the copy that
**pretends to be the source** is the antipattern.

- **Verifiable against the origin** — the replica proves it is still faithful
  (comparison, checksum); a copy nobody checks rots in silence.
- **Loss is the *default*; preserving is a verb** — without periodic
  reinvestment (re-copying, migrating substrate, **verifying integrity**) the
  natural trajectory of any record is disappearance. The carrier decays
  independently of whether the fact remains true — **physical** perishability,
  alongside the epistemic one of §6.

> **STRONG** (proportional to the intended life — §9): a short-lived ephemeral does
> not pay for redundancy; what needs to cross years demands dispersed and verified
> copies. There is no "store and forget"; there is "maintain, repeatedly, or lose".

> **Grounding** `[WEB ✓ 2026-06-03]`: *Lots Of Copies Keep Stuff Safe* — LOCKSS,
> Vicky Reich & David Rosenthal, Stanford 1999; redundancy and error correction —
> Shannon 1948 (*Bell System Technical Journal* 27) / von Neumann 1956 (*Automata
> Studies*); loss through lack of migration ("digital dark age") — Kuny 1997 (63rd
> IFLA General Conference, IFLA Publications); manuscript transmission as survival
> by dispersed copying — Reynolds & Wilson, *Scribes and Scholars: A Guide to the
> Transmission of Greek and Latin Literature* (Clarendon/Oxford, 1st ed. 1968; 4th
> ed. 2013).

## 11. Classification: form the scheme before organizing

§1 commands separation and §2 teaches finding — but both **presuppose an
already-formed scheme**: classes under one axis. **Forming the scheme is the
prior operation** — declaring the axis ("by which characteristic these
classes?") and dividing — and it is as old as organizing itself. It does not
repeat what the core already covers: the declared axis is the scheme's
rationale (§3), its revision is supersession (§3), and its warrant by the real
corpus is source discipline (§6). What this section adds to the repertoire are
the two rules those principles do not give:

- **Clean division** — on the same axis, classes are **mutually exclusive** and,
  together, **exhaustive**: each object has exactly one place, and no object is
  left placeless. Overlap produces "where do I put this?"; gaps produce "it
  does not fit" — the two symptoms of a sick scheme.
- **One axis is not enough → facets** — when the object carries several
  independent dimensions (type × time × authorship × genre), do not inflate the
  enumerative tree: declare facets and **synthesize** the position. It is the
  difference between enumerating every case (impossible) and generating the
  case on demand.

> **STRONG** (corollary of §4/§6): the object that does not fit is evidence
> **against the scheme**, not against the object — record it and revise the
> scheme; do not torture the object.

> **Adherence** (proportional to volume and to life — §9): three files do not
> call for a taxonomy — the pile will do. The formal scheme bites when the
> corpus grows, lasts, or will be read by a third party (human or agent) who
> cannot ask "where did you mean to put this?".

> **Grounding** `[WEB ✓ 2026-08-01]`: definition by nearest genus and specific
> difference — Aristotle, *Categories* (~4th c. BC) `[CANONICAL]`; the
> enumerative scheme and its limit — Dewey 1876 (*Decimal Classification*);
> scheme as consensus/domain hypothesis — Bliss 1929 (*The Organization of
> Knowledge and the System of the Sciences*); faceted analytico-synthetic
> classification — Ranganathan 1933 (*Colon Classification*, Madras Library
> Association); canons of division (exhaustiveness, exclusiveness) — Ranganathan
> 1937 (*Prolegomena to Library Classification*); facets in special schemes —
> Vickery 1960 (Classification Research Group) `[CANONICAL]`; *literary
> warrant* (the axis is warranted by the real corpus) — Svenonius 2000 (*The
> Intellectual Foundation of Information Organization*, MIT Press);
> domain-relative scheme — Hjørland & Albrechtsen 1995 (*JASIS* 46(6)); limit:
> classification is situated, not universal — Bowker & Star 1999 (*Sorting
> Things Out*, MIT Press) `[CANONICAL]`. Full development (hypothesis, internal
> evidence, threats): `lab/2026-08-01-fechamento-camadas/P1-classificacao.md`.

---

# PART II — CONSOLIDATED PATTERNS (L1)

> Each L0 need has **mature formalizations** that operationalize it. They are
> recommended and stable for decades — **but replaceable**. Here the mapping
> `L0 need → formalization`, always with the **change-signal**: when it makes sense
> to retire the *formalization* (never the *principle*).
>
> **How to read**: each entry = what it is · source · change-signal — the
> change-signal says **what replaces** the formalization (not *when to apply
> it*; proportionality of application is §9's Adherence). The **framework
> identities** were web-verified (2026-06-03) and re-verified against primary
> sources, with corrections, on 2026-08-01 — `[WEB ✓ date]` marks the latest
> verification; `[CANONICAL]` marks the established ones cited from knowledge.
> (Audit trail: `lab/2026-08-01-fechamento-camadas/L1-2-repesquisa-literatura.md`.)
> A principle (L0) is not swapped; a formalization (L1) is — when another fits the
> domain better, or when its overhead exceeds the gain at your scale (§9).

## For §1 — the three kinds, physically separated

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **Cookiecutter Data Science** | a standard layout that physically separates the three kinds of §1 — `notebooks/`≈exploration, `src/`+`reports/`≈product, `docs/`+`references/`≈knowledge | DrivenData (~2015) `[WEB ✓ 2026-08-01]` | the instance dies with the stack/domain; the pattern "separate the kinds in physical places" stays — the research compendium (For §4) is the academic expression |

## For §2 "How do I use / understand this?" — documentation

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **Diataxis** | 4 orthogonal doc types (tutorial / how-to / reference / explanation), organized by the reader's need, not the author's | Procida — diataxis.fr `[WEB ✓ 2026-08-01]` | if the 4-quadrant distinction does not fit the material (rare) |

## For §2 "Where is X?" — findability

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **Information architecture** | the discipline of organizing / labeling / navigating / searching content | Rosenfeld & Morville 1998 (1st ed.); 4th ed. w/ Arango 2015 `[WEB ✓ 2026-08-01]` | — (it is base theory; the *implementation* — map/index/entry — is L2) |

## For §3 — decisions + traceability

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **ADR** | a lightweight, immutable record, 1 decision per file, focused on the decision + context | Nygard 2011 `[WEB ✓ 2026-08-01]` | — (very stable format) |
| **MADR** (Markdown Any Decision Records) | community evolution of the ADR (template 4.0, 2024) | adr.github.io/madr `[WEB ✓ 2026-08-01]` | Y-Statement (Zimmermann) if you want 1 sentence; pure ADR-Nygard if you want minimal |
| **Conventional Commits / SemVer** | links each change to a type/meaning and to a version identity (commit→meaning→version trail) | conventionalcommits.org / semver.org `[WEB ✓ 2026-08-01]` | without a public release, commit hygiene suffices without the formal standard |

## For §3-bis — force of the artifact (type of act, reference frame, self-decodability)

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **ISAD(G)** (General International Standard Archival Description) | archival-description template operating §3-bis at institutional scale; its *conditions governing access* area records the **serving gate** (§6-bis) at the same scale | ICA, 2nd ed. 2000 `[WEB ✓ 2026-08-01]` | RiC-CM (Records in Contexts — official ICA successor, v1.0 late 2023); EAD for electronic exchange |
| **RFC 2119 / 8174 keywords** | requirement-level keywords (MUST / SHOULD / MAY) that mark the *force* of each statement — normative vs informative; the engineering-scale formalization of declaring the type of act | Bradner 1997 (RFC 2119); Leiba 2017 (RFC 8174) `[WEB ✓ 2026-08-01]` | — (stable since 1997; 8174 only clarifies that capitals alone carry the meaning) |
| **SI / ISO 80000** | international system of units and quantities — the formal *datum* of reference for science and engineering; operationalizes "declare the reference frame before measuring" | BIPM / ISO 80000 `[WEB ✓ 2026-08-01]` | EPSG/WGS84 for geodetic data; TAI/UTC for time; IEEE 754 for floating point |
| **PRONOM / DROID** | file-format registry (The National Archives UK) — identifies and documents codecs and formats for long-term self-decodability; the "dictionary" §3-bis requires be co-located | The National Archives UK — pronom.nationalarchives.gov.uk `[WEB ✓ 2026-08-01]` | relevant for long-term archiving; MIME-type (RFC 2046; IANA registry) suffices for the short term |

## For §4 — scientific recording

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **IMRaD** (template) | intro / method / result / discussion template for a report | Sollaci & Pereira 2004 `[WEB ✓ 2026-08-01]` | — (the 4 movements are L0; the template is flexible) |
| **Research Compendium** | a single container: article + analysis + data + environment, reproducible | Marwick, Boettiger & Mullen 2018 (*Am. Statistician* 72(1):80–88) `[WEB ✓ 2026-08-01]` | adapt the structure to your stack; the principle (everything together, reproducible) stays |
| **FAIR** (guiding principles) | Findable/Accessible/Interoperable/Reusable — the base principles for research *data* and digital objects; FAIR4RS is the software offspring | Wilkinson et al. 2016 (*Sci Data* 3:160018) `[WEB ✓ 2026-08-01]` | FAIR4RS for research software (next row); apply the subset your project publishes |
| **FAIR4RS** | Findable/Accessible/Interoperable/Reusable principles for research *software* | Barker et al. 2022 (*Sci Data* 9:622); RDA: Chue Hong et al. 2022 `[WEB ✓ 2026-08-01]` | apply only the subset your project publishes |
| **Pre-registration / Registered Reports** | declaring hypothesis + method before the data, formally | Nosek et al. 2018 / Chambers 2013; Chambers & Tzavella 2022 `[WEB ✓ 2026-08-01]` | an informal version (H1 in the experiment's README) suffices outside publication |
| **Research programmes** (hard core + protective belt) | a structure for a cross-experiment *registry* of hypotheses | Lakatos 1978 `[WEB ✓ 2026-08-01]` | any hypothesis table with status works; Lakatos gives the vocabulary |
| **Threats-to-validity** (checklist) | enumerate internal / external / construct / conclusion threats | Campbell & Stanley 1963 → Cook & Campbell 1979 / Wohlin et al. 2012 `[WEB ✓ 2026-08-01]` | — |

## For §5 — single source / oracle

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **Literate programming** | one source → doc (weave) + code (tangle), consistent by construction | Knuth 1984 `[WEB ✓ 2026-08-01]` | most use the weak version (docstrings + tests), not WEB |
| **Design by Contract** | pre/post-conditions + invariants = a self-checkable spec | Meyer 1997 `[WEB ✓ 2026-08-01]` | types + property-based tests cover much of it |
| **Specification by Example / living docs** | an automated example becomes an executable spec + single source | Adzic 2011 `[WEB ✓ 2026-08-01]` | — |
| **C4 model** | a single model of the system → views at 4 altitudes (consistency by construction) | Brown — c4model.com `[WEB ✓ 2026-08-01]` | any consistent context diagram works |

## For §6 — source discipline

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **Hierarchy of evidence / GRADE** | grade the strength of evidence | Sackett et al. 1996 / GRADE (Atkins et al. 2004; Guyatt et al. 2008) `[WEB ✓ 2026-08-01]` | — (L0 principle; GRADE is the formal grade) |
| **CRAAP test** | source-evaluation checklist (Currency / Relevance / Authority / Accuracy / Purpose) | Blakeslee 2004 `[WEB ✓ 2026-08-01]` | SIFT for fast web; CRAAP for academic sources |
| **SIFT** (Four Moves) | stop / investigate the source / find better coverage / trace to the origin | Caulfield 2019 (precursor 2017) `[WEB ✓ 2026-08-01]` | — |
| **Triangulation** | validate via N independent sources | Denzin 1978 `[WEB ✓ 2026-08-01]` | — |

## For §6-bis — authority to act **and to serve** (out-of-band channel, fail-closed)

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **PKI / X.509** | public-key infrastructure — the standard *out-of-band* channel: authority does not self-declare in the payload, it is certified by an external, verifiable chain of trust; operationalizes §6-bis in digital systems | RFC 5280 (IETF) `[WEB ✓ 2026-08-01]` | GPG web-of-trust without a hierarchical CA; JWT/PASETO change the token *format* — the out-of-band channel remains PKI |
| **Zero-trust / NIST SP 800-207** | "never trust, always verify" — no authority is assumed by position, network, or prior session; each executor verifies the channel independently | NIST SP 800-207 (2020) `[WEB ✓ 2026-08-01]` | BeyondCorp (Google) as a reference implementation; the principle (*verify, do not assume*) is L0 |
| **RBAC / ABAC** | access control by role or attribute — formalizes the §6-bis gate on **both** acts (executing and serving/reading); makes delegated authority explicit and auditable, without in-band self-declaration | RBAC: ANSI/INCITS 359-2004 (rev. 2012; NIST model — Ferraiolo et al. 2001); ABAC: NIST SP 800-162 (2014, updated 2019) `[WEB ✓ 2026-08-01]` | ABAC if role granularity is not enough; PBAC (policy-based) in advanced zero-trust contexts |

## For §7 — generation and maturation of knowledge

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **Zettelkasten** | atomic notes (1 idea) linked in a network; knowledge that is navigated | Ahrens 2017 (Luhmann's method) `[WEB ✓ 2026-08-01]` | good for heterogeneous knowledge; a hierarchical index suffices for low volume |
| **PARA** | organizing personal knowledge (Projects / Areas / Resources / Archives) | Forte 2022 `[WEB ✓ 2026-08-01]` | only if you manage knowledge beyond the project |
| **Rule of Three** | do not consolidate before the 3rd recurrence | Fowler 1999 (attrib. Roberts) `[WEB ✓ 2026-08-01]` | — |
| **Compendium / changelog / narrative** | consolidate findings, milestones (changelog), and the arc (project narrative) | conventions | choose the format by audience — changelog: see For §8 (Keep a Changelog); decision: see For §3 (ADR) |

## For §7 (cont.) — generating and prioritizing work from knowledge

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **Kanban** | workflow states + WIP limits | Anderson 2010 `[WEB ✓ 2026-08-01]` | Scrum (epic/story) if there are sprints; a simple list if solo |
| **OKR** | objectives + measurable key results | Grove 1983 (origin, Intel); Doerr 2018 `[WEB ✓ 2026-08-01]` | FAST goals / KPIs if OKR turns into quarterly theater |
| **MoSCoW** | Must / Should / Could / Won't prioritization | Clegg 1994 (Oracle UK); DSDM `[WEB ✓ 2026-08-01]` | Now/Next/Later, WSJF, etc. |

## For §8 — versioning / immutable history

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **Conventional Commits 1.0** | commit grammar → categorized change → automatic changelog | conventionalcommits.org `[WEB ✓ 2026-08-01]` | any consistent commit convention works |
| **SemVer 2.0 / Keep a Changelog** | version identity + changelog format | semver.org / keepachangelog.com `[WEB ✓ 2026-08-01]` | version by logical milestone if "release" is not the milestone |

## For §10 — durability of the carrier (verifiable redundancy, active preservation)

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **OAIS (ISO 14721)** | reference model for long-term digital preservation — defines roles (producer / archive / consumer), information packages (SIP/AIP/DIP), and the access-sustainability cycle; the conceptual anchor of any §10 strategy | ISO 14721:2012 / CCSDS 650.0-M-2 `[WEB ✓ 2026-08-01]` | — (it is the reference model; every digital-preservation formalization instantiates it) |
| **3-2-1 rule** | 3 copies, on 2 distinct media, 1 offsite — a minimal heuristic with independent failure modes; operationalizes §10's "N dispersed replicas" at any project scale | Krogh 2005/2009 (*The DAM Book*, O'Reilly); recommended by US-CERT (Ruggiero & Heckathorn 2012, CMU) `[WEB ✓ 2026-08-01]` | expand to **3-2-1-1-0** (+ 1 air-gapped + 0 verified errors) for critical data; LOCKSS for academic publications |
| **BagIt (RFC 8493)** | a package format for verifiable transfer and storage — an embedded checksum manifest, a self-declared payload; implements §10's *verifiable-against-origin* replica | RFC 8493 (IETF, 2018) / Library of Congress `[WEB ✓ 2026-08-01]` | git (with SHA-1/SHA-256 hashes) covers versioned code; BagIt for binary content or formal inter-institution transfer |
| **Fixity checking** | periodic integrity verification by hash (MD5/SHA-256) — operationalizes "preserving is a verb": without active re-verification, the copy rots in silence (bit rot) | NDSA Levels of Digital Preservation; Archivematica; standard digital-librarianship practice `[WEB ✓ 2026-08-01]` | automation via LOCKSS, rsync --checksum, or backup tools with embedded verification |

## For §11 — classification schemes

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **Enumerative schemes** (DDC, LCC) | pre-enumerated class trees under one axis; the default of large libraries | Dewey 1876 `[WEB ✓ 2026-08-01]` | the tree inflates and still misses cases → facets |
| **Faceted (analytico-synthetic)** | declare facets, synthesize the position on demand instead of enumerating it | Ranganathan 1933/1937; Vickery 1960 `[WEB ✓ 2026-08-01]` | overkill at low volume (§9 — see §11's Adherence) |
| **Domain-relative / literary warrant** | the axis is warranted by the real corpus and the domain's consensus, not by a universal scheme | Hjørland & Albrechtsen 1995; Svenonius 2000 `[WEB ✓ 2026-08-01]` | when the domain has no stable consensus, declare the axis as hypothesis (§4) |

## For publishing / making citable (external traceability — §3)

| Formalization | What it is | Source | Change-signal |
|---|---|---|---|
| **CITATION.cff** | machine-readable citation metadata | citation-file-format.github.io `[WEB ✓ 2026-08-01]` | CodeMeta if the ecosystem asks for JSON-LD |
| **Dublin Core / DataCite / schema.org** | interoperable metadata schemas (generic resources / research data / web) | datacite.org `[WEB ✓ 2026-08-01]` | DCAT for dataset catalogs; CodeMeta for software |
| **JOSS** | a peer-reviewed venue (journal + review criteria) for publishable research software | joss.theoj.org `[WEB ✓ 2026-08-01]` | SoftwareX / JORS as venues; Zenodo-DOI without a paper |

# PART III — ADAPTATION TO THE CURRENT ERA (L2)

> **A volatile, detachable layer.** How **today's** tools express the L0/L1.
> Everything here carries a `[2026-08-01]` capture and `re-verify-by: 2026-11-01`.
> **When a tool dies, only this part changes** — Parts I/II stay intact. Treat it
> as semi-live data (§6): re-verify at the source before treating it as truth.
>
> The **"expresses"** column ties each tool to a timeless need — it is what lets
> you swap it without losing the why. The AI layer below was web-verified on
> 2026-06-03 (modernization analysis in `Strata/lab/2026-06-03-modernizacao/` in
> the source repository) and re-verified on 2026-08-01
> (`lab/2026-08-01-fechamento-camadas/L2-2-ferramentas-ia.md`).

## 1. AI agents — today's form of the collaborator without memory

> **Expresses**: §2 (onboarding whoever arrives and does not know the project) +
> §3 (tracking who/what produced it) + layered memory. The "collaborator without
> memory between sessions" is timeless — a newly-arrived human is one too; the **AI
> agent is the 2026 instance**.

| Form (2026) | What it is | Expresses |
|---|---|---|
| **AGENTS.md** (+ `CLAUDE.md`) | an instruction file at the root: inventory + "before acting" checklist + a NEVER list | §2 entry point for the collaborator |
| **MCP** (Model Context Protocol) | a standard for connecting agent↔data/tools; expose `tickets`/`manifest`/dataset as a local server | §3 traceable access to resources |
| **Agent Skills** (`SKILL.md`) | a reusable packaged capability (progressive disclosure), cross-tool | repeatable operations (audit, promotion, export) |
| **Layered memory** | (1) versioned file · (2) agent-written auto memory (`MEMORY.md`, default-on) · (3) user-scope memory · (4) filesystem memory (memory tool, 1M context); hooks are **enforcement**, not a memory layer | the 4th layer of §3 (layers (2)+(4) generate opaque, unversioned drift — audit them) |
| **Context engineering + prompt caching** | curate > cram; route via the map; stable (cacheable) content before the volatile | §2 findability by routing |
| **Subagents / fan-out** | an orchestrator distributes N parallel subagents (they return summaries, do not dump context) | project review/audit are natural fan-outs |
| **Agent evals** | test AGENTS.md/Skills/hooks (they are prompts that silently regress) | §5 (the checkable becomes a test) |
| **Provenance / C2PA** | mark `authored-by: ai\|human\|mixed`; artifact signature | §3 authorship traceability |
| **Observability (OTel GenAI)** | traces/spans/tokens per agent session (semantic conventions still **Development** — pin the generation you use) | the machine complement of the diary/manifest (§3) |
| **grep-first search** | agents discover by grep/tree, not a vector DB; semantics (FTS5+sqlite-vec) only for a large corpus | §2 findability |

**State of the matrix (`[VERIFY: 2026-08-01]`)**: AGENTS.md is an **established**
standard (Agentic AI Foundation/Linux Foundation, 2025), native in
Codex/Copilot/Cursor/Gemini CLI/Aider/Windsurf/Zed; Claude Code auto-loads
`CLAUDE.md` (import AGENTS.md with `@AGENTS.md`). **Agent Skills** are now an
open **cross-tool** standard (agentskills.io, 2025; ~40 platforms) — audit
third-party skills like you audit MCP servers. **MCP**: current spec is
**2026-07-28** (stateless core; Roots/Sampling/Logging and the legacy HTTP+SSE
transport deprecated; governance under AAIF/Linux Foundation). **Security
(NEVER)**: an MCP server with write/action = an attack surface — least
privilege; an action with an external side effect requires approval. Marking
AI-generated content: **EU AI Act Art. 50 applies since 2-Aug-2026** and
requires machine-readable marking, but is **technology-neutral** (it names no
standard); C2PA 2.x (on its way to becoming **ISO 22144** — ISO/CD, still
under development) is today's de facto path — Layer 1 of the EU Code of
Practice on transparency of AI-generated content (Jun-2026). Systems placed on
the market before 2-Aug-2026 have until 2-Dec-2026 **for the Art. 50(2)
marking duty only** (Art. 111(4), Reg. (EU) 2026/1744).
`[re-verified: 2026-08-01]`

> **Boundary**: the *economy and routing* of AI resources (which model, local
> vs cloud, cost, caching strategy) belongs to the **Comporta** methodology —
> in research (`lab/2026-06-04-economia-ia-tokens/`). When distilled, this
> section **points** to it (ADR-005); the rows above stay about *expressing*
> timeless needs, not *pricing* them.

## 2. Editor / IDE — today's form of the working environment

> **Expresses**: the environment where knowledge is written, read, and navigated.
> VSCode (and Cursor, Zed, JetBrains…) are the 2026 form.

What matters for the method: the editor must **render** the knowledge (markdown,
clickable links, diagrams) and **integrate** wayfinding (map, search) and the
agent. Editor detail changes fast — **do not couple the method to a specific
editor** (knowledge is portable text/markdown, readable in any of them).

## 3. Version control — today's form of immutable history

> **Expresses**: §8 (immutable history, provenance, signal-vs-noise). git is the
> dominant 2026 form; the principles hold for mercurial/fossil/jj/successors.

| Form (2026) | Expresses | Note |
|---|---|---|
| **git** | §8 recoverable who/when/why history (successor to SCCS, 1975) | tool-agnostic; the syntax changes, the discipline stays |
| **`.gitignore`** | §8 signal vs noise (what is NOT versioned) | official github/gitignore templates |
| **Private / ignored paths** (`.gitignore`, private repos, ACLs) | §6-bis **authority-to-read** — retention by construction: what never enters the versioned surface cannot be served | not §8-noise: deliberate withholding; the sphere of readers is declared (frontmatter `audience:`), not implied |
| **Git LFS / DVC / lakeFS / Quilt** | §8 large irrecoverable files | only the irrecoverable enters; the recreation script enters |
| **Conventional Commits / SemVer / Keep a Changelog** | (L1, §8) the grammar of history | see Part II |
| **Signed commits / branch protection / CODEOWNERS** | §3 authorship + traceable collaboration | in a publishable/regulated project |

## 4. Filesystem — the physical instantiation

> **Expresses**: §1 (physical separation of artifact kinds) and §8's
> ephemeral-vs-canonical.

- **Folder structure** — an instantiation of §1 in the filesystem (e.g.: `src/`,
  `docs/{tutorials,how-to,reference,explanation}/` [Diataxis, L1], `docs/adr/`,
  `experiments/{dirty,clean}/`, `tickets/`, `data/{raw,interim,processed}/`
  [Cookiecutter DS, L1]). The names are **LOCAL**; the principle (separate kinds)
  is **L0**.
- **Caches and environments** — redirect the ephemeral (cache, venv, build) out of
  the working tree (`$XDG_CACHE_HOME`/`~/.cache/`, `%LOCALAPPDATA%`, or a dedicated
  folder like `Z:\caches\`). A clean working tree = §8. Per-tool detail (env vars
  `PIP_CACHE_DIR`, `CARGO_TARGET_DIR`, `HF_HOME`, etc.): each one's official docs.

## 5. External trackers (SaaS) — the corporate form of tracking

> **Expresses**: work management (L1: Kanban/OKR/MoSCoW) when the organization
> requires a corporate tool (Jira/Linear/Monday/etc.).

- The **canonical** (markdown+git) is the source of truth; the tracker is a
  **destination**.
- **One-way bridge** (export canonical → CSV/API). Bidirectional generates a dual
  source of truth and drift.
- Retroactive cards: always link versioned evidence (commit/ADR/EXP) — without it,
  it is fiction.

## Re-verification (this part is semi-live)

At each audit (or at the `re-verify-by`), check at the source. The **AI** tool
matrix is the highest-cadence one (AGENTS.md/MCP/Skills/memory). If an item in
this part becomes false, **correct only here** — the L0/L1 does not change. This is
the living proof of the layers thesis: the foundation (Parts I/II, from Pacioli
1494 to classical engineering) remains while the form (Part III) is swapped.

---

> **State**: Parts I (L0), II (L1), and III (L2) are written. The citations live
> inline (Grounding in the L0; source + change-signal in the L1; capture +
> re-verify in the L2); a consolidated bibliography per layer is an optional next
> step.
>
> **The layer names** — **Mneme** (memory, L0), **Morfé** (form, L1), **Órganon**
> (instrument, L2) — and the precedent for stratification-by-durability (*pace
> layering*, Brand 1999) are in the **[glossary](../GLOSSARIO.md)**, with the
> etymology and the source caveats.
>
> **Open items**:
> - **Axis 5 (security/adversariality)**: §6-bis now gates **both** acts
>   (executing and serving); the axis still deserves its own sweep on the
>   **evidence** side (today: completion-only signal).
> - **Part IV — Adoption and operation**: the brownfield path (how to adapt an
>   existing project) is a known gap; it awaits empirical recurrence (N≥3) to
>   formalize.
