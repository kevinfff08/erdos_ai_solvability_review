# Erdős Problem 572 — fixed-length even-cycle Turán lower bound

## Definitions and canonical target

For a finite simple undirected graph \(H\), let \(\operatorname{ex}(n,H)\) be the maximum number of edges in a finite simple graph on exactly \(n\) vertices containing no subgraph isomorphic to \(H\). A copy need not be induced. Let \(C_m\) denote a simple cycle of length \(m\).

Canonical target: prove that, for every fixed integer \(k\ge 3\), there are constants \(c_k>0\) and \(n_0(k)\) such that

\[
\operatorname{ex}(n,C_{2k})\ge c_k n^{1+1/k}\qquad\text{for every integer }n\ge n_0(k).
\]

Equivalently, \(\operatorname{ex}(n,C_{2k})=\Omega_k(n^{1+1/k})\). Quantify \(k\) before \(n\): the constants may depend on \(k\), never on \(n\). The cases \(k=3\) and \(k=5\) are established, so the active target is every fixed \(k\ge4\) with \(k\ne5\), beginning with \(k=4\) (the \(C_8\) case).

## Accepted background

- Bondy and Simonovits proved the matching-exponent upper bound \(\operatorname{ex}(n,C_{2k})=O_k(n^{1+1/k})\): [Cycles of even length in graphs (1974)](https://doi.org/10.1016/0095-8956(74)90052-5).
- Pikhurko proved \(\operatorname{ex}(n,C_{2k})\le (k-1)n^{1+1/k}+16(k-1)n\): [A Note on the Turán Function of Even Cycles (2012)](https://doi.org/10.1090/S0002-9939-2012-11274-2).
- Benson's girth-8 and girth-12 constructions establish the required order for \(k=3\) and \(k=5\): [Minimal Regular Graphs of Girths Eight and Twelve (1966)](https://doi.org/10.4153/CJM-1966-109-8).
- General algebraic constructions yield weaker lower exponents; see Lazebnik, Ustimenko and Woldar, [Polarities and 2k-cycle-free graphs (1999)](https://doi.org/10.1016/S0012-365X(99)90107-3).
- Conlon gives a geometric interpretation of Wenger constructions and verifies the target order for \(k=2,3,5\): [Extremal Numbers of Cycles Revisited (2021 preprint)](https://arxiv.org/abs/2011.11064).
- A 2026 peer-reviewed source still states that matching lower bounds for ordinary \(\operatorname{ex}(n,C_{2k})\) are known only for \(k=2,3,5\): Byrne and Tait, [New constructions and bounds for nonabelian Sidon sets with applications to Turán-type problems](https://doi.org/10.4153/S0008414X26102314).

These are accepted theorems/background, not a prescribed method. In particular, results about rainbow, ordered, directed, hypercube, induced, or multiple-forbidden-cycle variants are not results about this target unless a complete reduction is supplied.

## Complete resolutions

An affirmative resolution supplies a rigorous proof that, for every fixed unresolved \(k\), suitable \(c_k,n_0(k)\) exist and the stated lower bound holds for every \(n\ge n_0(k)\).

A negative resolution supplies a rigorous proof that for some fixed \(k\ge3\), \(\operatorname{ex}(n,C_{2k})\notin\Omega(n^{1+1/k})\); equivalently, the normalized ratio has no eventually positive lower bound.

## What does not count as a solution

- Reproving the known \(k=3\) or \(k=5\) cases.
- A graph that contains \(C_{2k}\), or a proof only excluding a different kind of cycle.
- A lower bound with a smaller exponent.
- A construction on special sizes without a proof covering every sufficiently large \(n\).
- A theorem about a related Turán function without a valid implication to ordinary \(C_{2k}\)-freeness.
- Numerical evidence, an exhaustive search at bounded order, or a heuristic algebraic pattern without a general certificate.

## Required correctness checks

1. State all quantifiers, especially whether \(k\) is fixed and what each constant depends on.
2. Verify that graphs are finite, simple, undirected, and that the forbidden object is a non-induced simple \(C_{2k}\).
3. For every construction, prove the vertex count and edge count and prove the absence of \(C_{2k}\), including degenerate parameter cases.
4. If using field/geometry parameters, prove that distinct parameters give the claimed objects and that all exceptional characteristics/orders are handled.
5. If using a subsequence of orders, provide a valid extension argument to every sufficiently large \(n\) with constants preserved.
6. Audit every imported lemma against its exact forbidden-family convention.
7. Have an independent adversarial checker try to construct the forbidden cycle from every alleged local configuration.

## Required deliverables

- A self-contained theorem statement with all quantifiers.
- A dependency map of cited lemmas, each with a direct primary-source URL and a precise statement actually used.
- A complete proof or disproof, with separate verification of graph size, edge count, and cycle exclusion.
- A short comparison table distinguishing this target from high-girth, rainbow, ordered, bipartite Zarankiewicz, and hypercube variants.
- If incomplete: a rigorous partial theorem, a clearly identified blocking lemma, failed approaches with failure modes, and an updated research-state checkpoint. Do not label partial work as a solution.

## Dynamic Multiagent v2 protocol

Maintain one research root responsible for the canonical statement, the evidence ledger, and final integration. At most four agents, including the root, may run concurrently.

Begin with multiple genuinely independent lines of inquiry selected dynamically from the evidence; do not lock agents into a static mathematical method. Before substantial work, register each approach in an approach registry containing: target \(k\) or parameter regime, precise intended lemma, assumptions, prior results used, expected certificate, and a falsification test. Do not duplicate an active approach unless the root records a concrete reason.

Use multiple waves. After each wave, the root compares proof obligations and evidence, retires disproved routes, and reuses slots for the most informative unresolved lemma. Every candidate proof receives adversarial checking by an agent not responsible for its construction. The checker must inspect quantifiers, graph simplicity, all parameter exceptions, the exact \(C_{2k}\)-exclusion claim, and the all-large-\(n\) extension.

Allocate resources proof-first. At most one optional computational subtask may run at once. Before it starts, record in the registry: the exact lemma/hypothesis being tested, finite input range, certificate to retain, and a stopping condition that answers a defined question. Immediately release and reassign that slot after the question is answered. Computation may generate or refute a lemma; it cannot substitute for the asymptotic proof.

## Persistence and resumability

The root must maintain `research_state.md` after each meaningful wave. It must record the canonical target, source ledger, approach registry, proved lemmas, rejected claims and counterexamples, open proof obligations, active tasks, and the next smallest checkable step.

If a runtime boundary occurs before a complete audited resolution, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, preserve all certificates and citations, and return only the checkpoint status plus the exact next proof obligation. Do not present an incomplete investigation as a solution.
