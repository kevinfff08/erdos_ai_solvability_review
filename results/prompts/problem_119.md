# Erdős Problem 119(iii): cumulative growth of unit-circle products

## Definitions and canonical target

Let \(\mathbb T=\{w\in\mathbb C:|w|=1\}\). Let \((z_i)_{i\ge1}\) be an arbitrary infinite sequence in \(\mathbb T\); repetitions and arbitrary ordering are allowed. Define
\[
p_n(w)=\prod_{i=1}^n(w-z_i),\qquad
M_n=\max_{w\in\mathbb T}|p_n(w)|\quad(n\ge1).
\]
The maximum exists because \(\mathbb T\) is compact.

Prove or disprove the following residual target:
\[
\forall (z_i)\subset\mathbb T\;\exists c>0\;\exists N_0\;\forall n\ge N_0,
\qquad \sum_{k=1}^{n}M_k>n^{1+c}.
\]

Use this quantifier order unless primary historical sources establish that the intended problem requires an absolute exponent \(c\) independent of the sequence. Do not silently switch to that stronger version. “For all large \(n\)” means every integer \(n\ge N_0\), and the inequality is strict.

## Accepted background

- Wagner proved the first, weaker question: for every admissible sequence, \(M_n>(\log n)^c\) for infinitely many \(n\), for some \(c>0\). See Gerold Wagner, [On a Problem of Erdős in Diophantine Approximation](https://doi.org/10.1112/blms/12.2.81), *Bull. London Math. Soc.* 12 (1980), 81–88.
- Beck proved the second question: a polynomial lower bound for \(\max_{m\le N}M_m\), hence polynomially large individual values for infinitely many indices. See József Beck, [The modulus of polynomials with zeros on the unit circle: A problem of Erdős](https://annals.math.princeton.edu/1991/134-3/p03), *Ann. of Math.* 134 (1991), 609–651.
- Erdős gave a sequence with \(M_n\le n+1\); Linden improved this to a sequence with \(M_n\ll n^{1-c_0}\) for some \(c_0>0\). See C. N. Linden, [The Modulus of Polynomials with Zeros on the unit Circle](https://academic.oup.com/blms/article/9/1/65/293413), *Bull. London Math. Soc.* 9 (1977), 65–69.
- The current Erdős Problems record still lists the third question as open and the first two as resolved: [Problem #119](https://www.erdosproblems.com/119). Its Lean statement is available in [Formal Conjectures #119](https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB119%C2%BB/), but the relevant theorem declarations contain `sorry`; this is not a proof.
- Treat reports from July 2026 of a one-page AI/human proof as unverified until an actual proof text or a proof-assistant artifact can be inspected. They are not accepted background.

## Complete resolutions

An affirmative resolution must give a rigorous proof of the displayed target for every admissible infinite sequence, including explicit quantifier handling for \(c\) and \(N_0\).

A negative resolution must give one explicit admissible infinite sequence and prove
\[
\forall c>0\;\forall N_0\;\exists n\ge N_0,
\qquad \sum_{k=1}^{n}M_k\le n^{1+c}.
\]

If archival research establishes that the intended exponent must be universal across sequences, document the exact source and treat that as a separate, stronger target rather than changing this one retroactively.

## What does not count as a solution

- A proof of \(\limsup M_n=\infty\), a logarithmic lower bound, or Beck's already-known initial-maximum theorem.
- Polynomially large \(M_n\) on merely infinitely many indices.
- A cumulative lower bound only along a subsequence of endpoints, without a proof covering every sufficiently large endpoint.
- A result for random, equidistributed, distinct, or specially ordered zeros only.
- Numerical experiments, plots, or finite exhaustive checks without a finite certificate that implies the quantified infinite theorem.
- A theorem declaration with `sorry`, a media report, or an inaccessible “one-page proof.”

## Required correctness checks

1. Verify that every argument is uniform over arbitrary ordered sequences in \(\mathbb T\), with repeated values allowed.
2. State whether each constant is absolute or sequence-dependent; never move a constant across a universal quantifier without proof.
3. Preserve the distinction between “infinitely many \(n\)” and “all sufficiently large \(n\).”
4. Track the sum convention \(\sum_{k=1}^n\). If using \(M_0=1\), \(\sum_{k<n}\), or dyadic intervals, prove the endpoint conversion.
5. Any block estimate must show exactly how it yields the all-\(n\) prefix-sum conclusion; bounds at isolated dyadic scales alone are insufficient.
6. Check any use of a maximum-over-prefix statement: it controls a peak, not automatically the density or total mass of peaks.
7. For a candidate 2026 proof, first write its precise claimed theorem, then independently verify all hypotheses, normalization factors, inequalities, and the final quantifier conversion.

## Required deliverables

- `research_state.md` containing the canonical statement, exact source URLs, a theorem/conjecture ledger, and a dated approach registry.
- A self-contained proof or counterexample manuscript with all lemmas stated precisely and citations for every imported theorem.
- An adversarial audit that identifies every nontrivial inference and reports whether it was independently checked.
- A short status memo distinguishing new proof, partial result, reproduction of Wagner/Beck, failed approach, and unresolved gap.
- If a computation is used, include code or an exact reproducible certificate, the declared lemma it tests, its hypotheses, and its stopping condition.
- If the 2026 candidate proof becomes available, archive its stable URL/hash and provide a line-by-line comparison to the canonical target.

## Dynamic Multiagent v2 protocol

Establish a research root responsible for `research_state.md`, source integrity, and merging only verified claims. Use at most four concurrent agents total.

At the first wave, create an approach registry before substantial work. Allocate independent approaches dynamically rather than fixing permanent roles: one may inspect primary literature and candidate claims, another may search for a structural proof/counterexample route, another may attempt a reduction to a precisely stated block-sum lemma, and another may adversarially audit emerging arguments. Record for every approach: target lemma, assumptions, dependency on external results, status, and decisive next check.

Run multiple waves. At the end of each wave, the research root must eliminate duplicated routes, promote only checked lemmas, and reuse freed slots for the highest-value unresolved dependency. Every purported proof receives an adversarial pass by an agent that did not develop it; the adversary must test quantifier order, endpoint conventions, zero multiplicities, constant dependence, and the jump from sparse peaks to cumulative growth.

Use proof-first allocation. At most one optional computational subtask may run at a time. Before any computation, register the exact lemma or counterexample property being tested, the finite input class, the certificate to be produced, and a stopping condition. Computation may guide or certify a finite auxiliary claim only; it cannot establish the asymptotic theorem by sampling. Immediately reassign that slot when its declared question is answered.

Do not prescribe a fixed mathematical method. Literature-derived observations may guide hypothesis selection, but incompatible proof and counterexample approaches must remain eligible while evidence supports them.

## Persistence and resumability

Update `research_state.md` after each material result with: canonical target, sources consulted, verified facts, failed approaches, open proof obligations, active approach registry, and exact next actions.

When a runtime boundary interrupts an incomplete investigation, do not claim completion. Write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, preserve all proof obligations and evidence links, and resume from the registry with fresh adversarial checks before making any status claim.
