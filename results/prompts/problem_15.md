# Erdős Problem 15 — unconditional convergence of an alternating prime-index series

## Definitions and canonical target

Let \(p_n\) be the \(n\)-th prime in strictly increasing order, so \(p_1=2,p_2=3,\ldots\). For \(N\ge1\), set
\[
S_N:=\sum_{n=1}^{N}(-1)^n\frac{n}{p_n}.
\]

Prove or disprove the unconditional proposition
\[
\exists L\in\mathbb R\quad \lim_{N\to\infty}S_N=L.
\]

This is ordinary convergence of the natural-order partial sums in \(\mathbb R\). Do not change the order, summation method, weights, or prime sequence. The series cannot converge absolutely: the prime number theorem gives \(n/p_n\sim1/\log n\).

## Accepted background

- The canonical problem is currently listed as open by the Erdős Problems database: <https://www.erdosproblems.com/15>. Treat that label as a research-status record, not as a theorem.
- Tao proved the affirmative statement **conditional** on a sufficiently strong quantitative Hardy--Littlewood prime-tuples conjecture: Terence Tao, *The convergence of an alternating series of Erdős, assuming the Hardy--Littlewood prime tuples conjecture*, Communications of the AMS 4 (2024), 80--96, <https://doi.org/10.1090/cams/29>; preprint <https://arxiv.org/abs/2308.07205>. This is not an unconditional solution.
- Tao records an equivalence, due to an unpublished observation of Mustafa Said (with harmless finite changes of initial terms): convergence of the target series is equivalent to convergence of
\[
\sum_{m\ge2}\frac{(-1)^{\pi(m)}}{m\log m}.
\]
See the author’s exposition <https://terrytao.wordpress.com/2023/08/14/the-convergence-of-an-alternating-series-of-erdos-assuming-the-hardy-littlewood-prime-tuples-conjecture/>.
- If \(F(x):=\sum_{m\le x}(-1)^{\pi(m)}\) satisfies \(F(x)=O(x/(\log x)^\varepsilon)\) for some \(\varepsilon>0\), then partial summation proves convergence. This is a sufficient intermediate result, not an established theorem.
- The Formal Conjectures Lean file formalizes the target but contains `sorry`, so it supplies no proof certificate: <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/15.lean>.
- A 2025 preprint by Mantzakouras concerns related integral/damped formulations and discusses hypotheses including RH; it must not be cited as a resolution of this target without a full scope check: <https://arxiv.org/abs/2505.06242>.

## Complete resolutions

An affirmative resolution is an unconditional proof that \((S_N)\) is Cauchy, hence has a finite real limit.

A negative resolution is an unconditional proof that \((S_N)\) fails to converge, such as two subsequences with different limiting behavior or a proof of unboundedness.

Every prime-distribution estimate used in either route must be either proved in the submission or cited to a precise, established unconditional source. If a result is conditional, identify the exact hypothesis and classify the work as partial only.

## What does not count as a solution

- A computation, graph, fitted limiting constant, or finite verification of partial sums.
- A conditional proof under Hardy--Littlewood, RH, Cramér-type models, or a random model.
- An application of the alternating-series test without establishing eventual monotonicity of \(n/p_n\).
- A proof only of \(n/p_n\to0\), only of non-absolute convergence, or only of qualitative parity equidistribution of \(\pi(x)\).
- A proof for a smoothed, damped, Abel/Cesàro-summed, rearranged, or modified prime-gap series.
- A formal theorem declaration containing `sorry`, axioms that encode the result, or unverified automation output.

## Required correctness checks

1. Fix \(p_1=2\) and the sign \((-1)^n\) throughout; state precisely why finite initial changes do or do not matter.
2. If using the \((-1)^{\pi(m)}\) formulation, prove the equivalence and all summation/error estimates at the claimed level of generality.
3. For any partial-summation route, verify the boundary term and the integrability of the resulting kernel, with explicit constants/ranges.
4. Audit all short-interval prime estimates for uniformity in interval length, tuple size, shifts, and exceptional sets. Do not replace Tao’s strong quantitative Hardy--Littlewood hypothesis by a weaker informal statement.
5. Separate theorem, conjecture, heuristic, numerical observation, and formalized statement in every write-up.
6. Independently adversarially check the decisive lemma before calling any result complete.

## Required deliverables

- A self-contained proof or disproof manuscript, with all definitions and a theorem exactly matching the canonical target.
- A dependency ledger distinguishing established unconditional inputs, newly proved lemmas, conditional lemmas, and heuristics.
- A line-by-line audit of the decisive estimate and a concise explanation of why it closes the Cauchy or divergence criterion.
- Reproducible formalization files for any formal claims, with a build command and no unresolved `sorry`/axioms for the claimed theorem.
- If incomplete: a sharply stated partial theorem, its exact hypotheses, the first unproved bottleneck, and a counter-check showing it does not overclaim a resolution.
- Direct URLs/DOIs/arXiv identifiers for every external theorem relied upon, including publication status and access date.

## Dynamic Multiagent v2 protocol

Create a research root that maintains `research_state.md`, an approach registry, a source ledger, and a proof-obligation queue. Use at most four concurrent agents, including the coordinator.

Begin with independent approaches rather than fixed assignments: agents should register a distinct proposed route, its precise target lemma, dependencies, predicted failure mode, and a falsifiable completion test. The coordinator admits only non-duplicative approaches and may merge or retire them when evidence warrants it.

Work in multiple waves. In each wave, reserve one slot for adversarial checking of another active route. Reuse a freed slot immediately for the most informative unresolved proof obligation, source verification, or independent alternative; do not keep static roles. Before any purported resolution, require two independent checks: one proof audit and one status/scope audit against the canonical statement.

Allocate proof work before computation. At most one optional computational subtask may run at once, and only after declaring: (i) the exact finite lemma or conjectural pattern being tested, (ii) all hypotheses and data-generation rules, (iii) a stopping condition, and (iv) how either outcome changes the proof plan. Once answered, release that slot immediately; numerical evidence cannot be a completion criterion.

## Persistence and resumability

Update `research_state.md` after every substantive step with: canonical target, sources checked, current status, active approaches, discarded approaches and reasons, proved lemmas, open proof obligations, exact commands/artifacts, and next adversarial check.

At a runtime boundary, do not state or imply success. Save the dependency ledger and partial derivations, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`, and record the next smallest verifiable action. On resumption, read the state file, revalidate any time-sensitive literature-status claim, and continue from the recorded proof obligation.
