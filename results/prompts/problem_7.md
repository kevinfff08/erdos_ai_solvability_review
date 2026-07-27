# Erdős Problem 7: odd distinct covering systems

## Definitions and canonical target

A **covering system** is a finite nonempty family of congruences
\[
 a_i \pmod {n_i}\qquad (i=1,\ldots,k)
\]
with integers \(n_i>1\), such that for every \(x\in\mathbb Z\), at least one \(i\) satisfies \(x\equiv a_i\pmod {n_i}\). It is **distinct** when \(n_i\ne n_j\) for \(i\ne j\). It is an **odd distinct covering system** when every \(n_i\) is odd.

Canonical target: determine whether an odd distinct covering system exists.

Equivalent finite formulation for a proposed construction: set \(L=\operatorname{lcm}(n_1,\ldots,n_k)\). The family covers \(\mathbb Z\) if and only if it covers every residue class in \(\mathbb Z/L\mathbb Z\).

Boundary conventions are mandatory: the family must be finite; every modulus must exceed 1; moduli, not merely residue classes, must be pairwise distinct; no disjointness or exact-cover condition is assumed. If modulus 1 were allowed, \(0\pmod 1\) would make the question trivial, so it is excluded.

## Accepted background

- Hough and Nielsen proved that every distinct covering system has a modulus divisible by 2 or 3: [arXiv:1703.02133](https://arxiv.org/abs/1703.02133), published in *Duke Mathematical Journal* 168 (2019), 3261–3295. Thus an odd candidate must contain a modulus divisible by 3.
- Balister, Bollobás, Morris, Sahasrabudhe, and Tiba proved that a finite distinct covering with square-free moduli has an even modulus: [arXiv:1901.11465](https://arxiv.org/abs/1901.11465), *Algebra & Number Theory* 15 (2021), 609–626. This proves only the square-free strengthening, not the canonical target.
- Their sieve/probabilistic-measure framework and further progress are in [arXiv:1811.03547](https://arxiv.org/abs/1811.03547), *Inventiones Mathematicae* 228 (2022), 377–414; a later overview is Balister’s [2024 survey](https://doi.org/10.1017/9781009490559.003).
- A 2025 preprint / 2026 *Discrete Mathematics* paper studies a different variant in which one odd modulus may repeat and explicitly describes the original odd-covering problem as open: [arXiv:2507.16135](https://arxiv.org/abs/2507.16135).
- The elementary necessary condition \(\sigma(L)\ge2L\) for the LCM \(L\) is useful but not decisive; see the transparent discussion at [MathOverflow](https://mathoverflow.net/questions/74644/on-integer-covering-systems-with-all-moduli-distinct).

Treat the above as theorems only to the extent stated. In particular, do not infer the general result from the square-free theorem. A 2026 candidate Lean proof is not accepted: its source declares a key `HoughNielsenGoodFibre` as an axiom ([source](https://raw.githubusercontent.com/spicylemonade/erdos-007/main/main.lean)); the associated forum discussion records a separate failed sieve formalization ([thread](https://www.erdosproblems.com/forum/thread/7?order=newest)).

## Complete resolutions

An affirmative resolution must provide an explicit finite list \((a_i,n_i)\) satisfying all canonical conditions and a rigorous certificate that every class modulo \(L=\operatorname{lcm}(n_i)\) is covered.

A negative resolution must prove that every finite family with pairwise distinct odd \(n_i>1\) has an uncovered integer. The proof may use established theorems, but every reduction must preserve finiteness, coverage, distinctness, and the full non-square-free range.

## What does not count as a solution

- Solving only square-free, primitive, antichain, bounded-prime, bounded-exponent, bounded-LCM, or bounded-cardinality cases.
- Establishing only necessary divisibility, density, reciprocal-sum, or abundance conditions.
- A numerical search without a theorem reducing all possible systems to the searched finite region.
- A repeated-modulus construction, a modulus-1 construction, an infinite covering, or a cover only of a finite interval or density-one set.
- A Lean/Coq/Isabelle artifact with `axiom`, `sorry`, `admit`, unverified external code, or a formal theorem not equivalent to the canonical target.

## Required correctness checks

1. State all quantifiers and prove that every modulus is an odd integer greater than 1 and that all moduli are pairwise distinct.
2. For an affirmative construction, verify coverage of **all** residues modulo the exact LCM. Supply machine-readable residue data or a short symbolic partition argument.
3. For a negative proof, identify every place where square-freeness, bounded exponents, minimality, irredundancy, or a divisibility-antichain condition might have been introduced; prove it is justified or remove it.
4. Audit all uses of Hough–Nielsen and BBMST results against their original statements. Do not substitute a qualitative theorem for a required quantitative sieve bound.
5. For every numerical inequality, give rational/interval bounds, rounding direction, parameter domains, source code, and a reproducible command. A computation is admissible only after its precise lemma, hypotheses, and finite stopping condition are written down.
6. Use adversarial checking: try to construct a small counterexample to each new reduction and independently rederive its key implication.

## Required deliverables

- A concise status memo separating established facts, conjectural ideas, and failed routes.
- A self-contained proof manuscript or explicit construction certificate.
- A dependency ledger listing every external theorem with a direct URL, exact formulation used, and a justification that its hypotheses hold.
- If computation is used, a reproducibility bundle with exact input, source, environment, certificate format, and a verifier independent of the search program.
- A proof-audit report describing attempted falsifications, unresolved gaps, and whether the target is fully resolved.
- If no resolution is reached, an honest `CHECKPOINT_NOT_FINAL` report with the strongest verified lemmas and exact remaining obligations.

## Dynamic Multiagent v2 protocol

Create a research root responsible for the canonical statement, source ledger, approach registry, and final integration. Run at most four agents concurrently.

Begin with independent early waves rather than fixed roles: agents should register mutually incompatible approaches or audit tasks before substantial overlap. The approach registry must record for each entry: target lemma, exact assumptions, relationship to the canonical problem, evidence required, current status, and a falsification test. Merge duplicate work only after comparing these entries.

Use multiple waves and dynamic slot reuse. When an approach reaches a proved lemma, counterexample, or decisive obstruction, immediately reassign its slot to a fresh unresolved obligation. Reserve adversarial proof checking throughout: any claimed reduction, construction, numerical certificate, or formalization must be checked by an agent that did not create it. The research root may stop an approach only after recording why it fails, what it would need to revive, and whether it leaves a reusable lemma.

Proof-first allocation is mandatory. At most one concurrent subtask may be computational. Before that task starts, its owner must declare the exact lemma it will decide, all hypotheses, the search domain, certificate, verifier, and stopping condition. Once that question is answered, release the slot immediately; do not convert it into open-ended experimentation.

## Persistence and resumability

Maintain `research_state.md` at the root with: canonical statement; source URLs and theorem-use ledger; approach registry; proved lemmas; rejected claims; computational certificates and hashes; open proof obligations; and next adversarial checks.

At every meaningful boundary, write a checkpoint that lets a new team resume without trusting conversation memory. If runtime ends before a complete affirmative construction or unconditional impossibility proof has passed independent audit, return `CHECKPOINT_NOT_FINAL`, not language implying resolution.
