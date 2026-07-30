# Erdős Problem 12 — residual harmonic-sum question

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(\mathbb N=\{1,2,\ldots\}\). A set \(A\subseteq\mathbb N\) has **Property P** if there are no pairwise distinct \(a,b,c\in A\) such that \(b>a\), \(c>a\), and \(a\mid(b+c)\).

The first two questions in the historical Erdős–Sárközy record are closed. The sole target here is:

> Determine whether every infinite Property-P set \(A\) satisfies
> \[
> \sum_{n\in A}\frac1n<\infty.
> \]

A positive answer means this assertion holds for every such \(A\). A negative answer requires one infinite Property-P set with divergent reciprocal sum.

## Frozen mathematical background

- Erdős and Sárközy proved that every Property-P set has natural density zero, while permitting counting functions that are close to linear on infinitely many scales: [Erdős–Sárközy (1970)](https://londmathsoc.onlinelibrary.wiley.com/doi/pdf/10.1112/plms/s3-21.1.97).
- Elsholtz and Planitzer constructed a Property-P set with a uniform lower bound of order \(\sqrt x/[\sqrt{\log x}(\log\log x)^2(\log\log\log x)^2]\): [Elsholtz–Planitzer (2017)](https://link.springer.com/article/10.1007/s00605-016-0995-9).
- Under the additional hypothesis that all elements are pairwise coprime, Schoen and Baier proved upper bounds on infinitely many scales; Baier obtains \(O(N^{2/3}/\log N)\): [Baier (2004)](https://math.colgate.edu/~integers/e13/e13.pdf). This extra hypothesis is not available in the target.
- The finite extremal problem was resolved by Bedert and does not settle the infinite harmonic-sum target: [Bedert (2023), arXiv:2301.07065](https://arxiv.org/abs/2301.07065).
- The historical first question is now formally proved affirmative and the second formally disproved. Inspect the official theorem records and linked Lean artifacts: [part (i)](https://google-deepmind.github.io/formal-conjectures/theorem/?name=Erdos12.erdos_12.parts.i), [part (ii)](https://google-deepmind.github.io/formal-conjectures/theorem/?name=Erdos12.erdos_12.parts.ii), and the [discussion with human-readable constructions](https://www.erdosproblems.com/forum/thread/12). These are formal artifacts/discussion, not peer-reviewed papers.

Do not assume that a near-linear \(N^{1-o(1)}\) counting lower bound forces reciprocal-sum divergence; it does not without a quantitative shell calculation.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that for every infinite A⊆N with Property P, the nonnegative series Σ_{n∈A}1/n converges. The proof must cover all Property-P sets, without silently imposing pairwise coprimality, a block construction, or a density regularity hypothesis.

**Negative obligation.** Give one explicitly defined infinite A⊆N with Property P and prove Σ_{n∈A}1/n=∞. Both the no-divisibility condition for all pairwise distinct triples and a rigorous divergence argument are required.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a proof that every infinite Property-P set \(A\) has \(\sum_{n\in A}1/n<\infty\).

A negative resolution is an explicit infinite Property-P set \(A\), with a complete proof of both Property P and \(\sum_{n\in A}1/n=\infty\).

## What does not count as a solution

- A result only for pairwise-coprime sets or another unannounced special subclass.
- Density zero, a bound holding only on a subsequence, or a construction with large counting function but no divergence proof.
- A finite computation, finite extremal theorem, or heuristic random model.
- Verifying only triples lying within one block of a construction.
- Re-answering the already closed first or second historical questions.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

- State all quantifiers explicitly and retain pairwise distinctness of \(a,b,c\), together with the strict conditions \(b,c>a\).
- In a construction, check every cross-block pattern and every possible order of the three elements.
- Do not treat \(b+c=2a\) as an admissible forbidden triple when \(b,c>a\); it is impossible under those strict inequalities.
- For divergence, provide a valid dyadic-shell, summation-by-parts, or equivalent argument with explicit lower bounds that make the positive series diverge.
- For convergence, derive a summable upper bound valid for all sufficiently large shells and for every Property-P set, not merely for a selected construction.
- Cite every external theorem by a direct primary or formal-artifact URL and distinguish theorem, conjecture, and heuristic.

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
