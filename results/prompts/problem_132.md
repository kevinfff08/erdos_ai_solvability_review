# Erdős Problem 132: Low-multiplicity planar distances

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-08-04. Treat the canonical target and frozen background below as settled inputs. Do not investigate whether the problem is open, and do not produce a literature survey, status report, or bibliography expansion. Work directly on the mathematics.

The task is complete only when a rigorous proof or rigorous disproof of the canonical target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, plans, and checkpoints are research material, not completion. Inspect an external source only when an active proof step requires the exact hypotheses of a named theorem, then return immediately to the proof.

## Definitions and canonical target

For every sufficiently large n and every set A of n distinct points in R^2, must at least two positive distances determined by A each occur among at most n unordered pairs? More strongly, does the number of positive distances of multiplicity at most n tend to infinity uniformly over all n-point sets?

## Frozen mathematical background

- 最大距离的重数至多 n。
- n=5,6 时至少两种低重数距离。
- 凸位置点集满足至少两种低重数距离。

Audited sources for this background:

- [On multiplicities of interpoint distances](https://arxiv.org/abs/2505.04283) — preprint.

Do not reinterpret a theorem, conjecture, computation, forum claim, or preprint as having stronger evidential status than stated here.

## Exact unresolved core

证明一般 n 点集至少有第二种重数≤n 的距离；更强地证明此类距离数一致趋于无穷。

**Affirmative obligation.** Prove the two-distance assertion for every n>=5 (or all sufficiently large n with the finite remaining cases separately certified), or prove the stronger uniform divergence statement.

**Negative obligation.** Give a rigorously specified infinite family of n-point configurations with at most one positive distance of multiplicity at most n, or with a uniformly bounded number of such distances.

Close this exact mathematical gap. Rechecking database status, extending the bibliography, restating the gap, or proposing methods does not address it.

## Complete resolution criteria

A complete solution must satisfy one of the two obligations above with all definitions and quantifiers exactly as stated. Every imported theorem must be quoted with its full hypotheses and applied explicitly. Every new lemma must have a complete proof. A disproof must include a counterexample or infinite family with a self-contained certificate of every required property.

## What does not count as a solution

- The Hopf–Pannwitz longest-distance theorem alone.
- A proof restricted to convex position.
- Checking finitely many configurations or only n=5,6.
- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of difficulty.
- A proof sketch, computation, or intermediate lemma presented as completion.
- A voluntary `CHECKPOINT_NOT_FINAL` while execution resources remain available.

## Required correctness checks

1. Count unordered pairs once.
2. Exclude zero distances by requiring distinct points.
3. Do not infer the second distance from the longest-distance bound.
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
