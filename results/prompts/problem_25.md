# Erdős Problem 25: logarithmic density of thresholded congruence sieves

## Definitions and canonical target

Let \(n_1<n_2<\cdots\) be any strictly increasing sequence of positive integers. For every \(i\), let \(a_i\pmod{n_i}\) be one residue class. Define
\[
 A=\{n\in\mathbb N:\ \forall i\ge1,\ n<n_i\ \text{or}\ n\not\equiv a_i\pmod {n_i}\}.
\]
Thus the \(i\)-th constraint is active exactly for \(n\ge n_i\), including \(n=n_i\). For each fixed \(n\), only finitely many constraints are active.

Prove or disprove the universal assertion that
\[
 \delta_{\log}(A)=\lim_{x\to\infty}\frac1{\log x}
 \sum_{\substack{n\le x\\n\in A}}\frac1n
\]
exists for every allowed \((n_i,a_i)\). Replacing \(n\le x\) by \(n<x\) is immaterial.

## Accepted background

- The live [Problem 25 discussion page](https://www.erdosproblems.com/forum/thread/25) lists this exact statement as open (last edited 2026-01-20), but explicitly says that the status reflects the curator's belief rather than an exhaustive literature proof.
- [Problem 486](https://www.erdosproblems.com/latex/486) is a broader residue-set problem. It records the Davenport–Erdős zero-residue result and says it generalizes Problem 25. Do not silently identify the two: 486 uses \(m>n\), while the target here activates at \(n\ge n_i\).
- Davenport and Erdős, [*On sequences of positive integers* (1936)](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/2/1/93274/on-sequences-of-positive-integers), prove the classical multiples/zero-class result. This does not settle arbitrary translated classes.
- For each finite prefix, \(A^{(k)}\) is eventually periodic, hence has a density \(\delta_k\); \(\delta_k\) decreases to some \(\delta\). The missing step is to prove that the infinite set \(A\) has logarithmic density \(\delta\), or to refute this.
- Przemyslaw Chojecki's [2026 manuscript](https://www.ulam.ai/research/erdos25.pdf) proves special cases \(\sum_i1/n_i<\infty\) and pairwise-coprime moduli, then gives a conditional quotient-sieve reduction. It explicitly does **not** prove the full statement.
- The [Lean file](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/25.lean) encodes the statement but contains `sorry`; it is not a verified proof.

## Complete resolutions

An affirmative resolution is a rigorous proof that the displayed logarithmic-density limit exists for every strictly increasing modulus sequence and every residue-class selection.

A negative resolution is one explicit allowed sequence together with a rigorous proof that the harmonic averages fail to converge; preferably certify two sequences \(X_j,Y_j\to\infty\) having distinct limiting values.

A claimed resolution must also state whether it treats the endpoint \(n=n_i\), all nonzero residues, and all non-coprime moduli. A theorem covering only an additional hypothesis is a partial result, not a resolution.

## What does not count as a solution

- Finite computation, finite-prefix enumeration, or observing numerical stabilization.
- Showing that every \(A^{(k)}\) is periodic.
- Establishing only natural-density failure or existence.
- Proving only the summable, pairwise-coprime, or zero-residue cases.
- Assuming a uniform quotient-sieve estimate, a tail bound, or an error summability statement without proving it.
- Treating the `sorry`-containing Lean declaration as a proof.
- Importing Problem 486 without resolving its strict-threshold endpoint difference.

## Required correctness checks

- Preserve all quantifiers: arbitrary increasing \((n_i)\), arbitrary classes \((a_i)\), and a universal conclusion.
- Use harmonic mass \(\sum 1/n\), not only counts of elements in intervals.
- Account for the active constraint at \(n=n_i\).
- If using the first-kill decomposition \(\mathbb N\setminus A=\bigsqcup_i E_i\), prove a uniform accumulated error estimate; termwise eventual periodicity is insufficient.
- If a construction claims oscillation, bound both the desired contribution and every earlier/later block on the stated cutoff subsequences.
- If a density is asserted to equal \(\lim_k\delta_k\), justify the exchange of the two limiting processes.
- Label every literature input as theorem, conditional theorem, heuristic, or informal claim, and cite its direct source.

## Required deliverables

1. A self-contained theorem or explicit counterexample, with a complete proof.
2. A dependency ledger separating proved lemmas, external theorems, assumptions, and failed routes.
3. A source log with stable URLs and exact statements used; distinguish peer-reviewed papers, manuscripts, and forum comments.
4. A short adversarial audit of the final argument against every correctness check above.
5. If incomplete, a precise new lemma or obstruction, including hypotheses, why it would advance the target, and any counterexamples ruled out.

## Dynamic Multiagent v2 protocol

Create a research root with an approach registry. Each registry record must state: target variant, definitions/endpoint convention, key lemma or construction, source dependencies, current proof status, falsification test, and next action.

Use at most four concurrent agents. Begin with independent approaches, not fixed roles: one may seek a positive uniform-tail mechanism, one may test a counterexample architecture, one may examine quotient-sieve/error estimates, and one may adversarially audit the statement and literature. These are starting directions only; dynamically reassign slots after evidence arrives rather than preserving a static assignment.

Run multiple waves. At every wave boundary, compare the registry entries, merge duplicate routes, abandon routes defeated by explicit counterexamples, and reuse freed slots for the sharpest unresolved lemma. Reserve an independent adversarial check for any proof that appears complete; the checker must reconstruct the threshold convention and challenge each limiting interchange.

Proof-first allocation is mandatory. At most one optional computational subtask may run at once, and only after recording: the exact lemma or counterexample hypothesis it tests, finite parameters, a certificate format, and a stopping condition. Stop and reassign the computational slot immediately when that question is answered. Computation cannot establish the universal limit by extrapolation.

## Persistence and resumability

Maintain `research_state.md` in the research root. After each wave record the canonical statement, sources checked, approach registry, proved lemmas, rejected claims, counterexamples to intermediate assertions, and the next smallest rigorous action.

If execution ends before a full proof or disproof, start `research_state.md` with `CHECKPOINT_NOT_FINAL`. Preserve exact cutoffs, constructions, source URLs, proof gaps, and the next adversarial check. Never convert an incomplete conditional reduction or finite experiment into a solution claim.
