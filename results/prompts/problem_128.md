# Erdős Problem 128 — sparse halves in triangle-free graphs

## Definitions and canonical target

Work with finite simple undirected graphs.  For a graph \(G=(V,E)\), write \(n=|V|\), and for \(S\subseteq V\) write \(e_G(S)=|E(G[S])|\).  A triangle means a copy of \(K_3\).

Prove or disprove the following exact statement:

> For every finite triangle-free simple graph \(G\) on \(n\) vertices, there exists \(S\subseteq V(G)\) with \(|S|=\lfloor n/2\rfloor\) and \(e_G(S)\le n^2/50\).

This is equivalent to the original local-density form: if every \(S\subseteq V(G)\) with \(|S|\ge\lfloor n/2\rfloor\) has \(e_G(S)>n^2/50\), then \(G\) contains a triangle.  Checking exactly \(\lfloor n/2\rfloor\) vertices suffices by monotonicity of induced edge counts.

Do not conflate this discrete target with a fractional-half relaxation.  In Razborov's notation a fractional half is \(\mu:V(G)\to[0,1]\) with total weight \(n/2\); for odd \(n\), its minimizer can have one weight \(1/2\).  A proved fractional upper bound \(\beta(G)\le1/50\) implies the discrete target, but that implication must be written out when used.

## Accepted background

