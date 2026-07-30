# Erdős Problem 568 — Ramsey size-linearity from tree and clique tests

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(G\) be a fixed finite graph. For finite graphs \(A,B\), \(R(A,B)\) is the least \(N\) such that every red-blue colouring of \(E(K_N)\) contains a red, non-induced copy of \(A\) or a blue, non-induced copy of \(B\).

The notation \(O_G(\cdot)\) means that the implied constant depends only on the fixed graph \(G\), not on \(n\), \(T\), \(H\), \(e(H)\), \(v(H)\), maximum degree, or a chosen decomposition.

Canonical target. Assume that:

1. \(R(G,T)\le C_T(G)|T|\) for one constant \(C_T(G)\), for every finite tree \(T\); and
2. \(R(G,K_n)\le C_K(G)n^2\) for one constant \(C_K(G)\), for every \(n\ge2\).

Prove or disprove that there is a constant \(C(G)\) such that
\[
R(G,H)\le C(G)e(H)
\]
for every finite graph \(H\) with no isolated vertices and \(e(H)\ge1\). This property is called *Ramsey size-linearity*.

Do not remove the no-isolated-vertices condition. Do not replace the target by an induced Ramsey problem, a size-Ramsey-number problem, or a result whose constant depends on \(H\).

## Frozen mathematical background

- Erdős, Faudree, Rousseau and Schelp, [*Ramsey Size Linear Graphs*](https://doi.org/10.1017/S096354830000078X), Combinatorics, Probability and Computing 2 (1993), 389–399, defines Ramsey size-linearity and proves, among other results, sufficient size-linear and non-size-linear edge-density regimes.
- Bradač, Gishboliner and Sudakov, [*On Ramsey size-linear graphs and related questions*](https://arxiv.org/abs/2202.10388), SIAM J. Discrete Math. 38 (2024), proves special cases including Ramsey size-linearity of every \(K_4\)-subdivision with at least six vertices, and a bipartite-target result for \(K_4^*\). These are theorems for special fixed graphs, not a proof of the canonical implication.
- Wigderson, [*Infinitely many minimally non-Ramsey size-linear graphs*](https://arxiv.org/abs/2409.05931), European J. Combin. 128 (2025), proves a different structural existence result and restates the standard definition.
- Recent cycle results, including [Cambie–Freschi–Morawski–Petrova–Pokrovskiy (2026)](https://arxiv.org/abs/2601.10238) and [Hng–Ji–Lamaison (2026)](https://arxiv.org/abs/2603.25453), concern particular fixed graphs and do not resolve this implication.

Treat all statements above strictly according to their cited source. Verify any stronger lemma from the full paper before relying on it.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that for every fixed finite G satisfying the two stated uniform hypotheses, one constant C(G) satisfies R(G,H)<=C(G)e(H) for every finite isolate-free H with e(H)>=1.

**Negative obligation.** Exhibit one fixed finite graph G; rigorously prove both uniform hypotheses for that same G; and give isolate-free graphs H_i with R(G,H_i)/e(H_i) unbounded.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a proof that every fixed \(G\) satisfying both hypotheses has one constant \(C(G)\) that works for every finite isolate-free \(H\).

A negative resolution is a specific fixed graph \(G\), rigorous proofs of both hypotheses for that exact \(G\), and a sequence \(H_i\) of isolate-free finite graphs with
\[
\frac{R(G,H_i)}{e(H_i)}\longrightarrow\infty.
\]

Either resolution must be self-contained enough to audit every quantifier and implied constant, while citing external theorems precisely by theorem/proposition number and direct URL.

## What does not count as a solution

- A proof only for trees, cliques, connected targets, bipartite targets, bounded-degree targets, cycles, or another subclass of \(H\).
- A result \(O_G(e(H)\log e(H))\), \(O_G(e(H)^{1+\varepsilon})\), or any superlinear bound.
- A bound with a hidden constant depending on \(H\), \(e(H)\), \(v(H)\), \(\Delta(H)\), or an auxiliary decomposition.
- Showing only one hypothesis for a prospective counterexample \(G\).
- A computation, finite table, heuristic, or literature citation with no proof of the required uniform asymptotic claim.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State the red/blue orientation and non-induced-copy convention before applying a Ramsey theorem.
2. At every \(O\), \(\ll\), or constant declaration, list its permitted dependencies. The final constant may depend only on \(G\).
3. Check the tree hypothesis uniformly over all trees and all orders, not separately tree by tree.
4. Preserve the no-isolated-vertices condition. If a reduction adds isolates, quantify its effect on the Ramsey number rather than silently discarding it.
5. For an affirmative proof, isolate and audit the exact transition from the two test families (trees and cliques) to arbitrary \(H\).
6. For a negative proof, independently audit both hypotheses for the same fixed \(G\), then prove the unbounded ratio for the stated \(H_i\).
7. Separate sourced facts, transparent deductions, conjectural ideas, and failed approaches.

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
