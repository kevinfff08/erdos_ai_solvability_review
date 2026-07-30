# Erdős Problem 82 — research prompt

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work with finite simple undirected graphs.  For a graph \(G\), define
\[
r(G)=\max\{|S|:S\subseteq V(G),\;G[S]\text{ is }d\text{-regular for some }0\le d\le |S|-1\},
\]
and
\[
F(n)=\min_{|V(G)|=n}r(G).
\]
The target is to prove
\[
\lim_{n\to\infty}\frac{F(n)}{\log n}=+\infty.
\]
Equivalently, for every \(C>0\), every sufficiently large \(n\)-vertex graph has an induced regular subgraph on at least \(C\log n\) vertices.  Independent sets and cliques count: 0-regular subgraphs are allowed.  The logarithm base is fixed and greater than 1.

## Frozen mathematical background

The current database record is [Erdős Problem 82](https://www.erdosproblems.com/82) and its [LaTeX record](https://www.erdosproblems.com/latex/82).  Ramsey theory proves only \(F(n)\gg\log n\).  This is a theorem-level baseline, not the conjecture.

The record cites Alon, Krivelevich, and Sudakov, [*Large nearly regular induced subgraphs* (2007)](https://arxiv.org/abs/0710.2106), for related upper-bound progress.  Do not infer exact regularity from “nearly regular” without a proved conversion.

The recent preprint Dyson and McKay, [*Ramsey numbers for regular induced subgraphs* (2026)](https://arxiv.org/abs/2604.08215), is reported by the database to establish \(F(n)\ll\sqrt n\) and lower bounds for the inverse function \(G(k)\).  Those are constraints and adversarial examples; they do not establish the target lower bound.  Re-read the primary preprint before relying on any theorem statement.

The problem is historically attributed to Erdős, Fajtlowicz, and Stanton.  Treat all claims beyond the linked sources as unverified until independently located and checked.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete affirmative resolution is a rigorous proof that for every C>0 there exists N(C) such that every finite simple graph on n≥N(C) vertices has an induced d-regular subgraph on at least C log n vertices, with d allowed to depend on the graph and induced set.

**Negative obligation.** A complete negative resolution is a rigorous construction, for one fixed C<∞ and infinitely many unbounded n, of n-vertex finite simple graphs whose every induced regular subgraph has order at most C log n. This is exactly the negation of F(n)/log n→∞.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a rigorous uniform proof that for every real \(C>0\) there is \(N(C)\) such that every graph on \(n\ge N(C)\) vertices has an induced exactly regular subgraph of order at least \(C\log n\).

A negative resolution is a fixed finite \(C\), an unbounded sequence \(n_i\), and rigorously verified graphs \(G_i\) on \(n_i\) vertices for which every induced regular subgraph has at most \(C\log n_i\) vertices.  This is the logical negation of the target.

## What does not count as a solution

- A fixed-constant lower bound \(F(n)\ge c\log n\).
- A result only for random, regular, dense, sparse, or otherwise restricted graphs.
- A merely nearly regular induced subgraph.
- A non-induced regular subgraph obtained by deleting edges.
- Finite computation of \(F(n)\) or \(G(k)\) without a general theorem.
- An asymptotic argument with constants or thresholds depending on the input graph.
- An upper-bound construction for \(F\) alone.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Preserve the quantifier order \(\min_G\max_S\).
2. Check that every claimed witness is induced and exactly \(d\)-regular.
3. Include \(d=0\); do not exclude independent sets or singleton witnesses.
4. Distinguish degrees in \(G[S]\) from degrees in \(G\).
5. Audit every asymptotic assertion with explicit uniform constants and an eventual threshold.
6. For a counterexample family, prove exclusion of *all* induced regular subgraphs, not merely a selected degree or size range.
7. Independently cross-check use of the 2026 preprint against the primary text and version history.

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
