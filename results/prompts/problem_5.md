# Erdős Problem 5: all normalized consecutive-prime-gap limit points

## Definitions and canonical target

Let \(p_n\) denote the \(n\)-th prime and let
\[
g_n:=p_{n+1}-p_n.
\]
All logarithms are natural. Define the finite limit-point set
\[
S:=\left\{C\in[0,\infty):\exists\ n_1<n_2<\cdots,\ n_i\to\infty,\ \frac{g_{n_i}}{\log n_i}\to C\right\}.
\]

The canonical target is
\[
S=[0,\infty).
\]
Equivalently, prove or disprove that for every finite \(C\ge0\), every \(\varepsilon>0\), and every \(N\ge1\), there is an \(n\ge N\) with
\[
\left|\frac{p_{n+1}-p_n}{\log n}-C\right|<\varepsilon.
\]

The primes must be consecutive. The separate extended-real assertion \(\infty\in S\) is already known. Literature frequently normalizes by \(\log p_n\); it is legitimate to transfer between the two normalizations only after explicitly using \(p_n\sim n\log n\), hence \(\log p_n/\log n\to1\).

## Accepted background

Verify exact theorem statements before use. The following are accepted prior results, not a solution of the canonical target.

- Goldston, Pintz, and Yıldırım prove \(\liminf g_n/\log p_n=0\), so \(0\in S\): https://annals.math.princeton.edu/2009/170-2/p10
- Banks, Freiberg, and Maynard prove that among any nine prescribed nonnegative targets, one pairwise difference is a limit point; in particular at least 12.5% of nonnegative reals are limit points: https://doi.org/10.1112/plms/pdw036
- Pintz proves a fixed interval \([0,c]\subset S\) for some ineffective \(c>0\), and later improves a measure lower bound: https://arxiv.org/abs/1305.6289 and https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/184/4/112647/a-note-on-the-distribution-of-normalized-prime-gaps
- Merikoski proves \(\lambda(S\cap[0,T])\ge T/3\) for every \(T\ge0\) and that \(S\) has bounded gaps: https://doi.org/10.1112/jlms.12314
- The current historical record, including the large-gap result giving \(\infty\) as an extended limit point, is: https://www.erdosproblems.com/5

Do not treat a positive-measure, positive-density, or bounded-gap statement as interval coverage. A 2026 upload calling itself a conditional solution depends on an unproved Hardy–Littlewood-type hypothesis and is not accepted as an unconditional result: https://www.researchgate.net/publication/405816241_Analytical_Investigation_of_Normalized_Prime_Gaps_and_Residue-Class_Driven_Sequences_A_conditional_solution_to_Erdos_Problem_5_by_the_use_of_AI

## Complete resolutions

An affirmative resolution is an unconditional proof that every finite \(C\ge0\) belongs to \(S\), with an unbounded index sequence for each \(C\), consecutiveness of the two primes, and normalization conversion all justified.

A negative resolution is an unconditional proof of one finite \(C\ge0\), an \(\varepsilon>0\), and \(N_0\) such that every \(n\ge N_0\) stays at least \(\varepsilon\) away from \(C\) after normalization.

## What does not count as a solution

- Covering only \(C=0\), a fixed initial interval, a large finite target, or a positive-measure/positive-density/relatively-dense subset.
- A conditional result under Hardy–Littlewood, Elliott–Halberstam, or another unproved assumption, unless explicitly labelled conditional.
- A numerical experiment, fitted distribution, or finite list of approximate gaps.
- A claim about primes that are not proved consecutive.
- Replacing \(\log n\) with \(\log p_n\), or changing scales, without a stated asymptotic transfer.
- Proving only \(\infty\) is an extended limit point.

## Required correctness checks

1. State the \(C,\varepsilon,N\) quantifier order and exhibit unbounded indices.
2. For each alleged consecutive gap, certify that every integer strictly between the endpoints is composite.
3. Track all parameters from construction scale to prime index and prove every \(\log p_n\leftrightarrow\log n\) replacement.
4. Separate \(C=0\), finite \(C>0\), and the extended \(\infty\) statement.
5. Check all analytic inputs for uniformity ranges, exceptional moduli, admissibility, and error terms.
6. Do not infer full coverage from Lebesgue measure, density, or bounded gaps.
7. Have an adversary attempt to convert each asserted limit into an explicit \(\varepsilon,N\) statement and locate any missing dependency.
8. Before a completion claim, repeat a current literature search and inspect the primary source for every claimed predecessor or competing result.

## Required deliverables

- `research_state.md` with the canonical target, exact bibliography, source-status table, theorem statements, approach registry, and all accepted/rejected lemmas.
- A source audit separating peer-reviewed results, preprints, databases, and forum claims.
- For any proposed proof or disproof: a dependency graph, quantified lemma statements, a consecutiveness audit, and a normalization/error ledger.
- For incomplete work: the strongest verified lemma, the first unsupported implication, failed approaches, and the next falsifiable sublemma.
- Stable links and theorem locations for every external mathematical claim; no citation may rest on a search snippet alone.

## Dynamic Multiagent v2 protocol

Operate under one research root with at most four concurrently active agents. In the first wave, launch genuinely independent lines of inquiry selected dynamically by the root: literature/theorem verification, direct proof-route formulation, obstruction/counterexample analysis, and a separate audit of normalization and consecutiveness may be appropriate, but do not lock in a static assignment or a prescribed method.

Maintain an approach registry in `research_state.md`. Each entry must record the exact target lemma, assumptions, dependencies, evidence inspected, status, and why it was retained or rejected. Work in multiple waves. At every wave boundary, the root compares results, directs at least one adversarial check at each pivotal claim, and reuses freed slots for the currently most informative unresolved dependency. No agent may accept another agent's summary in place of reading the cited source or checking the derivation.

Allocate effort proof-first. There may be at most one optional computation at a time. Before it starts, record: the precise lemma or counterexample predicate; all hypotheses; a machine-independent certificate format; a finite stopping condition; and what each possible outcome changes in the proof plan. Stop and reassign that slot immediately once the question is answered. Finite computation may certify a finite subclaim or falsify an auxiliary conjecture; it can never establish the required infinite universal limit-point assertion by extrapolation.

## Persistence and resumability

Update `research_state.md` after each source verification, wave, accepted lemma, rejected lemma, and computational subtask. Preserve exact queries, source links, theorem locations, parameter choices, and proof-audit findings.

If execution stops before a complete resolution, put `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`. State the last fully verified result, the first unresolved dependency, active approaches, and the next concrete verification task. On resumption, verify that checkpoint and refresh the literature search before continuing; do not promote an incomplete route to a solution claim.
