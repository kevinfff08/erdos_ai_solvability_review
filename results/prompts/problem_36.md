# Erdős Problem 36: minimum overlap constant

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For each integer \(N\ge 1\), let
\[
r_{A,B}(x)=\#\{(a,b)\in A\times B:a-b=x\},\qquad
M(N)=\min_{A\sqcup B=[2N],\ |A|=|B|=N}\ \max_{x\in\mathbb Z}r_{A,B}(x),
\]
where \([2N]=\{1,\ldots,2N\}\). The maximum is over all integers \(x\), although only \(|x|\le 2N-1\) can contribute.

The minimum-overlap constant is
\[
C=\lim_{N\to\infty}\frac{M(N)}N.
\]
The existence of this limit is accepted background. Determine \(C\) exactly. Interpret the original wording “the optimal \(c\)” as the supremum of constants \(c\) for which
\[
\exists N_0\ \forall N\ge N_0\ \forall(A,B)\ \exists x\in\mathbb Z:
 r_{A,B}(x)\ge cN.
\]
Do not assume without proof that the endpoint \(c=C\) itself satisfies this eventual inequality.

## Frozen mathematical background

- Haugland’s [2016 preprint](https://arxiv.org/abs/1609.08000) explains the reduction of asymptotic upper bounds to admissible density/step functions on \([0,2]\), with values in \([0,1]\) and integral \(1\). It reports an upper bound about \(0.380926\).
- White’s [2022 preprint](https://arxiv.org/abs/2201.05704), subsequently published as [A new bound for Erdős’ minimum overlap problem](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/online/115217/a-new-bound-for-erdos-minimum-overlap-problem), proves \(C>0.379005\) through Fourier analysis and a convex program.
- Recent preprints report stronger but not yet peer-reviewed records: [Kim--Pilanci (2026)](https://arxiv.org/abs/2606.31182) claims a certified lower bound \(C\ge0.37912\), and [Ye et al. (2026)](https://arxiv.org/abs/2604.19341) reports an upper construction \(C\le0.380856\) in an ablation run. Treat both as claims requiring independent artifact-level verification before relying on them.
- The current maintained [optimization-constants index](https://teorth.github.io/optimizationproblems/constants/1b.html) documents the sequence of reported upper constructions. The [Erdős Problems page](https://www.erdosproblems.com/36) remains open but has stale numerical records.

Theorems above are background only to the extent their cited proofs/certificates are checked. Search heuristics, LLM scores, and informal forum statements are not theorems.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Produce an explicit real number α and a complete proof that C=α: (i) for every ε>0, all sufficiently large balanced partitions have max_x r_{A,B}(x)≥(α-ε)N (or an equivalent rigorous lower-bound/limit argument), and (ii) give balanced partitions for arbitrarily large N, or a valid continuous construction with a proved transference theorem, giving M(N)/N≤α+o(1).

**Negative obligation.** For any claimed exact value α, a decisive rejection is a rigorous proof of C<α or C>α; for a claimed bound, a decisive rejection is a verified partition/function violating the asserted universal lower bound or a proof that the asserted upper construction/transference estimate is invalid.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

A complete affirmative resolution supplies an explicit \(\alpha\in\mathbb R\) and rigorous matching inequalities \(C\ge\alpha\) and \(C\le\alpha\), hence \(C=\alpha\).

Refuting a proposed value \(\alpha\) requires proving \(C<\alpha\) or \(C>\alpha\), but that refutation alone does not determine \(C\). A complete resolution must establish the exact value through matching valid lower and upper arguments.

## What does not count as a solution

- Computing \(M(N)\) for finitely many \(N\), regardless of scale.
- Reporting a sampled numerical objective without an exact or rigorously interval-certified bound for the continuous objective.
- Giving only a better upper construction or only a better lower relaxation.
- Treating an optimizer’s floating-point output as a universal lower-bound certificate.
- Proving a statement about autocorrelation of one set while failing to connect it exactly to the cross-difference quantity \(r_{A,B}\).
- Citing an AI-generated candidate, repository README, or forum post in place of a complete argument.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State every quantifier and normalize all functions and measures explicitly.
2. For an upper bound, verify range \([0,1]\), integral \(1\), all translates, endpoint conventions, and the discrete-to-continuous transference including the \(o(N)\) error.
3. For a lower bound, prove each relaxation constraint is necessary for every admissible object. Verify all dual feasibility conditions in exact rational arithmetic or validated interval arithmetic.
4. If a finite partition is claimed, recompute all cross-difference multiplicities independently from the supplied data.
5. Keep \(\liminf\), \(\limsup\), the known existence of the limit, and endpoint attainment separate.

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
