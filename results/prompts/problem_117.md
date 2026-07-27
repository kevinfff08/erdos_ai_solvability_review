# Erdős Problem 117 — statement-repair and target-selection audit

## Definitions and canonical target

For a group \(G\), define
\[
\alpha(G)=\sup\{|S|:S\subseteq G,\;xy\ne yx\text{ for all distinct }x,y\in S\}.
\]
For \(n\in\mathbb N\), \(n\ge1\), the condition in the historical problem is \(\alpha(G)\le n\). Let
\[
\beta(G)=\min\{|\mathcal A|: \mathcal A\text{ is a finite family of abelian subgroups of }G,\;G=\bigcup_{A\in\mathcal A}A\}.
\]
Define \(h(n)\) as the least integer \(H\) such that \(\beta(G)\le H\) for every group \(G\) with \(\alpha(G)\le n\).

The phrase “estimate \(h(n)\) as well as possible” is not itself a proposition with a unique terminal proof. This investigation must first produce a source-backed repair proposal choosing exactly one target, such as:

1. an exact formula for \(h(n)\);
2. existence and evaluation of \(\lim_{n\to\infty}\log h(n)/n\);
3. matching explicit exponential bases; or
4. a sharp theorem for a named, properly defined class of groups.

Do not silently choose one. State which target is selected, why it is a faithful repair, and what remains a different open target.

## Accepted background

