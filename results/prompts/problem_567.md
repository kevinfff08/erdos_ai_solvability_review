# Erdős Problem 567: Ramsey size-linearity of $Q_3$, $K_{3,3}$, and $H_5$

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For finite simple graphs $A,B$, let $r(A,B)$ be the least $N$ such that every red/blue colouring of the edges of $K_N$ contains a red (not necessarily induced) copy of $A$ or a blue copy of $B$.

Let $Q_3$ be the 3-dimensional cube graph. Let $K_{3,3}$ be the complete bipartite graph with parts of size three. Let $H_5$ be $C_5$ plus two vertex-disjoint chords; equivalently, it is $K_4$ with exactly one edge subdivided once.

For each fixed
\[
G\in\{Q_3,K_{3,3},H_5\},
\]
prove or disprove that there is a constant $C_G>0$ such that every finite simple graph $H$ with $m=e(H)\ge1$ and no isolated vertices satisfies
\[
r(G,H)\le C_Gm.
\]

This is three separate fixed-$G$ assertions. The constant may depend on $G$, but must not depend on $H$, $m$, $|V(H)|$, connectivity, or bipartiteness. The Ramsey parameter is the ordinary vertex Ramsey number $r$, not the size-Ramsey number $\hat r$.

## Frozen mathematical background

- Erdős, Faudree, Rousseau, and Schelp introduced Ramsey size-linearity and proved that $e(G)\ge2v(G)-2$ implies non-size-linearity, while every connected $G$ with $e(G)\le v(G)+1$ is size-linear: [EFRS 1993](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/ramsey-size-linear-graphs/2F50FFB56AD4E42EFA80DA5B280225A0).
- Erdős reiterated the $K_{3,3}$ case in 1995: [Erdős 1995](https://revistas.usp.br/resenhasimeusp/pt_BR/article/view/74798).
- Bradač, Gishboliner, and Sudakov proved that every subdivision of $K_4$ with at least six vertices is Ramsey size-linear. They also proved $r(H_5,H)=O(e(H))$ when the varying graph $H$ is bipartite and has no isolated vertices. Their paper explicitly does not establish that $H_5$ is Ramsey size-linear: [published version](https://epubs.siam.org/doi/10.1137/22M1481713), [open preprint](https://arxiv.org/abs/2202.10388).
- A recent result for fixed odd cycles is relevant methodology but does not settle any target here: [Hng--Ji--Lamaison, arXiv:2603.25453](https://arxiv.org/abs/2603.25453).

Do not treat the FormalConjectures entry as a proof: its three declarations contain `sorry`, and its introductory displayed formula uses a misleading $\hat r$ notation: [formal artifact](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/567.lean).

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** For each G in {Q_3,K_{3,3},H_5}, prove an explicit theorem: there is a finite constant C_G such that every finite simple graph H with e(H)=m>=1 and no isolated vertices satisfies r(G,H)<=C_G m. A proof must handle arbitrary (including non-bipartite and disconnected) H; for H_5 it must strictly extend the already known bipartite-H theorem.

**Negative obligation.** Disprove the conjunction by exhibiting at least one specified G in the set and an infinite family (H_i) of finite simple graphs without isolated vertices, with e(H_i)->infinity and r(G,H_i)/e(H_i)->infinity, together with a valid lower-bound proof. A single counterexample G and family refutes the literal three-part assertion.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution must prove, separately for every $G\in\{Q_3,K_{3,3},H_5\}$, a finite constant $C_G$ satisfying $r(G,H)\le C_Ge(H)$ for every permitted $H$.

A negative resolution must identify at least one particular target $G$ and give an infinite family $H_i$ of permitted graphs such that $e(H_i)\to\infty$ and
\[
\frac{r(G,H_i)}{e(H_i)}\to\infty.
\]
It must include a complete lower-bound proof. Such a family refutes the literal conjunction even if the other two cases remain open.

## What does not count as a solution

- Proving only $r(G,K_n)=O(n^2)$, only a bounded-degree case, only connected $H$, or only bipartite $H$.
- Reproving the BGS result for $H_5$ against bipartite $H$.
- Proving a result for a $K_4$ subdivision with at least six vertices and silently treating it as $H_5$.
- Checking finitely many graphs by computer.
- Giving an upper bound with a constant that depends on $H$, $m$, or another unbounded parameter.
- Proving an assertion about $\hat r(G,H)$ rather than $r(G,H)$.
- Citing a claimed solution without inspecting a proof-level source.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State the exact definition of $r(G,H)$ and maintain the red-$G$/blue-$H$ orientation throughout.
2. Quantify $C_G$ before the universal choice of $H$ and verify coverage of disconnected, non-bipartite $H$ with no isolated vertices.
3. Verify $H_5$ has five vertices and is the exception to, not an instance of, the BGS theorem on $K_4$ subdivisions with at least six vertices.
4. For every reduction, prove preservation of the no-isolated-vertices condition or account quantitatively for added/deleted isolated vertices.
5. For an upper bound, expose every use of an asymptotic constant and show it depends only on the fixed left graph.
6. For a lower-bound disproof, prove an unbounded ratio, not merely a large lower-bound constant.
7. Audit all imported results against their exact hypotheses and source links; distinguish peer-reviewed results from preprints.

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
