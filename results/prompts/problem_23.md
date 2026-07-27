# Erdős Problem 23 — exact max-cut / bipartization conjecture

## Definitions and canonical target

All graphs are finite, simple, and undirected. Let \(n\ge 1\) be an integer. For a graph \(G\), define

\[
\beta(G)=\min\{|F|:F\subseteq E(G),\ G-F\text{ is bipartite}\}.
\]

Equivalently, \(\beta(G)=e(G)-\operatorname{maxcut}(G)\), where \(\operatorname{maxcut}(G)\) is the maximum number of edges crossing a bipartition of \(V(G)\).

Prove or disprove:

> For every triangle-free graph \(G\) with \(|V(G)|=5n\), \(\beta(G)\le n^2\).

Equivalently, \(G\) has a spanning bipartite subgraph with at least \(e(G)-n^2\) edges. No vertices may be deleted.

The balanced blow-up \(C_5[n]\) has five independent classes of size \(n\), complete bipartite graphs exactly between cyclically consecutive classes, and satisfies \(\beta(C_5[n])=n^2\). Thus the proposed constant is sharp.

## Accepted background

- The current database record remains open: [Erdős Problems #23](https://www.erdosproblems.com/23). Treat this as a status index, not a proof.
- Balogh, Clemen, and Lidický prove the global bound \(\beta(G)\le N^2/23.5\) for an \(N\)-vertex triangle-free graph and the sharp \(N^2/25\) bound in two density ranges for sufficiently large \(N\): [arXiv:2103.14179](https://arxiv.org/abs/2103.14179). Their sharp conjecture is \(\beta(G)\le N^2/25\); at \(N=5n\) this is the target above.
- Ferudun's recent, unrefereed computer-assisted preprint claims \(a(5n)=n^2\) for \(1\le n\le40\), with ancillary exact-arithmetic material: [arXiv:2606.28041](https://arxiv.org/abs/2606.28041). This is partial progress only. Independently validate any use of its certificate or transfer lemmas.
- The statement, rather than a proof, appears in Lean with `sorry`: [FormalConjectures/23.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/23.lean).
- Historical sources include [Erdős–Faudree–Pach–Spencer (1988)](https://combinatorica.hu/~p_erdos/1988-12.pdf) and [Erdős–Győri–Simonovits (1992)](https://korandi.org/docs/misc/erdos_gyori_simonovits.pdf).

Clearly label every imported statement as proved, claimed in an unreviewed preprint, or conjectural. In particular, do not assume a stability classification of near-extremizers.

## Complete resolutions

An affirmative resolution is a rigorous proof for every positive integer \(n\) and every triangle-free \(G\) on exactly \(5n\) vertices that \(\beta(G)\le n^2\). It must cover all remaining \(n\), including \(n\ge41\), unless finite cases are imported from independently verified results.

A negative resolution is one explicit positive integer \(n\) and triangle-free graph \(G\) on \(5n\) vertices with \(\beta(G)>n^2\), together with a proof that every cut has fewer than \(e(G)-n^2\) crossing edges.

## What does not count as a solution

- Any bound \(\beta(G)\le c n^2\) with \(c>1\).
- A result only in one density range, for sufficiently large \(n\), for a graph subclass, or for finitely many values of \(n\), unless the omitted cases are proved separately.
- The C5 blow-up lower bound: it proves sharpness conditional on the upper bound, not the universal upper bound.
- A computational search without a proved finite reduction covering every possible counterexample.
- A floating-point flag-algebra output without exact, independently checkable certificates and a sound graphon-to-finite deduction.
- Deleting vertices, altering \(|V(G)|=5n\), or changing the problem to a balanced-cut requirement.

## Required correctness checks

1. Maintain the normalization \(N=5n\): \(N^2/25=n^2\) only under this equality.
2. Check triangle-freeness, simplicity, and exact vertex count for every construction.
3. Prove the maximum-cut/bipartization equivalence used at each step.
4. Count all edges left inside both parts of any proposed cut.
5. Verify every strict/non-strict density endpoint when importing a density-tail theorem or applying a blow-up limit.
6. If using induction or minimal counterexamples, prove a strengthened formulation that handles vertex-count remainders rather than silently assuming divisibility persists.
7. Audit equality cases and do not infer a uniqueness/stability theorem from the C5 example.
8. For any computer-assisted lemma, preserve source, input encoding, exact certificates, hashes, verifier command, output, and an independent rerun.

## Required deliverables

Deliver a dossier containing: the exact target and status; a source log with direct URLs and publication status; a dependency-ordered proof or counterexample; full proofs of every new lemma; a boundary/equality audit; an adversarial audit of each pivotal inference; and a clearly separated incomplete-results section if no resolution is achieved.

For computational work, include the predeclared finite lemma, hypotheses, stopping condition, code, certificates, reproducible command, and independent verification result. Cite primary papers or official repositories, never search snippets.

## Dynamic Multiagent v2 protocol

Create a research root containing `research_state.md`, `approach_registry.md`, source notes, proof drafts, certificate records, and adversarial reviews. Use at most four concurrent agents.

Begin with independent approaches rather than fixed assignments. Before substantial work, each agent registers an approach identifier, exact target lemma or counterexample condition, hypotheses, dependencies, expected falsifier, and evidence standard. Possible directions include source/certificate audit, minimal-counterexample reductions, cut inequalities, stability structure, or one bounded computational test; none is mandatory.

Work in multiple waves. At the end of each wave, update the registry with evidence, derivations, rejected claims, unresolved dependencies, status (`live`, `blocked`, `refuted`, `merged`), and the next falsifiable milestone. Reuse released slots dynamically for the highest-value open dependency. Before merging a pivotal result, assign an adversarial reviewer to test normalization, hidden asymptotics, equality cases, circularity, and explicit small constructions.

Use proof-first allocation. At most one optional computational subtask may run at once. Before it starts, record the exact lemma/hypothesis, finite family, certificate, and stopping condition. Stop immediately once that question is answered and reassign the slot; computation may guide or certify a finite lemma but cannot replace a universal proof.

## Persistence and resumability

Update `research_state.md` whenever a source is inspected, a claim changes status, a proof dependency is added, or a certificate is run. Record exact URLs, versions, hashes, commands, assumptions, and unresolved objections.

If a runtime boundary interrupts an incomplete investigation, place `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`. Preserve partial arguments as unproved, record active approaches and the next adversarial check, and resume by auditing that state before creating new claims. Never present partial numerical evidence, an unreviewed preprint assertion, or an unchecked certificate as a complete solution.
