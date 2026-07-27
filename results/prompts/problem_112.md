# Erdős Problem 112: exact oriented-graph Ramsey numbers

## Definitions and canonical target

For integers a,b >= 2, an oriented graph is a finite loopless digraph with at most one directed arc between each unordered pair of distinct vertices. An independent set I_a is a set of a vertices with no arc in either direction between any two of them. Let L_b be the transitive tournament on b vertices: its vertices admit an order v_1,...,v_b and its arcs are exactly v_i -> v_j for i<j.

Define k(a,b)=r(I_a,L_b) as the least N such that every oriented graph on N vertices contains I_a or L_b. Determine k(a,b) exactly for every a,b >= 2. Boundary conventions are k(1,b)=k(a,1)=1.

Do not replace this with the directed-path variant. Do not allow anti-parallel arcs. If a source uses a different convention, state the difference and do not transfer its theorem without proof.

## Accepted background

- Erdős and Rado (1967) gave fixed-b polynomial upper bounds; the current problem record states k(a,b)<= [2^(b-1)(a-1)^b+a-2]/(2a-3). Source: https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms/s1-42.1.624
- Larson and Mitchell (1997) studied these digraph Ramsey numbers and obtained improved estimates. Source: https://doi.org/10.1007/BF02558478
- Ihringer, Rajendraprasad, and Weinert proved r(I_4,L_3)=15, r(I_5,L_3)=23, r(I_a,L_3)=Theta(a^2/log a), and for fixed b>3, r(I_a,L_b)<=C_b a^(b-1)/(log a)^(b-2). These are theorems, not exact general formulas. Sources: https://arxiv.org/abs/1707.09556 and https://doi.org/10.1016/j.disc.2020.112268
- The 2021 paper identifies r(I_3,L_4) as a plausible next exact instance. This is a suggested restricted target, not a theorem and not a required method.

## Complete resolutions

A complete solution must prove an exact all-parameter characterization of k(a,b): an explicit formula, or a recurrence plus proved base cases and a terminating exact evaluation procedure, or an equally unambiguous theorem yielding every k(a,b). It must include both:

1. a universal proof that every oriented graph on k(a,b) vertices contains I_a or L_b; and
2. for every pair a,b, a certified oriented graph on k(a,b)-1 vertices containing neither.

A legitimate negative audit resolution of the unqualified literal wording would instead prove that an alternative convention makes k infinite, but that is not a resolution of the oriented-graph target.

## What does not count as a solution

- A fixed-b asymptotic, a one-sided bound, or a numerical table.
- A proof only for b=3, only for finitely many a, or only for a special graph class.
- A computer search without a complete instance encoding, exhaustive coverage proof, and independently checkable certificate.
- A directed-path proof or use of k(a,b)=(a-1)(b-1); that concerns another problem.
- An argument using bidirected arcs, an incomplete subtournament, or a merely acyclic induced subgraph in place of L_b.

## Required correctness checks

1. Verify every graph is oriented: no loops and no anti-parallel pair.
2. Verify I_a means no adjacency in either direction.
3. Verify each claimed L_b is complete on its chosen vertices and has a single transitive ordering.
4. For every lower-bound construction, supply a reproducible certificate for absence of both I_a and L_b.
5. For every upper bound, quantify over all N-vertex oriented graphs and check base cases and parameter ranges.
6. Keep exact equalities separate from O, Omega, and Theta assertions; state all dependence of constants.
7. Audit all Ramsey reductions for parameter order and inequality direction.
8. Cite primary sources with URLs and label theorem, conjecture, deduction, and computation separately.

## Required deliverables

- A concise research_state.md recording definitions, sources checked, active claims, attempted lemmas, and proof status.
- A proof manuscript or a precise restricted-result report, with every unproved statement labelled OPEN.
- A table separating verified theorems, new lemmas proved in the run, failed approaches, and unresolved gaps.
- For each construction or computation, a machine-readable encoding, verifier instructions, and a stopping condition.
- A bibliography with direct links, publication status, and page/theorem references where available.
- An adversarial audit that attempts to invalidate every claimed construction, induction, and convention transfer.

## Dynamic Multiagent v2 protocol

Create a research root that owns research_state.md and an approach registry. Use at most four concurrent agents total. In the first wave, assign genuinely independent lines of inquiry rather than a fixed division of a single proof; register each line with its target lemma, assumptions, expected falsifier, and source basis.

After each agent returns, the root updates the registry and reallocates slots dynamically. Retire duplicated or falsified approaches immediately. Each later wave must include at least one adversarial checker independent of the agent proposing the relevant claim. A checker receives the exact statement, all definitions, and all proof dependencies, and must report either a verified proof chain or a pinpointed gap.

Proof work has priority. At most one computational subtask may run at once, and only after the root records in research_state.md: the exact lemma or construction being tested, finite hypotheses, exhaustive search space, verifier, and stopping condition. Once that question is answered, terminate or repurpose that slot immediately; do not expand computation into open-ended value hunting.

Agents may propose a restricted theorem such as an exact small pair, but the registry must label it PARTIAL unless it satisfies the all-parameter completion test. Do not prescribe a single mathematical method; retain incompatible viable approaches until evidence eliminates them.

## Persistence and resumability

At every substantial result, update research_state.md with UTC time, source URLs, definitions in force, proof dependencies, counterexamples checked, and the next smallest unresolved obligation. Preserve failed approaches and their failure reason to prevent repetition.

If runtime ends before a complete resolution, do not present success. Write CHECKPOINT_NOT_FINAL in research_state.md, identify the current strongest verified result, list unverified claims separately, and give a concrete next action that can be resumed without rereading the full transcript.
