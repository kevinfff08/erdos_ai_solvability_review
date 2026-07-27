# Erdős Problem 102: dense four-rich lines

## Definitions and canonical target

Fix a constant \(c>0\), independently of \(n\).  For a finite set \(P\subset\mathbb R^2\), write
\[
\mathcal L_4(P)=\{\ell:\ell\text{ is a distinct geometric line and }|\ell\cap P|\ge4\}.
\]
For each \(n\) with a nonempty admissible class, define
\[
H_c(n)=\min_{\substack{P\subset\mathbb R^2,\ |P|=n\\|\mathcal L_4(P)|\ge c n^2}}\max_{\ell}|\ell\cap P|.
\]
The canonical target is to prove or disprove that, for every fixed \(c>0\) for which admissible configurations exist for arbitrarily large \(n\), \(H_c(n)\to\infty\) along those \(n\). Count a geometric line once only; do not count its point pairs or its incidences. “More than three” means at least four.

## Accepted background

- Paul Erdős stated the related Erdős–Purdy question in 1995 and wrote that even the constant lower bound \(h(n)\ge5\) was then unproved; he conjectured divergence and suggested a square-root lower bound. Source: [Erdős 1995](https://doczz.net/doc/7633256/some-of-my-favourite-problems-in-number---ime-usp).
- The current [Erdős Problems record](https://www.erdosproblems.com/102) remains open and reports that Zach Hunter’s high-dimensional-grid plus generic-projection construction refutes the square-root lower-bound suggestion. Treat the reported construction as a claim to reconstruct, not as an imported black-box theorem: this audit found no primary technical write-up.
- Szemerédi–Trotter proves the standard point-line incidence and rich-line bounds; at fixed richness four it still permits \(O(n^2)\) rich lines, so it does not settle the target. Source: [Szemerédi–Trotter 1983](https://trotter.math.gatech.edu/papers/38.pdf).
- Recent work on triple lines, e.g. [Elekes–Szabó](https://link.springer.com/article/10.1007/s00454-023-00556-3), is adjacent but is not a theorem about this four-rich-line target.

Distinguish every theorem from every conjecture and database report. Do not use an external result without a direct URL, exact statement, and hypothesis match.

## Complete resolutions

An affirmative resolution proves: for every fixed nonvacuous \(c>0\) and every \(M\in\mathbb N\), there exists \(N(c,M)\) such that every admissible \(P\) with \(|P|\ge N(c,M)\) has a line containing at least \(M\) points.

A negative resolution gives fixed constants \(c>0\) and \(B\in\mathbb N\), and arbitrarily large sets \(P_n\subset\mathbb R^2\), satisfying
\[
|\mathcal L_4(P_n)|\ge c|P_n|^2,\qquad \max_\ell|\ell\cap P_n|\le B.
\]
For a probabilistic family, prove simultaneous positive probability of all conditions and extract deterministic instances.

A separate asymptotic estimate for \(H_c(n)\) requires rigorously stated matching bounds; it is not required for a resolution of divergence.

## What does not count as a solution

- A family in which maximum collinearity grows, however slowly, with \(n\).
- Counting rich pairs or incidences instead of distinct rich lines.
- Allowing \(c\) to decay with \(n\), or exploiting an eventually empty admissible class.
- A result only for grids, algebraic configurations, bounded-degree curves, or another restricted subclass.
- Finite computation without an infinite-family proof or an exact certificate with an unbounded extension.
- A generic-projection assertion without proofs of injectivity, rich-line preservation, line deduplication, and control of unintended collinearities.

## Required correctness checks

1. Audit the quantifiers: fix \(c\), then quantify over all admissible \(P\); for an affirmative proof quantify over every \(M\).
2. Verify that every claimed \(\mathcal L_4\) count is a count of distinct Euclidean lines and uses threshold \(\ge4\).
3. If dualizing, explicitly map points to lines, four-rich primal lines to intersection multiplicities, and maximum primal collinearity to maximum dual intersection multiplicity; check projective/infinite exceptions.
4. For every construction, bound every line, not merely the intended rich lines, and prove a fixed positive density \(c\).
5. For every projection, identify the finite exceptional locus and prove the selected projection avoids it.
6. Record all dependencies on \(c\), dimension, floors, logarithm bases, and subsequences of \(n\).
7. Require an adversarial reader to try pair-overcounting, threshold changes, empty-class vacuity, and degenerate projection counterexamples.

## Required deliverables

1. `research_state.md` with the canonical statement, dated source log, approach registry, accepted lemmas, rejected approaches, gaps, and next proof obligations.
2. A self-contained proof manuscript or counterexample certificate, with a source URL and hypothesis match for each imported theorem.
3. A resolution memo mapping every completion condition above to exact proof locations; state separately whether the asymptotic-estimate question remains open.
4. An independent adversarial verification report by an agent other than the principal proposer.

## Dynamic Multiagent v2 protocol

Use one research root and at most four concurrent agents. Begin with genuinely independent approaches before merging: for example, a structural/duality route, a constructive route, a literature-and-hypothesis audit, and a proof auditor. Do not prescribe permanent roles.

Maintain an approach registry in `research_state.md` with: exact claim, owner, assumptions, dependencies, evidence, current status, obstruction or counterexample, and next smallest check. Before assigning a task, inspect the registry and choose the highest-value unresolved obligation. Work in multiple waves; immediately reuse a freed slot for a new obstruction, alternate approach, or verification task.

Any proposed lemma must receive an adversarial check by a different agent before it becomes accepted background. Merge approaches only after their quantifiers and hypotheses have been reconciled explicitly. A claimed resolution requires a final independent check against all seven correctness checks.

Allocate proof-first. At most one optional computational task may run at a time. Before running it, record the precise lemma or finite counterexample property tested, hypotheses, finite search space or certificate format, stopping condition, and how each outcome changes the proof plan. Stop it and reassign its slot as soon as that question is answered. Computation may test a bounded lemma or certify a finite instance; it cannot replace an arbitrarily-large-\(n\) argument.

## Persistence and resumability

After each material result, update `research_state.md` with the exact theorem or failure, sources consulted, proof gap, and next verifiable action. Preserve failed routes and the precise failure point.

If interrupted before a complete independently checked proof or counterexample, put `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`; record active proof obligations, registry states, and required source checks. Return that checkpoint rather than claiming a solution.
