# Erdős Problem 32 — revised research target

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(\mathbb N=\{1,2,\ldots\}\), let \(P\) be the positive primes, and set \(A(x)=|A\cap[1,x]|\) for \(A\subseteq\mathbb N\).  Call \(A\) an additive complement to \(P\) if
\[
\exists n_0\ \forall n\ge n_0\ \exists p\in P,\ a\in A:\quad n=p+a.
\]

Investigate the following surviving targets, keeping them separate.

- Q1: Does there exist one fixed additive complement \(A\) with \(A(x)=o((\log x)^2)\)?
- Q2: More strongly, does there exist one fixed additive complement \(A\) with \(A(x)=O(\log x)\)?

Q2 implies Q1.  The historical question whether every such \(A\) has \(\liminf A(x)/\log x>1\) is not an open target: it is implied by Ruzsa's stronger theorem \(\liminf A(x)/\log x\ge e^\gamma\).

## Frozen mathematical background

- Erdős proved that a fixed additive complement exists with \(A(x)=O((\log x)^2)\): [primary paper](https://users.renyi.hu/~p_erdos/1954-09.pdf).
- Kolountzakis obtained an almost complement of size \(O(\log x\log\log x)\), where an exceptional set of density zero is allowed: [paper](https://matwbn.icm.edu.pl/ksiazki/aa/aa77/aa7711.pdf).
- Ruzsa proved that for every \(\omega(x)\to\infty\), a density-one complement with \(A(x)=O(\omega(x)\log x)\) exists, and proved the lower bound \(\liminf A(x)/\log x\ge e^\gamma\) under a condition implied by eventual full coverage: [paper](https://matwbn.icm.edu.pl/ksiazki/aa/aa86/aa8638.pdf).
- Dai and Pan's peer-reviewed 2014 paper explicitly distinguishes these results and states that full coverage with \(O(\log x)\) was not known: [journal record and open paper](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/en/publishing-house/journals-and-series/acta-arithmetica/all/162/3/83028/the-additive-complements-of-primes-and-goldbach-s-problem).

Treat these as theorems only to the extent their original proofs are checked.  The conjectural status of Q1/Q2 is not itself a theorem.  Do not treat metadata saying that a statement was formalized as a formal proof unless a reproducible artifact and exact theorem are obtained.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** For Q1: exhibit one fixed A⊆N and prove both A(x)=o((log x)^2) and ∃n0∀n≥n0, n∈P+A. For the stronger Q2: prove the same coverage and A(x)=O(log x). A proof of Q2 is an affirmative resolution of Q1 as well. The historical third question is already affirmatively resolved by proving the universal bound liminf A(x)/log x≥e^γ>1.

**Negative obligation.** For Q1: prove that every A⊆N with P+A containing all sufficiently large integers fails A(x)=o((log x)^2); equivalently, prove a lower obstruction incompatible with little-o. Such a theorem also rules out Q2. For Q2 alone, prove that no fixed A with eventual P+A coverage has A(x)=O(log x), while recognizing that this would leave Q1 potentially open.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

A complete affirmative resolution of Q1 supplies a single fixed \(A\), a proof of eventual pointwise coverage \(P+A\), and a proof that \(A(x)=o((\log x)^2)\) for all sufficiently large real/integer \(x\).  A complete affirmative resolution of Q2 supplies the same coverage and a global eventual \(O(\log x)\) bound.

A complete negative resolution of Q1 proves that every eventual additive complement fails the little-o bound.  A complete negative resolution of Q2 proves that every eventual additive complement fails \(O(\log x)\); it may still leave Q1 open.  A proof of Q2 resolves both Q1 and Q2 affirmatively; a negative result for Q1 resolves both negatively.

## What does not count as a solution

- Density-one, lower-density-one, or “almost all integers” coverage.
- A set depending on the cutoff, an integer \(n\), a probability outcome not shown to work simultaneously, or a finite computation.
- A representation \(n=p+a_1+a_2\) with two elements of a sparse set.
- A bound established only on a subsequence of \(x\), or a per-block estimate without a bound for the cumulative set.
- Reproving Erdős's \(O((\log x)^2)\) construction, Ruzsa's \(e^\gamma\) lower bound, or the elementary \(\Omega(\log x)\) lower bound.
- A claimed formalization without a pinned, executable verifier that checks the exact target and dependencies.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State all quantifiers, constants, and thresholds.  In particular, \(A\) and every implied constant must be fixed independently of represented \(n\).
2. For any construction, prove coverage for every \(n\ge n_0\), not merely in expectation, in density, or in a prescribed interval.
3. Audit scale gluing: prove the union remains one fixed set and derive its full cumulative counting function.
4. Check that any use of prime-distribution estimates is uniform on the claimed intervals and that exceptional sets are not silently discarded.
5. Distinguish \(\liminf\), \(\limsup\), averaged bounds, and pointwise eventual bounds in every lower-bound argument.
6. Check parity, the role of \(2\), endpoints, and finite initial changes explicitly.
7. Require an adversarial reviewer to search for an accidental replacement of one-summand coverage by two-summand or almost-everywhere coverage.

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
