# Erdős Problem 503: Euclidean isosceles sets

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-08-04. Treat the canonical target and frozen background below as settled inputs. Do not investigate whether the problem is open, and do not produce a literature survey, status report, or bibliography expansion. Work directly on the mathematics.

The task is complete only when a rigorous proof or rigorous disproof of the canonical target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, plans, and checkpoints are research material, not completion. Inspect an external source only when an active proof step requires the exact hypotheses of a named theorem, then return immediately to the proof.

## Definitions and canonical target

For each d>=1, determine f(d), the maximum cardinality of a finite set S subset R^d such that every three distinct points of S determine at most two nonzero distances. A current unrefereed reduction claims f(d)=max{g(d),s(d)+1,s(d-1)+3}; it may be used only after its proof is independently audited.

## Frozen mathematical background

- 二维与三维精确值分别为 6、8。
- 一般上界 f(d)≤C(d+2,2)，下界至少 C(d+1,2)+1。
- 2026 修订笔记声称精确约化到欧氏/球面二距离极值函数。

Audited sources for this background:

- [Problem 503 discussion thread](https://www.erdosproblems.com/forum/thread/503) — informal_claim.
- [Euclidean isosceles sets and two-distance extremal functions](https://www.ulam.ai/research/erdos503-final.pdf) — preprint.

Do not reinterpret a theorem, conjecture, computation, forum claim, or preprint as having stronger evidential status than stated here.

## Exact unresolved core

独立核验或修正该约化，并进一步决定仍未知的 g(d)、s(d) 组合所给出的 f(d)。

**Affirmative obligation.** Give a complete proof determining f(d) for every d, or rigorously establish the stated reduction and close every remaining extremal term needed to make f(d) explicit.

**Negative obligation.** Refute the current reduction by an explicit configuration or a proved logical gap that survives the revised note, then provide the correct extremal statement if claiming resolution.

Close this exact mathematical gap. Rechecking database status, extending the bibliography, restating the gap, or proposing methods does not address it.

## Complete resolution criteria

A complete solution must satisfy one of the two obligations above with all definitions and quantifiers exactly as stated. Every imported theorem must be quoted with its full hypotheses and applied explicitly. Every new lemma must have a complete proof. A disproof must include a counterexample or infinite family with a self-contained certificate of every required property.

## What does not count as a solution

- Quoting the revised note without auditing it.
- Determining only finitely many dimensions.
- Repeating Blokhuis's upper bound.
- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of difficulty.
- A proof sketch, computation, or intermediate lemma presented as completion.
- A voluntary `CHECKPOINT_NOT_FINAL` while execution resources remain available.

## Required correctness checks

1. Use Ionin's correct condition |S_i|>=2, not >=3.
2. Separate at-most-two from exactly-two distance conventions.
3. Check affine dimension and spherical-center assumptions in the two-point block case.
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