- The original database record and bibliography are at [Erdős Problems 128](https://www.erdosproblems.com/latex/128).
- Erdős, Faudree, Rousseau and Schelp (1994) prove a general local-density criterion which, at \(\alpha=1/2\), yields the weaker \(n^2/16\) threshold; bibliographic record: [Erdős publication list](https://www.oakland.edu/Assets/upload/docs/Erdos-Number-Project/erdpubs.2010.pdf).
- Krivelevich, *On the Edge Distribution in Triangle-free Graphs*, JCTB 63 (1995), 245–260, is verified at the [author publication page](https://www.math.tau.ac.il/~krivelev/papers.html).
- Keevash and Sudakov, [*Sparse halves in triangle-free graphs*](https://www.sciencedirect.com/science/article/pii/S0095895605001644), JCTB 96 (2006), prove the target under \(|E(G)|\le n^2/12\) or \(|E(G)|\ge n^2/5\).
- Norin and Yepremyan, [*Sparse halves in dense triangle-free graphs*](https://arxiv.org/abs/1311.5818), establish further high-degree/high-average-degree and Petersen-neighborhood cases; the published version is JCTB 115 (2015), 1–25.
- Razborov, [*More about sparse halves in triangle-free graphs*](https://www.mathnet.ru/links/0062fe3a56efc9141ab3ee6dfdb710e6/sm9615_eng.pdf), Sbornik: Mathematics 213(1) (2022), proves the general fractional bound \(\beta(G)\le27/1024\), and proves the \(1/50\) target for several classes, including girth at least 5, independence number at least \(2n/5\), strongly regular graphs, and graphs with no induced \(2K_2\).  This is background, not a solution of the general target.
- A Lean statement exists in [FormalConjectures/ErdosProblems/128.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/128.lean), but its theorem body contains `sorry`; it is not a formal proof.

Treat every claimed theorem above as a theorem only within its stated hypotheses.  Treat the general \(1/50\) assertion as open unless you locate and inspect a later complete proof or counterexample.

## Complete resolutions

An affirmative resolution must give a rigorous proof, for every finite \(n\) and every finite triangle-free simple \(G\), of a set \(S\) with \(|S|=\lfloor n/2\rfloor\) and \(e_G(S)\le n^2/50\).  It must explicitly handle parity and any reduction from weighted/fractional halves.

A negative resolution must give one explicit finite triangle-free simple graph \(G\), plus an exact certificate that every \(S\subseteq V(G)\) of size \(\lfloor n/2\rfloor\) satisfies \(e_G(S)>n^2/50\).  The certificate must be independently reproducible.  Equality at \(n^2/50\) does not disprove the problem.

## What does not count as a solution

- A bound with any larger constant, including \(27/1024\), or a result with \(o(n^2)\) slack.
- A proof only for a special class, a density range, sufficiently large \(n\), or an asymptotic graph-limit statement with no finite transfer.
- A numerical SDP output, floating-point inequality, or failed heuristic counterexample search without an exact certificate and a declared stopping condition.
- A proof about crossing edges, arbitrary subgraphs, or weighted halves that never proves the required induced discrete-half statement.
- C5/Petersen blow-ups showing sharpness at equality without satisfying the strict universal counterexample condition.

## Required correctness checks

1. State every quantifier and retain \(n=|V(G)|\) in every normalization.
2. Check the direction and strictness of every inequality: affirmative uses \(\le\), while a counterexample requires \(>\) for every half.
3. Use induced edges \(e_G(S)\), not arbitrary selected edges or a cut size.
4. Check \(\lfloor n/2\rfloor\) for odd \(n\), including any conversion from a fractional half.
5. Check candidate lemmas on C5, Petersen, Clebsch, and relevant balanced blow-ups symbolically before using them as universal claims.
6. For a flag-algebra/SDP proof, provide exact rational data, a verifiable PSD certificate, coefficient identities, and the finite-graph transfer argument.  Floating-point feasibility is discovery evidence only.
7. For an explicit counterexample, independently verify triangle-freeness and exhaust all half-sized subsets using a transparent exact method or a symmetry-reduced proof with its orbit argument.
8. Before declaring resolution, conduct a fresh literature/status search and distinguish a verified paper or formal artifact from a database label, abstract, or forum assertion.

## Required deliverables

- `research_state.md` recording the canonical target, sources checked, active approaches, rejected lemmas, exact open gaps, and reproducible commands/certificates.
- A source ledger with direct URLs, publication/preprint status, accessed date, and a sentence identifying exactly what each source proves.
- A proof manuscript or counterexample certificate with all definitions and parity cases.
- An adversarial audit report listing every dependency, each inequality direction, all finite exceptions, and independent checks performed.
- If no complete resolution is obtained, a concise checkpoint that separates proved lemmas, falsified routes, conjectural observations, and the next bounded task.

## Dynamic Multiagent v2 protocol

Use a research root that maintains `research_state.md`, an approach registry, a source ledger, and a queue of proof obligations.  Run at most four agents concurrently.

Begin with independent reconnaissance rather than a fixed assignment: agents may investigate status/literature, structural reductions, analytic inequalities, exact verification, or counterexample mechanisms, but must register a precise claim, dependencies, and a falsification test before substantial work.  Do not require a common method.

Use multiple waves.  At each wave boundary, the research root compares evidence, merges only independently checkable results, and dynamically reuses freed slots for the highest-value unresolved obligation.  Retire routes once their stated falsification test fails; do not keep agents repeating equivalent searches.

Maintain an approach registry with: identifier, exact target lemma or counterexample condition, assumptions, status, evidence location, known obstruction, and next check.  Every promising proof is assigned an adversarial checker independent of its author.  Checkers must try parity failures, strictness reversals, invalid averaging, hidden asymptotics, and extremal-template counterexamples.

Allocate resources proof-first.  At most one optional computational subtask may run at once.  Before it begins, record the precise lemma/hypotheses it tests, input family, exact arithmetic/certificate format, and stopping condition.  Immediately release and reassign that slot when the question is answered.  Computation may discover a lemma or certify a finite exhaustive claim; it may not substitute for a universal proof.

## Persistence and resumability

After each meaningful action, update `research_state.md` with citations, exact statements, proof status, counterexamples considered, and a reproducible next action.  Preserve failed approaches because they prevent duplicated work.

If runtime ends before a complete affirmative proof or an exact counterexample certificate has been independently checked, write `CHECKPOINT_NOT_FINAL` at the top of the current status section.  State the last verified result, the unverified inference that remains, and the next smallest proof obligation.  Never present a partial bound, numerical observation, or unreviewed agent claim as a resolution.
