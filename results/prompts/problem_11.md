# Erdős Problem 11 — proof-first investigation

## Definitions and canonical target

A positive integer \(s\) is squarefree if no prime square divides \(s\). A power of two in the primary computational convention is \(2^k\) with \(k\in\mathbb Z_{\ge1}\).

Prove or disprove the literal current-page target:
\[
\exists N\ \forall\text{ odd }n\ge N\ \exists k\ge1:\quad 2^k<n\quad\text{and}\quad n-2^k\text{ is squarefree}.
\]
Equivalently, every sufficiently large odd \(n\) is \(s+2^k\) with \(s\) positive and squarefree.

Do not silently replace this target by the stronger historical statement “every odd \(n>1\),” by a \(k=0\) convention, by the \(4\nmid n\) variant, or by a two-powers variant. Any work on one of those must state and prove its implication to the canonical target.

## Accepted background

- The [Erdős Problems record](https://www.erdosproblems.com/11), updated 2026-04-05, lists the target as open. Its [forum thread](https://www.erdosproblems.com/forum/thread/11) contains an explicit 2026 rejection of an attempted reduction from \(\sum_p1/\operatorname{ord}_{p^2}(2)<\infty\) to the full conjecture.
- Christian Hercher, [*On the Sum of a Squarefree Integer and a Power of Two*](https://cs.uwaterloo.ca/journals/JIS/VOL28/Hercher2/hercher24.html), *Journal of Integer Sequences* 28 (2025), Article 25.3.1, proves a finite computational verification for all odd \(n\le2^{50}\). It is not an asymptotic proof.
- Granville and Soundararajan, [*A Binary Additive Problem of Erdős and the Order of 2 mod \(p^2\)*](https://link.springer.com/article/10.1023/A%3A1009786614584), *Ramanujan Journal* 2 (1998), 283–298, are the primary source for the order-mod-\(p^2\), Wieferich, and covering-system background. Obtain and inspect the full text before citing theorem content; record theorem number, hypotheses, and conclusion exactly.
- The [Formal Conjectures file](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/11.lean) contains only `sorry` declarations and is not a proof.

Classify every imported fact in the theorem ledger as: fully proved in this project; verified primary theorem; conditional theorem; finite computation; or heuristic. Do not rely on an informal forum post as a theorem.

## Complete resolutions

An affirmative resolution is a complete proof of an \(N\) such that every odd \(n\ge N\) has a \(k\ge1\) for which \(n-2^k\) is positive and squarefree.

A negative resolution is a proof of arbitrarily large odd \(n\) such that every \(n-2^k\), for \(k\ge1\) with \(2^k<n\), is non-squarefree. A certified unbounded family of such \(n\) disproves the eventual statement.

## What does not count as a solution

- Checking any finite interval, regardless of size.
- Establishing the claim for almost all odd integers, positive density, or a heuristic probability model.
- A representation with \(k=0\), two powers of two, or a different divisibility domain without a proved reduction.
- A conditional result whose assumptions are not proved.
- A CRT construction that covers only finitely many exponent classes or fails to prove positivity of \(n-2^k\).
- A theorem attribution to Granville–Soundararajan based only on a database summary, an unproved Lean comment, or a forum paraphrase.

## Required correctness checks

1. State all quantifiers and all uniformity ranges in every lemma.
2. For every candidate \(k\), verify \(1\le k<\log_2 n\), positivity of \(n-2^k\), and squarefreeness against every prime square.
3. For a congruence-cover construction, prove that it covers every relevant exponent, including the use of exact periods \(\operatorname{ord}_{p^2}(2)\) and CRT compatibility.
4. Never pass from density-one or expected representation count to universal coverage without an explicit theorem controlling all exceptions.
5. Treat dependencies among \(p^2\mid n-2^k\) exactly; independence may be used only as a labelled heuristic.
6. Verify any Wieferich-related theorem directly from the 1998 paper. Record and resolve the conflict between secondary summaries before using it.
7. Require an adversarial independent reconstruction of every decisive lemma, focused on missed exponent classes, incorrect order computations, non-coprime moduli, and hidden unproved assumptions.

## Required deliverables

- `research_state.md` containing the target, date-stamped source log, theorem ledger, approach registry, proof dependencies, and current status.
- A proof or disproof manuscript with every nontrivial assertion proved or pinpoint-cited to a verified primary source.
- `audit.md` mapping claims to proof lines or source pages, including rejected arguments and all use of computation.
- If computation is authorized: source code, exact inputs, output certificate, independent checker, environment details, and a proof that the finite computation establishes its stated lemma.
- A final status line exactly equal to `RESOLVED_AFFIRMATIVE`, `RESOLVED_NEGATIVE`, or `CHECKPOINT_NOT_FINAL`.

## Dynamic Multiagent v2 protocol

Use one research root and at most four concurrent agents. Start with independent proof-first explorations, not a fixed method or permanent role assignment. Before substantive work, each route enters an approach registry with: its precise target lemma, dependencies, falsification criterion, and whether it bears on the affirmative or negative direction.

Work in multiple waves. Early waves should be mathematically incompatible where possible: exact primary-source/theorem extraction, structural analysis of square-divisor coverings, and rigorous infinite-family construction attempts. At each wave boundary, merge only independently checked material into `research_state.md`; retire disproved routes and reuse their slots for the most informative open dependency.

Every claimed decisive proof must be audited by an agent who did not author it. The auditor must independently recompute central congruences and quantifiers and issue either a line-addressed defect report or a validation note. No claim enters the theorem ledger before this review.

Allow at most one optional computational subtask at any time. Before launch, record its exact finite lemma, hypotheses, modulus/range, certificate format, and stopping condition. Stop it immediately when that question is answered and reassign the slot; never extend a search bound merely because no counterexample was found.

## Persistence and resumability

Update `research_state.md` after every source verification, validated lemma, failed route, computation, and wave transition. Preserve commands, hashes, certificates, and proof-review results.

If a runtime boundary arrives before adversarial checking has validated a full affirmative proof or a full unbounded counterexample family, place `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`. State the last verified result, the exact unresolved dependency, and the next falsifiable task. Never present a partial density argument, a finite computation, or an unchecked proof draft as a solution.
