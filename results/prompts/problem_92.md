# Erdős Problem 92: verification of the claimed negative resolution

## Definitions and canonical target

For a finite set \(A\subset\mathbb R^2\) of distinct points and \(x\in A\), define
\[
d_A(x)=\max_{r>0}\bigl|\{y\in A\setminus\{x\}:\|x-y\|_2=r\}\bigr|,
\qquad F(A)=\min_{x\in A}d_A(x).
\]
For \(n\ge1\), let \(f(n)=\max_{|A|=n}F(A)\). The radius in \(d_A(x)\) may depend on \(x\).

Audit the claimed negative resolution of both assertions:

1. \(f(n)\le n^{o(1)}\), meaning that there is a function \(\varepsilon(n)\to0\) such that \(f(n)\le n^{\varepsilon(n)}\) eventually.
2. \(f(n)<n^{O(1/\log\log n)}\), meaning that there are constants \(C>0,N\) such that \(f(n)<n^{C/\log\log n}\) for every \(n\ge N\), where \(\log\log n>0\).

The verification target is the stronger certificate:
\[
\exists\alpha>0\ \exists\text{ infinitely many }m\quad f(m)\ge m^\alpha.
\]

## Accepted background

- The current [Erdős Problems page](https://www.erdosproblems.com/92) labels the problem disproved and states that the unit-distance disproof implies this result.
- [Planar Point Sets with Many Unit Distances](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf), Theorem 1.1, claims \(\nu(n)\ge n^{1+\delta}\) for a fixed \(\delta>0\) and infinitely many \(n\); its text immediately after the theorem explicitly identifies the Erdős--Fishburn stronger pointwise conjecture and invokes the minimum-degree-subgraph argument.
- [Sawin, *An explicit lower bound for the unit distance problem*](https://arxiv.org/abs/2605.20579) gives the explicit preprint statement that for arbitrarily large \(n\), an \(n\)-point set has at least \(n^{1.014114}/C\) ordered unit-distance pairs.
- [Alon et al., *Remarks on the disproof of the unit distance conjecture*](https://arxiv.org/abs/2605.20695) is a human-digested, human-verified preprint exposition.
- Earlier upper bounds remain valid background, not a solution: Pach--Sharir (1992) yields \(f(n)=O(n^{2/5})\); Janzer--Janzer--Methuku--Tardos ([arXiv:2411.07188](https://arxiv.org/abs/2411.07188), published in JLMS in 2025) yields \(f(n)=O(n^{4/11})\).
- The [Kim Morrison Lean repository](https://github.com/kim-em/erdos-unit-distance) claims a machine-checked formalization of a unit-distance uniform-bound disproof. Treat it as an artifact to build and audit, not as a substitute for checking the #92 reduction.

These sources establish claimed results, not a license to assume their proof details. No claim of peer-reviewed publication should be made for the 2026 arXiv/online manuscripts unless independently verified.

## Complete resolutions

A successful verification must establish one of these decisive outcomes.

- **Verified negative resolution:** verify a fixed \(\delta>0\) unit-distance lower bound for infinitely many \(n\), convert its pair count to a unit-distance graph of polynomial average degree, prove the pruning/core lemma, and derive an unbounded sequence \(m\) with \(f(m)\ge m^\alpha\) for a fixed \(\alpha>0\). Then explicitly prove this contradicts both canonical asymptotic assertions.
- **Failed claimed-resolution audit:** identify a precise invalid theorem dependency, convention mismatch, gap in the graph lemma, or failure of the subconfiguration translation. Explain exactly what then remains unverified. Do not infer that either original upper bound is true.

## What does not count as a solution

- A citation, database status, press release, forum comment, or assertion of expert review without an inspected mathematical chain.
- A configuration with many total equal-distance pairs but no proof that some retained point set has large minimum equal-distance degree.
- A numerical experiment, a finite graph drawing, or a construction for isolated small values of \(n\).
- An argument that uses different distances on individual edges without showing that each vertex has a single witness radius for all of its required neighbors.
- A proof of only the unit-distance statement while silently omitting the average-degree-to-minimum-degree reduction and the change from \(n\) to the retained cardinality \(m\).
- A Lean declaration, documentation page, or repository claim that has not been built under pinned dependencies and inspected for placeholders, extra axioms, or a mismatched theorem statement.

## Required correctness checks

1. State whether pair counts are ordered or unordered. Translate them correctly to \(\sum_v\deg(v)\), edge count, and average degree.
2. Prove the graph lemma: every finite graph of average degree at least \(2k\) has a nonempty subgraph of minimum degree at least \(k\). Give a deletion proof and handle rounding.
3. Let \(H\) be the resulting unit-distance subgraph. Verify that its vertex set is a valid planar subset and that every vertex has at least \(k\) other vertices at the common radius \(1\).
4. If \(|V(H)|=m\le n\), prove \(m\to\infty\) and correctly transfer a lower bound \(c n^\delta\) into \(m^\alpha\) for some fixed \(\alpha>0\), absorbing constants only after specifying a threshold.
5. Prove separately that a fixed positive power along an unbounded sequence negates both the \(o(1)\)-exponent and \(O(1/\log\log n)\)-exponent claims.
6. For every cited theorem, record title, author, version/date, URL, exact theorem/line location, publication status, and whether it was inspected rather than inferred from an abstract.
7. If using formalization, build it from a clean checkout with its declared toolchain; report the exact commit, command, exit status, dependency provenance, `sorry`/axiom audit, and whether the code covers the #92 reduction itself.

## Required deliverables

Produce:

1. A concise verdict: `VERIFIED_NEGATIVE_RESOLUTION`, `GAP_FOUND`, or `INCONCLUSIVE`.
2. A self-contained proof-audit note for the reduction from the verified unit-distance theorem to \(f(m)\ge m^\alpha\), with all constants and quantifiers exposed.
3. A source ledger separating peer-reviewed papers, preprints, formal artifacts, and informal reports.
4. A dependency graph naming every nontrivial imported theorem and marking each as inspected, formally checked, or unverified.
5. If a gap is found, a minimal counterexample to the claimed inference or a precisely located missing lemma; do not replace it with speculation.
6. If the audit is incomplete, a checkpoint with the last verified claim and the next falsifiable task.

## Dynamic Multiagent v2 protocol

Create a research root that owns the canonical definitions, source ledger, approach registry, and final consistency check. Use at most four concurrent agents total, including the root when it performs active work.

Start with independent approaches rather than fixed roles: register each proposed approach before substantial work, including its target claim, dependencies, anticipated certificate, and failure condition. Suitable independent directions include source-theorem inspection, a fully elementary graph-reduction audit, formal-artifact rebuilding, and adversarial quantifier/constant checking; do not require all of them or prescribe a mathematical method.

Run in multiple waves. In the first wave, assign distinct unblocked approaches. At each merge, the root compares claims against the registry, eliminates duplicated work, and requires adversarial checking of any proposed proof by an agent that did not produce it. Reuse a freed slot immediately for the highest-risk unresolved dependency, a counterexample search against the current chain, or source-version verification. Never exceed four concurrent agents.

Proof-first allocation is mandatory. At most one optional computational subtask may run at a time. Before it starts, the registry must state the exact lemma/hypotheses it tests, the finite certificate sought, and a stopping condition. End and reassign that slot as soon as the stated question is answered; computation may not substitute for an asymptotic proof.

## Persistence and resumability

Maintain `research_state.md` at the research root. It must list: canonical statement; current verdict; source URLs and version dates; inspected theorem locations; active approach registry; verified lemmas; open risks; commands and outcomes for any formal build; and the next smallest falsifiable task.

After every merge or material discovery, update `research_state.md`. If a runtime boundary interrupts work before one of the decisive audit outcomes, write `CHECKPOINT_NOT_FINAL` at the top of that file, preserve all evidence and failed approaches, and return only the checkpoint status with the next verification step. Do not present an incomplete audit as confirmation of the disproof.
