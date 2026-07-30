# Erdős Problem 15 — unconditional convergence of an alternating prime-index series

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(p_n\) be the \(n\)-th prime in strictly increasing order, so \(p_1=2,p_2=3,\ldots\). For \(N\ge1\), set
\[
S_N:=\sum_{n=1}^{N}(-1)^n\frac{n}{p_n}.
\]

Prove or disprove the unconditional proposition
\[
\exists L\in\mathbb R\quad \lim_{N\to\infty}S_N=L.
\]

This is ordinary convergence of the natural-order partial sums in \(\mathbb R\). Do not change the order, summation method, weights, or prime sequence. The series cannot converge absolutely: the prime number theorem gives \(n/p_n\sim1/\log n\).

## Frozen mathematical background

- Tao proved the affirmative statement **conditional** on a sufficiently strong quantitative Hardy--Littlewood prime-tuples conjecture: Terence Tao, *The convergence of an alternating series of Erdős, assuming the Hardy--Littlewood prime tuples conjecture*, Communications of the AMS 4 (2024), 80--96, <https://doi.org/10.1090/cams/29>; preprint <https://arxiv.org/abs/2308.07205>. This is not an unconditional solution.
- Tao records an equivalence, due to an unpublished observation of Mustafa Said (with harmless finite changes of initial terms): convergence of the target series is equivalent to convergence of
\[
\sum_{m\ge2}\frac{(-1)^{\pi(m)}}{m\log m}.
\]
See the author’s exposition <https://terrytao.wordpress.com/2023/08/14/the-convergence-of-an-alternating-series-of-erdos-assuming-the-hardy-littlewood-prime-tuples-conjecture/>.
- If \(F(x):=\sum_{m\le x}(-1)^{\pi(m)}\) satisfies \(F(x)=O(x/(\log x)^\varepsilon)\) for some \(\varepsilon>0\), then partial summation proves convergence. This is a sufficient intermediate result, not an established theorem.
- The Formal Conjectures Lean file formalizes the target but contains `sorry`, so it supplies no proof certificate: <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/15.lean>.
- A 2025 preprint by Mantzakouras concerns related integral/damped formulations and discusses hypotheses including RH; it must not be cited as a resolution of this target without a full scope check: <https://arxiv.org/abs/2505.06242>.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Provide a rigorous unconditional proof that the natural-order partial sums S_N=sum_{n<=N}(-1)^n n/p_n form a Cauchy sequence in R (equivalently, converge to a finite real limit). Every invoked estimate on primes must be proved or explicitly cited as an established unconditional theorem.

**Negative obligation.** Provide a rigorous unconditional proof that (S_N) does not converge in R, for example by proving two subsequences with distinct limits, or by proving unboundedness/another failure of the Cauchy criterion.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is an unconditional proof that \((S_N)\) is Cauchy, hence has a finite real limit.

A negative resolution is an unconditional proof that \((S_N)\) fails to converge, such as two subsequences with different limiting behavior or a proof of unboundedness.

Every prime-distribution estimate used in either route must be either proved in the submission or cited to a precise, established unconditional source. If a result is conditional, identify the exact hypothesis and classify the work as partial only.

## What does not count as a solution

- A computation, graph, fitted limiting constant, or finite verification of partial sums.
- A conditional proof under Hardy--Littlewood, RH, Cramér-type models, or a random model.
- An application of the alternating-series test without establishing eventual monotonicity of \(n/p_n\).
- A proof only of \(n/p_n\to0\), only of non-absolute convergence, or only of qualitative parity equidistribution of \(\pi(x)\).
- A proof for a smoothed, damped, Abel/Cesàro-summed, rearranged, or modified prime-gap series.
- A formal theorem declaration containing `sorry`, axioms that encode the result, or unverified automation output.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Fix \(p_1=2\) and the sign \((-1)^n\) throughout; state precisely why finite initial changes do or do not matter.
2. If using the \((-1)^{\pi(m)}\) formulation, prove the equivalence and all summation/error estimates at the claimed level of generality.
3. For any partial-summation route, verify the boundary term and the integrability of the resulting kernel, with explicit constants/ranges.
4. Audit all short-interval prime estimates for uniformity in interval length, tuple size, shifts, and exceptional sets. Do not replace Tao’s strong quantitative Hardy--Littlewood hypothesis by a weaker informal statement.
5. Separate theorem, conjecture, heuristic, numerical observation, and formalized statement in every write-up.
6. Independently adversarially check the decisive lemma before calling any result complete.

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
