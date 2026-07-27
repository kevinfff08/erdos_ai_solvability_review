# Erdős Problem 107: exact Erdős-Szekeres convex-polygon threshold

## Definitions and canonical target

For every integer \(n\ge 3\), let \(ES(n)\) be the least positive integer \(N\) such that every finite set \(P\subset\mathbb R^2\) with \(|P|=N\) and no three collinear contains a subset \(Q\subseteq P\) of size \(n\) in convex position. Here “in convex position” means that every member of \(Q\) is a vertex of \(\operatorname{conv}(Q)\); equivalently, \(Q\) is the vertex set of a convex \(n\)-gon.

Canonical target: prove
\[
ES(n)=2^{n-2}+1\qquad\text{for every integer }n\ge3.
\]

This is not an empty-polygon problem: points of \(P\setminus Q\) may lie inside the convex polygon. The lower bound \(ES(n)\ge2^{n-2}+1\) is accepted background. Thus a proof needs the corresponding universal upper bound. A disproof needs one \(n\ge7\) and a general-position set of exactly \(2^{n-2}+1\) points with no \(n\) points in convex position.

## Accepted background

- Erdős and Szekeres established the classical cap-cup upper bound \(ES(n)\le {2n-4\choose n-2}+1\), and their later construction gives \(ES(n)\ge2^{n-2}+1\). A precise recent exposition is Baek–Balko, [SoCG 2025](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.13).
- The exact result is known through \(n=6\): in particular, Szekeres and Peters proved \(ES(6)=17\) by a reproducible computer proof; see [the ANZIAM paper](https://www.cambridge.org/core/journals/anziam-journal/article/computer-solution-to-the-17point-erdosszekeres-problem/0EC7876789232266D60439A4C00D86D9). The first open concrete case is \(ES(7)=33\).
- Suk proved \(ES(n)=2^{n+o(n)}\); see [arXiv:1604.08657](https://arxiv.org/abs/1604.08657). Holmsen, Mojarrad, Pach, and Tardos improved the general upper-bound error to \(ES(n)\le2^{n+O(\sqrt{n\log n})}\); see [arXiv:1710.11415](https://arxiv.org/abs/1710.11415) and the precise review in [Baek–Balko](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.13).
- Baek–Balko prove a different theorem: the split-polygon threshold is exactly \(2^{n-2}+1\), and the original conjecture holds for decomposable point sets. These are useful constraints, not proofs of the canonical target. Their 2026 journal version also discusses failed abstract generalizations: [JCTA article](https://www.sciencedirect.com/science/article/pii/S0097316526000385).
- Dumitru’s [2025 preprint](https://arxiv.org/abs/2512.24061) gives a SAT encoding and UNSAT certificates only for certain anchored subfamilies of the 33-point case. Treat it as partial computational background, not as a resolution.

## Complete resolutions

An affirmative resolution is a fully detailed proof that every general-position set of \(2^{n-2}+1\) planar points contains \(n\) points in convex position for every \(n\ge3\). It must explicitly invoke or reprove the known lower bound to conclude equality.

A negative resolution is an explicit \(n\ge7\) and a fully verified general-position planar configuration of \(2^{n-2}+1\) points with no convex \(n\)-subset. Exact coordinates or a rigorously realizable order-type certificate must be supplied, together with a complete verification of avoidance.

## What does not count as a solution

- An asymptotic improvement, including \(2^{n+o(n)}\), does not establish the exact formula.
- A proof only for caps, cups, split polygons, decomposable sets, pseudoline arrangements, weak/strong abstract polygons, or a non-realizable oriented structure does not solve the planar problem unless a proved reduction covers all planar point sets.
- Resolving \(ES(7)\), or any finite collection of values, is substantial progress but not a proof of the all-\(n\) target.
- A purported counterexample with only \(2^{n-2}\) points merely recovers the known lower bound.
- Solver output, a claimed exhaustive search, or a numerical picture without an exact encoding, coverage proof, independently checkable certificate, and geometric-realizability audit does not count.

## Required correctness checks

1. Check every quantifier: \(n\ge3\), finite \(P\), \(|P|=2^{n-2}+1\), and no three collinear.
2. Check the intended predicate: every selected point must be a vertex of its selected subset’s convex hull; do not impose or assume emptiness.
3. Check every reduction from geometry to cups/caps, order types, allowable sequences, oriented matroids, or SAT. State both directions of the reduction and all hypotheses.
4. Check lower-bound direction separately from upper-bound direction. An avoiding set of size one below the threshold cannot disprove the conjecture.
5. For any perturbation, prove it preserves all orientation signs and the convexity/nonconvexity predicates used.
6. For any computational certificate, preserve the exact CNF and assumptions; audit symmetry breaking, exhaustive coverage, solver proof format, independent checking, and—where needed—realizability in \(\mathbb R^2\).
7. Require an adversarial reviewer to try to construct the omitted case in each structural lemma and to compare the claimed theorem precisely with the Baek–Balko restricted results.

## Required deliverables

- A concise `status.md` stating whether the work is a proof attempt, a counterexample attempt, a finite-case result, or an obstruction, with no overclaim.
- A self-contained mathematical write-up defining every auxiliary object and proving every new lemma.
- An `approach_registry.md` listing each live/dead approach, its exact target, dependencies, tested edge cases, and reason for abandonment or continuation.
- A `proof_audit.md` containing a line-by-line dependency graph, explicit quantifier audit, and adversarial objections with dispositions.
- If computation is used: source, deterministic environment details, encoding specification, input instances, a machine-checkable certificate, an independent checker, and a statement of exactly which lemma the computation establishes.
- A bibliography with direct links, distinguishing theorem, conjecture, preprint, peer-reviewed result, formal artifact, and informal observation.

## Dynamic Multiagent v2 protocol

Use one research root and at most four concurrent agents total, including the root. Begin with independent approaches rather than assigning a fixed mathematical method. The root maintains `approach_registry.md`; before starting a substantial branch, record its precise proposition, intended implication to the canonical target, assumptions, and known overlap with other branches.

Run multiple waves. In the first wave, prioritize mutually incompatible proof or counterexample reductions. In later waves, reuse a freed slot dynamically for the sharpest unresolved lemma, a literature/definition audit, or an adversarial check; do not preserve static roles. Every branch must report a proof object, a falsified subclaim, or a bounded uncertainty statement. The root periodically compares branches, merges only formally compatible claims, and kills duplicate or non-implicating work.

No branch may declare a breakthrough from a sketch. Any candidate proof or counterexample is immediately handed to a different active agent for hostile verification. The verifier must attempt small cases, boundary parameters, reversed implications, realizability failures, and confusion between convex position and empty polygons. Claims used by another branch remain provisional until the adversarial check passes.

Maintain an approach registry row for every route: identifier, exact claim, status, dependencies, evidence location, counterexample search status, and next falsifiable test. Agents may propose methods freely; the root must not prescribe a fixed method or assume that an existing literature approach is exhaustive.

Proof-first allocation is mandatory. At most one optional computational subtask may run at a time. Before it starts, the root must write: (i) the exact finite lemma it would establish, (ii) hypotheses and the formal geometry-to-encoding correspondence, (iii) a certificate/checker plan, and (iv) a stopping condition. Once that finite question is answered, immediately reassign the slot to proof development or adversarial verification. Never let open-ended computation consume the research budget.

## Persistence and resumability

Keep `research_state.md` current with the canonical target, verified facts, active branches, exact artifacts, failed ideas, unresolved proof obligations, and the next smallest checks. Save all citations and certificates by stable URL and hash where available.

At every interruption boundary, write a dated checkpoint. If the investigation is incomplete, end the checkpoint with the literal marker `CHECKPOINT_NOT_FINAL`, state what has and has not been established, and provide restart instructions tied to `research_state.md`. Do not convert partial progress, a solver timeout, a literature gap, or an unreviewed lemma into a solution claim.
