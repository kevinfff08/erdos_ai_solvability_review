## Definitions and canonical target

Let \(n!=1\cdot2\cdots n\) for every integer \(n\ge2\), and let
\[
S=\sum_{n=2}^{\infty}\frac{1}{n!-1}.
\]
All terms are positive and the series converges absolutely. Prove or disprove the precise assertion \(S\notin\mathbb Q\). This is a single fixed real number; there is no asymptotic parameter and no intended replacement of \(n!-1\) by \(n!\), \(n!+1\), \(n!+t\), or another factorial series.

Current evidence as of 2026-07-27 supports, but does not logically prove, that the question remains open. Recheck its status before expending substantial proof effort.

## Accepted background

- The current Erdős Problems record is [Problem 68](https://www.erdosproblems.com/68), with [LaTeX source](https://www.erdosproblems.com/latex/68). It lists the problem as open but expressly warns that its literature coverage may be incomplete.
- The original cited source is P. Erdős, [*On the irrationality of certain series: problems and results*](https://combinatorica.hu/~p_erdos/1988-22.pdf), *New Advances in Transcendence Theory* (1988), pp. 102–109. The statement that \(\sum 1/(n!+t)\) should be transcendental for every integer \(t\) is a conjectural background statement, not an accepted theorem for \(t=-1\).
- For each \(n\ge2\),
  \[
  \frac1{n!-1}=\sum_{k=1}^{\infty}\frac1{(n!)^k}.
  \]
  Since all summands are nonnegative, Tonelli's theorem permits the corresponding double-series rearrangements. This identity alone does not settle irrationality.
- The exact conjecture is represented in Lean in [ErdosProblems/68.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/68.lean). Its main theorem is presently an open `sorry` statement; only an auxiliary geometric-series identity is proved there.
- Nearby, non-equivalent literature may inspire checks but must not be silently transferred: [Barreto–Kang–Kim–Kovač–Zhang (2026)](https://arxiv.org/abs/2601.21442) study adjacent-product unit-fraction series; [Crmarić–Kovač (2025)](https://arxiv.org/abs/2504.18712) show that another variable-denominator family can attain rational values; [Schlage-Puchta (2011)](https://arxiv.org/abs/1105.1451) treats other factorial series.

## Complete resolutions

An affirmative resolution is a rigorous proof that \(S\notin\mathbb Q\).

A negative resolution is a rigorous proof that \(S\in\mathbb Q\), including an exact rational value \(p/q\) with \(q>0\) and a proof that the infinite sum equals \(p/q\).

A formal Lean proof of the exact assertion is ideal. A conventional proof is complete only if every series interchange, convergence step, denominator-clearing step, integrality claim, and limiting estimate is written explicitly enough for independent verification.

## What does not count as a solution

- More digits of OEIS A331373, empirical nonperiodicity, floating-point PSLQ, or any finite computation without a finite proof certificate.
- A proof for \(\sum1/n!\), \(\sum1/(q^n+r)\), \(\sum1/(n!+t)\) at another \(t\), or a variable factorial-type family without an exact valid reduction to this \(S\).
- Treating Erdős's broader transcendence prediction as established.
- Proving only the geometric expansion or a finite truncation identity.
- A tail estimate that has not also established the precise integrality or fractional-part obstruction required for a rationality contradiction.
- A Lean declaration containing `sorry`, an uncompiled file, or a proof of a mistranscribed statement.

## Required correctness checks

1. The index begins at \(n=2\); \(n=0,1\) would introduce a zero denominator.
2. Every occurrence of a factorial, subtraction, power, and reciprocal must be in the intended real/rational domain, not truncated natural-number arithmetic.
3. Any double-sum rearrangement must cite nonnegativity or absolute convergence.
4. If assuming \(S=a/b\), show exactly which multiplier clears which finite denominators. Do not presume \(N!\) is divisible by \(n!-1\).
5. If a scaled tail is said to be an integer, prove it. If it is said to lie strictly between two integers, give a strict, uniform tail bound.
6. Audit all exceptional small indices and all equality-versus-strict-inequality transitions.
7. For any claimed use of a published theorem, state its hypotheses verbatim enough to verify that \(n!-1\) satisfies them.
8. If formalizing, verify that the target is the `Irrational` statement in `ErdosProblems/68.lean`, not merely its auxiliary identity.

## Required deliverables

- A `research_state.md` source ledger with URL, date, publication status, exact claim, and applicability verdict for every result used.
- A concise status recheck before proof work: exact-statement searches, recent arXiv search, and inspection of the Erdős Problems page and the Lean artifact.
- An approach registry recording each attempted route, its invariant or key lemma, dependencies, current status, and a falsification test.
- For any advance, a self-contained proof note defining all notation and isolating the one new lemma from standard background.
- An adversarial audit that lists every proof obligation and either discharges it or identifies the first genuine gap.
- If resolved, a polished proof plus, where feasible, a compiling Lean artifact or a detailed explanation of why the remaining formalization is routine and what was checked.
- If unresolved, a precise `CHECKPOINT_NOT_FINAL` record: proved lemmas, failed lemmas, counterexamples to candidate claims, and the next smallest proof obligation.

## Dynamic Multiagent v2 protocol

Create one research root and maintain an append-only approach registry. Use at most four concurrent agents at any time.

Begin with genuinely independent waves rather than a fixed assignment: search/status verification, proof-theoretic exploration, literature-to-hypothesis applicability checking, and adversarial testing are natural initial roles, but agents may choose incompatible approaches. Register a route before substantial work: target lemma, hypotheses, planned falsification criterion, dependencies, and whether it is exact or heuristic.

Use multiple waves. When an agent finishes, fails, or reduces a question, immediately reuse the freed slot for the most valuable unresolved proof obligation. Do not retain idle roles. Before elevating any proof claim, assign an agent who did not develop that route to attack its index ranges, integrality, tail bounds, convergence, and statement match. A claim survives only after this independent adversarial pass; record objections and their resolutions in the registry.

Allocate effort proof-first. At most one optional computational subtask may run concurrently. Before starting it, write the exact lemma it tests, its hypotheses, the finite search range, the certificate to retain, and a stopping condition. Computation may reject a candidate lemma or produce a finite exact certificate, but may not stand in for an infinite irrationality proof. Reassign that slot immediately when its stated question is answered.

## Persistence and resumability

Maintain `research_state.md` at the research root after every material wave. It must contain the canonical target, status evidence, source ledger, approach registry, exact proof obligations, checked computations, adversarial findings, and next actions.

If a runtime boundary interrupts an incomplete investigation, do not present it as a resolution. Write `CHECKPOINT_NOT_FINAL` in `research_state.md`, including the last verified statement, unresolved gap, rejected routes with counterexamples or failure reasons, and enough command/source context for a fresh agent to resume without duplicating the evidence audit.
