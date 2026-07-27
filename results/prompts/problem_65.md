# Erdős Problem 65 — statement repair and evidence verification

## Definitions and canonical target

Work with finite simple undirected graphs. Let

\[
\mathcal C(G)=\{\ell\geq3:C_\ell\subseteq G\},\qquad
L(G)=\sum_{\ell\in\mathcal C(G)}\frac1\ell,
\]

where each *distinct cycle length* is counted once.

Do **not** attempt to solve the literal web statement as a current open problem. Under its natural universal fixed-\(n\), fixed-edge-count reading it is false: for \(n=5\), \(e(G)=5\), the graph \(C_5\) is admissible, but no complete bipartite graph has both five vertices and five edges (\(s(5-s)\in\{0,4,6\}\)).

The target is to repair and audit the intended exact extremal question. The leading candidate formulation, reported by Richard Montgomery, is:

> For integers \(1\le d\le n/2\), among all \(n\)-vertex graphs \(G\) with \(e(G)\ge d(n-d)\), is \(L(G)\) minimized exactly by \(K_{d,n-d}\)?

For this candidate, \(\mathcal C(K_{d,n-d})=\{4,6,\ldots,2d\}\) and
\[
L(K_{d,n-d})=\sum_{j=2}^{d}\frac1{2j}=\tfrac12(H_d-1).
\]

Before any proof search, determine whether this is the historically intended formulation or whether a fixed-\((n,m)\) formulation with necessary rounding conventions is required.

## Accepted background

- Gyárfás, Komlós and Szemerédi proved a logarithmic lower bound for all cycle lengths: [On the distribution of cycle lengths in graphs (1984)](https://www.renyi.hu/~gyarfas/Cikkek/20_GyarfasKomlosSzemeredi_OnTheDistributionOfCycleLengthsInGraphs.pdf).
- Liu and Montgomery proved the asymptotically sharp general lower bound \(L(G)\ge(1/2-o_d(1))\log d\); publication details are [JAMS 36 (2023), 1191–1234](https://doi.org/10.1090/jams/1018).
- Montgomery’s peer-reviewed 2025 survey states that forthcoming work with Aleksa Milojević, Alexey Pokrovskiy, and Benny Sudakov proves the displayed exact target for all sufficiently large \(d\): [Cycles and expansion in graphs, p. 8](https://ems.press/content/serial-article-files/52107). Treat this as an **unverified author report**, not as an available proof: obtain a manuscript or publication and audit it before relying on it.
- The Erdős Problems page contains a transcription error: it says “maximised” in its remark, whereas the author survey says “minimised”: [Problem 65](https://www.erdosproblems.com/65).

## Complete resolutions

A complete statement-repair outcome must do one of the following.

1. Establish from primary historical sources the exact intended quantifiers and parameter convention, state the corrected theorem/conjecture unambiguously, and prove or rigorously verify the applicable result.
2. If the corrected target is the \(e(G)\ge d(n-d)\) formulation, provide either:
   - a complete proof for every declared admissible \((n,d)\) that \(L(G)\ge\tfrac12(H_d-1)\), with equality classification; or
   - one admissible explicit counterexample with exact edge count and an exact or certified value of \(L(G)\).
3. Separately verify the claimed sufficiently-large-\(d\) theorem from its full proof. Verification must identify its threshold/range, its edge inequality, all rounding assumptions, and the exact equality statement.

The already-known literal closure must also be reported: \(n=5,e=5\) refutes the unqualified complete-bipartite optimizer sentence.

## What does not count as a solution

- Treating the literal statement as true by silently restricting to feasible \(K_{s,n-s}\) parameters.
- Citing a survey assertion, a forum post, or “forthcoming work” as a proof.
- Reproving only \(L(G)\gg\log d\) or \((1/2-o(1))\log d\).
- Computing examples without a proved reduction to a finite set of cases.
- Counting cycles rather than distinct cycle lengths.
- Proving only a non-strict lower bound while omitting equality/uniqueness, if the repaired target asserts exact minimization.
- Interchanging \(e(G)=d(n-d)\) and \(e(G)\ge d(n-d)\), or suppressing integrality and part-size restrictions.

## Required correctness checks

- Verify that every candidate complete bipartite graph has the same vertex and edge parameters as the optimization class.
- Check \(K_{d,n-d}\) only under \(d\le n-d\), and derive its cycle-length set explicitly.
- Keep the finite-simple-graph convention throughout; do not admit multicycles, loops, or repeated cycle lengths.
- In every structural reduction, prove that deleting edges/vertices does not invalidate the relevant density threshold or reverse the monotonicity argument for \(L\).
- Audit any claimed large-\(d\) proof line by line at each use of expansion, a consecutive-even-cycle interval, and the equality case.
- For a counterexample, certify \(|V|\), \(e\), every cycle length used to calculate \(L\), and the comparison value exactly.

## Required deliverables

1. `statement_audit.md`: original literal wording, the \(n=5,e=5\) closure, all viable repaired formulations, and a justified choice of canonical target.
2. `source_log.md`: direct URLs, authors, dates, publication status, exact theorem statements, and a separate label for unproved announcements.
3. `proof_audit.md`: either a full verification of the large-\(d\) manuscript or a precise list of inaccessible/unverified steps.
4. `resolution.md`: a proof, a certified counterexample, or a clearly delimited `CHECKPOINT_NOT_FINAL` status.
5. If computation is used, a reproducible certificate containing the formal finite domain, code/version, exhaustive stopping condition, and independently checked output.

## Dynamic Multiagent v2 protocol

Maintain one research root and at most four concurrent agents total. Begin with genuinely independent lines of inquiry rather than a fixed division of mathematical methods. Record each attempted route in an approach registry with: target formulation, assumptions, source dependencies, current lemma, falsifiable milestone, status, and owner.

Use several waves. In the first wave, prioritize source recovery/statement reconstruction, independent audit of the literal counterexample and parameter feasibility, and proof-structure reconnaissance. In later waves, dynamically reuse freed slots for the most informative unresolved issue. Do not retain a slot for a completed or blocked task.

Every proposed proof receives adversarial checking by an agent that did not produce it. The checker must test quantifiers, extremal class membership, monotonicity, cycle-length-versus-cycle multiplicity, boundary values \(d=1,2\), and equality claims. Disagreement must be logged and resolved with direct evidence rather than majority vote.

Allocate resources proof-first. At most one optional computational subtask may run at a time. Before it runs, the registry must declare the exact lemma or counterexample question, the finite hypotheses, and its stopping condition. Immediately reassign that slot once the stated question is answered. Computation may guide a proof or produce a finite certificate, but may not substitute for an all-parameter theorem.

## Persistence and resumability

Keep `research_state.md` continuously updated with the canonical formulation currently under test, source URLs and access status, approach registry, verified lemmas, rejected arguments, open proof obligations, and reproducibility data.

At each handoff or runtime limit, write enough state for a new team to resume without repeating source discovery. If the investigation is incomplete, output `CHECKPOINT_NOT_FINAL` prominently, identify the single next blocking verification, and do not present an unverified forthcoming theorem as established.
