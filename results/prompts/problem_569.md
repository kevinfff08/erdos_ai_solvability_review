# Erdős Problem 569 — verification task

## Definitions and canonical target

Let \(k\ge 1\). For finite simple graphs \(F,H\), \(R(F,H)\) is the least \(N\) such that every red-blue colouring of \(E(K_N)\) contains a red non-induced copy of \(F\) or a blue non-induced copy of \(H\). Let \(C_s\) be the cycle on \(s\) vertices. The literal target is to determine the least real \(c_k\) such that, for every finite simple graph \(H\) with \(m=e(H)\ge1\) and no isolated vertices,
\[
R(C_{2k+1},H)\le c_km.
\]

A claimed resolution is \(c_k=2k+1\). The claimed stronger theorem is: for every \(t\ge3\) and every such \(H\),
\[
R(C_t,H)\le (t-1)e(H)+1\le t e(H).
\]

## Accepted background

- The original framework is Erdős, Faudree, Rousseau, and Schelp, [*Ramsey Size Linear Graphs* (1993)](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/ramsey-size-linear-graphs/2F50FFB56AD4E42EFA80DA5B280225A0).
- The claimed complete proof is Stijn Cambie and Andrea Freschi, [*A general bound on \(R(C_k,H)\)*, arXiv:2606.11174 (2026)](https://arxiv.org/abs/2606.11174). It is a preprint, not a peer-reviewed result as of 2026-07-27.
- Related but non-equivalent background: Cambie, Freschi, Morawski, Petrova, and Pokrovskiy prove a sharper large-\(m\) result with an additive term in [arXiv:2601.10238](https://arxiv.org/abs/2601.10238). Do not substitute its asymptotic quantifiers for this task's all-\(m\) target.

The theorem and the exact-constant claim are assertions to verify, not accepted facts.

## Complete resolutions

An affirmative verification requires all of the following:

1. A valid proof of \(R(C_t,H)\le(t-1)e(H)+1\) for every integer \(t\ge3\) and every finite simple \(H\) with no isolated vertices.
2. A valid proof that \(R(C_t,K_2)=t\): exhibit the all-red colouring of \(K_{t-1}\) for the lower bound and check the \(K_t\) dichotomy for the upper bound.
3. The transparent deduction \((t-1)m+1\le tm\) for every \(m\ge1\), followed by \(t=2k+1\), yielding \(c_k=2k+1\).
4. A source-backed conclusion that the literal #569 record is solved, while clearly labeling the evidence as a preprint unless a later refereed version is found.

A negative verification outcome requires a concrete counterexample to the claimed theorem or a precise unrepaired flaw that makes the proof fail for a stated admissible case.

## What does not count as a solution

- An \(O_k(m)\) estimate without the least constant.
- A proof only for connected \(H\), for sufficiently large \(m\), or for selected graph classes.
- Treating the large-\(m\) coefficient \(2\) as the literal answer; \(H=K_2\), \(m=1\), is in scope.
- Numerical verification of finitely many graphs or cycle lengths.
- Repeating an abstract or relying on a forum comment without auditing the proof.
- Declaring a different Ramsey problem open or solved as if that settled this exact quantifier pattern.

## Required correctness checks

- Audit every induction use in arXiv:2606.11174: the base \(e(H)=1\), decomposition of disconnected \(H\), and deletion of a minimum-degree vertex for connected \(H\).
- Verify all uses of the no-isolated-vertices condition, especially after deleting the chosen vertex and in each inductive subgraph.
- Check the red-star construction, the path-to-cycle closure, and the second-neighbourhood lemma, including all small cycle-length cases.
- Recompute the random bipartition expectation and every inequality used to bound \(e(H_2)\), \(|U_2|\), and the final chromatic-number contradiction.
- Keep the paper's cycle parameter \(t\) distinct from the problem's \(k\), and check that no induced-copy convention slipped in.
- Independently check the exact lower-bound witness \(K_2\) and every endpoint: \((t-1)m+1\le tm\) needs \(m\ge1\).

## Required deliverables

1. A concise verification report with a theorem-dependency map and a pass/fail finding for each essential lemma.
2. A self-contained derivation from the verified theorem and \(H=K_2\) to \(c_k=2k+1\).
3. A list of every source consulted, with direct URL, author, date, and status (peer-reviewed/preprint/informal).
4. If a flaw is found, a minimal precise counterexample or gap report identifying the exact statement, page, and dependency affected.
5. A recommended database status: solved only if the complete proof survives audit; otherwise state the narrowest justified alternative.

## Dynamic Multiagent v2 protocol

Use research root `research_root/problem_569/`. Maintain at most four concurrent agents, including the coordinator. Begin with independent approaches rather than a fixed division of mathematical labor. The coordinator maintains an approach registry recording each active line's target claim, dependencies, evidence links, status, and duplicate-risk assessment.

Run multiple waves. In wave one, independently inspect: (a) the proof's induction and disconnected case, (b) its structural path/second-neighbourhood lemmas and small cases, and (c) its numerical/random-partition/chromatic inequalities plus the \(K_2\) lower bound. Before adding an agent, check the registry and assign an untested dependency or an adversarial audit, not a duplicate paraphrase. Reuse a freed slot immediately for the most consequential unresolved dependency, a counterexample search tied to a stated lemma, or cross-checking a claimed repair.

Every proposed verification must receive adversarial proof checking by an agent that did not produce it. Agents must report exact claims, assumptions, page/line references, and whether their conclusion is a proof, a source statement, or an inference. The coordinator decides only after reconciling conflicts and preserving failed approaches in the registry.

Resource allocation is proof-first. Allow at most one optional computational subtask. Before it starts, declare the exact lemma or boundary condition it tests, finite hypotheses, certificate format, and stopping condition. Stop it immediately when that question is answered and reassign its slot; computation cannot establish the universal theorem by sampling.

## Persistence and resumability

Keep `research_state.md` in the research root. After every material finding, record sources and versions, inspected proof ranges, active claims, approach registry, unresolved dependencies, counterexample attempts, and next adversarial check. Preserve citations as direct URLs. If a runtime boundary arrives before a decisive audit, write `CHECKPOINT_NOT_FINAL` at the top of the state file and return only the verified partial findings plus exact next steps; do not call the claimed solution verified or rejected prematurely.
