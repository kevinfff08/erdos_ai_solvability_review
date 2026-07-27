# Erdős Problem 98 — research prompt

## Definitions and canonical target

For every integer \(n\ge 2\), define
\[
h(n)=\min_{\substack{P\subset\mathbb R^2,\\ |P|=n,\\ \text{no three points of }P\text{ are collinear},\\ \text{no four points of }P\text{ are cocircular}}}|D(P)|,
\qquad
D(P)=\{\|p-q\|_2:p,q\in P,\ p\ne q\}.
\]
A cocircular quadruple means four distinct points lying on one nondegenerate Euclidean circle. Determine whether
\[
\lim_{n\to\infty}\frac{h(n)}n=+\infty.
\]

The target is a universal asymptotic lower bound. Its exact negation is: there exist a constant \(C<\infty\), an unbounded sequence \(n_j\), and admissible sets \(P_j\) of size \(n_j\) such that \(|D(P_j)|\le Cn_j\).

## Accepted background

- Erdős, Hickerson, and Pach formulated this general-position quantity \(G(n)\), recorded \(G(n)\ge (n-1)/3\), and explicitly asked whether \(G(n)/n\to\infty\): [A problem of Leo Moser about repeated distances on the sphere (1989)](https://www.renyi.hu/~p_erdos/1989-02.pdf).
- The elementary rounded form \(h(n)\ge\lceil(n-1)/3\rceil\) follows by fixing a point: every circle centred there contains at most three other points.
- Erdős, Füredi, Pach, and Ruzsa constructed general-position planar sets with \(h(n)\le n\exp(C\sqrt{\log n})\): [The grid revisited (1993)](https://doi.org/10.1016/0012-365X(93)90155-M). This is an upper bound, not a disproof of the target.
- The current problem record remains open: [Erdős Problems #98](https://www.erdosproblems.com/98).
- Nearby forbidden-pattern results must not be substituted for this target. In particular, [Dumitrescu (2008)](https://doi.org/10.1007/s10998-008-8165-4), [Tao (2024/2025)](https://arxiv.org/abs/2409.01343), and [Grayzel (2026)](https://arxiv.org/abs/2601.09102) concern non-equivalent restrictions.

## Complete resolutions

An affirmative resolution must prove: for every \(M>0\), there exists \(N(M)\) such that every \(n\ge N(M)\) and every admissible \(P\) have \(|D(P)|\ge Mn\).

A negative resolution must give one finite \(C\) and admissible examples for arbitrarily large \(n\) with \(|D(P)|\le Cn\). The construction must be explicit or existential with a complete proof of all three properties: cardinality, no collinear triples/no cocircular quadruples, and the uniform linear distance bound.

## What does not count as a solution

- Reproving \(h(n)\ge cn\) for a fixed \(c\), including \(\lceil(n-1)/3\rceil\).
- Improving only constants in a linear lower bound.
- Repeating the EFPR upper bound or producing any \(n^{1+o(1)}\) upper bound that is not \(O(n)\).
- A point set with a collinear triple or cocircular quadruple.
- A theorem for no isosceles triangles, \(\Phi(4,3)\), \(\Phi(4,5)\), no parallelograms, convex position, or no-four-cocircularity alone without a proved implication to the exact hypotheses.
- Finite searches, floating-point experiments, or heuristic perturbation arguments without a theorem uniform in \(n\).

## Required correctness checks

1. State all quantifiers and constants explicitly; distinguish an all-\(n\) claim from a subsequence construction.
2. For every proposed construction, certify no three collinear and no four cocircular exactly, not numerically or generically by assertion.
3. Count distinct distances rather than pairs of points; identify why every claimed equality of lengths survives each transformation.
4. For projection arguments, characterize and avoid the exceptional projections, and separately prove the distance-count upper bound after projection.
5. For lower-bound arguments, identify precisely where the two general-position assumptions enter; a proof using only one should say so.
6. Independently attempt to falsify every pivotal lemma with small symbolic examples before relying on it.
7. Audit all literature claims against a primary paper or authoritative publication page; label preprints as preprints.

## Required deliverables

- A self-contained theorem statement and proof, or a precise proof-status report if incomplete.
- A lemma dependency graph, with every nonstandard lemma proved or cited by stable URL and exact theorem/location.
- For a construction: exact coordinates or an exact generation rule; a general-position certificate; and an asymptotic distance-count proof with constants.
- For a lower bound: a standalone derivation of the growth function and a comparison showing it is \(\omega(n)\).
- A literature appendix separating verified theorems, conjectures, and non-equivalent neighbouring variants.
- An adversarial audit identifying the strongest plausible failure mode and its resolution.

## Dynamic Multiagent v2 protocol

Maintain one research root and use at most four concurrent agents total. Begin with independent approaches rather than a fixed division of mathematical labour. Before substantial work, create an approach registry recording for each live line: target implication, key lemma, assumptions, expected falsifier, evidence status, and owner.

Use multiple waves. In each wave, let agents choose incompatible proof-first directions from the registry; reserve one slot for adversarial checking whenever a nontrivial lemma or construction appears. At each handoff, merge only claims with a written proof sketch and exact hypotheses. Reuse freed slots dynamically for the highest-information unresolved issue, not for repeating completed searches.

Every proposed decisive argument receives an independent proof audit by an agent that did not develop it. The audit must test quantifiers, asymptotic uniformity, degeneracies, hidden dependence of constants, and every use of no-three-collinear/no-four-cocircular. Failed approaches remain in the registry with their obstruction so later waves do not rediscover them.

Computation is proof-support only. At most one optional computational subtask may run at a time, and it must declare in advance: the exact lemma or candidate construction it tests, its hypotheses, exhaustive domain/certificate format, and a stopping condition. Stop and reassign that slot immediately once the stated question is answered; numerical pattern-finding is not evidence of resolution.

## Persistence and resumability

Keep `research_state.md` current after every wave. It must include the canonical target, source ledger, approach registry, proved lemmas, rejected lemmas with counterexamples, pending proof obligations, and the next highest-value checks.

If execution ends before a complete affirmative or negative proof has passed adversarial audit, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`. Include enough exact context—definitions, equations, source URLs, partial proof boundaries, and failed routes—for a later research root to resume without treating preliminary claims as established.
