# Erdős Problem 106: arbitrary-orientation square packing

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For each positive integer \(k\), consider exactly \(k^2+1\) Euclidean squares \(Q_1,\ldots,Q_{k^2+1}\) of positive side lengths \(s_1,\ldots,s_{k^2+1}\). Each square is contained in the closed unit square \([0,1]^2\); its orientation is arbitrary. Their interiors are pairwise disjoint, while boundary contacts between squares and with \(\partial[0,1]^2\) are allowed.

Define
\[
f(n):=\sup\{\sum_{i=1}^{n}s_i: (Q_i)_{i=1}^n\text{ is such a packing in }[0,1]^2\}.
\]

Canonical target: prove or disprove
\[
\forall k\in\mathbb Z_{>0},\qquad f(k^2+1)=k.
\]

The lower bound is already known: start with the \(k\times k\) grid of side \(1/k\), remove one tile, and insert two side-\(1/(2k)\) squares. Thus the sole affirmative burden is the universal upper bound \(\sum_i s_i\le k\). Do not impose axis parallelism unless explicitly proving a restricted lemma.

## Frozen mathematical background

- By area and Cauchy–Schwarz, \(f(k^2)=k\): \(\sum s_i^2\le1\) and \((\sum s_i)^2\le k^2\sum s_i^2\). This does not prove the target with \(k^2+1\) squares.
- Halász gave neighboring-parameter lower-bound constructions in 1984: [paper and abstract](https://www.sciencedirect.com/science/article/pii/0097316584900244).
- Erdős–Soifer and Campbell–Staton conjectured the more general formula \(f(k^2+2c+1)=k+c/k\) for \(-k<c<k\); Campbell–Staton is [here](https://www.tandfonline.com/doi/abs/10.1080/00029890.2005.11920180). Praton showed that validity for one \(c\) implies validity for all \(c\), so the general formulation is equivalent to the target; see [arXiv:math/0504341](https://arxiv.org/abs/math/0504341) and the [2008 published version](https://www.tandfonline.com/doi/abs/10.1080/0025570X.2008.11953576).
- The axis-parallel analogue \(g\), in which every small-square side is parallel to an outer-square side, is solved: \(g(k^2+2c+1)=k+c/k\) for \(-k<c<k\). This is not the target. See Baek–Koizumi–Ueoro, [arXiv:2411.07274](https://arxiv.org/abs/2411.07274).
- Singh proves that the target is equivalent to its holding for infinitely many \(k\), and to convergence of \(\sum_{k\ge1}(f(k^2+1)-k)\); it remains an open target in that paper. See [arXiv:2601.22163](https://arxiv.org/abs/2601.22163).

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete affirmative resolution is a proof that for every positive integer k and every packing of exactly k^2+1 positive-side-length, arbitrarily oriented squares with pairwise disjoint interiors in [0,1]^2, the total side length is at most k. Together with the explicit grid-splitting construction, this proves f(k^2+1)=k for all k.

**Negative obligation.** A complete negative resolution is one explicit positive integer k and a rigorously verified packing of exactly k^2+1 such squares in [0,1]^2 whose total side length is strictly greater than k. The certificate must give exact or rigorously bounded coordinates, orientations, side lengths, containment, and pairwise interior-disjointness checks.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution requires a rigorous proof that every allowed packing of \(k^2+1\) squares has total side length at most \(k\), for every positive integer \(k\). Combine it with the stated construction to obtain equality.

A negative resolution requires one explicit integer \(k\) and a certified packing of exactly \(k^2+1\) positive-side-length, arbitrarily oriented squares in \([0,1]^2\) with total side length strictly greater than \(k\). Supply exact algebraic/rational data or rigorously validated interval data for every side length, vertex, orientation, containment inequality, and pairwise interior-disjointness condition.

## What does not count as a solution

- A proof only for the axis-parallel quantity \(g\).
- A finite list of checked \(k\), a floating-point optimizer output, a drawing, or an uncertified numerical search.
- A lower-bound construction of total \(k\) without the global upper bound.
- An asymptotic upper bound \(k+o(1)\), a bound with a positive error, or an area argument that does not handle \(k^2+1\).
- A proof for tilings, congruent squares, disjoint closed squares, or another strengthened/restricted model unless it is explicitly and rigorously reduced to the canonical target.
- Restating the equivalent series criterion without proving convergence or divergence.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State exactly where arbitrary orientations enter every lemma; audit every use of horizontal/vertical projections, grid lines, or coordinate-wise disjointness.
2. Preserve the quantifier \(\forall k\ge1\), exact count \(k^2+1\), and strictly positive side lengths.
3. Check containment for rotated squares using the full square geometry, not axis-aligned bounding boxes alone.
4. Check pairwise disjoint interiors, including boundary-touching and degenerating sequences.
5. If taking an extremal packing, justify maximum attainment or formulate the proof for suprema and pass to limits rigorously.
6. For any claimed counterexample, independently certify strict surplus and every non-overlap constraint.
7. Compare each claimed use of the 2024 axis-parallel proof against the point where axis parallelism is essential.
8. Label every cited claim as theorem, conjecture, construction, or deduction; cite primary sources with stable URLs.

If the proof uses an external theorem not fully stated in the frozen background, record its exact hypotheses and verify that they apply. Do not expand this local dependency check into a general literature or open-status investigation.

## Required research package

Create a coherent, self-contained research package. Choose the directory layout that best fits the mathematics, but preserve enough structure that another researcher can trace every final claim to its proof, computation, source, and adversarial check.

### Mandatory paper: `paper.tex`

Produce a journal-style mathematical paper containing:

- a title and abstract;
- the canonical problem and all definitions needed to read the paper independently;
- the frozen background actually used;
- a precise statement of every claimed contribution;
- complete proofs of all lemmas and the main theorem or counterexample;
- a clear comparison between the frozen background and what was newly established;
- an accurate final statement of whether the canonical target has been proved or disproved;
- complete citations for every external result used.

All references must be part of the archived package. They may be embedded in `paper.tex` or stored in an included `references.bib`; no citation may depend on a missing external bibliography file. The paper must not contain placeholders, omitted proof steps, or claims supported only by notes elsewhere in the package.

### Mandatory final audit: `audit.md`

Produce an independent adversarial audit of the final `paper.tex`. It must check:

- exact agreement between the paper's main claim and the canonical target;
- every quantifier, parameter dependence, boundary case, equality case, and uniformity requirement;
- the full dependency chain of every nontrivial lemma;
- possible circular reasoning, hidden assumptions, and illicit weakening of the target;
- exact applicability of every external theorem used;
- whether computational evidence proves only the finite statement claimed for it;
- whether citations support the statements attributed to them;
- whether every asserted new result is actually beyond the frozen background;
- whether the final solution claim is justified.

The audit must end with exactly one verdict:

- `COMPLETE_SOLUTION_VERIFIED`;
- `COMPLETE_DISPROOF_VERIFIED`; or
- `CHECKPOINT_NOT_FINAL`.

Only the first two verdicts count as completion.

### Intermediate research archive

Reasonably archive all intermediate material that matters to verification or resumption, such as proof drafts, proved and refuted lemmas, dependency notes, adversarial reviews, failed routes with exact failure points, computation code, exact certificates, test outputs, and the current research state. Filenames and subdirectories are flexible; organization, traceability, and resumability are mandatory. Do not allow the final paper to depend on an unarchived calculation or argument.

### LaTeX and PDF check

Compile `paper.tex` successfully and retain the resulting `paper.pdf`. All citations and cross-references must resolve, and there must be no fatal LaTeX errors. Successful compilation and an openable PDF are sufficient: do not perform page-by-page screenshot inspection, do not create visual-validation images, and do not add images, figures, diagrams, or a graphical abstract to the paper.

## Dynamic Multiagent constraints

Choose mathematical approaches, delegation, coordination, and changes of direction autonomously. Do not impose fixed roles, named stages, prescribed proof methods, or a predetermined sequence of work. Including the root agent, use at most four concurrent agents.

The following are prohibited:

- assigning any agent to investigate whether the problem is open;
- assigning a general literature survey or publication-status review;
- maintaining a long-running source-collection role disconnected from an active proof obligation;
- substituting a research plan, list of approaches, or organizational work for mathematical derivation;
- duplicating the same route across agents without a concrete adversarial or comparative purpose;
- recording a conjecture or proof sketch as a proved lemma;
- starting computation without a precise mathematical claim, hypotheses, finite scope, certificate format, and stopping condition;
- using finite computation or numerical evidence as a substitute for a universal proof;
- declaring a complete solution without independent adversarial checking of the actual proof;
- voluntarily stopping because the problem is difficult, initial routes failed, or only intermediate results have been obtained;
- allowing source management, status tracking, or process documentation to consume the main research effort.

Inspect an external source only when an active proof step requires the exact statement of a named theorem. Record the theorem and its hypotheses, check that they apply, and return to the mathematics.

## Persistence and external-interruption behavior

Continue mathematical research while execution resources remain available. Do not end the task merely because several approaches fail, a complete proof has not yet emerged, intermediate lemmas have been found, a paper draft exists, or the remaining gap has been identified. Autonomously repair, replace, combine, or abandon approaches as the mathematics requires.

Use `CHECKPOINT_NOT_FINAL` only when an external runtime, context, or system boundary forces interruption. It is not a voluntary completion option. On forced interruption, preserve the current `paper.tex`, `audit.md`, all verified results, unresolved proof obligations, failed routes with exact failure points, computations and certificates, and a clear resumable research state. Never convert an interrupted investigation into a solution claim.
