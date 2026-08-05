# Erdős Problem 545: Extremal Ramsey number among graphs with a fixed edge count

## Primary mathematical objective

**Task mode: mathematical proof research**

The status and statement audit was completed on 2026-08-05. Treat the canonical target and frozen background below as settled inputs. Do not investigate whether the problem is open, and do not produce a literature survey, status report, or bibliography expansion. Work directly on the mathematics.

The task is complete only when a rigorous proof or rigorous disproof of the canonical target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and plans are research material, not completion. Consult an external source only when an active proof step requires the exact hypotheses of a named theorem, then return to the proof.

## Definitions and canonical target

For each sufficiently large m, write m=binom(n,2)+t with 0<=t<n and let H_m be K_n plus one new vertex adjacent to t clique vertices. Determine whether every graph G with m edges and no isolated vertices satisfies R(G)<=R(H_m); more generally determine the maximizers of R(G) at fixed m.

## Frozen mathematical background

- Sudakov proved R(G)<=2^{O(sqrt(m))} for every m-edge graph without isolated vertices.
- The proposed almost-complete maximizer fails for several small edge counts.

Audited sources for this background:

- [A conjecture of Erdős on graph Ramsey numbers](https://arxiv.org/abs/1002.0095) — peer_reviewed.
- [Erdős Problem 545](https://www.erdosproblems.com/545) — database_record.

Do not assign any source a stronger evidential status than stated here.

## Exact unresolved core

证明 almost-complete 图从某个阈值起极大，或识别无限反例族并给出正确极值结构。

**Affirmative obligation.** Prove the revised eventual extremal statement and identify an explicit or effective threshold.

**Negative obligation.** Construct infinitely many m and m-edge graphs G with R(G)>R(H_m), or give a corrected extremal family.

Close this exact mathematical gap. Rechecking database status, extending the bibliography, restating the gap, or proposing methods does not address it.

## Complete resolution criteria

A complete solution must discharge one of the two obligations above with all definitions and quantifiers exactly as stated. Every imported theorem must be stated with its full hypotheses and applied explicitly. Every new lemma must have a complete proof. A disproof must include a counterexample or infinite family with a self-contained certificate of every required property.

## What does not count as a solution

- Reproving only the bound 2^{O(sqrt(m))}.
- Ignoring the recorded small counterexamples.
- Comparing only orders or clique numbers instead of Ramsey numbers.
- A literature survey, open-status assessment, source catalogue, or research plan.
- A proof sketch, computation, or intermediate lemma presented as completion.
- A voluntary `CHECKPOINT_NOT_FINAL` while execution resources remain available.

## Required correctness checks

1. Keep the edge count exactly m.
2. Exclude isolated vertices consistently.
3. Do not assume Ramsey number is monotone under degree sequence majorization.
4. Verify that the final theorem is logically identical to the canonical target.
5. Distinguish finite evidence from universal proof and theorem from conjecture.
6. Record the exact statement, version, and applicability of every external theorem used.

## Required research package

Create a coherent, self-contained research package. Choose a directory layout suited to the mathematics, while preserving enough structure that another researcher can trace every final claim to its proof, source, computation, and adversarial check.

### Mandatory paper: `paper.tex`

Produce a journal-style mathematical paper containing a title and abstract; the canonical problem and all definitions; only the frozen background actually used; a precise statement of every claimed contribution; complete proofs of every lemma and main theorem or counterexample; a comparison between frozen background and newly established results; an accurate final resolution statement; and complete citations for every external result used.

All references must be included in `paper.tex` or an included `references.bib`. The paper must contain no placeholders, omitted proof steps, or claims supported only by separate notes.

### Mandatory final audit: `audit.md`

Produce an independent adversarial audit of `paper.tex`. Check exact agreement with the canonical target; every quantifier, boundary, and equality case; the dependency chain of each nontrivial lemma; circularity and hidden assumptions; applicability of external theorems; the exact force of any computation; citation support; and whether each asserted new result is genuinely beyond the frozen background.

The audit must end with exactly one verdict:

- `COMPLETE_SOLUTION_VERIFIED`;
- `COMPLETE_DISPROOF_VERIFIED`; or
- `CHECKPOINT_NOT_FINAL`.

Only the first two count as completion.

### Intermediate research archive

Reasonably archive proof drafts, proved and refuted lemmas, dependency notes, adversarial reviews, failed routes with exact failure points, computation code, exact certificates, test outputs, and the current research state. The final paper may not depend on an unarchived argument or calculation.

### LaTeX and PDF check

Compile `paper.tex` successfully and retain `paper.pdf`. All citations and cross-references must resolve and there must be no fatal LaTeX error. Successful compilation and an openable PDF are sufficient: do not perform page-by-page screenshot inspection, do not create visual-validation images, and do not add images, figures, diagrams, or a graphical abstract.

## Dynamic Multiagent constraints

Choose mathematical approaches, delegation, coordination, and changes of direction autonomously. Do not impose fixed roles, named stages, prescribed proof methods, or a predetermined sequence. Including the root agent, use at most four concurrent agents.

The following are prohibited:

- assigning any agent to investigate whether the problem is open or to conduct a general literature survey;
- allowing source management, status tracking, or process documentation to consume the main effort;
- substituting a plan or list of approaches for mathematical derivation;
- duplicating the same route without a concrete adversarial purpose;
- recording conjectures or proof sketches as proved lemmas;
- starting computation without a precise claim, hypotheses, finite scope, certificate format, and stopping condition;
- running more than one computation-focused task concurrently;
- using finite computation or numerical evidence as a substitute for universal proof;
- declaring completion without independent adversarial checking of the actual proof;
- voluntarily stopping because the problem is difficult, initial routes failed, or only intermediate results were obtained.

## Persistence and external-interruption behavior

Continue mathematical research while execution resources remain available. Do not end merely because several approaches fail, a paper draft exists, or the remaining gap has been identified. Autonomously repair, combine, replace, or abandon approaches as the mathematics requires.

Use `CHECKPOINT_NOT_FINAL` only when an external runtime, context, or system boundary forces interruption. On forced interruption preserve `paper.tex`, `audit.md`, verified results, unresolved obligations, failed routes, computations, certificates, and a clear resumable state. Never convert interruption into a solution claim.
