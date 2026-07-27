# Erdős Problem 573: triangle- and four-cycle-free extremal number

## Definitions and canonical target

Work with finite simple undirected graphs.  Let \(C_k\) denote the cycle with \(k\) vertices.  For a finite family \(\mathcal F\) of graphs,
\[
\operatorname{ex}(n,\mathcal F)=\max\{e(G): |V(G)|=n,\ G\text{ contains no member of }\mathcal F\text{ as a subgraph}\}.
\]
Subgraph containment is not induced containment.  The canonical target is
\[
\operatorname{ex}(n,\{C_3,C_4\})\sim (n/2)^{3/2}
\quad(n\to\infty\text{ through positive integers}),
\]
equivalently \(\operatorname{ex}(n,\{C_3,C_4\})=(n/2)^{3/2}+o(n^{3/2})\).  The leading constant is \(1/(2\sqrt2)\), not \(1/2\).

## Accepted background

- Define \(z(n,C_4)\) as the maximum number of edges in an \(n\)-vertex bipartite \(C_4\)-free graph.  Since bipartite graphs are triangle-free, \(z(n,C_4)\le \operatorname{ex}(n,\{C_3,C_4\})\).  The standard asymptotic is \(z(n,C_4)=(n/2)^{3/2}+o(n^{3/2})\).  Ma and Yang record explicit bounds \((n/2)^{3/2}-cn^{4/3}\le z(n,C_4)\le (n/2)^{3/2}+n/4\).  Source: [Ma--Yang 2025](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-extremal-numbers-of-the-triangle-plus-the-fourcycle/ED3AF154970DCE68C1EF742401F0A919).
- The best generic upper bound recorded there is only \(\operatorname{ex}(n,\{C_3,C_4\})\le\operatorname{ex}(n,C_4)=\tfrac12n^{3/2}+O(n)\), from the classical \(C_4\)-free theory.  Thus the desired improvement is in the leading constant.
- Ma and Yang, in the peer-reviewed 2025 paper above, prove \(\operatorname{ex}(n,\{C_3,C_4\})\ge z(n,C_4)+c n^{5/4}\) for every \(n\ge7\), for an absolute \(c>0\), and obtain \((n/2)^{3/2}+\Omega(n^{5/4})\) on an infinite prime-power sequence.  This is a theorem, but it is compatible with the target because \(n^{5/4}=o(n^{3/2})\).
- The stronger Chung--Graham question \(\operatorname{ex}(n,\{C_3,C_4\})=(n/2)^{3/2}+O(n)\) is false by that result.  It is not the target here.
- For every \(k\ge2\), the different problem forbidding \(C_4\) and \(C_{2k+1}\) has \((n/2)^{3/2}+O(n)\) behavior; see [Keevash--Sudakov--Verstraëte 2013](https://doi.org/10.1007/s00493-013-2863-8).  Do not transfer a proof across the missing \(C_3\) condition without a new argument.
- A 2025 preprint improves finite-order lower bounds for \(74\le n\le198\) using hill climbing; it supplies test data, not an asymptotic theorem: [Goedgebeur--Jooken--Joret--Van den Eede](https://arxiv.org/abs/2508.05562).

## Complete resolutions

An affirmative resolution is a rigorous proof that for every \(\varepsilon>0\) there is \(N\) such that, for every integer \(n\ge N\),
\[
\operatorname{ex}(n,\{C_3,C_4\})\le(1+\varepsilon)(n/2)^{3/2}.
\]
The accepted bipartite lower bound then proves the asymptotic formula.

A negative resolution is a rigorous proof that the ratio fails to tend to one; for example, constants \(\varepsilon>0\) and infinitely many \(n\) with a \(\{C_3,C_4\}\)-free graph having at least \((1+\varepsilon)(n/2)^{3/2}\) edges.  An equivalent rigorous limsup/liminf separation also suffices.

## What does not count as a solution

- A finite computation, a heuristic, or a construction at finitely many orders.
- The extant \(\tfrac12n^{3/2}+O(n)\) upper bound, or any bound that retains a fixed factor larger than \(1/(2\sqrt2)\).
- An additive gain of \(o(n^{3/2})\), including \(\Omega(n^{5/4})\), as a purported disproof.
- Proving or disproving the separate \(O(n)\)-error strengthening only.
- A result only for bipartite graphs, only for prime powers, or only along a subsequence, unless it is explicitly used in a valid all-\(n\) argument.
- A proof for \(\{C_4,C_5\}\) or \(\{C_4,C_{2k+1}\}\) that does not address triangles.

## Required correctness checks

1. State all quantifiers over \(n\), \(\varepsilon\), and any infinite subsequence explicitly.
2. Preserve the constant \((n/2)^{3/2}=n^{3/2}/(2\sqrt2)\) at every normalization step.
3. Check that every claimed construction contains neither a triangle nor a 4-cycle as a non-induced subgraph, including cycles crossing modified and unmodified regions.
4. If using two-path counts, justify multiplicity bounds from \(C_4\)-freeness and separately use triangle-freeness where required.
5. For any stability or near-bipartiteness assertion, prove the exact error needed to be \(o(n^{3/2})\); do not assume it from the bipartite extremal problem.
6. For projective-plane or prime-power inputs, state existence hypotheses and distinguish all \(n\), almost all \(n\), and a subsequence.
7. Audit every imported theorem against its exact forbidden family, graph model, and asymptotic regime.

## Required deliverables

- A self-contained theorem statement identifying affirmative or negative resolution.
- A dependency map listing every external theorem with a stable URL, precise statement, and where it is used.
- A line-by-line proof, including an explicit leading-constant calculation and all asymptotic quantifiers.
- For a construction, an edge/vertex count and a standalone \(C_3\)- and \(C_4\)-freeness proof.
- For an upper bound, a named central lemma whose conclusion already implies the required \(o(n^{3/2})\) error, followed by a complete proof of that lemma.
- A short comparison with Ma--Yang explaining why the result is not merely their \(\Omega(n^{5/4})\) lower-bound phenomenon.
- A final adversarial audit listing failed approaches, unresolved gaps, and why none is being presented as a solution.

## Dynamic Multiagent v2 protocol

Create one research root and maintain at most four concurrent agents total, including the root.  Use multiple waves and dynamic slot reuse rather than a fixed assignment plan.

At the start of each wave, register each proposed approach in an approach registry containing: approach ID, exact target lemma, hypotheses, expected leading-constant consequence, dependencies, potential failure mode, and owner.  The first wave must explore genuinely independent directions before convergence, such as direct upper-bound counting, structural/stability analysis, and a construction-based attempt to disprove the target.  Do not require any particular method and do not duplicate an approach merely by changing notation.

After each substantive lemma or candidate proof, assign an adversarial checker independent of its origin.  The checker must attempt counterexamples, test all quantifiers and constants, verify forbidden-subgraph preservation, and classify the result as proved, refuted, or gap-located.  A proof cannot be promoted to a resolution until a separate checker has audited its key lemma and final asymptotic passage.

When an approach is refuted or reaches a defined dead end, record the reason in the registry and immediately reuse its slot for the most informative untested direction.  Periodically merge only validated facts into the root state; preserve incompatible approaches until their incompatibility is resolved.  Run further waves based on evidence, not a precommitted static agent schedule.

Use proof-first allocation.  At most one optional computational subtask may run at a time.  Before it begins, the registry must state the exact lemma or counterexample question it tests, finite hypotheses/range, certificate format, and stopping condition.  It may not be used as evidence for an asymptotic conclusion by itself.  Immediately release and reassign that slot once the stated question is answered.

## Persistence and resumability

Maintain `research_state.md` at the research root after every wave.  It must contain the canonical target, verified background with URLs, approach registry, proved lemmas, checker reports, exact open gaps, and next admissible actions.  Save proof fragments with dependencies and status labels; never merge conjectural claims into the verified ledger.

If a runtime boundary interrupts an incomplete investigation, write the current state and end with `CHECKPOINT_NOT_FINAL`.  That marker means no mathematical resolution has been established.  On resumption, read `research_state.md`, revalidate the active gaps, and continue from the registry rather than restarting or treating an unreviewed draft as a theorem.
