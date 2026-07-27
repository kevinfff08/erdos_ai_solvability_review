# Verification audit: Erdős Problem 90 (unit-distance conjecture)

## Definitions and canonical target

For a finite set \(P\subset\mathbb R^2\), let
\[
\nu(P)=\#\{\{x,y\}\subset P:\|x-y\|_2=1\}.
\]
For \(n\ge 1\), let \(u(n)=\max_{|P|=n}\nu(P)\). Pairs are unordered distinct pairs.

The historical target was the assertion that there exist constants \(C>0\) and \(N\) such that, for every integer \(n\ge N\),
\[
u(n)\le n^{1+C/\log\log n}.
\]
This is the precise meaning of \(u(n)\le n^{1+O(1/\log\log n)}\). The logarithm base is immaterial after changing \(C\).

This is a proof-verification task, not an open-problem-solving task. Verify the claimed disproof: establish, or locate a fatal gap in the claim, that some fixed \(\varepsilon>0\) and a sequence \(P_i\subset\mathbb R^2\) with \(|P_i|\to\infty\) satisfy
\[
\nu(P_i)\ge |P_i|^{1+\varepsilon}.
\]
Then prove explicitly that this contradicts the historical target.

## Accepted background

- Spencer, Szemerédi, and Trotter's 1984 result is the classical general upper bound \(u(n)=O(n^{4/3})\); the 2026 proof documents restate this as the best known general Euclidean upper bound.
- [Planar Point Sets with Many Unit Distances](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf) states the qualitative counterexample theorem: \(u(n)\ge n^{1+\delta}\) for infinitely many \(n\), for fixed \(\delta>0\).
- [Remarks on the disproof of the unit distance conjecture](https://arxiv.org/abs/2605.20695) is the multi-author human-digested and human-verified preprint. Its Theorem 1.1 gives the qualitative result and presents a complete proof through geometry-of-numbers and number-field lemmas.
- [An explicit lower bound for the unit distance problem](https://arxiv.org/abs/2605.20579) gives a one-author explicit refinement, with exponent \(1.014114\) up to an absolute multiplicative constant for arbitrarily large \(n\).
- [Many unit distances requires many directions](https://arxiv.org/abs/2504.04208) is relevant structural background, but it neither proves nor disproves the historical conjecture by itself.
- Treat the later numerical-exponent claims on [MathOverflow](https://mathoverflow.net/questions/511514/what-is-the-unit-distance-exponent?noredirect=1) and the unreviewed [certificate-optimization preprint](https://arxiv.org/abs/2606.03419) as leads only unless their full hypotheses, certificates, and proofs are independently checked.

Do not assume that a paper's authorship, an announcement, or a formalization page alone proves all load-bearing lemmas. Conversely, do not dismiss the claimed disproof merely because it is recent: inspect the proof and its logical quantifiers.

## Complete resolutions

A successful verification report must reach exactly one of these decisive outcomes.

1. **Verified disproof.** Supply a rigorous dependency audit establishing a fixed \(\varepsilon>0\), an unbounded sequence of finite Euclidean planar point sets, and the displayed lower bound. Give the short quantified contradiction: for a proposed \(C\), choose \(i\) with \(\log\log|P_i|>C/\varepsilon\) (with harmless slack for any multiplicative lower-bound constant). Thus the historical eventual upper bound fails.
2. **Closure not verified.** Identify a specific fatal gap or unproved premise in the current counterexample chain, explain precisely why it prevents a fixed-positive-exponent lower bound on an unbounded sequence, and state whether the original conjecture consequently remains unclassified. A vague concern about novelty, AI involvement, or lack of journal publication is not enough.

## What does not count as a solution

- A finite configuration, numerical search, or fitted exponent without an asymptotic theorem.
- A lower bound \(n^{1+c/\log\log n}\), which is compatible with the conjecture.
- A proof for another norm, for generic norms, or for a restricted family of point sets.
- Treating ordered and unordered pairs interchangeably without accounting for the factor two.
- Assuming a sequence indexed by field degree automatically yields valid unbounded integer cardinalities without proving the cardinalities tend to infinity.
- Reporting an improved \(\varepsilon\) from a forum post or program without checking every certificate condition and the reduction from the certificate to planar point sets.
- Rebranding the still-open question of the true asymptotic order of \(u(n)\) as a proof of the already-false historical assertion.

## Required correctness checks

- Write the original \(O\)-notation with its \(\exists C\exists N\forall n\) quantifiers.
- Check that \(\varepsilon\) is a fixed positive constant, not a parameter tending to zero with \(n\).
- Check the exact pair-count convention at every transition.
- If using the Sawin form \(u(n)\ge n^{1.014114}/C_0\), justify the passage to \(u(n)\ge n^{1+\varepsilon}\) for a fixed \(\varepsilon>0\) on an unbounded sequence.
- Audit the geometry-of-numbers reduction: lattice separation, covolume bound, unit-vector count, bounded-window count, and injectivity of the selected complex-coordinate projection.
- Audit the arithmetic reduction: CM-field conjugation, class-group pigeonhole step, denominator and class-number losses, root-discriminant control, prescribed prime splitting, and the proof that the relevant pro-p/class-field tower is infinite.
- Separate standard cited theorems from new deductions, and state every external theorem in the exact strength used.
- If Lean or another proof assistant is used, report all axioms, `sorry`/admitted declarations, opaque imports, and non-computational assumptions. A compiled theorem with extra axioms is not an unconditional independent verification.

## Required deliverables

1. A self-contained status verdict: `verified disproof` or `closure not verified`.
2. A dependency graph from the target lower bound back to external theorems and explicitly checked lemmas.
3. A quantifier audit of both the original conjecture and the claimed counterexample.
4. A lemma-by-lemma proof-check table: statement, source location, assumptions, verification result, and any gap.
5. A short formal contradiction from the verified lower bound to \(n^{1+O(1/\log\log n)}\).
6. A bibliography with direct URLs, publication/preprint status, dates, and a label for each source as theorem, conjecture, or informal claim.
7. If using computation, the precise lemma, input data, deterministic verifier, complete output, and stopping condition. Do not use computation merely to search for attractive exponents.
8. A final distinction between the closed historical conjecture and any separately stated open residual problem about the true order of \(u(n)\).

## Dynamic Multiagent v2 protocol

Create a research root containing `research_state.md`, an approach registry, a source ledger, and an evidence folder. Use at most four concurrent agents total.

In the first wave, split by independent evidential approaches rather than by a fixed mathematical recipe: at least one route should audit the quantified logical contradiction, one should inspect the human-digested proof chain, and one should independently inspect the explicit Sawin refinement and formalization claims. Register each route before substantial work: target claim, dependencies, falsification condition, source locations, and current confidence.

After each result, dynamically reuse slots. Merge duplicated routes, assign an adversarial checker to every apparently complete proof chain, and redirect freed capacity toward the highest-risk unchecked lemma. Do not preserve assignments merely because they were initial assignments. Run multiple waves until every load-bearing dependency is verified, refuted, or explicitly marked unresolved.

The adversarial checker must attempt concrete failures: reversed quantifiers, loss of a fixed exponent, accidental use of ordered pairs, noninjective projection, finite rather than unbounded cardinalities, uncontrolled constants, invalid use of a class-number/root-discriminant estimate, and dependence on an unproved formal axiom.

Proof-first allocation is mandatory. At most one optional computational subtask may run at any time. Before it starts, record the exact finite lemma to test, all hypotheses, accepted input encoding, deterministic verification command, and a stopping condition that answers the lemma. Once answered, immediately reassign that slot to proof checking; do not continue numerical optimization.

## Persistence and resumability

Maintain `research_state.md` after every wave. It must record the canonical target, source URLs and access dates, dependency graph, approach registry, checked lemmas, unresolved objections, commands and outputs for any computation, and the next highest-priority verification action.

If a runtime boundary interrupts work before a decisive audit outcome, save the state and return `CHECKPOINT_NOT_FINAL` with the exact unresolved lemma or source dependency. Do not present a provisional closure verdict as final. Resume from the recorded registry and prioritize independent adversarial checking of the current strongest claimed proof.
