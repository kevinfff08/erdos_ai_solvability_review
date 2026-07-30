# Erdős Problem 103 — research prompt

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For every integer \(n\ge 2\), define
\[
D(n)=\inf\{\operatorname{diam}(A):A\subset\mathbb R^2,\ |A|=n,\ \|x-y\|\ge1\text{ for all distinct }x,y\in A\},
\]
where \(\operatorname{diam}(A)=\max_{x,y\in A}\|x-y\|\).  Let \(\mathcal M_n\) be the family of sets attaining \(D(n)\).  Two members are equivalent precisely when a Euclidean isometry of \(\mathbb R^2\), including a reflection, maps one to the other.  Put
\[
h(n)=|\mathcal M_n/\operatorname{Isom}(\mathbb R^2)|.
\]
Use an explicit extended-cardinal convention if it becomes relevant.

Canonical target: prove or disprove
\[
\forall K\in\mathbb N\ \exists N\in\mathbb N\ \forall n\ge N,\qquad h(n)\ge K.
\]
This is a question about exact global diameter minimizers under the weak separation constraint \(\|x-y\|\ge1\), not about near minimizers, a prescribed lattice, or packings in a preselected container.

## Frozen mathematical background

- Erdős posed the problem in 1994: [Erdős, *Some problems in number theory, combinatorics and combinatorial geometry*](https://eudml.org/doc/232764), *Mathematica Pannonica* 5(2), 261–269. The public PDF is [here](https://mathematica-pannonica.ttk.pte.hu/articles/mp05-2/mp05-2-261-269.pdf).
- Even the eventual inequality \(h(n)\ge2\) is not part of the frozen known results.
- Bezdek and Fodor, [*Minimal Diameter of Certain Sets in the Plane*](https://doi.org/10.1006/jcta.1998.2889), *J. Combin. Theory Ser. A* 85 (1999), 105–111, study \(D(n)\). Its abstract reports exact small-\(n\) information through \(D(8)\), but it does not establish \(h(n)\to\infty\).
- The companion [Problem #99](https://www.erdosproblems.com/latex/99) concerns unit equilateral triangles in the same class of minimizers. Its triangular-lattice asymptotic discussion is contextual background only; it is neither a theorem about \(h(n)\) nor permission to restrict the target to lattice configurations.

Separate every theorem proved from any heuristic or conjecture. Do not infer multiplicity of exact minimizers from asymptotic packing density alone.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete affirmative resolution is a proof that for every K in N there exists N_K such that, for every integer n >= N_K, the quotient M_n / Isom(R^2) contains at least K distinct classes.

**Negative obligation.** A complete negative resolution is a proof of the logical negation: there exists K in N such that for every N there is an n >= N with h(n) < K. A proof that h(n) is globally bounded is sufficient but stronger than necessary.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a complete proof that for every \(K\) there is \(N\) such that all \(n\ge N\) satisfy \(h(n)\ge K\).

A negative resolution is a proof of the exact negation: there is a fixed \(K\) such that for arbitrarily large \(n\), \(h(n)<K\). A uniform bound on \(h(n)\) is sufficient but is stronger than the logical negation.

## What does not count as a solution

- A table of \(D(n)\) or \(h(n)\) at finitely many \(n\).
- A numerical optimizer output, a local minimum, or a near-optimal configuration without a rigorous global certificate.
- Distinct labelled coordinate lists that are congruent after relabelling, rotation, translation, or reflection.
- A construction that is only asymptotically optimal, rather than proved to attain \(D(n)\) exactly.
- Growth of \(h(n)\) on a subsequence only.
- Proving eventual \(h(n)\ge2\): record it as a major advance, but do not label it a resolution of \(h(n)\to\infty\).

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State and preserve the quantifiers over every sufficiently large integer \(n\).
2. For each purported minimizer, prove global equality \(\operatorname{diam}(A)=D(n)\), not merely an upper bound.
3. Audit congruence against the full Euclidean isometry group, including reflection.
4. Keep \(\|x-y\|\ge1\) and exact diameter throughout; justify every normalization.
5. If using contact graphs, prove that graph realizability, rigidity, and the claimed global optimality are all valid; a graph enumeration alone is insufficient.
6. Clearly distinguish deductions from the cited results from new lemmas.
7. For any computational claim, use exact/validated arithmetic and publish a certificate that independently checks both exhaustive coverage and every pruning inequality.

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
