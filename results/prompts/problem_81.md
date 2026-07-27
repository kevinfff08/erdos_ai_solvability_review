# Erdős Problem 81: chordal edge-clique partitions

## Definitions and canonical target

Work with finite simple graphs. A graph is **chordal** if it has no induced cycle of length at least four.

For a graph \(G\), define \(\operatorname{cp}(G)\) to be the minimum \(k\) such that there are cliques \(C_1,\ldots,C_k\), each containing at least one edge, for which
\[
E(G)=\bigsqcup_{i=1}^k E(G[C_i]).
\]
Thus cliques may overlap in vertices, but every edge must belong to exactly one chosen clique.

Canonical target: prove or refute the existence of an absolute constant \(C\) such that, for every \(n\ge 1\) and every \(n\)-vertex chordal graph \(G\),
\[
\operatorname{cp}(G)\le \frac{n^2}{6}+Cn.
\]

## Accepted background

- Erdős, Ordman, and Zalcstein proved that some absolute \(c>0\) gives \(\operatorname{cp}(G)\le (1-c)n^2/4\) for every \(n\)-vertex chordal graph. Their abstract also records that the \(n^2/6\) threshold was open. Treat this as a theorem, subject to checking the full paper before using proof details: [Cambridge record](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/clique-partitions-of-chordal-graphs/CEA1F929F2A88B5A4C7C8E23DFD0DD29).
- Chen, Erdős, and Ordman proved \((3/16)n^2+O(n)\) for split graphs. Their paper states that for \(6\mid n\), \(K_n-\overline K_{2n/3}\) has \(\operatorname{cp}=n^2/6+n/6\). This is a lower-bound family for the canonical target: [author-hosted paper PDF](https://ordman.net/MathResearch/CEOClique_Parts.pdf).
- Recent public work on fractional triangle packing/covering, even when accompanied by Lean artifacts, does **not** establish the integral edge-clique-partition target. Its own scope disclaimer must be respected: [research repository](https://github.com/jtraverso/erdos-81-chordal-clique-partitions).
- A 2026 forum note claims only a conditional result under wCDH and is not a proof of the unrestricted theorem: [discussion thread](https://www.erdosproblems.com/forum/thread/81).

Do not assume any more detailed theorem from these sources without locating the theorem statement and checking its hypotheses.

## Complete resolutions

An affirmative resolution is a self-contained proof of one absolute \(C\) that works for every finite chordal graph.

A negative resolution is a proof that no such \(C\) exists: equivalently, an infinite sequence \(G_i\) of chordal graphs for which
\[
\frac{\operatorname{cp}(G_i)-|V(G_i)|^2/6}{|V(G_i)|}
\]
is unbounded.

## What does not count as a solution

- Covering every edge by cliques while allowing an edge to appear twice.
- Partitioning vertices into cliques instead of partitioning edges.
- A bound with a leading quadratic coefficient larger than \(1/6\).
- A result only for split, threshold, interval, or other proper subclasses without a valid theorem reducing all chordal graphs to that class.
- A fractional packing/covering result without an integral rounding theorem whose loss is \(O(n)\).
- A theorem conditional on an unproved hypothesis.
- Exhaustive computation on bounded \(n\), a timestamped claim, or a proof still unavailable for inspection.

## Required correctness checks

- Verify that every selected set is a clique and that its full induced edge set is used.
- Prove pairwise edge-disjointness and exact coverage of \(E(G)\); checking only the number of cliques is insufficient.
- Establish chordality of every construction, preferably by an induced-cycle argument or a perfect elimination ordering.
- State all rounding conventions and show the linear error has one absolute constant.
- For a structural reduction, quantify every separator/clique-sum interface edge and prove the partition objective is preserved or charged correctly.
- For any fractional argument, identify the exact integrality statement needed and prove it rather than silently invoking LP duality or a packing-to-partition conversion.
- Compare any proposed extremizer with \(K_n-\overline K_{2n/3}\), while recognizing that matching this family does not prove global optimality.

## Required deliverables

1. A source ledger separating peer-reviewed theorems, preprints, formal artifacts, forum claims, and unverified claims, with direct URLs and inspected theorem locations.
2. A self-contained affirmative proof or counterexample-family proof satisfying the completion condition.
3. A lemma ledger: statement, hypotheses, proof status, dependencies, and explicit counterexamples to every rejected lemma.
4. A partition certificate format for each constructive step, showing each graph edge is assigned exactly once.
5. If incomplete, a precise account of the strongest proved reduction or obstruction, why it falls short, and the smallest next decisive lemma.

## Dynamic Multiagent v2 protocol

Maintain one research root and use at most four concurrent agents total. Begin with genuinely independent approaches; do not preassign a permanent method. Before substantial work is merged, record each approach in an approach registry with its target claim, definitions, assumptions, dependency chain, falsification test, and current status.

Use multiple waves. In an early wave, diversify among structural induction via perfect elimination/clique trees, extremal reduction attempts, integral-versus-fractional rounding, and adversarial counterexample construction. As soon as an approach is decisively blocked or a lemma is settled, reassign its slot to the most discriminating unresolved question. Do not maintain idle or duplicate agents.

Every proposed proof must receive adversarial checking by an agent not responsible for its main derivation. The adversarial review must explicitly test: partition versus cover, all separator-interface edges, uniformity of \(O(n)\), chordality, integral versus fractional claims, and hidden restrictions to a subclass.

Allocate proof work first. At most one optional computational subtask may run at a time. Before it starts, write the exact lemma or counterexample question, graph-generation hypotheses, certificate to be produced, and finite stopping condition. Immediately release and reuse the computational slot once that question is answered. Computation may reject a structural lemma or produce a certificate; it may not be used as evidence for the all-\(n\) target without a proof.

## Persistence and resumability

Maintain `research_state.md` at the research root. It must contain the canonical definitions, source ledger, approach registry, theorem/lemma ledger, counterexamples, failed routes, computation declarations and outcomes, pending verification, and the next smallest decisive task.

Checkpoint after each wave and before any runtime boundary. If the investigation is incomplete at a boundary, save the state and return `CHECKPOINT_NOT_FINAL`, identifying the exact incomplete claim and the next action. Never convert a partial theorem, a conditional result, or an unreviewed claim into a claimed resolution.
