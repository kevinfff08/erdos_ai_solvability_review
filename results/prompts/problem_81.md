# Erdős Problem 81: chordal edge-clique partitions

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work with finite simple graphs. A graph is **chordal** if it has no induced cycle of length at least four.

For a graph \(G\), define \(\operatorname{cp}(G)\) to be the minimum \(k\) such that there are cliques \(C_1,\ldots,C_k\), each containing at least one edge, for which
\[
E(G)=\bigsqcup_{i=1}^k E(G[C_i]).
\]
Thus cliques may overlap in vertices, but every edge must belong to exactly one chosen clique.

Canonical target: prove or refute the existence of an absolute constant \(C\) such that, for every \(n\ge 1\) and every \(n\)-vertex chordal graph \(G\),
\[
\operatorname{cp}(G)\le \frac{n^2}{6}+Cn.
\]

## Frozen mathematical background

- Erdős, Ordman, and Zalcstein proved that some absolute \(c>0\) gives \(\operatorname{cp}(G)\le (1-c)n^2/4\) for every \(n\)-vertex chordal graph. Their abstract also records that the \(n^2/6\) threshold was open. Treat this as a theorem, subject to checking the full paper before using proof details: [Cambridge record](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/clique-partitions-of-chordal-graphs/CEA1F929F2A88B5A4C7C8E23DFD0DD29).
- Chen, Erdős, and Ordman proved \((3/16)n^2+O(n)\) for split graphs. Their paper states that for \(6\mid n\), \(K_n-\overline K_{2n/3}\) has \(\operatorname{cp}=n^2/6+n/6\). This is a lower-bound family for the canonical target: [author-hosted paper PDF](https://ordman.net/MathResearch/CEOClique_Parts.pdf).
- Recent public work on fractional triangle packing/covering, even when accompanied by Lean artifacts, does **not** establish the integral edge-clique-partition target. Its own scope disclaimer must be respected: [research repository](https://github.com/jtraverso/erdos-81-chordal-clique-partitions).
- A 2026 forum note claims only a conditional result under wCDH and is not a proof of the unrestricted theorem: [discussion thread](https://www.erdosproblems.com/forum/thread/81).

Do not assume any more detailed theorem from these sources without locating the theorem statement and checking its hypotheses.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Give a proof with an absolute constant C such that every finite n-vertex chordal graph G has an edge clique partition of cardinality at most n^2/6 + Cn.

**Negative obligation.** Prove that no such absolute C exists; equivalently, exhibit chordal graphs G_i with n_i vertices and (cp(G_i)-n_i^2/6)/n_i unbounded.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a self-contained proof of one absolute \(C\) that works for every finite chordal graph.

A negative resolution is a proof that no such \(C\) exists: equivalently, an infinite sequence \(G_i\) of chordal graphs for which
\[
\frac{\operatorname{cp}(G_i)-|V(G_i)|^2/6}{|V(G_i)|}
\]
is unbounded.

## What does not count as a solution

- Covering every edge by cliques while allowing an edge to appear twice.
- Partitioning vertices into cliques instead of partitioning edges.
- A bound with a leading quadratic coefficient larger than \(1/6\).
- A result only for split, threshold, interval, or other proper subclasses without a valid theorem reducing all chordal graphs to that class.
- A fractional packing/covering result without an integral rounding theorem whose loss is \(O(n)\).
- A theorem conditional on an unproved hypothesis.
- Exhaustive computation on bounded \(n\), a timestamped claim, or a proof still unavailable for inspection.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

- Verify that every selected set is a clique and that its full induced edge set is used.
- Prove pairwise edge-disjointness and exact coverage of \(E(G)\); checking only the number of cliques is insufficient.
- Establish chordality of every construction, preferably by an induced-cycle argument or a perfect elimination ordering.
- State all rounding conventions and show the linear error has one absolute constant.
- For a structural reduction, quantify every separator/clique-sum interface edge and prove the partition objective is preserved or charged correctly.
- For any fractional argument, identify the exact integrality statement needed and prove it rather than silently invoking LP duality or a packing-to-partition conversion.
- Compare any proposed extremizer with \(K_n-\overline K_{2n/3}\), while recognizing that matching this family does not prove global optimality.

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
