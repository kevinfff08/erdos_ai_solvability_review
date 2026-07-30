# Erdős Problem 114: finite-degree complement to the EHP lemniscate theorem

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For an integer \(n\ge 1\) and a monic polynomial \(p\in\mathbb C[z]\) of degree \(n\), define
\[
E_1(p):=\{z\in\mathbb C:|p(z)|\le 1\},\qquad L(p):=\mathcal H^1(\partial E_1(p))=\mathcal H^1\{z:|p(z)|=1\}.
\]
Here \(\mathcal H^1\) is one-dimensional Hausdorff measure: treat a singular or self-intersecting lemniscate as a set, not as separately parametrized branches counted with multiplicity.

The Erdős--Herzog--Piranian (EHP) inequality is
\[
L(p)\le L(p_0),\qquad p_0(z)=z^n-1,
\]
for every monic \(p\) of degree \(n\). The benchmark is
\[
L(p_0)=2^{1/n}B\!\left(\tfrac12,\tfrac1{2n}\right).
\]

The current target is the residual finite-degree problem: rigorously identify an explicit threshold \(N_0\) justified by Tao's theorem, then prove the EHP inequality for every remaining \(3\le n<N_0\), or find a rigorously certified counterexample in that range. The original inequality does not require uniqueness. A stronger equality classification is separate.

## Frozen mathematical background

- Eremenko and Hayman proved the \(n=2\) case and established an extremal reduction: a maximizing monic polynomial exists and may be taken with connected lemniscate containing all critical points. See [On the length of lemniscates](https://arxiv.org/abs/0805.2295) (published in *Michigan Mathematical Journal* 46 (1999), 409--415).
- Fryntov and Nazarov proved local maximality of \(z^n-1\) and an asymptotically sharp upper bound. See [arXiv:0808.0717](https://arxiv.org/abs/0808.0717) and the 2009 AMS publication.
- Tao's [arXiv:2512.12455](https://arxiv.org/abs/2512.12455), Theorem 1.1(iv), proves that for all sufficiently large \(n\), \(L(p)\le L(p_0)\), with equality only for \(p(z)=(z-a)^n-e^{i\theta}\). Its constants are stated to be effectively computable, but the paper does not optimize or prominently state a numerical threshold. Treat this as an accepted theorem only after checking the cited preprint directly.
- Claims on the [Erdős Problems forum thread](https://www.erdosproblems.com/forum/thread/114) about degrees \(3\) through \(14\), and a claimed cubic manuscript, are unreviewed leads, not accepted background. In particular, a previously reported degree-13 certificate bug requires adversarial re-audit.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Establish, with a rigorous proof, that L(p)<=L(z^n-1) for every monic p of every remaining degree 3<=n<N0, where N0 is an explicit threshold legitimately extracted from Tao's theorem; combine this with n=1, n=2, and Tao's n>=N0 theorem. A proof for an individual fixed remaining n is an affirmative resolution only of that fixed-degree subproblem.

**Negative obligation.** Exhibit a specific integer n in the unresolved finite range and a specific monic polynomial p of degree n, together with a rigorous arclength computation or certificate proving L(p)>L(z^n-1). This disproves the original global EHP inequality.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution of the original problem requires a rigorous proof that \(L(p)\le L(z^n-1)\) for every remaining degree below a valid explicit \(N_0\), combined with the established \(n=1,2\) cases and Tao's \(n\ge N_0\) theorem.

A negative resolution requires one explicit integer \(n\) not already covered by Tao's theorem, one explicit monic \(p\) of degree \(n\), and a rigorous derivation or independently checkable certificate of
\[
L(p)>L(z^n-1).
\]

For a fixed degree \(n\), an affirmative subresolution proves the inequality for every monic polynomial of that degree, with all normalization and boundary cases included.

## What does not count as a solution

- A plot, numerical optimizer, floating-point integral, random search, or a list of plausible maximizers.
- An asymptotic estimate such as \(2n+O(1)\), even with an explicit constant, unless it proves the exact benchmark inequality in every residual degree.
- Local maximality around \(z^n-1\).
- A computation over an asserted parameter box without a proved reduction from all monic polynomials, certified outward rounding, and a complete coverage proof.
- A finite collection of checked degrees without a justified \(N_0\) and coverage of every degree below it.
- A nonstandard equality case as a purported counterexample to the EHP inequality. It matters only for a separately stated uniqueness claim.
- Reliance on an unreviewed forum post, Zenodo upload, or code repository without independently checking its mathematical reduction and its trusted computing base.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State exactly whether every length is \(\mathcal H^1\) of the level set and handle singular critical values without branch multiplicity errors.
2. Preserve monicity under translations and rotations. Record the symmetry orbit precisely as \((z-a)^n-e^{i\theta}\).
3. If invoking Tao, trace each constant needed for \(N_0\) to a stated lemma and prove that the resulting numerical threshold satisfies every prerequisite.
4. If reducing to extremizers, prove existence/compactness and invoke the Eremenko--Hayman reduction with all its hypotheses; do not assume a generic smooth lemniscate.
5. If using a fixed-degree analytic reduction, prove each equivalence, including degenerate critical-point configurations and endpoints of the normalized parameter domain.
6. If using certified computation, first prove a compact normalized domain and a rigorous enclosure of the arclength functional. Use directed/outward interval rounding; prove all boxes are covered; log split rules and termination; and run an independent checker that does not share the principal implementation's critical logic.
7. Distinguish \(<\), \(\le\), and equality exactly. An equality possibility cannot be discarded via floating-point comparison.

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
