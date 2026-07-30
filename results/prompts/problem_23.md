# Erdős Problem 23 — exact max-cut / bipartization conjecture

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

All graphs are finite, simple, and undirected. Let \(n\ge 1\) be an integer. For a graph \(G\), define

\[
\beta(G)=\min\{|F|:F\subseteq E(G),\ G-F\text{ is bipartite}\}.
\]

Equivalently, \(\beta(G)=e(G)-\operatorname{maxcut}(G)\), where \(\operatorname{maxcut}(G)\) is the maximum number of edges crossing a bipartition of \(V(G)\).

Prove or disprove:

> For every triangle-free graph \(G\) with \(|V(G)|=5n\), \(\beta(G)\le n^2\).

Equivalently, \(G\) has a spanning bipartite subgraph with at least \(e(G)-n^2\) edges. No vertices may be deleted.

The balanced blow-up \(C_5[n]\) has five independent classes of size \(n\), complete bipartite graphs exactly between cyclically consecutive classes, and satisfies \(\beta(C_5[n])=n^2\). Thus the proposed constant is sharp.

## Frozen mathematical background

- The current database record remains open: [Erdős Problems #23](https://www.erdosproblems.com/23). Treat this as a status index, not a proof.
- Balogh, Clemen, and Lidický prove the global bound \(\beta(G)\le N^2/23.5\) for an \(N\)-vertex triangle-free graph and the sharp \(N^2/25\) bound in two density ranges for sufficiently large \(N\): [arXiv:2103.14179](https://arxiv.org/abs/2103.14179). Their sharp conjecture is \(\beta(G)\le N^2/25\); at \(N=5n\) this is the target above.
- Ferudun's recent, unrefereed computer-assisted preprint claims \(a(5n)=n^2\) for \(1\le n\le40\), with ancillary exact-arithmetic material: [arXiv:2606.28041](https://arxiv.org/abs/2606.28041). This is partial progress only. Independently validate any use of its certificate or transfer lemmas.
- The statement, rather than a proof, appears in Lean with `sorry`: [FormalConjectures/23.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/23.lean).
- Historical sources include [Erdős–Faudree–Pach–Spencer (1988)](https://combinatorica.hu/~p_erdos/1988-12.pdf) and [Erdős–Győri–Simonovits (1992)](https://korandi.org/docs/misc/erdos_gyori_simonovits.pdf).

Clearly label every imported statement as proved, claimed in an unreviewed preprint, or conjectural. In particular, do not assume a stability classification of near-extremizers.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that for every positive integer n and every finite simple triangle-free graph G on exactly 5n vertices, beta(G)<=n^2; equivalently, construct or prove the existence of a cut of G with at least e(G)-n^2 crossing edges. The proof must cover n>=41 as well as the already claimed finite range, unless it rigorously imports independently verified finite-range results.

**Negative obligation.** Give an explicit positive integer n and a finite simple triangle-free graph G on 5n vertices with beta(G)>n^2, together with a proof that every bipartite spanning subgraph omits more than n^2 edges (equivalently maxcut(G)<e(G)-n^2).

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a rigorous proof for every positive integer \(n\) and every triangle-free \(G\) on exactly \(5n\) vertices that \(\beta(G)\le n^2\). It must cover all remaining \(n\), including \(n\ge41\), unless finite cases are imported from independently verified results.

A negative resolution is one explicit positive integer \(n\) and triangle-free graph \(G\) on \(5n\) vertices with \(\beta(G)>n^2\), together with a proof that every cut has fewer than \(e(G)-n^2\) crossing edges.

## What does not count as a solution

- Any bound \(\beta(G)\le c n^2\) with \(c>1\).
- A result only in one density range, for sufficiently large \(n\), for a graph subclass, or for finitely many values of \(n\), unless the omitted cases are proved separately.
- The C5 blow-up lower bound: it proves sharpness conditional on the upper bound, not the universal upper bound.
- A computational search without a proved finite reduction covering every possible counterexample.
- A floating-point flag-algebra output without exact, independently checkable certificates and a sound graphon-to-finite deduction.
- Deleting vertices, altering \(|V(G)|=5n\), or changing the problem to a balanced-cut requirement.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Maintain the normalization \(N=5n\): \(N^2/25=n^2\) only under this equality.
2. Check triangle-freeness, simplicity, and exact vertex count for every construction.
3. Prove the maximum-cut/bipartization equivalence used at each step.
4. Count all edges left inside both parts of any proposed cut.
5. Verify every strict/non-strict density endpoint when importing a density-tail theorem or applying a blow-up limit.
6. If using induction or minimal counterexamples, prove a strengthened formulation that handles vertex-count remainders rather than silently assuming divisibility persists.
7. Audit equality cases and do not infer a uniqueness/stability theorem from the C5 example.
8. For any computer-assisted lemma, preserve source, input encoding, exact certificates, hashes, verifier command, output, and an independent rerun.

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
