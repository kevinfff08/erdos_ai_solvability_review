# Erdős Problem 19: finite residual of the Erdős–Faber–Lovász conjecture

## Definitions and canonical target

For an integer \(n\ge 1\), let \(G\) be a finite simple graph with subgraphs \(C_1,\ldots,C_n\) such that each \(C_i\cong K_n\), the edge sets \(E(C_i)\) are pairwise disjoint, and \(E(G)=\bigcup_i E(C_i)\). Equivalently, the cliques may share vertices but any two share at most one vertex. Prove that \(\chi(G)=n\) for every such \(n,G\), or disprove it by an explicit counterexample.

The lower bound \(\chi(G)\ge n\) is immediate from any \(C_i\cong K_n\). Thus the substantive target is \(\chi(G)\le n\).

This is a revised target, not a fresh attempt at an unrestricted open conjecture. Kang, Kelly, Kühn, Methuku, and Osthus proved the assertion for every sufficiently large \(n\). Your first task is to audit that reduction and identify an effective threshold \(N\), or the exact finite reduction supplied by the proof. The residual target is then all \(13\le n<N\) not already covered by verified results.

## Accepted background

- Kang, Kelly, Kühn, Methuku, and Osthus, [A proof of the Erdős–Faber–Lovász conjecture](https://annals.math.princeton.edu/2023/198-2/p02), *Annals of Mathematics* 198(2), 537–618 (2023), proves the EFL assertion for every sufficiently large \(n\), and stability results. This is a theorem, not a proof for every \(n\).
- The corresponding [arXiv preprint](https://arxiv.org/abs/2101.04698) is useful for version comparison.
- Kang et al., [Algorithmic aspects](https://research.birmingham.ac.uk/en/publications/a-proof-of-the-erd%C3%B6s-faber-lov%C3%A1sz-conjecture-algorithmic-aspects/), FOCS 2022, give a randomized polynomial-time construction for the sufficiently-large regime. This does not close the finite residual.
- Kirchweger, Peitl, and Szeider, [A SAT Solver’s Opinion](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SAT.2023.13), SAT 2023, prove verified small cases: all \(n\le12\) and stated additional parameter ranges for \(13\le n\le18\), using independently checkable DRAT proofs. Treat their exact theorem statement as the authoritative coverage boundary.
- Kahn, [Coloring nearly-disjoint hypergraphs with \(n+o(n)\) colors](https://doi.org/10.1016/0097-3165(92)90096-D), JCTA 59 (1992), proves an asymptotic approximation only.
- The Erdős Problems [discussion thread](https://www.erdosproblems.com/forum/thread/19) describes the community-database status as “decidable rather than proved.” This is status context, not a substitute for proof checking.

You may use the equivalent linear-hypergraph/line-graph formulations only after writing the exact map and verifying that it preserves all hypotheses and the required colouring notion.

## Complete resolutions

An affirmative resolution must provide both:

1. a checked derivation from the Annals theorem of a concrete finite residual domain (or a valid exact alternative finite reduction); and
2. a rigorous proof covering every residual instance, with no unstated computational gap.

A negative resolution must provide one explicit \(n\), graph \(G\), and clique decomposition satisfying the canonical hypotheses, together with a proof that \(G\) is not \(n\)-colourable. A machine-assisted negative resolution must include a replayable, independently checkable unsatisfiability certificate.

## What does not count as a solution

- Restating that the theorem holds for sufficiently large \(n\).
- Treating a finite but unknown or impractically unspecified range as solved.
- Search exhaustion without complete isomorphism coverage and checkable proof logs.
- A colouring result for only one special class, one edge-count range, fractional colouring, or a changed hypergraph convention.
- A solver result whose symmetry-breaking constraints, encoding, certificate checker, or input-generation coverage cannot be audited.

## Required correctness checks

- State whether every graph edge is in one designated \(K_n\), and verify pairwise edge-disjointness of all designated cliques.
- Verify \(\chi(G)\ge n\) from a clique and separately verify the claimed \(n\)-colouring or non-colourability.
- If dualizing, define linearity, chromatic index, strong vertex colouring, the dual hypergraph, and the exact equivalence.
- Audit every invocation of the large-\(n\) theorem: its hypotheses, threshold, asymptotic quantifiers, effectiveness, and all parameter translations.
- For computation, validate the canonical augmentation/symmetry quotient, SAT encoding, DRAT proof checker, and a coverage theorem for all residual isomorphism classes.

## Required deliverables

1. `research_state.md` containing the current threshold/reduction status, exact source locations, checked lemmas, unresolved obligations, and command-independent certificate hashes.
2. A concise theorem ledger separating published theorems, conjectures, deductions, and computational claims.
3. Either a complete proof manuscript with a dependency graph, or an explicit counterexample plus a human-readable and machine-checkable non-colourability certificate.
4. A residual-coverage table listing every parameter family and its proof/certificate status; never infer unlisted coverage.
5. A bibliography with direct URLs, publication status, and page/theorem references for every externally used mathematical claim.

## Dynamic Multiagent v2 protocol

Maintain one research root and use at most four concurrent agents total. Start with independent approaches rather than fixed role assignments: one may audit the large-\(n\) reduction, another may seek structural finite reductions, another may examine certificates and encodings, and another may attempt adversarial counterexamples. Register every proposed approach in an approach registry containing its exact target lemma, assumptions, evidence, dependencies, and falsification test.

Work in multiple waves. At each checkpoint, compare approaches for overlap, retire routes contradicted by evidence, and reuse slots dynamically for the sharpest unresolved obligation. Every claimed lemma receives adversarial proof checking by an agent that did not originate it. No agent may promote a claim from “search evidence” to “theorem” without an inspectable proof or primary source.

Use proof-first allocation. At most one optional computational subtask may run at a time. Before it starts, record: the precise lemma or counterexample question, finite input domain, encoding, expected certificate type, stopping condition, and independent checker. Immediately reassign that slot when the stated question is answered; do not expand computation merely because hardware is available.

## Persistence and resumability

After every substantive result, update `research_state.md` with source URLs, exact theorem/section locations, attempted reductions, proof obligations, certificate locations and hashes, and the next smallest falsifiable task. Preserve failed approaches with their failure reason to prevent repetition.

If a runtime boundary occurs before a complete affirmative proof or verified counterexample, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, state exactly which completion condition remains unmet, and resume from the recorded obligation rather than issuing a conclusion.
