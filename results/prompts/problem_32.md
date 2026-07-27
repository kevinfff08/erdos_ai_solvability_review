# Erdős Problem 32 — revised research target

## Definitions and canonical target

Let \(\mathbb N=\{1,2,\ldots\}\), let \(P\) be the positive primes, and set \(A(x)=|A\cap[1,x]|\) for \(A\subseteq\mathbb N\).  Call \(A\) an additive complement to \(P\) if
\[
\exists n_0\ \forall n\ge n_0\ \exists p\in P,\ a\in A:\quad n=p+a.
\]

Investigate the following surviving targets, keeping them separate.

- Q1: Does there exist one fixed additive complement \(A\) with \(A(x)=o((\log x)^2)\)?
- Q2: More strongly, does there exist one fixed additive complement \(A\) with \(A(x)=O(\log x)\)?

Q2 implies Q1.  The historical question whether every such \(A\) has \(\liminf A(x)/\log x>1\) is not an open target: it is implied by Ruzsa's stronger theorem \(\liminf A(x)/\log x\ge e^\gamma\).

## Accepted background

- Erdős proved that a fixed additive complement exists with \(A(x)=O((\log x)^2)\): [primary paper](https://users.renyi.hu/~p_erdos/1954-09.pdf).
- Kolountzakis obtained an almost complement of size \(O(\log x\log\log x)\), where an exceptional set of density zero is allowed: [paper](https://matwbn.icm.edu.pl/ksiazki/aa/aa77/aa7711.pdf).
- Ruzsa proved that for every \(\omega(x)\to\infty\), a density-one complement with \(A(x)=O(\omega(x)\log x)\) exists, and proved the lower bound \(\liminf A(x)/\log x\ge e^\gamma\) under a condition implied by eventual full coverage: [paper](https://matwbn.icm.edu.pl/ksiazki/aa/aa86/aa8638.pdf).
- Dai and Pan's peer-reviewed 2014 paper explicitly distinguishes these results and states that full coverage with \(O(\log x)\) was not known: [journal record and open paper](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/en/publishing-house/journals-and-series/acta-arithmetica/all/162/3/83028/the-additive-complements-of-primes-and-goldbach-s-problem).

Treat these as theorems only to the extent their original proofs are checked.  The conjectural status of Q1/Q2 is not itself a theorem.  Do not treat metadata saying that a statement was formalized as a formal proof unless a reproducible artifact and exact theorem are obtained.

## Complete resolutions

A complete affirmative resolution of Q1 supplies a single fixed \(A\), a proof of eventual pointwise coverage \(P+A\), and a proof that \(A(x)=o((\log x)^2)\) for all sufficiently large real/integer \(x\).  A complete affirmative resolution of Q2 supplies the same coverage and a global eventual \(O(\log x)\) bound.

A complete negative resolution of Q1 proves that every eventual additive complement fails the little-o bound.  A complete negative resolution of Q2 proves that every eventual additive complement fails \(O(\log x)\); it may still leave Q1 open.  A proof of Q2 resolves both Q1 and Q2 affirmatively; a negative result for Q1 resolves both negatively.

## What does not count as a solution

- Density-one, lower-density-one, or “almost all integers” coverage.
- A set depending on the cutoff, an integer \(n\), a probability outcome not shown to work simultaneously, or a finite computation.
- A representation \(n=p+a_1+a_2\) with two elements of a sparse set.
- A bound established only on a subsequence of \(x\), or a per-block estimate without a bound for the cumulative set.
- Reproving Erdős's \(O((\log x)^2)\) construction, Ruzsa's \(e^\gamma\) lower bound, or the elementary \(\Omega(\log x)\) lower bound.
- A claimed formalization without a pinned, executable verifier that checks the exact target and dependencies.

## Required correctness checks

1. State all quantifiers, constants, and thresholds.  In particular, \(A\) and every implied constant must be fixed independently of represented \(n\).
2. For any construction, prove coverage for every \(n\ge n_0\), not merely in expectation, in density, or in a prescribed interval.
3. Audit scale gluing: prove the union remains one fixed set and derive its full cumulative counting function.
4. Check that any use of prime-distribution estimates is uniform on the claimed intervals and that exceptional sets are not silently discarded.
5. Distinguish \(\liminf\), \(\limsup\), averaged bounds, and pointwise eventual bounds in every lower-bound argument.
6. Check parity, the role of \(2\), endpoints, and finite initial changes explicitly.
7. Require an adversarial reviewer to search for an accidental replacement of one-summand coverage by two-summand or almost-everywhere coverage.

## Required deliverables

Produce a dated research report containing: a precise target selection (Q1, Q2, or a conditional lemma); a source ledger with direct URLs and publication status; independently checked statements of every imported theorem; an approach registry; complete proof text or a sharply delimited obstruction; and a final claim table marking each target as proved, disproved, conditional, or open.

If asserting a result, include a line-by-line dependency map, all asymptotic uniformity conditions, and an adversarial proof-check report.  If no resolution is reached, report exact failed lemmas, counterexamples to intermediate claims, and the strongest verified partial proposition.  Cite primary sources rather than search snippets.

## Dynamic Multiagent v2 protocol

Maintain one research root and use at most four concurrent agents.  Start with independent approaches rather than a fixed division of mathematical labor.  Create and update an approach registry recording for each route: precise target, imported facts, hypotheses, anticipated certificate, current evidence, and reason for continuation or retirement.

Run multiple waves.  In the first wave, assign independent investigations of construction-side barriers, lower-bound mechanisms, and literature/statement verification.  At each synchronization point, compare only verified lemmas and counterexamples, then dynamically reuse free slots for the most discriminating unresolved claim.  Do not lock agents into static roles.  Reserve adversarial proof checking for any purported lemma or resolution, preferably by an agent not involved in originating it.

Use proof-first allocation.  At most one optional computational subtask may run at once, and only after its exact lemma, hypotheses, certificate format, finite search domain, and stopping condition are entered in the registry.  Examples of acceptable computation are a finite counterexample search to a stated combinatorial sublemma or verification of an exact finite covering certificate.  A numerical trend, heuristic simulation, or a large finite cover is not evidence for Q1/Q2.  Immediately reassign that slot once its declared question is answered.

## Persistence and resumability

Maintain `research_state.md` at every synchronization point.  It must state the canonical target, source URLs checked, theorem dependency status, active and retired approaches, exact open lemmas, attempted computations and their stopping conditions, and the next highest-value task.

If a runtime boundary occurs before a complete, independently checked resolution, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`, preserve the approach registry and evidence ledger, and return a checkpoint report rather than language implying a solution.  On resumption, begin by validating the checkpoint against the cited sources and rerun adversarial checks for any newly promoted claim.
