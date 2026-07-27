# Erdős Problem 111: edge-bipartization in uncountably chromatic graphs

## Definitions and canonical target

All graphs are simple and undirected.  For a finite graph \(F\), define its edge-bipartization number
\[
\beta(F)=\min\{|D|:D\subseteq E(F),\ F-D\text{ is bipartite}\}.
\]
For an infinite graph \(G\) and \(n\in\mathbb N\), define
\[
h_G(n)=\max_{A\in[V(G)]^n}\beta(G[A]).
\]
This equals the least integer \(t\) for which every \(n\)-vertex subgraph of \(G\) can be made bipartite by deleting at most \(t\) edges: among subgraphs on a fixed vertex set, the induced one is the worst case.

The canonical target is the following ZFC question:
\[
\forall G\,[\chi(G)=\aleph_1\Rightarrow \lim_{n\to\infty}h_G(n)/n=+\infty].
\]
Equivalently, for every such \(G\) and every \(M>0\), prove that \(h_G(n)>Mn\) for all sufficiently large \(n\).

The broad historical request to “describe the behaviour” of \(h_G\) is not itself a unique target. Keep separate the related Erdős construction conjecture: for every \(\varepsilon>0\), does there exist a graph \(G\) with \(\chi(G)=\aleph_1\) and \(h_G(n)=O_{G,\varepsilon}(n^{1+\varepsilon})\)? Do not claim that resolving one automatically resolves the other.

## Accepted background

