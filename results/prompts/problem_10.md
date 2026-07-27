# Erdős Problem 10: prime plus boundedly many powers of two

## Definitions and canonical target

For \(k\in\mathbb Z_{\ge0}\), define
\[
S_k=\left\{p+\sum_{i=1}^{r}2^{a_i}:p\text{ is prime},\ 0\le r\le k,\ a_i\in\mathbb Z_{\ge0}\right\}.
\]
The empty sum is allowed. A power means \(2^a\) with \(a\ge0\), so \(1=2^0\); \(p=2\) is allowed. Repeated exponents are permitted, although pairs of equal powers can be merged, so an equivalent normalized representation has distinct exponents.

Resolve exactly one proposition:
\[
\exists k\,\exists N_0\,\forall n\ge N_0,\quad n\in S_k.
\]

## Accepted background

- Gallagher proved that for every \(\epsilon>0\) there is a \(k(\epsilon)\) with lower density \(\underline d(S_{k(\epsilon)})\ge1-\epsilon\): [Gallagher (1975)](https://link.springer.com/article/10.1007/BF01390190). This is a theorem, not eventual coverage.
- Crocker proved infinite obstructions for a two-power variant: [Crocker (1971)](https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-36/issue-1/On-the-sum-of-a-prime-and-two-powers-of-two/10.2140/pjm.1971.36.103.full). It does not decide arbitrary fixed \(k\).
- Granville and Soundararajan conjectured that three powers suffice for every odd integer \(>1\), hence four for positive even integers: [Granville--Soundararajan (1998)](https://link.springer.com/article/10.1023/A:1009786614584). This is a conjecture, not accepted background theorem.
- The adjacent Linnik--Goldbach problem has two primes, not one. Recent progress there, including six powers under GRH, does not settle this target: [Johnston--Trudgian (2026)](https://arxiv.org/abs/2605.17825).
- A Lean statement exists, but its proofs are `sorry`; do not treat it as a proof: [Formal Conjectures source](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/10.lean).

## Complete resolutions

An affirmative resolution is a rigorous proof of fixed \(k,N_0\) such that every \(n\ge N_0\) belongs to \(S_k\).

A negative resolution is a rigorous proof that for every \(k\) and every \(N_0\), there exists \(n\ge N_0\) with \(n\notin S_k\). Equivalently, for each fixed \(k\), there are arbitrarily large nonrepresentable integers.

## What does not count as a solution

- A density result, including density one, without a proof that the exceptional set is eventually empty.
- A counterexample only for one \(k\), including \(k=3\).
- Any finite search without a theorem controlling all larger integers.
- A result for two primes plus powers of two, or a result restricted to one parity class without closing the other.
- A claimed Lean proof containing `sorry`, `admit`, untrusted target axioms, or an unchecked external oracle.
- Heuristic Hardy--Littlewood calculations or probabilistic evidence presented as a proof.

## Required correctness checks

1. State and preserve the quantifier order \(\exists k\exists N_0\forall n\exists\) representation; \(k\) cannot vary with \(n\).
2. Check \(2^0=1\), the empty sum, repeated powers, and \(p=2\). If normalizing repetitions, prove that the transformation does not increase the number of summands.
3. For a negative construction, prove nonrepresentability against every sum of at most \(k\) powers, not merely sums with distinct positive exponents unless equivalence is justified.
4. For any density or sieve argument, identify exactly where exceptional integers are excluded rather than merely shown sparse.
5. For any modular covering argument, verify every residue/exponent class, coprimality condition, and the possibility that the alleged composite remainder equals its forced divisor.
6. For every cited theorem, provide a direct source URL and state whether it is a theorem, conjecture, preprint, or computation.
7. If formalized, compile the complete dependency closure and provide a proof-escape scan for `sorry`, `admit`, and new axioms.

## Required deliverables

- `research_state.md` with the canonical proposition, source ledger, approach registry, and current proof status.
- A self-contained proof or disproof manuscript with every lemma and dependency stated.
- An adversarial audit that targets quantifiers, parity, binary carries, and all finite-exception claims.
- If computation is used, reproducible code, exact input/output, primality certificates or a specified certified primality method, an exhaustiveness argument, and a statement of the computation's theorem-level role.
- A final status memo distinguishing proved facts, conjectures, failed approaches, and unresolved gaps; cite primary sources directly.

## Dynamic Multiagent v2 protocol

Create a research root and maintain an approach registry containing: proposition attacked, precise intermediate lemma, dependencies, evidence, failure mode, and audit owner. Run at most four agents concurrently. In the first wave, allocate slots to genuinely independent formulations or obstruction/positive routes; do not lock in a static assignment or a prescribed method.

The root must compare approaches as evidence arrives, stop duplicate work, and reuse freed slots dynamically. Every claimed lemma receives adversarial checking by an agent that did not derive it. Run multiple waves: discovery, cross-check/repair, then integration or falsification. Promote an approach only when it has a written lemma with explicit hypotheses and a route to the exact completion test. A route that yields only density, finite verification, or a fixed-small-\(k\) result must be labelled partial and must not consume all slots.

Use proof-first allocation. At most one computational subtask may run at once, and only after recording the target lemma, its hypotheses, the exact certificate required, and a stopping condition. Immediately reassign that slot once the computation answers its stated lemma. Never use computation as an open-ended search for a solution.

## Persistence and resumability

At the end of each wave, update `research_state.md` with source URLs, proof fragments, rejected claims, audit findings, and the next smallest unproved lemma. Preserve command lines and hashes for any artifacts. If a runtime boundary interrupts the work before an affirmative or negative proof has passed adversarial checking, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, state the exact remaining gap, and resume from that checkpoint rather than reporting a resolution.
