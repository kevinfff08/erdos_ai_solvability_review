# Erdős Problem 28 — research prompt

## Definitions and canonical target

Let \(A\subseteq\mathbb N\), where choosing \(\mathbb N=\{0,1,\ldots\}\) or \(\{1,2,\ldots\}\) is immaterial because the hypothesis and conclusion are stable under finite changes. Define
\[
r_A(n):=(1_A*1_A)(n)=\#\{(a,b)\in A\times A:a+b=n\}.
\]
Representations are **ordered**, and diagonal pairs \((a,a)\) count once. Say that \(A\) is an asymptotic additive basis of order \(2\) if there exists \(N_0\) such that every \(n\ge N_0\) belongs to \(A+A\), equivalently \(r_A(n)\ge1\).

Prove or disprove:
\[
\forall A\subseteq\mathbb N,\quad [A+A\text{ contains every sufficiently large integer}]\Longrightarrow\limsup_{n\to\infty}r_A(n)=\infty.
\]
Equivalently, under eventual coverage, for every \(M,X\in\mathbb N\) there must be \(n\ge X\) with \(r_A(n)\ge M\).

## Accepted background

- Erdős and Turán posed the problem in 1941: [Erdős–Turán, *J. London Math. Soc.*](https://doi.org/10.1112/jlms/s1-16.4.212). Their stronger conjecture is \(\limsup r_A(n)/\log n>0\); it is not the target here.
- Borwein, Choi, and Chu proved that an asymptotic order-2 basis cannot have its representation function globally bounded by \(7\): [*Mathematics of Computation* 75 (2006), 475–484](https://www.ams.org/mcom/2006-75-253/S0025-5718-05-01777-1/). This is a theorem, not a proof of unboundedness.
- Dowd studied finite and coding-theoretic formulations: [*SIAM J. Discrete Math.* 1 (1988), 142–150](https://doi.org/10.1137/0401016). A transfer between finite cyclic groups and the one-sided infinite problem must be proved, never presumed.
- Li and Zhang prove recent density-conditioned finite lower bounds, including \(\overline d(\mathbb N\setminus(A+A))<7/32\Rightarrow\limsup r_A>5\): [arXiv:2605.30922](https://arxiv.org/abs/2605.30922). This still gives only a fixed lower bound when \(A+A\) is cofinite.
- Ding, Sun, and Zhao prove \(R_m\le128\) for every finite cyclic group: [arXiv:2607.06167](https://arxiv.org/abs/2607.06167). This is relevant finite-group context, not a counterexample.
- The target statement has an official Lean declaration, but its proof is still `sorry`: [FormalConjectures/ErdosProblems/28.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/28.lean).
- Treat claimed proofs by Theophilus Agama ([arXiv:1707.05679](https://arxiv.org/abs/1707.05679)) and Konstantinos Smpokos ([OSF preprint record](https://sciety.org/articles/activity/10.31219/osf.io/mxgbu)) as unverified claims only. They must be independently audited before any lemma is reused.

## Complete resolutions

An affirmative resolution is a complete proof of the displayed universal implication, with all finite-exception and ordered-count conventions explicit.

A negative resolution is an explicit \(A\subseteq\mathbb N\), a finite constant \(C\), and complete proofs that \(A+A\) is cofinite and \(r_A(n)\le C\) for every \(n\). The construction must have a precise membership rule, not merely a numerical prefix.

## What does not count as a solution

- A result for a density-restricted, random, periodic, or otherwise special class of bases.
- Excluding one additional fixed bound \(C\), or recovering the known \(C=7\) result.
- An average-order theorem, a positive-density conclusion, or \(\limsup r_A>K\) for one fixed \(K\).
- A computation with no proved finite-to-infinite reduction, stopping condition, and exhaustive certificate.
- A construction in \(\mathbb Z\) or \(\mathbb Z_m\) presented as a construction in \(\mathbb N\).
- A proof for unordered representations without a fully justified conversion to the ordered statement.
- Reliance on an unreviewed claimed proof without line-by-line verification.

## Required correctness checks

1. State whether \(0\in\mathbb N\); show any finite convention change is harmless.
2. Verify every use of \(r_A\) counts ordered pairs, including the diagonal.
3. Preserve the exact hypothesis \(\exists N_0\,\forall n\ge N_0\), rather than a density-one or subsequential substitute.
4. Prove a limsup conclusion, not merely one large value or an average estimate.
5. For every finite-group reduction, prove the direction and quantify all losses; do not infer an infinite basis from bounded \(R_m\).
6. Audit all compactness, limit, and truncation arguments for preservation of both eventual coverage and a uniform representation bound.
7. For every computational claim, provide code, deterministic environment instructions, input domain, symmetry reductions, machine-readable output, and a human-checkable exhaustiveness certificate.
8. If a Lean proof is claimed, compile with no `sorry`, `admit`, or new axioms and compare the theorem type directly with the canonical target.

## Required deliverables

- A concise status memo distinguishing proved results, conjectures, and unverified claims, with direct URLs and publication status.
- Either a complete affirmative proof, or an explicit counterexample plus proof, matching the completion test exactly.
- A dependency graph of every nontrivial lemma and an adversarial audit of the central implication.
- A notation/convention sheet for \(\mathbb N\), ordered representations, finite exceptions, and limsup.
- If incomplete: the strongest precisely stated lemma proved, the exact blocking lemma, failed approaches with identified failure points, and a reproducible `research_state.md`.
- Citations for all imported mathematical claims. Primary papers or official repositories are required where available; label preprints and informal claims as such.

## Dynamic Multiagent v2 protocol

Maintain one research root with at most four concurrent agents total. Begin with independent approaches rather than a fixed division of mathematical labor. Create and continuously update an approach registry containing: approach identifier, exact target lemma, assumptions, relation to the canonical theorem, evidence used, current status, and falsification test.

Use multiple waves. In the first wave, allocate independent slots to source/claim verification, direct proof exploration, counterexample/obstruction exploration, and a finite-model bridge audit only if those are genuinely distinct. After each wave, the research root compares assumptions and merges only statements that have survived adversarial checking. Reuse freed slots dynamically for the current bottleneck; do not preserve assignments merely because they were initial.

Every proposed proof receives an adversarial proof-check pass by an agent that did not create its key argument. That pass must test quantifiers, one-sidedness of \(\mathbb N\), ordered-versus-unordered counts, hidden eventual thresholds, limiting steps, and theorem citation scope. A claimed resolution cannot be promoted until an independent agent reconstructs the crucial chain without relying on unexplained intuition.

Proof work has priority. At most one computational subtask may run at once. Before it begins, record the exact lemma or construction it tests, all hypotheses, the finite search space, the certificate format, and a stopping condition. Immediately reassign that slot after the question is answered; computation may not become an open-ended search for patterns.

## Persistence and resumability

At the end of every wave and before any runtime boundary, update `research_state.md` with the canonical target, source ledger, approach registry, verified lemmas, rejected claims, open proof obligations, commands/certificates if computation occurred, and the next highest-value adversarial check.

If the investigation is interrupted before a complete resolution, return `CHECKPOINT_NOT_FINAL` and the current `research_state.md` contents or path. Do not phrase partial progress, a plausible argument, or an unverified preprint as a solution.
