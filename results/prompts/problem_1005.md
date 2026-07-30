# Erdős Problem 1005: similarly ordered Farey fractions

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For each integer \(n\ge 4\), let
\[
F_n=(a_1/b_1,\ldots,a_{N_n}/b_{N_n})
\]
be the Farey sequence of order \(n\): all reduced fractions \(a/b\in[0,1]\) with \(0\le a\le b\le n\) and \(\gcd(a,b)=1\), listed in strictly increasing order, including \(0/1\) and \(1/1\). Two reduced fractions \(a/b\) and \(c/d\) are *similarly ordered* if
\[
(a-c)(b-d)\ge 0.
\]
Define \(f(n)\) as the largest integer \(m\ge0\) for which every pair
\[
1\le k<l\le N_n,\qquad l-k\le m,
\]
has \(a_k/b_k\) and \(a_l/b_l\) similarly ordered.

Primary target: determine whether there is a constant \(c>0\) such that
\[
f(n)=(c+o(1))n,
\]
equivalently whether \(f(n)/n\) converges to a positive limit as \(n\to\infty\) through all integers.

A stronger current conjecture is
\[
f(n)=\lfloor n/4\rfloor+d_n\quad(n\ge92),
\]
where \(d_n=1,2,2,4\) for \(n\equiv0,1,2,3\pmod4\), respectively.

## Frozen mathematical background

- Erdős proved that \(f(n)\gg n\) in 1943: [Erdős, *A Note on Farey Series*](https://www.renyi.hu/~p_erdos/1943-01.pdf). This is a theorem, not the requested asymptotic.
- Wouter van Doorn's publicly available 2025 arXiv v1 proves
  \[
  f(n)\ge\frac n{12}(1-4n^{-1/3})
  \]
  and, for every \(n\ge4\),
  \[
  f(n)\le\lfloor n/4\rfloor+d_n.
  \]
  See [arXiv:2509.00121](https://arxiv.org/abs/2509.00121) and its [HTML full text](https://arxiv.org/html/2509.00121v1). These are the strongest verified results located in this audit.
- The same preprint **conjectures**, but does not prove, equality in the latter formula for every \(n\ge92\); its finite calculation through \(n\le5000\) is evidence only.
- The standard consecutive-Farey criterion is available for use: two reduced fractions \(a/b<c/d\) are consecutive in \(F_n\) iff \(bc-ad=1\) and \(\max(b,d)\le n<b+d\).

Treat the 2025 result as a preprint: verify any imported lemma against the actual text and do not describe its conjecture as a theorem.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** For the original explicit subquestion: prove that there is a real c>0 such that lim_{n->infinity} f(n)/n=c, with all Farey-sequence conventions stated. A stronger affirmative resolution is a proof that f(n)=floor(n/4)+d_n for every n>=92, where d_n is 1,2,2,4 for residues 0,1,2,3 modulo 4; this implies c=1/4.

**Negative obligation.** Disprove the asymptotic-constant question by proving that f(n)/n has no limit (for example, by rigorously separating its liminf and limsup), or disprove the sharper conjecture by giving a specific n>=92 with an exact certified value of f(n) different from floor(n/4)+d_n. A proposed counterexample must enumerate or certify the relevant Farey indices and show the defining universal condition fails or holds as claimed.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution of the primary target is a rigorous proof of \(\lim_{n\to\infty}f(n)/n=c>0\), with the value of \(c\) identified. A proof of the displayed exact formula for every \(n\ge92\) is a stronger complete resolution and gives \(c=1/4\).

A negative resolution is a rigorous proof that \(f(n)/n\) has no limit, for example by proving a strict separation between its liminf and limsup. A negative resolution of the stronger conjecture is a rigorously certified counterexample \(n\ge92\), including the exact relevant Farey indices and a verification of the resulting value or of the failed universal condition.

## What does not count as a solution

- Checking finitely many values, regardless of range.
- Reproving either known linear bound without closing the asymptotic question.
- Establishing a limit only on a subsequence.
- Finding a non-similarly-ordered pair but mishandling the fact that distance \(d\) implies \(f(n)\le d-1\).
- Heuristic density arguments, floating-point evidence, or a proposed recurrence without proof that it controls every valid pair \((k,l)\).
- Claiming the exact formula solely because it matches data or the upper-bound construction.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State whether every fraction includes \(0/1\) and \(1/1\), and use reduced numerator-denominator representatives throughout.
2. For every global claim, quantify over all \(1\le k<l\le N_n\), not merely adjacent fractions or one local window.
3. Keep \((a_l-a_k)(b_l-b_k)\ge0\) distinct from its strict negation; audit all equality cases.
4. Audit every conversion between a bad-pair distance and a bound on \(f(n)\) for an off-by-one error.
5. If proving the sharp formula, separately audit the four classes modulo \(4\), the threshold \(92\), and every finite exceptional range needed by the proof.
6. If using an asymptotic \(o(1)\), give its quantifier order and demonstrate that it holds over all sufficiently large integers, not a density-one set.
7. Every citation must link to the primary paper or arXiv record and distinguish theorem, conjecture, and computation.

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
