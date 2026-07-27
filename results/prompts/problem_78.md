# Erdős Problem 78 — revised, strongly explicit Ramsey-graph target

## Definitions and canonical target

A finite simple graph \(G\) has clique number \(\omega(G)\) and independence number \(\alpha(G)\).  Call \(G\) \(K\)-Ramsey if \(\max\{\omega(G),\alpha(G)\}<K\).  Let \(R(k)\) be the least \(n\) for which every red/blue edge-colouring of \(K_n\) contains a monochromatic \(K_k\); equivalently, every \(n\)-vertex graph has a clique or independent set of size \(k\).

The historical wording says “constructive proof” but does not define it.  Work on the following repaired standard target unless the research root records a different, user-approved model:

Prove that there are absolute constants \(c>0\), \(N_0\), and one uniform deterministic algorithm \(A\) such that, for every \(N\ge N_0\) and distinct \(u,v\in[N]\), \(A(N,u,v)\) decides whether \(uv\in E(G_N)\) in time \(\operatorname{poly}(\log N)\), where \(G_N\) is a simple graph satisfying
\[
\max\{\alpha(G_N),\omega(G_N)\}<c\log_2 N.
\]

Then derive, with constants displayed, that \(R(k)>C^k\) for some fixed \(C>1\) and every sufficiently large integer \(k\).  A graph family available only on a stated cofinal size sequence is acceptable only if the proof includes a valid reduction/padding argument to the Ramsey-number conclusion.

## Accepted background

- Erdős’s 1947 probabilistic argument proves an exponential existence lower bound for diagonal Ramsey numbers, but does not provide the required explicit family: [Some Remarks on the Theory of Graphs](https://doi.org/10.1090/S0002-9904-1947-08785-1).
- Cohen proved an explicit \(K\)-Ramsey construction with \(K=2^{(\log\log N)^c}\), for an absolute \(c>0\): [SIAM Journal on Computing version](https://epubs.siam.org/doi/10.1137/16M1096219).  This is a theorem, not the desired conclusion.
- Li’s FOCS 2023 theorem gives explicit \(K\)-Ramsey graphs with \(K=\log^{O(1)}N\): [FOCS DOI](https://doi.org/10.1109/FOCS57990.2023.00075), [open preprint](https://arxiv.org/abs/2303.06802).  The hidden exponent is not known from this statement to be one; do not cite it as an \(O(\log N)\)-Ramsey construction.
- Literature distinguishes a global explicit construction from a very/strongly explicit construction with local \(\operatorname{poly}(\log N)\)-time adjacency; see the definition discussion in [Gopalan](https://www.cs.umd.edu/~gasarch/TOPICS/CRT/GopRam.pdf).  The target above deliberately requires the latter.

No source above is a proof of the target.  Treat any claimed post-2023 improvement as unaccepted until a primary paper, preprint, or formal artifact is inspected and its parameters are checked.

## Complete resolutions

An affirmative resolution must supply all of the following:

1. A fully specified uniform family \(G_N\) and local deterministic adjacency algorithm.
2. A proved \(\operatorname{poly}(\log N)\) runtime bound, including parameter encoding and any preprocessing assumptions.
3. A proof for every sufficiently large claimed \(N\) that both \(\alpha(G_N)\) and \(\omega(G_N)\) are less than \(c\log_2N\), with an absolute \(c\).
4. A correct derivation of \(R(k)>C^k\) for all sufficiently large \(k\).

A negative resolution must be a genuine impossibility theorem in this declared strong-explicit model, with all model assumptions stated.  Alternatively, if authoritative problem stewardship specifies that unbounded computability was intended, document that decision and prove the weaker formulation by a terminating exhaustive-search construction plus the relevant existence bound; label it as a statement repair, not as a resolution of the strong-explicit problem.

## What does not count as a solution

- Repeating the random-graph/probabilistic existence proof.
- A finite search, numerical experiment, or heuristic that works for selected sizes only.
- A \(\log^dN\)-Ramsey family for fixed \(d>1\), including the currently known Li-type bound.
- A construction that controls cliques but not independent sets, or vice versa.
- A bipartite result without a proved conversion to a non-bipartite graph preserving the needed parameters.
- Declaring an exponentially slow enumeration “explicit” without an approved weak model.
- A claim of adjacency computability that silently uses an exponentially large table, nonuniform advice, random bits, or unproved oracle.

## Required correctness checks

- State the graph model: vertex labels, graph size, symmetry, and absence of loops.
- Track every logarithm base and all absolute constants through the \(N\)-to-\(k\) conversion.
- Check quantifiers: constants independent of \(N,k\); construction for all sufficiently large sizes or a justified padding reduction.
- Prove both homogeneous-set obstructions, using complementation correctly.
- For extractor/disperser routes, prove the exact parameter transfer: source entropy, error/disperser property, monochromatic rectangle exclusion, bipartite-to-non-bipartite conversion, and the final \(K\) exponent.
- Distinguish theorem statements verified in primary sources from conjectural extrapolations or informal claims.
- Perform adversarial review aimed specifically at accidental \(\log^{O(1)}N\) notation hiding an exponent greater than one.

## Required deliverables

Produce:

1. `research_state.md` with the selected construction model, current status, source log, approach registry, and unresolved lemmas.
2. A self-contained proof manuscript or impossibility proof, with theorem/lemma dependencies and explicit constants.
3. A machine-readable or human-checkable description of the adjacency algorithm and complexity analysis.
4. A parameter ledger mapping each cited theorem’s input to its output; cite direct primary URLs for every imported result.
5. An adversarial proof-audit report listing every attempted counterexample, parameter mismatch, and repaired gap.
6. If incomplete, a checkpoint report that states exactly which lemma remains unproved and why no claimed result exceeds the known \(\log^{O(1)}N\) baseline.

## Dynamic Multiagent v2 protocol

Create a research root that maintains the single authoritative `research_state.md`.  Use at most four concurrent agents, including the root.  Begin with independent approaches rather than a fixed division of mathematical labor: each agent must first register a falsifiable approach, its required lemmas, source dependencies, and a predicted failure mode in the approach registry.

Run multiple waves.  In wave one, prioritize independent reconstruction of the parameter barrier, alternative construction ideas, and a hostile statement/model audit.  The root compares results, kills duplicate lines, and reuses freed slots dynamically for the most discriminating next lemma.  Every proposed proof is assigned an adversarial checker who did not author that proof; the checker must try complements, boundary sizes, hidden nonuniformity, and extractor-parameter substitutions.

Do not freeze roles or methods.  Reassign agents when an approach is refuted, a lemma is proved, or a source check changes the landscape.  Before accepting any claimed advance, record it in the registry with: exact proposition, assumptions, proof location, verifier, known dependency chain, and whether it improves the exponent all the way to one.  The root alone merges claims after adversarial review.

Proof-first allocation is mandatory.  At most one optional computational subtask may run at a time.  Before it runs, write in `research_state.md` the exact lemma or counterexample question, hypotheses, finite search domain, certificate format, and stopping condition.  Reassign that slot immediately after the question is answered; computation may not substitute for an asymptotic proof.

## Persistence and resumability

Update `research_state.md` after every wave and before any context/runtime boundary.  It must contain: canonical target and model, verified sources with URLs and dates, rejected claims, live lemmas, completed proof fragments, failed approaches, and the current approach registry.

If the investigation stops before a complete resolution, output `CHECKPOINT_NOT_FINAL` and preserve enough detail for another root to resume without repeating source verification.  Never present a checkpoint, a finite construction, or an unverified paper claim as a solution.
