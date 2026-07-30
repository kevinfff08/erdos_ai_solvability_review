# Erdős Problem 28 — research prompt

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(A\subseteq\mathbb N\), where choosing \(\mathbb N=\{0,1,\ldots\}\) or \(\{1,2,\ldots\}\) is immaterial because the hypothesis and conclusion are stable under finite changes. Define
\[
r_A(n):=(1_A*1_A)(n)=\#\{(a,b)\in A\times A:a+b=n\}.
\]
Representations are **ordered**, and diagonal pairs \((a,a)\) count once. Say that \(A\) is an asymptotic additive basis of order \(2\) if there exists \(N_0\) such that every \(n\ge N_0\) belongs to \(A+A\), equivalently \(r_A(n)\ge1\).

Prove or disprove:
\[
\forall A\subseteq\mathbb N,\quad [A+A\text{ contains every sufficiently large integer}]\Longrightarrow\limsup_{n\to\infty}r_A(n)=\infty.
\]
Equivalently, under eventual coverage, for every \(M,X\in\mathbb N\) there must be \(n\ge X\) with \(r_A(n)\ge M\).

## Frozen mathematical background

- Erdős and Turán posed the problem in 1941: [Erdős–Turán, *J. London Math. Soc.*](https://doi.org/10.1112/jlms/s1-16.4.212). Their stronger conjecture is \(\limsup r_A(n)/\log n>0\); it is not the target here.
- Borwein, Choi, and Chu proved that an asymptotic order-2 basis cannot have its representation function globally bounded by \(7\): [*Mathematics of Computation* 75 (2006), 475–484](https://www.ams.org/mcom/2006-75-253/S0025-5718-05-01777-1/). This is a theorem, not a proof of unboundedness.
- Dowd studied finite and coding-theoretic formulations: [*SIAM J. Discrete Math.* 1 (1988), 142–150](https://doi.org/10.1137/0401016). A transfer between finite cyclic groups and the one-sided infinite problem must be proved, never presumed.
- Li and Zhang prove recent density-conditioned finite lower bounds, including \(\overline d(\mathbb N\setminus(A+A))<7/32\Rightarrow\limsup r_A>5\): [arXiv:2605.30922](https://arxiv.org/abs/2605.30922). This still gives only a fixed lower bound when \(A+A\) is cofinite.
- Ding, Sun, and Zhao prove \(R_m\le128\) for every finite cyclic group: [arXiv:2607.06167](https://arxiv.org/abs/2607.06167). This is relevant finite-group context, not a counterexample.
- The target statement has an official Lean declaration, but its proof is still `sorry`: [FormalConjectures/ErdosProblems/28.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/28.lean).
- Treat claimed proofs by Theophilus Agama ([arXiv:1707.05679](https://arxiv.org/abs/1707.05679)) and Konstantinos Smpokos ([OSF preprint record](https://sciety.org/articles/activity/10.31219/osf.io/mxgbu)) as unverified claims only. They must be independently audited before any lemma is reused.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete proof that for every A⊆ℕ and every N0 with [N0,∞)∩ℕ⊆A+A, for every M,X∈ℕ there is n≥X with #{(a,b)∈A²:a+b=n}≥M.

**Negative obligation.** An explicit set A⊆ℕ (with a mathematically precise membership rule) and a finite C such that A+A contains every sufficiently large natural number and #{(a,b)∈A²:a+b=n}≤C for every n∈ℕ, together with complete proofs of both properties.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a complete proof of the displayed universal implication, with all finite-exception and ordered-count conventions explicit.

A negative resolution is an explicit \(A\subseteq\mathbb N\), a finite constant \(C\), and complete proofs that \(A+A\) is cofinite and \(r_A(n)\le C\) for every \(n\). The construction must have a precise membership rule, not merely a numerical prefix.

## What does not count as a solution

- A result for a density-restricted, random, periodic, or otherwise special class of bases.
- Excluding one additional fixed bound \(C\), or recovering the known \(C=7\) result.
- An average-order theorem, a positive-density conclusion, or \(\limsup r_A>K\) for one fixed \(K\).
- A computation with no proved finite-to-infinite reduction, stopping condition, and exhaustive certificate.
- A construction in \(\mathbb Z\) or \(\mathbb Z_m\) presented as a construction in \(\mathbb N\).
- A proof for unordered representations without a fully justified conversion to the ordered statement.
- Reliance on an unreviewed claimed proof without line-by-line verification.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State whether \(0\in\mathbb N\); show any finite convention change is harmless.
2. Verify every use of \(r_A\) counts ordered pairs, including the diagonal.
3. Preserve the exact hypothesis \(\exists N_0\,\forall n\ge N_0\), rather than a density-one or subsequential substitute.
4. Prove a limsup conclusion, not merely one large value or an average estimate.
5. For every finite-group reduction, prove the direction and quantify all losses; do not infer an infinite basis from bounded \(R_m\).
6. Audit all compactness, limit, and truncation arguments for preservation of both eventual coverage and a uniform representation bound.
7. For every computational claim, provide code, deterministic environment instructions, input domain, symmetry reductions, machine-readable output, and a human-checkable exhaustiveness certificate.
8. If a Lean proof is claimed, compile with no `sorry`, `admit`, or new axioms and compare the theorem type directly with the canonical target.

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
