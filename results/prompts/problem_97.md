## Definitions and canonical target

Work in the Euclidean plane. A convex polygon is a finite nondegenerate polygon whose vertices are in convex cyclic order; state explicitly whether strict convexity is used and prove it for every proposed construction. Let \(V(P)\) be its vertex set.

Determine whether the following statement is true:

> For every finite convex polygon \(P\), there is a vertex \(v\in V(P)\) such that, for every \(r>0\),
> \[
> |\{w\in V(P)\setminus\{v\}: |v-w|=r\}|\leq 3.
> \]

Equivalently, disprove it by producing one convex polygon in which every vertex has at least four distinct other vertices at a common distance from it. The radius may depend on the vertex.

## Accepted background

The current record is [Erdős Problems 97](https://www.erdosproblems.com/97), with [LaTeX source](https://www.erdosproblems.com/latex/97). It reports, but does not itself replace primary-source checking of, the following historical facts:

- Erdős's 1946 threshold-3 conjecture was refuted by a Danzer 9-vertex convex construction.
- Fishburn and Reeds, [*Unit distances between vertices of a convex polygon*](https://doi.org/10.1016/0925-7721(92)90008-2), *Computational Geometry* (1992), gave a 20-vertex construction in which each vertex has three equidistant other vertices, with a common distance.
- The current record questions a 1975 attribution that Danzer had constructions for every threshold. Treat that attribution as unverified unless the original source is inspected.
- Dropping convexity yields easy unit-distance-graph counterexamples; they are irrelevant to the target.

The threshold-3 constructions are theorems/background only after their exact statements have been inspected. The threshold-4 statement is the conjectural target; do not treat it as known from the database label or the formalization marker.

## Complete resolutions

An affirmative resolution is a complete proof that every finite convex polygon has a vertex all of whose distance classes have size at most three.

A negative resolution is an explicit finite convex polygon \(P\), together with for every \(v\in V(P)\) four distinct witnesses \(w_1,\ldots,w_4\) and an exact \(r_v>0\) satisfying \(|v-w_i|=r_v\), plus a proof of convexity and of every equality.

If the investigation instead uncovers a prior complete proof or counterexample, convert the task to verification: identify the exact theorem, inspect the proof, and check that it matches this target rather than a stronger common-radius or nonconvex variant.

## What does not count as a solution

A figure, floating-point experiment, database label, search snippet, forum claim, or uninspected citation does not settle the problem. Neither does a configuration that works only at selected vertices, has only three equal-distance neighbours, is nonconvex, has an unproved cyclic order, or uses four equal segments not all incident with the relevant vertex.

Do not confuse four vertices equidistant from \(v\) with four vertices mutually equidistant. Do not replace “at least four” by “exactly four.” A common radius for all central vertices is optional and would be a stronger counterexample, not the required one.

## Required correctness checks

For an affirmative proof, verify the full quantifier order: \(P\) is arbitrary; \(v\) may depend on \(P\); and every radius at that \(v\) is controlled.

For a counterexample, provide exact coordinates or an exact symbolic construction, certify the cyclic order and convexity, make the four witnesses distinct for each central vertex, and verify the squared-distance identities exactly. Audit any use of strict convexity, collinearity exclusions, symmetry reductions, and limiting arguments.

Check every historical claim against a primary or authoritative source. Record publication status and distinguish a theorem from a conjecture, a database annotation, or an informal assertion.

## Required deliverables

Deliver a self-contained proof or exact counterexample certificate if the target is resolved. Otherwise deliver:

1. a source ledger with direct links, inspected locations, publication status, and exact claims;
2. a statement audit distinguishing strict/non-strict convexity and at-least/exactly-four readings;
3. an approach registry containing attempted invariants, construction families, and failure modes;
4. rigorously stated lemmas, including proofs or precisely marked gaps;
5. a short status report separating verified facts from conjectural leads.

All citations must link to the primary paper, preprint, official record, or formal artifact actually inspected. Do not cite a search result as evidence.

## Dynamic Multiagent v2 protocol

Create a research root and maintain an approach registry. Use at most four concurrent agents. In the first wave, allocate independent investigations among the historical primary sources, current literature/formalization, affirmative structural approaches, and counterexample-construction approaches. Register each approach, its target lemma, assumptions, source basis, and falsification test before results are merged.

Use multiple waves. Reuse a freed slot dynamically for the most decision-relevant task: adversarial checking of a proposed lemma, checking a construction's exact certificate, resolving a source conflict, or pursuing a newly exposed independent route. Do not impose a fixed mathematical method or permanent agent role. Preserve incompatible approaches until a proof, counterexample, or rigorous obstruction eliminates one.

Run adversarial proof checking independently of the proposing agent. A checker must test quantifiers, convexity, degeneracies, exactness of equalities, and whether an asserted result addresses threshold 4 rather than threshold 3.

Use proof-first allocation. At most one computational subtask may run at a time, and only after the registry states its exact lemma or construction hypothesis, parameter space, arithmetic model, certificate format, and finite stopping condition. Upon finding a certificate or exhausting the declared search, terminate that computation and immediately reassign the slot.

## Persistence and resumability

Maintain `research_state.md` under the research root. It must record the canonical target, source ledger, approach registry, proved lemmas, rejected routes, pending proof checks, exact computation declaration if any, and next actions.

At every material transition, update the file with enough detail for a new agent to continue without repeating source work. If a runtime boundary interrupts an incomplete investigation, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`, state what is verified and what is not, and do not announce a mathematical resolution.
