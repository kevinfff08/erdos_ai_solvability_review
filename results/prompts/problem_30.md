# Erdős Problem 30 — research prompt

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

For each positive integer \(N\), write \([N]=\{1,\ldots,N\}\). A set \(A\subseteq[N]\) is a Sidon set (equivalently a \(B_2\)-set here) when
\[
a+b=c+d\quad(a,b,c,d\in A)\implies\{a,b\}=\{c,d\}
\]
as unordered pairs. In particular, sums with repeated terms such as \(a+a\) are included.

Define
\[
h(N)=\max\{|A|:A\subseteq[N]\text{ is a Sidon set}\}.
\]

Prove or disprove the following exact asymptotic assertion:
\[
\forall\epsilon>0\ \exists C_\epsilon\ge0\ \exists N_\epsilon\ \forall N\in\mathbb N,\ N\ge N_\epsilon:\quad
|h(N)-\sqrt N|\le C_\epsilon N^\epsilon.
\]

Use this interval \(B_2\) definition throughout. Do not substitute the harmonic-analysis meaning of “Sidon set,” a weak-Sidon convention, a modular-only statement, or an infinitely-often statement.

## Frozen mathematical background

The following are accepted only to the scope explicitly stated in their sources.

- Erdős Problems currently records this as open: <https://www.erdosproblems.com/30>.
- Classical Singer constructions establish the \((1-o(1))\sqrt N\) main-term lower-bound phenomenon; this does not give the required error term for every \(N\).
- Carter, Hunter, and O'Bryant proved, in a peer-reviewed 2025 paper,
  \[
  h(N)\le\sqrt N+0.98183N^{1/4}+O(1).
  \]
  Source: <https://link.springer.com/article/10.1007/s10474-024-01499-8>.
- Hou and Zhao's unrefereed July 2026 preprint claims the stronger
  \[
  h(N)\le\sqrt N+0.9435N^{1/4}+O(1),
  \]
  with an exact rational finite certificate for a component of the proof. This is useful background, not a resolution: <https://arxiv.org/abs/2607.01169>.
- A 2026 Lean 4 preprint reports formalized Singer/Sidon infrastructure and a conditional reduction, not a proof of this target: <https://arxiv.org/abs/2605.03274>.
- Earlier upper-bound advances include Balogh--Füredi--Roy, <https://arxiv.org/abs/2103.15850>, and O'Bryant, <https://arxiv.org/abs/2207.07800>.

Clearly label every other input as either a proved theorem with a source, a conjecture/assumption, or a proposed lemma. In particular, do not silently assume a subpolynomial prime-gap statement.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete affirmative resolution proves that for every ε>0 there are C_ε,N_ε such that every integer N≥N_ε satisfies |h(N)-√N|≤C_εN^ε, using the B_2 definition stated above and with no unproved analytic hypotheses.

**Negative obligation.** A complete negative resolution proves that there exists ε_0>0 such that h(N)-√N is not O(N^{ε_0}); equivalently, for every C,N_0 there is N≥N_0 with |h(N)-√N|>CN^{ε_0} (or provides an explicit unbounded witnessing sequence).

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a self-contained proof of the displayed quantified estimate, including both signs of the error, for all sufficiently large integers \(N\), without unproved hypotheses.

A negative resolution is a proof that there is an \(\epsilon_0>0\) for which the displayed estimate fails: equivalently, for every \(C,N_0\) some \(N\ge N_0\) obeys \(|h(N)-\sqrt N|>CN^{\epsilon_0}\). A concrete sequence witnessing this divergence is acceptable if rigorously proved.

## What does not count as a solution

- Any improvement only to the coefficient of \(N^{1/4}\).
- A bound for one fixed \(\epsilon\), a subsequence, or infinitely many \(N\).
- Only an upper bound or only a lower bound.
- A conditional implication from a prime-gap conjecture, RH, or an assumed Sidon-set estimate.
- Exhaustive computation below a cutoff without a theorem covering all larger \(N\).
- A result for a changed Sidon convention, a cyclic group, or a shifted interval without an explicit, valid transfer to the canonical target.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State the Sidon predicate and verify it includes repeated sums.
2. Audit every asymptotic quantifier: constants and thresholds may depend on \(\epsilon\), never on \(N\).
3. If using a diameter formulation, prove the exact conversion to \(h(N)\), including shifts, floors, ceilings, and endpoint offsets.
4. Identify separately the theorem establishing each lower-bound construction and the theorem transferring it to every required interval length.
5. For a computational certificate, prove the bridge from the finite certificate to the claimed asymptotic theorem; rerun an exact-arithmetic verifier where available and record the version/hash.
6. Subject every candidate proof to an adversarial check for an unproved distributional hypothesis, an “infinitely many”/“all sufficiently large” swap, and an accidental fixed-exponent argument.

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
