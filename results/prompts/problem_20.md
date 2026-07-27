# Erdős Problem 20: the fixed-k sunflower conjecture

## Definitions and canonical target

For integers n >= 1 and k >= 2, a k-sunflower is a collection of k distinct sets A_1,...,A_k for which a set K exists with A_i intersection A_j = K whenever i != j. Equivalently, the petals A_i minus K are pairwise disjoint. Let f(n,k) be the least m such that every family of at least m distinct n-element sets contains a k-sunflower.

Prove or disprove: for every fixed k >= 3, there exists a finite constant c_k, independent of n, such that f(n,k) < c_k^n for every n >= 1. The k=2 case is trivial and is not a target.

## Accepted background

Erdős and Rado proved f(n,k) <= (k-1)^n n!; see [their 1960 paper](https://doi.org/10.1112/jlms/s1-35.1.85). Alweiss, Lovett, Wu, and Zhang broke the factorial barrier; see the [preprint](https://arxiv.org/abs/1908.08483) and [peer-reviewed version](https://doi.org/10.1017/fmp.2021.5). Further relevant work includes Rao's [Coding for sunflowers](https://discreteanalysisjournal.com/article/13833-coding-for-sunflowers), Bell–Chueluecha–Warnke's [Note on sunflowers](https://doi.org/10.1016/j.disc.2021.112517), and the current [Erdős Problems record](https://www.erdosproblems.com/20).

These are upper-bound theorems, not resolutions of the constant-base conjecture. The public record summarizes the current qualitative bound as (C k log n)^n. Record the exact statement and hypotheses of every imported theorem before use.

## Complete resolutions

An affirmative resolution is a complete proof that, for every fixed k >= 3, one finite c_k works for all n >= 1.

A negative resolution is a fixed k >= 3 and rigorously verified k-sunflower-free n-uniform families F_n for infinitely many n with |F_n| > c^n for every constant c > 0.

## What does not count as a solution

- Any upper bound with a base that diverges with n, including a logarithmic factor.
- A theorem only for k=2, for growing k, for finitely many n, or for restricted families.
- Numerical evidence without an all-n theorem or an infinite certified counterexample sequence.
- A purported constant that depends on n.
- A family not proved to have distinct n-sets and no k-sunflower.

## Required correctness checks

1. State the quantifiers at every principal claim and certify c_k is independent of n.
2. Verify the sunflower condition by equal pairwise intersections, or prove the equivalent disjoint-petals condition.
3. Audit every induction, restriction, and base case for n-dependent losses.
4. For a counterexample, prove both sunflower-freeness and growth beyond every fixed-base exponential along infinitely many n.
5. Attach direct primary-source citations and exact hypotheses to imported results.
6. Subject every candidate proof to adversarial checking for hidden ground-set restrictions, repeated sets, nonuniformity, and illicit parameter dependence.

## Required deliverables

Deliver a self-contained report with the canonical target, a source ledger, an approach registry, all proved lemmas and dependencies, failed-route records, and adversarial proof checks. A claimed resolution must include a complete line-by-line proof or a complete infinite counterexample construction meeting the stated completion condition. Cite primary papers or official records directly; search snippets are not evidence.

## Dynamic Multiagent v2 protocol

Maintain a research root and use at most four concurrent agents. Start with independent approaches rather than one shared proof plan. Maintain an approach registry containing each route's precise claim, dependencies, evidence, falsification attempt, status, and next decisive lemma. Agents must consult it before duplicating work.

Use multiple waves. Retire or redirect a route after its decisive lemma fails or is blocked, then reuse its slot for an incompatible route or adversarial proof checking. Every substantial candidate lemma requires an independent adversarial check before supporting later work.

Use proof-first allocation. At most one optional computational task may run at once, and only after recording its exact lemma or construction, hypotheses, finite search space, certificate format, and stopping condition. Reassign its slot immediately once answered.

## Persistence and resumability

Maintain research_state.md with the canonical statement, source ledger, approach registry, proof dependencies, checks performed, rejected claims, and next actions. Checkpoint after each wave and before expensive computation. If interrupted before a resolution, begin research_state.md with CHECKPOINT_NOT_FINAL and specify exactly what was verified and what remains. A checkpoint is not a solution.
