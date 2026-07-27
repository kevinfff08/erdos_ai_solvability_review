# Erdős Problem 74 — research prompt

## Definitions and canonical target

Work in ZFC with simple undirected graphs.  For a finite graph \(H\), define
\[
b(H):=\min\{|D|:D\subseteq E(H)\text{ and }H-D\text{ is bipartite}\}.
\]
Thus \(b(H)\) is the minimum odd-cycle edge-transversal size.

Prove or disprove the following exact statement:

> For every function \(f:\mathbb N\to\mathbb N\) satisfying \(f(n)\to\infty\), there exists a graph \(G=G_f\) with infinite chromatic number such that \(b(H)\le f(|V(H)|)\) for every finite subgraph \(H\subseteq G\).

“Infinite chromatic number” means that \(G\) has no finite proper vertex-colouring; it does not mean that \(|V(G)|\) is uncountable, nor that \(\chi(G)=\aleph_1\). Subgraphs are arbitrary finite edge-subgraphs. It is harmless, but must be justified, to work with induced subgraphs because deleting edges cannot increase \(b\).

The quantifier order is \(\forall f\,\exists G_f\,\forall H\). No monotonicity of \(f\) is assumed.

## Accepted background

- Erdős, Hajnal, and Szemerédi introduced this family of almost-bipartite large-chromatic-graph questions: [1982 primary paper](https://users.renyi.hu/~p_erdos/1982-11.pdf).
- Rödl's 1982 paper is the source for the known near-bipartite constructions: [Nearly bipartite graphs with large chromatic number](https://doi.org/10.1007/BF02579434). The current problem record reports a graph result for every fixed linear budget \(f(n)=\epsilon n\), and a corresponding 3-uniform-hypergraph result: [current record](https://www.erdosproblems.com/74). Treat the exact theorem wording as something to inspect before relying on it.
- The residual graph problem is publicly recorded as open even for \(f(n)=\sqrt n\): [Problem 74](https://www.erdosproblems.com/74). This is background status, not a proof of openness.
- Lambie-Hanson proved a different result about the rate at which chromatic numbers of finite subgraphs can grow: [arXiv:1902.08177](https://arxiv.org/abs/1902.08177), published in [Advances in Mathematics 369 (2020)](https://doi.org/10.1016/j.aim.2020.107176). It controls finite-subgraph chromatic number, not \(b(H)\); do not cite it as a solution to this target.
- A statement-only Lean formalization of the intended quantifiers is available at [ErdosProblems/74.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/74.lean). It contains `sorry` and supplies no proof.

## Complete resolutions

An affirmative resolution is a ZFC proof that every diverging \(f\) has a witnessing \(G_f\), including a proof that \(\chi(G_f)\) is infinite and a uniform proof of \(b(H)\le f(|V(H)|)\) for every finite \(H\subseteq G_f\).

A negative resolution is a ZFC construction of one diverging \(f\) together with a proof that every infinite-chromatic graph \(G\) contains a finite \(H\subseteq G\) with \(b(H)>f(|V(H)|)\).

## What does not count as a solution

- A result only for \(f(n)=\epsilon n\), for one convenient \(f\), or for the hypergraph analogue.
- A proof for \(f(n)=\sqrt n\) presented as a proof for all diverging \(f\); it is important partial progress, not the full theorem.
- A construction with large vertex cardinality but finite chromatic number.
- A claim based only on large odd girth, slowly growing finite-subgraph chromatic number, or a bound on the number of odd cycles. Each must be converted into the required bound on \(b(H)\).
- A result for induced subgraphs without the reduction to all finite subgraphs.
- A model-dependent statement under CH, diamond, forcing axioms, or another additional assumption presented as a ZFC answer.
- Finite experiments, heuristic random constructions, or unverified AI-generated arguments without a finite lemma and complete proof.

## Required correctness checks

1. State every quantifier and ensure the constructed graph may depend on \(f\), but not on \(H\).
2. Define the deletion set \(D\) for each finite \(H\), prove \(|D|\le f(|V(H)|)\), and prove \(H-D\) bipartite.
3. Prove infinite chromatic number independently; do not infer it from infinite order.
4. Check that the argument tolerates arbitrary, possibly nonmonotone, diverging \(f\).
5. Check small \(n\), integer rounding, and the exact interpretation of a finite subgraph.
6. Identify every external theorem used with a stable link and a precise statement; inspect the original source for Rödl-type claims.
7. Subject any candidate proof to an adversarial audit seeking a finite subgraph violating the proposed budget, a hidden extra set-theoretic axiom, or a quantifier swap.

## Required deliverables

Produce:

1. `research_state.md` containing the target, sources checked, the approach registry, proved lemmas, rejected routes, and unresolved gaps.
2. A literature note distinguishing the 1982 results, the exact Rödl theorem used, and the distinct Lambie-Hanson finite-chromatic-growth result.
3. A proof manuscript or a disproof manuscript with all definitions and quantified claims self-contained.
4. A lemma ledger: each lemma, hypotheses, dependencies, proof status, and an adversarial-check result.
5. If incomplete, a precise checkpoint identifying the strongest proved statement and the first missing implication. Do not phrase a partial result as a resolution.
6. Bibliographic citations with author, title, year, venue/status, theorem/page or section where possible, and direct URLs. Cite primary sources rather than search snippets.

## Dynamic Multiagent v2 protocol

Maintain one research root and run at most four concurrent agents total. Begin with independent approaches rather than a fixed division of labour. Before substantive work, add each attempted route to an approach registry in `research_state.md`, recording: target subclaim, relevant sources, expected bridge lemma, assumptions, and falsification test.

Use multiple waves. In the first wave, obtain independent analyses of: the exact known Rödl bounds; possible positive construction invariants controlling \(b(H)\); possible negative/compactness obstructions; and a hostile statement-and-literature audit. Do not assign these permanently: after each wave, compare evidence and reuse slots dynamically for the most informative unresolved branch.

Every proposed theorem passes to a different agent for adversarial proof checking. That checker must attempt counterexamples, inspect quantifier order, test the passage from induced to arbitrary subgraphs, and list unproved external inputs. A route with a failed bridge lemma is marked rejected or conditional in the registry; its slot is immediately reused.

Proof work has priority. At most one computational subtask may run at once, and only after the registry declares its exact lemma, hypotheses, finite search domain, certificate format, and stopping condition. When that question is answered, reassign the slot immediately to proof verification or a new proof route. Computation may discover or falsify a finite auxiliary pattern; it cannot certify the infinite target by itself.

## Persistence and resumability

Update `research_state.md` after each material result, source inspection, failed proof attempt, or adversarial check. Preserve exact statements, dependency links, and the reason each route remains live or is rejected.

If a runtime boundary occurs before a complete resolution, stop cleanly with `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`. Include the active target, all verified lemmas, unverified claims, source URLs, the approach registry, and the next smallest proof obligation. On resumption, verify the checkpoint against the cited primary sources before extending any argument.
