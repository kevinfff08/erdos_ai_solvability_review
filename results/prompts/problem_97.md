# Erdős Problem 97

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work in the Euclidean plane. A convex polygon is a finite nondegenerate polygon whose vertices are in convex cyclic order; state explicitly whether strict convexity is used and prove it for every proposed construction. Let \(V(P)\) be its vertex set.

Determine whether the following statement is true:

> For every finite convex polygon \(P\), there is a vertex \(v\in V(P)\) such that, for every \(r>0\),
> \[
> |\{w\in V(P)\setminus\{v\}: |v-w|=r\}|\leq 3.
> \]

Equivalently, disprove it by producing one convex polygon in which every vertex has at least four distinct other vertices at a common distance from it. The radius may depend on the vertex.

## Frozen mathematical background

The current record is [Erdős Problems 97](https://www.erdosproblems.com/97), with [LaTeX source](https://www.erdosproblems.com/latex/97). It reports, but does not itself replace primary-source checking of, the following historical facts:

- Erdős's 1946 threshold-3 conjecture was refuted by a Danzer 9-vertex convex construction.
- Fishburn and Reeds, [*Unit distances between vertices of a convex polygon*](https://doi.org/10.1016/0925-7721(92)90008-2), *Computational Geometry* (1992), gave a 20-vertex construction in which each vertex has three equidistant other vertices, with a common distance.
- The current record questions a 1975 attribution that Danzer had constructions for every threshold. Treat that attribution as unverified unless the original source is inspected.
- Dropping convexity yields easy unit-distance-graph counterexamples; they are irrelevant to the target.

The threshold-3 constructions are theorems/background only after their exact statements have been inspected. The threshold-4 statement is the conjectural target; do not treat it as known from the database label or the formalization marker.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that for every finite convex polygon P there is a vertex v such that every set {w in V(P) minus {v} : |v-w|=r} has cardinality at most 3 for every r>0.

**Negative obligation.** Give a finite convex polygon P and, for every v in V(P), exhibit four distinct vertices w1,w2,w3,w4 different from v and a number r_v>0 with |v-w_i|=r_v for i=1,2,3,4; prove that the listed cyclic order is convex and that all asserted equalities are exact.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a complete proof that every finite convex polygon has a vertex all of whose distance classes have size at most three.

A negative resolution is an explicit finite convex polygon \(P\), together with for every \(v\in V(P)\) four distinct witnesses \(w_1,\ldots,w_4\) and an exact \(r_v>0\) satisfying \(|v-w_i|=r_v\), plus a proof of convexity and of every equality.

Do not replace the target by the stronger common-radius problem or by a nonconvex variant.

## What does not count as a solution

A figure, floating-point experiment, database label, search snippet, forum claim, or uninspected citation does not settle the problem. Neither does a configuration that works only at selected vertices, has only three equal-distance neighbours, is nonconvex, has an unproved cyclic order, or uses four equal segments not all incident with the relevant vertex.

Do not confuse four vertices equidistant from \(v\) with four vertices mutually equidistant. Do not replace “at least four” by “exactly four.” A common radius for all central vertices is optional and would be a stronger counterexample, not the required one.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

For an affirmative proof, verify the full quantifier order: \(P\) is arbitrary; \(v\) may depend on \(P\); and every radius at that \(v\) is controlled.

For a counterexample, provide exact coordinates or an exact symbolic construction, certify the cyclic order and convexity, make the four witnesses distinct for each central vertex, and verify the squared-distance identities exactly. Audit any use of strict convexity, collinearity exclusions, symmetry reductions, and limiting arguments.

Check every historical claim against a primary or authoritative source. Record publication status and distinguish a theorem from a conjecture, a database annotation, or an informal assertion.

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
