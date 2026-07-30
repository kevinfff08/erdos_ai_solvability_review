# Erdős Problem 19: finite residual of the Erdős–Faber–Lovász conjecture

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For an integer \(n\ge 1\), let \(G\) be a finite simple graph with subgraphs \(C_1,\ldots,C_n\) such that each \(C_i\cong K_n\), the edge sets \(E(C_i)\) are pairwise disjoint, and \(E(G)=\bigcup_i E(C_i)\). Equivalently, the cliques may share vertices but any two share at most one vertex. Prove that \(\chi(G)=n\) for every such \(n,G\), or disprove it by an explicit counterexample.

The lower bound \(\chi(G)\ge n\) is immediate from any \(C_i\cong K_n\). Thus the substantive target is \(\chi(G)\le n\).

This is a revised finite-range target. Kang, Kelly, Kühn, Methuku, and Osthus proved the assertion for every sufficiently large \(n\). Use the exact effective threshold or finite reduction supplied by that theorem, and resolve every remaining case \(13\le n<N\) not covered by the frozen results.

## Frozen mathematical background

- Kang, Kelly, Kühn, Methuku, and Osthus, [A proof of the Erdős–Faber–Lovász conjecture](https://annals.math.princeton.edu/2023/198-2/p02), *Annals of Mathematics* 198(2), 537–618 (2023), proves the EFL assertion for every sufficiently large \(n\), and stability results. This is a theorem, not a proof for every \(n\).
- The corresponding [arXiv preprint](https://arxiv.org/abs/2101.04698) is useful for version comparison.
- Kang et al., [Algorithmic aspects](https://research.birmingham.ac.uk/en/publications/a-proof-of-the-erd%C3%B6s-faber-lov%C3%A1sz-conjecture-algorithmic-aspects/), FOCS 2022, give a randomized polynomial-time construction for the sufficiently-large regime. This does not close the finite residual.
- Kirchweger, Peitl, and Szeider, [A SAT Solver’s Opinion](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SAT.2023.13), SAT 2023, prove verified small cases: all \(n\le12\) and stated additional parameter ranges for \(13\le n\le18\), using independently checkable DRAT proofs. Treat their exact theorem statement as the authoritative coverage boundary.
- Kahn, [Coloring nearly-disjoint hypergraphs with \(n+o(n)\) colors](https://doi.org/10.1016/0097-3165(92)90096-D), JCTA 59 (1992), proves an asymptotic approximation only.
- The Erdős Problems [discussion thread](https://www.erdosproblems.com/forum/thread/19) describes the community-database status as “decidable rather than proved.” This is status context, not a substitute for proof checking.

You may use the equivalent linear-hypergraph/line-graph formulations only after writing the exact map and verifying that it preserves all hypotheses and the required colouring notion.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Produce a rigorous proof that every finite residual parameter n below a correctly derived threshold N satisfies the canonical EFL statement, together with a verified derivation that all n≥N are covered by Kang–Kelly–Kühn–Methuku–Osthus. Equivalently, prove the original universal statement for every n≥1.

**Negative obligation.** Exhibit a specific n≥1, a finite simple graph G, and n explicit K_n subgraphs whose edge sets are pairwise disjoint and whose union is E(G), plus a rigorous certificate that χ(G)≥n+1 (or an independently checkable unsatisfiability certificate for n-colourability).

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution must provide both:

1. a checked derivation from the Annals theorem of a concrete finite residual domain (or a valid exact alternative finite reduction); and
2. a rigorous proof covering every residual instance, with no unstated computational gap.

A negative resolution must provide one explicit \(n\), graph \(G\), and clique decomposition satisfying the canonical hypotheses, together with a proof that \(G\) is not \(n\)-colourable. A machine-assisted negative resolution must include a replayable, independently checkable unsatisfiability certificate.

## What does not count as a solution

- Restating that the theorem holds for sufficiently large \(n\).
- Treating a finite but unknown or impractically unspecified range as solved.
- Search exhaustion without complete isomorphism coverage and checkable proof logs.
- A colouring result for only one special class, one edge-count range, fractional colouring, or a changed hypergraph convention.
- A solver result whose symmetry-breaking constraints, encoding, certificate checker, or input-generation coverage cannot be audited.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

- State whether every graph edge is in one designated \(K_n\), and verify pairwise edge-disjointness of all designated cliques.
- Verify \(\chi(G)\ge n\) from a clique and separately verify the claimed \(n\)-colouring or non-colourability.
- If dualizing, define linearity, chromatic index, strong vertex colouring, the dual hypergraph, and the exact equivalence.
- Audit every invocation of the large-\(n\) theorem: its hypotheses, threshold, asymptotic quantifiers, effectiveness, and all parameter translations.
- For computation, validate the canonical augmentation/symmetry quotient, SAT encoding, DRAT proof checker, and a coverage theorem for all residual isomorphism classes.

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
