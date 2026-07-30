# Erdős Problem 89 — distinct distances in the plane

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For a finite set \(A\subset\mathbb R^2\), define
\[
\Delta(A)=\{\|x-y\|_2:x,y\in A,\ x\ne y\}.
\]
Prove or disprove the following precise assertion:

> There exist absolute constants \(c>0\) and \(n_0\) such that, for every integer \(n\ge n_0\) and every \(A\subset\mathbb R^2\) with \(|A|=n\),
> \[
> |\Delta(A)|\ge c\frac{n}{\sqrt{\log n}}.
> \]

Use natural logarithms; changing base only changes \(c\). Distances are distinct positive values, not ordered pairs or multiplicities. All constants must be independent of \(A\) and \(n\).

## Frozen mathematical background

- Erdős introduced the problem and supplied the square-grid upper construction \(\min_{|A|=n}|\Delta(A)|=O(n/\sqrt{\log n})\): [Erdős (1946)](https://users.renyi.hu/~p_erdos/1946-03.pdf). This is an upper-bound construction, not a proof of the target lower bound.
- Guth and Katz proved the currently verified universal lower bound
  \[
  |\Delta(A)|=\Omega(n/\log n).
  \]
  Their peer-reviewed paper is [Guth–Katz (2015)](https://annals.math.princeton.edu/2015/181-1/p02), with the accessible preprint at [arXiv:1011.4105](https://arxiv.org/abs/1011.4105). Its framework passes through equal-distance quadruples, rigid motions, and point-line incidences in \(\mathbb R^3\).
- A 2026 peer-reviewed source still describes the gap as a factor \(\sqrt{\log n}\): [Pach–Raz–Solymosi (SoCG 2026)](https://drops.dagstuhl.de/storage/00lipics/lipics-vol367-socg2026/html/LIPIcs.SoCG.2026.83/LIPIcs.SoCG.2026.83.html).
- Treat [Yazici, arXiv:2002.01248](https://arxiv.org/abs/2002.01248) as an *unverified claimed resolution*, not accepted background. Before using it, audit the proof and seek independent confirmation. The [Formal Conjectures Lean file](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/89.lean) formalizes the statement but contains `sorry`; it is not a formal proof.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Produce a complete proof of universal constants c>0 and n0 such that every finite A⊂R² with |A|=n>=n0 has |Δ(A)|>=c n/sqrt(log n), with every reduction and asymptotic constant independent of A and n.

**Negative obligation.** Produce a rigorous infinite counterexample family A_j⊂R² with n_j=|A_j|→∞ and |Δ(A_j)|/(n_j/sqrt(log n_j))→0; equivalently, refute every proposed universal c,n0 by arbitrarily large examples.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a complete proof with explicit logical quantifiers of universal \(c,n_0\) for the canonical target.

A negative resolution is an infinite family \(A_j\) with \(|A_j|=n_j\to\infty\) such that
\[
\frac{|\Delta(A_j)|}{n_j/\sqrt{\log n_j}}\to0.
\]
This is the logical negation in asymptotic form.

## What does not count as a solution

- Reproving \(\Omega(n/\log n)\), or improving only constants there.
- A theorem for a restricted family of point sets.
- A finite computation, heuristic, numerical optimization, or empirical asymptotic fit.
- The square-grid construction by itself.
- A claim that \(n^{1-o(1)}\) distances suffice without deriving the exact \(n/\sqrt{\log n}\) lower bound.
- Citing an arXiv claim, a `sorry` declaration, or a search snippet as a proof.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State every constant dependency and every sufficiently-large threshold.
2. Verify that all distance-energy and Cauchy–Schwarz inequalities have the required direction.
3. Check diagonal exclusions, ordered/unordered conventions, and the meaning of distinct values at every reduction.
4. Audit degenerate arrangements: collinearity, many points on curves, planes/reguli in lifted incidence geometry, and grid-like cases.
5. If a new incidence or structure lemma is used, prove exactly its hypotheses for the line family generated by \(A\); do not import a generic theorem without checking exceptional surfaces.
6. Maintain a separate audit of Yazici 2020 if it is examined: identify the exact claimed implication and independently verify every nonstandard lemma.
7. Before declaring success, require an adversarial reconstruction of the full proof by agents that did not develop the main approach.

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
