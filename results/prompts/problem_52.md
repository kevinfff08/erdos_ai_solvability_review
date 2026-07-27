# Erdős Problem 52 — integer sum-product conjecture

## Definitions and canonical target

Let A be a finite nonempty subset of Z. Define

- A+A = {a+b : a,b∈A};
- AA = {ab : a,b∈A}.

Resolve the following integer-domain statement:

For every ε∈(0,1), there is cε>0 such that every finite nonempty A⊆Z satisfies

max(|A+A|,|AA|) ≥ cε |A|^(2−ε).

The constant cε may depend on ε only, not on A, |A|, the height of elements, or any auxiliary parameter. This is equivalent to a lower bound |A|^(2−o(1)).

The only target is A⊆Z. Do not silently replace it by subsets of R, C, a number field, a finite field, or a restricted class of integers.

## Accepted background

- Erdős and Szemerédi established a nontrivial |A|^(1+c) lower bound and constructed integer examples with a subpolynomial saving from |A|²: [On sums and products of integers (1983)](https://users.renyi.hu/~p_erdos/1983-16.pdf).
- The current verified record relevant to arbitrary integer sets follows from the real theorem of Adam Cushman: for finite A⊆R, max(|A+A|,|AA|) is at least |A|^(4/3+10/4407−ε), hence at least |A|^(1962/1469−ε). See [arXiv:2512.13849](https://arxiv.org/abs/2512.13849). This is a theorem claimed in a preprint, not a resolution of the conjecture.
- Bloom's earlier control framework and exponent are background, not a prescribed method: [arXiv:2501.09470](https://arxiv.org/abs/2501.09470).
- Stronger exponents are known only under extra integer hypotheses, such as few prime factors: [Hanson–Rudnev–Shkredov–Zhelezov](https://arxiv.org/abs/2305.04038) and [Bloom](https://arxiv.org/abs/2512.04931). Such hypotheses are not part of the target.
- The real version was disproved in 2026 by sets of algebraic integers in growing-degree number fields: [Bloom–Sawin–Schildkraut–Zhelezov](https://arxiv.org/abs/2605.28781). This does not disprove the integer statement. The author explanation explicitly says the integer case remains open: [Sum-product, unit distances, and number fields](https://www.erdosproblems.com/forum/thread/blog%3A6).
- The official current record is [Erdős Problems #52](https://www.erdosproblems.com/52). A Lean formalization of the statement exists at [FormalConjectures/ErdosProblems/52.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/52.lean), but it contains `sorry` and is not a proof.

## Complete resolutions

An affirmative resolution must prove the canonical statement for every ε∈(0,1), with cε uniform over all finite A⊆Z.

A negative resolution must prove the logical negation. A sufficient concrete certificate is constants C,δ>0 and arbitrarily large finite A⊆Z such that

max(|A+A|,|AA|) ≤ C|A|^(2−δ).

Every resolution must identify the exact theorem proved, all ambient domains, all parameter dependencies, and a complete citation trail for external inputs.

## What does not count as a solution

- A better fixed lower-bound exponent below 2.
- A theorem or counterexample over R, C, a number field, p-adics, function fields, or finite fields.
- A theorem for positive integers, smooth numbers, bounded-prime-factor sets, or another restricted subclass without removing that restriction.
- Finite computation, numerical evidence, or an arbitrary constant-factor improvement over |A|².
- A family whose exponent saving tends to zero, unless it is rigorously converted to a fixed δ>0.
- A proof sketch with unproved structural claims, an appeal to a named theorem without checking its hypotheses, or a Lean file with `sorry`, `admit`, or untrusted axioms.

## Required correctness checks

1. State and check the quantifier order: ε first, then cε, then every finite integer set A.
2. Keep all constants independent of the cardinality, height, rank, field degree, and construction parameters of A.
3. Count distinct elements of A+A and AA, not representations or ordered pairs.
4. For any proposed counterexample, prove both unbounded |A| and a fixed positive power saving.
5. For any attempted transfer from a number field, prove that it remains a subset of Z and that sum/product collision estimates survive the transfer; a coordinate or norm map alone is not enough.
6. Verify every use of incidence, energy, inverse, or arithmetic theorem against its exact domain and hypotheses.
7. If formal verification is attempted, pin dependencies, eliminate all placeholders, and build the whole Lean artifact with the kernel.

## Required deliverables

- A concise `status.md` distinguishing proved statements, conjectures, failed routes, and open gaps.
- A self-contained proof manuscript or counterexample manuscript, with numbered lemmas and explicit constants/dependencies.
- A source ledger linking each imported result to a primary source and recording its exact usable statement.
- An adversarial audit report that attempts to falsify the main claim through quantifier, domain-transfer, asymptotic, and collision-count checks.
- If incomplete, a precise list of proved lemmas, the first unresolved lemma, and why resolving it would advance or close the target.
- If a formal artifact is produced, a reproducible verifier command and pinned revision.

## Dynamic Multiagent v2 protocol

Create a research root containing `research_state.md`, an approach registry, source ledger, proof drafts, and audit reports. Use at most four concurrent agents total.

Begin with independent exploration waves rather than a fixed assignment: register each approach before substantial work, including its claimed target lemma, domain, dependencies, predicted failure mode, and what outcome would make it noncompetitive. Preserve incompatible approaches until evidence rules them out.

Use dynamic slot reuse. After each short wave, the root compares registered approaches by proof progress, rigor, and relevance to the canonical integer target; stop duplicated or domain-mismatched work and reassign freed capacity to the strongest unresolved lemma or to adversarial checking. Run multiple waves, with a separate adversarial proof-check pass whenever a main lemma or construction appears complete.

Proof-first allocation is mandatory. At most one optional computational subtask may run at once. Before it starts, record its exact lemma or candidate family, hypotheses, finite search space or certificate format, stopping condition, and the proof decision it will inform. End and reassign that slot immediately once the question is answered. Computation may test or certify a local claim; it may not stand in for an asymptotic argument.

## Persistence and resumability

Update `research_state.md` after every wave with the canonical target, source versions, active approach registry, proved lemmas, failed claims, unverified dependencies, next proof obligations, and any computation's declared stopping condition.

If interrupted before a complete affirmative proof or complete integer counterexample has been independently audited, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`. Preserve all partial proofs and counterexample attempts with their exact gap locations. Do not report a resolution merely because a real-domain result, a conditional theorem, a numerical pattern, or a formalized statement has been found.
