# Erdős Problem 70: audit-driven research task

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work in ZFC. Let \(\mathfrak c=2^{\aleph_0}\), identified with the initial ordinal of that cardinality. For an ordinal \(\kappa\), \([\kappa]^3\) is the set of unordered three-element subsets of \(\kappa\). For a coloring \(d:[\mathfrak c]^3\to\{0,1\}\), write
\[
\mathfrak c\to(\beta,n)^3_2
\]
when every such \(d\) has either:

1. a color-0 homogeneous set \(A\subseteq\mathfrak c\) with inherited ordinal order type \(\operatorname{otp}(A)=\beta\), or
2. a color-1 homogeneous set \(B\subseteq\mathfrak c\) with \(|B|=n\).

Canonical target: prove or refute in ZFC that \(\mathfrak c\to(\beta,n)^3_2\) for every countable ordinal \(\beta<\omega_1\) and every finite \(n\ge2\).

The cases \(n=2\) and \(n=3\) are trivial for triple colorings. Substantive work begins at \(n=4\). Do not replace \(\mathfrak c\), the initial ordinal, by the ordinary ordered real line unless an explicitly proved reduction justifies it.

## Frozen mathematical background

- Erdős and Rado introduced the partition calculus in [A Partition Calculus in Set Theory (1956)](https://www.renyi.hu/~p_erdos/1956-02.pdf). Their real-order theorem gives the historical \(\omega+m\), finite-4 level; a modern accessible statement and proof discussion is in [Jones (2000)](https://doi.org/10.37236/1502). This is a theorem, not the desired all-countable-ordinal result.
- Milner and Prikry proved in ZFC that \(\omega_1\to(\omega\cdot2+1,4)^3\), using a forcing model and absoluteness; see [their 1991 paper](https://doi.org/10.1016/0012-365X(91)90336-Z). This is a theorem.
- Jones proved \(\omega_1\to(\omega+m,n)^3\) for all finite \(m,n\); see [Jones (2007)](https://doi.org/10.1090/S0002-9939-06-08538-8). This is a theorem.
- Jones proved \(\omega_1\to(\omega\cdot2+1,n)^3\) for every finite \(n\); see [Jones (2018)](https://doi.org/10.1090/proc/13503). This is the strongest directly verified result in this audit.
- Since \(\omega_1\le\mathfrak c\), restriction of a coloring proves the left-monotonic implication \(\omega_1\to(\beta,n)^3_2\Rightarrow\mathfrak c\to(\beta,n)^3_2\). Hence the 2018 theorem settles the canonical target for \(\beta\le\omega\cdot2+1\).
- The general assertion is still treated as open by the current [Erdős Problems entry](https://www.erdosproblems.com/70). A 2025 expert discussion also describes the stronger \(\omega_1\)-version as a conjecture, but that forum source is not a proof: [MathOverflow](https://mathoverflow.net/questions/448855/are-infinite-ramsey-numbers-completely-known/488725).

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete affirmative resolution is a ZFC proof that for every countable ordinal beta, every finite n >= 2, and every d:[c]^3 -> 2, one of the two stated homogeneous alternatives exists. The proof must explicitly use c as the initial ordinal of continuum and must cover beta beyond omega*2+1 and n >= 4.

**Negative obligation.** A complete negative resolution is a ZFC construction of a specific countable beta and finite n >= 4 together with a coloring d:[c]^3 -> 2 having neither a color-0 homogeneous subset of order type beta nor a color-1 homogeneous n-set. If the intended objective is ZFC decidability rather than truth in the ambient universe, an independence resolution requires rigorously verified models establishing opposite outcomes for the canonical statement.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution requires a complete ZFC proof of the canonical target for every countable \(\beta\) and every finite \(n\ge2\), explicitly covering the presently unverified range beyond \(\omega\cdot2+1\) for \(n\ge4\).

A negative resolution requires a specific countable \(\beta\), a finite \(n\ge4\), and a ZFC-defined coloring \(d:[\mathfrak c]^3\to2\) for which neither stipulated homogeneous alternative exists, with a proof of both failures.

An independence resolution is complete only if it precisely concerns the canonical initial-ordinal statement and rigorously gives opposite models (or otherwise establishes the exact metamathematical status). A one-sided relative-consistency theorem is not, by itself, a resolution of the ZFC question.

## What does not count as a solution

- Reproving any case already covered by \(\beta\le\omega\cdot2+1\), or treating only \(n\le3\).
- A theorem about a real order, a separable linear order, an arbitrary set of reals, or a different ordering, without a proved transfer to the initial ordinal \(\mathfrak c\).
- A coloring of pairs, ordered triples rather than the intended unordered triples without an equivalence proof, a symmetric Ramsey relation, or a different color assignment.
- A result conditional on MA, CH, PFA, large cardinals, or another additional hypothesis unless it is converted into the claimed ZFC conclusion or used in a complete independence proof.
- Finite computation, random experiments, pattern matching, or a literature citation without reconstructing the exact theorem hypotheses and conclusion.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State every arrow relation in expanded quantifier form before using it.
2. Distinguish the cardinal \(\mathfrak c\), its initial ordinal, and the usual linear order on \(\mathbb R\).
3. For a \(\beta\)-homogeneous set, verify exact inherited order type \(\beta\), not merely countable cardinality.
4. Verify the asymmetric color roles: color 0 produces \(\beta\), color 1 produces \(n\).
5. When using monotonicity, write the restriction/embedding map explicitly and preserve the relevant order type.
6. For any forcing argument, state the forcing extension, the formula being transferred, all parameters, and the absoluteness principle used.
7. Independently adversarial-check every purported counterexample against both alternatives.
8. Before declaring a new boundary case open or solved, inspect the relevant primary paper rather than relying on a survey snippet.

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
