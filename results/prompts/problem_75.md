# Erdős Problem 75 — corrected ZFC target

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work in ZFC. A graph is simple and undirected. Its chromatic number \(\chi(G)\) is the least cardinality of a proper vertex-colour set; \(\alpha(H)\) is the largest size of an independent vertex set in a finite graph \(H\).

Primary target P: construct, or rule out in ZFC, a graph \(G\) with \(|V(G)|=\chi(G)=\aleph_1\) such that
\[
\forall\epsilon>0\ \exists N_\epsilon\ \forall n\ge N_\epsilon\ \forall H\subseteq G\ (|V(H)|=n\Rightarrow\alpha(H)>n^{1-\epsilon}).
\]
It is equivalent to test every induced subgraph on an \(n\)-vertex set. The threshold may depend on \(\epsilon\), never on \(H\).

Treat the follow-up Q separately unless a source explicitly requires a common witness: does there exist a graph with \(|V(G)|=\chi(G)=\aleph_1\) and fixed \(c>0,N\) such that every finite \(H\subseteq G\) with \(|H|\ge N\) has \(\alpha(H)\ge c|H|\)? Q is strictly stronger than P.

## Frozen mathematical background

- Erdős–Hajnal–Szemerédi introduced the almost-bipartite large-chromatic setting: [EHS82](https://doi.org/10.1016/S0304-0208(08)73497-2).
- Lambie-Hanson proved in ZFC that finite subgraph chromatic numbers can grow arbitrarily slowly in an \(\aleph_1\)-chromatic graph: [arXiv:1902.08177](https://arxiv.org/abs/1902.08177), published in *Advances in Mathematics* 369 (2020), 107176. Combined with \(\alpha(H)\ge |H|/\chi(H)\), this solves the old version that omitted \(|G|=\aleph_1\), but does not settle P.
- Komjáth–Shelah obtained a relevant relative-consistency result with both size and chromatic number \(\aleph_1\): [arXiv:math/0212064](https://arxiv.org/abs/math/0212064). This is not an unconditional ZFC solution.
- Lambie-Hanson–Uhrik give recent conditional Hajnal--Máté/forcing progress: [arXiv:2312.01828](https://arxiv.org/abs/2312.01828).
- The current statement is formalized but unproved (`sorry`) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/75.lean).

Do not treat the historical missing-cardinality formulation as P. The repair is documented by the [current database page](https://www.erdosproblems.com/75) and its [revision history](https://www.erdosproblems.com/history/75).

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** For P, prove in ZFC that there is one simple graph G with |V(G)|=chi(G)=aleph_1 and prove the stated forall-epsilon, eventually-forall-n, forall-finite-subgraph alpha(H)>n^(1-epsilon) property. For Q, additionally prove the same for a graph (which may be separately chosen unless explicitly required otherwise) with fixed c>0 and eventual alpha(H)>=c|H|.

**Negative obligation.** Prove in ZFC that no graph with both |V(G)|=chi(G)=aleph_1 satisfies P (respectively Q), with the quantified failure made explicit. A relative-consistency separation may establish independence only if both directions over ZFC are rigorously supplied; it is not itself a ZFC negative proof.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

A positive resolution of P is a ZFC proof of one graph satisfying every displayed quantifier, including both exact cardinal equalities. A negative resolution is a ZFC proof that no such graph exists. A genuine independence result must prove the required relative consistency in both directions over clearly stated base theories.

For Q, the same standards apply with a fixed positive linear constant. A proof of Q resolves P, but a proof of P does not resolve Q.

## What does not count as a solution

- A construction with no proof that its vertex cardinality is \(\aleph_1\).
- A proof under CH, \(\Diamond\), disjoint type guessing, or in a forcing extension presented as ZFC.
- Lambie-Hanson's solution of the no-size version.
- A finite-subgraph chromatic estimate without the quantified conversion to \(\alpha(H)>n^{1-\epsilon}\).
- A result for selected subgraphs, or thresholds depending on \(H\).
- A Lean declaration whose proof is `sorry`.
- A solution of P advertised as a solution of Q.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State the ambient axioms at the beginning and log every additional set-theoretic hypothesis.
2. Prove separately \(|V(G)|=\aleph_1\), \(\chi(G)\le\aleph_1\), and \(\chi(G)>\aleph_0\).
3. For every finite-subgraph lemma, verify all quantifier directions when inverting a growth function.
4. Derive \(\alpha(H)\ge |H|/\chi(H)\) from a proper colouring, then establish the target's strict inequality after choosing an explicit eventual threshold.
5. Check induced versus non-induced subgraphs correctly.
6. Subject every alleged ZFC extraction of an \(\aleph_1\)-sized subgraph to adversarial review; this is the known failure point.
7. If pursuing Q by shift graphs, identify exactly where CH enters and prove that no hidden cardinal-arithmetic assumption remains.

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
