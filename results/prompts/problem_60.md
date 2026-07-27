# Erdős Problem 60: audit-ready research prompt

## Definitions and canonical target

Work with finite simple undirected graphs. Let \(C_4\) be the cycle on four vertices, and let

\[
\operatorname{ex}(n,C_4)=\max\{e(H): |V(H)|=n,\ H\text{ contains no }C_4\}.
\]

Let \(\#C_4(G)\) denote the number of distinct unlabelled ordinary subgraphs of \(G\) isomorphic to \(C_4\), and define

\[
h(n,t)=\min\{\#C_4(G): |V(G)|=n,\ e(G)=\operatorname{ex}(n,C_4)+t\},\qquad h(n)=h(n,1).
\]

Prove the literal audited target:

\[
\exists c>0\ \exists N\ \forall n\ge N:\quad h(n)\ge c\sqrt n.
\]

Equivalently, every sufficiently large \(n\)-vertex graph with more than \(\operatorname{ex}(n,C_4)\) edges has at least \(c\sqrt n\) copies of \(C_4\). It is enough to prove the exact-edge version because any graph with more edges has a spanning subgraph with exactly \(\operatorname{ex}(n,C_4)+1\) edges, and deleting edges cannot create a \(C_4\).

## Accepted background

- The stronger Erdős–Simonovits conjecture is \(h(n)\ge (1+o(1))\sqrt n\), not merely \(\Omega(\sqrt n)\). See He–Ma–Yang, [arXiv:1912.00986](https://arxiv.org/abs/1912.00986), and its [2023 peer-reviewed version](https://www.global-sci.com/csiam-am/article/view/7823).
- For \(q=2^k\) and sufficiently large \(k\), He–Ma–Yang prove the exact result
  \[
  h(q^2+q+1)=q-1,
  \]
  with an extremal graph obtained from an orthogonal polarity graph by adding an edge between two degree-\(q\) vertices. This verifies the stronger conjecture on an infinite subsequence. It does not settle all \(n\).
- Their work also proves stability and exact low-excess results at the special finite-geometric orders. Use only the theorem statements actually cited from the paper; do not extrapolate from \(q=2^k\) to arbitrary even \(q\).
- Nagy's [2019 paper](https://real.mtak.hu/83888/) studies a related balanced-bipartite Zarankiewicz supersaturation problem. It may supply methods, but it has a different host class and threshold.
- Qiao–Zhan's [2022 paper](https://www.cambridge.org/core/journals/bulletin-of-the-australian-mathematical-society/article/abs/on-a-problem-of-erdos-about-graphs-whose-size-is-the-turan-number-plus-one/E5E215F3ACD73F6164C862E5078BE13D) gives small-\(n\) examples with one \(C_4\); these do not refute the asymptotic target.
- Before relying on it, audit the unsupported secondary assertion in Ning–Zhai [arXiv:2112.15279](https://arxiv.org/abs/2112.15279) about an alleged \(q^2+q+2\) counterexample to a weaker two-copy statement. It is not a verified counterexample to the present target.

## Complete resolutions

An affirmative resolution must prove explicit \(c>0\) and \(N\) such that \(h(n)\ge c\sqrt n\) for every integer \(n\ge N\). The proof must apply to arbitrary finite simple graphs and use the true \(\operatorname{ex}(n,C_4)\) threshold.

A negative resolution must prove the exact negation: for every \(c>0\) and \(N\), there exist \(n\ge N\) and an \(n\)-vertex graph \(G\) with \(e(G)=\operatorname{ex}(n,C_4)+1\) and \(\#C_4(G)<c\sqrt n\). An explicit infinite family with \(\#C_4(G_n)=o(\sqrt{|V(G_n)|})\), plus a proof of the exact extremal edge condition, is sufficient.

## What does not count as a solution

- A proof restricted to \(n=q^2+q+1\), \(q=2^k\), bipartite graphs, triangle-free graphs, regular graphs, or a spectral-radius condition.
- Replacing \(\operatorname{ex}(n,C_4)\) by an asymptotic estimate, a Reiman upper bound, or a finite-geometric construction without controlling the direction and additive error.
- A result at \(\operatorname{ex}(n,C_4)+t\) only when \(t\) grows rapidly with \(n\).
- A finite computation without an all-\(n\) theorem, or a construction whose claimed edge count is not proved to equal \(\operatorname{ex}(n,C_4)+1\).
- Proving one \(C_4\), two \(C_4\)'s, or the result on a subsequence only.
- Treating \((1+o(1))\sqrt n\) as synonymous with \(\Omega(\sqrt n)\), or confusing labelled, induced, and ordinary copies.

## Required correctness checks

1. State all quantifiers and constants, including the dependence of every \(o(1)\), \(O(1)\), or \(\Omega(1)\) term.
2. Verify the monotonic reduction to exactly \(\operatorname{ex}(n,C_4)+1\) edges.
3. For every use of a C4 count, check the normalization: \(\#C_4(G)=\frac12\sum_{\{u,v\}}\binom{|N(u)\cap N(v)|}{2}\) for unlabelled copies.
4. Check all comparisons with \(\operatorname{ex}(n,C_4)\) in the correct direction; an asymptotic \(o(n^{3/2})\) error is unusable at an additive-one threshold.
5. If using a polarity graph, prove or cite precisely its parameter existence, vertex and edge counts, C4-freeness, degrees, and the exact C4 count after each edge modification.
6. Explicitly explain why any structural/stability theorem applies outside its original finite-geometric parameter range, if it does.
7. Maintain a claim ledger separating proved statements, cited theorems, conjectures, and computational observations.

## Required deliverables

- `research_state.md` with definitions, bibliography, theorem ledger, attempted routes, open proof obligations, and a timestamped status.
- A self-contained proof manuscript or counterexample manuscript, with every nontrivial external theorem linked to a primary paper/preprint and stated in the exact form used.
- A one-page audit table mapping each conclusion to its proof location or source.
- An adversarial verification report that checks quantifiers, C4 normalization, extremal-threshold comparisons, finite-geometry assumptions, and all asymptotics.
- If no resolution is reached: a precise conditional lemma list, failed approaches with their failure point, and the strongest rigorously established partial theorem. Do not label this a solution.

## Dynamic Multiagent v2 protocol

Use a research root that owns `research_state.md`, the theorem ledger, and the approach registry. Run at most four agents concurrently, including the root. Begin with genuinely independent proof directions rather than a fixed role assignment; candidate directions may include structural deletion/saturation, codegree inequalities, transfer from finite geometry, and counterexample obstruction.

Before an agent spends substantial effort, register its proposed claim, hypotheses, intended certificate, dependencies, and disjointness from active approaches. The root may stop, merge, or redirect work when two routes become equivalent. Reuse a freed slot immediately for the highest-value unresolved proof obligation, literature verification, or adversarial check; do not reserve idle slots.

Work in multiple waves. In each wave: consolidate valid lemmas; adversarially test each against edge-threshold and quantifier traps; update the approach registry; then launch only the next experiments that are justified by the remaining bottleneck. Every candidate proof must be independently checked by an agent that did not write it. A claimed resolution requires a final adversarial pass plus a fresh source audit for any theorem on which it depends.

Proof work has priority. At most one optional computational subtask may run at a time, and only after `research_state.md` declares: (i) the exact lemma or construction question, (ii) its hypotheses, (iii) the certificate to be produced, and (iv) a stopping condition. On answer, terminate that subtask and immediately reassign the slot to proof verification or the next proof bottleneck. Computation may guide a lemma but never substitute for an all-\(n\) argument.

## Persistence and resumability

At every wave boundary, update `research_state.md` with citations checked, exact statements extracted, active definitions, proven lemmas, counterexamples ruled in/out, and the next smallest proof obligations. Preserve negative results and failed reductions because they prevent repeated work.

If a runtime boundary interrupts the investigation before a complete affirmative proof or a verified infinite counterexample is obtained, output `CHECKPOINT_NOT_FINAL` and include the current theorem ledger, the approach registry, the last verified line of each argument, and concrete next actions. Never convert an incomplete route, a finite search, or a cited subsequence result into a claimed solution.
