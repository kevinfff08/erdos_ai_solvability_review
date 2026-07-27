# Erdős Problem 39: dense infinite Sidon sets

## Definitions and canonical target

Let \(A\subseteq\mathbb N=\{1,2,\ldots\}\), and write \(A(N)=|A\cap[1,N]|\).  Call \(A\) a Sidon set (equivalently a \(B_2\) sequence) if, for all \(a,b,c,d\in A\),
\[
a+b=c+d\quad\Longrightarrow\quad \{a,b\}=\{c,d\}\text{ as multisets}.
\]
Thus diagonal sums and repeated elements are included.

Prove or disprove the following proposition:
\[
\exists\,A\subseteq\mathbb N\;\bigl[A\text{ is infinite and Sidon, and }\forall\epsilon\in(0,1/2)\;\exists c_\epsilon>0\;\exists N_\epsilon\;\forall N\ge N_\epsilon,\ A(N)\ge c_\epsilon N^{1/2-\epsilon}\bigr].
\]
The set \(A\) must be fixed before \(\epsilon\) is chosen.  Constants and thresholds may depend on \(\epsilon\), not on \(N\).

## Accepted background

- Ajtai, Komlós, and Szemerédi proved an infinite Sidon construction with \(A(N)\gg(N\log N)^{1/3}\): [A Dense Infinite Sidon Sequence (1981)](https://www.sciencedirect.com/science/article/pii/S0195669881800145).
- Ruzsa proved existence at exponent \(\sqrt2-1\): [An Infinite Sidon Sequence (1998)](https://www.sciencedirect.com/science/article/pii/S0022314X97921922). This is a theorem, not the target result.
- Cilleruelo gave an explicit construction with the same exponent: [Infinite Sidon sequences](https://arxiv.org/abs/1209.0326), later published in *Advances in Mathematics* 255 (2014), DOI 10.1016/j.aim.2014.01.011.
- Erdős's theorem \(\liminf A(N)/\sqrt N=0\) for every infinite Sidon set does not refute the target. The Erdős Problems record and its forum have no claimed solution: [problem page](https://www.erdosproblems.com/39), [forum thread](https://www.erdosproblems.com/forum/thread/39).
- Bounded-representation constructions are weaker: [Cilleruelo–Kiss–Ruzsa–Vinuesa (2010)](https://onlinelibrary.wiley.com/doi/abs/10.1002/rsa.20350) gives dense \(B_2[g]\)-type results, but \(g>1\) is not Sidon.
- Recent related work: [O'Bryant (2026)](https://arxiv.org/abs/2606.28651) proves liminf thickness bounds for \(\gamma\)-Golomb rulers and states that Ruzsa's exponent remains the record. It does not settle this target.
- A Lean statement exists at [FormalConjectures/ErdosProblems/39.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/39.lean), but its theorem is a `sorry` placeholder and is not an accepted proof.

## Complete resolutions

An affirmative resolution supplies one infinite Sidon set and a complete proof of the stated all-large-\(N\), every-\(\epsilon\) lower bound.

A negative resolution proves that for every infinite Sidon set \(A\), some \(\epsilon\in(0,1/2)\) satisfies \(A(N)\not=\Omega(N^{1/2-\epsilon})\); equivalently, for every \(c>0\) and \(N_0\), there is \(N\ge N_0\) with \(A(N)<cN^{1/2-\epsilon}\).

## What does not count as a solution

- A different set for each \(\epsilon\).
- A \(B_2[g]\) set for \(g>1\), bounded convolution, or bounded average energy without unique sums.
- A density result only on a subsequence, only at block endpoints, or only as a limsup.
- A finite computation, experimental sequence, or unproved heuristic about random deletions.
- Re-establishing the \(\sqrt2-1\) exponent without a valid path to the target.
- Treating \(\liminf A(N)/\sqrt N=0\) as a contradiction.

## Required correctness checks

1. State and maintain the quantifier order \(\exists A\,\forall\epsilon\,\exists c_\epsilon,N_\epsilon\,\forall N\).
2. Check all additive quadruples, including diagonal sums and collisions between nonadjacent construction blocks.
3. If elements are deleted, prove a cumulative density estimate for every sufficiently large \(N\), not only chosen scales.
4. Separate the exact Sidon condition from \(B_2[g]\), energy, and representation-function surrogates.
5. Give complete estimates with dependence on every parameter displayed.
6. Subject every claimed proof to an adversarial independent audit; identify any imported theorem precisely and verify its hypotheses.

## Required deliverables

- A concise theorem statement matching the canonical target and either a full proof or a precise proof of the negation.
- A collision ledger: all categories of possible equal sums and the lemma that eliminates each.
- A density ledger proving the all-large-\(N\) estimate with quantified constants.
- A source log with direct links, theorem numbers/pages where available, and a label for theorem, conjecture, heuristic, or computation.
- An adversarial proof-check report that attempts to break quantifiers, diagonal cases, cross-block cases, and asymptotic estimates.
- If incomplete, a sharply stated surviving lemma and an explanation of why it would advance the target.

## Dynamic Multiagent v2 protocol

Create a research root and use at most four concurrent agents. Begin with genuinely independent approaches rather than a fixed division of mathematical labor. Maintain an approach registry recording: approach identifier, exact target lemma, assumptions, status, evidence, collision risks, and reason for continuation or termination.

Use multiple waves. In the first wave, allocate agents to independent proof ideas and one adversarial literature/statement check. In later waves, dynamically reuse freed slots for the most promising unresolved lemma, an independent reconstruction, or hostile proof auditing. Do not retain a slot merely because it was assigned initially. Any proposed proof must be checked by an agent that did not develop it, and major claims require a second independent derivation or a pinpointed citation.

Use proof-first allocation. At most one optional computational subtask may run at a time. Before it runs, record the exact finite lemma/hypotheses it tests, the certificate it must output, and its stopping condition. When that question is answered, immediately reassign its slot to proof work. Computation may guide a lemma or expose a counterexample pattern; it cannot establish the asymptotic target.

## Persistence and resumability

Maintain `research_state.md` at the research root. At every material transition record the canonical target, current literature status, source URLs, approach registry, proved lemmas, rejected arguments and their failure modes, pending checks, and the next smallest proof obligation.

If a runtime boundary occurs before a complete audited resolution, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, preserve all evidence and exact open obligations, and return only a checkpoint report. Never present an incomplete construction, numerical evidence, or an unverified cited claim as a solution.
