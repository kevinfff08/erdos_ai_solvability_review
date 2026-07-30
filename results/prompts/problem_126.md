# Erdős Problem 126

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(\mathbb N=\{1,2,\ldots\}\).  For a positive integer \(m\), let \(\omega(m)\) be the number of distinct prime divisors of \(m\), with \(\omega(1)=0\).  Define
\[
f(n)=\min_{\substack{A\subseteq\mathbb N\\|A|=n}}\omega\!\left(\prod_{\substack{(a,b)\in A^2\\a\ne b}}(a+b)\right).
\]
Equivalently, \(f(n)\) is the largest integer lower bound valid for every \(n\)-element set \(A\).  The pair product is over ordered pairs; replacing it by unordered pairs squares the product and leaves \(\omega\) unchanged.

Prove or disprove
\[
\lim_{n\to\infty}\frac{f(n)}{\log n}=+\infty.
\]
The positive statement means: for every \(C>0\), there is \(N_C\) such that every \(n\ge N_C\) and every \(A\subseteq\mathbb N\) of cardinality \(n\) satisfy
\[
\omega\!\left(\prod_{a\ne b}(a+b)\right)\ge C\log n.
\]

## Frozen mathematical background

- Erdős and Turán proved in 1934 that the pair sums of \(3\cdot2^{k-1}\) positive integers cannot all be composed from a prescribed set of \(k\) primes.  Hence \(f(n)\gg\log n\).  Read and cite the primary paper: [Erdős–Turán (1934)](https://www.renyi.hu/~p_erdos/1934-03.pdf), bibliographically verified at [Taylor & Francis](https://www.tandfonline.com/doi/abs/10.1080/00029890.1934.11987659).
- Taking \(A=\{1,\ldots,n\}\) gives \(f(n)\le\pi(2n)\ll n/\log n\).  This is an upper bound, not evidence against the target.
- The 1934 paper appears to conjecture a much stronger estimate for the associated maximum \(n(k)\); record its exact quantifiers before using it.  It is conjectural, not accepted background.
- [The Lean statement](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/126.lean) contains `sorry` placeholders and uses nonnegative rather than positive integers.  It is not a proof.  A separate comparison is needed if it is used for definitions.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that for every real C>0 there exists N_C such that, for every integer n>=N_C and every A⊆{1,2,...} with |A|=n, ω(∏_{a≠b∈A}(a+b))>=C log n.

**Negative obligation.** Prove that the limit is not +∞. Equivalently, exhibit a finite C and infinitely many n for which there is an n-element set A_n⊆{1,2,...} satisfying ω(∏_{a≠b∈A_n}(a+b))<=C log n.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

A complete affirmative resolution proves the stated uniform \(C\)-then-\(N_C\)-then-all-\(A\) assertion.

A complete negative resolution supplies a constant \(C<\infty\), infinitely many integers \(n\), and explicit or rigorously established sets \(A_n\subseteq\mathbb N\), \(|A_n|=n\), such that
\[
\omega\!\left(\prod_{a\ne b\in A_n}(a+b)\right)\le C\log n.
\]

Before announcing either outcome, subject the actual proof or counterexample to the required independent mathematical audit.

## What does not count as a solution

- Increasing a fixed constant in the known \(c\log n\) lower bound.
- Treating only intervals, random sets, bounded-height sets, or another special family without a rigorous reduction from arbitrary sets.
- Finite computations, heuristics, or numerical plots.
- Showing only that \(f(n)\) is unbounded.
- Proving \(f(n)=o(n/\log n)\), which is compatible with the target.
- Counting prime factors with multiplicity, i.e. \(\Omega\), rather than distinct prime divisors, \(\omega\).
- Citing a database label or a formalized statement as a proof.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Preserve quantifier order and ensure constants never depend on the chosen set \(A\).
2. Track distinct prime support rather than repeated divisibility among the \(\binom n2\) sums.
3. State whether pairs are ordered, and justify any replacement by unordered pairs.
4. Keep positive integers separate from Lean's \(\mathbb N\) containing zero.  If using the Lean variant, prove the comparison between the two extremal functions.
5. Verify all asymptotic inversions involving the auxiliary maximum \(n(k)\), including monotonicity and integer rounding.
6. For any proposed counterexample family, prove its cardinality, infinitude of parameters, and prime-support estimate.
7. Require a derivation audit by an investigator who did not produce the relevant argument.

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
