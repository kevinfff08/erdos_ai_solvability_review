# Erdős Problem 120 — research prompt

## Definitions and canonical target

Let \(\lambda\) be Lebesgue measure on \(\mathbb R\).  For \(A\subseteq\mathbb R\) and \(a,b\in\mathbb R\), write
\[
aA+b:=\{ax+b:x\in A\}.
\]
A set \(A\) is *measure universal* if every Lebesgue-measurable \(E\subseteq\mathbb R\) with \(\lambda(E)>0\) contains \(aA+b\) for some \(a\ne0\), \(b\in\mathbb R\).

Canonical target: prove
\[
\forall A\subseteq\mathbb R\;[A\text{ infinite}\Rightarrow \exists E\subseteq\mathbb R\;(E\text{ Lebesgue measurable}\wedge\lambda(E)>0\wedge\forall a,b\in\mathbb R\;(a\ne0\Rightarrow aA+b\not\subseteq E))].
\]
No regularity is assumed on \(A\).  Negative scales are included.  The one set \(E\) may depend on \(A\), but must exclude every nonconstant affine copy simultaneously.

## Accepted background

- The problem is equivalent to saying that no infinite subset of \(\mathbb R\) is measure universal.  Finite sets are measure universal by the density-point argument; see [Jung–Lai–Mooroogen, 2025](https://arxiv.org/abs/2412.11062).
- It is enough to settle the residual class of strictly decreasing sequences tending to zero after standard reductions; unbounded sets and sets dense in an interval are already non-universal.  See the [current problem record](https://www.erdosproblems.com/120) and the 2025 survey.
- Falconer (1984) and Eigen (1985) proved non-universality for sublacunary sequences \(a_{n+1}/a_n\to1\); this is background, not the general theorem.  The geometric sequence \(\{2^{-n}\}\) remains an explicit open case in the 2025 survey.
- [Shmerkin–Yavicoli, *Advances in Mathematics* 2026](https://www.sciencedirect.com/science/article/pii/S0001870826002008) prove non-full-measure-universality, hence the original conclusion, for Borel sets satisfying \(\dim_H^{\log}>1\) or \(\dim_P^{\log}>2\).  Their weaker all-Cantor-set statement is not by itself a resolution of the original problem.
- [Iosevich–Yavicoli, 2026 preprint](https://arxiv.org/abs/2604.01493) prove the conclusion for further very thin Falconer-lattice/Cantor-type families, using additive branching and Bourgain's triple-sum theorem; they explicitly leave general rapid decay open.
- [Mora Cuellar et al., 2026 preprint](https://arxiv.org/abs/2607.03584) prove non-universality for specified sumsets and difference sets, including \(\{2^{-n}\}\pm B\) for every infinite \(B\).  This does not settle \(\{2^{-n}\}\) alone.
- Treat [Cruz–Lai–Pramanik 2020](https://arxiv.org/abs/2001.02395) only as an unverified historical claim, not accepted background: later work by the same authors [states the conjecture remains open](https://arxiv.org/abs/2204.12720).

## Complete resolutions

An affirmative resolution is a rigorous proof of the canonical target for every infinite \(A\subseteq\mathbb R\), including genuine lacunary sequences such as \(\{2^{-n}\}\).

A negative resolution is a concrete infinite \(A\subseteq\mathbb R\) plus a proof that every measurable positive-measure \(E\) contains \(aA+b\) for some \(a\ne0,b\in\mathbb R\).

## What does not count as a solution

- A proof for only a dimension class, decay class, Cantor family, sumset/difference-set family, or finite truncation.
- A null, residual, full-Hausdorff-dimension, or parameter-almost-everywhere avoidance result without a positive-measure avoiding set satisfying the canonical quantifiers.
- A proof of a topological, bi-Lipschitz, full-measure, or “in the large” variant unless it includes a checked implication to the target.
- An argument that chooses \(E\) after choosing \(a\) or \(b\), or that excludes only a finite subset of \(A\).
- Numerical evidence, finite-grid experiments without a proved lifting lemma, or reliance on an uninspected preprint claim.

## Required correctness checks

1. Write the quantifier order explicitly at the start and end of every candidate proof.
2. Verify \(E\) is Lebesgue measurable and \(\lambda(E)>0\), rather than merely non-null in an informal or finite-stage sense.
3. Verify exclusion of all \(a\ne0\), both signs, and all \(b\), for the entire infinite pattern.
4. If reducing from \(A\) to a subset \(B\subseteq A\), check the inclusion direction: an \(E\) avoiding \(B\) also avoids \(A\).
5. For any sumset or full-measure theorem, reproduce its exact hypotheses, class of maps, and the deduction to a positive-measure avoiding set.
6. Stress-test any alleged general proof on \(A=\{2^{-n}:n\ge1\}\) and explain precisely why it escapes all known obstructions.
7. Maintain a claim ledger distinguishing theorem, conjecture, transparent deduction, and unverified assertion; cite each nontrivial external theorem with a stable URL and publication status.

## Required deliverables

- A concise problem restatement and a status/literature ledger with direct source links.
- An approach registry listing each attempted route, its exact intermediate proposition, dependencies, status, and failure mode.
- For each promising route, a complete lemma chain with all hypotheses and a proof or a precisely isolated gap.
- An adversarial audit of any candidate proof, including the seven checks above.
- A final conclusion labeled exactly `RESOLVED_AFFIRMATIVE`, `RESOLVED_NEGATIVE`, or `CHECKPOINT_NOT_FINAL`; only the first two may claim resolution.
- If unresolved, a rigorous partial-results report that states neither a solution nor progress beyond what is actually proved.

## Dynamic Multiagent v2 protocol

Set a research root responsible for the canonical target, the claim ledger, source verification, and merge decisions.  Permit at most four concurrent agents including the root.

Begin with independent exploration waves rather than fixed roles.  Before substantial work, each active agent registers in the approach registry: target lemma, compatibility with the exact quantifiers, prerequisites, expected falsifiers, and whether the route overlaps a registered approach.  Prefer materially incompatible approaches early.

After each wave, the root compares outputs, retires routes with a proved obstruction, and dynamically reuses freed slots for the sharpest unresolved lemma, a literature/source check, or an adversarial proof audit.  Run multiple waves; no agent owns a route permanently.  Any candidate complete proof must be checked by an agent who did not develop it, then by a second audit focused on quantifier order, measure theory, and the \(\{2^{-n}\}\) test case.

Allocate resources proof-first.  At most one optional computational subtask may run at any time.  Before it starts, record the exact lemma or conjectured obstruction it probes, finite hypotheses, certificate format, and a stopping condition that decides when the answer is informative.  End and reassign that slot immediately once the declared question is answered; computation may not substitute for a proof of an infinite assertion.

## Persistence and resumability

Use `research_state.md` as the single checkpoint: canonical target, verified sources, approach registry, proved lemmas, rejected claims, active dependencies, and the next smallest proof obligation.  Update it at the end of every wave and before handoff.

If a runtime boundary interrupts an incomplete investigation, do not write a solution-like conclusion.  Preserve the state and return `CHECKPOINT_NOT_FINAL` with the exact unproved lemma, evidence reviewed, and the next verification action.
