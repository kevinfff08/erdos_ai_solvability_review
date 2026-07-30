# Erdős Problem 112: exact oriented-graph Ramsey numbers

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For integers a,b >= 2, an oriented graph is a finite loopless digraph with at most one directed arc between each unordered pair of distinct vertices. An independent set I_a is a set of a vertices with no arc in either direction between any two of them. Let L_b be the transitive tournament on b vertices: its vertices admit an order v_1,...,v_b and its arcs are exactly v_i -> v_j for i<j.

Define k(a,b)=r(I_a,L_b) as the least N such that every oriented graph on N vertices contains I_a or L_b. Determine k(a,b) exactly for every a,b >= 2. Boundary conventions are k(1,b)=k(a,1)=1.

Do not replace this with the directed-path variant. Do not allow anti-parallel arcs. If a source uses a different convention, state the difference and do not transfer its theorem without proof.

## Frozen mathematical background

- Erdős and Rado (1967) gave fixed-b polynomial upper bounds; the current problem record states k(a,b)<= [2^(b-1)(a-1)^b+a-2]/(2a-3). Source: https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms/s1-42.1.624
- Larson and Mitchell (1997) studied these digraph Ramsey numbers and obtained improved estimates. Source: https://doi.org/10.1007/BF02558478
- Ihringer, Rajendraprasad, and Weinert proved r(I_4,L_3)=15, r(I_5,L_3)=23, r(I_a,L_3)=Theta(a^2/log a), and for fixed b>3, r(I_a,L_b)<=C_b a^(b-1)/(log a)^(b-2). These are theorems, not exact general formulas. Sources: https://arxiv.org/abs/1707.09556 and https://doi.org/10.1016/j.disc.2020.112268
- The 2021 paper identifies r(I_3,L_4) as a plausible next exact instance. This is a suggested restricted target, not a theorem and not a required method.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** For the canonical oriented-graph problem, prove an exact all-parameter theorem: give a formula, recurrence with proved base cases and a terminating exact evaluation procedure, or another unambiguous characterization that yields k(a,b) for every a,b>=2; prove both the universal upper bound and matching oriented-graph lower-bound constructions for every parameter pair.

**Negative obligation.** Disprove a proposed exact characterization by constructing certified oriented graphs that violate it, then replace the false candidate. The all-parameter determination task is complete only when the exact values are established; changing the graph convention is outside the canonical target.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

A complete solution must prove an exact all-parameter characterization of k(a,b): an explicit formula, or a recurrence plus proved base cases and a terminating exact evaluation procedure, or an equally unambiguous theorem yielding every k(a,b). It must include both:

1. a universal proof that every oriented graph on k(a,b) vertices contains I_a or L_b; and
2. for every pair a,b, a certified oriented graph on k(a,b)-1 vertices containing neither.

An argument based on a different digraph convention does not resolve the canonical oriented-graph target.

## What does not count as a solution

- A fixed-b asymptotic, a one-sided bound, or a numerical table.
- A proof only for b=3, only for finitely many a, or only for a special graph class.
- A computer search without a complete instance encoding, exhaustive coverage proof, and independently checkable certificate.
- A directed-path proof or use of k(a,b)=(a-1)(b-1); that concerns another problem.
- An argument using bidirected arcs, an incomplete subtournament, or a merely acyclic induced subgraph in place of L_b.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Verify every graph is oriented: no loops and no anti-parallel pair.
2. Verify I_a means no adjacency in either direction.
3. Verify each claimed L_b is complete on its chosen vertices and has a single transitive ordering.
4. For every lower-bound construction, supply a reproducible certificate for absence of both I_a and L_b.
5. For every upper bound, quantify over all N-vertex oriented graphs and check base cases and parameter ranges.
6. Keep exact equalities separate from O, Omega, and Theta assertions; state all dependence of constants.
7. Audit all Ramsey reductions for parameter order and inequality direction.
8. Distinguish proved theorems, conjectures, deductions, and computations throughout the paper.

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
