# Erdős Problem 30 — research prompt

## Definitions and canonical target

For each positive integer \(N\), write \([N]=\{1,\ldots,N\}\). A set \(A\subseteq[N]\) is a Sidon set (equivalently a \(B_2\)-set here) when
\[
a+b=c+d\quad(a,b,c,d\in A)\implies\{a,b\}=\{c,d\}
\]
as unordered pairs. In particular, sums with repeated terms such as \(a+a\) are included.

Define
\[
h(N)=\max\{|A|:A\subseteq[N]\text{ is a Sidon set}\}.
\]

Prove or disprove the following exact asymptotic assertion:
\[
\forall\epsilon>0\ \exists C_\epsilon\ge0\ \exists N_\epsilon\ \forall N\in\mathbb N,\ N\ge N_\epsilon:\quad
|h(N)-\sqrt N|\le C_\epsilon N^\epsilon.
\]

Use this interval \(B_2\) definition throughout. Do not substitute the harmonic-analysis meaning of “Sidon set,” a weak-Sidon convention, a modular-only statement, or an infinitely-often statement.

## Accepted background

The following are accepted only to the scope explicitly stated in their sources.

- Erdős Problems currently records this as open: <https://www.erdosproblems.com/30>.
- Classical Singer constructions establish the \((1-o(1))\sqrt N\) main-term lower-bound phenomenon; this does not give the required error term for every \(N\).
- Carter, Hunter, and O'Bryant proved, in a peer-reviewed 2025 paper,
  \[
  h(N)\le\sqrt N+0.98183N^{1/4}+O(1).
  \]
  Source: <https://link.springer.com/article/10.1007/s10474-024-01499-8>.
- Hou and Zhao's unrefereed July 2026 preprint claims the stronger
  \[
  h(N)\le\sqrt N+0.9435N^{1/4}+O(1),
  \]
  with an exact rational finite certificate for a component of the proof. This is useful background, not a resolution: <https://arxiv.org/abs/2607.01169>.
- A 2026 Lean 4 preprint reports formalized Singer/Sidon infrastructure and a conditional reduction, not a proof of this target: <https://arxiv.org/abs/2605.03274>.
- Earlier upper-bound advances include Balogh--Füredi--Roy, <https://arxiv.org/abs/2103.15850>, and O'Bryant, <https://arxiv.org/abs/2207.07800>.

Clearly label every other input as either a proved theorem with a source, a conjecture/assumption, or a proposed lemma. In particular, do not silently assume a subpolynomial prime-gap statement.

## Complete resolutions

An affirmative resolution is a self-contained proof of the displayed quantified estimate, including both signs of the error, for all sufficiently large integers \(N\), without unproved hypotheses.

A negative resolution is a proof that there is an \(\epsilon_0>0\) for which the displayed estimate fails: equivalently, for every \(C,N_0\) some \(N\ge N_0\) obeys \(|h(N)-\sqrt N|>CN^{\epsilon_0}\). A concrete sequence witnessing this divergence is acceptable if rigorously proved.

## What does not count as a solution

- Any improvement only to the coefficient of \(N^{1/4}\).
- A bound for one fixed \(\epsilon\), a subsequence, or infinitely many \(N\).
- Only an upper bound or only a lower bound.
- A conditional implication from a prime-gap conjecture, RH, or an assumed Sidon-set estimate.
- Exhaustive computation below a cutoff without a theorem covering all larger \(N\).
- A result for a changed Sidon convention, a cyclic group, or a shifted interval without an explicit, valid transfer to the canonical target.

## Required correctness checks

1. State the Sidon predicate and verify it includes repeated sums.
2. Audit every asymptotic quantifier: constants and thresholds may depend on \(\epsilon\), never on \(N\).
3. If using a diameter formulation, prove the exact conversion to \(h(N)\), including shifts, floors, ceilings, and endpoint offsets.
4. Identify separately the theorem establishing each lower-bound construction and the theorem transferring it to every required interval length.
5. For a computational certificate, prove the bridge from the finite certificate to the claimed asymptotic theorem; rerun an exact-arithmetic verifier where available and record the version/hash.
6. Subject every candidate proof to an adversarial check for an unproved distributional hypothesis, an “infinitely many”/“all sufficiently large” swap, and an accidental fixed-exponent argument.

## Required deliverables

- A concise research-state report listing the canonical target, every theorem used with a direct URL, and the exact remaining lemma(s).
- Either a complete affirmative or negative proof meeting the criteria above, or a rigorously delimited partial result that says exactly why it does not resolve the problem.
- A dependency ledger separating proved facts, formalized facts, computer-verified finite facts, assumptions, and conjectures.
- For every nontrivial claimed lemma: a full proof, all parameter ranges, and an adversarial-proof-check report.
- If any computation is used: code/version/hash, inputs, exact or validated numerical model, certificate, stopping condition, and a proof of relevance to the target.

## Dynamic Multiagent v2 protocol

Maintain one research root and at most four concurrent agents total. Begin with independent approaches rather than a fixed division of mathematical labor. Before a route receives sustained effort, enter it in an approach registry containing: its precise intermediate target, dependencies, whether it addresses the upper or lower side, expected falsifiers, and its stopping condition.

Use multiple waves. In an early wave, agents may independently audit the current bounds, test candidate reductions, and seek incompatible proof routes. At each wave boundary, the research root deduplicates the registry, terminates routes whose stated lemma is false or already known, and dynamically reuses freed slots for the most informative unresolved route. Do not retain an agent merely because it was initially assigned.

Every proof-producing route must receive adversarial review by an agent that did not derive it. The reviewer must inspect quantifiers, boundary cases, convention changes, hidden external hypotheses, and exact dependency links. A route is not promoted from conjectural to proved until that review is answered in writing.

Allocate resources proof-first. At most one optional computational subtask may run at once. Before it starts, record the exact lemma/hypotheses it tests, the certificate or falsifier sought, and a finite stopping condition. Immediately release and reassign that slot once the question is answered; computation may not become an open-ended search for a better coefficient.

## Persistence and resumability

Keep `research_state.md` current after each material result, failed lemma, source verification, proof gap, certificate run, and reassignment. It must contain the approach registry, dependency ledger, active hypotheses, exact next checks, and links/hashes for external artifacts.

If runtime ends before a complete resolution, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, state precisely what has and has not been established, preserve all proof gaps, and leave the next smallest verifiable action. Never phrase an incomplete exploration, a numerical pattern, or a conditional derivation as a solution.
