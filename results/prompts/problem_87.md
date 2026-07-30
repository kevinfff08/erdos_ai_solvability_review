# Erdős Problem 87: Ramsey numbers of high-chromatic graphs

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The revised target stated below is the sole target for this run. Do not reopen the repair decision or revert to a superseded literal formulation. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

All graphs are finite and simple. For a graph H, let R(H) be the least N such that every red/blue colouring of E(K_N) contains a monochromatic, non-induced copy of H. Write R(k)=R(K_k), and let χ(G) be the chromatic number.

The historical page asks whether, for every ε>0 and all sufficiently large k,

\[
R(G)>(1-\epsilon)^kR(k)
\]

for every G with χ(G)=k. Taken literally this is false for ε>1. For this research task, the audited repaired target is the following precise statement:

\[
0<\epsilon<1,\qquad \forall\epsilon\ \exists k_0(\epsilon)\ \forall k\ge k_0(\epsilon)\ \forall G\,[\chi(G)=k\Rightarrow R(G)>(1-\epsilon)^kR(k)].
\]

The record also states the stronger target:

\[
\exists c>0\ \exists k_0\ \forall k\ge k_0\ \forall G\,[\chi(G)=k\Rightarrow R(G)>cR(k)].
\]

The threshold in the first target may depend on ε, but never on G. In the stronger target \(c\) and \(k_0\) are absolute. Prove or disprove these repaired mathematical targets directly; do not reopen the wording repair.

## Frozen mathematical background

- The literal ε>0 formulation fails for ε=2 and \(G=K_k\); the canonical target in this prompt has already repaired the range to \(0<\epsilon<1\).
- Erdős's historical claim R(G)≥R(k) is false. Faudree and McKay proved r(W_6)=17<18=r(K_4); see the peer-reviewed [1993 article](https://combinatorialpress.com/jcmcc-articles/volume-013/a-conjecture-of-erdes-the-ramsey-number-rw_6/). This bounded-k example does not settle either repaired asymptotic target.
- A random-colouring argument is reported to give \(R(G)\gg2^{k/2}\). It may be used only after its exact hypotheses and uniform constants have been proved in the paper or obtained from a theorem whose assumptions are checked for the active proof step.
- Do not confuse ordinary R(G) with the different host-chromatic parameter R_χ(G) studied by [Axenovich, Gaa, and Liu](https://arxiv.org/abs/2409.07535).

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove the repaired assertion for every fixed \(0<\epsilon<1\), with \(k_0(\epsilon)\) uniform over every finite simple \(G\) satisfying \(\chi(G)=k\). A stronger affirmative resolution proves the absolute constant-factor target with \(c>0\) and \(k_0\) independent of \(G\) and \(k\).

**Negative obligation.** Give a fixed \(\epsilon\in(0,1)\), infinitely many \(k_i\to\infty\), and finite simple \(G_i\) with \(\chi(G_i)=k_i\) and \(R(G_i)\le(1-\epsilon)^{k_i}R(k_i)\), certified by rigorous Ramsey bounds. For the stronger target, give such a family with \(R(G_i)/R(k_i)\to0\).

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution must prove the repaired \(0<\epsilon<1\) assertion with all displayed quantifiers and uniformity over every finite simple \(k\)-chromatic graph. Proving the absolute constant-factor statement is a stronger complete resolution.

A negative resolution must give a fixed \(\epsilon\in(0,1)\), infinitely many \(k_i\to\infty\), and graphs \(G_i\) with \(\chi(G_i)=k_i\) and rigorously certified inequalities
\[
R(G_i)\le(1-\epsilon)^{k_i}R(k_i).
\]
To disprove the stronger constant-factor target, prove \(R(G_i)/R(k_i)\to0\) for an admissible family.

## What does not count as a solution

- Returning to the already-settled literal \(\epsilon>1\) counterexample instead of addressing the canonical repaired target.
- Calling the W_6 example a disproof of an eventual repaired statement.
- Treating a website Open label or an unsuccessful search as proof of openness.
- Proving a claim only for a selected graph family without a reduction from all k-chromatic graphs.
- Using R(G)≫2^{k/2} without comparing it in the required direction with the actual R(k).
- Confusing R_χ(G), off-diagonal, induced, multicolour, or vertex-deletion Ramsey numbers with R(G).

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Use the fixed canonical range \(0<\epsilon<1\) throughout; do not revert to the defective literal range.
2. For the literal counterexample, check ε=2, k even, χ(K_k)=k, R(K_k)=R(k), and the strict inequality.
3. Keep the ordinary two-colour diagonal Ramsey convention throughout.
4. Audit every asymptotic quantifier: k_0(ε) must be independent of G, and c,k_0 in the stronger target must be absolute.
5. For any counterexample family, certify both chromatic number and the Ramsey-number comparison.
6. Require an adversarial proof audit to test sign changes in (1−ε)^k, strictness, and accidental substitution of χ(G)≤k or ω(G)=k.

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
