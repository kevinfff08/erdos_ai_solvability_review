# Erdős Problem 40 — density threshold for unbounded additive representations

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work in \(\mathbb N=\{1,2,\ldots\}\).  For \(A\subseteq\mathbb N\), write
\[
 A(N):=|A\cap\{1,\ldots,N\}|,\qquad
 r_A(n):=(1_A*1_A)(n)=|\{(a,b)\in A^2:a+b=n\}|.
\]
Thus \(r_A\) counts **ordered** representations.  For an eventually positive function \(g:\mathbb N\to(0,\infty)\), define \(P(g)\) to mean
\[
 \forall A\subseteq\mathbb N,\quad
 \bigl[(\exists c>0,\exists N_0,\forall N\ge N_0,\ A(N)\ge c\sqrt N/g(N))\bigr]
 \Longrightarrow \limsup_{n\to\infty}r_A(n)=\infty.
\]

The target is to characterize
\[
 \mathcal G_*:=\{g:\mathbb N\to(0,\infty):g(N)\to\infty\text{ and }P(g)\}.
\]
A complete answer must say exactly which functions belong to \(\mathcal G_*\), under a stated equivalence or comparison relation if one is used.  Do not silently assume monotonicity; if it is imposed, prove a reduction from the unrestricted formulation or label the result as conditional.

Source statement: [Erdős Problems #40](https://www.erdosproblems.com/40).  The formal target is encoded in [FormalConjectures/ErdosProblems/40.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/40.lean); that file contains an unresolved `sorry`, not a proof.

## Frozen mathematical background

- The classical Erdős–Turán conjecture says that an asymptotic order-2 additive basis \(A\) has unbounded \(r_A\).  The formal file verifies that proving \(P(g)\) for any diverging \(g\) implies this classical conjecture.  Treat this as a checked reduction, not as a solution.
- A known negative region is essential: the Erdős–Rényi construction reported in [Erdős Problem #39](https://www.erdosproblems.com/39) gives, for every \(\varepsilon>0\), a set with \(A(N)\gg_\varepsilon N^{1/2-\varepsilon}\) and bounded \(r_A\).  Consequently \(P(N^\varepsilon)\) fails, and so does \(P(g)\) whenever \(N^\varepsilon=O(g(N))\).  Before relying on this in a formal paper, locate and cite the original construction.
- Do not confuse economical bases with bounded-representation bases.  Jain–Pham–Sawhney–Zakharov construct an explicit \(A\) with \(A+A=\mathbb N\) and \(r_A(n)=n^{o(1)}\): [arXiv:2405.08650](https://arxiv.org/abs/2405.08650).  This does not settle boundedness.
- Recent fixed-threshold results use generating functions and density of the exceptional sumset.  Li–Zhang prove results such as \(D(\mathbb N\setminus(A+A))<7/32\Rightarrow\limsup r_A>5\): [arXiv:2605.30922](https://arxiv.org/abs/2605.30922).  The hypothesis of this problem does not itself control \(A+A\), so no direct application is licensed.
- A claimed proof of the classical conjecture exists as an unevaluated OSF preprint, but it has not been accepted as a resolution: [record](https://sciety.org/articles/activity/10.31219/osf.io/mxgbu).  Treat it only as an unverified claim to audit, never as background theorem.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete affirmative classification supplies a precisely defined class C of eventually positive functions g with g(N)->infinity and proves, for every such g, P(g) iff g belongs to C. At minimum, an affirmative membership result for a named diverging g0 requires a proof that every A with A(N)>=c sqrt(N)/g0(N) eventually has unbounded ordered representation function; it must quantify uniformly over all A and all admissible constants c.

**Negative obligation.** A complete negative classification supplies the complementary rigor: for every diverging eventually positive g outside the asserted class, an A_g subseteq N and a finite C_g with A_g(N)>>sqrt(N)/g(N) and r_{A_g}(n)<=C_g for every n (or eventually every n). In particular, proving G_* is empty would be a complete negative answer; for a named g0, such an A_g0 is a decisive disproof of P(g0).

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

A complete positive resolution is a theorem giving a precisely specified class \(\mathcal C\) of all eventually positive diverging functions and proving
\[
 g\in\mathcal C\iff P(g)
\]
for every such \(g\).  It must include the handling of nonmonotone functions or an explicit proved normalization theorem.

A complete negative resolution is a proof that \(\mathcal G_*\) is empty, namely: for every eventually positive \(g\to\infty\), construct \(A_g\subseteq\mathbb N\) and \(C_g<\infty\) with
\[
 A_g(N)\gg\sqrt N/g(N)\quad\text{for all sufficiently large }N,
 \qquad r_{A_g}(n)\le C_g\quad\text{for all }n.
\]

A significant but partial result must be labelled as such.  It may prove \(P(g_0)\) for one explicit diverging \(g_0\), or disprove \(P(g_0)\) by a fully specified bounded-representation construction.  A positive instance automatically resolves the classical Erdős–Turán conjecture, so it requires correspondingly stringent checking.

## What does not count as a solution

- Proving a statement only for additive bases, positive-density sets, or sets with a sumset-density condition not implied by the displayed counting hypothesis.
- Establishing the lower bound only for infinitely many \(N\), on average, or with a constant depending on \(N\).
- Switching silently between ordered and unordered representations.
- A construction over \(\mathbb Z\) or \(\mathbb Z/m\mathbb Z\) without a proof that transfers to one-sided \(\mathbb N\).
- A finite computation, numerical experiment, heuristic, random model, or a claim that an existing preprint is correct without independently checking its proof.
- A theorem for one function \(g\) presented as the requested characterization of all \(g\).

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State exactly the domains, all quantifiers, the final positivity of \(g\), and the all-sufficiently-large-\(N\) meaning of \(\gg\).
2. Prove each comparison-direction claim.  In particular, if \(g_1=O(g_2)\), then the hypothesis for \(g_1\) is stronger; therefore \(P(g_2)\Rightarrow P(g_1)\).  Conversely, one counterexample for \(g_1\) refutes \(P(g_2)\).
3. For every counterexample, prove both the uniform counting lower bound and a single finite global bound on \(r_A(n)\), including diagonal and ordered-pair conventions.
4. For every positive proof, show why the density hypothesis alone supplies every subsequently used coverage, energy, or regularity hypothesis.
5. Audit every use of a result over \(\mathbb Z\), a finite cyclic group, or a random construction for the missing one-sided/infinite/uniform step.
6. If formalization is attempted, build against the linked Formal Conjectures definition or provide an explicit translation lemma; no `sorry`, axiom, or unproved external theorem may be concealed in the final certificate.

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
