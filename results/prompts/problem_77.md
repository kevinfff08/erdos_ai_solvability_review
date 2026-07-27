# Erdős Problem 77 — exponential-rate limit of diagonal Ramsey numbers

## Definitions and canonical target

For every integer k >= 1, let R(k)=R(k,k) be the least integer n such that every red-blue colouring of the edges of the complete graph K_n contains a red K_k or a blue K_k. Determine whether the full sequence a_k=R(k)^(1/k) converges as k tends to infinity. If it does, determine its limit.

The target is the ordinary limit over every integer k, not a limit along a subsequence. Equivalently, establish or refute equality of liminf a_k and limsup a_k.

## Accepted background

- The live problem record is [Erdős Problems 77](https://www.erdosproblems.com/77). It records the classical bounds sqrt(2) <= liminf a_k <= limsup a_k <= 4.
- Campos, Griffiths, Morris, and Sahasrabudhe proved that R(k) <= (4-epsilon)^k for some epsilon>0: [arXiv:2303.09521](https://arxiv.org/abs/2303.09521). This is a theorem about an upper bound, not a convergence theorem.
- Gupta, Ndiaye, Norin, and Wei obtained R(k,k) <= (3.8)^(k+o(k)): [arXiv:2407.19026](https://arxiv.org/abs/2407.19026). A recent paper expresses the associated base as 4 exp(-0.14/e), approximately 3.7992: [arXiv:2512.16062](https://arxiv.org/abs/2512.16062).
- Balister et al. proved a multicolour exponential upper-bound improvement; for two colours it gives another proof of the CGMS-type result: [arXiv:2410.17197](https://arxiv.org/abs/2410.17197), published in JAMS 2026, [record](https://ora.ox.ac.uk/objects/uuid%3A18dfcd97-a793-407e-a375-0de18d094646).
- The CGMS 4-epsilon upper bound has an Isabelle/HOL formalization: [Archive of Formal Proofs](https://isa-afp.org/entries/Diagonal_Ramsey.html). It does not settle the present limit problem.
- Araujo, Filipe, and Miyazaki treat existence of log R(k,k)/k as an assumption in a conditional connection to another Erdős problem: [arXiv:2512.16062](https://arxiv.org/abs/2512.16062). Do not treat their conditional theorem or the Ramsey Diagonal Conjecture as established background.

## Complete resolutions

An affirmative resolution proves a real number L such that for every epsilon>0 there is K for which |R(k)^(1/k)-L|<epsilon for every integer k>=K. It must also determine L, as requested by the problem.

A negative resolution proves liminf R(k)^(1/k) < limsup R(k)^(1/k), for example through rigorously separated exponential rates along two infinite subsequences.

## What does not count as a solution

- Improving only a global exponential upper or lower bound.
- Proving convergence only on a subsequence.
- Finite computation, numerical regression, or a heuristic candidate for L.
- A result for off-diagonal, multicolour, ordered, induced, or altered Ramsey numbers without a proved transfer to R(k,k).
- A conditional argument based on the Ramsey Diagonal Conjecture or any unproved comparison principle.
- A formalization of a one-sided bound.
- An unproved assertion that R(k) is submultiplicative, log R(k) is subadditive, or R(k)^(1/k) is monotone.

## Required correctness checks

1. State every asymptotic quantifier over all sufficiently large integer k; distinguish it from an infinite-subsequence statement.
2. Track o(k), rounding, and multiplicative errors after kth roots and through every iteration.
3. For every colouring construction, verify both colours and every forbidden clique size.
4. For every recursive, product, or substitution inequality, verify its direction, parameter transformation, colour count, and applicability to the same diagonal sequence.
5. If applying a Fekete-type lemma, prove its exact approximate subadditivity/submultiplicativity hypothesis and show its error survives iteration.
6. Cross-check each imported theorem against its primary source; explicitly label theorems, conjectures, and conditional deductions.
7. Subject every central lemma to an independent hostile proof audit.

## Required deliverables

Deliver a self-contained report containing: a precise claimed theorem; complete proofs of new lemmas; a dependency ledger separating proven, imported, conjectural, and conditional statements; an asymptotic-error ledger; an adversarial audit of the decisive construction or inequality; and linked citations with theorem/page identifiers.

If incomplete, report the strongest proved intermediate result, the exact missing lemma, and a falsification attempt for the leading route. Do not present a conjecture, numerical evidence, or conditional consequence as progress resolving the problem.

## Dynamic Multiagent v2 protocol

Create a research root and maintain an approach registry. Use at most four concurrent agents. Begin with independent, logically distinct investigations, but do not impose a fixed mathematical method or permanent role assignment.

For each live route, record its target lemma, exact assumptions, proof status, dependencies, overlap with other routes, and next falsification test. Use multiple waves. Reuse a slot immediately once a route is duplicated, decisively refuted, or reduced to a completed lemma. An agent other than an argument's originator must adversarially check every key proof.

Allocate proof-first. At most one computational subtask may run at one time, only after recording the precise lemma it tests, hypotheses, finite search/certificate format, and stopping condition. Computation may only support a bounded lemma or counterexample search; it may not extrapolate the asymptotic limit. Reassign that slot immediately when its declared question is answered.

## Persistence and resumability

Maintain `research_state.md` in the research root. At each checkpoint record the canonical target, sources checked, approach registry, proved results, rejected arguments and failure points, unresolved dependencies, and exact next actions.

If a runtime boundary occurs before a complete proof or disproof, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`, preserve proof drafts and citations, and resume from that state. Never convert an interrupted investigation into a claimed resolution.
