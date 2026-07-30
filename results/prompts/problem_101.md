# Erdős Problem 101: four-point lines with no five collinear

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For a finite set \(P\subset\mathbb R^2\), write
\[
L_4(P)=\{\ell\text{ an affine line}:|\ell\cap P|=4\}.
\]
For \(n\in\mathbb N\), define
\[
t_4^{(5)}(n)=\max\{|L_4(P)|:P\subset\mathbb R^2,\ |P|=n,\ \text{no affine line contains five distinct points of }P\}.
\]
The target is
\[
t_4^{(5)}(n)=o(n^2)\quad(n\to\infty).
\]
Equivalently: for every \(\varepsilon>0\) there is \(N\) such that every \(n\ge N\) and every admissible \(P\) satisfy \(|L_4(P)|\le\varepsilon n^2\).

Lines are distinct geometric affine lines. Under the no-five condition, “contains four” and “contains exactly four” are equivalent, but retain the exact-four definition throughout.

## Frozen mathematical background

- Erdős stated the extremal formulation \(L(n)=o(n^2)\) in [On some metric and combinatorial geometric problems (1986)](https://citeseerx.ist.psu.edu/document?doi=a5f8148c337665cc71edfd1c47cad337c3a2e334&repid=rep1&type=pdf). This is the conjectural target, not a theorem.
- Solymosi and Stojaković proved that, for every fixed \(k>3\), there are planar \(n\)-point sets with no \(k+1\) collinear points and at least \(n^{2-c(k)/\sqrt{\log n}}\) lines containing exactly \(k\) points; see [arXiv:1107.0327](https://arxiv.org/abs/1107.0327) and the peer-reviewed version [DOI:10.1007/s00454-013-9526-9](https://doi.org/10.1007/s00454-013-9526-9). For \(k=4\), this is a theorem giving \(t_4^{(5)}(n)=n^{2-o(1)}\) as a lower bound. It does not disprove \(o(n^2)\).
- Elekes and Szabó proved a restricted positive result for sets on a fixed-degree algebraic curve; see [On Triple Lines and Cubic Curves: The Orchard Problem Revisited](https://doi.org/10.1007/s00454-023-00556-3), especially Theorem 4.3. This is a theorem under extra algebraic-curve hypotheses, not a solution of the unrestricted problem.
- A Lean statement exists in [Formal Conjectures](https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB101%C2%BB/), but its proof body is `sorry`; it fixes notation only and supplies no accepted proof.

Every new use of a result must cite a primary source and state exactly whether it is a theorem, a conjecture, a heuristic, or an unverified claim.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that for every ε>0 there is N such that every n≥N and every n-point P⊂R² with no five collinear points satisfies |{ℓ: |ℓ∩P|=4}|≤εn².

**Negative obligation.** Exhibit ε>0, infinitely many integers n, and admissible n-point sets P_n⊂R² with no five collinear points such that |{ℓ: |ℓ∩P_n|=4}|≥εn² for every n in that infinite set.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a rigorous proof that for every \(\varepsilon>0\), all sufficiently large admissible \(n\)-point sets have at most \(\varepsilon n^2\) distinct four-point lines.

A negative resolution is a rigorous construction of a fixed \(\varepsilon>0\) and admissible sets \(P_n\) for infinitely many \(n\), with \(|L_4(P_n)|\ge\varepsilon n^2\). The construction must verify real planar realizability, distinctness of points and lines, and the no-five condition.

## What does not count as a solution

- Reproducing or modestly improving a lower bound of the form \(n^{2-o(1)}\).
- Proving only \(O(n^2)\), or any upper bound whose normalized ratio is not shown to tend to zero.
- Proving the result only for points on a fixed-degree curve, lattice-like families, random sets, or another proper subclass.
- Testing finitely many \(n\), numerically optimizing configurations, or reporting a search without a finite certificate proving a stated lemma.
- Treating an informal forum post, an LLM derivation, or a Lean theorem containing `sorry`, `admit`, or an added axiom as a proof.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Write all quantifiers explicitly and prove a uniform bound over every admissible \(P\).
2. Count distinct lines exactly once; do not substitute incidences, ordered quadruples, or multiplicity-weighted counts.
3. Check every use of “exactly four” against the no-five hypothesis.
4. For any claimed counterexample, prove a fixed positive density on an infinite sequence of \(n\), not merely an exponent \(2-o(1)\).
5. Audit all geometric transformations and finite-field/projective constructions for preservation of real realizability and of the no-five condition.
6. State constants, thresholds, and dependencies. Do not conceal a degree, \(\varepsilon\), or configuration parameter that grows with \(n\).
7. Have an independent adversarial checker attempt to falsify every pivotal lemma and audit every cited theorem’s hypotheses.

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
