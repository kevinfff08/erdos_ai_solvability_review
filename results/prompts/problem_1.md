# Erdős Problem #1: distinct subset sums

## Definitions and canonical target

Let \(A\) be a finite set of positive integers. Call \(A\) **sum-distinct** (or dissociated in this integer setting) when the map
\[
S\subseteq A\longmapsto \sum_{a\in S}a
\]
is injective. Equivalently, for every two distinct subsets \(S,T\subseteq A\), their sums differ; equivalently, there is no nonzero coefficient vector \(\varepsilon\in\{-1,0,1\}^{A}\) with \(\sum_{a\in A}\varepsilon_a a=0\).

Define
\[
m(n):=\min\{\max A: A\subset\mathbb Z_{>0},\ |A|=n,\ A\text{ is sum-distinct}\}.
\]

Canonical target: prove that there is an absolute constant \(c>0\) such that
\[
m(n)\ge c2^n\quad\text{for every }n\ge1.
\]
Equivalently, for every \(N,n\ge1\) and every \(A\subseteq\{1,\ldots,N\}\) with \(|A|=n\) and distinct subset sums, prove \(N\ge c2^n\). The constant must not depend on \(n\), \(N\), or \(A\).

A disproof is a rigorously verified sequence \(A_j\) of sum-distinct positive-integer sets with \(|A_j|\to\infty\) and \(\max A_j/2^{|A_j|}\to0\).

## Accepted background

- The elementary counting argument gives \(m(n)\ge(2^n-1)/n\).
- Dubroff, Fox, and Xu proved
  \[
  m(n)\ge\binom n{\lfloor n/2\rfloor}
  =\left(\sqrt{2/\pi}-o(1)\right)\frac{2^n}{\sqrt n}.
  \]
  Their paper supplies a Berry--Esseen argument and a second proof via Harper's vertex-isoperimetric inequality: [arXiv version](https://arxiv.org/abs/2006.12988), [published SIAM version](https://doi.org/10.1137/20M1385883).
