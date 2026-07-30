# Erdős Problem 39: dense infinite Sidon sets

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

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

## Frozen mathematical background

- Ajtai, Komlós, and Szemerédi proved an infinite Sidon construction with \(A(N)\gg(N\log N)^{1/3}\): [A Dense Infinite Sidon Sequence (1981)](https://www.sciencedirect.com/science/article/pii/S0195669881800145).
- Ruzsa proved existence at exponent \(\sqrt2-1\): [An Infinite Sidon Sequence (1998)](https://www.sciencedirect.com/science/article/pii/S0022314X97921922). This is a theorem, not the target result.
- Cilleruelo gave an explicit construction with the same exponent: [Infinite Sidon sequences](https://arxiv.org/abs/1209.0326), later published in *Advances in Mathematics* 255 (2014), DOI 10.1016/j.aim.2014.01.011.
- Erdős's theorem \(\liminf A(N)/\sqrt N=0\) for every infinite Sidon set does not refute the target.
- Bounded-representation constructions are weaker: [Cilleruelo–Kiss–Ruzsa–Vinuesa (2010)](https://onlinelibrary.wiley.com/doi/abs/10.1002/rsa.20350) gives dense \(B_2[g]\)-type results, but \(g>1\) is not Sidon.
- Recent related work: [O'Bryant (2026)](https://arxiv.org/abs/2606.28651) proves liminf thickness bounds for \(\gamma\)-Golomb rulers and states that Ruzsa's exponent remains the record. It does not settle this target.
- A Lean statement exists at [FormalConjectures/ErdosProblems/39.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/39.lean), but its theorem is a `sorry` placeholder and is not an accepted proof.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Give a rigorous construction of one infinite B₂ set A⊆ℕ and prove: for every 0<ε<1/2 there exist cε>0 and Nε such that A(N)≥cεN^(1/2−ε) for all integers N≥Nε. The proof must establish uniqueness of all unordered two-term sums, including diagonal sums, across the entire infinite union.

**Negative obligation.** Prove that for every infinite Sidon set A⊆ℕ there exists ε∈(0,1/2) such that A(N) is not Ω(N^(1/2−ε)); equivalently, for every c>0 and N0 there is N≥N0 with A(N)<cN^(1/2−ε).

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution supplies one infinite Sidon set and a complete proof of the stated all-large-\(N\), every-\(\epsilon\) lower bound.

A negative resolution proves that for every infinite Sidon set \(A\), some \(\epsilon\in(0,1/2)\) satisfies \(A(N)\not=\Omega(N^{1/2-\epsilon})\); equivalently, for every \(c>0\) and \(N_0\), there is \(N\ge N_0\) with \(A(N)<cN^{1/2-\epsilon}\).

## What does not count as a solution

- A different set for each \(\epsilon\).
- A \(B_2[g]\) set for \(g>1\), bounded convolution, or bounded average energy without unique sums.
- A density result only on a subsequence, only at block endpoints, or only as a limsup.
- A finite computation, experimental sequence, or unproved heuristic about random deletions.
- Re-establishing the \(\sqrt2-1\) exponent without a valid path to the target.
- Treating \(\liminf A(N)/\sqrt N=0\) as a contradiction.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State and maintain the quantifier order \(\exists A\,\forall\epsilon\,\exists c_\epsilon,N_\epsilon\,\forall N\).
2. Check all additive quadruples, including diagonal sums and collisions between nonadjacent construction blocks.
3. If elements are deleted, prove a cumulative density estimate for every sufficiently large \(N\), not only chosen scales.
4. Separate the exact Sidon condition from \(B_2[g]\), energy, and representation-function surrogates.
5. Give complete estimates with dependence on every parameter displayed.
6. Subject every claimed proof to an adversarial independent audit; identify any imported theorem precisely and verify its hypotheses.

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
