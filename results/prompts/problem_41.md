# Erdős Problem 41: infinite B_3 sequences

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(\mathbb N_{>0}=\{1,2,\ldots\}\).  For \(A\subseteq\mathbb N_{>0}\), write
\[
A(N)=|A\cap\{1,\ldots,N\}|.
\]

Call \(A\) a \(B_3\) set if for every two sorted triples
\[
a_1\le a_2\le a_3,\qquad b_1\le b_2\le b_3,\qquad a_i,b_i\in A,
\]
we have
\[
a_1+a_2+a_3=b_1+b_2+b_3 \implies (a_1,a_2,a_3)=(b_1,b_2,b_3).
\]
Equivalently, each integer has at most one representation as a sum of three members of \(A\), up to permutation. Repetitions are allowed: \(a+a+b\) and \(3a\) are legitimate representations.

Canonical target: prove that every infinite \(B_3\) set \(A\subseteq\mathbb N_{>0}\) satisfies
\[
\liminf_{N\to\infty}\frac{A(N)}{N^{1/3}}=0.
\]
Equivalently, for each such \(A\) there are integers \(N_j\to\infty\) with \(A(N_j)=o(N_j^{1/3})\).

## Frozen mathematical background

- The \(h=2\) Sidon-set analogue is reported there as proved by Erdős.
- For every even order \(h=2k\), the analogue is proved in Martin Helm, [On \(B_{2k}\)-sequences (1993)](https://eudml.org/doc/206528). This theorem does not include \(h=3\).
- Martin Helm, [On the distribution of \(B_3\)-sequences (1996)](https://www.sciencedirect.com/science/article/pii/S0022314X96900694), proves that no \(B_3\) sequence can satisfy \(A(N)\sim\alpha N^{1/3}\) for fixed \(\alpha>0\), and gives further necessary conditions. Treat this as a theorem, but inspect the full paper before relying on any condition beyond this verified abstract-level statement. The target above remains a conjecture because positive liminf does not force such an asymptotic.
- Ethan Patrick White, [An optimal \(L^2\) autoconvolution inequality (2024)](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/an-optimal-l2-autoconvolution-inequality/8D109D51F271CC78EBDA2C99FB35612D), improves finite \(B_3[1]\) extremal constants. It is relevant background but is not a resolution of the infinite liminf target.
- The existing [Lean file for #41](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/41.lean) uses cardinality-three `Finset`s and therefore omits repeated summands; do not use it as a formalization of the canonical target without repairing the definition.

Separate all proved facts from conjectures and from deductions made during the investigation. Cite a primary paper or a formal artifact for every imported theorem.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete affirmative resolution is a rigorous proof that every infinite B_3 set A subseteq N_{>0}, where equal triple sums are identified only up to permutation and repetitions are allowed, satisfies liminf_{N->infinity} A(N)/N^{1/3}=0.

**Negative obligation.** A complete negative resolution is one explicit infinite set A subseteq N_{>0}, together with a proof of the full repeated-summand B_3 property and a proof that liminf_{N->infinity} A(N)/N^{1/3}>0.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a complete proof, for every infinite repeated-summand \(B_3\) set \(A\), that \(\liminf_{N\to\infty}A(N)/N^{1/3}=0\).

A negative resolution is an explicit infinite \(A\subseteq\mathbb N_{>0}\) with a full proof of the repeated-summand \(B_3\) property and a proof that
\[
\liminf_{N\to\infty}A(N)/N^{1/3}>0.
\]

## What does not count as a solution

- Ruling out only \(A(N)\sim\alpha N^{1/3}\), which is Helm's known partial result.
- A finite \(B_3\) construction, a numerical optimization, or finite bounds for \(R_3(N)\) without a theorem about one fixed infinite set.
- A result about \(\limsup\), upper density, average density, or a logarithmically weakened bound that does not imply the required liminf conclusion.
- Invoking an even-order theorem without proving a valid reduction for order three.
- Verifying only uniqueness for three distinct summands, or relying on the current incomplete Lean encoding.
- A claimed construction whose cross-block three-sum collisions have not been proved absent.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State and use the multiplicity-aware \(B_3\) condition exactly. Every collision check must include \(a+a+b\), \(3a\), and all other repeated-summand triples.
2. Normalize triples before comparing them, or work with multisets; permutations are trivial coincidences and only permutations.
3. Audit every asymptotic quantifier. A proof of the affirmative target needs arbitrarily large scales with ratio tending to zero; a disproof needs one fixed infinite set and a uniform eventual positive lower bound in the liminf sense.
4. For each imported result, provide a direct source link, exact theorem/lemma number or page, its hypotheses, and a short explanation of why they apply.
5. If a finite-to-infinite passage is proposed, prove nesting or cross-scale compatibility explicitly. Do not infer it from a sequence of unrelated finite extremizers.
6. If formalization is used, first prove that the encoding permits repeated summands and is equivalent to the sorted-triple definition above. No `sorry`, unchecked axiom, or distinct-elements-only substitute may certify the target.
7. Subject every claimed proof or counterexample to an adversarial independent audit focused on the six preceding checks.

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
