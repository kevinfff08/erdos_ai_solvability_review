# Erdős Problem 129: verification and statement-provenance audit

## Definitions and canonical target

For integers \(n,k,r\ge2\), let \(R(n;k,r)\) be the least \(N\) such that every \(r\)-edge-colouring of \(K_N\) has an \(n\)-vertex set \(S\) and a colour \(i\) for which the colour-\(i\) graph induced by \(S\) contains no \(K_k\).

Audit the literal displayed target
\[
\forall r\ge2\;\exists C_r>1,n_0(r)\;\forall n\ge n_0(r):
R(n;3,r)<C_r^{\sqrt n}.
\]
The working claim is that it is false at \(r=2\). The task is to verify that disproof rigorously and to determine whether an inspectable primary source states a different intended problem. Do not turn an unverified guess such as \(r\ge3\) into the target.

## Accepted background

- The current record is [Erdős Problems 129](https://www.erdosproblems.com/129), with [LaTeX source](https://www.erdosproblems.com/latex/129) and [discussion thread](https://www.erdosproblems.com/forum/thread/129). These are database/forum records, not primary proofs. They explicitly report Antonio Girão’s r=2 objection and state that the original source is ambiguous.
- For a fixed \(n\)-set, a greedy packing yields \(\Theta(n^2)\) edge-disjoint triangles: \(K_n\) has \(\Theta(n^3)\) triangles and a chosen triangle conflicts through its three edges with only \(O(n)\) triangles.
- In a uniformly random red/blue edge-colouring, a specified edge-disjoint triangle is monochromatic in a prescribed colour with probability \(1/8\), independently across the packing.
- Do not conflate this problem with the distinct local-colour function \(f(n,p,q)\) defined in Conlon, Fox, Lee, and Sudakov, [*The Erdős–Gyárfás problem on generalized Ramsey numbers*](https://arxiv.org/abs/1403.0250), or the later [Bennett–Dudek–English preprint](https://arxiv.org/abs/2212.06957).

## Complete resolutions

A complete verification has two parts.

1. Prove that for some \(c>0\) and all sufficiently large \(n\), \(R(n;3,2)\ge e^{cn}\). This is enough to disprove the literal target, because \(e^{cn}>C^{\sqrt n}\) for every fixed \(C>1\) and sufficiently large \(n\).
2. Either locate and inspect the primary source denoted [Er97b] (or another authoritative correction) and transcribe its exact quantified target, or document that no uniquely specified replacement was recovered. A distinct recovered statement is a new audit target, not a rescue of the literal proposition.

## What does not count as a solution

- A simulation of random colourings, finite cases, or an expectation calculation without a union bound over all \(n\)-sets.
- Showing only that one selected \(n\)-set has both colours’ triangles.
- Using triangles that share edges while claiming independence.
- An assertion that the intended condition is \(r\ge3\), or that it concerns \(f(n,p,q)\), without an inspected primary source.
- Treating the database open label or a forum comment as stronger than a valid disproof of the literal statement.

## Required correctness checks

- Explicitly state the quantifier order in \(R(n;k,r)\) and show why a colouring in which every \(n\)-set has both a red and a blue triangle implies \(R(n;3,2)>N\).
- Supply a self-contained \(\Omega(n^2)\) lower bound for the size of an edge-disjoint triangle packing in every \(K_n\).
- For a fixed \(S\), bound the probability that \(S\) lacks a red or blue triangle by \(2(7/8)^{c_0n^2}\).
- Bound the expected number of bad \(n\)-sets by \(\binom Nn\,2(7/8)^{c_0n^2}\), choose a concrete \(N=\lfloor e^{cn}\rfloor\), and prove it is below one for all sufficiently large \(n\).
- Check the final comparison \(e^{cn}>C^{\sqrt n}\) for arbitrary fixed \(C>1\).
- For every provenance claim, give a stable URL and distinguish primary source, peer-reviewed paper, preprint, database record, and informal forum assertion.

## Required deliverables

1. A concise, complete disproof proof with all constants and asymptotic thresholds made explicit.
2. A claim ledger separating the database’s historical attributions from independently inspected primary evidence.
3. A source ledger for [Er97b], if recovered: full bibliography, pages, exact definition, parameter domain, theorem/conjecture status, and quotation/paraphrase sufficient to compare it with the literal target.
4. A final disposition stating either `literal statement disproved; no verified replacement` or identifying a separately named and fully specified new target for a fresh audit.
5. An adversarial audit list describing any remaining unverified bibliographic claim.

## Dynamic Multiagent v2 protocol

Maintain one research root and at most four concurrent agents. Begin with independently registered approaches: direct probabilistic-disproof verification; historical-source recovery; current-literature search for an explicit correction; and adversarial quantifier/definition checking. The approach registry must record each question, sources inspected, exact conclusion, and blocker.

Run in multiple waves. When a bounded question is answered, free its slot and reuse it for the most decisive unresolved question. The research root must reconcile conflicting source descriptions, ensure that no inference from an informal note becomes a theorem claim, and send every finished proof to an adversarial checker.

Use proof-first allocation. At most one computational task is permitted, only after it declares the exact lemma, hypotheses, certificate format, and stopping condition; terminate and reassign that slot as soon as the question is answered. Computation may not substitute for the universal union-bound proof or establish authors’ intended wording.

## Persistence and resumability

Maintain `research_state.md` containing the canonical literal target, proof draft, source ledger, search log, approach registry, disputed inferences, and the smallest next decisive task. Checkpoint after every wave. If interrupted before source provenance or proof checking is complete, place `CHECKPOINT_NOT_FINAL` at the beginning of `research_state.md`; preserve all URLs, exact missing evidence, and proof obligations, and do not report a final status beyond the verified portion.
