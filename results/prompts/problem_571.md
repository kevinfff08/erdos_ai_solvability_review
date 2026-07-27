# Erdős Problem 571: inverse rational Turán exponent conjecture

## Definitions and canonical target

For a finite simple graph \(G\), let \(\operatorname{ex}(n,G)\) be the largest number of edges in a finite simple graph on \(n\) vertices that contains no (ordinary, non-induced) subgraph isomorphic to \(G\). A rational \(\alpha\) is a Turán exponent if some finite simple bipartite \(G\) satisfies \(\operatorname{ex}(n,G)=\Theta(n^\alpha)\).

Canonical target: prove that for every \(\alpha\in\mathbb{Q}\cap(1,2)\), there is a finite simple bipartite graph \(G_\alpha\) and constants \(c,C>0\), \(n_0\), such that \(c n^\alpha\le\operatorname{ex}(n,G_\alpha)\le C n^\alpha\) for every \(n\ge n_0\). Constants and \(G_\alpha\) may depend on \(\alpha\), not on \(n\). The endpoint \(\alpha=1\) is already elementary: \(G=P_3\) gives \(\operatorname{ex}(n,P_3)=\lfloor n/2\rfloor\).

## Accepted background

- The target is currently listed open, with no forum solution claims: <https://www.erdosproblems.com/forum/thread/571>. This is status evidence, not a proof of openness.
- Bukh and Conlon proved the finite-family analogue: for every rational \(r\in(1,2)\), a finite graph family \(\mathcal H_r\) has \(\operatorname{ex}(n,\mathcal H_r)=\Theta(n^r)\). This is a theorem, but it does **not** yield a single forbidden graph. See <https://arxiv.org/abs/1506.06406> and the published record <https://authors.library.caltech.edu/records/fjteg-4ys50>.
- Kang, Kim, and Liu proved specified families of single-graph exponents and showed that their subdivision conjecture would imply the full rational-exponent conjecture. The implication is conditional, not a resolution: <https://arxiv.org/abs/1811.06916>.
- Verified examples of subsequent single-graph progress include Conlon--Janzer, *Rational exponents near two* (2022), <https://www.advancesincombinatorics.com/article/57310-rational-exponents-near-two>, Conlon--Janzer--Lee on subdivisions, <https://arxiv.org/abs/1903.10631>, and Jiang--Qiu, *Many Turán exponents via subdivisions* (2023), <https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/many-turan-exponents-via-subdivisions/3AF62F3C0AAEA4C1EFE0C7CC5D41CA24>.
- Recent work remains partial: a 2025 induced-family theorem is not the present non-induced single-graph target (<https://arxiv.org/abs/2506.09020>), and a 2026 feedback-vertex-number paper supplies particular further exponents rather than all rationals (<https://arxiv.org/abs/2607.07157>).

Do not assume any unquoted theorem beyond what you independently inspect and cite. Clearly label every use as a proved theorem, a conditional implication, or a conjecture.

## Complete resolutions

An affirmative resolution must provide, for every rational \(\alpha\in(1,2)\), a finite simple bipartite \(G_\alpha\) and complete proofs of both asymptotic bounds \(\operatorname{ex}(n,G_\alpha)=O(n^\alpha)\) and \(\operatorname{ex}(n,G_\alpha)=\Omega(n^\alpha)\), with all parameter restrictions discharged.

A negative resolution must specify a rational \(\alpha\in(1,2)\) and prove that **no** finite simple bipartite graph \(G\) has \(\operatorname{ex}(n,G)=\Theta(n^\alpha)\). It must prove the universal obstruction over all such \(G\), not merely defeat one construction.

## What does not count as a solution

- A construction for a finite forbidden family instead of one graph.
- An induced-forbidden result, a host-restricted result, or a multigraph/hypergraph result without a valid reduction to this target.
- Only an upper bound, only a lower bound, a logarithmic-gap estimate, or a result on a subsequence of \(n\) without a valid extension.
- Any parametrized family that does not demonstrably cover every rational in \((1,2)\).
- A proof that a conjectural subdivision principle would imply the target, unless that principle is itself proved in the required generality.
- Exhaustive small-graph computation, numerical fitting, or a database search without an asymptotic proof.

## Required correctness checks

1. Fix the exact rational \(\alpha=a/b\) in lowest terms and state which graph is forbidden.
2. Verify that \(G_\alpha\) is finite, simple, and bipartite.
3. Audit ordinary subgraph containment versus induced containment, and the direction of every forbidden-subgraph monotonicity inequality.
4. Prove both bounds with constants independent of \(n\); state the threshold \(n_0\).
5. For rooted graphs, blow-ups, and subdivisions, verify all balance, root-identification, edge-disjointness, density, and integrality hypotheses before invoking a lemma.
6. Compare the exact exponent and parameter region with the cited literature to establish novelty.
7. Subject every proposed proof to an adversarial check that tries to construct a counterexample to each embedding/counting claim and recomputes every exponent algebraically.
8. If an argument purports to unite a forbidden family into one graph, explicitly prove why avoidance of the proposed one graph is equivalent to the relevant family avoidance; do not rely on intuition.

## Required deliverables

- A concise `status_and_scope.md` with the canonical target, the precise chosen subtarget, and links to every source used.
- An `approach_registry.md` recording attempted routes, hypotheses, dependency graph, result status, and duplication checks.
- A proof manuscript in which every external theorem has a precise citation and every new lemma has a full proof or an explicitly labeled gap.
- A two-column table mapping each claimed bound to its exact graph, exponent, theorem/lemma, and hypothesis check.
- An adversarial audit listing rejected arguments, failed edge cases, and the final verification outcome.
- If incomplete, a rigorous partial-progress report identifying the first unproved lemma and why it would materially advance the target.

## Dynamic Multiagent v2 protocol

Create a research root that owns the canonical statement, source registry, and the evolving `approach_registry.md`. Use at most four concurrent agents total, including the coordinator. Begin with independent approaches rather than a fixed division of labor; register an approach before substantial work and immediately merge duplicate efforts.

Run multiple waves. In each wave, allocate agents to non-overlapping mathematical questions, such as a candidate-graph lower bound, a candidate-graph upper bound, a conditional reduction, or adversarial auditing. Reuse a freed slot dynamically for the highest-value unresolved dependency, not for a predetermined role. The coordinator must compare intermediate claims against the registry and redirect work if two approaches secretly rely on the same unproved assertion.

Every nontrivial claimed lemma receives adversarial proof checking by an agent that did not originate it. A checker must attempt parameter counterexamples, containment-direction reversals, and exponent recalculation. A claim is not promoted to accepted background until its hypotheses, source, and proof status are recorded.

Allocate resources proof-first. At most one optional computational subtask may run at a time. Before it runs, record the exact lemma or conjecture it tests, its input class, its stopping condition, and why a positive or negative result changes the proof plan. When that question is answered, terminate or archive the computation and reassign the slot immediately to proof work. Computation may never substitute for an asymptotic proof.

## Persistence and resumability

Maintain `research_state.md` after each wave: date, canonical target, sources inspected, accepted lemmas, rejected claims, open dependencies, active approach registry, and the next smallest checkable task. Preserve exact parameter conventions and links so a new agent can audit the work without relying on conversation memory.

If a runtime boundary arrives before a complete affirmative or negative resolution, do not present a solution. Write `CHECKPOINT_NOT_FINAL` in `research_state.md`, identify the first unresolved proof obligation, save all counterexamples or failed checks, and resume from that checkpoint in the next wave.
