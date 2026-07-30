# Erdős Problem 111: edge-bipartization in uncountably chromatic graphs

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

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

## Frozen mathematical background

- Erdős, Hajnal, and Szemerédi define the equivalent function \(f_W^3(n)\), prove a linear lower bound for each uncountably chromatic graph, and construct graphs with \(f_W^3(n)<2n^{3/2}\). Their methods use ordered-edge/shift graphs. Source: [Erdős–Hajnal–Szemerédi (1982)](https://www.renyi.hu/~p_erdos/1982-11.pdf).
- The linear lower bound comes from uncountably many vertex-disjoint odd cycles of one fixed odd length. It gives \(h_G(n)\ge c_Gn\) in the relevant asymptotic sense, not \(h_G(n)/n\to\infty\).
- Erdős recorded the hoped-for \(n^{1+\varepsilon}\) improvement in [Combinatorica 1 (1981), 25–42](https://doi.org/10.1007/BF02579174).
- Lambie-Hanson proved that finite-subgraph chromatic numbers can grow arbitrarily slowly in a graph of chromatic number \(\aleph_1\): [arXiv:1902.08177](https://arxiv.org/abs/1902.08177), published in *Advances in Mathematics* 369 (2020). This controls a different function. In particular, a small chromatic number of a finite graph does not imply small \(\beta\); disjoint unions of triangles are a basic warning.
- Related later work on Hajnal–Máté graphs and chromatic-growth constructions is [Lambie-Hanson–Uhrik (2024)](https://doi.org/10.1112/mtk.12261). It is background, not a known solution of the edge-deletion problem.

Distinguish proved theorems, conjectures, and deductions. Import an external theorem only through the exact hypotheses required by an active proof step.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete affirmative resolution proves in ZFC that for every simple graph G with χ(G)=aleph_1 and every real M>0, there is N=N(G,M) such that h_G(n)>Mn for all n≥N.

**Negative obligation.** A complete negative resolution gives, in a stated foundational setting, a specific graph G with χ(G)=aleph_1, a constant C<∞, and arbitrarily large integers n such that h_G(n)≤Cn. This is exactly the negation of h_G(n)/n→∞.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

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

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Verify that the claimed \(h_G(n)\) bound is uniform over every \(A\in[V(G)]^n\).
2. Verify that the retained graph after deleting the named edge set is actually bipartite, preferably by providing an explicit bipartition or a general lemma.
3. Verify \(\chi(G)=\aleph_1\), including both \(\chi(G)>\aleph_0\) and \(\chi(G)\le\aleph_1\). Do not silently substitute a larger uncountable chromatic number.
4. Audit every asymptotic quantifier: constants may depend only on stated parameters and never on \(n\) or on the chosen \(n\)-vertex subgraph.
5. For a positive universal proof, check the all-sufficiently-large-\(n\) conclusion. For a counterexample, check that the bounded-ratio values of \(n\) are unbounded.
6. Check that any invocation of the EHS construction uses its exact cardinal and induced-subgraph conventions; document any passage to a subgraph of chromatic number exactly \(\aleph_1\).
7. Subject any proposed proof to adversarial review that attempts to construct the worst-case induced \(n\)-vertex subgraph and to separate edge- from vertex-deletion assertions.

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
