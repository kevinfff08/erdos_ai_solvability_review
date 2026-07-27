# Erdős Problem 66: pointwise logarithmic additive representation function

## Definitions and canonical target

Let \(\mathbb N=\{1,2,\ldots\}\). For a set \(A\subseteq\mathbb N\), define the **ordered additive representation function**

\[
r_A(n):=\sum_{a=1}^{n-1}1_A(a)1_A(n-a)
      =|\{(a,b)\in A^2:a+b=n\}|.
\]

Thus the convolution is additive, not Dirichlet convolution; diagonal pairs \(a=b\) are counted once as ordered pairs. The target is:

\[
\text{Does there exist }A\subseteq\mathbb N\text{ and a finite }L>0
\text{ such that } r_A(n)/\log n\to L?
\]

The limit is along **every** integer \(n\to\infty\), and \(\log\) is natural. Equivalently, for every \(\varepsilon>0\) there must be \(N\) such that every integer \(n\ge N\) satisfies

\[
|r_A(n)-L\log n|\le \varepsilon\log n.
\]

Do not interpret the limit in the extended reals: otherwise \(A=\mathbb N\) gives a trivial \(+\infty\) ratio. Erdős historically asked the special case \(L=1\); do not assume that it is equivalent to the present existential-any-\(L\) formulation.

## Accepted background

- The current [Erdős Problems entry](https://www.erdosproblems.com/latex/66) records this as open and summarizes the relevant earlier barriers.
- Erdős and Sárközy, [Problems and Results on Additive Properties of General Sequences, II (1986)](https://users.renyi.hu/~p_erdos/1986-12.pdf), record the conjectural negative answer and prove that, for suitable increasing \(F=o(n/(\log n)^2)\), approximation of the representation function on the \(o(\sqrt F)\) scale is impossible. This is a theorem, but it does **not** rule out \(L\log n+o(\log n)\).
- Horváth, [An Improvement of a Theorem of Erdős and Sárközy (2007)](https://doi.org/10.1556/Pollack.2.2007.S.14), proves a stronger \(\sqrt{F}\)-scale pointwise obstruction. It remains insufficient for the target error \(o(\log n)\).
- Erdős and Tetali, [Representations of Integers as the Sum of k Terms (1990)](https://onlinelibrary.wiley.com/doi/10.1002/rsa.3240010302), construct bases with representation count \(\Theta(\log n)\). This establishes the scale, not convergence of the normalized count.
- Kuang and Wang, [arXiv:2607.16613 (2026)](https://arxiv.org/abs/2607.16613), prove a related density-one result: outside a density-zero exceptional set, an ordered representation function can approximate a slowly growing \(O(\log\log n)\) function extremely well. This is a preprint and is not a solution here, because this problem forbids every exceptional set and asks for the \(\log n\) scale.

All claims beyond these sources require independent proof. Clearly label any conjectural heuristic as such.

## Complete resolutions

An affirmative resolution must provide a set \(A\subseteq\mathbb N\), a finite \(L>0\), and a proof of the all-integers epsilon definition above.

A negative resolution must prove that for every \(A\subseteq\mathbb N\) and every finite \(L>0\), \(r_A(n)/\log n\) fails to converge to \(L\). It is enough to derive a contradiction from the assumed asymptotic \(r_A(n)=L\log n+o(\log n)\), but the derivation must retain uniform control over all sufficiently large integers.

## What does not count as a solution

- \(r_A(n)=\Theta(\log n)\), bounded limsup, or convergence on any subsequence.
- An almost-all, density-one, averaged, Cesàro, probabilistic-high-probability, or finite-range result.
- Repeating an \(o(\sqrt{\log n})\) obstruction without bridging the gap to \(o(\log n)\).
- A construction or theorem for unordered representations, distinct summands, a different ambient set, or Dirichlet convolution unless a rigorous conversion establishes this exact target.
- Evidence from computation without a proved lemma, explicit hypotheses, and a stopping condition.
- Resolving only \(L=1\) without proving it resolves the stated all-\(L\) existential target.

## Required correctness checks

1. State the representation convention in every lemma; check ordered pairs and diagonal terms explicitly.
2. State every quantifier: an exceptional set of size \(o(x)\) is still forbidden.
3. When invoking Erdős–Sárközy or Horváth, match every hypothesis on the comparison function, monotonicity, and error scale.
4. Check that no passage from \(\Theta(\log n)\) to a limit is tacit.
5. For any generating-function argument, justify coefficient extraction, convergence domain, and all boundary-limit interchanges.
6. For a proposed construction, prove that later additions to \(A\) do not destroy estimates already claimed for infinitely many sums.
7. For a negative proof, identify exactly where the assumption \(o(\log n)\) yields a stronger forbidden estimate; an unexplained error loss invalidates the conclusion.

## Required deliverables

- A `research_state.md` containing the canonical statement, convention ledger, source URLs, approach registry, and status of each lemma.
- A short literature memo separating proved theorems, preprints, heuristics, and non-transferable variants.
- For each serious route, a self-contained lemma sheet with assumptions, target conclusion, dependency graph, and proof or precise failure point.
- A final proof manuscript only if all required checks pass; otherwise a `CHECKPOINT_NOT_FINAL` report that lists verified partial lemmas, invalidated approaches, and the next falsifiable subgoal.
- Citations must link directly to the sources above; do not cite search snippets or state a forum/AI claim as a theorem without an inspectable proof.

## Dynamic Multiagent v2 protocol

Create a research root that maintains `research_state.md`. Use at most four concurrent agents total. Begin with independent approaches rather than a fixed division of labor: at least two agents should test incompatible proof routes before the root commits effort.

Maintain an approach registry with: identifier, exact target lemma, conventions used, dependencies, current evidence, status (`active`, `blocked`, `refuted`, `verified`), and an adversarial reviewer. Agents must read the registry before claiming novelty or reusing a result.

Run multiple waves. In each wave, the root allocates slots to the most falsifiable unresolved lemmas, then requests adversarial checking of any claimed proof before downstream work relies on it. Reuse a slot immediately after its lemma is proved, disproved, or shown irrelevant; do not preserve static roles. An agent finding a convention mismatch, hidden density-one exception, or unsupported analytic interchange may stop the affected route and trigger reallocation.

Use proof-first allocation. At most one optional computational subtask may run at once. Before computation, record its exact lemma or counterexample question, finite hypotheses, certificate format, and stopping condition in `research_state.md`. On answering that question, terminate the computation and reassign the slot to proof validation or a new lemma; computation may not become open-ended exploration.

## Persistence and resumability

At the end of every wave, update `research_state.md` with source checks, exact statements of accepted lemmas, rejected arguments and their counterexamples, open proof obligations, and the next ranked tasks. Preserve all convention decisions.

If a runtime boundary occurs before a complete affirmative construction or complete universal impossibility proof has survived adversarial review, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`. State what is verified, what is only conjectural, and the exact next action. Do not present a partial argument, numerical experiment, density-one result, or unreviewed agent claim as a resolution.
