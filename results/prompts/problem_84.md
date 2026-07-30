# Erdős Problem 84 — surviving lower-bound target

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work with finite simple undirected graphs. For an integer \(n\ge 3\) and an \(n\)-vertex graph \(G\), define its cycle spectrum
\[
\mathcal C(G)=\{\ell\in\{3,\ldots,n\}:G\text{ contains a simple cycle of length }\ell\}.
\]
Let
\[
f(n)=|\{\mathcal C(G): |V(G)|=n\}|,
\]
the number of distinct spectra, not the number of labelled graphs.

Canonical target: prove
\[
\lim_{n\to\infty}\frac{f(n)}{2^{n/2}}=+\infty.
\]
Equivalently, prove that for every real \(M>0\), there is \(N\) such that every integer \(n\ge N\) satisfies \(f(n)\ge M2^{n/2}\).

This is a revised target. The separate database request \(f(n)=o(2^n)\) is already solved and is not part of the task.

## Frozen mathematical background

- Verstraëte proved the now-closed upper-bound request, in fact \(f(n)=o(2^{n-n^c})\) for an absolute \(c\ge0.1\): [publisher record](https://link.springer.com/article/10.1007/s00493-004-0043-6).
- Nenadov proved the stronger upper bound
  \[
  f(n)\le 2^{n-\Omega(\sqrt n/\log^{3/2}n)}.
  \]
  The peer-reviewed paper also states that the best known lower bound is Faudree's \(2^{n/2}\) construction: [article and PDF](https://escholarship.org/uc/item/4k75b3z7), [arXiv v2](https://arxiv.org/abs/2501.09904).
- For even \(n\), Faudree's construction takes \(A\subseteq\{n/2+1,\ldots,n\}\), starts with a Hamilton path, and adds edges from one endpoint to vertices indexed by \(A\). Its high-length spectrum recovers \(A\), yielding at least \(2^{n/2}\) distinct spectra.
- Nenadov's paper concerns upper bounds: its tools include Hamiltonian reductions, chord fingerprints, and container lemmas. These are accepted background, not a prescribed method for the lower-bound task.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Give a rigorous proof that for every M>0 there exists N such that, for every integer n>=N, at least M·2^(n/2) pairwise distinct subsets of {3,...,n} occur as C(G) for n-vertex finite simple graphs G.

**Negative obligation.** Give a rigorous proof of the logical negation: there exists a finite M>0 such that for every N there is an integer n>=N with f(n)<=M·2^(n/2). An explicit infinite sequence n_j→∞ with this uniform upper bound suffices.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a fully rigorous proof that \(f(n)/2^{n/2}\to+\infty\), with all quantifiers over every sufficiently large integer \(n\).

A negative resolution is a rigorous proof of the negation: there is a finite \(M>0\) such that for every \(N\) some \(n\ge N\) has \(f(n)\le M2^{n/2}\). An explicit infinite sequence with a uniform bound of this kind is sufficient.

## What does not count as a solution

- Reproving or strengthening an upper bound such as \(f(n)=o(2^n)\).
- Obtaining only \(f(n)\ge2^{n/2}\), \(f(n)\ge c2^{n/2}\) for fixed \(c\), or a bound on an unspecified subsequence.
- Counting labelled graphs rather than distinct sets \(\mathcal C(G)\).
- Giving a family whose parameter choices are not proved to have different complete spectra.
- Demonstrating only that selected desired lengths occur, while failing to exclude extra cycles caused by interactions among gadgets or chords.
- A finite computation without a proved reduction, exact certificate, and a stopping condition tied to a named lemma.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State the graph model and exact vertex count for every construction.
2. Prove a complete characterization of \(\mathcal C(G)\), including cycles using several added edges or several gadgets.
3. Prove injectivity from every encoding parameter to the full spectrum, not merely to a chosen subset unless the chosen subset itself is recovered from the full spectrum.
4. Establish all sufficiently large \(n\), including parity and rounding. Isolated-vertex padding changes the denominator and must be analyzed quantitatively.
5. Keep constants and thresholds uniform in \(n\); distinguish a limit from an unbounded limsup.
6. For a claimed negative resolution, verify that the bound applies to the actual \(f(n)\), not a restricted graph class.

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
