# Erdős Problem 96: verification-first audit of a claimed solution

## Definitions and canonical target

Let \(P=\{p_1,\ldots,p_n\}\subset\mathbb R^2\) be the vertex set of a strictly convex Euclidean \(n\)-gon: all points are distinct vertices of their convex hull and no three are collinear. Define
\[
u(P)=\bigl|\{\{p,q\}\subset P:\|p-q\|_2=1\}\bigr|,
\qquad f(n)=\max_{|P|=n}\nu(P).
\]
The target is to establish, or correctly reject the claimed establishment of, the assertion \(f(n)=O(n)\): there must exist absolute constants \(C,n_0\) such that \(\nu(P)\le Cn\) for every \(n\ge n_0\) and every such \(P\).

The immediate object of verification is Abhijeet Khopkar, *Edge complexity of geometric graphs on convex independent point sets*, arXiv:1605.08066v2 (2017), https://arxiv.org/pdf/1605.08066 . Its abstract and Theorem 4 claim exactly this linear upper bound. It is an unpublished preprint, not an accepted theorem for purposes of this project.

## Accepted background

- Füredi proved an \(O(n\log n)\) upper bound; Brass--Pach gave a short proof. Bibliographic primary links: https://doi.org/10.1016/0097-3165(90)90074-7 and https://doi.org/10.1006/jcta.2000.3133.
- Aggarwal proved the verified explicit upper bound \(f(n)\le n\log_2 n+4n\): *On unit distances in a convex polygon*, Discrete Mathematics 338 (2015), 88--92, https://www.sciencedirect.com/science/article/pii/S0012365X14003847 ; preprint https://arxiv.org/abs/1009.2216. Its distance-matrix approach uses the diagonal and obtuse-angle properties of convex quadrilaterals.
- Edelsbrunner--Hajnal proved that for every \(n\ge4\), some convex \(n\)-gon has at least \(2n-7\) unit-distance pairs: https://www.sciencedirect.com/science/article/pii/009731659190042F . This is a lower bound and disproves an earlier stronger \(5n/3+O(1)\) upper conjecture; it does not disprove linearity.
- In the centrally symmetric subcase, Ábrego--Fernández-Merchant proved a linear bound (in particular \(f_{sym}(n)\le2n-3\)): https://www.csun.edu/~ba70714/publications/unit.pdf . This is not a proof for arbitrary convex polygons.
- The current database record remains OPEN: https://www.erdosproblems.com/96 . Its 2026 forum thread records the Khopkar paper as an unconfirmed claimed solution: https://www.erdosproblems.com/forum/thread/96 . Treat both the database label and the forum assessment as evidence to investigate, not as proofs.

## Complete resolutions

For this verification project, either of these two outcomes is complete:

1. A self-contained, line-by-line validated proof that Khopkar's argument, perhaps with explicitly supplied valid repairs, proves \(f(n)\le Cn\) with an absolute \(C\). Every imported lemma must be stated precisely and cited. This resolves Erdős Problem 96 affirmatively.
2. A rigorous invalidation of the claimed proof: identify the earliest unsupported or false lemma/inference, state its exact hypotheses and conclusion, and give a concrete counterexample or a decisive explanation that the conclusion does not follow. Record which later claims then fail. This completes the verification audit but leaves the mathematical problem open under the verified \(n\log_2n+4n\) bound.

A genuine mathematical disproof of the original problem is also logically possible, but requires an infinite family \(P_k\) of strictly convex polygons with \(\nu(P_k)/|P_k|\to\infty\), not merely a dense finite example.

## What does not count as a solution

- A finite search over polygons, numerical diagrams, or checks for small \(n\).
- Restating the 2017 abstract or accepting a diagrammatic argument without a formalized case analysis.
- Re-proving \(O(n\log n)\), proving a special symmetric case, or giving a bound whose constant depends on the polygon.
- Proving sparsity of a larger/smaller abstract graph class without proving that the precise geometric UDG reduction preserves the hypotheses and loses only \(O(n)\) edges.
- Claiming \(2n\) is the answer without proving that stronger statement; it is not required for \(O(n)\).

## Required correctness checks

1. Use unordered pairs and exact Euclidean distance \(1\); do not switch to unit-disk graphs or arbitrary unit-distance subgraphs.
2. Audit strictness of every angle inequality and every convexity inference, including endpoints, equality cases, and cyclic order.
3. In the Khopkar proof, independently verify the antipodal-line cut, the assertion that only \(O(n)\) edges are discarded, the split into the two GUDG graphs, and the ordering conventions.
4. Do not infer a linear result from path-restricted ordered bipartite graphs alone: the paper itself gives \(\Theta(n\log n)\) for that broader class.
5. Audit the special GUDG argument in Section 5: module definitions, auxiliary edges, charging/counting statements, and the use of Lemmas 10--13 leading to Theorem 4. Check that each abstract configuration is geometrically realizable or that realizability is not being silently assumed.
6. For every purported repair, re-run all downstream lemmas under the repaired hypotheses. A repair that changes a quantifier, deletes superlinearly many edges, or only treats generic configurations is insufficient.

## Required deliverables

- `research_state.md` containing the current theorem-dependency graph, citation log, verified/failed/open status for each lemma, and exact next checks.
- A proof-audit report with page/lemma references to arXiv:1605.08066v2, a compact restatement of every nontrivial lemma used, and a verdict for each.
- If valid: a standalone polished proof of \(f(n)=O(n)\), with an explicit absolute constant if derivable, plus an adversarial audit appendix.
- If invalid: a minimal counterexample or detailed gap certificate, including coordinates/combinatorial data when applicable and an explanation of why it satisfies every stated hypothesis.
- A literature update limited to primary or official sources; distinguish peer-reviewed papers, preprints, and forum discussion. Give direct URLs and access dates.

## Dynamic Multiagent v2 protocol

Maintain one research root responsible for `research_state.md`, provenance, dependency tracking, and final integration. Use at most four concurrent agents. Begin with independent approaches rather than fixed roles: agents may choose a proof-dependency audit, a geometric counterexample search to one exact lemma, a literature/publication-status audit, or an adversarial reconstruction. Register each approach before substantial work in an approach registry containing its target claim, assumptions, expected certificate, and stop condition.

Work in multiple waves. In the first wave, maximize independence and require each result to name the exact paper location and logical dependency it affects. In later waves, dynamically reuse slots for the most consequential unresolved lemma; do not preserve a static assignment once an approach has concluded. Every proposed proof or repair must receive adversarial checking by an agent that did not produce it. The root must merge only statements whose hypotheses, constants, and degenerate cases have been checked.

Use proof-first allocation. At most one optional computational subtask may run at a time, and only after declaring: (i) the exact lemma or candidate configuration it tests, (ii) the mathematical hypotheses encoded, (iii) the certificate expected from either outcome, and (iv) a finite stopping condition. Computation may expose a counterexample or validate bookkeeping for a finite lemma; it cannot establish the asymptotic theorem by sampling. Reassign that slot immediately when its declared question is answered.

## Persistence and resumability

Update `research_state.md` after every meaningful lemma check, source inspection, counterexample attempt, or change of verdict. Include a dated checkpoint with: current global status, dependency graph, citations accessed, exact unresolved claims, failed attempts, and the next smallest check.

If a runtime boundary arrives before either complete audit outcome, do not issue a solution claim. Save the state and return `CHECKPOINT_NOT_FINAL`, identifying the first unchecked dependency and the evidence required to settle it.
