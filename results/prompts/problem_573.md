# Erdős Problem 573: triangle- and four-cycle-free extremal number

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

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

## Frozen mathematical background

- Define \(z(n,C_4)\) as the maximum number of edges in an \(n\)-vertex bipartite \(C_4\)-free graph.  Since bipartite graphs are triangle-free, \(z(n,C_4)\le \operatorname{ex}(n,\{C_3,C_4\})\).  The standard asymptotic is \(z(n,C_4)=(n/2)^{3/2}+o(n^{3/2})\).  Ma and Yang record explicit bounds \((n/2)^{3/2}-cn^{4/3}\le z(n,C_4)\le (n/2)^{3/2}+n/4\).  Source: [Ma--Yang 2025](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-extremal-numbers-of-the-triangle-plus-the-fourcycle/ED3AF154970DCE68C1EF742401F0A919).
- The best generic upper bound recorded there is only \(\operatorname{ex}(n,\{C_3,C_4\})\le\operatorname{ex}(n,C_4)=\tfrac12n^{3/2}+O(n)\), from the classical \(C_4\)-free theory.  Thus the desired improvement is in the leading constant.
- Ma and Yang, in the peer-reviewed 2025 paper above, prove \(\operatorname{ex}(n,\{C_3,C_4\})\ge z(n,C_4)+c n^{5/4}\) for every \(n\ge7\), for an absolute \(c>0\), and obtain \((n/2)^{3/2}+\Omega(n^{5/4})\) on an infinite prime-power sequence.  This is a theorem, but it is compatible with the target because \(n^{5/4}=o(n^{3/2})\).
- The stronger Chung--Graham question \(\operatorname{ex}(n,\{C_3,C_4\})=(n/2)^{3/2}+O(n)\) is false by that result.  It is not the target here.
- For every \(k\ge2\), the different problem forbidding \(C_4\) and \(C_{2k+1}\) has \((n/2)^{3/2}+O(n)\) behavior; see [Keevash--Sudakov--Verstraëte 2013](https://doi.org/10.1007/s00493-013-2863-8).  Do not transfer a proof across the missing \(C_3\) condition without a new argument.
- A 2025 preprint improves finite-order lower bounds for \(74\le n\le198\) using hill climbing; it supplies test data, not an asymptotic theorem: [Goedgebeur--Jooken--Joret--Van den Eede](https://arxiv.org/abs/2508.05562).

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Give a complete proof that for every epsilon>0 there exists N such that every integer n>=N satisfies ex(n,{C_3,C_4}) <= (1+epsilon)(n/2)^(3/2). Together with the established bipartite lower bound z(n,C_4)=(1-o(1))(n/2)^(3/2), this proves the required asymptotic equivalence.

**Negative obligation.** Give a complete proof that the ratio does not tend to 1; for example, exhibit epsilon>0 and infinitely many integers n for which there exists an n-vertex {C_3,C_4}-free graph with at least (1+epsilon)(n/2)^(3/2) edges. A rigorous incompatible liminf/limsup statement would also resolve the question negatively.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

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

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State all quantifiers over \(n\), \(\varepsilon\), and any infinite subsequence explicitly.
2. Preserve the constant \((n/2)^{3/2}=n^{3/2}/(2\sqrt2)\) at every normalization step.
3. Check that every claimed construction contains neither a triangle nor a 4-cycle as a non-induced subgraph, including cycles crossing modified and unmodified regions.
4. If using two-path counts, justify multiplicity bounds from \(C_4\)-freeness and separately use triangle-freeness where required.
5. For any stability or near-bipartiteness assertion, prove the exact error needed to be \(o(n^{3/2})\); do not assume it from the bipartite extremal problem.
6. For projective-plane or prime-power inputs, state existence hypotheses and distinguish all \(n\), almost all \(n\), and a subsequence.
7. Audit every imported theorem against its exact forbidden family, graph model, and asymptotic regime.

If the proof uses an external theorem not fully stated in the frozen background, record its exact hypotheses and verify that they apply. Do not expand this local dependency check into a general literature or open-status investigation.

## Required research package

Create a coherent, self-contained research package. Choose the directory layout that best fits the mathematics, but preserve enough structure that another researcher can trace every final claim to its proof, computation, source, and adversarial check.

### Mandatory paper: `paper.tex`

Produce a journal-style mathematical paper containing:

- a title and abstract;
- the canonical problem and all definitions needed to read the paper independently;
- the frozen background actually used;
- a precise statement of every claimed contribution;
- complete proofs of all lemmas and the main theorem or counterexample;
- a clear comparison between the frozen background and what was newly established;
- an accurate final statement of whether the canonical target has been proved or disproved;
- complete citations for every external result used.

All references must be part of the archived package. They may be embedded in `paper.tex` or stored in an included `references.bib`; no citation may depend on a missing external bibliography file. The paper must not contain placeholders, omitted proof steps, or claims supported only by notes elsewhere in the package.

### Mandatory final audit: `audit.md`

Produce an independent adversarial audit of the final `paper.tex`. It must check:

- exact agreement between the paper's main claim and the canonical target;
- every quantifier, parameter dependence, boundary case, equality case, and uniformity requirement;
- the full dependency chain of every nontrivial lemma;
- possible circular reasoning, hidden assumptions, and illicit weakening of the target;
- exact applicability of every external theorem used;
- whether computational evidence proves only the finite statement claimed for it;
- whether citations support the statements attributed to them;
- whether every asserted new result is actually beyond the frozen background;
- whether the final solution claim is justified.

The audit must end with exactly one verdict:

- `COMPLETE_SOLUTION_VERIFIED`;
- `COMPLETE_DISPROOF_VERIFIED`; or
- `CHECKPOINT_NOT_FINAL`.

Only the first two verdicts count as completion.

### Intermediate research archive

Reasonably archive all intermediate material that matters to verification or resumption, such as proof drafts, proved and refuted lemmas, dependency notes, adversarial reviews, failed routes with exact failure points, computation code, exact certificates, test outputs, and the current research state. Filenames and subdirectories are flexible; organization, traceability, and resumability are mandatory. Do not allow the final paper to depend on an unarchived calculation or argument.

### LaTeX and PDF check

Compile `paper.tex` successfully and retain the resulting `paper.pdf`. All citations and cross-references must resolve, and there must be no fatal LaTeX errors. Successful compilation and an openable PDF are sufficient: do not perform page-by-page screenshot inspection, do not create visual-validation images, and do not add images, figures, diagrams, or a graphical abstract to the paper.

## Dynamic Multiagent constraints

Choose mathematical approaches, delegation, coordination, and changes of direction autonomously. Do not impose fixed roles, named stages, prescribed proof methods, or a predetermined sequence of work. Including the root agent, use at most four concurrent agents.

The following are prohibited:

- assigning any agent to investigate whether the problem is open;
- assigning a general literature survey or publication-status review;
- maintaining a long-running source-collection role disconnected from an active proof obligation;
- substituting a research plan, list of approaches, or organizational work for mathematical derivation;
- duplicating the same route across agents without a concrete adversarial or comparative purpose;
- recording a conjecture or proof sketch as a proved lemma;
- starting computation without a precise mathematical claim, hypotheses, finite scope, certificate format, and stopping condition;
- using finite computation or numerical evidence as a substitute for a universal proof;
- declaring a complete solution without independent adversarial checking of the actual proof;
- voluntarily stopping because the problem is difficult, initial routes failed, or only intermediate results have been obtained;
- allowing source management, status tracking, or process documentation to consume the main research effort.

Inspect an external source only when an active proof step requires the exact statement of a named theorem. Record the theorem and its hypotheses, check that they apply, and return to the mathematics.

## Persistence and external-interruption behavior

Continue mathematical research while execution resources remain available. Do not end the task merely because several approaches fail, a complete proof has not yet emerged, intermediate lemmas have been found, a paper draft exists, or the remaining gap has been identified. Autonomously repair, replace, combine, or abandon approaches as the mathematics requires.

Use `CHECKPOINT_NOT_FINAL` only when an external runtime, context, or system boundary forces interruption. It is not a voluntary completion option. On forced interruption, preserve the current `paper.tex`, `audit.md`, all verified results, unresolved proof obligations, failed routes with exact failure points, computations and certificates, and a clear resumable research state. Never convert an interrupted investigation into a solution claim.
