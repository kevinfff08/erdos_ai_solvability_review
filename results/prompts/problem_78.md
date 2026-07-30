# Erdős Problem 78 — revised, strongly explicit Ramsey-graph target

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

A finite simple graph \(G\) has clique number \(\omega(G)\) and independence number \(\alpha(G)\).  Call \(G\) \(K\)-Ramsey if \(\max\{\omega(G),\alpha(G)\}<K\).  Let \(R(k)\) be the least \(n\) for which every red/blue edge-colouring of \(K_n\) contains a monochromatic \(K_k\); equivalently, every \(n\)-vertex graph has a clique or independent set of size \(k\).

The historical wording says “constructive proof” but does not define it. For this prompt, the following repaired strong-explicit formulation is the fixed canonical target:

Prove that there are absolute constants \(c>0\), \(N_0\), and one uniform deterministic algorithm \(A\) such that, for every \(N\ge N_0\) and distinct \(u,v\in[N]\), \(A(N,u,v)\) decides whether \(uv\in E(G_N)\) in time \(\operatorname{poly}(\log N)\), where \(G_N\) is a simple graph satisfying
\[
\max\{\alpha(G_N),\omega(G_N)\}<c\log_2 N.
\]

Then derive, with constants displayed, that \(R(k)>C^k\) for some fixed \(C>1\) and every sufficiently large integer \(k\).  A graph family available only on a stated cofinal size sequence is acceptable only if the proof includes a valid reduction/padding argument to the Ramsey-number conclusion.

## Frozen mathematical background

- Erdős’s 1947 probabilistic argument proves an exponential existence lower bound for diagonal Ramsey numbers, but does not provide the required explicit family: [Some Remarks on the Theory of Graphs](https://doi.org/10.1090/S0002-9904-1947-08785-1).
- Cohen proved an explicit \(K\)-Ramsey construction with \(K=2^{(\log\log N)^c}\), for an absolute \(c>0\): [SIAM Journal on Computing version](https://epubs.siam.org/doi/10.1137/16M1096219).  This is a theorem, not the desired conclusion.
- Li’s FOCS 2023 theorem gives explicit \(K\)-Ramsey graphs with \(K=\log^{O(1)}N\): [FOCS DOI](https://doi.org/10.1109/FOCS57990.2023.00075), [open preprint](https://arxiv.org/abs/2303.06802).  The hidden exponent is not known from this statement to be one; do not cite it as an \(O(\log N)\)-Ramsey construction.
- Literature distinguishes a global explicit construction from a very/strongly explicit construction with local \(\operatorname{poly}(\log N)\)-time adjacency; see the definition discussion in [Gopalan](https://www.cs.umd.edu/~gasarch/TOPICS/CRT/GopRam.pdf).  The target above deliberately requires the latter.

No frozen result above proves the target.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** For the repaired strong-explicit target: exhibit absolute constants c>0 and N0 and prove that a single deterministic local algorithm constructs, for every N>=N0, a simple graph G_N with max{alpha(G_N),omega(G_N)}<c log_2 N and the declared poly(log N) adjacency runtime. Derive explicitly that this implies R(k)>C^k for a fixed C>1 and every sufficiently large k.

**Negative obligation.** Give a rigorous impossibility theorem in the declared construction model showing that no uniform strongly explicit family can have \(\max\{\alpha(G_N),\omega(G_N)\}=O(\log N)\), or prove that the fixed target model is internally inconsistent.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution must supply all of the following:

1. A fully specified uniform family \(G_N\) and local deterministic adjacency algorithm.
2. A proved \(\operatorname{poly}(\log N)\) runtime bound, including parameter encoding and any preprocessing assumptions.
3. A proof for every sufficiently large claimed \(N\) that both \(\alpha(G_N)\) and \(\omega(G_N)\) are less than \(c\log_2N\), with an absolute \(c\).
4. A correct derivation of \(R(k)>C^k\) for all sufficiently large \(k\).

A negative resolution must be a genuine impossibility theorem in this declared strong-explicit model, with all model assumptions stated.

## What does not count as a solution

- Repeating the random-graph/probabilistic existence proof.
- A finite search, numerical experiment, or heuristic that works for selected sizes only.
- A \(\log^dN\)-Ramsey family for fixed \(d>1\), including the currently known Li-type bound.
- A construction that controls cliques but not independent sets, or vice versa.
- A bipartite result without a proved conversion to a non-bipartite graph preserving the needed parameters.
- Declaring an exponentially slow enumeration “explicit” under the fixed strong-explicit model.
- A claim of adjacency computability that silently uses an exponentially large table, nonuniform advice, random bits, or unproved oracle.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

- State the graph model: vertex labels, graph size, symmetry, and absence of loops.
- Track every logarithm base and all absolute constants through the \(N\)-to-\(k\) conversion.
- Check quantifiers: constants independent of \(N,k\); construction for all sufficiently large sizes or a justified padding reduction.
- Prove both homogeneous-set obstructions, using complementation correctly.
- For extractor/disperser routes, prove the exact parameter transfer: source entropy, error/disperser property, monochromatic rectangle exclusion, bipartite-to-non-bipartite conversion, and the final \(K\) exponent.
- Distinguish theorem statements verified in primary sources from conjectural extrapolations or informal claims.
- Perform adversarial review aimed specifically at accidental \(\log^{O(1)}N\) notation hiding an exponent greater than one.

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
