# Erdős Problem 91

## Definitions and canonical target

For every integer \(n\ge 2\), set
\[
D(n)=\min_{\substack{A\subset\mathbb R^2\\|A|=n}}
\left|\{\|x-y\|:x,y\in A,\ x\ne y\}\right|.
\]
An \(n\)-point set is a *global minimizer* if it determines exactly \(D(n)\) distinct nonzero Euclidean distances. Two finite point sets are *similar* if one is obtained from the other by a translation, an orthogonal map (reflections included), and a positive uniform scaling.

Resolve this target:

> Does there exist \(n_0\) such that, for every integer \(n\ge n_0\), there are two non-similar global minimizers of size \(n\) in \(\mathbb R^2\)?

Do not replace this with the historical phrase “probably many”; that phrase has no quantified completion condition.

## Accepted background

- The [official Erdős Problems data entry](https://raw.githubusercontent.com/teorth/erdosproblems/refs/heads/main/data/problems.yaml) lists #91 as open and its solution status as unformalized. Its `formalized: yes` metadata concerns a statement formalization, not a verified solution.
- The problem record reports small cases: uniqueness for \(n=3\) and \(n=5\), two non-similar examples for \(n=4\), and an Erdős-attributed statement for \(6\le n\le9\). Inspect the primary text before using the latter as a theorem.
- Z. Kovács, [A note on Erdős's mysterious remark](https://arxiv.org/abs/2412.05190) (2024 preprint) gives a computer-assisted algebraic proof of the \(n=5\) uniqueness statement. It does not settle the asymptotic problem.
- Guth and Katz, [On the Erdős distinct distances problem in the plane](https://annals.math.princeton.edu/2015/181-1/p02), *Annals of Mathematics* 181 (2015), prove \(D(n)\ge c n/\log n\). This is a bound on the number of distances, not a classification of exact minimizers.

## Complete resolutions

An affirmative resolution proves one integer \(n_0\) and, for every \(n\ge n_0\), produces or proves the existence of two non-similar \(n\)-point global minimizers. For each minimizer, establish its exact distance count and global optimality.

A negative resolution proves that infinitely many \(n\) have exactly one global minimizer up to the stated similarity convention. This is sufficient to refute the eventual-for-all-\(n\) target.

## What does not count as a solution

- Two non-similar sets with the same distance count unless that count is proved to be \(D(n)\).
- Two labelled, congruent, or scaled copies.
- A finite list of values of \(n\), or an affirmative result only on a subsequence.
- A new upper or lower bound for \(D(n)\) without a theorem about exact minimizers.
- Floating-point searches, heuristic optimizers, or informal diagrams without an exact completeness and optimality certificate.
- A claim about “many” minimizers without explicit quantifiers.

## Required correctness checks

1. Fix the Euclidean metric, exclusion of diagonal pairs, and similarity convention at the outset.
2. For every proposed minimizer, separately prove \(D(n)\ge k\) and exhibit exactly \(k\) distances.
3. Verify the eventual quantifier: one threshold must cover every subsequent integer.
4. Prove non-similarity by an invariant or an argument valid under translations, rotations, reflections, and scaling.
5. Audit all imported theorems for exact hypotheses, parameter range, and whether they concern distinct values rather than repeated pairs.
6. If computation is used, give a finite candidate universe, exact representation, completeness proof, code/data, and independently checkable certificates.
7. Treat historical database remarks as leads until their primary proof or a complete modern proof is inspected.

## Required deliverables

- A standalone theorem statement with definitions and quantifiers.
- Either a full affirmative/negative proof or a labelled partial report whose first unproved lemma is explicit.
- A source ledger: direct URL, authors, date, status, exact statement used, and hypothesis check for every external result.
- Exact constructions, distance-count proofs, optimality proofs, and non-similarity proofs for every asserted family.
- An adversarial proof audit identifying possible failures and their disposition.
- If unresolved, a precise residual lemma and an explanation of why it advances the canonical target.

## Dynamic Multiagent v2 protocol

Maintain a research root responsible for the canonical target, source ledger, approach registry, and proof integration. Use at most four concurrent agents. Begin with independent approaches, such as structural consequences of exact minimization, transformations that might preserve exact optimality, and adversarial source/statement checking. Do not prescribe a preferred mathematical method.

The approach registry must record, for each active line: target lemma, hypotheses, claimed consequence, imported results, proof state, and a falsification test. Work in multiple waves. After each wave, retain only verified statements, compare independent approaches, and dynamically reassign completed, disproved, or derivative slots to the sharpest unresolved dependency.

Every candidate proof must be checked by an agent not responsible for discovering it. The adversarial check must test global-minimality claims, quantifiers, equality cases, similarity convention, hidden classifications, and imported hypotheses. Integrate a claim only after this audit is recorded.

Allocate resources proof-first. At most one optional computation may run at once. Before it starts, declare the exact lemma or counterexample question, finite search universe, exact arithmetic, certificate format, and stopping condition. Immediately reassign that slot when its stated question is answered. Computation must not stand in for the eventual asymptotic proof.

## Persistence and resumability

Maintain `research_state.md` after every material step. It must record the canonical target, source ledger and access dates, approach registry, proved lemmas with dependencies, failed routes and counterexamples, any computation specification/certificate, and the next falsifiable task.

If runtime ends before resolution, place `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`. Preserve unresolved proof obligations and source URLs, then resume from the next unverified dependency. Never report a solution or status change merely because a search or computation was interrupted.
