# Erdős problem 36: minimum overlap constant

## Definitions and canonical target

For each integer \(N\ge 1\), let
\[
r_{A,B}(x)=\#\{(a,b)\in A\times B:a-b=x\},\qquad
M(N)=\min_{A\sqcup B=[2N],\ |A|=|B|=N}\ \max_{x\in\mathbb Z}r_{A,B}(x),
\]
where \([2N]=\{1,\ldots,2N\}\). The maximum is over all integers \(x\), although only \(|x|\le 2N-1\) can contribute.

The minimum-overlap constant is
\[
C=\lim_{N\to\infty}\frac{M(N)}N.
\]
The existence of this limit is accepted background. Determine \(C\) exactly. Interpret the original wording “the optimal \(c\)” as the supremum of constants \(c\) for which
\[
\exists N_0\ \forall N\ge N_0\ \forall(A,B)\ \exists x\in\mathbb Z:
 r_{A,B}(x)\ge cN.
\]
Do not assume without proof that the endpoint \(c=C\) itself satisfies this eventual inequality.

## Accepted background

- Haugland’s [2016 preprint](https://arxiv.org/abs/1609.08000) explains the reduction of asymptotic upper bounds to admissible density/step functions on \([0,2]\), with values in \([0,1]\) and integral \(1\). It reports an upper bound about \(0.380926\).
- White’s [2022 preprint](https://arxiv.org/abs/2201.05704), subsequently published as [A new bound for Erdős’ minimum overlap problem](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/online/115217/a-new-bound-for-erdos-minimum-overlap-problem), proves \(C>0.379005\) through Fourier analysis and a convex program.
- Recent preprints report stronger but not yet peer-reviewed records: [Kim--Pilanci (2026)](https://arxiv.org/abs/2606.31182) claims a certified lower bound \(C\ge0.37912\), and [Ye et al. (2026)](https://arxiv.org/abs/2604.19341) reports an upper construction \(C\le0.380856\) in an ablation run. Treat both as claims requiring independent artifact-level verification before relying on them.
- The current maintained [optimization-constants index](https://teorth.github.io/optimizationproblems/constants/1b.html) documents the sequence of reported upper constructions. The [Erdős Problems page](https://www.erdosproblems.com/36) remains open but has stale numerical records.

Theorems above are background only to the extent their cited proofs/certificates are checked. Search heuristics, LLM scores, and informal forum statements are not theorems.

## Complete resolutions

A complete affirmative resolution supplies an explicit \(\alpha\in\mathbb R\) and rigorous matching inequalities \(C\ge\alpha\) and \(C\le\alpha\), hence \(C=\alpha\).

A complete negative audit of a proposed value \(\alpha\) proves \(C<\alpha\) or \(C>\alpha\). A complete disproof of a proposed bound supplies either a valid admissible object violating its claimed universal lower-bound premise or a proof that its upper-bound construction/transference argument fails.

## What does not count as a solution

- Computing \(M(N)\) for finitely many \(N\), regardless of scale.
- Reporting a sampled numerical objective without an exact or rigorously interval-certified bound for the continuous objective.
- Giving only a better upper construction or only a better lower relaxation.
- Treating an optimizer’s floating-point output as a universal lower-bound certificate.
- Proving a statement about autocorrelation of one set while failing to connect it exactly to the cross-difference quantity \(r_{A,B}\).
- Citing an AI-generated candidate, repository README, or forum post in place of a complete argument.

## Required correctness checks

1. State every quantifier and normalize all functions and measures explicitly.
2. For an upper bound, verify range \([0,1]\), integral \(1\), all translates, endpoint conventions, and the discrete-to-continuous transference including the \(o(N)\) error.
3. For a lower bound, prove each relaxation constraint is necessary for every admissible object. Verify all dual feasibility conditions in exact rational arithmetic or validated interval arithmetic.
4. If a finite partition is claimed, recompute all cross-difference multiplicities independently from the supplied data.
5. Keep \(\liminf\), \(\limsup\), the known existence of the limit, and endpoint attainment separate.
6. Every use of a prior record must cite a primary paper, preprint, formal artifact, or executable certificate and identify its publication status.

## Required deliverables

- A self-contained proof manuscript or a precise obstruction report.
- A machine-readable statement of every candidate construction/certificate and an independent verifier.
- A provenance table distinguishing theorem, preprint claim, numerical observation, and conjecture, with direct URLs and access dates.
- If incomplete, a best-current bound with a complete proof/certificate, an explicit remaining gap, and a list of failed approaches and counterexamples.
- A final proof-audit checklist mapping each nontrivial line to its supporting lemma or verified computation.

## Dynamic Multiagent v2 protocol

Establish a research root that maintains an approach registry containing: target formulation, active hypotheses, source status, proof dependencies, artifact hashes, and adversarial findings. Use at most four concurrent agents total.

Begin with independent approaches rather than a fixed division of labor. In the first wave, assign distinct lines of attack such as source/certificate audit, structural analytic lower bounds, rigorous upper constructions, or attempted counterexamples to proposed lemmas. Register each approach before substantial work so duplicates are visible, but do not prescribe a method in advance.

At every handoff, an adversarial checker must inspect claimed lemmas, quantifiers, normalization, asymptotic transfer, and numerical certificates. Reuse slots dynamically: terminate or redirect an approach when it proves a lemma, finds a flaw, or has no falsifiable next claim; open a new independent approach in the released slot. Run multiple waves, using confirmed intermediate results to generate new incompatible approaches rather than converging prematurely on the best numerical candidate.

Allocate resources proof-first. At most one optional computational subtask may run at a time. Before it runs, record the exact lemma or candidate it tests, hypotheses, input representation, verifier, and a stopping condition. When answered, immediately release that slot to proof development or adversarial verification; computation is never evidence by itself.

## Persistence and resumability

Maintain `research_state.md` after each material result. It must record the canonical target, citations checked, approach registry, current bounds and their verification status, artifact locations/hashes, rejected arguments, and the next falsifiable tasks.

If a runtime boundary occurs before a complete independently checked proof or disproof, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`, preserve all partial certificates and their verification status, and resume from that checkpoint. Never convert an interrupted numerical search, an unreviewed source claim, or an incomplete proof sketch into a final resolution.
