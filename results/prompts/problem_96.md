# Erdős Problem 96: unit distances in convex polygons

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(P=\{p_1,\ldots,p_n\}\subset\mathbb R^2\) be the vertex set of a strictly convex Euclidean \(n\)-gon: all points are distinct vertices of their convex hull and no three are collinear. Define
\[
u(P)=\bigl|\{\{p,q\}\subset P:\|p-q\|_2=1\}\bigr|,
\qquad f(n)=\max_{|P|=n}u(P).
\]
The canonical target is to prove or disprove \(f(n)=O(n)\): determine whether there exist absolute constants \(C,n_0\) such that \(u(P)\le Cn\) for every \(n\ge n_0\) and every such \(P\).

## Frozen mathematical background

- Füredi proved an \(O(n\log n)\) upper bound; Brass--Pach gave a short proof. Bibliographic primary links: https://doi.org/10.1016/0097-3165(90)90074-7 and https://doi.org/10.1006/jcta.2000.3133.
- Aggarwal proved the verified explicit upper bound \(f(n)\le n\log_2 n+4n\): *On unit distances in a convex polygon*, Discrete Mathematics 338 (2015), 88--92, https://www.sciencedirect.com/science/article/pii/S0012365X14003847 ; preprint https://arxiv.org/abs/1009.2216. Its distance-matrix approach uses the diagonal and obtuse-angle properties of convex quadrilaterals.
- Edelsbrunner--Hajnal proved that for every \(n\ge4\), some convex \(n\)-gon has at least \(2n-7\) unit-distance pairs: https://www.sciencedirect.com/science/article/pii/009731659190042F . This is a lower bound and disproves an earlier stronger \(5n/3+O(1)\) upper conjecture; it does not disprove linearity.
- In the centrally symmetric subcase, Ábrego--Fernández-Merchant proved a linear bound (in particular \(f_{sym}(n)\le2n-3\)): https://www.csun.edu/~ba70714/publications/unit.pdf . This is not a proof for arbitrary convex polygons.
- Khopkar's [2017 preprint](https://arxiv.org/pdf/1605.08066) claims the required linear upper bound, but that claim is not part of the frozen accepted background. Its lemmas may be repaired or reused only if their mathematical proofs and hypotheses are independently established as part of the active solution.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Produce a complete, independently checkable proof that there are absolute \(C,n_0\) with \(u(P)\le Cn\) for every strictly convex Euclidean \(n\)-gon \(P\) and all \(n\ge n_0\). The proof may use, repair, or replace ideas from the claimed preprint, but it must establish every required mathematical step.

**Negative obligation.** Construct and rigorously verify strictly convex polygons \(P_k\) with \(|P_k|\to\infty\) and \(u(P_k)/|P_k|\to\infty\). Finding a flaw in a claimed proof does not disprove the mathematical target.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a self-contained proof of \(f(n)\le Cn\) for an absolute constant \(C\), uniformly over all strictly convex \(n\)-gons. Every imported theorem must be stated with the hypotheses actually used.

A negative resolution requires an infinite family \(P_k\) of strictly convex polygons with
\[
\frac{u(P_k)}{|P_k|}\longrightarrow\infty.
\]
Invalidating or failing to validate an existing claimed proof is not a resolution of the mathematical problem.

## What does not count as a solution

- A finite search over polygons, numerical diagrams, or checks for small \(n\).
- Restating the 2017 abstract or accepting a diagrammatic argument without a formalized case analysis.
- Identifying a gap in Khopkar's preprint without proving or disproving the canonical \(O(n)\) target.
- Re-proving \(O(n\log n)\), proving a special symmetric case, or giving a bound whose constant depends on the polygon.
- Proving sparsity of a larger/smaller abstract graph class without proving that the precise geometric UDG reduction preserves the hypotheses and loses only \(O(n)\) edges.
- Claiming \(2n\) is the answer without proving that stronger statement; it is not required for \(O(n)\).

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Use unordered pairs and exact Euclidean distance \(1\); do not switch to unit-disk graphs or arbitrary unit-distance subgraphs.
2. Audit strictness of every angle inequality and every convexity inference, including endpoints, equality cases, and cyclic order.
3. In the Khopkar proof, independently verify the antipodal-line cut, the assertion that only \(O(n)\) edges are discarded, the split into the two GUDG graphs, and the ordering conventions.
4. Do not infer a linear result from path-restricted ordered bipartite graphs alone: the paper itself gives \(\Theta(n\log n)\) for that broader class.
5. Audit the special GUDG argument in Section 5: module definitions, auxiliary edges, charging/counting statements, and the use of Lemmas 10--13 leading to Theorem 4. Check that each abstract configuration is geometrically realizable or that realizability is not being silently assumed.
6. For every purported repair, re-run all downstream lemmas under the repaired hypotheses. A repair that changes a quantifier, deletes superlinearly many edges, or only treats generic configurations is insufficient.

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
