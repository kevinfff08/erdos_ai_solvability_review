# Erdős Problem 68

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(n!=1\cdot2\cdots n\) for every integer \(n\ge2\), and let
\[
S=\sum_{n=2}^{\infty}\frac{1}{n!-1}.
\]
All terms are positive and the series converges absolutely. Prove or disprove the precise assertion \(S\notin\mathbb Q\). This is a single fixed real number; there is no asymptotic parameter and no intended replacement of \(n!-1\) by \(n!\), \(n!+1\), \(n!+t\), or another factorial series.

The displayed identity is the fixed mathematical target for this run.

## Frozen mathematical background

- The current Erdős Problems record is [Problem 68](https://www.erdosproblems.com/68), with [LaTeX source](https://www.erdosproblems.com/latex/68). It lists the problem as open but expressly warns that its literature coverage may be incomplete.
- The original cited source is P. Erdős, [*On the irrationality of certain series: problems and results*](https://combinatorica.hu/~p_erdos/1988-22.pdf), *New Advances in Transcendence Theory* (1988), pp. 102–109. The statement that \(\sum 1/(n!+t)\) should be transcendental for every integer \(t\) is a conjectural background statement, not an accepted theorem for \(t=-1\).
- For each \(n\ge2\),
  \[
  \frac1{n!-1}=\sum_{k=1}^{\infty}\frac1{(n!)^k}.
  \]
  Since all summands are nonnegative, Tonelli's theorem permits the corresponding double-series rearrangements. This identity alone does not settle irrationality.
- The exact conjecture is represented in Lean in [ErdosProblems/68.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/68.lean). Its main theorem is presently an open `sorry` statement; only an auxiliary geometric-series identity is proved there.
- Nearby, non-equivalent literature may inspire checks but must not be silently transferred: [Barreto–Kang–Kim–Kovač–Zhang (2026)](https://arxiv.org/abs/2601.21442) study adjacent-product unit-fraction series; [Crmarić–Kovač (2025)](https://arxiv.org/abs/2504.18712) show that another variable-denominator family can attain rational values; [Schlage-Puchta (2011)](https://arxiv.org/abs/1105.1451) treats other factorial series.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Produce a complete rigorous proof that S = sum_{n=2}^infinity 1/(n!-1) is not rational. A formal Lean proof of the exact real-series statement, or a conventional proof whose every convergence, integrality, and limiting step can be checked, qualifies.

**Negative obligation.** Produce a complete rigorous proof that S is rational, including an exact pair of integers p,q with q>0 and S=p/q; a certified construction must prove equality to the infinite series, not merely fit numerical digits.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a rigorous proof that \(S\notin\mathbb Q\).

A negative resolution is a rigorous proof that \(S\in\mathbb Q\), including an exact rational value \(p/q\) with \(q>0\) and a proof that the infinite sum equals \(p/q\).

A formal Lean proof of the exact assertion is ideal. A conventional proof is complete only if every series interchange, convergence step, denominator-clearing step, integrality claim, and limiting estimate is written explicitly enough for independent verification.

## What does not count as a solution

- More digits of OEIS A331373, empirical nonperiodicity, floating-point PSLQ, or any finite computation without a finite proof certificate.
- A proof for \(\sum1/n!\), \(\sum1/(q^n+r)\), \(\sum1/(n!+t)\) at another \(t\), or a variable factorial-type family without an exact valid reduction to this \(S\).
- Treating Erdős's broader transcendence prediction as established.
- Proving only the geometric expansion or a finite truncation identity.
- A tail estimate that has not also established the precise integrality or fractional-part obstruction required for a rationality contradiction.
- A Lean declaration containing `sorry`, an uncompiled file, or a proof of a mistranscribed statement.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. The index begins at \(n=2\); \(n=0,1\) would introduce a zero denominator.
2. Every occurrence of a factorial, subtraction, power, and reciprocal must be in the intended real/rational domain, not truncated natural-number arithmetic.
3. Any double-sum rearrangement must cite nonnegativity or absolute convergence.
4. If assuming \(S=a/b\), show exactly which multiplier clears which finite denominators. Do not presume \(N!\) is divisible by \(n!-1\).
5. If a scaled tail is said to be an integer, prove it. If it is said to lie strictly between two integers, give a strict, uniform tail bound.
6. Audit all exceptional small indices and all equality-versus-strict-inequality transitions.
7. For any claimed use of a published theorem, state its hypotheses verbatim enough to verify that \(n!-1\) satisfies them.
8. If formalizing, verify that the target is the `Irrational` statement in `ErdosProblems/68.lean`, not merely its auxiliary identity.

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
