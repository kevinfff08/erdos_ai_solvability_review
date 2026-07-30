# Erdős Problem 80

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work with finite simple undirected graphs.  For an edge \(xy\) of \(G\), its triangle multiplicity is \(|N_G(x)\cap N_G(y)|\).  Define
\[
 bk(G)=\max_{xy\in E(G)}|N_G(x)\cap N_G(y)|.
\]
For fixed \(0<c<1/2\) and sufficiently large \(n\),
\[
 f_c(n)=\min\{bk(G): |V(G)|=n,\ e(G)\ge cn^2,\ \text{every edge of }G\text{ belongs to a triangle}\}.
\]
The restriction \(c<1/2\) is essential: for \(c\ge1/2\) the literal family is empty, so the original “largest \(m\)” definition has no finite value.

The primary target is the repaired, explicit residual question:

> For every fixed \(c\in(0,1/4)\), do there exist \(A_c>0\) and \(n_0(c)\) such that \(f_c(n)\ge A_c\log n\) for all \(n\ge n_0(c)\)?

A stronger asymptotic determination of \(f_c(n)\) is welcome, but do not replace this target by a statement with \(c=c(n)\), an extra degree condition, or a different graph class.

## Frozen mathematical background

Verify citations from the primary sources before using them.

- Fox and Loh proved a construction with every edge in a triangle, approximately \(n^2/4\) edges, and booksize at most \(n^{14/\log\log n}\): [arXiv:1106.0290](https://arxiv.org/abs/1106.0290).  Consequently, for each fixed \(c<1/4\), \(f_c(n)\le n^{O(1/\log\log n)}=n^{o(1)}\).  This disproves the historical positive-power conjecture; it does not disprove a logarithmic lower bound.
- The same paper explains the qualitative lower bound \(f_c(n)\to\infty\) from triangle removal and a quantitative lower bound exponential in \(\log^*n\).  Fox’s removal-lemma paper is [here](https://annals.math.princeton.edu/2011/174-1/p17).  A 2025 source still describes Fox’s general triangle-removal bound as best known: [Gishboliner–Shapira–Wigderson](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F5E7BAF97A98F8228054413823888C62/S2050509424000689a.pdf/an-efficient-asymmetric-removal-lemma-and-its-limitations.pdf).
- For \(c>1/4\), the classical Edwards/Khadzhiivanov–Nikiforov result gives a linear book, so this is not the hard regime; see [Erdős Problem 905](https://www.erdosproblems.com/latex/905).
- Potechin studies the near-threshold scale \(n^2/4-nf(n)\), not the fixed \(c<1/4\) gap: [arXiv:1412.1838](https://arxiv.org/abs/1412.1838).

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** For the explicit residual logarithmic target: prove that for every fixed c in (0,1/4) there are constants A_c>0 and n_0(c) such that every n-vertex simple graph G with n>=n_0(c), e(G)>=c n^2, and every edge in a triangle has bk(G)>=A_c log n. A stronger determination f_c(n)=Theta_c(g_c(n)) with matching upper and lower bounds also resolves the original repaired estimation request.

**Negative obligation.** Disprove the logarithmic target by giving one fixed c in (0,1/4) and graphs G_i with |V(G_i)|=n_i→infinity, e(G_i)>=c n_i^2, every edge in a triangle, and bk(G_i)/log n_i→0 (or otherwise proving that no positive A_c can work).

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution proves, with all constants and quantifiers explicit, that every fixed \(c\in(0,1/4)\) has constants \(A_c,n_0(c)\) such that every eligible graph on \(n\ge n_0(c)\) vertices satisfies \(bk(G)\ge A_c\log n\).

A negative resolution gives one fixed \(c\in(0,1/4)\) and an infinite family \(G_i\) with \(|V(G_i)|=n_i\to\infty\), \(e(G_i)\ge c n_i^2\), every edge in a triangle, and \(bk(G_i)/\log n_i\to0\), or an equally rigorous proof that no positive \(A_c\) can work.

A proof of matching asymptotic bounds \(f_c(n)=\Theta_c(g_c(n))\) for an explicit \(g_c\) is a stronger complete resolution of the repaired estimation problem.

## What does not count as a solution

- Treating the historical \(n^\epsilon\) conjecture as open: Fox–Loh already refuted it for fixed \(c<1/4\).
- Reproving merely \(f_c(n)\to\infty\), or giving no bound beyond the established removal-lemma scale.
- A construction failing the condition that every retained edge lies in a triangle.
- A theorem only near \(c=1/4\), only for \(c(n)\), or only after imposing minimum-degree, pseudorandomness, or multipartite assumptions.
- Counting total triangles, average edge codegree, or triangles through a vertex instead of maximum triangles through one edge.
- Finite experiments, heuristic asymptotics, or citations not checked in the cited source.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

- State the order of limits: fix \(c\), then let \(n\to\infty\).  State whether every constant depends on \(c\).
- Check \(e(G)\ge cn^2\) with rounding handled explicitly.
- Check triangle coverage and bound \(|N(x)\cap N(y)|\) for every edge type in a construction.
- For lower bounds, account for all eligible graphs rather than only a structured subclass.
- Do not apply a removal lemma with an unstated or directionally incorrect \(\epsilon,\delta\) dependence.
- Separate the repaired hard interval \((0,1/4)\) from the linear regime \([1/4,1/2)\) and the vacuous literal regime \([1/2,\infty)\).
- Have an independent adversarial reader check every claimed lemma, especially quantifier order and the conversion between booksize and edge common-neighborhood counts.

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
