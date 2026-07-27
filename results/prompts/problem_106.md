# Erdős Problem 106: arbitrary-orientation square packing

## Definitions and canonical target

For each positive integer \(k\), consider exactly \(k^2+1\) Euclidean squares \(Q_1,\ldots,Q_{k^2+1}\) of positive side lengths \(s_1,\ldots,s_{k^2+1}\). Each square is contained in the closed unit square \([0,1]^2\); its orientation is arbitrary. Their interiors are pairwise disjoint, while boundary contacts between squares and with \(\partial[0,1]^2\) are allowed.

Define
\[
f(n):=\sup\{\sum_{i=1}^{n}s_i: (Q_i)_{i=1}^n\text{ is such a packing in }[0,1]^2\}.
\]

Canonical target: prove or disprove
\[
\forall k\in\mathbb Z_{>0},\qquad f(k^2+1)=k.
\]

The lower bound is already known: start with the \(k\times k\) grid of side \(1/k\), remove one tile, and insert two side-\(1/(2k)\) squares. Thus the sole affirmative burden is the universal upper bound \(\sum_i s_i\le k\). Do not impose axis parallelism unless explicitly proving a restricted lemma.

## Accepted background

- By area and Cauchy–Schwarz, \(f(k^2)=k\): \(\sum s_i^2\le1\) and \((\sum s_i)^2\le k^2\sum s_i^2\). This does not prove the target with \(k^2+1\) squares.
- Halász gave neighboring-parameter lower-bound constructions in 1984: [paper and abstract](https://www.sciencedirect.com/science/article/pii/0097316584900244).
- Erdős–Soifer and Campbell–Staton conjectured the more general formula \(f(k^2+2c+1)=k+c/k\) for \(-k<c<k\); Campbell–Staton is [here](https://www.tandfonline.com/doi/abs/10.1080/00029890.2005.11920180). Praton showed that validity for one \(c\) implies validity for all \(c\), so the general formulation is equivalent to the target; see [arXiv:math/0504341](https://arxiv.org/abs/math/0504341) and the [2008 published version](https://www.tandfonline.com/doi/abs/10.1080/0025570X.2008.11953576).
- The axis-parallel analogue \(g\), in which every small-square side is parallel to an outer-square side, is solved: \(g(k^2+2c+1)=k+c/k\) for \(-k<c<k\). This is not the target. See Baek–Koizumi–Ueoro, [arXiv:2411.07274](https://arxiv.org/abs/2411.07274).
- Singh proves that the target is equivalent to its holding for infinitely many \(k\), and to convergence of \(\sum_{k\ge1}(f(k^2+1)-k)\); it remains an open target in that paper. See [arXiv:2601.22163](https://arxiv.org/abs/2601.22163).
- The historical database record is [Erdős Problems 106](https://www.erdosproblems.com/106). Treat it as a secondary status record, not as proof.

## Complete resolutions

An affirmative resolution requires a rigorous proof that every allowed packing of \(k^2+1\) squares has total side length at most \(k\), for every positive integer \(k\). Combine it with the stated construction to obtain equality.

A negative resolution requires one explicit integer \(k\) and a certified packing of exactly \(k^2+1\) positive-side-length, arbitrarily oriented squares in \([0,1]^2\) with total side length strictly greater than \(k\). Supply exact algebraic/rational data or rigorously validated interval data for every side length, vertex, orientation, containment inequality, and pairwise interior-disjointness condition.

## What does not count as a solution

- A proof only for the axis-parallel quantity \(g\).
- A finite list of checked \(k\), a floating-point optimizer output, a drawing, or an uncertified numerical search.
- A lower-bound construction of total \(k\) without the global upper bound.
- An asymptotic upper bound \(k+o(1)\), a bound with a positive error, or an area argument that does not handle \(k^2+1\).
- A proof for tilings, congruent squares, disjoint closed squares, or another strengthened/restricted model unless it is explicitly and rigorously reduced to the canonical target.
- Restating the equivalent series criterion without proving convergence or divergence.

## Required correctness checks

1. State exactly where arbitrary orientations enter every lemma; audit every use of horizontal/vertical projections, grid lines, or coordinate-wise disjointness.
2. Preserve the quantifier \(\forall k\ge1\), exact count \(k^2+1\), and strictly positive side lengths.
3. Check containment for rotated squares using the full square geometry, not axis-aligned bounding boxes alone.
4. Check pairwise disjoint interiors, including boundary-touching and degenerating sequences.
5. If taking an extremal packing, justify maximum attainment or formulate the proof for suprema and pass to limits rigorously.
6. For any claimed counterexample, independently certify strict surplus and every non-overlap constraint.
7. Compare each claimed use of the 2024 axis-parallel proof against the point where axis parallelism is essential.
8. Label every cited claim as theorem, conjecture, construction, or deduction; cite primary sources with stable URLs.

## Required deliverables

Maintain a concise research report containing: the exact target; an approach registry; proved lemmas with hypotheses; failed approaches and the precise obstruction; a dependency graph for any proposed proof; and a final resolution status.

If affirming, provide a self-contained proof with a separate adversarial audit of all orientation, compactness, and equality cases. If refuting, provide a machine-checkable or independently checkable geometric certificate and a verification script or calculation transcript. If incomplete, provide the strongest new rigorously proved lemma and explain exactly why it falls short.

Every literature-dependent statement must include a direct source URL. Do not cite search snippets as proof. Separate peer-reviewed papers from arXiv preprints.

## Dynamic Multiagent v2 protocol

Use a research root that owns `research_state.md`, the approach registry, source log, proof dependency graph, and final synthesis. Run at most four agents concurrently.

Begin with multiple genuinely independent approaches rather than a fixed mathematical method or static job allocation. Before substantive work, register each approach with: target lemma or certificate, assumptions, possible stopping condition, relation to prior work, and a falsification test. The research root deduplicates only after agents have independently identified their initial route.

Work in multiple waves. In each wave, agents may pursue proof, counterexample, reduction, literature verification, or adversarial checking as justified by the current registry. When a route proves a lemma, fails decisively, or reaches its stopping condition, immediately reuse that slot for the most valuable unresolved dependency. Do not keep an agent assigned merely because of an initial role.

Every nontrivial proposed proof is assigned an adversarial checker independent of its author. The checker must attempt to break quantifiers, arbitrary-rotation coverage, exact-square count, boundary contacts, limiting arguments, and any equality claim. A claim cannot enter the synthesis as proved until the checker records either a valid verification or a precisely isolated unresolved issue.

Allocate resources proof-first. At most one optional computational subtask may run at once. Before it starts, record the precise lemma or counterexample hypothesis being tested, the bounded parameter domain, the exact certification method, and the stopping condition. Computation must stop and its slot must be reassigned as soon as that question is answered; it may not become an open-ended optimization campaign.

## Persistence and resumability

After each meaningful event, update `research_state.md` with the canonical statement, source links, status of each registered approach, verified lemmas, rejected claims and reasons, proof dependencies, computational certificates if any, and the next highest-value question.

If a runtime boundary arrives before a complete resolution, do not present a conjectural proof or imply completion. Write `CHECKPOINT_NOT_FINAL` at the top of the current state, record the last verified claim and all unresolved proof obligations, preserve citations and artifacts, and leave a concrete next action for the next wave. A later session must resume from this state rather than restart the literature audit or silently discard failed routes.
