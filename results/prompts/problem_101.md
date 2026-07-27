# Erdős Problem 101: four-point lines with no five collinear

## Definitions and canonical target

For a finite set \(P\subset\mathbb R^2\), write
\[
L_4(P)=\{\ell\text{ an affine line}:|\ell\cap P|=4\}.
\]
For \(n\in\mathbb N\), define
\[
t_4^{(5)}(n)=\max\{|L_4(P)|:P\subset\mathbb R^2,\ |P|=n,\ \text{no affine line contains five distinct points of }P\}.
\]
The target is
\[
t_4^{(5)}(n)=o(n^2)\quad(n\to\infty).
\]
Equivalently: for every \(\varepsilon>0\) there is \(N\) such that every \(n\ge N\) and every admissible \(P\) satisfy \(|L_4(P)|\le\varepsilon n^2\).

Lines are distinct geometric affine lines. Under the no-five condition, “contains four” and “contains exactly four” are equivalent, but retain the exact-four definition throughout.

## Accepted background

- Erdős stated the extremal formulation \(L(n)=o(n^2)\) in [On some metric and combinatorial geometric problems (1986)](https://citeseerx.ist.psu.edu/document?doi=a5f8148c337665cc71edfd1c47cad337c3a2e334&repid=rep1&type=pdf). This is the conjectural target, not a theorem.
- Solymosi and Stojaković proved that, for every fixed \(k>3\), there are planar \(n\)-point sets with no \(k+1\) collinear points and at least \(n^{2-c(k)/\sqrt{\log n}}\) lines containing exactly \(k\) points; see [arXiv:1107.0327](https://arxiv.org/abs/1107.0327) and the peer-reviewed version [DOI:10.1007/s00454-013-9526-9](https://doi.org/10.1007/s00454-013-9526-9). For \(k=4\), this is a theorem giving \(t_4^{(5)}(n)=n^{2-o(1)}\) as a lower bound. It does not disprove \(o(n^2)\).
- Elekes and Szabó proved a restricted positive result for sets on a fixed-degree algebraic curve; see [On Triple Lines and Cubic Curves: The Orchard Problem Revisited](https://doi.org/10.1007/s00454-023-00556-3), especially Theorem 4.3. This is a theorem under extra algebraic-curve hypotheses, not a solution of the unrestricted problem.
- A Lean statement exists in [Formal Conjectures](https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB101%C2%BB/), but its proof body is `sorry`; it fixes notation only and supplies no accepted proof.

Every new use of a result must cite a primary source and state exactly whether it is a theorem, a conjecture, a heuristic, or an unverified claim.

## Complete resolutions

An affirmative resolution is a rigorous proof that for every \(\varepsilon>0\), all sufficiently large admissible \(n\)-point sets have at most \(\varepsilon n^2\) distinct four-point lines.

A negative resolution is a rigorous construction of a fixed \(\varepsilon>0\) and admissible sets \(P_n\) for infinitely many \(n\), with \(|L_4(P_n)|\ge\varepsilon n^2\). The construction must verify real planar realizability, distinctness of points and lines, and the no-five condition.

## What does not count as a solution

- Reproducing or modestly improving a lower bound of the form \(n^{2-o(1)}\).
- Proving only \(O(n^2)\), or any upper bound whose normalized ratio is not shown to tend to zero.
- Proving the result only for points on a fixed-degree curve, lattice-like families, random sets, or another proper subclass.
- Testing finitely many \(n\), numerically optimizing configurations, or reporting a search without a finite certificate proving a stated lemma.
- Treating an informal forum post, an LLM derivation, or a Lean theorem containing `sorry`, `admit`, or an added axiom as a proof.

## Required correctness checks

1. Write all quantifiers explicitly and prove a uniform bound over every admissible \(P\).
2. Count distinct lines exactly once; do not substitute incidences, ordered quadruples, or multiplicity-weighted counts.
3. Check every use of “exactly four” against the no-five hypothesis.
4. For any claimed counterexample, prove a fixed positive density on an infinite sequence of \(n\), not merely an exponent \(2-o(1)\).
5. Audit all geometric transformations and finite-field/projective constructions for preservation of real realizability and of the no-five condition.
6. State constants, thresholds, and dependencies. Do not conceal a degree, \(\varepsilon\), or configuration parameter that grows with \(n\).
7. Have an independent adversarial checker attempt to falsify every pivotal lemma and audit every cited theorem’s hypotheses.

## Required deliverables

- A self-contained statement using \(t_4^{(5)}(n)\), plus a proof-status conclusion: affirmative, negative, or incomplete.
- A source ledger with direct URLs, publication status, exact theorem/lemma used, and a statement of what each source does not establish.
- A proof map identifying the first genuinely new lemma and all dependencies.
- For a positive result, a complete epsilon--N proof. For a negative result, a complete infinite-family construction and density calculation.
- A separate adversarial audit listing all attempted counterexamples to the proof, unresolved gaps, and repairs.
- If formalization is attempted, compilable Lean code with no `sorry`, `admit`, or new axioms, together with an informal-to-formal statement comparison.

## Dynamic Multiagent v2 protocol

Maintain one research root and at most four concurrently active agents total, including the root. Begin with genuinely independent lines of investigation rather than cloning a single proposed method. The root maintains an approach registry containing: identifier, precise target lemma or construction, hypotheses, source dependencies, current evidence, falsification attempts, status, and next decision point.

Choose work packages dynamically from the registry; do not impose fixed agent roles or a fixed mathematical method. In the first wave, reserve independence by pursuing at least two incompatible proof/construction perspectives and one source/statement or adversarial audit. Every wave ends with a synthesis that merges only verified claims, discards duplicated work, and reassigns freed slots to the most discriminating unresolved question.

Any agent asserting progress must provide a proof object or a line-by-line derivation, identify the exact claim proved, and list all unproved assumptions. A different active agent must adversarially check each pivotal lemma before it is promoted to accepted background. Reuse slots immediately after a task reaches a decisive positive or negative answer; run multiple waves until the completion test is met or the runtime boundary is reached.

Use proof-first allocation. At most one optional computational subtask may run at a time, and only after the root records: (i) the exact lemma or counterexample template being tested, (ii) all hypotheses, (iii) the finite search space or certificate format, and (iv) a stopping condition that answers a mathematical question. End and reassign that slot immediately when the stopping condition is met. Computation may not be used as evidence for the asymptotic theorem without a proved reduction.

## Persistence and resumability

Keep `research_state.md` current after each wave. It must record the canonical statement, source ledger, approach registry, accepted lemmas, rejected routes with failure reasons, active proof obligations, computational-task contract if any, and the next smallest independently checkable task.

If execution ends before a complete resolution, do not state or imply success. Save the current audit trail and end the report with `CHECKPOINT_NOT_FINAL`, naming the exact unresolved proof obligation and the next verification step. A later run must read `research_state.md`, revalidate all nontrivial cited claims, and resume from the recorded frontier rather than treating hypotheses or partial arguments as established.
