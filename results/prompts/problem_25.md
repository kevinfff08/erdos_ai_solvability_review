# Erdős Problem 25: logarithmic density of thresholded congruence sieves

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(n_1<n_2<\cdots\) be any strictly increasing sequence of positive integers. For every \(i\), let \(a_i\pmod{n_i}\) be one residue class. Define
\[
 A=\{n\in\mathbb N:\ \forall i\ge1,\ n<n_i\ \text{or}\ n\not\equiv a_i\pmod {n_i}\}.
\]
Thus the \(i\)-th constraint is active exactly for \(n\ge n_i\), including \(n=n_i\). For each fixed \(n\), only finitely many constraints are active.

Prove or disprove the universal assertion that
\[
 \delta_{\log}(A)=\lim_{x\to\infty}\frac1{\log x}
 \sum_{\substack{n\le x\\n\in A}}\frac1n
\]
exists for every allowed \((n_i,a_i)\). Replacing \(n\le x\) by \(n<x\) is immaterial.

## Frozen mathematical background

- [Problem 486](https://www.erdosproblems.com/latex/486) is a broader residue-set problem. It records the Davenport–Erdős zero-residue result and says it generalizes Problem 25. Do not silently identify the two: 486 uses \(m>n\), while the target here activates at \(n\ge n_i\).
- Davenport and Erdős, [*On sequences of positive integers* (1936)](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/2/1/93274/on-sequences-of-positive-integers), prove the classical multiples/zero-class result. This does not settle arbitrary translated classes.
- For each finite prefix, \(A^{(k)}\) is eventually periodic, hence has a density \(\delta_k\); \(\delta_k\) decreases to some \(\delta\). The missing step is to prove that the infinite set \(A\) has logarithmic density \(\delta\), or to refute this.
- Przemyslaw Chojecki's [2026 manuscript](https://www.ulam.ai/research/erdos25.pdf) proves special cases \(\sum_i1/n_i<\infty\) and pairwise-coprime moduli, then gives a conditional quotient-sieve reduction. It explicitly does **not** prove the full statement.
- The [Lean file](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/25.lean) encodes the statement but contains `sorry`; it is not a verified proof.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove, for every allowed (n_i,a_i), that lim_{x→∞}(log x)^{-1}∑_{n≤x,n∈A}1/n exists. The proof must control the infinite tail uniformly enough to justify the limit; identifying a candidate δ=lim_k δ_k is not sufficient by itself.

**Negative obligation.** Give one explicit strictly increasing modulus sequence and residue choices for which the displayed harmonic averages do not converge, with a rigorous certificate of two subsequences X_j,Y_j→∞ whose limiting values differ (or an equally rigorous nonconvergence argument).

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a rigorous proof that the displayed logarithmic-density limit exists for every strictly increasing modulus sequence and every residue-class selection.

A negative resolution is one explicit allowed sequence together with a rigorous proof that the harmonic averages fail to converge; preferably certify two sequences \(X_j,Y_j\to\infty\) having distinct limiting values.

A claimed resolution must also state whether it treats the endpoint \(n=n_i\), all nonzero residues, and all non-coprime moduli. A theorem covering only an additional hypothesis is a partial result, not a resolution.

## What does not count as a solution

- Finite computation, finite-prefix enumeration, or observing numerical stabilization.
- Showing that every \(A^{(k)}\) is periodic.
- Establishing only natural-density failure or existence.
- Proving only the summable, pairwise-coprime, or zero-residue cases.
- Assuming a uniform quotient-sieve estimate, a tail bound, or an error summability statement without proving it.
- Treating the `sorry`-containing Lean declaration as a proof.
- Importing Problem 486 without resolving its strict-threshold endpoint difference.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

- Preserve all quantifiers: arbitrary increasing \((n_i)\), arbitrary classes \((a_i)\), and a universal conclusion.
- Use harmonic mass \(\sum 1/n\), not only counts of elements in intervals.
- Account for the active constraint at \(n=n_i\).
- If using the first-kill decomposition \(\mathbb N\setminus A=\bigsqcup_i E_i\), prove a uniform accumulated error estimate; termwise eventual periodicity is insufficient.
- If a construction claims oscillation, bound both the desired contribution and every earlier/later block on the stated cutoff subsequences.
- If a density is asserted to equal \(\lim_k\delta_k\), justify the exchange of the two limiting processes.
- Label every literature input as theorem, conditional theorem, heuristic, or informal claim, and cite its direct source.

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
