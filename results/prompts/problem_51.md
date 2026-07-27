# Erdős Problem 51 — least inverse totients

## Definitions and canonical target

Let \(\varphi(n)=\#(\mathbb Z/n\mathbb Z)^\times\) be Euler’s totient function. A **totient** is an integer \(a\in\operatorname{Im}(\varphi)\). For each totient \(a\), define
\[
n_*(a):=\min\{n\in\mathbb N:\varphi(n)=a\}.
\]

Prove or disprove:
\[
\sup_{a\in\operatorname{Im}(\varphi)}\frac{n_*(a)}a=\infty.
\]
Equivalently, prove or disprove that for every real \(C>0\) there is a totient \(a\) such that every \(n\in\mathbb N\) satisfying \(\varphi(n)=a\) obeys \(n>Ca\). A positive proof must explicitly extract an infinite set \(A\) of totients for which \(n_*(a)/a\to\infty\) along \(a\in A\).

## Accepted background

- Kevin Ford’s 2025 CIRM problem report states exactly the constant formulation above and records that it is wide open even for \(C=3\): <https://www.cirm-math.fr/RepOrga/3213/Slides/Open-Problems-mardi2.pdf>.
- Ford’s paper *The distribution of totients* develops the distribution of totients and their preimages: <https://www.ford126.web.illinois.edu/wwwpapers/totients.pdf>. Use the published theorem only after checking its exact hypotheses and quantifiers.
- Ford proved that every multiplicity \(k\ge2\) occurs for \(\varphi\), but this does not control least preimages: <https://arxiv.org/abs/math/9907204>.
- Related work uses Erdős’s convenient-prime mechanism to preserve complete preimage patterns; it is relevant background, not a resolution of this target: <https://math.dartmouth.edu/~carlp/monotone4-1.pdf>.

Treat the following as conjectural/open, not as established background: the canonical target itself; any assertion that all preimages of a constructed totient satisfy a desired divisibility condition unless a complete proof is supplied; and any heuristic about shifted primes or smooth shifted primes.

## Complete resolutions

An affirmative resolution consists of a rigorous proof that for every \(C>0\) there is a totient \(a\) whose full inverse image \(\{n:\varphi(n)=a\}\) is contained in \((Ca,\infty)\). It must then prove that the selected \(a\)'s can be chosen distinct and tend to infinity.

A negative resolution consists of a rigorous absolute constant \(C>0\) and a proof that every totient \(a\) has at least one preimage \(n\le Ca\).

## What does not count as a solution

- A family with large constructed preimages but no proof that smaller preimages do not exist.
- A proof for one fixed constant only, including \(C=3\).
- A statement about the number of preimages that does not bound their minimum.
- A finite table, numerical search, heuristic density argument, or probabilistic model without a theorem reducing the required check to a finite certified search.
- An application of multiplicativity that silently assumes all inverse images have the constructed form.
- A result conditional on an unproved prime-distribution hypothesis, unless it is clearly labeled conditional and separated from a complete resolution.

## Required correctness checks

1. Define every candidate \(a\), every auxiliary set, and every asymptotic quantifier precisely.
2. For \(\varphi(n)=a\), justify a complete classification or exclusion of all possible prime factors of \(n\); do not only enumerate a preferred construction.
3. If a convenient-prime or lifting argument is used, prove both directions: every asserted preimage exists and no other preimage exists.
4. Check that inequalities use the least preimage \(n_*(a)\), not an arbitrary preimage.
5. Verify every passage between the unbounded-ratio, every-\(C\), sequence, and infinite-set formulations.
6. State dependencies on external theorems exactly, with theorem number, version, and URL. Audit whether their hypotheses hold in the proposed construction.
7. Treat the published forum claim rejected in January 2026 as invalid unless its missing minimality argument is independently repaired.

## Required deliverables

- A self-contained proof manuscript, or a self-contained disproof manuscript, with a concise dependency map.
- A lemma ledger marking each lemma as proved, imported, conditional, computationally certified, or open.
- An inverse-image audit for every central construction, including a proof of minimality.
- A literature note distinguishing the exact current target from Carmichael’s multiplicity-one conjecture.
- Source links for every external theorem; cite peer-reviewed versions where available and identify preprints as preprints.
- If incomplete, a sharply stated remaining lemma and an explanation of why it would suffice.

## Dynamic Multiagent v2 protocol

Maintain one research root and use at most four concurrent agents. Begin with independent approaches rather than assigning a fixed mathematical method. Keep an approach registry containing: target subclaim, definitions, dependencies, current status, attempted proof route, falsification tests, and owner.

Use multiple waves. In the first wave, split only genuinely independent tasks, such as a complete audit of inverse-totient classification constraints, a verification of relevant Ford/Erdős transfer lemmas, and an adversarial search for hidden small preimages. At each merge, the research root compares approaches, retires duplicated routes, and reallocates slots dynamically to the strongest unresolved lemma. No agent may declare progress solely from another agent’s summary: inspect the actual derivation or cited source.

Reserve adversarial proof checking throughout. A checker must attempt to construct an omitted smaller preimage, challenge every claimed exhaustive case split, test quantifier changes, and verify all imported theorem hypotheses. If a proof candidate survives one checker, send it to a fresh checker with no commitment to the approach.

Allocate resources proof-first. At most one optional computational subtask may run at a time. Before it runs, record the exact lemma it tests, all hypotheses, the finite search domain, the certification method for completeness, and a stopping condition. Immediately return that slot to proof work once the question is answered. Computation may refute a proposed lemma or certify a finite residue of a proved reduction; it may not substitute for an infinite argument.

## Persistence and resumability

Maintain `research_state.md` after each substantive wave. It must contain the canonical target, verified sources, approach registry, proved lemmas with locations, rejected arguments and counterexamples, open dependencies, and the next smallest proof obligation.

If execution ends before a complete affirmative or negative proof is independently checked, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`. Preserve exact citations, theorem versions, and the current adversarial-check status so a later research root can resume without treating a partial argument as a solution.
