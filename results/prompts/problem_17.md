# Erdős Problem 17: cluster primes

## Definitions and canonical target

A prime $p>2$ is a **cluster prime** if, for every positive even integer $n$ satisfying $2\le n\le p-3$, there exist primes $q_1,q_2\le p$ such that $n=q_1-q_2$. The choices of $q_1,q_2$ may depend on $n$.

Prove or disprove that cluster primes are infinite. Formally, resolve exactly one of the following:

- Positive: for every real $B$, there is a cluster prime $p>B$.
- Negative: there is a real $B$ such that no prime $p>B$ is a cluster prime.

Use the positive-even convention above. Do not use the ambiguous phrase “every even number” without this lower bound. The convention $p>2$ is part of the definition.

## Accepted background

- Blecksmith, Erdős, and Selfridge, [*Cluster Primes* (1999)](https://www.tandfonline.com/doi/abs/10.1080/00029890.1999.12005005), proved that if $C(x)$ counts cluster primes at most $x$, then $C(x)\ll_A x/(\log x)^A$ for every fixed $A>0$. This is a theorem, not a finiteness result.
- Elsholtz, [*On cluster primes* (2003)](https://www.math.tugraz.at/~elsholtz/WWW/papers/papers13clusteractarith.pdf), proves that for every fixed $0<c<1/8$, $C(x)=O_c\bigl(x\exp(-c(\log\log x)^2)\bigr)$. It uses upper-bound sieve arguments and explicitly states that the infinitude question is open.
- The current [Erdős Problems record](https://www.erdosproblems.com/17) remains labelled open, but that is evidence rather than a proof of current status.
- [OEIS A038133](https://oeis.org/A038133) is the sequence of odd **non**-cluster primes. The cluster-prime sequence is [OEIS A038134](https://oeis.org/A038134). Do not propagate the database page's reversed OEIS annotation.
- The [FormalConjectures entry](https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB17%C2%BB/) contains `sorry`; it is a statement formalization, not a verified proof of this problem or its cited bounds.

## Complete resolutions

An affirmative resolution is a rigorous unconditional proof of arbitrarily large primes $p$ satisfying every required difference condition simultaneously.

A negative resolution is a rigorous unconditional proof of an eventual obstruction: a bound $B$ and a proof that every prime $p>B$ has at least one positive even $n\le p-3$ absent from the difference set of primes at most $p$.

Any result conditional on an unproved hypothesis must be labeled conditional and does not resolve the target unless the task is explicitly changed.

## What does not count as a solution

- Checking finitely many primes or extending the numerical range.
- Reproving either known upper bound, improving its constants, or proving any upper bound compatible with $C(x)\to\infty$.
- Showing only that cluster primes have density zero, their reciprocal sum converges, or many primes fail the property.
- Showing infinitely many bounded prime gaps or any fixed finite prime pattern.
- A heuristic, random model, claimed asymptotic without proof, or an argument that covers only most required even differences.
- A proof whose witness pairs exceed $p$, use non-primes, omit a boundary value, or vary $p$ while covering different differences.
- A formal declaration with `sorry`, unchecked axioms, or nonmatching quantifiers.

## Required correctness checks

1. State the quantifiers before each main claim and preserve the order: choose $p$, then require all admissible $n$, then choose $q_1,q_2$.
2. Verify $n$ is positive, even, and includes the endpoint $p-3$ when applicable.
3. Verify $q_1,q_2$ are both primes and both at most $p$.
4. Distinguish a necessary condition from a sufficient condition; in particular, bounded prime gaps do not imply the cluster-prime property.
5. For an upper-bound lemma, state precisely what is fixed and how every implied constant depends on parameters.
6. For a negative proof, audit the universal “every sufficiently large prime” step; infinitely many failures are insufficient.
7. For an affirmative proof, audit simultaneous coverage of all differences for each produced $p$.
8. Independently adversarially check every imported theorem against a primary source and every formal claim for `sorry` or extra axioms.

## Required deliverables

- A self-contained theorem statement identifying whether the affirmative or negative alternative was established.
- A complete proof with a dependency ledger: each external theorem, exact version, hypotheses, and direct URL.
- A quantifier audit and boundary-case audit for the final proof.
- An adversarial proof-check report that attempts to falsify each key lemma and the final inference.
- If no resolution is reached, a dated `research_state.md` recording verified facts, failed approaches, open proof obligations, source links, and the next falsifiable lemma.
- Citation records must distinguish peer-reviewed papers, preprints, databases, and formal artifacts. Do not cite search snippets as mathematical evidence.

## Dynamic Multiagent v2 protocol

Maintain one research root and an approach registry in `research_state.md`. The registry must record each active approach, its exact target lemma, dependencies, status, falsification attempt, and handoff artifact.

Use at most four concurrent agents. In the first wave, allocate slots dynamically to genuinely independent approaches or verification tasks; do not impose a fixed permanent assignment. Require early reports to state a concrete lemma or obstruction and its completion test before substantial effort continues.

After each report, the research root compares approaches, merges duplicate work, assigns an adversarial checker to any promising proof, and reuses freed slots in later waves for the most informative unresolved obligation. A claim may advance only after an agent not responsible for its creation checks its quantifiers, cited inputs, and edge cases.

Proof work has priority. At most one optional computational subtask may run at once, and only after its owner records in the registry: (i) the exact lemma or hypothesis being tested, (ii) the finite input range and certificate format, and (iii) a stopping condition that answers the stated question. The computation slot must be immediately reassigned once that condition is met. Computation may generate or refute a lemma, never substitute for an infinitude proof.

Run multiple waves until either a complete resolution survives adversarial review or the remaining gap is explicitly isolated and checkpointed.

## Persistence and resumability

Update `research_state.md` after every material source check, proof attempt, counterexample, computation, or adversarial review. Include links, dates, exact statements, and unresolved dependencies so work can resume without rediscovering assumptions.

If a runtime boundary interrupts an incomplete investigation, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, summarize verified progress and the next smallest proof obligation, and do not present a partial argument as a solution.
