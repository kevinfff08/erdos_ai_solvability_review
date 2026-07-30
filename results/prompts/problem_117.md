# Erdős Problem 117: exact abelian covering function

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For a group \(G\), define
\[
\alpha(G)=\sup\{|S|:S\subseteq G,\;xy\ne yx\text{ for all distinct }x,y\in S\}.
\]
For \(n\in\mathbb N\), \(n\ge1\), the condition in the historical problem is \(\alpha(G)\le n\). Let
\[
\beta(G)=\min\{|\mathcal A|: \mathcal A\text{ is a finite family of abelian subgroups of }G,\;G=\bigcup_{A\in\mathcal A}A\}.
\]
Define \(h(n)\) as the least integer \(H\) such that \(\beta(G)\le H\) for every group \(G\) with \(\alpha(G)\le n\).

For this research task, the canonical target is to determine the exact extremal function \(h(n)\) for every \(n\ge1\). A complete answer must give an explicit formula or equivalent exact characterization and prove both the universal upper bound and matching examples. Asymptotic bounds and results for selected group families are background toward this target, not alternative target-selection tasks.

## Frozen mathematical background

- B. H. Neumann proved that a group has no infinite pairwise noncommuting subset if and only if its centre has finite index: [Neumann 1976](https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/problem-of-paul-erdos-on-groups/43D46201BABB2E6319B72C008DC3F42B). Thus the unrestricted-group formulation reduces to centre-by-finite groups.
- Pyber proved that, for a finite group with \(\alpha(G)\le n\), \(|G:Z(G)|\le c^n\) for an absolute \(c\): [Pyber 1987](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms/s2-35.2.287). The problem record and an accessible scan of Erdős’s 1997 chapter report exponential lower and upper bounds for \(h\), but do not state optimal bases: [record](https://www.erdosproblems.com/117), [original chapter scan](https://rexresearch1.com/ErdosMath/Combinatorics%2C%20Geometry%20and%20Probability%20A%20Tribute%20to%20Paul%20Erd%C3%B6s.pdf).
- For each representative \(g\) of a coset of \(Z(G)\), \(\langle Z(G),g\rangle\) is abelian and covers that coset. This elementary observation converts an index bound into an abelian-subgroup cover.
- Results for special families, including \(\mathrm{GL}_d(q)\), are not automatically universal extremal results: [Azad–Iranmanesh–Praeger–Spiga](https://arxiv.org/abs/1004.3402).
- Treat the 2025 work on higher noncommuting subsets as adjacent only; it does not, from its accessible abstract, settle the universal \(h(n)\) problem: [Yang–Zarrin 2025](https://doi.org/10.1017/S0004972724001370).

Do not use an attributed lower-bound theorem unless its exact statement and proof are supplied in the paper or its hypotheses are checked from the named source for an active proof step.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Give an explicit formula or equivalent exact characterization of \(h(n)\) for every \(n\ge1\), prove that every group \(G\) with \(\alpha(G)\le n\) satisfies the claimed upper bound for \(\beta(G)\), and construct matching groups for every required \(n\).

**Negative obligation.** If a proposed exact formula is false, give a rigorously verified counterexample group and replace the false candidate rather than treating that failure as completion. The extremal determination task itself is completed only by a correct exact characterization.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

A complete resolution must determine \(h(n)\) exactly for every \(n\ge1\). It must prove:

1. a universal upper bound \(\beta(G)\le h(n)\) for every group \(G\) satisfying \(\alpha(G)\le n\), including the reduction needed for infinite groups; and
2. matching examples showing that no smaller uniform value works for each \(n\).

An equivalent exact structural characterization is acceptable only if it determines the same integer \(h(n)\) without an unresolved optimization step.

## What does not count as a solution

- Repeating that \(h(n)\) lies between unspecified exponentials.
- Solving a finite list of groups or a single family without a theorem determining the universal extremal function.
- Giving a cover by cosets, arbitrary subsets, or nonabelian subgroups.
- Confusing \(\alpha(G)\), \(\beta(G)\), \(|G:Z(G)|\), maximal-by-inclusion sets, and maximum-cardinality sets.
- Suppressing the infinite-group quantifier without invoking and checking the Neumann reduction.
- Claiming that a better numerical bound is “best possible” without a matching obstruction under the same normalization.
- Treating an informal post, search snippet, computation, or inaccessible citation as proof.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Restate all definitions before each claimed theorem and check \(n\ge1\).
2. Verify every candidate lower-bound family has \(\alpha(G)\le n\), not merely a large centre quotient or a large order.
3. Verify every claimed cover contains all elements and every member is a subgroup and abelian.
4. Audit all conversions between centre index, clique size, and cover number with explicit inequalities and constants.
5. If quotient arguments are used, check that lifting preserves the property asserted; do not assume preimages of abelian quotient subgroups are abelian.
6. Separate finite-family asymptotics from the universal supremum defining \(h(n)\).
7. Have an adversarial reviewer try to falsify the result using central elements, direct products, small \(n\), and the distinction between graph colouring and clique number.

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
