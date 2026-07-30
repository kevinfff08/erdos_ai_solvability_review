# Erdős Problem 128 — sparse halves in triangle-free graphs

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work with finite simple undirected graphs.  For a graph \(G=(V,E)\), write \(n=|V|\), and for \(S\subseteq V\) write \(e_G(S)=|E(G[S])|\).  A triangle means a copy of \(K_3\).

Prove or disprove the following exact statement:

> For every finite triangle-free simple graph \(G\) on \(n\) vertices, there exists \(S\subseteq V(G)\) with \(|S|=\lfloor n/2\rfloor\) and \(e_G(S)\le n^2/50\).

This is equivalent to the original local-density form: if every \(S\subseteq V(G)\) with \(|S|\ge\lfloor n/2\rfloor\) has \(e_G(S)>n^2/50\), then \(G\) contains a triangle.  Checking exactly \(\lfloor n/2\rfloor\) vertices suffices by monotonicity of induced edge counts.

Do not conflate this discrete target with a fractional-half relaxation.  In Razborov's notation a fractional half is \(\mu:V(G)\to[0,1]\) with total weight \(n/2\); for odd \(n\), its minimizer can have one weight \(1/2\).  A proved fractional upper bound \(\beta(G)\le1/50\) implies the discrete target, but that implication must be written out when used.

## Frozen mathematical background

- The original database record and bibliography are at [Erdős Problems 128](https://www.erdosproblems.com/latex/128).
- Erdős, Faudree, Rousseau and Schelp (1994) prove a general local-density criterion which, at \(\alpha=1/2\), yields the weaker \(n^2/16\) threshold; bibliographic record: [Erdős publication list](https://www.oakland.edu/Assets/upload/docs/Erdos-Number-Project/erdpubs.2010.pdf).
- Krivelevich, *On the Edge Distribution in Triangle-free Graphs*, JCTB 63 (1995), 245–260, is verified at the [author publication page](https://www.math.tau.ac.il/~krivelev/papers.html).
- Keevash and Sudakov, [*Sparse halves in triangle-free graphs*](https://www.sciencedirect.com/science/article/pii/S0095895605001644), JCTB 96 (2006), prove the target under \(|E(G)|\le n^2/12\) or \(|E(G)|\ge n^2/5\).
- Norin and Yepremyan, [*Sparse halves in dense triangle-free graphs*](https://arxiv.org/abs/1311.5818), establish further high-degree/high-average-degree and Petersen-neighborhood cases; the published version is JCTB 115 (2015), 1–25.
- Razborov, [*More about sparse halves in triangle-free graphs*](https://www.mathnet.ru/links/0062fe3a56efc9141ab3ee6dfdb710e6/sm9615_eng.pdf), Sbornik: Mathematics 213(1) (2022), proves the general fractional bound \(\beta(G)\le27/1024\), and proves the \(1/50\) target for several classes, including girth at least 5, independence number at least \(2n/5\), strongly regular graphs, and graphs with no induced \(2K_2\).  This is background, not a solution of the general target.
- A Lean statement exists in [FormalConjectures/ErdosProblems/128.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/128.lean), but its theorem body contains `sorry`; it is not a formal proof.

Treat every claimed theorem above as a theorem only within its stated hypotheses.  Treat the general \(1/50\) assertion as open unless you locate and inspect a later complete proof or counterexample.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete affirmative resolution is a proof that for every finite simple triangle-free graph G on n vertices there is S⊆V(G) with |S|=⌊n/2⌋ and e(G[S])≤n²/50, including all parity and finite-size cases. Equivalently, prove the stated local-density implication for every finite simple graph.

**Negative obligation.** A complete negative resolution is one explicit finite simple triangle-free graph G on n vertices, together with an exact, independently checkable certificate that every S⊆V(G) of size ⌊n/2⌋ satisfies e(G[S])>n²/50. Equality at n²/50 is not a counterexample.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution must give a rigorous proof, for every finite \(n\) and every finite triangle-free simple \(G\), of a set \(S\) with \(|S|=\lfloor n/2\rfloor\) and \(e_G(S)\le n^2/50\).  It must explicitly handle parity and any reduction from weighted/fractional halves.

A negative resolution must give one explicit finite triangle-free simple graph \(G\), plus an exact certificate that every \(S\subseteq V(G)\) of size \(\lfloor n/2\rfloor\) satisfies \(e_G(S)>n^2/50\).  The certificate must be independently reproducible.  Equality at \(n^2/50\) does not disprove the problem.

## What does not count as a solution

- A bound with any larger constant, including \(27/1024\), or a result with \(o(n^2)\) slack.
- A proof only for a special class, a density range, sufficiently large \(n\), or an asymptotic graph-limit statement with no finite transfer.
- A numerical SDP output, floating-point inequality, or failed heuristic counterexample search without an exact certificate and a declared stopping condition.
- A proof about crossing edges, arbitrary subgraphs, or weighted halves that never proves the required induced discrete-half statement.
- C5/Petersen blow-ups showing sharpness at equality without satisfying the strict universal counterexample condition.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State every quantifier and retain \(n=|V(G)|\) in every normalization.
2. Check the direction and strictness of every inequality: affirmative uses \(\le\), while a counterexample requires \(>\) for every half.
3. Use induced edges \(e_G(S)\), not arbitrary selected edges or a cut size.
4. Check \(\lfloor n/2\rfloor\) for odd \(n\), including any conversion from a fractional half.
5. Check candidate lemmas on C5, Petersen, Clebsch, and relevant balanced blow-ups symbolically before using them as universal claims.
6. For a flag-algebra/SDP proof, provide exact rational data, a verifiable PSD certificate, coefficient identities, and the finite-graph transfer argument.  Floating-point feasibility is discovery evidence only.
7. For an explicit counterexample, independently verify triangle-freeness and exhaust all half-sized subsets using a transparent exact method or a symmetry-reduced proof with its orbit argument.
8. Before declaring resolution, conduct a fresh literature/status search and distinguish a verified paper or formal artifact from a database label, abstract, or forum assertion.

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
