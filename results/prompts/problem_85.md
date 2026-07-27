# Erdős Problem 85: eventual monotonicity of the C4-free minimum-degree threshold

## Definitions and canonical target

Work with finite simple undirected graphs. Let C4 be the cycle on four vertices, as a non-induced subgraph. For every integer n >= 4 define

f(n) = min { d in Z : every n-vertex graph G with delta(G) >= d contains C4 }.

Equivalently,

f(n) = 1 + max { delta(G) : G is an n-vertex C4-free simple graph }.

Canonical target: prove or disprove

there exists N >= 4 such that, for every integer n >= N, f(n+1) >= f(n).

This is an eventual statement. A proof must identify or establish the existence of one uniform threshold N; it is not a statement about infinitely many n or about a chosen subsequence.

The associated Ramsey number R(C4,K_{1,t}) is useful only with a derivation from definitions. For an m-vertex graph, a K_{1,t}-free complement is equivalent to minimum degree at least m-t in the original graph, giving

R(C4,K_{1,t}) = min { m : f(m) <= m-t }.

Do not rely without repair on the other inverse formula printed in the Erdős Problems remark: its variables and boundary range are unclear.

## Accepted background

The following are accepted background, not resolutions of the target.

- Double counting common neighbours in C4-free graphs gives the standard scale f(n) < sqrt(n)+1 and hence f(n)=(1+o(1))sqrt(n) when combined with constructions. See the current [Erdős Problems #85 record](https://www.erdosproblems.com/85) and its [LaTeX source](https://www.erdosproblems.com/latex/85).
- Burr, Erdős, Faudree, Rousseau, and Schelp initiated the C4-versus-star Ramsey line in [Some Complete Bipartite Graph–Tree Ramsey Numbers](https://www.sciencedirect.com/science/article/pii/S0167506008704527) (1989).
- Chen proved R(C4,K_{1,t+1}) <= R(C4,K_{1,t})+2 in [A result on C4-star Ramsey numbers](https://doi.org/10.1016/0012-365X(95)00340-3) (1997). This is not the requested monotonicity theorem.
- Parsons-type projective-plane constructions and their extensions give exact Ramsey values on special parameter families. One precise extension is Zhang, Chen, and Cheng, [Polarity graphs and Ramsey numbers for C4 versus stars](https://research.polyu.edu.hk/en/publications/polarity-graphs-and-ramsey-numbers-for-csub4subversus-stars/) (2017).
- Luis Boza's [2024 preprint](https://arxiv.org/abs/2409.12770) determines the previously unknown values with t <= 37 and proves several special-parameter bounds. Treat it as a preprint and audit every theorem used.
- The current companion [Erdős Problem #552 record](https://www.erdosproblems.com/552) summarizes exact known C4-versus-star cases and remains open.
- A Lean statement exists at [FormalConjectures/ErdosProblems/85.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/85.lean), but it contains `sorry`; it formalizes a target, not a proof.

## Complete resolutions

An affirmative resolution is a rigorous proof of one N >= 4 such that f(n+1) >= f(n) for every n >= N.

A negative resolution is a rigorous proof that for every N there exists n >= N with f(n+1) < f(n). In particular, a single strict descent is not a disproof; the descents must occur arbitrarily far out.

Every claimed resolution must state the exact convention for C4, graphs, f, and all ranges, and must include a source-audited derivation if it translates through Ramsey numbers.

## What does not count as a solution

- A finite table, SAT run, enumeration, or computation of Ramsey values without a proved reduction from all large n to that finite computation.
- The asymptotic f(n)=(1+o(1))sqrt(n), a bound f(n)<sqrt(n)+1, or a bounded-drop statement f(m)>f(n)-c.
- A result only for prime-power, square, congruence, or other infinite subsequences.
- A result about maximum edge count or average degree that is not converted rigorously to the maximum minimum degree of C4-free graphs.
- Chen's Ramsey increment bound, by itself.
- A proof for induced C4-free graphs, multigraphs, directed graphs, or a different Ramsey convention.
- An unverified citation, inaccessible claimed proof, or formal file containing an axiom/sorry in the part that establishes the target.

## Required correctness checks

1. Verify that every occurrence of C4 means a non-induced subgraph.
2. Check f(n)-1 is the maximum possible minimum degree, not maximum degree, average degree, or an edge extremal number.
3. Check the polarity/projective-plane construction parameters, primality/prime-power assumptions, deleted vertices, and preservation of minimum degree.
4. For every complement/Ramsey conversion, rederive delta(G)=m-1-Delta(complement G) and check the star has t leaves and t+1 vertices.
5. Audit all integer roundings, strict versus weak inequalities, and index shifts n, n+1, m, and t.
6. For an affirmative proof, identify where one uniform N is produced. For a negative proof, identify where arbitrary largeness of descents is produced.
7. If computation is used, demand an independently checkable certificate and a theorem saying exactly why the computation has a stopping condition.
8. If formal verification is claimed, compile the exact commit and ensure the final theorem has no `sorry`, axiomatized target lemma, or unproved noncomputable gap.

## Required deliverables

- `research_state.md`: dated source log, definitions, approach registry, current claims, failed lemmas, and exact next tests.
- A concise literature ledger with stable URLs, authors, year, publication status, and a one-sentence statement of what each source actually proves.
- A proof manuscript or counterexample manuscript with every auxiliary lemma stated precisely.
- A proof-audit document that independently checks the central reduction, all boundary cases, and all Ramsey translations.
- If a computational subtask is approved, its code, input, environment, certificate, proof of the stopping condition, and a human-readable verification script.
- A final status memo distinguishing proved results, conjectures, computational evidence, and unresolved gaps.

## Dynamic Multiagent v2 protocol

Create one research root with a shared `research_state.md`. Use at most four concurrent agents total, including the coordinator. Do not fix roles permanently.

At the first wave, register at least two genuinely independent proof directions before deepening either: for example, a direct C4-free minimum-degree structural route and a rigorously derived Ramsey-number route. A third slot may audit the literature/formalization. The coordinator maintains an approach registry containing: approach ID, exact target lemma, hypotheses, source dependencies, attempted deductions, status, and falsification tests.

After each material lemma, assign an adversarial checker who did not write that lemma to test quantifiers, C4 convention, degree type, parameter shifts, and hidden use of a stronger theorem. Negative results, failed constructions, and counterexamples to intermediate claims must be recorded in the registry and used to reallocate slots.

Reuse a slot immediately when its question is answered, rather than preserving a static assignment. Run multiple waves: discovery, cross-checking, synthesis, and final adversarial audit. At every wave boundary, compare routes only by their proved lemmas and remaining logical gap, not by plausibility or amount of computation.

Proof-first allocation rule: at most one optional computational subtask may run at once. Before it runs, the registry must state the exact finite lemma/question, hypotheses, certificate format, and stopping condition. When that question is answered, terminate or archive the computation and reassign the slot to proof development or auditing. Do not use computation merely to extend a table.

## Persistence and resumability

Update `research_state.md` after every source audit, proposed lemma, proof failure, computation result, or change in status. Include exact URLs/versions and enough detail to reproduce all deductions.

If execution time ends before a complete audited proof or disproof exists, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, summarize the verified state and the next smallest proof obligation, and do not claim a resolution. On resumption, begin by auditing the checkpoint and the approach registry before launching new work.
