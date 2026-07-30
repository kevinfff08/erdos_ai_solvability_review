# Erdős Problem 119(iii): cumulative growth of unit-circle products

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(\mathbb T=\{w\in\mathbb C:|w|=1\}\). Let \((z_i)_{i\ge1}\) be an arbitrary infinite sequence in \(\mathbb T\); repetitions and arbitrary ordering are allowed. Define
\[
p_n(w)=\prod_{i=1}^n(w-z_i),\qquad
M_n=\max_{w\in\mathbb T}|p_n(w)|\quad(n\ge1).
\]
The maximum exists because \(\mathbb T\) is compact.

Prove or disprove the following residual target:
\[
\forall (z_i)\subset\mathbb T\;\exists c>0\;\exists N_0\;\forall n\ge N_0,
\qquad \sum_{k=1}^{n}M_k>n^{1+c}.
\]

Use this quantifier order unless primary historical sources establish that the intended problem requires an absolute exponent \(c\) independent of the sequence. Do not silently switch to that stronger version. “For all large \(n\)” means every integer \(n\ge N_0\), and the inequality is strict.

## Frozen mathematical background

- Wagner proved the first, weaker question: for every admissible sequence, \(M_n>(\log n)^c\) for infinitely many \(n\), for some \(c>0\). See Gerold Wagner, [On a Problem of Erdős in Diophantine Approximation](https://doi.org/10.1112/blms/12.2.81), *Bull. London Math. Soc.* 12 (1980), 81–88.
- Beck proved the second question: a polynomial lower bound for \(\max_{m\le N}M_m\), hence polynomially large individual values for infinitely many indices. See József Beck, [The modulus of polynomials with zeros on the unit circle: A problem of Erdős](https://annals.math.princeton.edu/1991/134-3/p03), *Ann. of Math.* 134 (1991), 609–651.
- Erdős gave a sequence with \(M_n\le n+1\); Linden improved this to a sequence with \(M_n\ll n^{1-c_0}\) for some \(c_0>0\). See C. N. Linden, [The Modulus of Polynomials with Zeros on the unit Circle](https://academic.oup.com/blms/article/9/1/65/293413), *Bull. London Math. Soc.* 9 (1977), 65–69.
- The current Erdős Problems record still lists the third question as open and the first two as resolved: [Problem #119](https://www.erdosproblems.com/119). Its Lean statement is available in [Formal Conjectures #119](https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB119%C2%BB/), but the relevant theorem declarations contain `sorry`; this is not a proof.
- Treat reports from July 2026 of a one-page AI/human proof as unverified until an actual proof text or a proof-assistant artifact can be inspected. They are not accepted background.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that for every sequence (z_i) in the unit circle there exist c>0 and N_0 such that, for every integer n>=N_0, sum_{k=1}^n max_{|w|=1} product_{i=1}^k |w-z_i| > n^(1+c), with the quantifier convention stated in the canonical target.

**Negative obligation.** Exhibit one explicit infinite sequence (z_i) in the unit circle and prove that it defeats every positive exponent: for every c>0 and every N_0 there exists an integer n>=N_0 with sum_{k=1}^n M_k <= n^(1+c).

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution must give a rigorous proof of the displayed target for every admissible infinite sequence, including explicit quantifier handling for \(c\) and \(N_0\).

A negative resolution must give one explicit admissible infinite sequence and prove
\[
\forall c>0\;\forall N_0\;\exists n\ge N_0,
\qquad \sum_{k=1}^{n}M_k\le n^{1+c}.
\]

If archival research establishes that the intended exponent must be universal across sequences, document the exact source and treat that as a separate, stronger target rather than changing this one retroactively.

## What does not count as a solution

- A proof of \(\limsup M_n=\infty\), a logarithmic lower bound, or Beck's already-known initial-maximum theorem.
- Polynomially large \(M_n\) on merely infinitely many indices.
- A cumulative lower bound only along a subsequence of endpoints, without a proof covering every sufficiently large endpoint.
- A result for random, equidistributed, distinct, or specially ordered zeros only.
- Numerical experiments, plots, or finite exhaustive checks without a finite certificate that implies the quantified infinite theorem.
- A theorem declaration with `sorry`, a media report, or an inaccessible “one-page proof.”

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Verify that every argument is uniform over arbitrary ordered sequences in \(\mathbb T\), with repeated values allowed.
2. State whether each constant is absolute or sequence-dependent; never move a constant across a universal quantifier without proof.
3. Preserve the distinction between “infinitely many \(n\)” and “all sufficiently large \(n\).”
4. Track the sum convention \(\sum_{k=1}^n\). If using \(M_0=1\), \(\sum_{k<n}\), or dyadic intervals, prove the endpoint conversion.
5. Any block estimate must show exactly how it yields the all-\(n\) prefix-sum conclusion; bounds at isolated dyadic scales alone are insufficient.
6. Check any use of a maximum-over-prefix statement: it controls a peak, not automatically the density or total mass of peaks.
7. For a candidate 2026 proof, first write its precise claimed theorem, then independently verify all hypotheses, normalization factors, inequalities, and the final quantifier conversion.

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
