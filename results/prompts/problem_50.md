# Erdős Problem 50 — proof-first investigation

## Definitions and canonical target

Let \(\phi(n)\) be Euler's totient function. For \(0\le c\le1\), define
\[
f(c)=\lim_{N\to\infty}\frac{1}{N}\#\{1\le n\le N:\phi(n)/n<c\}.
\]
Schoenberg's theorem gives this natural density, and the resulting distribution function is continuous. Investigate the following exact target:

> Is there an \(x\in(0,1)\) such that the finite ordinary two-sided derivative \(f'(x)\) exists and is positive?

Equivalently, prove or refute
\[
\forall x\in(0,1),\qquad f'(x)\in\mathbb R\ \Longrightarrow\ f'(x)\le0.
\]

Do not silently change \(<\) to \(\le\), include endpoints, replace an ordinary derivative by a one-sided/Dini/approximate derivative, or omit the finiteness requirement.

## Accepted background

- [Erdős Problems #50](https://www.erdosproblems.com/50) currently labels the question open (accessed 2026-07-27); its [forum thread](https://www.erdosproblems.com/forum/thread/50?order=oldest) reports no claimed solutions or partial solutions. This is status evidence, not proof of literature completeness.
- In the primary source, [Erdős (1995)](https://revistas.usp.br/resenhasimeusp/en/article/view/74798), the question is explicitly about a **finite positive derivative**.
- Schoenberg established the limiting distribution; see [Schoenberg (1936)](https://doi.org/10.1090/S0002-9947-1936-1501849-X) and the historical account in [Tenenbaum–Toulmonde (2006)](https://tenenb.perso.math.cnrs.fr/PPP/EulerLocal.pdf).
- Erdős proved the distribution measure is purely singular. Thus \(f'=0\) almost everywhere, but this does not itself exclude exceptional points of positive finite derivative.
- Tenenbaum–Toulmonde obtain detailed local information near \(1\), including an asymptotic expansion for \(1-f(1-1/\sigma)\); this is accepted background only, not a solution of the global pointwise target.
- The [FormalConjectures file](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/50.lean) contains declarations, but the relevant proofs are `sorry`; it is not a verified resolution.

## Complete resolutions

A complete proof of Erdős's assertion proves, for every \(x\in(0,1)\), that existence of the finite two-sided derivative implies \(f'(x)\le0\).

A complete disproof gives a concrete \(x\in(0,1)\) and \(L\in(0,\infty)\), then proves
\[
\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=L.
\]

Every use of external theorems must give a direct source URL, exact statement, hypotheses, and an explanation of how those hypotheses apply.

## What does not count as a solution

- Proving pure singularity or \(f'=0\) almost everywhere.
- Proving a claim only outside a null set, on a dense set, or at special rational points.
- A one-sided, Dini, approximate, distributional, or numerical derivative.
- A result for a different CDF convention without proving its equivalence for the exact target.
- A finite-prime model or computer experiment lacking a uniform, rigorous tail estimate at the difference-quotient scale.
- An assertion that the Lean declaration is formalized proof while its dependencies contain `sorry`.

## Required correctness checks

1. State whether each argument uses \(<\) or \(\le\), and justify any transfer using continuity/no-atom facts.
2. Verify the density-to-probability-model correspondence before using independent prime-divisibility variables.
3. Audit every interchange of \(N\to\infty\), prime cutoff \(\to\infty\), and \(h\to0\).
4. For any derivative claim, prove convergence for both signs of \(h\), to one finite real limit.
5. For any universal exclusion, handle all \(x\in(0,1)\), including exceptional points where singular-measure theorems are silent.
6. For local asymptotics near \(1\), verify their domain and show exactly how they imply a statement at the proposed point.
7. Subject every promising proof to an adversarial check specifically testing the invalid inference “singular implies no positive derivative anywhere.”

## Required deliverables

- `research_state.md` with canonical statement, source ledger, theorem-versus-conjecture labels, and retrieval dates.
- A dependency graph of all claimed lemmas, especially all limiting and truncation steps.
- Either a self-contained proof manuscript or a specified counterexample construction with certified two-sided limits.
- An adversarial referee report identifying every unchecked hypothesis or the first fatal gap.
- If incomplete, a frontier report: strongest proved lemma, its exact hypotheses, blocked implication, and the next falsifiable lemma.

## Dynamic Multiagent v2 protocol

Maintain a research root and an approach registry. Each registry item must record an identifier, precise target lemma, hypotheses, dependencies, status, source evidence, and failure mode. Use at most four concurrent agents.

Begin each wave with independent approaches rather than a fixed assignment. Examples of distinct starting directions include source reconstruction, exact limiting-distribution representation, local-measure estimates, and adversarial search for a positive-derivative mechanism. Each agent must register a falsifiable lemma before substantial derivation. Merge claims only when supported by an inspectable proof or a direct source.

Run multiple waves. After each wave, retire disproved routes, merge duplicate dependencies, and reuse freed slots dynamically. Reserve an adversarial proof-checking pass for every promising claim; where possible, use a fresh agent who did not develop that route. If multiple approaches rely on the same unproved tail estimate or interchange, record it once as a common dependency rather than treating the routes as independent confirmation.

Allocate resources proof-first. At most one optional computational subtask may run at any time. Before it starts, the registry must state its exact lemma, hypotheses, certificate format, and finite stopping condition. Stop it immediately when that question is answered and reassign the slot. Computation may suggest a lemma but cannot count as a proof of the target.

## Persistence and resumability

Update `research_state.md` after every wave with the source ledger, approach registry, proved lemmas and assumptions, rejected arguments, counterexamples to intermediate claims, unresolved dependencies, and the next smallest proof obligation.

If an execution boundary interrupts an incomplete investigation, put `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`. Preserve URLs, theorem statements, and all proof-audit notes. On resumption, begin with the smallest unverified dependency; never present a checkpoint as a mathematical resolution.
