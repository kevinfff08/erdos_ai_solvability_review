# Erdős Problem 64 — Erdős–Gyárfás conjecture

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work with finite, nonempty, simple, undirected graphs.  For a graph \(G\), write \(\delta(G)\) for its minimum vertex degree.  A cycle always means a simple cycle, and its length is its number of edges (equivalently vertices).

Prove or disprove the following statement:

> For every finite simple undirected graph \(G\) with \(\delta(G)\ge 3\), there are an integer \(k\ge2\) and a simple cycle \(C\subseteq G\) with \(|C|=2^k\).

Thus the allowed cycle lengths are \(4,8,16,32,\ldots\).  The exponent and cycle may depend on \(G\).  No connectedness assumption is made or needed.

A negative resolution must give one explicit finite simple graph \(G\) with \(\delta(G)\ge3\) that has no simple cycle of every allowed length \(2^k\le |V(G)|\).

## Frozen mathematical background

The following are accepted only with the stated scope; do not silently strengthen them.

1. Liu and Montgomery proved that there is an absolute average-degree threshold forcing a cycle whose length is a power of two.  This disproves the historical stronger conjecture that counterexamples exist at arbitrarily large minimum degree; it does **not** settle the fixed threshold \(\delta(G)\ge3\).  Their article is peer-reviewed in JAMS 36 (2023), 1191–1234: https://arxiv.org/abs/2010.15802 and https://wrap.warwick.ac.uk/id/eprint/171505/.
2. Gao and Shan proved the conjecture for \(P_8\)-free graphs, in fact producing a 4- or 8-cycle: https://arxiv.org/abs/2109.01277.
3. Hu and Shen extended that restricted-class result to \(P_{10}\)-free graphs: https://arxiv.org/abs/2308.05675.
4. Hegde, Sandeep, and Shashank report a computer-assisted proof for \(P_{13}\)-free graphs.  This is a preprint, not a general theorem: https://arxiv.org/abs/2410.22842.  Accompanying code is at https://github.com/rbsandeep/Erdos-Gyarfas.
5. Carr proved the diameter-2 subclass (a 4- or 8-cycle) in a preprint accepted for BICA: https://arxiv.org/abs/2508.19302.  A later preprint derives conditional degree structure for a hypothetical minimal counterexample: https://arxiv.org/abs/2605.22844.
6. The official current problem record is https://www.erdosproblems.com/64.  Its Lean file is only a statement containing `sorry`, not a proof: https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/64.lean.

Before relying on any source, inspect its theorem statement and distinguish a peer-reviewed theorem, a preprint claim, a computational experiment, and a conjectural remark.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete affirmative resolution is a rigorous proof that every finite simple undirected graph G with δ(G)≥3 contains a simple cycle C with |C|=2^k for some integer k≥2. The proof must cover arbitrary order, disconnected graphs, and all exponents permitted by the statement.

**Negative obligation.** A complete negative resolution is one explicit finite simple undirected graph G, together with a checkable certificate that δ(G)≥3 and that G has no simple cycle of length 2^k for every k≥2 with 2^k≤|V(G)|. Since G is finite, this is a finite exhaustive cycle-length verification.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a complete proof for every finite simple graph \(G\) with \(\delta(G)\ge3\), including arbitrary order and disconnected graphs.

A negative resolution is an explicit finite simple graph \(G\), plus independently checkable evidence that:

1. every vertex has degree at least 3; and
2. for every integer \(k\ge2\) with \(2^k\le |V(G)|\), \(G\) has no simple cycle of length \(2^k\).

For a negative resolution, provide the graph in a canonical machine-readable format and an independently reproducible certificate or verifier.

## What does not count as a solution

- A proof only for a named subclass such as cubic, planar, claw-free, diameter-2, \(P_t\)-free, or sufficiently high average/minimum degree.
- A graph without 4-cycles, or even without 4- and 8-cycles, if it has a 16-, 32-, or other permitted cycle.
- An infinite graph, a multigraph, a graph with loops, or an object whose conventions differ from finite simple graphs.
- A closed walk that repeats vertices rather than a simple cycle.
- A computation over graphs up to a specified order, unless the work proves that this bounded domain exhausts the mathematical target.
- A claimed reduction that loses the minimum-degree hypothesis, changes cycle length, or proves only average-degree information.
- A Lean declaration with `sorry`, an unverified forum post, or a search-result snippet.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State graph conventions before every reduction and verify that all transformations preserve simplicity and the needed minimum-degree condition.
2. For every constructed cycle, list why it is simple and calculate its exact length; “even” or “close to a power of two” is insufficient.
3. For a minimal-counterexample argument, justify the chosen minimality order and every use of it.  In particular, deletion typically lowers neighboring degrees and cannot be treated as harmless.
4. For a counterexample, check every \(2^k\le |V(G)|\), not just the smallest powers.  Provide an independent cycle enumerator or a formally specified verifier.
5. For computer-assisted lemmas, prove search-space completeness, isomorphism handling, pruning validity, induced-path conventions, and stopping condition.  Preserve raw logs, source revision, compiler/environment, and exact input hashes.
6. Audit all imported literature claims against their primary sources.  Do not infer the \(\delta\ge3\) theorem from Liu–Montgomery's high-average-degree theorem.

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
