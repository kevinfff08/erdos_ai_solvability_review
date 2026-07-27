# Erdős Problem 18 — repaired primary target

## Definitions and canonical target

For a positive integer \(m\), let \(\operatorname{Div}(m)\) be its set of positive divisors. Call \(m\) *practical* if every integer \(t\) with \(1\le t<m\) is a sum of distinct members of \(\operatorname{Div}(m)\).

For practical \(m\), define
\[
r_m(t)=\min\{ |A|: A\subseteq\operatorname{Div}(m),\ \sum_{d\in A}d=t\},\qquad
h(m)=\max_{1\le t<m} r_m(t).
\]
The set \(A\) may depend on \(t\). All logarithms are natural.

Resolve this repaired primary target:
\[
\exists C>0\ \exists^\infty\text{ practical }m\quad h(m)<(\log\log m)^C.
\]
The historical unqualified formulation is not the target: Erdős set \(S(n)=0\) for non-practical \(n\), making an unqualified infinitude statement trivial. The current database explicitly repairs the quantification to practical \(m\).

The questions \(h(n!)=n^{o(1)}\) and \(h(n!)<(\log n)^{O(1)}\) are separate variants. Do not report either as resolving the primary target. The latter would imply the former.

## Accepted background

- Erdős defined the historical function \(S(n)\), noted \(S(n!)<n\), and offered $250 for the polylogarithmic-in-\(\log n\) infinitude question; inspect p. 172 of [Erdős 1981](https://renyi.hu/~p_erdos/1981-33.pdf). The historical zero convention is a statement defect, not a shortcut.
- The current [Erdős Problems record](https://www.erdosproblems.com/18) labels the repaired problem open and attributes to Vose the weaker existence result \(h(m)\ll(\log m)^{1/2}\) for infinitely many practical \(m\).
- [Vose 1985](https://academic.oup.com/blms/article-abstract/17/1/21/296830) is the cited primary paper; inspect its proof before relying on any detailed reconstruction.
- The current [forum thread](https://www.erdosproblems.com/forum/thread/18) records the ambiguity and its repair. Forum discussion is context, not a proof source.
- The [Formal Conjectures file](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/18.lean) supplies a useful max–min formalization of \(h\), but its research assertions contain `sorry`; it is not a formal proof of any open claim.

## Complete resolutions

An affirmative resolution must prove one fixed \(C>0\) and an infinite family of practical integers \(m\) for which every \(1\le t<m\) has a distinct-divisor representation using fewer than \((\log\log m)^C\) terms.

A negative resolution must prove that for every \(C>0\), only finitely many practical \(m\) satisfy that bound.

Both directions require a fully auditable proof and a precise treatment of the fixed exponent and the sufficiently-large range where \(\log\log m\) is positive.

## What does not count as a solution

- Exploiting \(S(n)=0\) for non-practical \(n\), or omitting the practicalness condition.
- A finite computation, a heuristic, numerical fit, or a family whose infinitude is unproved.
- Short representations for many targets but not the worst target \(t\).
- A bound with an exponent depending on \(m\), such as \((\log\log m)^{C(m)}\).
- An Egyptian-fraction result with variable denominators that does not use distinct divisors of one fixed \(m\).
- A proof only about \(n!\), unless it explicitly establishes the repaired primary target.

## Required correctness checks

1. State and use the order \(\max_t\min_A |A|\) correctly.
2. For every construction, verify practicalness and verify that all summands are distinct divisors of the same \(m\).
3. Ensure the representing subset may vary with \(t\), but that the term-count upper bound is uniform in \(t\).
4. Track every constant: the final exponent \(C\) must be independent of \(m\).
5. Prove infinitude of the family, not merely existence at sampled parameters.
6. Compare any claimed improvement honestly with Vose's \((\log m)^{1/2}\) scale.
7. If using a historical statement, first reconcile \(<m\) versus \(\le m\), and the convention for non-practical inputs.
8. Subject any claimed proof to an independent adversarial check that seeks a target \(t\) lacking the asserted representation and checks all asymptotic quantifiers.

## Required deliverables

- A `research_state.md` containing the exact target, source URLs, a claim ledger, attempted lemmas, counterexamples, and current unresolved dependencies.
- A self-contained proof or disproof manuscript with definitions, theorem statements, and all dependencies identified.
- A representation-verification appendix for every constructed family, including the uniform worst-case argument.
- A literature note that distinguishes inspected primary results from database summaries and informal forum observations.
- If incomplete, a precise list of proved lemmas, failed routes, and the first unproved implication; do not present it as a resolution.

## Dynamic Multiagent v2 protocol

Use one research root and at most four concurrent agents. Begin with independent approaches rather than assigning a fixed mathematical method: one may audit constructions, another seek structural divisor-sum lemmas, another analyze the historical/Vose literature, and another adversarially test definitions. Record every approach in an approach registry in `research_state.md` with its hypothesis, target lemma, evidence, status, and reason for abandonment or continuation.

Run multiple waves. After each wave, the root compares approaches, merges only verified claims, and dynamically reuses freed slots for the sharpest unresolved lemma or independent proof checking. At least one active slot in every proof-producing wave must act as an adversarial auditor. No agent may convert a conjectural lemma, an uninspected citation, or a computation into an accepted fact.

Allocate proof work first. At most one optional computational subtask may run at once, and only after declaring in `research_state.md`: the exact lemma or candidate construction it tests, all hypotheses, the finite search domain, what output would distinguish the alternatives, and the stopping condition. Stop and reassign that slot immediately once the stated question is answered.

## Persistence and resumability

Update `research_state.md` at each honest boundary: source checked, lemma proved, counterexample found, or route blocked. Preserve exact citations and proof obligations so a later wave can resume without trusting narrative summaries.

If a runtime boundary occurs before a complete affirmative or negative proof has passed adversarial review, end the current report with `CHECKPOINT_NOT_FINAL`, identify the next concrete proof obligation, and retain all failed-route evidence. Never relabel an incomplete investigation as a solution.
