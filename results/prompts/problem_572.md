# Erdős Problem 572 — fixed-length even-cycle Turán lower bound

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For a finite simple undirected graph \(H\), let \(\operatorname{ex}(n,H)\) be the maximum number of edges in a finite simple graph on exactly \(n\) vertices containing no subgraph isomorphic to \(H\). A copy need not be induced. Let \(C_m\) denote a simple cycle of length \(m\).

Canonical target: prove that, for every fixed integer \(k\ge 3\), there are constants \(c_k>0\) and \(n_0(k)\) such that

\[
\operatorname{ex}(n,C_{2k})\ge c_k n^{1+1/k}\qquad\text{for every integer }n\ge n_0(k).
\]

Equivalently, \(\operatorname{ex}(n,C_{2k})=\Omega_k(n^{1+1/k})\). Quantify \(k\) before \(n\): the constants may depend on \(k\), never on \(n\). The cases \(k=3\) and \(k=5\) are established, so the active target is every fixed \(k\ge4\) with \(k\ne5\), beginning with \(k=4\) (the \(C_8\) case).

## Frozen mathematical background

- Bondy and Simonovits proved the matching-exponent upper bound \(\operatorname{ex}(n,C_{2k})=O_k(n^{1+1/k})\): [Cycles of even length in graphs (1974)](https://doi.org/10.1016/0095-8956(74)90052-5).
- Pikhurko proved \(\operatorname{ex}(n,C_{2k})\le (k-1)n^{1+1/k}+16(k-1)n\): [A Note on the Turán Function of Even Cycles (2012)](https://doi.org/10.1090/S0002-9939-2012-11274-2).
- Benson's girth-8 and girth-12 constructions establish the required order for \(k=3\) and \(k=5\): [Minimal Regular Graphs of Girths Eight and Twelve (1966)](https://doi.org/10.4153/CJM-1966-109-8).
- General algebraic constructions yield weaker lower exponents; see Lazebnik, Ustimenko and Woldar, [Polarities and 2k-cycle-free graphs (1999)](https://doi.org/10.1016/S0012-365X(99)90107-3).
- Conlon gives a geometric interpretation of Wenger constructions and verifies the target order for \(k=2,3,5\): [Extremal Numbers of Cycles Revisited (2021 preprint)](https://arxiv.org/abs/2011.11064).
- A 2026 peer-reviewed source still states that matching lower bounds for ordinary \(\operatorname{ex}(n,C_{2k})\) are known only for \(k=2,3,5\): Byrne and Tait, [New constructions and bounds for nonabelian Sidon sets with applications to Turán-type problems](https://doi.org/10.4153/S0008414X26102314).

These are accepted theorems/background, not a prescribed method. In particular, results about rainbow, ordered, directed, hypercube, induced, or multiple-forbidden-cycle variants are not results about this target unless a complete reduction is supplied.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete affirmative resolution proves that for every fixed integer k >= 4 with k != 5, there are c_k>0 and n_0(k) such that every n >= n_0(k) admits a finite simple C_{2k}-free graph with at least c_k n^{1+1/k} edges. Together with the established k=3,5 cases, this proves the canonical statement.

**Negative obligation.** A complete negative resolution proves, for at least one fixed integer k >= 3, that ex(n,C_{2k}) is not Omega(n^{1+1/k}); equivalently, ex(n,C_{2k})/n^{1+1/k} has no eventually positive lower bound. This must be a rigorous asymptotic upper obstruction, not failure of one construction family.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution supplies a rigorous proof that, for every fixed unresolved \(k\), suitable \(c_k,n_0(k)\) exist and the stated lower bound holds for every \(n\ge n_0(k)\).

A negative resolution supplies a rigorous proof that for some fixed \(k\ge3\), \(\operatorname{ex}(n,C_{2k})\notin\Omega(n^{1+1/k})\); equivalently, the normalized ratio has no eventually positive lower bound.

## What does not count as a solution

- Reproving the known \(k=3\) or \(k=5\) cases.
- A graph that contains \(C_{2k}\), or a proof only excluding a different kind of cycle.
- A lower bound with a smaller exponent.
- A construction on special sizes without a proof covering every sufficiently large \(n\).
- A theorem about a related Turán function without a valid implication to ordinary \(C_{2k}\)-freeness.
- Numerical evidence, an exhaustive search at bounded order, or a heuristic algebraic pattern without a general certificate.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State all quantifiers, especially whether \(k\) is fixed and what each constant depends on.
2. Verify that graphs are finite, simple, undirected, and that the forbidden object is a non-induced simple \(C_{2k}\).
3. For every construction, prove the vertex count and edge count and prove the absence of \(C_{2k}\), including degenerate parameter cases.
4. If using field/geometry parameters, prove that distinct parameters give the claimed objects and that all exceptional characteristics/orders are handled.
5. If using a subsequence of orders, provide a valid extension argument to every sufficiently large \(n\) with constants preserved.
6. Audit every imported lemma against its exact forbidden-family convention.
7. Have an independent adversarial checker try to construct the forbidden cycle from every alleged local configuration.

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
