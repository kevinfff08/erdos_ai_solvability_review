# Erdős Problem 62: common 4-chromatic subgraphs

## Definitions and canonical target

Work in ZFC. A graph is simple, undirected, and loopless. Its chromatic number \(\chi(G)\) is the least cardinality of a proper vertex colouring. A graph \(H\) is a subgraph of \(G\) when there is an injective map \(e:V(H)\to V(G)\) taking every edge of \(H\) to an edge of \(G\); this is **not** induced-subgraph containment.

Canonical weak target:

\[
\forall G_1,G_2\;[\chi(G_1)=\chi(G_2)=\aleph_1\Rightarrow
\exists H\;(\chi(H)=4\ \land\ H\hookrightarrow G_1\ \land\ H\hookrightarrow G_2)].
\]

The graph \(H\) may depend on the pair and may be finite or infinite. Do not replace \(\chi(G_i)=\aleph_1\) by a different cardinal hypothesis.

A separately labelled stronger target replaces \(\chi(H)=4\) by \(\chi(H)=\aleph_0\). Do not conflate the two. The extension from two graphs to an arbitrary finite family is also separately stronger and is not an automatic iteration.

## Accepted background

The following are accepted only with their stated scope.

- **Theorem (Erdős–Hajnal–Shelah, 1974):** every graph with \(\chi(G)>\aleph_0\) contains all sufficiently long odd cycles. Therefore every pair of \(\aleph_1\)-chromatic graphs has a common 3-chromatic subgraph. This does not produce a 4-chromatic one. Source: [Erdős–Hajnal–Shelah (1974)](https://www.renyi.hu/~p_erdos/1974-17.pdf).
- **Known finite-spectrum facts:** Komjáth–Shelah report the Erdős–Hajnal classification of fixed finite graphs unavoidable in every uncountably chromatic graph, and develop consistency constructions with delayed finite high-chromatic witnesses. Source: [Komjáth–Shelah (2005)](https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.20060).
- **Theorem (Lambie-Hanson, 2020):** for every \(f:\mathbb N\to\mathbb N\), there is a \(\chi=\aleph_1\) graph in which every subgraph with fewer than \(f(k)\) vertices has chromatic number below \(k\). Hence there is no uniform bound on the size of a finite 4-chromatic witness across all such graphs. This is an obstacle, not a disproof of the pair-dependent target. Source: [published paper](https://doi.org/10.1016/j.aim.2020.107176) and [preprint](https://arxiv.org/abs/1902.08177).
- **Restricted theorem, not a solution:** for stable graphs of chromatic number greater than \(\beth_2(\aleph_0)\), Halevi–Kaplan–Shelah prove a version of strong Taylor's conjecture. It does not apply to arbitrary \(\chi=\aleph_1\) graphs. Source: [JEMS paper](https://ems.press/journals/jems/articles/11115712).
- The historical formulation is recorded at [Erdős Problems 62](https://www.erdosproblems.com/latex/62) and independently in [the UCSD archive](https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/FourChromaticSubgraph.html). These are problem records, not proofs.

No cited source above proves or refutes the canonical 4-chromatic pair target.

## Complete resolutions

An affirmative resolution must give a ZFC proof of the canonical quantified statement and verify both embeddings and \(\chi(H)=4\).

A negative resolution must give, in ZFC, explicit graphs \(G_1,G_2\) with \(\chi(G_1)=\chi(G_2)=\aleph_1\), and prove that every graph embedding into both has chromatic number different from 4. A result in a forcing extension or under \(\diamondsuit\), CH, or another extra axiom is not a ZFC disproof; it may instead be part of a rigorously stated independence resolution if the complementary consistency result is also established.

The \(\chi(H)=\aleph_0\) and finite-family variants require their own complete-resolution statements and proofs.

## What does not count as a solution

- A common odd cycle, or any common 3-chromatic graph.
- Separate 4-chromatic subgraphs in \(G_1\) and \(G_2\) without an isomorphism type occurring in both.
- A common homomorphic image, minor, quotient, or induced-subgraph statement unless it is converted into the required non-induced embeddings.
- A proof only for stable graphs, a named construction class, or a larger chromatic threshold.
- A result that silently changes \(\chi=\aleph_1\) to \(\chi>\aleph_0\), or conversely.
- A model-specific forcing construction presented as a theorem of ZFC.
- Finite enumeration with no theorem reducing the universal infinite problem to that enumeration.

## Required correctness checks

1. State every use of choice, forcing, diamond, CH, or cardinal-arithmetic assumption.
2. Audit the exact quantifier order: \(H\) may depend on the pair, but not separately on an embedding claim that yields different graphs \(H\).
3. Prove \(\chi(H)=4\) exactly. A lower bound \(\chi(H)\ge4\) and a separate colouring bound must be justified.
4. Check that both maps are injective edge-preserving embeddings; do not require or assume preservation of nonedges.
5. Check that each proposed counterexample has chromatic number exactly \(\aleph_1\), not merely an unverified uncountable or large chromatic number.
6. If using the EHS odd-cycle theorem, retain its graph-dependent threshold and explain why any attempted 4-chromatic analogue follows.
7. Before accepting any claimed solution, run an adversarial proof audit aimed at hidden cardinal changes, induced/non-induced confusion, and a switch from relative consistency to ZFC.

## Required deliverables

- A one-page canonical statement and notation sheet.
- A source ledger with direct URLs, precise theorem statements, publication status, and a theorem/conjecture/heuristic label for each item.
- An approach registry recording attempted invariants, hypotheses, overlap with prior approaches, and a falsification test.
- Either a complete proof/counterexample with lemma dependencies, or a rigorous barrier report identifying the first unproved lemma and why all checked routes stop there.
- For any set-theoretic construction, a full assumption ledger and a proof that the asserted chromatic numbers and non-embedding property hold in the intended universe.
- A final adversarial referee report written by an agent that did not author the main argument.

## Dynamic Multiagent v2 protocol

Maintain a research root that owns the canonical statement, source ledger, approach registry, and `research_state.md`. Use at most four concurrent agents total, including the research root.

Run multiple waves rather than fixed roles. In the first wave, allocate independent approaches only after each records a distinct testable claim in the approach registry; suitable directions may include spectrum-intersection lemmas, analysis of the EHS threshold argument, and counterexample invariants for canonical uncountably chromatic constructions. Do not prescribe a single mathematical method.

At every handoff, the registry must record: target variant, assumptions, exact proposed lemma, evidence, dependency status, and whether the route has been falsified. If two approaches converge, merge their evidence and free a slot. Reuse freed slots dynamically for source verification, a genuinely independent approach, or adversarial checking.

Before a proof is treated as progress, assign an adversarial agent to try to break its exact cardinal hypothesis, embedding notion, and use of any auxiliary axiom. Before a counterexample is accepted, assign an adversarial agent to search for a possible common 4-chromatic subgraph or a flaw in the chromatic-number proof.

Use proof-first resource allocation. At most one optional computational subtask may run at a time, and only after the research root records: (i) the exact lemma or finite obstruction being tested, (ii) all hypotheses linking it to the infinite target, (iii) the certificate to be returned, and (iv) a stopping condition. Computation may not be used as evidence for the unrestricted theorem without that bridge. As soon as the finite question is answered, immediately reassign that slot to proof work or checking.

## Persistence and resumability

Update `research_state.md` after each meaningful source check, lemma attempt, counterexample attempt, or adversarial review. Include the canonical target, source URLs, assumptions, live and rejected approaches, proof dependency graph, and next falsifiable tasks.

If a runtime boundary occurs before a complete resolution or a rigorous barrier report, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`. State exactly what has been checked, what remains unverified, which claims are only conjectural, and the next actions for a later wave. Never present a checkpoint as a solution.
