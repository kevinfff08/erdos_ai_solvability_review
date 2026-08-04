# Erdős Problem 885: Common factor-difference sets

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-08-04. Treat the canonical target and frozen background below as settled inputs. Do not investigate whether the problem is open, and do not produce a literature survey, status report, or bibliography expansion. Work directly on the mathematics.

The task is complete only when a rigorous proof or rigorous disproof of the canonical target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, plans, and checkpoints are research material, not completion. Inspect an external source only when an active proof step requires the exact hypotheses of a named theorem, then return immediately to the proof.

## Definitions and canonical target

For n>=1 define D(n)={|a-b|: a,b are positive integers and ab=n}. Prove or disprove that for every k>=1 there exist distinct integers N_1<...<N_k with |D(N_1)∩...∩D(N_k)|>=k.

## Frozen mathematical background

- k=2 成立。
- k=3 成立。
- k=4 成立。

Audited sources for this background:

- [Erdős Problem 885](https://www.erdosproblems.com/885) — audited database record.

Do not reinterpret a theorem, conjecture, computation, forum claim, or preprint as having stronger evidential status than stated here.

## Exact unresolved core

建立对任意 k 可扩展的共同因子差构造，或证明某个 k 不可能。

**Affirmative obligation.** Give a construction valid for every k and prove all N_i are distinct positive integers and at least k explicitly identified differences lie in every D(N_i).

**Negative obligation.** Give a specific k and prove that no k integers can have k common factor differences.

Close this exact mathematical gap. Rechecking database status, extending the bibliography, restating the gap, or proposing methods does not address it.

## Complete resolution criteria

A complete solution must satisfy one of the two obligations above with all definitions and quantifiers exactly as stated. Every imported theorem must be quoted with its full hypotheses and applied explicitly. Every new lemma must have a complete proof. A disproof must include a counterexample or infinite family with a self-contained certificate of every required property.

## What does not count as a solution

- Another isolated construction for fixed small k.
- Numerical examples without a scalable proof.
- Counting repeated or signed differences as distinct.
- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of difficulty.
- A proof sketch, computation, or intermediate lemma presented as completion.
- A voluntary `CHECKPOINT_NOT_FINAL` while execution resources remain available.

## Required correctness checks

1. Require positive integer factor pairs.
2. Verify the same k distinct differences work for every N_i.
3. Do not infer global novelty from absence in the frozen sources.
4. Verify that the final theorem is logically identical to the canonical target and has not strengthened hypotheses or weakened conclusions.
5. Distinguish finite evidence from universal proof and theorem from conjecture.
6. If using an external theorem, record its exact statement, version, and applicability at the point of use.

## Required research package

Create a coherent, self-contained research package. Choose a directory layout suited to the mathematics, but preserve enough structure that another researcher can trace each final claim to its proof, source, computation, and adversarial check.

### Mandatory paper: `paper.tex`

Produce a journal-style mathematical paper containing a title and abstract; the canonical problem and all definitions; only the frozen background actually used; a precise statement of every claimed contribution; complete proofs of every lemma and main theorem or counterexample; a comparison between frozen background and newly established results; an accurate final resolution statement; and complete citations for every external result used.

All references must be archived with the package, either embedded in `paper.tex` or in an included `references.bib`. The paper must contain no placeholders, omitted proof steps, or claims supported only by separate notes.

### Mandatory final audit: `audit.md`

Produce an independent adversarial audit of `paper.tex`. It must check exact agreement with the canonical target; every quantifier, boundary and equality case; the dependency chain of each nontrivial lemma; circularity and hidden assumptions; applicability of external theorems; the exact force of any computation; citation support; and whether each asserted new result is genuinely beyond the frozen background.

The audit must end with exactly one verdict:

- `COMPLETE_SOLUTION_VERIFIED`;
- `COMPLETE_DISPROOF_VERIFIED`; or
- `CHECKPOINT_NOT_FINAL`.

Only the first two count as completion.

### Intermediate research archive

Reasonably archive proof drafts, proved and refuted lemmas, dependency notes, adversarial reviews, failed routes with exact failure points, computation code, exact certificates, test outputs, and the current research state. The final paper may not depend on an unarchived argument or calculation.

### LaTeX and PDF check

Compile `paper.tex` successfully and retain `paper.pdf`. All citations and cross-references must resolve and there must be no fatal LaTeX error. Successful compilation and an openable PDF are sufficient: do not perform page-by-page screenshot inspection, do not create visual-validation images, and do not add images, figures, diagrams, or a graphical abstract.

## Dynamic Multiagent constraints

Choose mathematical approaches, delegation, coordination, and changes of direction autonomously. Do not impose fixed roles, named stages, prescribed proof methods, or a predetermined sequence. Including the root agent, use at most four concurrent agents.

The following are prohibited:

- assigning any agent to investigate whether the problem is open or to conduct a general literature survey;
- allowing source management, status tracking, or process documentation to consume the main effort;
- substituting a plan or list of approaches for mathematical derivation;
- duplicating the same route without a concrete adversarial purpose;
- recording conjectures or proof sketches as proved lemmas;
- starting computation without a precise claim, hypotheses, finite scope, certificate format, and stopping condition;
- using finite computation or numerical evidence as a substitute for universal proof;
- declaring completion without independent adversarial checking of the actual proof;
- voluntarily stopping because the problem is difficult, initial routes failed, or only intermediate results were obtained.

## Persistence and external-interruption behavior

Continue mathematical research while execution resources remain available. Do not end merely because several approaches fail, a paper draft exists, or the remaining gap has been identified. Autonomously repair, combine, replace, or abandon approaches as the mathematics requires.

Use `CHECKPOINT_NOT_FINAL` only when an external runtime, context, or system boundary forces interruption. On forced interruption preserve `paper.tex`, `audit.md`, verified results, unresolved obligations, failed routes, computations, certificates, and a clear resumable state. Never convert interruption into a solution claim.
