# Erdős Problem 50 — proof-first investigation

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let \(\phi(n)\) be Euler's totient function. For \(0\le c\le1\), define
\[
f(c)=\lim_{N\to\infty}\frac{1}{N}\#\{1\le n\le N:\phi(n)/n<c\}.
\]
Schoenberg's theorem gives this natural density, and the resulting distribution function is continuous. Investigate the following exact target:

> Is there an \(x\in(0,1)\) such that the finite ordinary two-sided derivative \(f'(x)\) exists and is positive?

Equivalently, prove or refute
\[
\forall x\in(0,1),\qquad f'(x)\in\mathbb R\ \Longrightarrow\ f'(x)\le0.
\]

Do not silently change \(<\) to \(\le\), include endpoints, replace an ordinary derivative by a one-sided/Dini/approximate derivative, or omit the finiteness requirement.

## Frozen mathematical background

- In the primary source, [Erdős (1995)](https://revistas.usp.br/resenhasimeusp/en/article/view/74798), the question is explicitly about a **finite positive derivative**.
- Schoenberg established the limiting distribution; see [Schoenberg (1936)](https://doi.org/10.1090/S0002-9947-1936-1501849-X) and the historical account in [Tenenbaum–Toulmonde (2006)](https://tenenb.perso.math.cnrs.fr/PPP/EulerLocal.pdf).
- Erdős proved the distribution measure is purely singular. Thus \(f'=0\) almost everywhere, but this does not itself exclude exceptional points of positive finite derivative.
- Tenenbaum–Toulmonde obtain detailed local information near \(1\), including an asymptotic expansion for \(1-f(1-1/\sigma)\); this is accepted background only, not a solution of the global pointwise target.
- The [FormalConjectures file](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/50.lean) contains declarations, but the relevant proofs are `sorry`; it is not a verified resolution.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A proof of the Erdős assertion: for every x∈(0,1), if the finite ordinary two-sided derivative f'(x) exists, then f'(x)≤0. Since f is nondecreasing, this is equivalently the exclusion of positive finite derivatives, but the proof must establish the required pointwise statement rather than only an a.e. statement.

**Negative obligation.** A disproof of the Erdős assertion: give a specified x∈(0,1) and L∈(0,∞), and prove lim_{h→0}[f(x+h)-f(x)]/h=L, controlling both h>0 and h<0 under the exact density-defined f.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

A complete proof of Erdős's assertion proves, for every \(x\in(0,1)\), that existence of the finite two-sided derivative implies \(f'(x)\le0\).

A complete disproof gives a concrete \(x\in(0,1)\) and \(L\in(0,\infty)\), then proves
\[
\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=L.
\]

Every use of external theorems must give a direct source URL, exact statement, hypotheses, and an explanation of how those hypotheses apply.

## What does not count as a solution

- Proving pure singularity or \(f'=0\) almost everywhere.
- Proving a claim only outside a null set, on a dense set, or at special rational points.
- A one-sided, Dini, approximate, distributional, or numerical derivative.
- A result for a different CDF convention without proving its equivalence for the exact target.
- A finite-prime model or computer experiment lacking a uniform, rigorous tail estimate at the difference-quotient scale.
- An assertion that the Lean declaration is formalized proof while its dependencies contain `sorry`.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State whether each argument uses \(<\) or \(\le\), and justify any transfer using continuity/no-atom facts.
2. Verify the density-to-probability-model correspondence before using independent prime-divisibility variables.
3. Audit every interchange of \(N\to\infty\), prime cutoff \(\to\infty\), and \(h\to0\).
4. For any derivative claim, prove convergence for both signs of \(h\), to one finite real limit.
5. For any universal exclusion, handle all \(x\in(0,1)\), including exceptional points where singular-measure theorems are silent.
6. For local asymptotics near \(1\), verify their domain and show exactly how they imply a statement at the proposed point.
7. Subject every promising proof to an adversarial check specifically testing the invalid inference “singular implies no positive derivative anywhere.”

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