- Erdős, Hajnal, and Szemerédi define the equivalent function \(f_W^3(n)\), prove a linear lower bound for each uncountably chromatic graph, and construct graphs with \(f_W^3(n)<2n^{3/2}\). Their methods use ordered-edge/shift graphs. Source: [Erdős–Hajnal–Szemerédi (1982)](https://www.renyi.hu/~p_erdos/1982-11.pdf).
- The linear lower bound comes from uncountably many vertex-disjoint odd cycles of one fixed odd length. It gives \(h_G(n)\ge c_Gn\) in the relevant asymptotic sense, not \(h_G(n)/n\to\infty\).
- Erdős recorded the hoped-for \(n^{1+\varepsilon}\) improvement in [Combinatorica 1 (1981), 25–42](https://doi.org/10.1007/BF02579174).
- Lambie-Hanson proved that finite-subgraph chromatic numbers can grow arbitrarily slowly in a graph of chromatic number \(\aleph_1\): [arXiv:1902.08177](https://arxiv.org/abs/1902.08177), published in *Advances in Mathematics* 369 (2020). This controls a different function. In particular, a small chromatic number of a finite graph does not imply small \(\beta\); disjoint unions of triangles are a basic warning.
- Related later work on Hajnal–Máté graphs and chromatic-growth constructions is [Lambie-Hanson–Uhrik (2024)](https://doi.org/10.1112/mtk.12261). It is background, not a known solution of the edge-deletion problem.

Before making a new claim, re-check current status and inspect every source relied upon. Distinguish a theorem, a conjecture, and a deduction made in this investigation.

## Complete resolutions

An affirmative resolution is a ZFC proof that for every graph \(G\) with \(\chi(G)=\aleph_1\), every \(M>0\) has an \(N\) such that \(h_G(n)>Mn\) for every \(n\ge N\).

A negative resolution is a construction, in an explicitly stated foundational setting, of a graph \(G\) with \(\chi(G)=\aleph_1\), a constant \(C<\infty\), and arbitrarily large \(n\) for which \(h_G(n)\le Cn\). This is exactly the negation of the asserted limit.

For the separate construction conjecture, a positive resolution must state the quantifiers precisely and prove the \(O(n^{1+\varepsilon})\) bound for every \(n\), not merely a subsequence.

## What does not count as a solution

- Reproving \(h_G(n)\ge c_Gn\), which is known and does not imply divergence of the ratio.
- Establishing an upper bound for a graph whose chromatic number is only countable, or merely producing finite graphs of unbounded chromatic number.
- Replacing edge deletion by vertex deletion, average deletion cost, or a statement about one selected finite subgraph.
- Controlling only finite-subgraph chromatic number without a proved implication for \(\beta\).
- A finite computation, a heuristic random construction, or checks for finitely many \(n\) without a theorem that discharges the asymptotic and uncountable-chromatic quantifiers.
- A conditional result presented as a ZFC result. State every use of \(\diamondsuit\), CH, forcing, or other set-theoretic assumption.

## Required correctness checks

1. Verify that the claimed \(h_G(n)\) bound is uniform over every \(A\in[V(G)]^n\).
2. Verify that the retained graph after deleting the named edge set is actually bipartite, preferably by providing an explicit bipartition or a general lemma.
3. Verify \(\chi(G)=\aleph_1\), including both \(\chi(G)>\aleph_0\) and \(\chi(G)\le\aleph_1\). Do not silently substitute a larger uncountable chromatic number.
4. Audit every asymptotic quantifier: constants may depend only on stated parameters and never on \(n\) or on the chosen \(n\)-vertex subgraph.
5. For a positive universal proof, check the all-sufficiently-large-\(n\) conclusion. For a counterexample, check that the bounded-ratio values of \(n\) are unbounded.
6. Check that any invocation of the EHS construction uses its exact cardinal and induced-subgraph conventions; document any passage to a subgraph of chromatic number exactly \(\aleph_1\).
7. Subject any proposed proof to adversarial review that attempts to construct the worst-case induced \(n\)-vertex subgraph and to separate edge- from vertex-deletion assertions.

## Required deliverables

- A status memo with direct URLs, bibliographic metadata, publication status, and a line-by-line account of which cited claims are used.
- A self-contained theorem statement using \(\beta\) and \(h_G\), with all set-theoretic assumptions visible.
- Either a complete proof of one resolution above, or a clearly labelled partial result with exact scope and no open-problem resolution claim.
- A lemma dependency graph or numbered proof outline, followed by complete proofs of all nonstandard lemmas.
- An adversarial proof-audit report listing attempted counterexamples, quantifier checks, and any unresolved gap.
- If computation is used, source code or an exact reproducible certificate, the proved lemma it addresses, all hypotheses, and a stopping condition. Cite original sources rather than database summaries whenever possible.

## Dynamic Multiagent v2 protocol

Maintain one research root and use at most four concurrent agents total. Start with multiple genuinely independent approaches, selected dynamically from the current obstacle rather than by a fixed mathematical-method assignment. Examples of eligible early directions are a universal compactness/lower-bound route, a counterexample-construction route, a translation to odd-cycle transversals/max-cut, and a literature/status verification route.

Maintain an approach registry containing: approach identifier; precise target lemma; assumptions; dependencies; evidence or proof state; falsifying tests; and the reason for continuation, merge, or retirement. Do not allow two agents to work on indistinguishable reformulations without recording the difference.

Use multiple waves. In each wave, the research root compares proof obligations and evidence, asks at least one agent to adversarially audit each serious claimed lemma, and then reuses freed slots for the most discriminating unresolved question. A slot is immediately reassigned when its question is answered, falsified, or reduced to a documented dependency. Do not treat majority agreement as proof.

Allocate proof work before computation. At most one optional computational subtask may run concurrently, and only after the registry states its exact finite lemma, hypotheses, expected certificate, and stopping condition. The computation must be stopped and its slot reassigned immediately once that question is answered; it may not become a broad search for patterns.

## Persistence and resumability

Keep `research_state.md` current after every material result. It must record the canonical target, sources checked, approach registry, proved lemmas with assumptions, failed approaches, active proof obligations, audit findings, and exact commands/certificates for any computation.

At any runtime boundary, preserve the state and return `CHECKPOINT_NOT_FINAL` unless a complete resolution and adversarial audit have both been completed. A later session must begin by reading `research_state.md`, verifying cited sources and assumptions, and continuing from the recorded proof obligations rather than restarting or presenting an incomplete argument as final.
