# Erdős Problem 84 — surviving lower-bound target

## Definitions and canonical target

Work with finite simple undirected graphs. For an integer \(n\ge 3\) and an \(n\)-vertex graph \(G\), define its cycle spectrum
\[
\mathcal C(G)=\{\ell\in\{3,\ldots,n\}:G\text{ contains a simple cycle of length }\ell\}.
\]
Let
\[
f(n)=|\{\mathcal C(G): |V(G)|=n\}|,
\]
the number of distinct spectra, not the number of labelled graphs.

Canonical target: prove
\[
\lim_{n\to\infty}\frac{f(n)}{2^{n/2}}=+\infty.
\]
Equivalently, prove that for every real \(M>0\), there is \(N\) such that every integer \(n\ge N\) satisfies \(f(n)\ge M2^{n/2}\).

This is a revised target. The separate database request \(f(n)=o(2^n)\) is already solved and is not part of the task.

## Accepted background

- Verstraëte proved the now-closed upper-bound request, in fact \(f(n)=o(2^{n-n^c})\) for an absolute \(c\ge0.1\): [publisher record](https://link.springer.com/article/10.1007/s00493-004-0043-6).
- Nenadov proved the stronger upper bound
  \[
  f(n)\le 2^{n-\Omega(\sqrt n/\log^{3/2}n)}.
  \]
  The peer-reviewed paper also states that the best known lower bound is Faudree's \(2^{n/2}\) construction: [article and PDF](https://escholarship.org/uc/item/4k75b3z7), [arXiv v2](https://arxiv.org/abs/2501.09904).
- For even \(n\), Faudree's construction takes \(A\subseteq\{n/2+1,\ldots,n\}\), starts with a Hamilton path, and adds edges from one endpoint to vertices indexed by \(A\). Its high-length spectrum recovers \(A\), yielding at least \(2^{n/2}\) distinct spectra.
- Nenadov's paper concerns upper bounds: its tools include Hamiltonian reductions, chord fingerprints, and container lemmas. These are accepted background, not a prescribed method for the lower-bound task.

## Complete resolutions

An affirmative resolution is a fully rigorous proof that \(f(n)/2^{n/2}\to+\infty\), with all quantifiers over every sufficiently large integer \(n\).

A negative resolution is a rigorous proof of the negation: there is a finite \(M>0\) such that for every \(N\) some \(n\ge N\) has \(f(n)\le M2^{n/2}\). An explicit infinite sequence with a uniform bound of this kind is sufficient.

## What does not count as a solution

- Reproving or strengthening an upper bound such as \(f(n)=o(2^n)\).
- Obtaining only \(f(n)\ge2^{n/2}\), \(f(n)\ge c2^{n/2}\) for fixed \(c\), or a bound on an unspecified subsequence.
- Counting labelled graphs rather than distinct sets \(\mathcal C(G)\).
- Giving a family whose parameter choices are not proved to have different complete spectra.
- Demonstrating only that selected desired lengths occur, while failing to exclude extra cycles caused by interactions among gadgets or chords.
- A finite computation without a proved reduction, exact certificate, and a stopping condition tied to a named lemma.

## Required correctness checks

1. State the graph model and exact vertex count for every construction.
2. Prove a complete characterization of \(\mathcal C(G)\), including cycles using several added edges or several gadgets.
3. Prove injectivity from every encoding parameter to the full spectrum, not merely to a chosen subset unless the chosen subset itself is recovered from the full spectrum.
4. Establish all sufficiently large \(n\), including parity and rounding. Isolated-vertex padding changes the denominator and must be analyzed quantitatively.
5. Keep constants and thresholds uniform in \(n\); distinguish a limit from an unbounded limsup.
6. For a claimed negative resolution, verify that the bound applies to the actual \(f(n)\), not a restricted graph class.

## Required deliverables

- A self-contained proof manuscript or a self-contained disproof manuscript.
- A precise lemma dependency graph, with every external theorem cited by stable URL and exact statement used.
- For each proposed construction, a spectrum-classification lemma and an injection/collision lemma.
- A short status memo distinguishing proved facts, failed approaches, and open gaps.
- If computation is used, source code or executable pseudocode, input range, certificates, and an explanation of the proved lemma it tests; computation alone is not evidence of the asymptotic claim.

## Dynamic Multiagent v2 protocol

Maintain a research root coordinating at most four concurrent agents. Begin with independent approaches rather than a fixed decomposition. Maintain an approach registry recording each approach's target lemma, assumptions, current evidence, collision risks, and disposition.

Use multiple waves. In the first wave, diversify between constructive encodings, composition operations, structural obstructions, and adversarial spectrum analysis. At every later wave, reuse a freed slot for the highest-value unresolved lemma rather than preserving a static assignment. Before merging a claimed advance, assign an independent adversarial proof check focused on extra cycles, non-injective spectra, parity, and asymptotic quantifiers.

Allocate resources proof-first. At most one concurrent computational subtask is allowed. Before it starts, declare the exact lemma or counterexample question, hypotheses, finite stopping condition, and certificate format. Immediately reassign that slot once the stated question is answered. Do not let enumeration become a surrogate for a proof.

## Persistence and resumability

Maintain `research_state.md` after every wave. It must record the canonical target, source URLs and access dates, approach registry, proved lemmas, rejected claims and counterexamples, pending proof obligations, and the next smallest verifiable tasks.

If a runtime boundary occurs before an affirmative or negative proof passes adversarial checking, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`. Preserve all proof dependencies and exact unresolved gaps. Do not report a solution, partial solution, or status change merely because an exploratory computation or heuristic construction looked promising.
