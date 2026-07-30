# Erdős Problem 33 — revised open target

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(\mathbb N_0=\{0,1,2,\ldots\}\), \(\mathcal S=\{n^2:n\in\mathbb N_0\}\), and \(A\subseteq\mathbb N_0\).  Say that \(A\) is an additive complement of the squares if
\[
\exists X_0\in\mathbb N_0\ \forall m\in\mathbb N_0,\quad m\ge X_0\Rightarrow\exists a\in A\ \exists n\in\mathbb N_0:\ m=a+n^2.
\]
For real \(x\ge1\), write \(A(x)=|A\cap\{1,\ldots,\lfloor x\rfloor\}|\), and define
\[
 C_*:=\inf_{A}\ \limsup_{x\to\infty}\frac{A(x)}{\sqrt{x}},
\]
where the infimum ranges over all additive complements \(A\) of \(\mathcal S\).

Resolve the revised target: determine \(C_*\) exactly.  If asserting that there is a literal “smallest possible value,” separately prove that some admissible \(A\) attains the infimum.  The historical question \(\liminf A(x)/\sqrt{x}>1\) is already solved and is not the target of this investigation.

Finite modifications preserve both normalized limits.  Thus an eventual complement may be augmented by finitely many small elements to cover every nonnegative integer, but do not confuse this optimization-level equivalence with literal equivalence of the two predicates for a fixed set.

## Frozen mathematical background

The following are accepted only with the stated scope; recheck primary sources before relying on finer constants.

- Moser proved in 1965 that every additive complement satisfies \(\liminf A(x)/\sqrt{x}>1.06\).  See https://doi.org/10.1090/pspum/008/0175874.
- Cilleruelo (1993), Habsieger (1995), and Balasubramanian--Ramana (2001) independently give the stronger universal lower bound \(\liminf A(x)/\sqrt{x}\ge4/\pi\).  Relevant primary identifiers are https://doi.org/10.1006/jnth.1993.1049 and https://doi.org/10.1006/jnth.1995.1039; a published accessible historical summary is https://comptes-rendus.academie-sciences.fr/mathematique/item/CRMATH_2020__358_8_897_0/.
- Hence \(C_*\ge4/\pi\).
- The Erdős Problems record and its discussion thread report a construction by Wouter van Doorn with \(A(N)<2\varphi^{5/2}\sqrt N\) for all \(N\), hence \(C_*\le2\varphi^{5/2}\).  The proof is an informal GitHub PDF, not a peer-reviewed theorem: https://github.com/Woett/Mathematical-shorts/blob/main/The%20smallest%20set%20such%20that%20every%20positive%20integer%20is%20the%20sum%20of%20a%20square%20and%20an%20element%20from%20this%20set.pdf.  The current database record and forum are https://www.erdosproblems.com/33 and https://www.erdosproblems.com/forum/thread/33.
- Chen--Fang and later Ding et al. study representation functions and a distinct question of Ben Green.  Ding--Sun--Wang--Xia, Discrete Mathematics 349(2), 114763 (2026), DOI https://doi.org/10.1016/j.disc.2025.114763, proves a representation-excess result.  Ding's preprint https://arxiv.org/abs/2512.15407 rules out exact-on-average complements.  Neither result by itself determines \(C_*\).

Separate every theorem proved in a cited source from a conjecture, heuristic, forum claim, or consequence you derive.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** For an explicitly identified real constant C, prove C*=C: (i) construct additive complements A_ε with limsup A_ε(x)/√x≤C+ε for every ε>0 (or one complement attaining C), and (ii) prove limsup A(x)/√x≥C for every additive complement A. If the assertion is that a smallest value is attained, also exhibit an A with limsup=C.

**Negative obligation.** For any proposed exact constant C or claimed extremal construction, decisively refute that claim by either producing an additive complement with limsup<C, or proving a universal lower bound limsup>C, respectively. A proof that C* is not attained is also decisive only for the attainment claim, not for determining C*.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

A complete affirmative resolution specifies a real constant \(C\) and proves \(C_*=C\):

1. for every \(\varepsilon>0\), construct an additive complement \(A_\varepsilon\) with \(\limsup A_\varepsilon(x)/\sqrt{x}\le C+\varepsilon\), or construct one attaining \(C\); and
2. prove \(\limsup A(x)/\sqrt{x}\ge C\) for every additive complement \(A\).

If the conclusion says that \(C\) is a minimum, include an admissible extremizer.  A negative resolution of a specific proposed value \(C\) must give either a valid complement with smaller limsup or a universal lower bound strictly larger than \(C\).  A proof of non-attainment resolves only the attainment subquestion.

## What does not count as a solution

- Reproving \(\liminf A(x)/\sqrt x\ge4/\pi\), or only answering the already-settled question \(\liminf>1\).
- A new upper construction or a new universal lower bound without matching the other side.
- A result solely about exact-on-average complements, representation multiplicities, or Ben Green's ordered \(w_n\) problem without a proved implication for \(C_*\).
- Finite verification, numerical optimization, or coverage through a bounded cutoff presented as proof of eventual coverage or a limsup statement.
- A formal declaration with `sorry`, `admit`, opaque axioms, or a changed eventual-coverage predicate without a proof that the intended optimization quantity is preserved.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

- State the eventual threshold and maintain the quantifier order for every construction and lower bound.
- Verify coverage for every sufficiently large integer, not merely a density-one set or a subsequence.
- Distinguish the number of elements of \(A\) from the number of square-plus-\(A\) representations.
- Check all endpoint and rounding conventions: \(0\in\mathcal S\), \(A(x)\) uses positive elements, and floor/ceiling errors are harmless only after proof.
- A construction bounded on selected scales must have a rigorous interpolation argument for all scales before it gives a limsup bound.
- A universal inequality must apply to arbitrary admissible infinite \(A\), with its threshold allowed to depend on \(A\).
- Audit every claimed bridge from representation-function estimates or ordered-element estimates to the limsup objective.
- Independently inspect the van Doorn construction before using it as a lemma; record whether its claimed strict all-\(N\) inequality is established.

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
