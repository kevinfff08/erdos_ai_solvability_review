# Erdős Problem 571: inverse rational Turán exponent conjecture

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For a finite simple graph \(G\), let \(\operatorname{ex}(n,G)\) be the largest number of edges in a finite simple graph on \(n\) vertices that contains no (ordinary, non-induced) subgraph isomorphic to \(G\). A rational \(\alpha\) is a Turán exponent if some finite simple bipartite \(G\) satisfies \(\operatorname{ex}(n,G)=\Theta(n^\alpha)\).

Canonical target: prove that for every \(\alpha\in\mathbb{Q}\cap(1,2)\), there is a finite simple bipartite graph \(G_\alpha\) and constants \(c,C>0\), \(n_0\), such that \(c n^\alpha\le\operatorname{ex}(n,G_\alpha)\le C n^\alpha\) for every \(n\ge n_0\). Constants and \(G_\alpha\) may depend on \(\alpha\), not on \(n\). The endpoint \(\alpha=1\) is already elementary: \(G=P_3\) gives \(\operatorname{ex}(n,P_3)=\lfloor n/2\rfloor\).

## Frozen mathematical background

- Bukh and Conlon proved the finite-family analogue: for every rational \(r\in(1,2)\), a finite graph family \(\mathcal H_r\) has \(\operatorname{ex}(n,\mathcal H_r)=\Theta(n^r)\). This is a theorem, but it does **not** yield a single forbidden graph. See <https://arxiv.org/abs/1506.06406> and the published record <https://authors.library.caltech.edu/records/fjteg-4ys50>.
- Kang, Kim, and Liu proved specified families of single-graph exponents and showed that their subdivision conjecture would imply the full rational-exponent conjecture. The implication is conditional, not a resolution: <https://arxiv.org/abs/1811.06916>.
- Verified examples of subsequent single-graph progress include Conlon--Janzer, *Rational exponents near two* (2022), <https://www.advancesincombinatorics.com/article/57310-rational-exponents-near-two>, Conlon--Janzer--Lee on subdivisions, <https://arxiv.org/abs/1903.10631>, and Jiang--Qiu, *Many Turán exponents via subdivisions* (2023), <https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/many-turan-exponents-via-subdivisions/3AF62F3C0AAEA4C1EFE0C7CC5D41CA24>.
- Recent work remains partial: a 2025 induced-family theorem is not the present non-induced single-graph target (<https://arxiv.org/abs/2506.09020>), and a 2026 feedback-vertex-number paper supplies particular further exponents rather than all rationals (<https://arxiv.org/abs/2607.07157>).

Do not assume any unquoted theorem beyond what you independently inspect and cite. Clearly label every use as a proved theorem, a conditional implication, or a conjecture.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** For every rational α∈(1,2), give an explicit finite simple bipartite graph G_α and prove constants c_α,C_α>0 and n0(α) such that c_α n^α≤ex(n,G_α)≤C_α n^α for every n≥n0(α). A uniform construction indexed by reduced fractions is acceptable only if both inequalities are proved for every index.

**Negative obligation.** Disprove the statement by exhibiting a specific rational α∈(1,2) and proving that no finite simple bipartite graph G satisfies ex(n,G)=Θ(n^α). The universal nonexistence quantifier over G must be discharged rigorously; a failure of one construction or one method is not a negative resolution.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution must provide, for every rational \(\alpha\in(1,2)\), a finite simple bipartite \(G_\alpha\) and complete proofs of both asymptotic bounds \(\operatorname{ex}(n,G_\alpha)=O(n^\alpha)\) and \(\operatorname{ex}(n,G_\alpha)=\Omega(n^\alpha)\), with all parameter restrictions discharged.

A negative resolution must specify a rational \(\alpha\in(1,2)\) and prove that **no** finite simple bipartite graph \(G\) has \(\operatorname{ex}(n,G)=\Theta(n^\alpha)\). It must prove the universal obstruction over all such \(G\), not merely defeat one construction.

## What does not count as a solution

- A construction for a finite forbidden family instead of one graph.
- An induced-forbidden result, a host-restricted result, or a multigraph/hypergraph result without a valid reduction to this target.
- Only an upper bound, only a lower bound, a logarithmic-gap estimate, or a result on a subsequence of \(n\) without a valid extension.
- Any parametrized family that does not demonstrably cover every rational in \((1,2)\).
- A proof that a conjectural subdivision principle would imply the target, unless that principle is itself proved in the required generality.
- Exhaustive small-graph computation, numerical fitting, or a database search without an asymptotic proof.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Fix the exact rational \(\alpha=a/b\) in lowest terms and state which graph is forbidden.
2. Verify that \(G_\alpha\) is finite, simple, and bipartite.
3. Audit ordinary subgraph containment versus induced containment, and the direction of every forbidden-subgraph monotonicity inequality.
4. Prove both bounds with constants independent of \(n\); state the threshold \(n_0\).
5. For rooted graphs, blow-ups, and subdivisions, verify all balance, root-identification, edge-disjointness, density, and integrality hypotheses before invoking a lemma.
6. Compare the exact exponent and parameter region with the cited literature to establish novelty.
7. Subject every proposed proof to an adversarial check that tries to construct a counterexample to each embedding/counting claim and recomputes every exponent algebraically.
8. If an argument purports to unite a forbidden family into one graph, explicitly prove why avoidance of the proposed one graph is equivalent to the relevant family avoidance; do not rely on intuition.

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
