# Erdős Problem 91

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For every integer \(n\ge 2\), set
\[
D(n)=\min_{\substack{A\subset\mathbb R^2\\|A|=n}}
\left|\{\|x-y\|:x,y\in A,\ x\ne y\}\right|.
\]
An \(n\)-point set is a *global minimizer* if it determines exactly \(D(n)\) distinct nonzero Euclidean distances. Two finite point sets are *similar* if one is obtained from the other by a translation, an orthogonal map (reflections included), and a positive uniform scaling.

Resolve this target:

> Does there exist \(n_0\) such that, for every integer \(n\ge n_0\), there are two non-similar global minimizers of size \(n\) in \(\mathbb R^2\)?

Do not replace this with the historical phrase “probably many”; that phrase has no quantified completion condition.

## Frozen mathematical background

- The [official Erdős Problems data entry](https://raw.githubusercontent.com/teorth/erdosproblems/refs/heads/main/data/problems.yaml) lists #91 as open and its solution status as unformalized. Its `formalized: yes` metadata concerns a statement formalization, not a verified solution.
- The problem record reports small cases: uniqueness for \(n=3\) and \(n=5\), two non-similar examples for \(n=4\), and an Erdős-attributed statement for \(6\le n\le9\). Inspect the primary text before using the latter as a theorem.
- Z. Kovács, [A note on Erdős's mysterious remark](https://arxiv.org/abs/2412.05190) (2024 preprint) gives a computer-assisted algebraic proof of the \(n=5\) uniqueness statement. It does not settle the asymptotic problem.
- Guth and Katz, [On the Erdős distinct distances problem in the plane](https://annals.math.princeton.edu/2015/181-1/p02), *Annals of Mathematics* 181 (2015), prove \(D(n)\ge c n/\log n\). This is a bound on the number of distances, not a classification of exact minimizers.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that there exists an integer n0 such that for every integer n >= n0 there are n-point sets A_n,B_n subset R^2, each determining exactly D(n) distinct nonzero distances, and prove that no Euclidean similarity maps A_n to B_n.

**Negative obligation.** Prove that infinitely many integers n have a unique D(n)-minimizing n-point set up to the stated Euclidean-similarity convention. Such an infinite sequence contradicts the eventual-for-every-n affirmative statement.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution proves one integer \(n_0\) and, for every \(n\ge n_0\), produces or proves the existence of two non-similar \(n\)-point global minimizers. For each minimizer, establish its exact distance count and global optimality.

A negative resolution proves that infinitely many \(n\) have exactly one global minimizer up to the stated similarity convention. This is sufficient to refute the eventual-for-all-\(n\) target.

## What does not count as a solution

- Two non-similar sets with the same distance count unless that count is proved to be \(D(n)\).
- Two labelled, congruent, or scaled copies.
- A finite list of values of \(n\), or an affirmative result only on a subsequence.
- A new upper or lower bound for \(D(n)\) without a theorem about exact minimizers.
- Floating-point searches, heuristic optimizers, or informal diagrams without an exact completeness and optimality certificate.
- A claim about “many” minimizers without explicit quantifiers.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Fix the Euclidean metric, exclusion of diagonal pairs, and similarity convention at the outset.
2. For every proposed minimizer, separately prove \(D(n)\ge k\) and exhibit exactly \(k\) distances.
3. Verify the eventual quantifier: one threshold must cover every subsequent integer.
4. Prove non-similarity by an invariant or an argument valid under translations, rotations, reflections, and scaling.
5. Audit all imported theorems for exact hypotheses, parameter range, and whether they concern distinct values rather than repeated pairs.
6. If computation is used, give a finite candidate universe, exact representation, completeness proof, code/data, and independently checkable certificates.
7. Treat historical database remarks as leads until their primary proof or a complete modern proof is inspected.

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
