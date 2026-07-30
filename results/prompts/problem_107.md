# Erdős Problem 107: exact Erdős-Szekeres convex-polygon threshold

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For every integer \(n\ge 3\), let \(ES(n)\) be the least positive integer \(N\) such that every finite set \(P\subset\mathbb R^2\) with \(|P|=N\) and no three collinear contains a subset \(Q\subseteq P\) of size \(n\) in convex position. Here “in convex position” means that every member of \(Q\) is a vertex of \(\operatorname{conv}(Q)\); equivalently, \(Q\) is the vertex set of a convex \(n\)-gon.

Canonical target: prove
\[
ES(n)=2^{n-2}+1\qquad\text{for every integer }n\ge3.
\]

This is not an empty-polygon problem: points of \(P\setminus Q\) may lie inside the convex polygon. The lower bound \(ES(n)\ge2^{n-2}+1\) is accepted background. Thus a proof needs the corresponding universal upper bound. A disproof needs one \(n\ge7\) and a general-position set of exactly \(2^{n-2}+1\) points with no \(n\) points in convex position.

## Frozen mathematical background

- Erdős and Szekeres established the classical cap-cup upper bound \(ES(n)\le {2n-4\choose n-2}+1\), and their later construction gives \(ES(n)\ge2^{n-2}+1\). A precise recent exposition is Baek–Balko, [SoCG 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.13).
- The exact result is known through \(n=6\): in particular, Szekeres and Peters proved \(ES(6)=17\) by a reproducible computer proof; see [the ANZIAM paper](https://www.cambridge.org/core/journals/anziam-journal/article/computer-solution-to-the-17point-erdosszekeres-problem/0EC7876789232266D60439A4C00D86D9). The first open concrete case is \(ES(7)=33\).
- Suk proved \(ES(n)=2^{n+o(n)}\); see [arXiv:1604.08657](https://arxiv.org/abs/1604.08657). Holmsen, Mojarrad, Pach, and Tardos improved the general upper-bound error to \(ES(n)\le2^{n+O(\sqrt{n\log n})}\); see [arXiv:1710.11415](https://arxiv.org/abs/1710.11415) and the precise review in [Baek–Balko](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.13).
- Baek–Balko prove a different theorem: the split-polygon threshold is exactly \(2^{n-2}+1\), and the original conjecture holds for decomposable point sets. These are useful constraints, not proofs of the canonical target. Their 2026 journal version also discusses failed abstract generalizations: [JCTA article](https://www.sciencedirect.com/science/article/pii/S0097316526000385).
- Dumitru’s [2025 preprint](https://arxiv.org/abs/2512.24061) gives a SAT encoding and UNSAT certificates only for certain anchored subfamilies of the 33-point case. Treat it as partial computational background, not as a resolution.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Provide a complete proof that for every integer n >= 3, every general-position set P subset R^2 with |P| = 2^(n-2)+1 has an n-element subset in convex position. Together with the established lower-bound construction, this proves ES(n)=2^(n-2)+1 for all n >= 3.

**Negative obligation.** Provide one explicit integer n >= 7 and a finite general-position P subset R^2 with |P| = 2^(n-2)+1 such that every n-element subset of P has a point in the convex hull of the other n-1 points. This proves ES(n)>2^(n-2)+1 and disproves the universal conjecture.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a fully detailed proof that every general-position set of \(2^{n-2}+1\) planar points contains \(n\) points in convex position for every \(n\ge3\). It must explicitly invoke or reprove the known lower bound to conclude equality.

A negative resolution is an explicit \(n\ge7\) and a fully verified general-position planar configuration of \(2^{n-2}+1\) points with no convex \(n\)-subset. Exact coordinates or a rigorously realizable order-type certificate must be supplied, together with a complete verification of avoidance.

## What does not count as a solution

- An asymptotic improvement, including \(2^{n+o(n)}\), does not establish the exact formula.
- A proof only for caps, cups, split polygons, decomposable sets, pseudoline arrangements, weak/strong abstract polygons, or a non-realizable oriented structure does not solve the planar problem unless a proved reduction covers all planar point sets.
- Resolving \(ES(7)\), or any finite collection of values, is substantial progress but not a proof of the all-\(n\) target.
- A purported counterexample with only \(2^{n-2}\) points merely recovers the known lower bound.
- Solver output, a claimed exhaustive search, or a numerical picture without an exact encoding, coverage proof, independently checkable certificate, and geometric-realizability audit does not count.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Check every quantifier: \(n\ge3\), finite \(P\), \(|P|=2^{n-2}+1\), and no three collinear.
2. Check the intended predicate: every selected point must be a vertex of its selected subset’s convex hull; do not impose or assume emptiness.
3. Check every reduction from geometry to cups/caps, order types, allowable sequences, oriented matroids, or SAT. State both directions of the reduction and all hypotheses.
4. Check lower-bound direction separately from upper-bound direction. An avoiding set of size one below the threshold cannot disprove the conjecture.
5. For any perturbation, prove it preserves all orientation signs and the convexity/nonconvexity predicates used.
6. For any computational certificate, preserve the exact CNF and assumptions; audit symmetry breaking, exhaustive coverage, solver proof format, independent checking, and—where needed—realizability in \(\mathbb R^2\).
7. Require an adversarial reviewer to try to construct the omitted case in each structural lemma and to compare the claimed theorem precisely with the Baek–Balko restricted results.

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