- B. H. Neumann proved that a group has no infinite pairwise noncommuting subset if and only if its centre has finite index: [Neumann 1976](https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/problem-of-paul-erdos-on-groups/43D46201BABB2E6319B72C008DC3F42B). Thus the unrestricted-group formulation reduces to centre-by-finite groups.
- Pyber proved that, for a finite group with \(\alpha(G)\le n\), \(|G:Z(G)|\le c^n\) for an absolute \(c\): [Pyber 1987](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms/s2-35.2.287). The problem record and an accessible scan of Erdős’s 1997 chapter report exponential lower and upper bounds for \(h\), but do not state optimal bases: [record](https://www.erdosproblems.com/117), [original chapter scan](https://rexresearch1.com/ErdosMath/Combinatorics%2C%20Geometry%20and%20Probability%20A%20Tribute%20to%20Paul%20Erd%C3%B6s.pdf).
- For each representative \(g\) of a coset of \(Z(G)\), \(\langle Z(G),g\rangle\) is abelian and covers that coset. This elementary observation converts an index bound into an abelian-subgroup cover.
- Results for special families, including \(\mathrm{GL}_d(q)\), are not automatically universal extremal results: [Azad–Iranmanesh–Praeger–Spiga](https://arxiv.org/abs/1004.3402).
- Treat the 2025 work on higher noncommuting subsets as adjacent only; it does not, from its accessible abstract, settle the universal \(h(n)\) problem: [Yang–Zarrin 2025](https://doi.org/10.1017/S0004972724001370).

Label every use of these items as theorem, transparent deduction, conjecture, or unverified lead. Do not claim an Isaacs lower-bound theorem until its primary source is located and inspected.

## Complete resolutions

For this statement-repair mode, complete either one of the following audit outcomes.

1. **Repaired research target accepted.** Give one exact mathematical target, its full quantifiers, its relationship to \(h(n)\), and a source-backed rationale that it is the intended next question. Then provide a proof or a cited verification that it is already closed; otherwise label it open.
2. **No unique target justified.** Demonstrate that at least two inequivalent targets (for example, exact values versus an exponential rate) are compatible with the historical wording and current literature, and that no authoritative source selects one. Recommend the minimal human decision needed to proceed.

A later proof project is complete only if it proves the selected target in both directions where appropriate. For an exact formula, prove both the universal upper bound and matching examples. For a rate \(\lambda\), prove the stated limit, not merely unrelated exponential bounds.

## What does not count as a solution

- Repeating that \(h(n)\) lies between unspecified exponentials.
- Solving a finite list of groups or a single family without a theorem transferring it to all groups in the selected target.
- Giving a cover by cosets, arbitrary subsets, or nonabelian subgroups.
- Confusing \(\alpha(G)\), \(\beta(G)\), \(|G:Z(G)|\), maximal-by-inclusion sets, and maximum-cardinality sets.
- Suppressing the infinite-group quantifier without invoking and checking the Neumann reduction.
- Claiming that a better numerical bound is “best possible” without a matching obstruction under the same normalization.
- Treating an informal post, search snippet, computation, or inaccessible citation as proof.

## Required correctness checks

1. Restate all definitions before each claimed theorem and check \(n\ge1\).
2. Verify every candidate lower-bound family has \(\alpha(G)\le n\), not merely a large centre quotient or a large order.
3. Verify every claimed cover contains all elements and every member is a subgroup and abelian.
4. Audit all conversions between centre index, clique size, and cover number with explicit inequalities and constants.
5. If quotient arguments are used, check that lifting preserves the property asserted; do not assume preimages of abelian quotient subgroups are abelian.
6. Separate finite-family asymptotics from the universal supremum defining \(h(n)\).
7. For any claimed historical attribution or current-status change, inspect a primary paper, formal artifact, or detailed proof; cite a stable URL and publication status.
8. Have an adversarial reviewer try to falsify the result using central elements, direct products, small \(n\), and the distinction between graph colouring and clique number.

## Required deliverables

- `statement_repair.md`: original wording, canonical definition, the selected target or a justified refusal to select one, and all boundary conventions.
- `literature_audit.md`: annotated bibliography with direct links, publication status, what each source proves, and an explicit post-2023 search log.
- `proof_or_gap.md`: either a complete proof of the selected target or a lemma-by-lemma account of the unresolved gap; no prose that blurs the two.
- `counterexample_and_edge_cases.md`: checks of \(n=1\), infinite groups, quotient lifting, and all proposed extremal families.
- `approach_registry.md`: live registry required below.
- `research_state.md`: current target, completed checks, citations, failed ideas, next proof obligation, and the exact command or source needed to resume.

## Dynamic Multiagent v2 protocol

Create a research root that owns `research_state.md` and `approach_registry.md`. Use at most four concurrent agents, including any coordinator.

Work in multiple waves. In the first wave, independently explore incompatible lines: source/statement reconstruction, universal upper-bound mechanisms, lower-bound/extremal-family mechanisms, and adversarial verification. Do not force these into a shared mathematical method.

Before claiming a lemma, register it in `approach_registry.md` with: identifier, precise statement, hypotheses, intended role, source or derivation, status, and a designated adversarial check. Avoid duplicate work by checking the registry, but preserve genuinely incompatible approaches.

At every wave boundary, the root compares evidence, retires disproved paths, and reuses freed slots for the most valuable unresolved proof obligation. No fixed permanent assignments are allowed. Reserve a slot for adversarial proof checking whenever a nontrivial proposed theorem appears; the checker must attempt counterexamples and verify quantifiers independently.

Allocate proof work before computation. At most one optional computational subtask may run at any time, and only after its owner writes: the exact lemma or conjecture it tests, the finite family and hypotheses, the certificate format, and a stopping condition. On reaching that stopping condition, record the result and immediately reassign the slot to proof, source verification, or adversarial checking. Computation may generate evidence or an exact finite certificate; it cannot establish a universal asymptotic statement without a proved transfer theorem.

## Persistence and resumability

Update `research_state.md` after each material source check, proof attempt, counterexample, or agent-wave decision. Include URLs, theorem numbering where available, definitions in force, and unresolved dependencies so that a later agent can reproduce the state without relying on chat history.

If a runtime boundary occurs before the selected target is resolved or rejected, do not present a solution. Save the best verified state, identify the next smallest proof obligation, and end the report with `CHECKPOINT_NOT_FINAL`.
