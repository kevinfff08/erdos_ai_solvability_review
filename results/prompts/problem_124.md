# Erdős Problem 124 — repaired BEGL high-power target

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Do **not** work from the literal supplied condition \(\sum_{i=1}^r1/(d_r-1)\ge1\). For strictly increasing integers \(3\le d_1<\cdots<d_r\), it has no instances: \(d_r\ge r+2\), so its left side is at most \(r/(r+1)<1\).

Fix a finite set \(A=\{d_1,\ldots,d_r\}\) of distinct integers \(d_i\ge3\). For \(d\ge1\), \(k\ge0\), define
\[
P(d,k)=\left\{\sum_{j\in F}d^j:F\subseteq\{k,k+1,\ldots\}\text{ finite}\right\},
\]
where the empty sum is \(0\).

The target is the repaired Burr--Erdős--Graham--Li conjecture:
\[
\sum_{i=1}^r\frac1{d_i-1}\ge1,\qquad\gcd(d_1,\ldots,d_r)=1
\]
imply that for every fixed \(k\ge1\) there exists \(N=N(A,k)\) such that every integer \(n\ge N\) lies in
\[
P(d_1,k)+\cdots+P(d_r,k).
\]
Equivalently, \(n=\sum_i c_i a_i\) with \(c_i\in\{0,1\}\), \(a_i\in P(d_i,k)\); if \(0\in P(d_i,k)\) is retained, the \(c_i\) are redundant. The finite exponent sets may depend on \(n\), but \(A,k\) are fixed before \(N\).

## Frozen mathematical background

- BEGL96 is the primary source: Burr, Erdős, Graham, and Li, *Complete sequences of sets of integer powers*, Acta Arith. 77 (1996), 133--138, https://matwbn.icm.edu.pl/ksiazki/aa/aa77/aa7722.pdf . It defines \(\operatorname{Pow}(A;s)\) using exponents \(\ge s\ge1\), states the repaired conjecture, and supplies several non-general sufficient conditions.
- BEGL96 records that the finite-family reciprocal condition is necessary when it fails, via Diophantine approximation, and that gcd one is immediately necessary. These are necessary conditions, not a proof of sufficiency.
- BEGL96 explicitly reports that the largest omission for \(\operatorname{Pow}(\{3,4,7\};1)\) is 581. Before using an all-\(k\) \(\{3,4,7\}\) special case, inspect the primary proof or clearly label it as a database-reported result.
- The k=0 version allowing \(1\) is a different, solved statement; the current record and its forum explain the distinction: https://www.erdosproblems.com/124 and https://www.erdosproblems.com/forum/thread/124?order=oldest . Do not infer the target from that solution.
- Melfi's infinite-base construction is outside scope: https://www.rivmat.unipr.it/fulltext/2004-3s/pdf/16.pdf . The target requires finite \(A\).

Every imported result must be labeled theorem, conjecture, observation, or computational evidence, with an inspected direct source link.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** For the repaired BEGL target, prove that for every finite A={d_1,...,d_r} of distinct integers at least 3 with sum_i 1/(d_i-1)>=1 and gcd(A)=1, and every k>=1, there exists N(A,k) such that every n>=N(A,k) belongs to sum_i P(d_i,k).

**Negative obligation.** Give one explicit finite A and k>=1 satisfying d_i>=3, sum_i 1/(d_i-1)>=1, and gcd(A)=1, together with a rigorous proof that arbitrarily large integers are absent from sum_i P(d_i,k).

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution proves the displayed statement for every finite admissible \(A\), every \(k\ge1\), and every integer beyond a valid \(N(A,k)\).

A negative resolution gives one explicit finite admissible \(A\) and \(k\ge1\), plus a rigorous proof that arbitrarily large integers do not belong to \(\sum_{d\in A}P(d,k)\).

## What does not count as a solution

- Declaring victory from the supplied d_r-only condition: that merely finds the transcription's empty parameter domain.
- Reproving the k=0 theorem, allowing \(d_i^0=1\), or using any exponent below k.
- Proving only a special tuple, k=1, strict reciprocal inequality, an infinite base family, or a base set depending on n.
- Checking any finite interval without a proved finite-to-infinite tail argument.
- Establishing density, an average representation count, or selected residue classes instead of every sufficiently large integer.
- Treating a search snippet, forum assertion, or `sorry`-containing formal statement as a proof.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Establish from BEGL96 that the reciprocal condition is \(\sum_i1/(d_i-1)\ge1\), and preserve the audit record of the d_r typo.
2. Check finiteness, distinctness, \(d_i\ge3\), gcd one, and the exact quantifier order in every claimed theorem.
3. Audit every carry, scaling, and residue adjustment: it must not create an exponent \(<k\) or repeat an exponent within a base expansion.
4. For an affirmative route, identify exactly why all n beyond N are covered, including equality cases of the reciprocal sum.
5. For a negative route, prove the omission is unbounded and recheck all hypotheses for the proposed tuple.
6. Independently verify any cited Lean artifact: source imports, theorem statement, absence of `sorry`, and successful typecheck.

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
