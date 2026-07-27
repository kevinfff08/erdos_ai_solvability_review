# Erdős Problem 126

## Definitions and canonical target

Let \(\mathbb N=\{1,2,\ldots\}\).  For a positive integer \(m\), let \(\omega(m)\) be the number of distinct prime divisors of \(m\), with \(\omega(1)=0\).  Define
\[
f(n)=\min_{\substack{A\subseteq\mathbb N\\|A|=n}}\omega\!\left(\prod_{\substack{(a,b)\in A^2\\a\ne b}}(a+b)\right).
\]
Equivalently, \(f(n)\) is the largest integer lower bound valid for every \(n\)-element set \(A\).  The pair product is over ordered pairs; replacing it by unordered pairs squares the product and leaves \(\omega\) unchanged.

Prove or disprove
\[
\lim_{n\to\infty}\frac{f(n)}{\log n}=+\infty.
\]
The positive statement means: for every \(C>0\), there is \(N_C\) such that every \(n\ge N_C\) and every \(A\subseteq\mathbb N\) of cardinality \(n\) satisfy
\[
\omega\!\left(\prod_{a\ne b}(a+b)\right)\ge C\log n.
\]

## Accepted background

- Erdős and Turán proved in 1934 that the pair sums of \(3\cdot2^{k-1}\) positive integers cannot all be composed from a prescribed set of \(k\) primes.  Hence \(f(n)\gg\log n\).  Read and cite the primary paper: [Erdős–Turán (1934)](https://www.renyi.hu/~p_erdos/1934-03.pdf), bibliographically verified at [Taylor & Francis](https://www.tandfonline.com/doi/abs/10.1080/00029890.1934.11987659).
- Taking \(A=\{1,\ldots,n\}\) gives \(f(n)\le\pi(2n)\ll n/\log n\).  This is an upper bound, not evidence against the target.
- The 1934 paper appears to conjecture a much stronger estimate for the associated maximum \(n(k)\); record its exact quantifiers before using it.  It is conjectural, not accepted background.
- The current [Erdős Problems page](https://www.erdosproblems.com/126) labels the problem open but explicitly warns that its literature knowledge may be incomplete.  Its [discussion page](https://www.erdosproblems.com/forum/thread/126) currently has no comments claiming a solution.
- [The Lean statement](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/126.lean) contains `sorry` placeholders and uses nonnegative rather than positive integers.  It is not a proof.  A separate comparison is needed if it is used for definitions.

## Complete resolutions

A complete affirmative resolution proves the stated uniform \(C\)-then-\(N_C\)-then-all-\(A\) assertion.

A complete negative resolution supplies a constant \(C<\infty\), infinitely many integers \(n\), and explicit or rigorously established sets \(A_n\subseteq\mathbb N\), \(|A_n|=n\), such that
\[
\omega\!\left(\prod_{a\ne b\in A_n}(a+b)\right)\le C\log n.
\]

Before announcing either outcome, audit the current literature and inspect every purported prior solution or counterexample at proof level.

## What does not count as a solution

- Increasing a fixed constant in the known \(c\log n\) lower bound.
- Treating only intervals, random sets, bounded-height sets, or another special family without a rigorous reduction from arbitrary sets.
- Finite computations, heuristics, or numerical plots.
- Showing only that \(f(n)\) is unbounded.
- Proving \(f(n)=o(n/\log n)\), which is compatible with the target.
- Counting prime factors with multiplicity, i.e. \(\Omega\), rather than distinct prime divisors, \(\omega\).
- Citing a database label or a formalized statement as a proof.

## Required correctness checks

1. Preserve quantifier order and ensure constants never depend on the chosen set \(A\).
2. Track distinct prime support rather than repeated divisibility among the \(\binom n2\) sums.
3. State whether pairs are ordered, and justify any replacement by unordered pairs.
4. Keep positive integers separate from Lean's \(\mathbb N\) containing zero.  If using the Lean variant, prove the comparison between the two extremal functions.
5. Verify all asymptotic inversions involving the auxiliary maximum \(n(k)\), including monotonicity and integer rounding.
6. For any proposed counterexample family, prove its cardinality, infinitude of parameters, and prime-support estimate.
7. Require a derivation audit by an investigator who did not produce the relevant argument.

## Required deliverables

Provide:

1. a source ledger with URLs, publication status, exact theorem/claim, and verification status;
2. a self-contained statement with all conventions;
3. a complete proof or disproof, or a sharply delimited partial lemma with its exact implication;
4. a line-by-line adversarial audit of every claimed key lemma;
5. an unresolved-state report listing precise next lemmas and why each would constitute quantified progress;
6. if computation is used, source code, input domain, outputs, certificates, and proof that the computation answers its finite pre-registered question.

## Dynamic Multiagent v2 protocol

Create a research root and an approach registry.  Use at most four concurrent agents.  In the first wave, preserve independence by exploring incompatible possibilities: source verification and reconstruction of the 1934 mechanism; structural consequences of small prime support; possible counterexample families; and adversarial stress testing of candidate reductions.  These are initial directions, not permanent assignments or mandatory methods.

For every registry entry record: hypothesis, precise target lemma, required assumptions, expected implication, falsification test, evidence location, owner, and audit state.  At the end of each wave, compare dependencies; retire duplicated or falsified routes; and dynamically reuse available slots for the sharpest unresolved lemma or independent proof audit.  No investigator may certify their own central argument.  Run multiple waves until a resolution, a certified obstruction, or a runtime boundary.

Use proof-first allocation.  At most one optional computational task may run concurrently, and only after the registry specifies its exact finite lemma/question, hypotheses, search space, certificate format, and stopping condition.  Reassign that slot immediately when the declared question is answered.  Computation may test a lemma or find a finite configuration; it cannot replace the uniform asymptotic proof.

## Persistence and resumability

Maintain `research_state.md` at the research root.  It must contain the canonical statement, source ledger, approach registry, proof fragments and audit status, failures, open dependencies, and any computation specifications and certificates.  Checkpoint after every wave and before a runtime boundary.

If the investigation is incomplete, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`, identify every unverified claim and unfinished source check, and leave concrete next actions so the next research wave can resume without duplicating work.
