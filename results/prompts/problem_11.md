# Erdős Problem 11 — proof-first investigation

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

A positive integer \(s\) is squarefree if no prime square divides \(s\). A power of two in the primary computational convention is \(2^k\) with \(k\in\mathbb Z_{\ge1}\).

Prove or disprove the literal current-page target:
\[
\exists N\ \forall\text{ odd }n\ge N\ \exists k\ge1:\quad 2^k<n\quad\text{and}\quad n-2^k\text{ is squarefree}.
\]
Equivalently, every sufficiently large odd \(n\) is \(s+2^k\) with \(s\) positive and squarefree.

Do not silently replace this target by the stronger historical statement “every odd \(n>1\),” by a \(k=0\) convention, by the \(4\nmid n\) variant, or by a two-powers variant. Any work on one of those must state and prove its implication to the canonical target.

## Frozen mathematical background

- The [Erdős Problems record](https://www.erdosproblems.com/11), updated 2026-04-05, lists the target as open. Its [forum thread](https://www.erdosproblems.com/forum/thread/11) contains an explicit 2026 rejection of an attempted reduction from \(\sum_p1/\operatorname{ord}_{p^2}(2)<\infty\) to the full conjecture.
- Christian Hercher, [*On the Sum of a Squarefree Integer and a Power of Two*](https://cs.uwaterloo.ca/journals/JIS/VOL28/Hercher2/hercher24.html), *Journal of Integer Sequences* 28 (2025), Article 25.3.1, proves a finite computational verification for all odd \(n\le2^{50}\). It is not an asymptotic proof.
- Granville and Soundararajan, [*A Binary Additive Problem of Erdős and the Order of 2 mod \(p^2\)*](https://link.springer.com/article/10.1023/A%3A1009786614584), *Ramanujan Journal* 2 (1998), 283–298, are the primary source for the order-mod-\(p^2\), Wieferich, and covering-system background. Obtain and inspect the full text before citing theorem content; record theorem number, hypotheses, and conclusion exactly.
- The [Formal Conjectures file](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/11.lean) contains only `sorry` declarations and is not a proof.

Classify every imported fact in the theorem ledger as: fully proved in this project; verified primary theorem; conditional theorem; finite computation; or heuristic. Do not rely on an informal forum post as a theorem.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that there exists an integer N such that every odd n>=N has a positive integer k with 2^k<n and n-2^k squarefree.

**Negative obligation.** Prove that there are arbitrarily large odd integers n such that, for every positive integer k with 2^k<n, n-2^k is not squarefree. This refutes the eventual statement.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a complete proof of an \(N\) such that every odd \(n\ge N\) has a \(k\ge1\) for which \(n-2^k\) is positive and squarefree.

A negative resolution is a proof of arbitrarily large odd \(n\) such that every \(n-2^k\), for \(k\ge1\) with \(2^k<n\), is non-squarefree. A certified unbounded family of such \(n\) disproves the eventual statement.

## What does not count as a solution

- Checking any finite interval, regardless of size.
- Establishing the claim for almost all odd integers, positive density, or a heuristic probability model.
- A representation with \(k=0\), two powers of two, or a different divisibility domain without a proved reduction.
- A conditional result whose assumptions are not proved.
- A CRT construction that covers only finitely many exponent classes or fails to prove positivity of \(n-2^k\).
- A theorem attribution to Granville–Soundararajan based only on a database summary, an unproved Lean comment, or a forum paraphrase.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State all quantifiers and all uniformity ranges in every lemma.
2. For every candidate \(k\), verify \(1\le k<\log_2 n\), positivity of \(n-2^k\), and squarefreeness against every prime square.
3. For a congruence-cover construction, prove that it covers every relevant exponent, including the use of exact periods \(\operatorname{ord}_{p^2}(2)\) and CRT compatibility.
4. Never pass from density-one or expected representation count to universal coverage without an explicit theorem controlling all exceptions.
5. Treat dependencies among \(p^2\mid n-2^k\) exactly; independence may be used only as a labelled heuristic.
6. Verify any Wieferich-related theorem directly from the 1998 paper. Record and resolve the conflict between secondary summaries before using it.
7. Require an adversarial independent reconstruction of every decisive lemma, focused on missed exponent classes, incorrect order computations, non-coprime moduli, and hidden unproved assumptions.

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
