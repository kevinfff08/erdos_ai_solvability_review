# Erdős Problem 12 — residual harmonic-sum question

## Definitions and canonical target

Let \(\mathbb N=\{1,2,\ldots\}\). A set \(A\subseteq\mathbb N\) has **Property P** if there are no pairwise distinct \(a,b,c\in A\) such that \(b>a\), \(c>a\), and \(a\mid(b+c)\).

The first two questions in the historical Erdős–Sárközy record are closed. The sole target here is:

> Determine whether every infinite Property-P set \(A\) satisfies
> \[
> \sum_{n\in A}\frac1n<\infty.
> \]

A positive answer means this assertion holds for every such \(A\). A negative answer requires one infinite Property-P set with divergent reciprocal sum.

## Accepted background

- Erdős and Sárközy proved that every Property-P set has natural density zero, while permitting counting functions that are close to linear on infinitely many scales: [Erdős–Sárközy (1970)](https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/10.1112/plms/s3-21.1.97).
- Elsholtz and Planitzer constructed a Property-P set with a uniform lower bound of order \(\sqrt x/[\sqrt{\log x}(\log\log x)^2(\log\log\log x)^2]\): [Elsholtz–Planitzer (2017)](https://link.springer.com/article/10.1007/s00605-016-0995-9).
- Under the additional hypothesis that all elements are pairwise coprime, Schoen and Baier proved upper bounds on infinitely many scales; Baier obtains \(O(N^{2/3}/\log N)\): [Baier (2004)](https://math.colgate.edu/~integers/e13/e13.pdf). This extra hypothesis is not available in the target.
- The finite extremal problem was resolved by Bedert and does not settle the infinite harmonic-sum target: [Bedert (2023), arXiv:2301.07065](https://arxiv.org/abs/2301.07065).
- The historical first question is now formally proved affirmative and the second formally disproved. Inspect the official theorem records and linked Lean artifacts: [part (i)](https://google-deepmind.github.io/formal-conjectures/theorem/?name=Erdos12.erdos_12.parts.i), [part (ii)](https://google-deepmind.github.io/formal-conjectures/theorem/?name=Erdos12.erdos_12.parts.ii), and the [discussion with human-readable constructions](https://www.erdosproblems.com/forum/thread/12). These are formal artifacts/discussion, not peer-reviewed papers.

Do not assume that a near-linear \(N^{1-o(1)}\) counting lower bound forces reciprocal-sum divergence; it does not without a quantitative shell calculation.

## Complete resolutions

An affirmative resolution is a proof that every infinite Property-P set \(A\) has \(\sum_{n\in A}1/n<\infty\).

A negative resolution is an explicit infinite Property-P set \(A\), with a complete proof of both Property P and \(\sum_{n\in A}1/n=\infty\).

## What does not count as a solution

- A result only for pairwise-coprime sets or another unannounced special subclass.
- Density zero, a bound holding only on a subsequence, or a construction with large counting function but no divergence proof.
- A finite computation, finite extremal theorem, or heuristic random model.
- Verifying only triples lying within one block of a construction.
- Re-answering the already closed first or second historical questions.

## Required correctness checks

- State all quantifiers explicitly and retain pairwise distinctness of \(a,b,c\), together with the strict conditions \(b,c>a\).
- In a construction, check every cross-block pattern and every possible order of the three elements.
- Do not treat \(b+c=2a\) as an admissible forbidden triple when \(b,c>a\); it is impossible under those strict inequalities.
- For divergence, provide a valid dyadic-shell, summation-by-parts, or equivalent argument with explicit lower bounds that make the positive series diverge.
- For convergence, derive a summable upper bound valid for all sufficiently large shells and for every Property-P set, not merely for a selected construction.
- Cite every external theorem by a direct primary or formal-artifact URL and distinguish theorem, conjecture, and heuristic.

## Required deliverables

1. A standalone statement of Property P and the exact target.
2. A proof manuscript with numbered lemmas and a dependency graph.
3. A source ledger giving URL, authors, date, status, and exact role for every external result.
4. An adversarial audit of each main lemma, including boundary cases and quantifier checks.
5. If proposing a construction, a separate verification of Property P and a separate reciprocal-sum analysis.
6. A final verdict limited to `proved affirmative`, `proved negative`, or `CHECKPOINT_NOT_FINAL`.

## Dynamic Multiagent v2 protocol

Maintain a research root that owns the canonical statement, source ledger, and approach registry. Use at most four concurrent agents.

Begin with independent approaches rather than a fixed method: at minimum, one route should seek a universal structural/convergence theorem, one should seek a divergent construction, and one should audit the 2026 constructions and their harmonic mass. Register each approach before substantial work with its target lemma, assumptions, falsification test, and current evidence.

Run in multiple waves. After each wave, the research root compares results, retires duplicates, and dynamically reuses slots for the sharpest unresolved lemma. Before accepting any claimed proof, assign an adversarial checker that did not author the central argument. The checker must attack quantifiers, cross-scale triples, strict inequalities, and the analytic summation step.

Proof work has priority. At most one optional computational subtask may run at a time. Before it begins, record the exact lemma or counterexample family tested, hypotheses, finite search domain, certificate format, and stopping condition. End and reassign that slot immediately when the declared question is answered. Computation may guide a lemma but cannot establish the infinite target by extrapolation.

## Persistence and resumability

Keep `research_state.md` at the research root. At each checkpoint record: canonical target; source ledger; approach registry; proved lemmas with dependencies; rejected claims and counterexamples; active proof obligations; and any computation's declared stopping condition and certificate.

If a runtime boundary interrupts an incomplete investigation, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`, preserve all source URLs and proof obligations, and do not report a mathematical resolution. On resumption, first audit the checkpoint against the canonical target before allocating new agents.
