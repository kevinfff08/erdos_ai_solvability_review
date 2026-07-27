# Erdős Problem 567: Ramsey size-linearity of $Q_3$, $K_{3,3}$, and $H_5$

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

## Accepted background

- Erdős, Faudree, Rousseau, and Schelp introduced Ramsey size-linearity and proved that $e(G)\ge2v(G)-2$ implies non-size-linearity, while every connected $G$ with $e(G)\le v(G)+1$ is size-linear: [EFRS 1993](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/ramsey-size-linear-graphs/2F50FFB56AD4E42EFA80DA5B280225A0).
- Erdős reiterated the $K_{3,3}$ case in 1995: [Erdős 1995](https://revistas.usp.br/resenhasimeusp/pt_BR/article/view/74798).
- Bradač, Gishboliner, and Sudakov proved that every subdivision of $K_4$ with at least six vertices is Ramsey size-linear. They also proved $r(H_5,H)=O(e(H))$ when the varying graph $H$ is bipartite and has no isolated vertices. Their paper explicitly does not establish that $H_5$ is Ramsey size-linear: [published version](https://epubs.siam.org/doi/10.1137/22M1481713), [open preprint](https://arxiv.org/abs/2202.10388).
- A recent result for fixed odd cycles is relevant methodology but does not settle any target here: [Hng--Ji--Lamaison, arXiv:2603.25453](https://arxiv.org/abs/2603.25453).
- The status database currently records this problem as open, while explicitly warning that its label is not a substitute for a literature search: [Erdős Problems #567](https://www.erdosproblems.com/567).

Do not treat the FormalConjectures entry as a proof: its three declarations contain `sorry`, and its introductory displayed formula uses a misleading $\hat r$ notation: [formal artifact](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/567.lean).

## Complete resolutions

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

## Required correctness checks

1. State the exact definition of $r(G,H)$ and maintain the red-$G$/blue-$H$ orientation throughout.
2. Quantify $C_G$ before the universal choice of $H$ and verify coverage of disconnected, non-bipartite $H$ with no isolated vertices.
3. Verify $H_5$ has five vertices and is the exception to, not an instance of, the BGS theorem on $K_4$ subdivisions with at least six vertices.
4. For every reduction, prove preservation of the no-isolated-vertices condition or account quantitatively for added/deleted isolated vertices.
5. For an upper bound, expose every use of an asymptotic constant and show it depends only on the fixed left graph.
6. For a lower-bound disproof, prove an unbounded ratio, not merely a large lower-bound constant.
7. Audit all imported results against their exact hypotheses and source links; distinguish peer-reviewed results from preprints.

## Required deliverables

- A `status_update.md` listing searches performed, sources inspected, publication status, and whether any newer closure was found.
- A self-contained `definitions.md` fixing all graph and Ramsey conventions.
- Either a complete proof manuscript with a dependency map, or a complete counterexample-family manuscript with its lower-bound certificate.
- A `proof_audit.md` that independently checks every nontrivial lemma, all quantifiers, constants, exceptional cases, and the $r$ versus $\hat r$ distinction.
- A `literature_delta.md` separating established theorems, conjectures, and deductions made by the investigation.
- Verifiable citations with direct URLs for all nontrivial imported facts.

## Dynamic Multiagent v2 protocol

Use a research root containing `research_state.md`, an approach registry, source notes, proof drafts, and audit reports. Run at most four concurrent agents at any time.

Start with independent early waves rather than fixed roles: agents should register a distinct candidate route, such as a structural reduction for arbitrary $H$, a close audit/extension attempt of the BGS machinery, a possible obstruction family, or a fresh status-and-source verification. Each registry entry must state its target case(s), precise proposed lemma, dependencies, falsification test, and current evidence.

After each wave, compare approaches, merge only compatible proven lemmas, and use freed slots dynamically for the most informative unresolved bottleneck. Require adversarial proof checking by an agent who did not author the argument. Reassign agents when a route is disproved, duplicated, or reduced to a finite verification task. Continue in multiple waves until a complete resolution or a rigorously documented checkpoint is reached.

Use proof-first allocation. At most one optional computational subtask may run at a time, and only after its owner declares in the registry: the exact lemma or counterexample question, all hypotheses, finite search domain, certificate format, and a stopping condition. Stop that computation immediately once the stated question is answered and reassign its slot to proof or audit work. Computation may guide a lemma but is never evidence for the universal theorem without a separately proved reduction.

## Persistence and resumability

Maintain `research_state.md` after each substantial action. It must record the canonical target, source links and dates, verified lemmas, failed approaches, open proof obligations, active approach-registry entries, and the next smallest auditable tasks.

If a runtime boundary interrupts an incomplete investigation, do not report success or an open-ended partial proof as final. Save the current state and emit `CHECKPOINT_NOT_FINAL`, naming the exact missing lemma, audit, source verification, or counterexample certificate needed to continue.
