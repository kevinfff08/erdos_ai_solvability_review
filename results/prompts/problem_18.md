# Erdős Problem 18 — repaired primary target

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For a positive integer \(m\), let \(\operatorname{Div}(m)\) be its set of positive divisors. Call \(m\) *practical* if every integer \(t\) with \(1\le t<m\) is a sum of distinct members of \(\operatorname{Div}(m)\).

For practical \(m\), define
\[
r_m(t)=\min\{ |A|: A\subseteq\operatorname{Div}(m),\ \sum_{d\in A}d=t\},\qquad
h(m)=\max_{1\le t<m} r_m(t).
\]
The set \(A\) may depend on \(t\). All logarithms are natural.

Resolve this repaired primary target:
\[
\exists C>0\ \exists^\infty\text{ practical }m\quad h(m)<(\log\log m)^C.
\]
The historical unqualified formulation is not the target: Erdős set \(S(n)=0\) for non-practical \(n\), making an unqualified infinitude statement trivial. The current database explicitly repairs the quantification to practical \(m\).

The questions \(h(n!)=n^{o(1)}\) and \(h(n!)<(\log n)^{O(1)}\) are separate variants. Do not report either as resolving the primary target. The latter would imply the former.

## Frozen mathematical background

- Erdős defined the historical function \(S(n)\), noted \(S(n!)<n\), and offered $250 for the polylogarithmic-in-\(\log n\) infinitude question; inspect p. 172 of [Erdős 1981](https://renyi.hu/~p_erdos/1981-33.pdf). The historical zero convention is a statement defect, not a shortcut.
- The current [Erdős Problems record](https://www.erdosproblems.com/18) labels the repaired problem open and attributes to Vose the weaker existence result \(h(m)\ll(\log m)^{1/2}\) for infinitely many practical \(m\).
- [Vose 1985](https://academic.oup.com/blms/article-abstract/17/1/21/296830) is the cited primary paper; inspect its proof before relying on any detailed reconstruction.
- The current [forum thread](https://www.erdosproblems.com/forum/thread/18) records the ambiguity and its repair. Forum discussion is context, not a proof source.
- The [Formal Conjectures file](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/18.lean) supplies a useful max–min formalization of \(h\), but its research assertions contain `sorry`; it is not a formal proof of any open claim.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Primary repaired target: prove that there exists a fixed C>0 and infinitely many practical m for which every t with 1≤t<m is a sum of at most (log log m)^C distinct positive divisors of m.

**Negative obligation.** Primary repaired target: prove that for every C>0, only finitely many practical m satisfy h(m)<(log log m)^C.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution must prove one fixed \(C>0\) and an infinite family of practical integers \(m\) for which every \(1\le t<m\) has a distinct-divisor representation using fewer than \((\log\log m)^C\) terms.

A negative resolution must prove that for every \(C>0\), only finitely many practical \(m\) satisfy that bound.

Both directions require a fully auditable proof and a precise treatment of the fixed exponent and the sufficiently-large range where \(\log\log m\) is positive.

## What does not count as a solution

- Exploiting \(S(n)=0\) for non-practical \(n\), or omitting the practicalness condition.
- A finite computation, a heuristic, numerical fit, or a family whose infinitude is unproved.
- Short representations for many targets but not the worst target \(t\).
- A bound with an exponent depending on \(m\), such as \((\log\log m)^{C(m)}\).
- An Egyptian-fraction result with variable denominators that does not use distinct divisors of one fixed \(m\).
- A proof only about \(n!\), unless it explicitly establishes the repaired primary target.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State and use the order \(\max_t\min_A |A|\) correctly.
2. For every construction, verify practicalness and verify that all summands are distinct divisors of the same \(m\).
3. Ensure the representing subset may vary with \(t\), but that the term-count upper bound is uniform in \(t\).
4. Track every constant: the final exponent \(C\) must be independent of \(m\).
5. Prove infinitude of the family, not merely existence at sampled parameters.
6. Compare any claimed improvement honestly with Vose's \((\log m)^{1/2}\) scale.
7. If using a historical statement, first reconcile \(<m\) versus \(\le m\), and the convention for non-practical inputs.
8. Subject any claimed proof to an independent adversarial check that seeks a target \(t\) lacking the asserted representation and checks all asymptotic quantifiers.

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
