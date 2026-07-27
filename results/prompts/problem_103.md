# Erdős Problem 103 — research prompt

## Definitions and canonical target

For every integer \(n\ge 2\), define
\[
D(n)=\inf\{\operatorname{diam}(A):A\subset\mathbb R^2,\ |A|=n,\ \|x-y\|\ge1\text{ for all distinct }x,y\in A\},
\]
where \(\operatorname{diam}(A)=\max_{x,y\in A}\|x-y\|\).  Let \(\mathcal M_n\) be the family of sets attaining \(D(n)\).  Two members are equivalent precisely when a Euclidean isometry of \(\mathbb R^2\), including a reflection, maps one to the other.  Put
\[
h(n)=|\mathcal M_n/\operatorname{Isom}(\mathbb R^2)|.
\]
Use an explicit extended-cardinal convention if it becomes relevant.

Canonical target: prove or disprove
\[
\forall K\in\mathbb N\ \exists N\in\mathbb N\ \forall n\ge N,\qquad h(n)\ge K.
\]
This is a question about exact global diameter minimizers under the weak separation constraint \(\|x-y\|\ge1\), not about near minimizers, a prescribed lattice, or packings in a preselected container.

## Accepted background

- Erdős posed the problem in 1994: [Erdős, *Some problems in number theory, combinatorics and combinatorial geometry*](https://eudml.org/doc/232764), *Mathematica Pannonica* 5(2), 261–269. The public PDF is [here](https://mathematica-pannonica.ttk.pte.hu/articles/mp05-2/mp05-2-261-269.pdf).
- The current curated record is [Erdős Problems #103](https://www.erdosproblems.com/103), with [LaTeX statement](https://www.erdosproblems.com/latex/103). It records that even eventual \(h(n)\ge2\) is unknown. This is a status record, not a proof that no overlooked literature exists.
- Bezdek and Fodor, [*Minimal Diameter of Certain Sets in the Plane*](https://doi.org/10.1006/jcta.1998.2889), *J. Combin. Theory Ser. A* 85 (1999), 105–111, study \(D(n)\). Its abstract reports exact small-\(n\) information through \(D(8)\), but it does not establish \(h(n)\to\infty\).
- The companion [Problem #99](https://www.erdosproblems.com/latex/99) concerns unit equilateral triangles in the same class of minimizers. Its triangular-lattice asymptotic discussion is contextual background only; it is neither a theorem about \(h(n)\) nor permission to restrict the target to lattice configurations.

Separate every theorem proved from any heuristic or conjecture. Do not infer multiplicity of exact minimizers from asymptotic packing density alone.

## Complete resolutions

An affirmative resolution is a complete proof that for every \(K\) there is \(N\) such that all \(n\ge N\) satisfy \(h(n)\ge K\).

A negative resolution is a proof of the exact negation: there is a fixed \(K\) such that for arbitrarily large \(n\), \(h(n)<K\). A uniform bound on \(h(n)\) is sufficient but is stronger than the logical negation.

## What does not count as a solution

- A table of \(D(n)\) or \(h(n)\) at finitely many \(n\).
- A numerical optimizer output, a local minimum, or a near-optimal configuration without a rigorous global certificate.
- Distinct labelled coordinate lists that are congruent after relabelling, rotation, translation, or reflection.
- A construction that is only asymptotically optimal, rather than proved to attain \(D(n)\) exactly.
- Growth of \(h(n)\) on a subsequence only.
- Proving eventual \(h(n)\ge2\): record it as a major advance, but do not label it a resolution of \(h(n)\to\infty\).

## Required correctness checks

1. State and preserve the quantifiers over every sufficiently large integer \(n\).
2. For each purported minimizer, prove global equality \(\operatorname{diam}(A)=D(n)\), not merely an upper bound.
3. Audit congruence against the full Euclidean isometry group, including reflection.
4. Keep \(\|x-y\|\ge1\) and exact diameter throughout; justify every normalization.
5. If using contact graphs, prove that graph realizability, rigidity, and the claimed global optimality are all valid; a graph enumeration alone is insufficient.
6. Clearly distinguish deductions from the cited results from new lemmas.
7. For any computational claim, use exact/validated arithmetic and publish a certificate that independently checks both exhaustive coverage and every pruning inequality.

## Required deliverables

- A concise theorem statement saying whether the target is proved, disproved, or remains open.
- A self-contained proof manuscript with all new lemmas, dependencies, and an explicit treatment of equality cases.
- A source log with direct URLs, bibliographic metadata, and a sentence identifying exactly what each source proves.
- A congruence and global-optimality audit for every key construction.
- If computation is used: source code, environment instructions, exact input/output, machine-checkable certificates where feasible, the declared lemma tested, and a verifier independent of the search implementation.
- A final scope statement separating any partial theorem from a complete resolution.

## Dynamic Multiagent v2 protocol

Maintain one research root responsible for the canonical statement, approach registry, proof integration, and stop/go decisions. Run at most four agents concurrently.

At the outset, pursue independent approaches rather than a fixed division of labor. Register each approach in `research_state.md` with: target lemma, assumptions, exact completion criterion, relation to the canonical target, evidence consulted, and falsification conditions. Avoid duplicating an existing approach unless it is an explicit adversarial check.

Use multiple waves. In each wave, retain only approaches with a precise proof obligation; reassign freed slots dynamically to the most informative unresolved lemma or to adversarial verification. At least one active or newly assigned slot in each substantive wave must challenge a leading argument by testing quantifiers, equality cases, congruence, and hidden use of asymptotic rather than exact optimality.

Before merging any proposed proof, an independent agent must reconstruct the argument from the stated lemmas, seek counterexamples to each nontrivial reduction, and report whether every conclusion is theorem-level, conditional, or heuristic. A claim of success requires this adversarial check plus citation verification. No agent may declare a solution from unverified numerical output or a secondary-source assertion.

Allocate resources proof-first. At most one optional computational subtask may run at any time. Before it starts, the registry must specify the exact finite lemma or counterexample question, hypotheses, exact arithmetic/certification method, and a stopping condition. Once that question is answered, immediately release and reassign the slot; do not expand computation opportunistically.

## Persistence and resumability

Maintain `research_state.md` after every material step. It must record the canonical target, verified sources, active and rejected approaches, proved lemmas with dependencies, open proof obligations, computation declarations/certificates, and next adversarial checks.

If runtime ends before a complete resolution has passed adversarial checking, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, preserve all evidence and unresolved gaps, and report only the verified partial state. Never convert an incomplete investigation, a computational observation, or a plausible lattice heuristic into a final mathematical claim.
