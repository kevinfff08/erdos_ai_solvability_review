# Erdős Problem 82 — research prompt

## Definitions and canonical target

Work with finite simple undirected graphs.  For a graph \(G\), define
\[
r(G)=\max\{|S|:S\subseteq V(G),\;G[S]\text{ is }d\text{-regular for some }0\le d\le |S|-1\},
\]
and
\[
F(n)=\min_{|V(G)|=n}r(G).
\]
The target is to prove
\[
\lim_{n\to\infty}\frac{F(n)}{\log n}=+\infty.
\]
Equivalently, for every \(C>0\), every sufficiently large \(n\)-vertex graph has an induced regular subgraph on at least \(C\log n\) vertices.  Independent sets and cliques count: 0-regular subgraphs are allowed.  The logarithm base is fixed and greater than 1.

## Accepted background

The current database record is [Erdős Problem 82](https://www.erdosproblems.com/82) and its [LaTeX record](https://www.erdosproblems.com/latex/82).  Ramsey theory proves only \(F(n)\gg\log n\).  This is a theorem-level baseline, not the conjecture.

The record cites Alon, Krivelevich, and Sudakov, [*Large nearly regular induced subgraphs* (2007)](https://arxiv.org/abs/0710.2106), for related upper-bound progress.  Do not infer exact regularity from “nearly regular” without a proved conversion.

The recent preprint Dyson and McKay, [*Ramsey numbers for regular induced subgraphs* (2026)](https://arxiv.org/abs/2604.08215), is reported by the database to establish \(F(n)\ll\sqrt n\) and lower bounds for the inverse function \(G(k)\).  Those are constraints and adversarial examples; they do not establish the target lower bound.  Re-read the primary preprint before relying on any theorem statement.

The problem is historically attributed to Erdős, Fajtlowicz, and Stanton.  Treat all claims beyond the linked sources as unverified until independently located and checked.

## Complete resolutions

An affirmative resolution is a rigorous uniform proof that for every real \(C>0\) there is \(N(C)\) such that every graph on \(n\ge N(C)\) vertices has an induced exactly regular subgraph of order at least \(C\log n\).

A negative resolution is a fixed finite \(C\), an unbounded sequence \(n_i\), and rigorously verified graphs \(G_i\) on \(n_i\) vertices for which every induced regular subgraph has at most \(C\log n_i\) vertices.  This is the logical negation of the target.

## What does not count as a solution

- A fixed-constant lower bound \(F(n)\ge c\log n\).
- A result only for random, regular, dense, sparse, or otherwise restricted graphs.
- A merely nearly regular induced subgraph.
- A non-induced regular subgraph obtained by deleting edges.
- Finite computation of \(F(n)\) or \(G(k)\) without a general theorem.
- An asymptotic argument with constants or thresholds depending on the input graph.
- An upper-bound construction for \(F\) alone.

## Required correctness checks

1. Preserve the quantifier order \(\min_G\max_S\).
2. Check that every claimed witness is induced and exactly \(d\)-regular.
3. Include \(d=0\); do not exclude independent sets or singleton witnesses.
4. Distinguish degrees in \(G[S]\) from degrees in \(G\).
5. Audit every asymptotic assertion with explicit uniform constants and an eventual threshold.
6. For a counterexample family, prove exclusion of *all* induced regular subgraphs, not merely a selected degree or size range.
7. Independently cross-check use of the 2026 preprint against the primary text and version history.

## Required deliverables

Provide a self-contained proof or disproof, with every external theorem cited by stable URL and exact statement.  Include a definitions ledger, a dependency graph of lemmas, a quantifier audit, and a short adversarial review explaining why the argument does not merely prove a Ramsey bound or a near-regular result.  If incomplete, provide the strongest proved lemma, its exact hypotheses, failed approaches, and the precise remaining implication.

## Dynamic Multiagent v2 protocol

Maintain one research root and `research_state.md`.  Use at most four concurrent agents, with early waves deliberately exploring independent approaches rather than a fixed division of labor.  Keep an approach registry recording: target lemma, assumptions, status, dependencies, counterexamples checked, and next falsifiable test.

Run multiple waves.  In each wave, the root selects complementary active approaches from the registry, reserves one slot for adversarial proof checking when a substantive claim appears, and reuses any freed slot dynamically for the most informative unresolved branch.  Agents may propose new methods, but must first state a precise claim and how it would imply the canonical target or its negation.

Use proof-first allocation.  At most one computational subtask may run at a time; before it starts, record the exact lemma or hypothesis being tested, graph class, certificate format, and stopping condition.  Once that question is answered, immediately release and reassign the slot.  Computation may falsify or certify a bounded lemma but may not substitute for the asymptotic proof.

## Persistence and resumability

Update `research_state.md` after every wave with sources checked, theorem statements verified, active registry entries, proof dependencies, failed ideas, and the next smallest checkable task.  Preserve counterexamples and proof-audit objections.  If a runtime boundary interrupts work before a complete resolution, write `CHECKPOINT_NOT_FINAL` and resume from the recorded state; do not present conjectural progress as a solution.
