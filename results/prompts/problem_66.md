# Erdős Problem 66: pointwise logarithmic additive representation function

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(\mathbb N=\{1,2,\ldots\}\). For a set \(A\subseteq\mathbb N\), define the **ordered additive representation function**

\[
r_A(n):=\sum_{a=1}^{n-1}1_A(a)1_A(n-a)
      =|\{(a,b)\in A^2:a+b=n\}|.
\]

Thus the convolution is additive, not Dirichlet convolution; diagonal pairs \(a=b\) are counted once as ordered pairs. The target is:

\[
\text{Does there exist }A\subseteq\mathbb N\text{ and a finite }L>0
\text{ such that } r_A(n)/\log n\to L?
\]

The limit is along **every** integer \(n\to\infty\), and \(\log\) is natural. Equivalently, for every \(\varepsilon>0\) there must be \(N\) such that every integer \(n\ge N\) satisfies

\[
|r_A(n)-L\log n|\le \varepsilon\log n.
\]

Do not interpret the limit in the extended reals: otherwise \(A=\mathbb N\) gives a trivial \(+\infty\) ratio. Erdős historically asked the special case \(L=1\); do not assume that it is equivalent to the present existential-any-\(L\) formulation.

## Frozen mathematical background

- The current [Erdős Problems entry](https://www.erdosproblems.com/latex/66) records this as open and summarizes the relevant earlier barriers.
- Erdős and Sárközy, [Problems and Results on Additive Properties of General Sequences, II (1986)](https://users.renyi.hu/~p_erdos/1986-12.pdf), record the conjectural negative answer and prove that, for suitable increasing \(F=o(n/(\log n)^2)\), approximation of the representation function on the \(o(\sqrt F)\) scale is impossible. This is a theorem, but it does **not** rule out \(L\log n+o(\log n)\).
- Horváth, [An Improvement of a Theorem of Erdős and Sárközy (2007)](https://doi.org/10.1556/Pollack.2.2007.S.14), proves a stronger \(\sqrt{F}\)-scale pointwise obstruction. It remains insufficient for the target error \(o(\log n)\).
- Erdős and Tetali, [Representations of Integers as the Sum of k Terms (1990)](https://onlinelibrary.wiley.com/doi/10.1002/rsa.3240010302), construct bases with representation count \(\Theta(\log n)\). This establishes the scale, not convergence of the normalized count.
- Kuang and Wang, [arXiv:2607.16613 (2026)](https://arxiv.org/abs/2607.16613), prove a related density-one result: outside a density-zero exceptional set, an ordered representation function can approximate a slowly growing \(O(\log\log n)\) function extremely well. This is a preprint and is not a solution here, because this problem forbids every exceptional set and asks for the \(\log n\) scale.

All claims beyond these sources require independent proof. Clearly label any conjectural heuristic as such.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Exhibit an explicitly defined or rigorously proved-to-exist set A⊆N and a finite L>0, and prove that for every ε>0 there is N such that every integer n≥N satisfies |r_A(n)/log n−L|<ε, where r_A counts ordered pairs (a,b)∈A² with a+b=n.

**Negative obligation.** Prove that for every A⊆N and every finite L>0, the sequence r_A(n)/log n does not converge to L; equivalently, show that no A has r_A(n)=L log n+o(log n) simultaneously for all integers n→∞.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution must provide a set \(A\subseteq\mathbb N\), a finite \(L>0\), and a proof of the all-integers epsilon definition above.

A negative resolution must prove that for every \(A\subseteq\mathbb N\) and every finite \(L>0\), \(r_A(n)/\log n\) fails to converge to \(L\). It is enough to derive a contradiction from the assumed asymptotic \(r_A(n)=L\log n+o(\log n)\), but the derivation must retain uniform control over all sufficiently large integers.

## What does not count as a solution

- \(r_A(n)=\Theta(\log n)\), bounded limsup, or convergence on any subsequence.
- An almost-all, density-one, averaged, Cesàro, probabilistic-high-probability, or finite-range result.
- Repeating an \(o(\sqrt{\log n})\) obstruction without bridging the gap to \(o(\log n)\).
- A construction or theorem for unordered representations, distinct summands, a different ambient set, or Dirichlet convolution unless a rigorous conversion establishes this exact target.
- Evidence from computation without a proved lemma, explicit hypotheses, and a stopping condition.
- Resolving only \(L=1\) without proving it resolves the stated all-\(L\) existential target.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State the representation convention in every lemma; check ordered pairs and diagonal terms explicitly.
2. State every quantifier: an exceptional set of size \(o(x)\) is still forbidden.
3. When invoking Erdős–Sárközy or Horváth, match every hypothesis on the comparison function, monotonicity, and error scale.
4. Check that no passage from \(\Theta(\log n)\) to a limit is tacit.
5. For any generating-function argument, justify coefficient extraction, convergence domain, and all boundary-limit interchanges.
6. For a proposed construction, prove that later additions to \(A\) do not destroy estimates already claimed for infinitely many sums.
7. For a negative proof, identify exactly where the assumption \(o(\log n)\) yields a stronger forbidden estimate; an unexplained error loss invalidates the conclusion.

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
