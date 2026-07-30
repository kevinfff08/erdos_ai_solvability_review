# Erdős Problem 44 — prescribed-prefix near-optimal Sidon extension

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

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

## Frozen mathematical background

- The current Erdős Problems record lists this exact target as open and notes the historical implication \(#707\Rightarrow#44\Rightarrow#329\): <https://www.erdosproblems.com/44>.
- A Lean statement exists, with \(M>N\), but contains `sorry` and is not a proof: <https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/44.lean>.
- Alexeev and Mixon disproved the stronger assertion that every finite Sidon set extends to a finite perfect difference set (PDS): <https://arxiv.org/abs/2510.19804>. This invalidates one sufficient route but does **not** disprove the target here.
- Cilleruelo and Nathanson construct infinite perfect difference sets from dense Sidon sets: <https://arxiv.org/abs/math/0609244>. This is background on infinite extension and does not give the prescribed-prefix near-optimal finite endpoint required here.
- Eberhard and Manners study the apparent structure of dense finite-group Sidon sets and explicitly leave relevant structural conjectures open: <https://doi.org/10.37236/11191>.

Treat each item above as exactly what it states. In particular, PDS non-extension, finite computations, and informal claims do not settle this problem.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that for every N∈Z_{≥1}, every Sidon A⊆[1,N], and every ε∈(0,1), there are integers M>N and B⊆[N+1,M] such that A∪B is Sidon and |A∪B|≥(1−ε)√M. The proof must cover arbitrary finite A, not merely selected or maximal A.

**Negative obligation.** Exhibit explicit N, a Sidon A⊆[1,N], and ε0∈(0,1) and prove that for every integer M>N and every B⊆[N+1,M], either A∪B is not Sidon or |A∪B|<(1−ε0)√M.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

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

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State the Sidon convention precisely and include repeated summands such as \(2a=b+c\).
2. For every proposed extension, separately audit all old–old, old–new, and new–new difference/sum collisions.
3. Keep all quantifiers in the target order; a construction may depend on \(N,A,\varepsilon\).
4. If representatives of a cyclic-group construction are used, prove that modular uniqueness survives passage to integers; explicitly exclude wraparound collisions.
5. If a negative proof uses a maximality or compactness assertion, prove its scope covers every larger \(M\), not only a chosen family of endpoints.
6. Identify exactly where any density loss occurs and prove it can be made at most \(\varepsilon\), rather than merely \(o(1)\) under incompatible limits.
7. Do not invoke the known PDS counterexamples as a counterexample to this target.

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
