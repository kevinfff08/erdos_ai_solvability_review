# Erdős Problem 61 — Erdős–Hajnal conjecture

## Definitions and canonical target

All graphs in this task are finite and simple. Fix a finite simple graph \(H\). A graph \(G\) is **induced-\(H\)-free** if there is no \(S\subseteq V(G)\) for which \(G[S]\cong H\). Let \(\omega(G)\) be the largest clique size and \(\alpha(G)\) the largest independent (stable) set size.

Resolve the following statement:

\[
\forall\text{ finite simple }H\;\exists c(H)>0\;\forall\text{ finite induced-}H\text{-free }G,
\qquad \max\{\omega(G),\alpha(G)\}\ge |V(G)|^{c(H)}.
\]

The order of quantifiers is mandatory: \(H\) is fixed first; \(c(H)\) may depend on \(H\) only; then the result must hold for every \(G\) and every order. The statement is invariant under replacing both \(G\) and \(H\) by their complements.

## Accepted background

- **Theorem.** Erdős and Hajnal proved the general lower bound \(\exp(c_H\sqrt{\log n})\): [Ramsey-type theorems (1989)](https://doi.org/10.1016/0166-218X(89)90045-0).
- **Theorem.** Bucić, Nguyen, Scott, and Seymour improved the general bound to \(\exp(c_H\sqrt{\log n\log\log n})\): [IMRN 2024](https://doi.org/10.1093/imrn/rnae065). This remains \(n^{o(1)}\), not a proof of the target.
- **Theorem.** The property is closed under vertex substitution: [Alon–Pach–Solymosi (2001)](https://doi.org/10.1007/s004930100016).
- **Theorems for special \(H\).** The bull: [Chudnovsky–Safra (2008)](https://doi.org/10.1016/j.jctb.2008.02.005); \(C_5\): [Chudnovsky–Scott–Seymour–Spirkl (2023)](https://doi.org/10.1112/plms.12504); \(P_5\): [Nguyen–Scott–Seymour (2026)](https://doi.org/10.1112/plms.70133). The last source explains why all five-vertex graphs are thereby covered.
- **Theorems for broader but still restricted classes.** Infinitely many prime graphs and buildable configurations: [Nguyen–Scott–Seymour, accepted 2026](https://ora.ox.ac.uk/objects/uuid%3Adb84da08-f522-45c5-8691-eb4108f14017). Bounded VC-dimension graphs: [Nguyen–Scott–Seymour (2025)](https://arxiv.org/abs/2312.15572). Neither theorem covers arbitrary \(H\).
- **Recent preprint.** The six-vertex E-graph is settled in [Huang–Ju–Zhou (2026)](https://arxiv.org/abs/2606.06258); it is a special case, not a resolution of the conjecture.

Before using any cited result, inspect its exact theorem and state which hypotheses are invoked. Do not upgrade an abstract, a forum comment, a preprint, or a conjectural strengthening into a theorem.

## Complete resolutions

An affirmative resolution is a self-contained proof of the displayed statement, including a derivation of a strictly positive exponent for every fixed finite \(H\).

A negative resolution is a proof that one fixed finite simple graph \(H\) violates it: for every \(c>0\), construct an induced-\(H\)-free finite graph \(G\) with \(\max\{\omega(G),\alpha(G)\}<|V(G)|^c\). A sufficient form is an unbounded family with homogeneous number \(n^{o(1)}\).

## What does not count as a solution

- Handling only finitely many new \(H\), or infinitely many \(H\) without a theorem covering all finite graphs.
- A bound still of form \(n^{o(1)}\), including \(\exp((\log n)^a)\) for \(a<1\).
- A result assuming bounded VC-dimension, geometric representability, a structural restriction, or any hypothesis not implied by induced-\(H\)-freeness.
- Forbidding \(H\) merely as a non-induced subgraph.
- Finite computation without an all-order theorem or a rigorously verified infinite construction.
- Selecting \(c\) after observing \(G\) or \(|V(G)|\).

## Required correctness checks

1. Check the complete quantifier order and prove that the final exponent depends only on \(H\).
2. For every induced-copy assertion, check every required edge and nonedge.
3. Maintain an explicit exponent/asymptotic ledger; reject any argument that proves only a subpolynomial bound.
4. Check each complement transformation, including the replacement \(H\mapsto\overline H\) and clique/stable-set exchange.
5. For substitution, modular decomposition, or recursive sparsification, prove preservation of the relevant induced-forbidden condition and that accumulated exponent losses remain positive.
6. For a negative construction, prove fixed \(H\), unbounded orders, induced-\(H\)-freeness, and a bound defeating every positive constant exponent.
7. Require adversarial line-by-line proof checking by an agent that did not originate the candidate argument.

## Required deliverables

- `research_state.md` with canonical target, sources checked, exact theorem statements, approach registry, proved lemmas, failed routes, and next falsifiable obligations.
- A proof manuscript or counterexample manuscript, self-contained apart from a dependency ledger.
- A dependency ledger giving each cited theorem, its stable link, its exact hypothesis, and its use in the argument.
- An adversarial verification report covering inducedness, quantifiers, exponent accounting, and all limiting arguments.
- If incomplete, a frontier report containing the strongest proved lemma, its proof, the first unproved implication, and why that implication would advance the target.

## Dynamic Multiagent v2 protocol

Use a research root responsible for `research_state.md`, with at most four concurrent agents total. Begin with independent exploration of incompatible affirmative and negative routes; do not commit prematurely to one named technique.

Maintain an approach registry with fields: identifier, exact proposition tested, dependencies, status, evidence, owner, and required adversarial check. Consult it before starting work to prevent duplicated investigations. Use multiple waves: later work must be selected from evidence and bottlenecks generated by earlier work rather than fixed in advance.

Dynamically reuse a slot whenever an approach proves a lemma, finds a counterexample to its lemma, or reaches a documented obstruction. Every nontrivial proof claim must be checked independently by a different agent; a failed check restores the claim to `unproved` status.

Allocate proof-first. At most one optional computational subtask may be active at any time. Before it begins, record the precise lemma or construction hypothesis, its finite parameter range, generation and isomorphism-elimination method, saved certificate format, and a stopping condition. Reassign that slot immediately once its stated question is answered. Computation may produce a finite counterexample to a proposed lemma or a certificate, but never substitutes for the universal proof/disproof.

## Persistence and resumability

Checkpoint `research_state.md` after each material literature check, registry update, proved/falsified lemma, and proof-review result. Preserve scripts, explicit graph certificates, proof notes, source versions, and reproducible commands.

If a runtime boundary occurs before a complete proof/disproof and independent adversarial verification, write the exact rigorous frontier to `research_state.md` and return `CHECKPOINT_NOT_FINAL`. Never represent a promising route, a finite experiment, or an unchecked draft as a resolution.
