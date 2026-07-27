# Erdős Problem 635: sharp secondary term after the resolved density bound

## Definitions and canonical target

For integers \(t,N\ge 1\), write \([N]=\{1,\ldots,N\}\), and define
\[
F_t(N):=\max\{|A|:A\subseteq[N],\; \forall a,b\in A,\; a<b,\;b-a\ge t\Rightarrow (b-a)\nmid b\}.
\]
Because \(b=a+(b-a)\), the divisibility condition \((b-a)\mid b\) is equivalent to \((b-a)\mid a\); either form may be used only with this equivalence stated.

The original record asked both for the size of \(F_t(N)\) and for the weaker statement \(F_t(N)\le(1/2+o_t(1))N\) for every fixed \(t\). The latter is now recorded as resolved. Investigate the following explicit revised target, rather than claiming to solve the original compound question wholesale:
\[
\boxed{\text{For every fixed }t\ge2,\quad F_t(N)\le N/2+C_t\log N\text{ for all sufficiently large }N.}
\]
Here \(C_t\) and the starting threshold may depend on fixed \(t\), while \(N\to\infty\). A proof establishes the target; a disproof must give one fixed \(t\ge2\) and arbitrarily large \(N\) with \(F_t(N)-N/2\) not \(O(\log N)\).

## Accepted background

- The current [Erdős Problems record](https://www.erdosproblems.com/635) states \(F_1(N)=\lfloor(N+1)/2\rfloor\), attained by the odd numbers.
- The same record states that for \(t=2\), \(F_2(N)\ge N/2+c\log N\) for some \(c>0\), using the odd numbers together with powers \(2^k\) for odd \(k\). The forum notes that this construction remains admissible for larger \(t\). Thus a \(N/2+O_t(1)\) upper bound is false for \(t\ge2\).
- The record says the fixed-\(t\) density assertion \(F_t(N)\le(1/2+o_t(1))N\) has been resolved. The [discussion thread](https://www.erdosproblems.com/forum/thread/635?order=oldest) attributes a proof to GPT/Lean work and records Terence Tao's observation that the same qualitative result follows from an inequality in P. D. T. A. Elliott, *Probabilistic Number Theory I: Mean-Value Theorems* (1979), cited there as Lemma 4.7; see the [publisher record](https://link.springer.com/book/10.1007/978-1-4612-9989-9).
- Do not treat the preceding claim as a substitute for reading the proof. The forum also says Elliott-type arguments give only a slowly decaying error such as \(O(1/\log\log N)\) at density level, not the proposed logarithmic additive error. Tao's [notes on the weak Elliott inequality](https://terrytao.wordpress.com/2019/11/12/254a-notes-9-second-moment-and-entropy-methods/comment-page-1/) give relevant second-moment context, but do not themselves solve this sharp target.
- It is not established here that \(N/2+O_t(\log N)\) was the unique wording intended in Erdős's original letter. It is the explicitly declared revised target.

## Complete resolutions

An affirmative resolution must provide a self-contained proof that for each fixed \(t\ge2\), named constants \(C_t,N_t\) exist with
\[
F_t(N)\le N/2+C_t\log N\qquad(N\ge N_t).
\]
Every imported theorem must be stated with its hypotheses and cited by a direct source. If combining this upper bound with the recorded lower construction, separately verify that the construction is admissible for the exact value of \(t\) being claimed.

A negative resolution must prove that the displayed upper bound fails: exhibit a fixed \(t\ge2\), a sequence \(N_j\to\infty\), and admissible \(A_j\subseteq[N_j]\) with \((|A_j|-N_j/2)/\log N_j\to\infty\), or an equally strong logically equivalent certificate.

## What does not count as a solution

- Re-establishing only \(F_t(N)\le(1/2+o_t(1))N\).
- A computation at finitely many \(N\), heuristic graph-density calculation, or randomized experiment without a theorem for all large \(N\).
- A new \(N/2+c\log N\) lower construction without a matching upper bound, or a putative upper bound that is only \(N/2+o_t(N)\).
- A result where \(t\) grows with \(N\), unless it rigorously implies the fixed-\(t\) target with the required quantifiers.
- A proof that silently changes \(b-a\ge t\) to \(b-a>t\), deletes the short-difference exception, or replaces divisibility of \(b\) by a non-equivalent relation.
- An uninspected AI output, forum assertion, or formalization claim presented as a proof.

## Required correctness checks

1. Define \(F_t(N)\) and quantify \(t,N,a,b\) explicitly.
2. Verify every use of \((b-a)\mid b\Longleftrightarrow(b-a)\mid a\).
3. Keep \(t=1\) separate from the \(t\ge2\) target.
4. Track all \(t\)-dependent constants and all thresholds in \(N\).
5. For every analytic/mean-value estimate, state its interval, modulus or prime range, exceptional set, norm, and quantitative error before applying it to \(1_A\).
6. For every graph-theoretic step, show why the relevant edge count or expansion estimate applies to an arbitrary admissible set rather than an average set.
7. Stress-test candidate proofs against the odd-plus-powers-of-two construction and against small boundary cases \(b-a<t\).
8. Have a separate adversarial checker seek hidden loss factors that turn \(O(\log N)\) into \(o(N)\) only.

## Required deliverables

- `research_state.md` containing the exact target, source log, active approaches, proved lemmas, failed approaches, and unresolved proof obligations.
- A literature note distinguishing the published Elliott source, the current database record, forum claims, and any inspected formal artifact; include direct URLs and access dates.
- Either a complete proof/disproof meeting the preceding section or a rigorously delimited partial result whose theorem statement makes its remaining gap explicit.
- A lemma dependency graph with each nontrivial lemma labeled proved, imported, conjectural, or refuted.
- An adversarial audit of the final argument, including all quantifiers and asymptotic dependencies.

## Dynamic Multiagent v2 protocol

Use a research root that maintains `research_state.md` and an approach registry. Run at most four agents concurrently. In the first wave, independently explore incompatible proof directions, source verification, structural extremal arguments, and counterexample mechanisms; do not force a common method prematurely.

Before work starts, register for every approach: its precise claimed lemma, assumptions, proposed certificate, dependencies, and a falsification test. Reuse slots dynamically: when an approach proves, refutes, or stalls on its registered lemma, summarize the evidence in the registry and reassign the slot to the highest-value unresolved obligation. Run multiple waves, including a late adversarial wave whose sole task is to break the strongest candidate argument.

Allocate effort proof-first. At most one optional computational subtask may run at once, and only after its lemma, hypotheses, finite search domain, certificate format, and stopping condition are recorded. Stop it immediately once the stated question is answered, archive the certificate, and reassign its slot to proof work. Computation may discover a counterexample to a lemma or verify a bounded exact claim; it cannot substitute for the all-\(N\) theorem.

Require all agents to distinguish theorem, conjecture, deduction, and informal claim. A proposed proof advances only after an independent agent checks its statements against the canonical target and tests its most fragile lemma.

## Persistence and resumability

Update `research_state.md` after each material source inspection, lemma proof, refutation, or reassignment. Record exact citations, theorem versions, definitions, and outstanding proof obligations so another session can resume without reconstructing context.

If a runtime boundary occurs before an affirmative or negative resolution, do not issue a solution claim. Write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, preserve the approach registry and evidence log, state the last verified lemma and the next falsifiable task, and resume from that checkpoint in the next wave.
