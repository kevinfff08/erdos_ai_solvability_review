# Erdős Problem #1: distinct subset sums

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(A\) be a finite set of positive integers. Call \(A\) **sum-distinct** (or dissociated in this integer setting) when the map
\[
S\subseteq A\longmapsto \sum_{a\in S}a
\]
is injective. Equivalently, for every two distinct subsets \(S,T\subseteq A\), their sums differ; equivalently, there is no nonzero coefficient vector \(\varepsilon\in\{-1,0,1\}^{A}\) with \(\sum_{a\in A}\varepsilon_a a=0\).

Define
\[
m(n):=\min\{\max A: A\subset\mathbb Z_{>0},\ |A|=n,\ A\text{ is sum-distinct}\}.
\]

Canonical target: prove that there is an absolute constant \(c>0\) such that
\[
m(n)\ge c2^n\quad\text{for every }n\ge1.
\]
Equivalently, for every \(N,n\ge1\) and every \(A\subseteq\{1,\ldots,N\}\) with \(|A|=n\) and distinct subset sums, prove \(N\ge c2^n\). The constant must not depend on \(n\), \(N\), or \(A\).

A disproof is a rigorously verified sequence \(A_j\) of sum-distinct positive-integer sets with \(|A_j|\to\infty\) and \(\max A_j/2^{|A_j|}\to0\).

## Frozen mathematical background

- The elementary counting argument gives \(m(n)\ge(2^n-1)/n\).
- Dubroff, Fox, and Xu proved
  \[
  m(n)\ge\binom n{\lfloor n/2\rfloor}
  =\left(\sqrt{2/\pi}-o(1)\right)\frac{2^n}{\sqrt n}.
  \]
  Their paper supplies a Berry--Esseen argument and a second proof via Harper's vertex-isoperimetric inequality: [arXiv version](https://arxiv.org/abs/2006.12988), [published SIAM version](https://doi.org/10.1137/20M1385883).
- Steinerberger gave a Fourier/random-walk proof of the same best known asymptotic lower bound and a real 1-separated extension: [published paper](https://doi.org/10.1142/S1793042123500860).
- Constructions show the exponential scale is attainable from above; Bohman's construction gives \(m(n)<0.22002\,2^n\) asymptotically: [paper](https://doi.org/10.1090/S0002-9939-96-03653-2).
- The 2025 paper of Cambie, Gao, Kim, and Liu proves a sharp result for a modular variant, not for this target: [journal page](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/en/publishing-house/journals-and-series/acta-arithmetica/all/217/4/115883/the-erdos-distinct-subset-sums-problem-in-a-modular-setting).
- The exact finite extremal function is OEIS [A276661](https://oeis.org/A276661). Its finite values and constructions are background only.
- Do not cite the 2025 Bado manuscript as a solution. Its claimed uniform lower-bound step is not established, and the author's later [2026 note](https://www.researchgate.net/publication/405215338_FOURIER_RIGIDITY_AND_MODULAR_STRUCTURE_OF_SUM-DISTINCT_SETS) explicitly separates what remains needed for the conjectural bound.

The conjecture is not the stronger Conway--Guy exact-value conjecture \(F(2^k)=k+2\) for large \(k\), nor the real 1-separated variant, nor the modular problem.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove, with an absolute explicit or non-explicit constant c>0, that every positive-integer n-element set A with pairwise distinct subset sums satisfies max(A)>=c·2^n. The proof must make c independent of n and must establish the assertion for all sufficiently large n (or all n after a finite adjustment).

**Negative obligation.** Construct and rigorously verify a sequence of positive-integer sum-distinct sets A_j with |A_j|→∞ and max(A_j)/2^{|A_j|}→0. This is equivalent to showing that no absolute c>0 can satisfy the asserted lower bound.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution must provide a complete proof of an absolute \(c>0\) such that \(\max A\ge c2^{|A|}\) for every sum-distinct finite set \(A\subset\mathbb Z_{>0}\). It must state exactly where uniformity in \(A\) and \(|A|\) enters.

A negative resolution must provide an explicit or rigorously proved infinite family \(A_j\) of sum-distinct sets with \(|A_j|\to\infty\) and \(\max(A_j)=o(2^{|A_j|})\), together with a full proof that every subset-sum collision is excluded.

## What does not count as a solution

- Reobtaining the DFX/Steinerberger \(2^n/\sqrt n\) scale or improving only its constant.
- A theorem for a special family, a real-separated model, a modular model, or random instances without a proved reduction to all integer sum-distinct sets.
- Finite exact values, finite computer searches, or numerical evidence for a conjectured constant.
- An estimate with a constant depending on \(n\), \(A\), or a parameter tending to infinity.
- A proof sketch that turns pointwise positivity into a uniform positive infimum without compactness or a quantitative lower bound.
- A Lean encoding that leaves `sorry`, introduces an axiom equivalent to the target, or formalizes a weakened statement.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Verify the exact quantifier order: \(\exists c>0\ \forall n,N,A\), with \(c\) absolute.
2. Verify that all subset pairs are covered, including the empty subset and pairs of different cardinalities.
3. In a signed-sum formulation, prove the exact equivalence between a collision and a nontrivial \(\{-1,0,1\}\)-relation.
4. In any probabilistic proof, retain lattice spacing, parity, normalization, and all error terms.
5. In any Fourier or circle-method proof, specify arc ranges, overlap/disjointness, minor-arc control, and uniform dependence on \(A\) and \(n\).
6. In any compactness, infimum, or limiting argument, prove the needed uniform quantitative step rather than inferring it from positivity for each individual set.
7. In any computational contribution, require a precise lemma, hypotheses, machine-checkable certificate format, and a finite stopping condition before running it.

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
