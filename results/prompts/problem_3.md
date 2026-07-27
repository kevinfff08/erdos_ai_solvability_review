# Erdős Problem 3 — research prompt

## Definitions and canonical target

Let \(A\subseteq\mathbb N=\{1,2,\ldots\}\). Assume
\[
\sum_{a\in A}\frac1a=\infty.
\]
Resolve whether, for every integer \(k\ge3\), there are \(x\in\mathbb N\) and \(d\in\mathbb N_{>0}\) such that
\[
\{x,x+d,\ldots,x+(k-1)d\}\subseteq A.
\]
A progression is non-trivial exactly when \(d>0\). “Arbitrarily long” means that the assertion holds for every finite \(k\); it does not ask for one infinite progression. The choices \(x,d\) may depend on \(A,k\).

For fixed \(k\), let \(r_k(N)\) be the maximum size of a subset of \([N]=\{1,\ldots,N\}\) containing no non-trivial \(k\)-term arithmetic progression.

Primary record: <https://www.erdosproblems.com/3>. LaTeX record: <https://www.erdosproblems.com/latex/3>.

## Accepted background

- Bloom and Sisask proved that a 3-AP-free \(A\subseteq[N]\) has \(|A|\ll N/(\log N)^{1+c}\), which settles the \(k=3\) instance after a dyadic summability argument: <https://arxiv.org/abs/2007.03528>.
- Kelley and Meka obtained much stronger 3-AP bounds, published in FOCS 2023: <https://doi.org/10.1109/FOCS57990.2023.00059>. Bloom and Sisask subsequently gave an \(\exp(-c(\log N)^{1/9})N\) 3-AP-free bound in a preprint: <https://arxiv.org/abs/2309.02353>. These are results only for \(k=3\).
- Green and Tao proved a polylogarithmic bound for \(r_4(N)\): <https://doi.org/10.1112/S0025579317000492>. Do not assume it settles the harmonic-divergence case for \(k=4\).
- Leng, Sah, and Sawhney proved for every \(k\ge5\) that \(r_k(N)\ll N\exp(- (\log\log N)^{c_k})\): <https://arxiv.org/abs/2402.17995>. This does not prove the canonical target.

Treat all other claims as unproved until checked against a primary source. Refresh the literature through the actual start date before claiming novelty or a resolution.

## Complete resolutions

An affirmative resolution is a complete proof that every \(A\subseteq\mathbb N\) with divergent reciprocal sum contains a non-trivial \(k\)-term progression for every \(k\ge3\).

A negative resolution is an explicit or rigorously constructed \(A\subseteq\mathbb N\) and a fixed \(k\ge3\) with divergent reciprocal sum and no non-trivial \(k\)-term progression.

## What does not count as a solution

- Settling only \(k=3\), \(k=4\), or finitely many lengths.
- A finite computation or a construction that avoids progressions only below a cutoff.
- An \(r_k(N)\) estimate without a rigorous derivation that it forces convergence of the reciprocal subseries.
- A density statement valid only on selected scales, a heuristic, or numerical evidence.
- Forgetting that the common difference must be positive.
- Treating a forum post, search snippet, or unreviewed claim as a proof.

## Required correctness checks

1. Write quantifiers explicitly in the order \(\forall A\,\forall k\,\exists x,d\).
2. Verify \(d\ge1\), positivity of all terms, and containment of every progression term in \(A\).
3. If using \(r_k\), state and prove a precise block or summation-by-parts lemma. Track all constants, starting thresholds, and dependence on \(k\).
4. Check all dyadic blocks, not only a subsequence of scales.
5. Do not infer the \(k=4\) target from \(r_4(N)\ll N/(\log N)^c\) without proving that the resulting reciprocal series converges.
6. For a counterexample, separately certify global AP-freeness for one fixed length and divergence of the full positive series.
7. Check every cited theorem from its original paper or formal artifact, not merely its abstract.

## Required deliverables

- A dated literature log with direct URLs, publication status, and the exact theorem statement used from each source.
- A self-contained proof or counterexample, with a dependency-labelled lemma ledger.
- A rigorous derivation of every finite-to-infinite summability transfer.
- An adversarial audit of quantifiers, asymptotic ranges, summability, and AP conventions.
- If incomplete, a frontier report recording the strongest verified intermediate result, failed constructions, and the next falsifiable lemma.

## Dynamic Multiagent v2 protocol

Maintain a research root and an approach registry containing, for each active approach: target lemma, hypotheses, source dependencies, proposed falsification test, current evidence, owner, and status. Use at most four concurrent agents. Begin with early independent approaches; do not impose a static mathematical division of labor.

Work in multiple waves. At each wave boundary, the research root compares evidence, merges duplicate approaches, archives disproved paths, and allocates newly free slots to the smallest unresolved bottleneck. Reuse a slot immediately when its prior question is answered. Every nontrivial proof fragment must be adversarially checked by an agent that did not develop it, with explicit attacks on quantifier order, k-dependence, scale coverage, and summation steps.

Allocate proof-first. At most one optional computational subtask may run at a time. Before it starts, the registry must state its exact target lemma or counterexample hypothesis, finite domain, certificate format, and stopping condition. Once that question is answered, stop the computation and immediately reassign the slot to proof development or verification. Computation is not evidence for an all-scale theorem without a proved transfer argument.

## Persistence and resumability

Update `research_state.md` after each wave with the canonical target, literature cutoff date, approach registry, proved/cited/falsified lemmas, citations, adversarial findings, and next decisive tasks. If execution ends before a proof or counterexample has passed adversarial checking, put `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`; preserve exact partial arguments and failed tests, then resume from the recorded bottleneck rather than claiming a resolution.
