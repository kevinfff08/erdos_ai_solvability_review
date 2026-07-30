# Erdős Problem 51 — least inverse totients

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(\varphi(n)=\#(\mathbb Z/n\mathbb Z)^\times\) be Euler’s totient function. A **totient** is an integer \(a\in\operatorname{Im}(\varphi)\). For each totient \(a\), define
\[
n_*(a):=\min\{n\in\mathbb N:\varphi(n)=a\}.
\]

Prove or disprove:
\[
\sup_{a\in\operatorname{Im}(\varphi)}\frac{n_*(a)}a=\infty.
\]
Equivalently, prove or disprove that for every real \(C>0\) there is a totient \(a\) such that every \(n\in\mathbb N\) satisfying \(\varphi(n)=a\) obeys \(n>Ca\). A positive proof must explicitly extract an infinite set \(A\) of totients for which \(n_*(a)/a\to\infty\) along \(a\in A\).

## Frozen mathematical background

- Kevin Ford’s 2025 CIRM problem report states exactly the constant formulation above and records that it is wide open even for \(C=3\): <https://www.cirm-math.fr/RepOrga/3213/Slides/Open-Problems-mardi2.pdf>.
- Ford’s paper *The distribution of totients* develops the distribution of totients and their preimages: <https://www.ford126.web.illinois.edu/wwwpapers/totients.pdf>. Use the published theorem only after checking its exact hypotheses and quantifiers.
- Ford proved that every multiplicity \(k\ge2\) occurs for \(\varphi\), but this does not control least preimages: <https://arxiv.org/abs/math/9907204>.
- Related work uses Erdős’s convenient-prime mechanism to preserve complete preimage patterns; it is relevant background, not a resolution of this target: <https://math.dartmouth.edu/~carlp/monotone4-1.pdf>.

Treat the following as conjectural/open, not as established background: the canonical target itself; any assertion that all preimages of a constructed totient satisfy a desired divisibility condition unless a complete proof is supplied; and any heuristic about shifted primes or smooth shifted primes.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that for every C>0 there exists a totient a such that φ(n)=a implies n>Ca. The proof must then explicitly derive an infinite sequence a_j with n_*(a_j)/a_j→∞.

**Negative obligation.** Prove a uniform constant C>0 such that every a∈Im(φ) has at least one preimage n with φ(n)=a and n≤Ca.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution consists of a rigorous proof that for every \(C>0\) there is a totient \(a\) whose full inverse image \(\{n:\varphi(n)=a\}\) is contained in \((Ca,\infty)\). It must then prove that the selected \(a\)'s can be chosen distinct and tend to infinity.

A negative resolution consists of a rigorous absolute constant \(C>0\) and a proof that every totient \(a\) has at least one preimage \(n\le Ca\).

## What does not count as a solution

- A family with large constructed preimages but no proof that smaller preimages do not exist.
- A proof for one fixed constant only, including \(C=3\).
- A statement about the number of preimages that does not bound their minimum.
- A finite table, numerical search, heuristic density argument, or probabilistic model without a theorem reducing the required check to a finite certified search.
- An application of multiplicativity that silently assumes all inverse images have the constructed form.
- A result conditional on an unproved prime-distribution hypothesis, unless it is clearly labeled conditional and separated from a complete resolution.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Define every candidate \(a\), every auxiliary set, and every asymptotic quantifier precisely.
2. For \(\varphi(n)=a\), justify a complete classification or exclusion of all possible prime factors of \(n\); do not only enumerate a preferred construction.
3. If a convenient-prime or lifting argument is used, prove both directions: every asserted preimage exists and no other preimage exists.
4. Check that inequalities use the least preimage \(n_*(a)\), not an arbitrary preimage.
5. Verify every passage between the unbounded-ratio, every-\(C\), sequence, and infinite-set formulations.
6. State dependencies on external theorems exactly, with theorem number, version, and URL. Audit whether their hypotheses hold in the proposed construction.
7. Treat the published forum claim rejected in January 2026 as invalid unless its missing minimality argument is independently repaired.

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
