# Erdős Problem 10: prime plus boundedly many powers of two

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For \(k\in\mathbb Z_{\ge0}\), define
\[
S_k=\left\{p+\sum_{i=1}^{r}2^{a_i}:p\text{ is prime},\ 0\le r\le k,\ a_i\in\mathbb Z_{\ge0}\right\}.
\]
The empty sum is allowed. A power means \(2^a\) with \(a\ge0\), so \(1=2^0\); \(p=2\) is allowed. Repeated exponents are permitted, although pairs of equal powers can be merged, so an equivalent normalized representation has distinct exponents.

Resolve exactly one proposition:
\[
\exists k\,\exists N_0\,\forall n\ge N_0,\quad n\in S_k.
\]

## Frozen mathematical background

- Gallagher proved that for every \(\epsilon>0\) there is a \(k(\epsilon)\) with lower density \(\underline d(S_{k(\epsilon)})\ge1-\epsilon\): [Gallagher (1975)](https://link.springer.com/article/10.1007/BF01390190). This is a theorem, not eventual coverage.
- Crocker proved infinite obstructions for a two-power variant: [Crocker (1971)](https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-36/issue-1/On-the-sum-of-a-prime-and-two-powers-of-two/10.2140/pjm.1971.36.103.full). It does not decide arbitrary fixed \(k\).
- Granville and Soundararajan conjectured that three powers suffice for every odd integer \(>1\), hence four for positive even integers: [Granville--Soundararajan (1998)](https://link.springer.com/article/10.1023/A:1009786614584). This is a conjecture, not accepted background theorem.
- The adjacent Linnik--Goldbach problem has two primes, not one. Recent progress there, including six powers under GRH, does not settle this target: [Johnston--Trudgian (2026)](https://arxiv.org/abs/2605.17825).
- A Lean statement exists, but its proofs are `sorry`; do not treat it as a proof: [Formal Conjectures source](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/10.lean).

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that there are fixed integers k,N0 such that every integer n >= N0 has n = p + sum_{i=1}^r 2^{a_i}, where p is prime, 0 <= r <= k, and all a_i >= 0.

**Negative obligation.** Prove that for every fixed k and every N0 there is an n >= N0 for which no representation n = p + sum_{i=1}^r 2^{a_i} with p prime, r <= k, and a_i >= 0 exists.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a rigorous proof of fixed \(k,N_0\) such that every \(n\ge N_0\) belongs to \(S_k\).

A negative resolution is a rigorous proof that for every \(k\) and every \(N_0\), there exists \(n\ge N_0\) with \(n\notin S_k\). Equivalently, for each fixed \(k\), there are arbitrarily large nonrepresentable integers.

## What does not count as a solution

- A density result, including density one, without a proof that the exceptional set is eventually empty.
- A counterexample only for one \(k\), including \(k=3\).
- Any finite search without a theorem controlling all larger integers.
- A result for two primes plus powers of two, or a result restricted to one parity class without closing the other.
- A claimed Lean proof containing `sorry`, `admit`, untrusted target axioms, or an unchecked external oracle.
- Heuristic Hardy--Littlewood calculations or probabilistic evidence presented as a proof.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State and preserve the quantifier order \(\exists k\exists N_0\forall n\exists\) representation; \(k\) cannot vary with \(n\).
2. Check \(2^0=1\), the empty sum, repeated powers, and \(p=2\). If normalizing repetitions, prove that the transformation does not increase the number of summands.
3. For a negative construction, prove nonrepresentability against every sum of at most \(k\) powers, not merely sums with distinct positive exponents unless equivalence is justified.
4. For any density or sieve argument, identify exactly where exceptional integers are excluded rather than merely shown sparse.
5. For any modular covering argument, verify every residue/exponent class, coprimality condition, and the possibility that the alleged composite remainder equals its forced divisor.
6. For every cited theorem, provide a direct source URL and state whether it is a theorem, conjecture, preprint, or computation.
7. If formalized, compile the complete dependency closure and provide a proof-escape scan for `sorry`, `admit`, and new axioms.

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
