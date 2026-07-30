# Erdős Problem 5: all normalized consecutive-prime-gap limit points

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(p_n\) denote the \(n\)-th prime and let
\[
g_n:=p_{n+1}-p_n.
\]
All logarithms are natural. Define the finite limit-point set
\[
S:=\left\{C\in[0,\infty):\exists\ n_1<n_2<\cdots,\ n_i\to\infty,\ \frac{g_{n_i}}{\log n_i}\to C\right\}.
\]

The canonical target is
\[
S=[0,\infty).
\]
Equivalently, prove or disprove that for every finite \(C\ge0\), every \(\varepsilon>0\), and every \(N\ge1\), there is an \(n\ge N\) with
\[
\left|\frac{p_{n+1}-p_n}{\log n}-C\right|<\varepsilon.
\]

The primes must be consecutive. The separate extended-real assertion \(\infty\in S\) is already known. Literature frequently normalizes by \(\log p_n\); it is legitimate to transfer between the two normalizations only after explicitly using \(p_n\sim n\log n\), hence \(\log p_n/\log n\to1\).

## Frozen mathematical background

Verify exact theorem statements before use. The following are accepted prior results, not a solution of the canonical target.

- Goldston, Pintz, and Yıldırım prove \(\liminf g_n/\log p_n=0\), so \(0\in S\): https://annals.math.princeton.edu/2009/170-2/p10
- Banks, Freiberg, and Maynard prove that among any nine prescribed nonnegative targets, one pairwise difference is a limit point; in particular at least 12.5% of nonnegative reals are limit points: https://doi.org/10.1112/plms/pdw036
- Pintz proves a fixed interval \([0,c]\subset S\) for some ineffective \(c>0\), and later improves a measure lower bound: https://arxiv.org/abs/1305.6289 and https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/184/4/112647/a-note-on-the-distribution-of-normalized-prime-gaps
- Merikoski proves \(\lambda(S\cap[0,T])\ge T/3\) for every \(T\ge0\) and that \(S\) has bounded gaps: https://doi.org/10.1112/jlms.12314
- The current historical record, including the large-gap result giving \(\infty\) as an extended limit point, is: https://www.erdosproblems.com/5

Do not treat a positive-measure, positive-density, or bounded-gap statement as interval coverage. A 2026 upload calling itself a conditional solution depends on an unproved Hardy–Littlewood-type hypothesis and is not accepted as an unconditional result: https://www.researchgate.net/publication/405816241_Analytical_Investigation_of_Normalized_Prime_Gaps_and_Residue-Class_Driven_Sequences_A_conditional_solution_to_Erdos_Problem_5_by_the_use_of_AI

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that for every finite C≥0, ε>0, and N≥1, there exists n≥N such that |(p_{n+1}-p_n)/log n-C|<ε. Equivalently, construct for each C an increasing subsequence along which the quotient converges to C.

**Negative obligation.** Prove that there exist a finite C≥0, ε>0, and N_0 such that for every n≥N_0, |(p_{n+1}-p_n)/log n-C|≥ε. This proves C is not a limit point and disproves the universal statement.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is an unconditional proof that every finite \(C\ge0\) belongs to \(S\), with an unbounded index sequence for each \(C\), consecutiveness of the two primes, and normalization conversion all justified.

A negative resolution is an unconditional proof of one finite \(C\ge0\), an \(\varepsilon>0\), and \(N_0\) such that every \(n\ge N_0\) stays at least \(\varepsilon\) away from \(C\) after normalization.

## What does not count as a solution

- Covering only \(C=0\), a fixed initial interval, a large finite target, or a positive-measure/positive-density/relatively-dense subset.
- A conditional result under Hardy–Littlewood, Elliott–Halberstam, or another unproved assumption, unless explicitly labelled conditional.
- A numerical experiment, fitted distribution, or finite list of approximate gaps.
- A claim about primes that are not proved consecutive.
- Replacing \(\log n\) with \(\log p_n\), or changing scales, without a stated asymptotic transfer.
- Proving only \(\infty\) is an extended limit point.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State the \(C,\varepsilon,N\) quantifier order and exhibit unbounded indices.
2. For each alleged consecutive gap, certify that every integer strictly between the endpoints is composite.
3. Track all parameters from construction scale to prime index and prove every \(\log p_n\leftrightarrow\log n\) replacement.
4. Separate \(C=0\), finite \(C>0\), and the extended \(\infty\) statement.
5. Check all analytic inputs for uniformity ranges, exceptional moduli, admissibility, and error terms.
6. Do not infer full coverage from Lebesgue measure, density, or bounded gaps.
7. Have an adversary attempt to convert each asserted limit into an explicit \(\varepsilon,N\) statement and locate any missing dependency.
8. Before a completion claim, repeat a current literature search and inspect the primary source for every claimed predecessor or competing result.

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
