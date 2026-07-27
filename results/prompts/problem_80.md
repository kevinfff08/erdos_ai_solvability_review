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

## Accepted background

Verify citations from the primary sources before using them.

- Fox and Loh proved a construction with every edge in a triangle, approximately \(n^2/4\) edges, and booksize at most \(n^{14/\log\log n}\): [arXiv:1106.0290](https://arxiv.org/abs/1106.0290).  Consequently, for each fixed \(c<1/4\), \(f_c(n)\le n^{O(1/\log\log n)}=n^{o(1)}\).  This disproves the historical positive-power conjecture; it does not disprove a logarithmic lower bound.
- The same paper explains the qualitative lower bound \(f_c(n)\to\infty\) from triangle removal and a quantitative lower bound exponential in \(\log^*n\).  Fox’s removal-lemma paper is [here](https://annals.math.princeton.edu/2011/174-1/p17).  A 2025 source still describes Fox’s general triangle-removal bound as best known: [Gishboliner–Shapira–Wigderson](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F5E7BAF97A98F8228054413823888C62/S2050509424000689a.pdf/an-efficient-asymmetric-removal-lemma-and-its-limitations.pdf).
- For \(c>1/4\), the classical Edwards/Khadzhiivanov–Nikiforov result gives a linear book, so this is not the hard regime; see [Erdős Problem 905](https://www.erdosproblems.com/latex/905).
- Potechin studies the near-threshold scale \(n^2/4-nf(n)\), not the fixed \(c<1/4\) gap: [arXiv:1412.1838](https://arxiv.org/abs/1412.1838).
- The current database record remains open but is not proof of status: [Problem 80](https://www.erdosproblems.com/80) and its [forum thread](https://www.erdosproblems.com/forum/thread/80).

## Complete resolutions

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

## Required correctness checks

- State the order of limits: fix \(c\), then let \(n\to\infty\).  State whether every constant depends on \(c\).
- Check \(e(G)\ge cn^2\) with rounding handled explicitly.
- Check triangle coverage and bound \(|N(x)\cap N(y)|\) for every edge type in a construction.
- For lower bounds, account for all eligible graphs rather than only a structured subclass.
- Do not apply a removal lemma with an unstated or directionally incorrect \(\epsilon,\delta\) dependence.
- Separate the repaired hard interval \((0,1/4)\) from the linear regime \([1/4,1/2)\) and the vacuous literal regime \([1/2,\infty)\).
- Have an independent adversarial reader check every claimed lemma, especially quantifier order and the conversion between booksize and edge common-neighborhood counts.

## Required deliverables

Produce a research report containing:

1. A self-contained statement of the exact target and all conventions.
2. A source ledger with direct URLs, publication status, and a distinction between proved results, conjectures, and deductions.
3. A proof or counterexample family if complete; otherwise a rigorously proved intermediate lemma, its exact scope, and a precise explanation of the remaining gap.
4. An adversarial proof audit for every claimed result, including a checklist for density, edge coverage by triangles, and booksize.
5. A short status update comparing any new result quantitatively with \(2^{\Omega_c(\log^*n)}\) and \(n^{O(1/\log\log n)}\).
6. Reproducible artifacts only if a permitted finite computation is used, including code, input bounds, certificates, and a verification script.

## Dynamic Multiagent v2 protocol

Create a research root and maintain an approach registry containing: approach identifier, target lemma, assumptions, references checked, current proof state, counterexamples found, dependencies, and reason for stopping or continuing.  Use at most four concurrent agents.

Start with independent waves rather than fixed permanent assignments.  Early work should independently audit the current literature, seek lower-bound mechanisms, test incompatibility with known upper constructions, and inspect exact statement/threshold issues.  After each wave, merge only verified facts into the registry, identify duplicated approaches, and dynamically reuse released slots for the most consequential unresolved lemma.  Do not prescribe a permanent mathematical method or a static agent allocation.

Every proposed proof, construction, or reduction must receive adversarial checking by an agent that did not originate it.  The checker must attempt to falsify the claimed quantifiers, density estimate, edge-in-triangle condition, and maximum-book bound.  Maintain multiple waves until all active lines either produce a verified deliverable or have a recorded obstruction.

Allocate resources proof-first.  At most one optional computational subtask may run at once, and only after the registry states its exact lemma, finite hypotheses, certificate format, vertex/parameter range, and stopping condition.  Computation may search for a counterexample to a specified finite lemma or verify a finite certificate; it may not be used as asymptotic evidence.  Reassign that slot immediately after its declared question is answered.

## Persistence and resumability

Maintain `research_state.md` at the research root.  At every checkpoint record the canonical target, repaired parameter domain, source ledger, approach registry, verified lemmas, failed approaches with reasons, computational certificates if any, and next highest-priority questions.

If a runtime boundary interrupts incomplete work, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`, state exactly which claims were verified and which were not, preserve all audit objections, and resume from the registry.  Do not issue a final mathematical-resolution claim until an independent adversarial proof check has passed.
