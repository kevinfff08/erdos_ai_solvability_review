# Erdős Problem 100: planar diameter under separated distance values

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

## Accepted background

- The current [Erdős Problems record](https://www.erdosproblems.com/100) lists this as open; treat that label as evidence, not as a proof of current status.
- [Guth and Katz (Annals of Mathematics, 2015)](https://annals.math.princeton.edu/2015/181-1/p02) proved that every \(n\)-point planar set determines \(\Omega(n/\log n)\) distinct distances. For an admissible \(A\), if \(d_1<\cdots<d_m\) are its distinct values, then \(d_1\ge1\) and \(d_{i+1}-d_i\ge1\), so \(\operatorname{diam}(A)=d_m\ge m\). Hence \(\operatorname{diam}(A)=\Omega(n/\log n)\). This deduction is accepted background, not the desired result.
- [Brass (Discrete Mathematics, 1996)](https://www.sciencedirect.com/science/article/pii/0012365X9500208E) records the stronger eventual \(n-1\) conjecture and proves an asymptotic version for sets contained in a parallel half-strip. This is a restricted-case theorem, not a reduction of the general problem.
- The database records a Kanold \(n^{3/4}\) bound and a Piepmeyer 9-point example of diameter \(<5\), but their original proofs/construction data must be independently checked before being used.
- [Ho (arXiv:2604.15305, 2026)](https://arxiv.org/abs/2604.15305) gives a high-dimensional counterexample to a different, dimension-growing quadratic conjecture. It neither proves nor disproves the fixed planar target.

The stronger statement \(\operatorname{diam}(A)\ge n-1\) for all sufficiently large \(n\) is a conjectural variant. Do not state or use it as an accepted theorem.

## Complete resolutions

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

## Required correctness checks

1. State every quantifier and prove that all asymptotic constants are uniform in \(A\) and \(n\).
2. Keep the minimum interpoint-distance hypothesis separate from the separation of distinct distance values.
3. Whenever distances are sorted, prove the sorting covers every realized value and that the largest one equals the Euclidean diameter.
4. For a positive proof, isolate the new lemma that removes the logarithmic loss and check that it applies to repeated distances.
5. For a negative construction, certify cardinality, planarity, minimum distance, every distinct-value gap, diameter, and the limiting sublinear ratio.
6. Audit every imported theorem against its exact dimension, normalization, strict/non-strict inequalities, and quantifier order.
7. Before relying on Kanold, Piepmeyer, or any Lean claim, obtain the primary source or run the pinned formal development and record the result.

## Required deliverables

- A self-contained theorem statement using the definitions above.
- A proof or counterexample manuscript with all new lemmas and dependencies explicitly marked.
- A source log with direct URLs, authors, year, publication status, and the precise claim extracted from each source.
- An adversarial proof-audit memo that tries to break the normalization, repeated-distance handling, limiting quantifiers, and any cited implication.
- If incomplete, a concise gap report: strongest proved statement, exact blocking lemma, attempted routes, and why each failed.
- Any computational output only as a reproducible certificate tied to one declared lemma; include code, input data, exact arithmetic/interval policy, and a stopping condition.

## Dynamic Multiagent v2 protocol

Use one research root and at most four concurrent agents total. Start with independently chosen approaches rather than a fixed division of mathematical labor. Maintain an approach registry recording: target lemma or construction, hypotheses, expected payoff, sources checked, current status, and the reason to continue, merge, or stop.

Run multiple waves. In the first wave, prioritize independent literature verification, structural proof ideas, and adversarial attempts to construct sublinear-diameter families. Reallocate slots dynamically when an approach reaches a precise obstruction or produces a checkable lemma. Do not keep agents assigned merely because an initial role was named.

Every proposed proof receives adversarial checking by an agent that did not originate its central argument. The checker must test small-parameter cases, equality versus strictness, multiplicity of equal distances, dependency cycles, and quantifier order. Merge only statements whose prerequisites and citations have been inspected.

Use proof-first allocation. At most one optional computational subtask may run at any time. Before it starts, the registry must state its exact lemma/question, hypotheses, certificate format, and finite stopping condition. End and immediately reassign that slot when the condition is met; computation may not become an open-ended search or substitute for a uniform proof.

## Persistence and resumability

Maintain `research_state.md` at the research root. At each meaningful checkpoint record the canonical target, verified facts with URLs, open proof obligations, approach registry, rejected claims, current agent results, and the next smallest checkable action.

If a runtime boundary arrives before a complete resolution, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`, preserve all citations and failed-route diagnostics, and resume from the recorded proof obligation. Never present an incomplete lower bound, an unverified citation, or a finite computation as a final solution.