- Steinerberger gave a Fourier/random-walk proof of the same best known asymptotic lower bound and a real 1-separated extension: [published paper](https://doi.org/10.1142/S1793042123500860).
- Constructions show the exponential scale is attainable from above; Bohman's construction gives \(m(n)<0.22002\,2^n\) asymptotically: [paper](https://doi.org/10.1090/S0002-9939-96-03653-2).
- The 2025 paper of Cambie, Gao, Kim, and Liu proves a sharp result for a modular variant, not for this target: [journal page](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/en/publishing-house/journals-and-series/acta-arithmetica/all/217/4/115883/the-erdos-distinct-subset-sums-problem-in-a-modular-setting).
- The exact finite extremal function is OEIS [A276661](https://oeis.org/A276661). Its finite values and constructions are background only.
- Do not cite the 2025 Bado manuscript as a solution. Its claimed uniform lower-bound step is not established, and the author's later [2026 note](https://www.researchgate.net/publication/405215338_FOURIER_RIGIDITY_AND_MODULAR_STRUCTURE_OF_SUM-DISTINCT_SETS) explicitly separates what remains needed for the conjectural bound.

The conjecture is not the stronger Conway--Guy exact-value conjecture \(F(2^k)=k+2\) for large \(k\), nor the real 1-separated variant, nor the modular problem.

## Complete resolutions

An affirmative resolution must provide a complete proof of an absolute \(c>0\) such that \(\max A\ge c2^{|A|}\) for every sum-distinct finite set \(A\subset\mathbb Z_{>0}\). It must state exactly where uniformity in \(A\) and \(|A|\) enters.

A negative resolution must provide an explicit or rigorously proved infinite family \(A_j\) of sum-distinct sets with \(|A_j|\to\infty\) and \(\max(A_j)=o(2^{|A_j|})\), together with a full proof that every subset-sum collision is excluded.

## What does not count as a solution

- Reobtaining the DFX/Steinerberger \(2^n/\sqrt n\) scale or improving only its constant.
- A theorem for a special family, a real-separated model, a modular model, or random instances without a proved reduction to all integer sum-distinct sets.
- Finite exact values, finite computer searches, or numerical evidence for a conjectured constant.
- An estimate with a constant depending on \(n\), \(A\), or a parameter tending to infinity.
- A proof sketch that turns pointwise positivity into a uniform positive infimum without compactness or a quantitative lower bound.
- A Lean encoding that leaves `sorry`, introduces an axiom equivalent to the target, or formalizes a weakened statement.

## Required correctness checks

1. Verify the exact quantifier order: \(\exists c>0\ \forall n,N,A\), with \(c\) absolute.
2. Verify that all subset pairs are covered, including the empty subset and pairs of different cardinalities.
3. In a signed-sum formulation, prove the exact equivalence between a collision and a nontrivial \(\{-1,0,1\}\)-relation.
4. In any probabilistic proof, retain lattice spacing, parity, normalization, and all error terms.
5. In any Fourier or circle-method proof, specify arc ranges, overlap/disjointness, minor-arc control, and uniform dependence on \(A\) and \(n\).
6. In any compactness, infimum, or limiting argument, prove the needed uniform quantitative step rather than inferring it from positivity for each individual set.
7. In any computational contribution, require a precise lemma, hypotheses, machine-checkable certificate format, and a finite stopping condition before running it.

## Required deliverables

- `research_state.md`: dated source ledger, definitions, theorem/conjecture separation, approach registry, attempted lemmas, proof dependencies, and unresolved blockers.
- A literature memo with direct URLs, publication status, and a separate log for rejected solution claims.
- A self-contained proof manuscript or counterexample manuscript, with every nonstandard lemma proved or cited to a stable primary source.
- An adversarial proof-audit report that identifies every uniformity, quantifier, asymptotic, and collision check.
- If any computation is used, code, exact input/output specification, certificate/verifier, and a statement of the lemma that the computation establishes.
- If formalization is attempted, the source, compiler version, final theorem statement, dependency/axiom audit, and confirmation of no placeholders.

## Dynamic Multiagent v2 protocol

Create a research root containing `research_state.md`, `approach_registry.md`, `sources.md`, `proofs/`, and `audits/`. Use at most four concurrent agents total.

Start with an early exploration wave that keeps approaches independent. Each agent must first register a one-paragraph conjectured mechanism, its precise target lemma, dependencies, and a falsification test in `approach_registry.md`; do not merge approaches merely because they share terminology.

The coordinator dynamically assigns and reassigns slots based on evidence, not a fixed role list. At each wave boundary:

- preserve only approaches with a stated lemma and a checkable next implication;
- assign one independent adversarial reviewer to every candidate central lemma;
- close or downgrade paths whose key step is circular, non-uniform, or already known to yield only the \(\sqrt n\)-loss bound;
- reuse freed slots for a genuinely different line of attack, source verification, or proof audit;
- record failed approaches with the exact failure point so they are not silently retried.

Run multiple waves. Later waves may combine two validated lemmas only after checking their assumptions are compatible. No agent may claim resolution until another agent has audited the canonical target, quantifiers, collision condition, and every cited external theorem.

Proof-first allocation rule: computation may occupy at most one optional slot. Before computation begins, declare in the registry the exact lemma or counterexample predicate, hypotheses, certificate, and stopping condition. Release that slot immediately once the bounded question is answered; computation must never substitute for the asymptotic proof.

## Persistence and resumability

Update `research_state.md` after each substantive result, failed proof, source check, and review. Include the current canonical target, active assumptions, dependency graph, citations, agent status, and the next smallest verifiable task.

If a runtime boundary interrupts the investigation before a complete affirmative proof or complete counterexample is verified, do not present a solution. Write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, record the exact proof gap or rejected step, preserve all certificates and audit findings, and resume from the smallest unresolved check in a later wave.
