# Erdős Problem 40 — density threshold for unbounded additive representations

## Definitions and canonical target

Work in \(\mathbb N=\{1,2,\ldots\}\).  For \(A\subseteq\mathbb N\), write
\[
 A(N):=|A\cap\{1,\ldots,N\}|,\qquad
 r_A(n):=(1_A*1_A)(n)=|\{(a,b)\in A^2:a+b=n\}|.
\]
Thus \(r_A\) counts **ordered** representations.  For an eventually positive function \(g:\mathbb N\to(0,\infty)\), define \(P(g)\) to mean
\[
 \forall A\subseteq\mathbb N,\quad
 \bigl[(\exists c>0,\exists N_0,\forall N\ge N_0,\ A(N)\ge c\sqrt N/g(N))\bigr]
 \Longrightarrow \limsup_{n\to\infty}r_A(n)=\infty.
\]

The target is to characterize
\[
 \mathcal G_*:=\{g:\mathbb N\to(0,\infty):g(N)\to\infty\text{ and }P(g)\}.
\]
A complete answer must say exactly which functions belong to \(\mathcal G_*\), under a stated equivalence or comparison relation if one is used.  Do not silently assume monotonicity; if it is imposed, prove a reduction from the unrestricted formulation or label the result as conditional.

Source statement: [Erdős Problems #40](https://www.erdosproblems.com/40).  The formal target is encoded in [FormalConjectures/ErdosProblems/40.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/40.lean); that file contains an unresolved `sorry`, not a proof.

## Accepted background

- Erdős Problems #40 is currently listed open, and its forum thread has no claimed solution: [problem page](https://www.erdosproblems.com/40), [thread](https://www.erdosproblems.com/forum/thread/40).
- The classical Erdős–Turán conjecture says that an asymptotic order-2 additive basis \(A\) has unbounded \(r_A\).  The formal file verifies that proving \(P(g)\) for any diverging \(g\) implies this classical conjecture.  Treat this as a checked reduction, not as a solution.
- A known negative region is essential: the Erdős–Rényi construction reported in [Erdős Problem #39](https://www.erdosproblems.com/39) gives, for every \(\varepsilon>0\), a set with \(A(N)\gg_\varepsilon N^{1/2-\varepsilon}\) and bounded \(r_A\).  Consequently \(P(N^\varepsilon)\) fails, and so does \(P(g)\) whenever \(N^\varepsilon=O(g(N))\).  Before relying on this in a formal paper, locate and cite the original construction.
- Do not confuse economical bases with bounded-representation bases.  Jain–Pham–Sawhney–Zakharov construct an explicit \(A\) with \(A+A=\mathbb N\) and \(r_A(n)=n^{o(1)}\): [arXiv:2405.08650](https://arxiv.org/abs/2405.08650).  This does not settle boundedness.
- Recent fixed-threshold results use generating functions and density of the exceptional sumset.  Li–Zhang prove results such as \(D(\mathbb N\setminus(A+A))<7/32\Rightarrow\limsup r_A>5\): [arXiv:2605.30922](https://arxiv.org/abs/2605.30922).  The hypothesis of this problem does not itself control \(A+A\), so no direct application is licensed.
- A claimed proof of the classical conjecture exists as an unevaluated OSF preprint, but it has not been accepted as a resolution: [record](https://sciety.org/articles/activity/10.31219/osf.io/mxgbu).  Treat it only as an unverified claim to audit, never as background theorem.

## Complete resolutions

A complete positive resolution is a theorem giving a precisely specified class \(\mathcal C\) of all eventually positive diverging functions and proving
\[
 g\in\mathcal C\iff P(g)
\]
for every such \(g\).  It must include the handling of nonmonotone functions or an explicit proved normalization theorem.

A complete negative resolution is a proof that \(\mathcal G_*\) is empty, namely: for every eventually positive \(g\to\infty\), construct \(A_g\subseteq\mathbb N\) and \(C_g<\infty\) with
\[
 A_g(N)\gg\sqrt N/g(N)\quad\text{for all sufficiently large }N,
 \qquad r_{A_g}(n)\le C_g\quad\text{for all }n.
\]

A significant but partial result must be labelled as such.  It may prove \(P(g_0)\) for one explicit diverging \(g_0\), or disprove \(P(g_0)\) by a fully specified bounded-representation construction.  A positive instance automatically resolves the classical Erdős–Turán conjecture, so it requires correspondingly stringent checking.

## What does not count as a solution

- Proving a statement only for additive bases, positive-density sets, or sets with a sumset-density condition not implied by the displayed counting hypothesis.
- Establishing the lower bound only for infinitely many \(N\), on average, or with a constant depending on \(N\).
- Switching silently between ordered and unordered representations.
- A construction over \(\mathbb Z\) or \(\mathbb Z/m\mathbb Z\) without a proof that transfers to one-sided \(\mathbb N\).
- A finite computation, numerical experiment, heuristic, random model, or a claim that an existing preprint is correct without independently checking its proof.
- A theorem for one function \(g\) presented as the requested characterization of all \(g\).

## Required correctness checks

1. State exactly the domains, all quantifiers, the final positivity of \(g\), and the all-sufficiently-large-\(N\) meaning of \(\gg\).
2. Prove each comparison-direction claim.  In particular, if \(g_1=O(g_2)\), then the hypothesis for \(g_1\) is stronger; therefore \(P(g_2)\Rightarrow P(g_1)\).  Conversely, one counterexample for \(g_1\) refutes \(P(g_2)\).
3. For every counterexample, prove both the uniform counting lower bound and a single finite global bound on \(r_A(n)\), including diagonal and ordered-pair conventions.
4. For every positive proof, show why the density hypothesis alone supplies every subsequently used coverage, energy, or regularity hypothesis.
5. Audit every use of a result over \(\mathbb Z\), a finite cyclic group, or a random construction for the missing one-sided/infinite/uniform step.
6. If formalization is attempted, build against the linked Formal Conjectures definition or provide an explicit translation lemma; no `sorry`, axiom, or unproved external theorem may be concealed in the final certificate.

## Required deliverables

- `statement.md`: normalized target, conventions, and a proof of any reduction between variants.
- `literature_audit.md`: primary-source bibliography with stable links; separate theorems, conjectures, and unverified claims.
- `main.tex` or `main.md`: a self-contained proof or construction, with a dependency graph of lemmas.
- `adversarial_check.md`: line-by-line audit focused on quantifiers, asymptotic constants, ordered representations, and transfer between algebraic settings.
- If a computational subtask is used, provide code, exact inputs, version information, output certificate, and a proof that the computation answers the declared finite lemma.
- Update `research_state.md` after every substantive wave.

## Dynamic Multiagent v2 protocol

Use a research root coordinating at most four concurrent agents total, including the root.  Begin with independent approaches rather than fixed role assignments.  Maintain an approach registry recording for every live or retired route: exact target lemma, hypotheses, claimed novelty, dependencies, status, and a link to its proof notes.

In wave 1, allocate independent probes among: source and claim verification; construction/counterexample transfer; proof of a positive density-to-representation lemma; and formal statement/quantifier audit.  The root compares results before opening wave 2, eliminates duplicated routes, and reuses freed slots for the most falsifiable remaining lemma.  No agent may treat another agent's assertion as a theorem without reading its argument.

Each wave ends with adversarial checking by an agent not authoring the argument.  Counterexample work must be checked for every sufficiently large \(N\), not samples.  Positive work must receive an adversarial search for hidden additive-basis, regularity, or monotonicity assumptions.  Reassign a slot immediately when its declared question is resolved, blocked by a proved obstruction, or shown redundant.  Continue in multiple waves until a complete proof/counterexample exists or the current bottleneck has been isolated with rigorous partial results.

Resource allocation is proof-first.  Permit at most one optional computational subtask at a time.  Before launching it, write in the registry: the exact finite lemma, hypotheses, input range, certificate format, and stopping condition.  On obtaining the answer, validate the certificate and immediately return that slot to proof or audit work; computation may not become open-ended exploration.

## Persistence and resumability

`research_state.md` is the authoritative checkpoint.  It must list the canonical target, checked sources, active definitions, accepted lemmas with proof locations, rejected routes and counterexamples, unresolved obligations, agent registry, and the next smallest proof obligation.

At every checkpoint, save enough detail that a fresh research root can reproduce the state without relying on chat history.  If a runtime boundary occurs before a complete resolution, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, state exactly what remains unproved, preserve all citations and certificates, and resume from the smallest unresolved obligation.  Never report a solution merely because a promising route, formal statement, or finite experiment exists.
