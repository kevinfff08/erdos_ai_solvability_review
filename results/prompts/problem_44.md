# Erdős Problem 44 — prescribed-prefix near-optimal Sidon extension

## Definitions and canonical target

A finite set \(S\subset\mathbb Z\) is a **Sidon set** if
\[
a+b=c+d\quad(a,b,c,d\in S)
\]
implies equality of the multisets \(\{a,b\}=\{c,d\}\). Equivalently, every positive integer occurs as a difference \(x-y\) of two distinct members of \(S\) in at most one ordered way.

Prove or disprove the following exact statement:

> For every integer \(N\ge1\), every Sidon set \(A\subseteq\{1,\ldots,N\}\), and every real \(\varepsilon>0\), there are an integer \(M>N\) and a set \(B\subseteq\{N+1,\ldots,M\}\) such that \(A\cup B\) is Sidon and
> \[
> |A\cup B|\ge(1-\varepsilon)\sqrt M.
> \]

Only \(0<\varepsilon<1\) is substantive. \(M\) and \(B\) may depend on \(N,A,\varepsilon\). Do not strengthen the task by demanding a uniform \(M(\varepsilon)\), and do not weaken it by allowing an extension that omits elements of \(A\).

## Accepted background

- The current Erdős Problems record lists this exact target as open and notes the historical implication \(#707\Rightarrow#44\Rightarrow#329\): <https://www.erdosproblems.com/44>.
- A Lean statement exists, with \(M>N\), but contains `sorry` and is not a proof: <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/44.lean>.
- Alexeev and Mixon disproved the stronger assertion that every finite Sidon set extends to a finite perfect difference set (PDS): <https://arxiv.org/abs/2510.19804>. This invalidates one sufficient route but does **not** disprove the target here.
- Cilleruelo and Nathanson construct infinite perfect difference sets from dense Sidon sets: <https://arxiv.org/abs/math/0609244>. This is background on infinite extension and does not give the prescribed-prefix near-optimal finite endpoint required here.
- Eberhard and Manners study the apparent structure of dense finite-group Sidon sets and explicitly leave relevant structural conjectures open: <https://doi.org/10.37236/11191>.

Treat each item above as exactly what it states. In particular, PDS non-extension, finite computations, and informal claims do not settle this problem.

## Complete resolutions

An affirmative resolution is a rigorous proof of the displayed universal statement, including all finite initial Sidon sets \(A\) and every \(0<\varepsilon<1\).

A negative resolution is explicit data \(N,A,\varepsilon_0\), with \(A\subseteq[1,N]\) Sidon and \(0<\varepsilon_0<1\), plus a proof that for every integer \(M>N\) and every \(B\subseteq[N+1,M]\), either \(A\cup B\) is not Sidon or
\[
|A\cup B|<(1-\varepsilon_0)\sqrt M.
\]

## What does not count as a solution

- Showing only that \(A\) cannot extend to a finite PDS or a Singer-type difference set.
- Constructing dense Sidon sets that need not contain the given \(A\).
- Proving a fixed positive density \(c\sqrt M\) with \(c<1\), or obtaining the claim only for \(\varepsilon\ge1\).
- Testing finitely many \(M\), moduli, or candidate sets without a theorem that handles all later \(M\).
- Giving an infinite Sidon/PDS extension without proving that some finite endpoint has the required coefficient.
- Establishing the claim for selected, random, maximal, or algebraically structured initial sets only.

## Required correctness checks

1. State the Sidon convention precisely and include repeated summands such as \(2a=b+c\).
2. For every proposed extension, separately audit all old–old, old–new, and new–new difference/sum collisions.
3. Keep all quantifiers in the target order; a construction may depend on \(N,A,\varepsilon\).
4. If representatives of a cyclic-group construction are used, prove that modular uniqueness survives passage to integers; explicitly exclude wraparound collisions.
5. If a negative proof uses a maximality or compactness assertion, prove its scope covers every larger \(M\), not only a chosen family of endpoints.
6. Identify exactly where any density loss occurs and prove it can be made at most \(\varepsilon\), rather than merely \(o(1)\) under incompatible limits.
7. Do not invoke the known PDS counterexamples as a counterexample to this target.

## Required deliverables

- A `research_state.md` containing the canonical statement, source URLs, an approach registry, precise proved lemmas, failed approaches, and open proof obligations.
- A self-contained proof manuscript or counterexample manuscript with every nonstandard lemma proved or cited by theorem number and stable URL.
- A collision audit table for every central construction or obstruction.
- A short status memo distinguishing proved statements, computational observations, conjectures, and external results.
- If formalization is attempted, a compilable Lean artifact with no `sorry` in the claimed theorem and an explanation of correspondence with the canonical target.
- Complete bibliographic citations and direct links for every material external claim.

## Dynamic Multiagent v2 protocol

Set up a research root that owns `research_state.md`. Use at most four concurrent agents total. Start with independent approaches rather than a fixed division of mathematical labor; register each proposed route with its exact target lemma, assumptions, predicted payoff, and falsification test before substantial effort.

Use multiple waves. After an early wave, compare approaches against the registry, preserve reusable lemmas, and reassign freed slots to the sharpest unresolved proof obligation or to adversarial checking. No agent should regard a heuristic, a search result, or another agent's summary as a proof.

Every promising proof receives an adversarial audit by an agent not responsible for its derivation. The audit must check quantifiers, Sidon convention, boundary cases, modular-to-integer transfer, and all density limits. Record accepted, rejected, and unresolved arguments in the registry with evidence.

Allocate resources proof-first. At most one computational subtask may run at a time. Before it runs, write in `research_state.md` the exact lemma or counterexample predicate being tested, all hypotheses, the certificate expected from the computation, and a finite stopping condition. On answer, immediately release and reassign that slot; computation may guide a proof but cannot substitute for an all-\(M\) argument.

## Persistence and resumability

Update `research_state.md` after each material lemma, failed route, source check, or audit. Include enough detail for another agent to reproduce definitions and continue without relying on chat history.

If a runtime boundary occurs before a complete affirmative proof or complete negative certificate, stop with `CHECKPOINT_NOT_FINAL` in `research_state.md`. State the exact remaining obligation, the strongest verified intermediate result, active assumptions, and the next adversarial check. Do not describe incomplete evidence as a resolution.
