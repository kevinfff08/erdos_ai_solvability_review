# Erdős Problem 75 — corrected ZFC target

## Definitions and canonical target

Work in ZFC. A graph is simple and undirected. Its chromatic number \(\chi(G)\) is the least cardinality of a proper vertex-colour set; \(\alpha(H)\) is the largest size of an independent vertex set in a finite graph \(H\).

Primary target P: construct, or rule out in ZFC, a graph \(G\) with \(|V(G)|=\chi(G)=\aleph_1\) such that
\[
\forall\epsilon>0\ \exists N_\epsilon\ \forall n\ge N_\epsilon\ \forall H\subseteq G\ (|V(H)|=n\Rightarrow\alpha(H)>n^{1-\epsilon}).
\]
It is equivalent to test every induced subgraph on an \(n\)-vertex set. The threshold may depend on \(\epsilon\), never on \(H\).

Treat the follow-up Q separately unless a source explicitly requires a common witness: does there exist a graph with \(|V(G)|=\chi(G)=\aleph_1\) and fixed \(c>0,N\) such that every finite \(H\subseteq G\) with \(|H|\ge N\) has \(\alpha(H)\ge c|H|\)? Q is strictly stronger than P.

## Accepted background

- Erdős–Hajnal–Szemerédi introduced the almost-bipartite large-chromatic setting: [EHS82](https://doi.org/10.1016/S0304-0208(08)73497-2).
- Lambie-Hanson proved in ZFC that finite subgraph chromatic numbers can grow arbitrarily slowly in an \(\aleph_1\)-chromatic graph: [arXiv:1902.08177](https://arxiv.org/abs/1902.08177), published in *Advances in Mathematics* 369 (2020), 107176. Combined with \(\alpha(H)\ge |H|/\chi(H)\), this solves the old version that omitted \(|G|=\aleph_1\), but does not settle P.
- Komjáth–Shelah obtained a relevant relative-consistency result with both size and chromatic number \(\aleph_1\): [arXiv:math/0212064](https://arxiv.org/abs/math/0212064). This is not an unconditional ZFC solution.
- Lambie-Hanson–Uhrik give recent conditional Hajnal--Máté/forcing progress: [arXiv:2312.01828](https://arxiv.org/abs/2312.01828).
- The current statement is formalized but unproved (`sorry`) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/75.lean).

Do not treat the historical missing-cardinality formulation as P. The repair is documented by the [current database page](https://www.erdosproblems.com/75) and its [revision history](https://www.erdosproblems.com/history/75).

## Complete resolutions

A positive resolution of P is a ZFC proof of one graph satisfying every displayed quantifier, including both exact cardinal equalities. A negative resolution is a ZFC proof that no such graph exists. A genuine independence result must prove the required relative consistency in both directions over clearly stated base theories.

For Q, the same standards apply with a fixed positive linear constant. A proof of Q resolves P, but a proof of P does not resolve Q.

## What does not count as a solution

- A construction with no proof that its vertex cardinality is \(\aleph_1\).
- A proof under CH, \(\Diamond\), disjoint type guessing, or in a forcing extension presented as ZFC.
- Lambie-Hanson's solution of the no-size version.
- A finite-subgraph chromatic estimate without the quantified conversion to \(\alpha(H)>n^{1-\epsilon}\).
- A result for selected subgraphs, or thresholds depending on \(H\).
- A Lean declaration whose proof is `sorry`.
- A solution of P advertised as a solution of Q.

## Required correctness checks

1. State the ambient axioms at the beginning and log every additional set-theoretic hypothesis.
2. Prove separately \(|V(G)|=\aleph_1\), \(\chi(G)\le\aleph_1\), and \(\chi(G)>\aleph_0\).
3. For every finite-subgraph lemma, verify all quantifier directions when inverting a growth function.
4. Derive \(\alpha(H)\ge |H|/\chi(H)\) from a proper colouring, then establish the target's strict inequality after choosing an explicit eventual threshold.
5. Check induced versus non-induced subgraphs correctly.
6. Subject every alleged ZFC extraction of an \(\aleph_1\)-sized subgraph to adversarial review; this is the known failure point.
7. If pursuing Q by shift graphs, identify exactly where CH enters and prove that no hidden cardinal-arithmetic assumption remains.

## Required deliverables

- A self-contained theorem statement, axiom ledger, and proof or disproof.
- A source ledger with direct URLs, theorem numbers/pages where available, and publication status.
- A dependency graph separating proved lemmas, conditional lemmas, conjectures, and failed routes.
- A quantifier audit mapping every target quantifier to a proof step.
- For any positive construction, a cardinality/chromaticity certificate and a finite-subgraph independence certificate.
- For an incomplete investigation, a precise frontier statement naming the smallest unproved lemma.

## Dynamic Multiagent v2 protocol

Create a research root and maintain an approach registry containing: approach ID, exact target (P or Q), axiom context, claimed lemma, dependencies, evidence links, status, and an assigned adversarial checker.

Use at most four concurrent agents. In the first wave, require independent approaches rather than a fixed division of labour: one may reconstruct the ZFC slow-growth construction, another may audit cardinal-reduction principles, another may analyse forcing/consistency boundaries, and another may audit shift-graph benchmarks. Do not lock these assignments; merge or replace them based on registry evidence.

At each merge point, reserve an adversarial proof check for every promising route. Checkers must attempt to falsify cardinal arithmetic, quantifier order, and inherited-subgraph claims before effort is expanded. Reuse a freed slot immediately for the most informative unresolved dependency, and run multiple waves until the remaining bottleneck is explicit.

Adopt proof-first allocation. At most one computational subtask may run at a time, and only after declaring its exact lemma, hypotheses, finite search space/certificate format, and stopping condition. Computation may test a finite shift-graph lemma or counterexample pattern; it cannot establish an uncountable ZFC existence theorem. Reassign that slot as soon as the declared question is answered.

## Persistence and resumability

Maintain `research_state.md` after each substantive wave with: target P/Q, current axiom context, approach registry, checked sources, proved lemmas, rejected claims and reasons, pending proof obligations, and the next highest-value check.

If interrupted before a complete resolution, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, preserve all citation URLs and exact counterexample/proof gaps, and resume from the first unverified dependency. Never convert a conditional result or an unreviewed model output into a final answer on resume.
