# Erdős Problem 14 — audited revised target

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work in the positive integers \(\mathbb N=\{1,2,\ldots\}\).  For \(A\subseteq\mathbb N\) and \(n\in\mathbb N\), define the **unordered, repetition-allowed** representation function
\[
r_A(n)=\#\{(a,b)\in A^2:a\le b,\ a+b=n\}.
\]
Set
\[
B_A=\{n\in\mathbb N:r_A(n)=1\},\qquad
U_A(N)=|[1,N]\setminus B_A|.
\]
Thus \(U_A(N)\) counts both missing sums (\(r_A(n)=0\)) and sums with at least two unordered representations (\(r_A(n)\ge2\)).

Investigate the following two independent targets, and keep their statuses separate.

- **Q1:** For every \(A\subseteq\mathbb N\) and every \(\varepsilon>0\), prove or disprove that there are \(c=c(A,\varepsilon)>0\) and \(N_0=N_0(A,\varepsilon)\) such that \(U_A(N)\ge cN^{1/2-\varepsilon}\) for every \(N\ge N_0\).
- **Q2:** Prove or disprove the existence of one \(A\subseteq\mathbb N\) with \(U_A(N)=o(\sqrt N)\).

Before substantive work, record whether the problem owner instead intends Q1 with constants uniform in \(A\). Do not silently change between these variants.

## Frozen mathematical background

- The current Erdős Problems record states Q1/Q2 and reports an Erdős construction with \(U_A(N)\ll_\varepsilon N^{1/2+\varepsilon}\), plus a lower estimate along infinitely many \(N\). Treat these as historical claims requiring source verification before using their detailed parameters: <https://www.erdosproblems.com/history/14>.
- Erdős and Freud, *On sums of a Sidon-sequence*, J. Number Theory 38(2) (1991), 196–205, DOI: <https://doi.org/10.1016/0022-314X(91)90083-N>, is the primary finite-Sidon reference. The current database reports a finite \(2^{3/2}\sqrt N\) construction, but verify the original theorem before invoking that constant.
- O'Bryant's annotated bibliography describes the finite Sidon/quasi-Sidon context: <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS11/pdf/>.
- A 2026 LeanGenius artifact fixes the \(a\le b\) convention and formalizes elementary definitions, but lists the main historical estimates as axioms; it is not a formal solution: <https://leangenius.org/proof/erdos-14-unique-sums>.

Do not infer \(\neg\mathrm{Q2}\) from Q1. A function such as \(\sqrt N/\log N\) illustrates why a lower bound \(\gg_\varepsilon N^{1/2-\varepsilon}\) for every fixed \(\varepsilon\) is compatible with \(o(\sqrt N)\).

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** For Q1, a complete affirmative resolution is a proof, under the declared unordered convention and declared A-dependence of constants, that ∀A⊆ℕ ∀ε>0 ∃c>0 ∃N_0 ∀N≥N_0: U_A(N)≥cN^(1/2−ε). For Q2, a complete affirmative resolution is one explicitly defined A⊆ℕ together with a proof that lim_{N→∞}U_A(N)/√N=0.

**Negative obligation.** For Q1, a complete negative resolution is an explicit A⊆ℕ and ε>0 for which U_A(N)/N^(1/2−ε) has liminf 0 (equivalently, no eventual positive lower constant exists). For Q2, a complete negative resolution is a proof that every A⊆ℕ has limsup or an eventual lower obstruction incompatible with U_A(N)=o(√N). The two questions must be audited independently because these outcomes are not logical complements across Q1 and Q2.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

A complete resolution must identify which question it resolves.

- A **yes** to Q1 is a proof with the exact quantifiers \(\forall A\,\forall\varepsilon\,\exists c,N_0\,\forall N\ge N_0\).
- A **no** to Q1 is an explicit \(A\) and \(\varepsilon>0\) for which no eventual positive lower constant exists.
- A **yes** to Q2 is one explicit infinite \(A\), with a proof that \(U_A(N)/\sqrt N\to0\) for all sufficiently large \(N\), not merely on a subsequence.
- A **no** to Q2 is a universal theorem excluding \(U_A(N)=o(\sqrt N)\) for every \(A\).

## What does not count as a solution

- Treating ordered pairs \((a,b)\) and \((b,a)\) as distinct representations.
- Counting only multiply represented sums and omitting missing sums.
- A finite set \(A_N\) chosen separately for each \(N\).
- An \(N^{1/2+\varepsilon}\) upper bound, an infinite-subsequence lower bound, or numerical data alone.
- A proof of Q1 claimed to settle Q2 without a genuine \(\Omega(\sqrt N)\)-type consequence.
- A citation to a database, forum, search snippet, or an axiomatized formal file in place of a proof.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State the representation convention before every use of a representation count; include the diagonal \(a=b\).
2. Audit the dependence of every \(O\), \(o\), \(\ll\), \(\gg\), threshold, and construction parameter on \(A\), \(\varepsilon\), and scale.
3. Separate the counts \(r_A(n)=0\), \(r_A(n)=1\), and \(r_A(n)\ge2\) before applying a counting argument.
4. For an infinite construction, prove compatibility of all stages and control all large \(N\), including gaps between construction scales.
5. For a lower bound, test sparse, dense, periodic, Sidon, and finite-prefix perturbation regimes.
6. Independently verify every imported historical theorem from the primary paper or an equally authoritative accessible source.

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
