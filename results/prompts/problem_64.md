# Erdős Problem 64 — Erdős–Gyárfás conjecture

## Definitions and canonical target

Work with finite, nonempty, simple, undirected graphs.  For a graph \(G\), write \(\delta(G)\) for its minimum vertex degree.  A cycle always means a simple cycle, and its length is its number of edges (equivalently vertices).

Prove or disprove the following statement:

> For every finite simple undirected graph \(G\) with \(\delta(G)\ge 3\), there are an integer \(k\ge2\) and a simple cycle \(C\subseteq G\) with \(|C|=2^k\).

Thus the allowed cycle lengths are \(4,8,16,32,\ldots\).  The exponent and cycle may depend on \(G\).  No connectedness assumption is made or needed.

A negative resolution must give one explicit finite simple graph \(G\) with \(\delta(G)\ge3\) that has no simple cycle of every allowed length \(2^k\le |V(G)|\).

## Accepted background

The following are accepted only with the stated scope; do not silently strengthen them.

1. Liu and Montgomery proved that there is an absolute average-degree threshold forcing a cycle whose length is a power of two.  This disproves the historical stronger conjecture that counterexamples exist at arbitrarily large minimum degree; it does **not** settle the fixed threshold \(\delta(G)\ge3\).  Their article is peer-reviewed in JAMS 36 (2023), 1191–1234: https://arxiv.org/abs/2010.15802 and https://wrap.warwick.ac.uk/id/eprint/171505/.
2. Gao and Shan proved the conjecture for \(P_8\)-free graphs, in fact producing a 4- or 8-cycle: https://arxiv.org/abs/2109.01277.
3. Hu and Shen extended that restricted-class result to \(P_{10}\)-free graphs: https://arxiv.org/abs/2308.05675.
4. Hegde, Sandeep, and Shashank report a computer-assisted proof for \(P_{13}\)-free graphs.  This is a preprint, not a general theorem: https://arxiv.org/abs/2410.22842.  Accompanying code is at https://github.com/rbsandeep/Erdos-Gyarfas.
5. Carr proved the diameter-2 subclass (a 4- or 8-cycle) in a preprint accepted for BICA: https://arxiv.org/abs/2508.19302.  A later preprint derives conditional degree structure for a hypothetical minimal counterexample: https://arxiv.org/abs/2605.22844.
6. The official current problem record is https://www.erdosproblems.com/64.  Its Lean file is only a statement containing `sorry`, not a proof: https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/64.lean.

Before relying on any source, inspect its theorem statement and distinguish a peer-reviewed theorem, a preprint claim, a computational experiment, and a conjectural remark.

## Complete resolutions

An affirmative resolution is a complete proof for every finite simple graph \(G\) with \(\delta(G)\ge3\), including arbitrary order and disconnected graphs.

A negative resolution is an explicit finite simple graph \(G\), plus independently checkable evidence that:

1. every vertex has degree at least 3; and
2. for every integer \(k\ge2\) with \(2^k\le |V(G)|\), \(G\) has no simple cycle of length \(2^k\).

For a negative resolution, provide the graph in a canonical machine-readable format and an independently reproducible certificate or verifier.

## What does not count as a solution

- A proof only for a named subclass such as cubic, planar, claw-free, diameter-2, \(P_t\)-free, or sufficiently high average/minimum degree.
- A graph without 4-cycles, or even without 4- and 8-cycles, if it has a 16-, 32-, or other permitted cycle.
- An infinite graph, a multigraph, a graph with loops, or an object whose conventions differ from finite simple graphs.
- A closed walk that repeats vertices rather than a simple cycle.
- A computation over graphs up to a specified order, unless the work proves that this bounded domain exhausts the mathematical target.
- A claimed reduction that loses the minimum-degree hypothesis, changes cycle length, or proves only average-degree information.
- A Lean declaration with `sorry`, an unverified forum post, or a search-result snippet.

## Required correctness checks

1. State graph conventions before every reduction and verify that all transformations preserve simplicity and the needed minimum-degree condition.
2. For every constructed cycle, list why it is simple and calculate its exact length; “even” or “close to a power of two” is insufficient.
3. For a minimal-counterexample argument, justify the chosen minimality order and every use of it.  In particular, deletion typically lowers neighboring degrees and cannot be treated as harmless.
4. For a counterexample, check every \(2^k\le |V(G)|\), not just the smallest powers.  Provide an independent cycle enumerator or a formally specified verifier.
5. For computer-assisted lemmas, prove search-space completeness, isomorphism handling, pruning validity, induced-path conventions, and stopping condition.  Preserve raw logs, source revision, compiler/environment, and exact input hashes.
6. Audit all imported literature claims against their primary sources.  Do not infer the \(\delta\ge3\) theorem from Liu–Montgomery's high-average-degree theorem.

## Required deliverables

- `research_state.md`: dated source ledger, exact target, approach registry, currently live lemmas, failed approaches, proof dependencies, and next actions.
- A literature memo separating verified theorems from preprints, computational claims, and conjectures, with direct URLs and access dates.
- Either a complete proof manuscript or an explicit counterexample package as defined above.
- A proof-audit document that checks every nontrivial inference and explicitly addresses all six correctness checks.
- If computation is used, a reproducibility package with the declared lemma, hypotheses, finite domain, stopping condition, code hash, command line, raw output, and an independent verification path.
- A final status note saying exactly whether the general conjecture was proved, disproved, or remains unresolved.

## Dynamic Multiagent v2 protocol

Create one research root that owns `research_state.md`, the source ledger, and an append-only approach registry.  Use at most four concurrent agents total, including any coordinator role.  Begin with early independence: agents should initially investigate incompatible proof-level avenues rather than duplicate a preferred technique.

For every live approach, register: target lemma; assumptions; relation to the full theorem; anticipated falsifier; dependencies; verification plan; and a concrete stop/reassign condition.  Do not allocate an agent merely to summarize literature already recorded.

Operate in waves.  After each wave, an adversarial checker reviews proposed lemmas, searches for hidden degree loss and cycle-length errors, and decides whether a slot is continued, redirected, or released.  Reuse released slots dynamically for the strongest unresolved bottleneck, a genuinely independent route, or proof auditing.  Never use more than four concurrent agents, and never freeze a static assignment when evidence changes.

Proof-first allocation is mandatory.  At most one optional computational subtask may run at once.  Before it starts, the registry must state a precise lemma or counterexample property, all hypotheses, the finite search domain, a completeness argument or explicit non-exhaustive label, and a stopping condition.  Once that question is answered, immediately stop the computation and reassign its slot to proof construction or adversarial checking.  Computation may test a rigorously delimited lemma or certify an explicit graph; it may not substitute for a proof of the universal conjecture.

Every claimed decisive advance must receive an adversarial proof check by an agent not responsible for the original argument.  The check must attempt counterexamples, inspect quantifiers, verify simple-cycle status and exact powers of two, and trace each external theorem to a source.

## Persistence and resumability

Update `research_state.md` whenever a source is verified, a lemma changes status, a computation starts/stops, or an approach is retired.  Include enough detail for a new agent to reproduce the current state without relying on chat history.

If a runtime boundary interrupts an unfinished investigation, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, followed by: the exact canonical target; verified sources; active and rejected approaches; all unverified claims; computation status; and the next smallest proof-first action.  Do not report a resolution after such an interruption.  On resumption, first audit the checkpoint and refresh time-sensitive literature before opening new approaches.

All citations in any final manuscript or audit must use direct primary or authoritative URLs, give publication/preprint status, and identify precisely which statement each source supports.
