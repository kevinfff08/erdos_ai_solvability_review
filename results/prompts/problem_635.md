# Erdős Problem 635: sharp secondary term after the resolved density bound

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

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

## Frozen mathematical background

- The current [Erdős Problems record](https://www.erdosproblems.com/635) states \(F_1(N)=\lfloor(N+1)/2\rfloor\), attained by the odd numbers.
- The same record states that for \(t=2\), \(F_2(N)\ge N/2+c\log N\) for some \(c>0\), using the odd numbers together with powers \(2^k\) for odd \(k\). The forum notes that this construction remains admissible for larger \(t\). Thus a \(N/2+O_t(1)\) upper bound is false for \(t\ge2\).
- The record says the fixed-\(t\) density assertion \(F_t(N)\le(1/2+o_t(1))N\) has been resolved. The [discussion thread](https://www.erdosproblems.com/forum/thread/635?order=oldest) attributes a proof to GPT/Lean work and records Terence Tao's observation that the same qualitative result follows from an inequality in P. D. T. A. Elliott, *Probabilistic Number Theory I: Mean-Value Theorems* (1979), cited there as Lemma 4.7; see the [publisher record](https://link.springer.com/book/10.1007/978-1-4612-9989-9).
- Do not treat the preceding claim as a substitute for reading the proof. The forum also says Elliott-type arguments give only a slowly decaying error such as \(O(1/\log\log N)\) at density level, not the proposed logarithmic additive error. Tao's [notes on the weak Elliott inequality](https://terrytao.wordpress.com/2019/11/12/254a-notes-9-second-moment-and-entropy-methods/comment-page-1/) give relevant second-moment context, but do not themselves solve this sharp target.
- It is not established here that \(N/2+O_t(\log N)\) was the unique wording intended in Erdős's original letter. It is the explicitly declared revised target.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** For the revised sharp-error target: prove that for every fixed integer t≥2 there exist constants C_t and N_t such that F_t(N)≤N/2+C_t log N for every N≥N_t. Together with the recorded t=2 construction, valid also for larger t, this yields F_t(N)=N/2+Θ_t(log N) for every fixed t≥2.

**Negative obligation.** Disprove the revised sharp-error target by proving that for some fixed t≥2 and a sequence N_j→∞, F_t(N_j)−N_j/2 is not O(log N_j); equivalently, for every C there are arbitrarily large N with F_t(N)>N/2+C log N.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

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

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Define \(F_t(N)\) and quantify \(t,N,a,b\) explicitly.
2. Verify every use of \((b-a)\mid b\Longleftrightarrow(b-a)\mid a\).
3. Keep \(t=1\) separate from the \(t\ge2\) target.
4. Track all \(t\)-dependent constants and all thresholds in \(N\).
5. For every analytic/mean-value estimate, state its interval, modulus or prime range, exceptional set, norm, and quantitative error before applying it to \(1_A\).
6. For every graph-theoretic step, show why the relevant edge count or expansion estimate applies to an arbitrary admissible set rather than an average set.
7. Stress-test candidate proofs against the odd-plus-powers-of-two construction and against small boundary cases \(b-a<t\).
8. Have a separate adversarial checker seek hidden loss factors that turn \(O(\log N)\) into \(o(N)\) only.

If the proof uses an external theorem not fully stated in the frozen background, record its exact hypotheses and verify that they apply. Do not expand this local dependency check into a general literature or open-status investigation.

## Required research package

Create a coherent, self-contained research package. Choose the directory layout that best fits the mathematics, but preserve enough structure that another researcher can trace every final claim to its proof, computation, source, and adversarial check.

### Mandatory paper: `paper.tex`

Produce a journal-style mathematical paper containing:

- a title and abstract;
- the canonical problem and all definitions needed to read the paper independently;
- the frozen background actually used;
- a precise statement of every claimed contribution;
- complete proofs of all lemmas and the main theorem or counterexample;
- a clear comparison between the frozen background and what was newly established;
- an accurate final statement of whether the canonical target has been proved or disproved;
- complete citations for every external result used.

All references must be part of the archived package. They may be embedded in `paper.tex` or stored in an included `references.bib`; no citation may depend on a missing external bibliography file. The paper must not contain placeholders, omitted proof steps, or claims supported only by notes elsewhere in the package.

### Mandatory final audit: `audit.md`

Produce an independent adversarial audit of the final `paper.tex`. It must check:

- exact agreement between the paper's main claim and the canonical target;
- every quantifier, parameter dependence, boundary case, equality case, and uniformity requirement;
- the full dependency chain of every nontrivial lemma;
- possible circular reasoning, hidden assumptions, and illicit weakening of the target;
- exact applicability of every external theorem used;
- whether computational evidence proves only the finite statement claimed for it;
- whether citations support the statements attributed to them;
- whether every asserted new result is actually beyond the frozen background;
- whether the final solution claim is justified.

The audit must end with exactly one verdict:

- `COMPLETE_SOLUTION_VERIFIED`;
- `COMPLETE_DISPROOF_VERIFIED`; or
- `CHECKPOINT_NOT_FINAL`.

Only the first two verdicts count as completion.

### Intermediate research archive

Reasonably archive all intermediate material that matters to verification or resumption, such as proof drafts, proved and refuted lemmas, dependency notes, adversarial reviews, failed routes with exact failure points, computation code, exact certificates, test outputs, and the current research state. Filenames and subdirectories are flexible; organization, traceability, and resumability are mandatory. Do not allow the final paper to depend on an unarchived calculation or argument.

### LaTeX and PDF check

Compile `paper.tex` successfully and retain the resulting `paper.pdf`. All citations and cross-references must resolve, and there must be no fatal LaTeX errors. Successful compilation and an openable PDF are sufficient: do not perform page-by-page screenshot inspection, do not create visual-validation images, and do not add images, figures, diagrams, or a graphical abstract to the paper.

## Dynamic Multiagent constraints

Choose mathematical approaches, delegation, coordination, and changes of direction autonomously. Do not impose fixed roles, named stages, prescribed proof methods, or a predetermined sequence of work. Including the root agent, use at most four concurrent agents.

The following are prohibited:

- assigning any agent to investigate whether the problem is open;
- assigning a general literature survey or publication-status review;
- maintaining a long-running source-collection role disconnected from an active proof obligation;
- substituting a research plan, list of approaches, or organizational work for mathematical derivation;
- duplicating the same route across agents without a concrete adversarial or comparative purpose;
- recording a conjecture or proof sketch as a proved lemma;
- starting computation without a precise mathematical claim, hypotheses, finite scope, certificate format, and stopping condition;
- using finite computation or numerical evidence as a substitute for a universal proof;
- declaring a complete solution without independent adversarial checking of the actual proof;
- voluntarily stopping because the problem is difficult, initial routes failed, or only intermediate results have been obtained;
- allowing source management, status tracking, or process documentation to consume the main research effort.

Inspect an external source only when an active proof step requires the exact statement of a named theorem. Record the theorem and its hypotheses, check that they apply, and return to the mathematics.

## Persistence and external-interruption behavior

Continue mathematical research while execution resources remain available. Do not end the task merely because several approaches fail, a complete proof has not yet emerged, intermediate lemmas have been found, a paper draft exists, or the remaining gap has been identified. Autonomously repair, replace, combine, or abandon approaches as the mathematics requires.

Use `CHECKPOINT_NOT_FINAL` only when an external runtime, context, or system boundary forces interruption. It is not a voluntary completion option. On forced interruption, preserve the current `paper.tex`, `audit.md`, all verified results, unresolved proof obligations, failed routes with exact failure points, computations and certificates, and a clear resumable research state. Never convert an interrupted investigation into a solution claim.
