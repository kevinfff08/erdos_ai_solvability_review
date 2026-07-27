# Erdős Problem 108 research task

## Definitions and canonical target

Work with finite simple graphs. For a graph X, chi(X) is its ordinary vertex chromatic number. Its girth is the length of a shortest cycle; define girth(X)=infinity when X is acyclic.

A subgraph H of G is ordinary, not necessarily induced: vertices and edges may both be deleted. Thus H must satisfy V(H) subseteq V(G) and E(H) subseteq E(G). This convention is essential.

For r>=4 define h_r(G)=max{chi(H): H is a subgraph of G and girth(H)>=r}. Prove or disprove the following canonical target:

For every integers r>=5 and k>=2, there exists F(k,r) such that every finite simple graph G with chi(G)>=F(k,r) has h_r(G)>=k.

The r=4 case is accepted background, so the task is the genuinely remaining r>=5 target. A disproof must fix one r>=5 and one k>=2 and provide graphs G_n with chi(G_n)->infinity but h_r(G_n)<k for every n.

## Accepted background

- Rödl, "On the chromatic number of subgraphs of a given graph," Proceedings of the American Mathematical Society 64(2), 370-371 (1977), DOI: https://doi.org/10.1090/S0002-9939-1977-0469806-4. Its clique-or-triangle-free theorem yields the r=4 case under the ordinary-subgraph convention.
- The current Erdős Problems record lists the full finite statement as open and distinguishes a stronger infinitary question: https://www.erdosproblems.com/108 and https://www.erdosproblems.com/forum/thread/108.
- Pettie, Tardos, Walczak, "On a Clique Game and the Erdős-Hajnal Problem on High-Chromatic High-Girth Subgraphs," SODA 2026, pp. 2903-2927, DOI: https://doi.org/10.1137/1.9781611978971.108. This is a theorem, not a resolution: it gives a tower-type lower bound via Burling graphs for girth 5.
- Li, "The Erdős-Hajnal High-Girth Subgraph Conjecture Holds in the Polynomial Chromatic-Sparsity Regime," arXiv:2606.17901v1 (2026), https://arxiv.org/abs/2606.17901. This is an unrefereed preprint. Treat only its explicitly verified hypotheses and conclusions as provisional background: it claims the result under fixed bounds e(G)<=C chi(G)^P, not for all graphs.
- The FormalConjectures artifact formalizes a statement but contains sorry and is not a proof: https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB108%C2%BB/.

Do not confuse this problem with the unrelated induced-subgraph Erdős-Hajnal conjecture.

## Complete resolutions

An affirmative resolution is a rigorous proof of the canonical target for every r>=5 and k>=2, with a threshold depending only on (k,r), and with no unadvertised restriction on G.

A negative resolution is a rigorous construction and proof of fixed r>=5, fixed k>=2, and a finite graph family (G_n) with unbounded chromatic number and h_r(G_n)<k.

Either outcome must include a proof audit of all imported theorems and an explicit dependency ledger for every parameter.

## What does not count as a solution

- The r=4 theorem.
- A statement about induced subgraphs, or an argument that forbids edge deletion.
- A result only for sparse, bounded-degree, bounded-order, pseudorandom, Kneser, Burling, or any other special graph class.
- A result only for fractional, list, online, or approximate chromatic number.
- A proof with F depending on G, |V(G)|, e(G), an edge-density exponent, or a host-specific auxiliary object.
- Finding examples of high-girth high-chromatic graphs without embedding them as subgraphs of every high-chromatic host.
- Finite computation without a proved reduction and stopping condition that covers all finite graphs.
- Repeating an unverified claim from a preprint, talk, forum, or database entry.

## Required correctness checks

1. State every quantifier in order and verify F=F(k,r) is independent of G.
2. At every extraction/deletion step, prove that the output is an ordinary subgraph of G.
3. Check girth exactly: for r=5, eliminate both C_3 and C_4.
4. Establish chi(H)>=k for ordinary chromatic number after all cycle-killing operations.
5. If using randomization, prove a positive-probability simultaneous event and extract a deterministic witness.
6. Separate finite and infinitary claims. Do not claim the stronger infinite-chromatic-subgraph version unless it is independently proved.
7. Audit each external theorem against its original source and state the exact version used.
8. For a proposed counterexample, verify h_r(G_n)<k over all ordinary subgraphs, not merely a chosen subclass.

## Required deliverables

- A self-contained theorem statement and a one-page quantifier/notation sheet.
- A research log that separates established facts, conjectural lemmas, failed approaches, and computational observations.
- A proof or counterexample manuscript with numbered lemmas and a dependency graph.
- A correctness audit explaining how each required check above was passed.
- A literature update with direct URLs, authors, dates, publication status, and a statement of what each source actually proves.
- If incomplete, a sharply stated surviving lemma or obstruction, including hypotheses, plausible falsifiers, and the exact reason it would advance the target.

## Dynamic Multiagent v2 protocol

Maintain a research root that owns the canonical statement, source ledger, approach registry, and final consistency audit. Use at most four concurrent agents, including the root. Begin with independent exploration rather than a fixed division of mathematical methods.

Create an approach registry before substantial work. Each entry must contain: identifier; exact target or lemma; assumptions; intended invariant; relevant sources; status; falsification test; and whether it overlaps an existing route. Do not duplicate a route merely because it uses different notation.

Run multiple waves. In an early wave, allocate distinct high-level approaches that can be checked independently. At each evidence boundary, the root compares conclusions, retires disproved routes, merges compatible lemmas, and dynamically reuses open slots for the most informative unresolved bottleneck. No static role assignment is permitted.

Every nontrivial claimed lemma receives adversarial proof checking by an agent that did not originate it. The check must attempt counterexamples, inspect parameter dependencies, test the ordinary-versus-induced subgraph convention, and identify any hidden density assumption. A claim enters the accepted ledger only after this adversarial pass or is explicitly marked provisional.

Use proof-first allocation. At most one optional computational subtask may run at a time. Before it begins, register the exact lemma or construction question, finite hypotheses, certificate format, and stopping condition. End and reassign that slot immediately once the question is answered; computation may not become open-ended exploration.

## Persistence and resumability

Maintain research_state.md at the research root. After every meaningful wave, record the canonical target, source URLs and status, accepted lemmas, rejected claims, active approach-registry entries, proof dependencies, unresolved checks, and the next smallest decisive tasks.

If a runtime boundary occurs before an affirmative proof or a verified counterexample, do not present a solution. Save the state and return CHECKPOINT_NOT_FINAL followed by: current status, exact unresolved bottleneck, evidence gathered, rejected routes, and the next proof-first actions. On resumption, read research_state.md, revalidate time-sensitive literature claims, and continue from the registered bottleneck rather than restarting.
