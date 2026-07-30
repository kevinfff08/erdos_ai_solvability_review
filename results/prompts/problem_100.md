# Erdős Problem 100: planar diameter under separated distance values

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(A\subset\mathbb R^2\) be finite. Define
\[
D(A)=\{\lVert x-y\rVert:x,y\in A,\ x\ne y\},\qquad
\operatorname{diam}(A)=\max D(A).
\]
Call \(A\) *admissible* when:

1. \(\lVert x-y\rVert\ge 1\) for every distinct \(x,y\in A\);
2. whenever \(a,b\in D(A)\) and \(a\ne b\), \(|a-b|\ge1\).

Repeated distances are allowed: condition 2 concerns different numerical distance values, not different pairs of points.

Prove or disprove the following exact target:
\[
\exists c>0\ \exists n_0\in\mathbb N\ \forall n\ge n_0\ \forall A\subset\mathbb R^2,
\quad |A|=n\text{ and }A\text{ admissible}\implies \operatorname{diam}(A)\ge cn.
\]

Equivalently, the minimum diameter of admissible \(n\)-point planar sets is \(\Omega(n)\). All constants must be absolute and independent of \(A\) and \(n\).

## Frozen mathematical background

- [Guth and Katz (Annals of Mathematics, 2015)](https://annals.math.princeton.edu/2015/181-1/p02) proved that every \(n\)-point planar set determines \(\Omega(n/\log n)\) distinct distances. For an admissible \(A\), if \(d_1<\cdots<d_m\) are its distinct values, then \(d_1\ge1\) and \(d_{i+1}-d_i\ge1\), so \(\operatorname{diam}(A)=d_m\ge m\). Hence \(\operatorname{diam}(A)=\Omega(n/\log n)\). This deduction is accepted background, not the desired result.
- [Brass (Discrete Mathematics, 1996)](https://www.sciencedirect.com/science/article/pii/0012365X9500208E) records the stronger eventual \(n-1\) conjecture and proves an asymptotic version for sets contained in a parallel half-strip. This is a restricted-case theorem, not a reduction of the general problem.
- The database records a Kanold \(n^{3/4}\) bound and a Piepmeyer 9-point example of diameter \(<5\), but their original proofs/construction data must be independently checked before being used.
- [Ho (arXiv:2604.15305, 2026)](https://arxiv.org/abs/2604.15305) gives a high-dimensional counterexample to a different, dimension-growing quadratic conjecture. It neither proves nor disproves the fixed planar target.

The stronger statement \(\operatorname{diam}(A)\ge n-1\) for all sufficiently large \(n\) is a conjectural variant. Do not state or use it as an accepted theorem.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that there exist absolute constants c>0 and n0 such that every admissible A⊂R² with |A|=n≥n0 satisfies diam(A)≥cn.

**Negative obligation.** Construct admissible planar sets A_j with |A_j|=n_j→∞ and diam(A_j)/n_j→0; equivalently, for every c>0 and N there exist n≥N and an admissible n-point set A with diam(A)<cn.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a rigorous proof of absolute \(c>0,n_0\) satisfying the canonical target for every admissible planar set.

A negative resolution is a rigorous infinite family \(A_j\subset\mathbb R^2\) of admissible sets with \(|A_j|=n_j\to\infty\) and
\[
\operatorname{diam}(A_j)/n_j\to0.
\]

These are genuine logical alternatives. A counterexample to the stronger eventual \(n-1\) assertion alone is not a negative resolution of the canonical target.

## What does not count as a solution

- Repeating the \(\Omega(n/\log n)\) lower bound, or obtaining another still-sublinear lower bound.
- A finite search, a floating-point configuration, or a collection of examples without exact certification of all distance inequalities.
- A theorem restricted to a line, a half-strip, convex position, or any subclass unless a proved reduction covers all admissible sets.
- Treating all unordered pairs as having distinct lengths; equal lengths may occur arbitrarily often.
- A claim based solely on an unreviewed web post, an uncompiled formalization, or a citation not inspected for its exact hypotheses.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State every quantifier and prove that all asymptotic constants are uniform in \(A\) and \(n\).
2. Keep the minimum interpoint-distance hypothesis separate from the separation of distinct distance values.
3. Whenever distances are sorted, prove the sorting covers every realized value and that the largest one equals the Euclidean diameter.
4. For a positive proof, isolate the new lemma that removes the logarithmic loss and check that it applies to repeated distances.
5. For a negative construction, certify cardinality, planarity, minimum distance, every distinct-value gap, diameter, and the limiting sublinear ratio.
6. Audit every imported theorem against its exact dimension, normalization, strict/non-strict inequalities, and quantifier order.
7. Before relying on Kanold, Piepmeyer, or any Lean claim, obtain the primary source or run the pinned formal development and record the result.

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
