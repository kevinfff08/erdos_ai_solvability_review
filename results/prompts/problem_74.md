# Erdős Problem 74 — research prompt

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work in ZFC with simple undirected graphs.  For a finite graph \(H\), define
\[
b(H):=\min\{|D|:D\subseteq E(H)\text{ and }H-D\text{ is bipartite}\}.
\]
Thus \(b(H)\) is the minimum odd-cycle edge-transversal size.

Prove or disprove the following exact statement:

> For every function \(f:\mathbb N\to\mathbb N\) satisfying \(f(n)\to\infty\), there exists a graph \(G=G_f\) with infinite chromatic number such that \(b(H)\le f(|V(H)|)\) for every finite subgraph \(H\subseteq G\).

“Infinite chromatic number” means that \(G\) has no finite proper vertex-colouring; it does not mean that \(|V(G)|\) is uncountable, nor that \(\chi(G)=\aleph_1\). Subgraphs are arbitrary finite edge-subgraphs. It is harmless, but must be justified, to work with induced subgraphs because deleting edges cannot increase \(b\).

The quantifier order is \(\forall f\,\exists G_f\,\forall H\). No monotonicity of \(f\) is assumed.

## Frozen mathematical background

- Erdős, Hajnal, and Szemerédi introduced this family of almost-bipartite large-chromatic-graph questions: [1982 primary paper](https://users.renyi.hu/~p_erdos/1982-11.pdf).
- Rödl's 1982 paper is the source for the known near-bipartite constructions: [Nearly bipartite graphs with large chromatic number](https://doi.org/10.1007/BF02579434). The current problem record reports a graph result for every fixed linear budget \(f(n)=\epsilon n\), and a corresponding 3-uniform-hypergraph result: [current record](https://www.erdosproblems.com/74). Treat the exact theorem wording as something to inspect before relying on it.
- The residual graph problem is publicly recorded as open even for \(f(n)=\sqrt n\): [Problem 74](https://www.erdosproblems.com/74). This is background status, not a proof of openness.
- Lambie-Hanson proved a different result about the rate at which chromatic numbers of finite subgraphs can grow: [arXiv:1902.08177](https://arxiv.org/abs/1902.08177), published in [Advances in Mathematics 369 (2020)](https://doi.org/10.1016/j.aim.2020.107176). It controls finite-subgraph chromatic number, not \(b(H)\); do not cite it as a solution to this target.
- A statement-only Lean formalization of the intended quantifiers is available at [ErdosProblems/74.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/74.lean). It contains `sorry` and supplies no proof.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Provide a ZFC proof that for every f:N→N with f(n)→∞ there exists a simple graph G of infinite chromatic number such that b(H)≤f(|V(H)|) for every finite subgraph H⊆G, where b(H) is the minimum number of edges whose deletion makes H bipartite.

**Negative obligation.** Provide a ZFC proof of the logical negation: exhibit one f:N→N with f(n)→∞ and prove that every graph G of infinite chromatic number has a finite subgraph H with b(H)>f(|V(H)|).

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a ZFC proof that every diverging \(f\) has a witnessing \(G_f\), including a proof that \(\chi(G_f)\) is infinite and a uniform proof of \(b(H)\le f(|V(H)|)\) for every finite \(H\subseteq G_f\).

A negative resolution is a ZFC construction of one diverging \(f\) together with a proof that every infinite-chromatic graph \(G\) contains a finite \(H\subseteq G\) with \(b(H)>f(|V(H)|)\).

## What does not count as a solution

- A result only for \(f(n)=\epsilon n\), for one convenient \(f\), or for the hypergraph analogue.
- A proof for \(f(n)=\sqrt n\) presented as a proof for all diverging \(f\); it is important partial progress, not the full theorem.
- A construction with large vertex cardinality but finite chromatic number.
- A claim based only on large odd girth, slowly growing finite-subgraph chromatic number, or a bound on the number of odd cycles. Each must be converted into the required bound on \(b(H)\).
- A result for induced subgraphs without the reduction to all finite subgraphs.
- A model-dependent statement under CH, diamond, forcing axioms, or another additional assumption presented as a ZFC answer.
- Finite experiments, heuristic random constructions, or unverified AI-generated arguments without a finite lemma and complete proof.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State every quantifier and ensure the constructed graph may depend on \(f\), but not on \(H\).
2. Define the deletion set \(D\) for each finite \(H\), prove \(|D|\le f(|V(H)|)\), and prove \(H-D\) bipartite.
3. Prove infinite chromatic number independently; do not infer it from infinite order.
4. Check that the argument tolerates arbitrary, possibly nonmonotone, diverging \(f\).
5. Check small \(n\), integer rounding, and the exact interpretation of a finite subgraph.
6. Identify every external theorem used with a stable link and a precise statement; inspect the original source for Rödl-type claims.
7. Subject any candidate proof to an adversarial audit seeking a finite subgraph violating the proposed budget, a hidden extra set-theoretic axiom, or a quantifier swap.

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
