# Erdős Problem 114: finite-degree complement to the EHP lemniscate theorem

## Definitions and canonical target

For an integer \(n\ge 1\) and a monic polynomial \(p\in\mathbb C[z]\) of degree \(n\), define
\[
E_1(p):=\{z\in\mathbb C:|p(z)|\le 1\},\qquad L(p):=\mathcal H^1(\partial E_1(p))=\mathcal H^1\{z:|p(z)|=1\}.
\]
Here \(\mathcal H^1\) is one-dimensional Hausdorff measure: treat a singular or self-intersecting lemniscate as a set, not as separately parametrized branches counted with multiplicity.

The Erdős--Herzog--Piranian (EHP) inequality is
\[
L(p)\le L(p_0),\qquad p_0(z)=z^n-1,
\]
for every monic \(p\) of degree \(n\). The benchmark is
\[
L(p_0)=2^{1/n}B\!\left(\tfrac12,\tfrac1{2n}\right).
\]

The current target is the residual finite-degree problem: rigorously identify an explicit threshold \(N_0\) justified by Tao's theorem, then prove the EHP inequality for every remaining \(3\le n<N_0\), or find a rigorously certified counterexample in that range. The original inequality does not require uniqueness. A stronger equality classification is separate.

## Accepted background

- Eremenko and Hayman proved the \(n=2\) case and established an extremal reduction: a maximizing monic polynomial exists and may be taken with connected lemniscate containing all critical points. See [On the length of lemniscates](https://arxiv.org/abs/0805.2295) (published in *Michigan Mathematical Journal* 46 (1999), 409--415).
- Fryntov and Nazarov proved local maximality of \(z^n-1\) and an asymptotically sharp upper bound. See [arXiv:0808.0717](https://arxiv.org/abs/0808.0717) and the 2009 AMS publication.
- Tao's [arXiv:2512.12455](https://arxiv.org/abs/2512.12455), Theorem 1.1(iv), proves that for all sufficiently large \(n\), \(L(p)\le L(p_0)\), with equality only for \(p(z)=(z-a)^n-e^{i\theta}\). Its constants are stated to be effectively computable, but the paper does not optimize or prominently state a numerical threshold. Treat this as an accepted theorem only after checking the cited preprint directly.
- Claims on the [Erdős Problems forum thread](https://www.erdosproblems.com/forum/thread/114) about degrees \(3\) through \(14\), and a claimed cubic manuscript, are unreviewed leads, not accepted background. In particular, a previously reported degree-13 certificate bug requires adversarial re-audit.

## Complete resolutions

An affirmative resolution of the original problem requires a rigorous proof that \(L(p)\le L(z^n-1)\) for every remaining degree below a valid explicit \(N_0\), combined with the established \(n=1,2\) cases and Tao's \(n\ge N_0\) theorem.

A negative resolution requires one explicit integer \(n\) not already covered by Tao's theorem, one explicit monic \(p\) of degree \(n\), and a rigorous derivation or independently checkable certificate of
\[
L(p)>L(z^n-1).
\]

For a fixed degree \(n\), an affirmative subresolution proves the inequality for every monic polynomial of that degree, with all normalization and boundary cases included.

## What does not count as a solution

- A plot, numerical optimizer, floating-point integral, random search, or a list of plausible maximizers.
- An asymptotic estimate such as \(2n+O(1)\), even with an explicit constant, unless it proves the exact benchmark inequality in every residual degree.
- Local maximality around \(z^n-1\).
- A computation over an asserted parameter box without a proved reduction from all monic polynomials, certified outward rounding, and a complete coverage proof.
- A finite collection of checked degrees without a justified \(N_0\) and coverage of every degree below it.
- A nonstandard equality case as a purported counterexample to the EHP inequality. It matters only for a separately stated uniqueness claim.
- Reliance on an unreviewed forum post, Zenodo upload, or code repository without independently checking its mathematical reduction and its trusted computing base.

## Required correctness checks

1. State exactly whether every length is \(\mathcal H^1\) of the level set and handle singular critical values without branch multiplicity errors.
2. Preserve monicity under translations and rotations. Record the symmetry orbit precisely as \((z-a)^n-e^{i\theta}\).
3. If invoking Tao, trace each constant needed for \(N_0\) to a stated lemma and prove that the resulting numerical threshold satisfies every prerequisite.
4. If reducing to extremizers, prove existence/compactness and invoke the Eremenko--Hayman reduction with all its hypotheses; do not assume a generic smooth lemniscate.
5. If using a fixed-degree analytic reduction, prove each equivalence, including degenerate critical-point configurations and endpoints of the normalized parameter domain.
6. If using certified computation, first prove a compact normalized domain and a rigorous enclosure of the arclength functional. Use directed/outward interval rounding; prove all boxes are covered; log split rules and termination; and run an independent checker that does not share the principal implementation's critical logic.
7. Distinguish \(<\), \(\le\), and equality exactly. An equality possibility cannot be discarded via floating-point comparison.

## Required deliverables

- `research_state.md` containing the exact target, source versions and access dates, an approach registry, checked lemmas, unresolved obligations, and reproducibility commands.
- A literature-verification note that records what Tao, Eremenko--Hayman, and Fryntov--Nazarov actually prove, with direct URLs and page/theorem references.
- Either a complete proof manuscript, a fully specified counterexample with proof, or a rigorously delimited fixed-degree theorem. Every external mathematical claim must cite a primary paper, preprint, or inspectable formal/certified artifact.
- If an explicit \(N_0\) is extracted, a dependency table for every numerical constant and an independent recalculation.
- If computation is used, source, exact environment, certificate files, hashes, a minimal independent verifier, and a written trusted-base analysis.
- An adversarial audit report listing every failed approach, all unproved assumptions, and whether it affects the global result, a fixed-degree result, or only uniqueness.

## Dynamic Multiagent v2 protocol

Use one research root and no more than four concurrent agents total. Work in multiple waves rather than fixed permanent assignments. At the beginning of each wave, update an approach registry in `research_state.md` containing: approach identifier, precise claim, dependencies, status, evidence links, falsification tests, and owner.

Begin with genuinely independent lines of inquiry: proof extraction from the high-degree theorem, fixed-degree analytic reductions, and adversarial examination of any claimed certificate. Do not force agreement on a method. The research root assigns and reassigns slots dynamically according to information gained, terminates duplicated work, and immediately reuses a freed slot for the highest-value unresolved lemma or audit.

Every proposed proof is handed to a different active or newly assigned agent for hostile checking. The checker must attempt counterexamples, inspect quantifiers and equality cases, verify cited theorems against sources, and report a line-by-line dependency verdict. A claim is not promoted to the registry's `proved` state until this adversarial pass succeeds. Use later waves to combine only independently validated components.

Proof-first allocation is mandatory. At most one agent may perform an optional computational subtask at a time. Before computation, the registry must state the exact lemma or fixed-degree proposition being certified, the compact domain and hypotheses, the certified numerical predicate, the checker, and a finite stopping condition. Once answered, stop that computation and immediately reassign the slot to proof development or verification.

## Persistence and resumability

After every substantive result, contradiction, source discovery, or certificate run, update `research_state.md` with enough detail for a new research root to resume without relying on chat history. Preserve failed routes and the reason they failed.

If a runtime boundary occurs before a complete affirmative or negative resolution, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`. State the current strongest rigorously verified result, the exact next unproved lemma, the evidence already inspected, and the next safest action. Never present a checkpoint, numerical evidence, or an unreviewed artifact as a solution.
