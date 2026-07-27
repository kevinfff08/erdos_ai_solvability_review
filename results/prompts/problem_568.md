# Erdős Problem 568 — Ramsey size-linearity from tree and clique tests

## Definitions and canonical target

Let \(G\) be a fixed finite graph. For finite graphs \(A,B\), \(R(A,B)\) is the least \(N\) such that every red-blue colouring of \(E(K_N)\) contains a red, non-induced copy of \(A\) or a blue, non-induced copy of \(B\).

The notation \(O_G(\cdot)\) means that the implied constant depends only on the fixed graph \(G\), not on \(n\), \(T\), \(H\), \(e(H)\), \(v(H)\), maximum degree, or a chosen decomposition.

Canonical target. Assume that:

1. \(R(G,T)\le C_T(G)|T|\) for one constant \(C_T(G)\), for every finite tree \(T\); and
2. \(R(G,K_n)\le C_K(G)n^2\) for one constant \(C_K(G)\), for every \(n\ge2\).

Prove or disprove that there is a constant \(C(G)\) such that
\[
R(G,H)\le C(G)e(H)
\]
for every finite graph \(H\) with no isolated vertices and \(e(H)\ge1\). This property is called *Ramsey size-linearity*.

Do not remove the no-isolated-vertices condition. Do not replace the target by an induced Ramsey problem, a size-Ramsey-number problem, or a result whose constant depends on \(H\).

## Accepted background

- The current problem record is [Erdős Problems #568](https://www.erdosproblems.com/568), which was edited on 2026-01-18 and labels the question open, while explicitly warning that this is not a complete literature certification. Its [forum thread](https://www.erdosproblems.com/forum/thread/568) had no comments at audit time.
- Erdős, Faudree, Rousseau and Schelp, [*Ramsey Size Linear Graphs*](https://doi.org/10.1017/S096354830000078X), Combinatorics, Probability and Computing 2 (1993), 389–399, defines Ramsey size-linearity and proves, among other results, sufficient size-linear and non-size-linear edge-density regimes.
- Bradač, Gishboliner and Sudakov, [*On Ramsey size-linear graphs and related questions*](https://arxiv.org/abs/2202.10388), SIAM J. Discrete Math. 38 (2024), proves special cases including Ramsey size-linearity of every \(K_4\)-subdivision with at least six vertices, and a bipartite-target result for \(K_4^*\). These are theorems for special fixed graphs, not a proof of the canonical implication.
- Wigderson, [*Infinitely many minimally non-Ramsey size-linear graphs*](https://arxiv.org/abs/2409.05931), European J. Combin. 128 (2025), proves a different structural existence result and restates the standard definition.
- Recent cycle results, including [Cambie–Freschi–Morawski–Petrova–Pokrovskiy (2026)](https://arxiv.org/abs/2601.10238) and [Hng–Ji–Lamaison (2026)](https://arxiv.org/abs/2603.25453), concern particular fixed graphs and do not resolve this implication.

Treat all statements above strictly according to their cited source. Verify any stronger lemma from the full paper before relying on it.

## Complete resolutions

An affirmative resolution is a proof that every fixed \(G\) satisfying both hypotheses has one constant \(C(G)\) that works for every finite isolate-free \(H\).

A negative resolution is a specific fixed graph \(G\), rigorous proofs of both hypotheses for that exact \(G\), and a sequence \(H_i\) of isolate-free finite graphs with
\[
\frac{R(G,H_i)}{e(H_i)}\longrightarrow\infty.
\]

Either resolution must be self-contained enough to audit every quantifier and implied constant, while citing external theorems precisely by theorem/proposition number and direct URL.

## What does not count as a solution

- A proof only for trees, cliques, connected targets, bipartite targets, bounded-degree targets, cycles, or another subclass of \(H\).
- A result \(O_G(e(H)\log e(H))\), \(O_G(e(H)^{1+\varepsilon})\), or any superlinear bound.
- A bound with a hidden constant depending on \(H\), \(e(H)\), \(v(H)\), \(\Delta(H)\), or an auxiliary decomposition.
- Showing only one hypothesis for a prospective counterexample \(G\).
- A computation, finite table, heuristic, or literature citation with no proof of the required uniform asymptotic claim.

## Required correctness checks

1. State the red/blue orientation and non-induced-copy convention before applying a Ramsey theorem.
2. At every \(O\), \(\ll\), or constant declaration, list its permitted dependencies. The final constant may depend only on \(G\).
3. Check the tree hypothesis uniformly over all trees and all orders, not separately tree by tree.
4. Preserve the no-isolated-vertices condition. If a reduction adds isolates, quantify its effect on the Ramsey number rather than silently discarding it.
5. For an affirmative proof, isolate and audit the exact transition from the two test families (trees and cliques) to arbitrary \(H\).
6. For a negative proof, independently audit both hypotheses for the same fixed \(G\), then prove the unbounded ratio for the stated \(H_i\).
7. Separate sourced facts, transparent deductions, conjectural ideas, and failed approaches.

## Required deliverables

Deliver a research report containing:

1. a formal statement with all quantifiers and constant dependencies;
2. a source ledger with direct URLs, publication status, theorem locations, and the exact claim used;
3. an approach registry recording each approach, its target lemma, dependencies, status, and an adversarial checker;
4. either a complete proof, a complete counterexample dossier, or a clearly delimited partial-progress report;
5. a proof-audit appendix that checks every imported theorem against the stated orientation and quantifiers; and
6. a final status sentence that does not call a partial class result a solution.

Every material literature assertion needs a direct primary URL where available. Do not cite search snippets as proof.

## Dynamic Multiagent v2 protocol

Maintain a research root responsible for the canonical target, source ledger, approach registry, conflict resolution, and final audit. Use at most four concurrent agents.

Start with independent approaches rather than fixed roles: literature/definition verification; affirmative structural reductions; counterexample candidates among known non-size-linear graphs; and adversarial scrutiny of hidden constant dependencies. Record every active approach in the registry with a precise claim being tested, inputs, output criterion, and a different agent assigned to check it.

Work in multiple waves. After the first independent wave, compare only documented lemmas and evidence. Dynamically reuse freed slots for the most promising unresolved sublemma or for adversarial checking; do not preserve a static assignment. Any claimed proof or counterexample must be checked by an agent who did not originate it. Resolve disagreements by tracing the proof or source, not by majority vote.

Use proof-first allocation. At most one optional computational subtask may run at any time, and only after declaring: the exact lemma or counterexample question; hypotheses; finite search domain; certificate format; and stopping condition. Computation may test a structural conjecture or produce a certificate, but cannot establish the required asymptotic conclusion by sampling. Reassign that slot immediately once its declared question is answered.

## Persistence and resumability

Maintain `research_state.md` throughout. It must include the canonical statement, source URLs actually inspected, theorem locations, current source ledger, approach registry, rejected leads, proof obligations, and the next smallest verifiable tasks.

Checkpoint after each wave and before a runtime boundary. If an interruption occurs before a complete resolution, put `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, state exactly which claims remain unverified, preserve all evidence and failed attempts, and do not issue a final solution claim.
