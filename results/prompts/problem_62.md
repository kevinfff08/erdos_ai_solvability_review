# Erdős Problem 62: common 4-chromatic subgraphs

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work in ZFC. A graph is simple, undirected, and loopless. Its chromatic number \(\chi(G)\) is the least cardinality of a proper vertex colouring. A graph \(H\) is a subgraph of \(G\) when there is an injective map \(e:V(H)\to V(G)\) taking every edge of \(H\) to an edge of \(G\); this is **not** induced-subgraph containment.

Canonical weak target:

\[
\forall G_1,G_2\;[\chi(G_1)=\chi(G_2)=\aleph_1\Rightarrow
\exists H\;(\chi(H)=4\ \land\ H\hookrightarrow G_1\ \land\ H\hookrightarrow G_2)].
\]

The graph \(H\) may depend on the pair and may be finite or infinite. Do not replace \(\chi(G_i)=\aleph_1\) by a different cardinal hypothesis.

A separately labelled stronger target replaces \(\chi(H)=4\) by \(\chi(H)=\aleph_0\). Do not conflate the two. The extension from two graphs to an arbitrary finite family is also separately stronger and is not an automatic iteration.

## Frozen mathematical background

The following are accepted only with their stated scope.

- **Theorem (Erdős–Hajnal–Shelah, 1974):** every graph with \(\chi(G)>\aleph_0\) contains all sufficiently long odd cycles. Therefore every pair of \(\aleph_1\)-chromatic graphs has a common 3-chromatic subgraph. This does not produce a 4-chromatic one. Source: [Erdős–Hajnal–Shelah (1974)](https://www.renyi.hu/~p_erdos/1974-17.pdf).
- **Known finite-spectrum facts:** Komjáth–Shelah report the Erdős–Hajnal classification of fixed finite graphs unavoidable in every uncountably chromatic graph, and develop consistency constructions with delayed finite high-chromatic witnesses. Source: [Komjáth–Shelah (2005)](https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.20060).
- **Theorem (Lambie-Hanson, 2020):** for every \(f:\mathbb N\to\mathbb N\), there is a \(\chi=\aleph_1\) graph in which every subgraph with fewer than \(f(k)\) vertices has chromatic number below \(k\). Hence there is no uniform bound on the size of a finite 4-chromatic witness across all such graphs. This is an obstacle, not a disproof of the pair-dependent target. Source: [published paper](https://doi.org/10.1016/j.aim.2020.107176) and [preprint](https://arxiv.org/abs/1902.08177).
- **Restricted theorem, not a solution:** for stable graphs of chromatic number greater than \(\beth_2(\aleph_0)\), Halevi–Kaplan–Shelah prove a version of strong Taylor's conjecture. It does not apply to arbitrary \(\chi=\aleph_1\) graphs. Source: [JEMS paper](https://ems.press/journals/jems/articles/11115712).
- The historical formulation is recorded at [Erdős Problems 62](https://www.erdosproblems.com/latex/62) and independently in [the UCSD archive](https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/FourChromaticSubgraph.html). These are problem records, not proofs.

No cited source above proves or refutes the canonical 4-chromatic pair target.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** A complete affirmative resolution is a ZFC proof that for every pair of simple graphs G_1,G_2 with chi(G_1)=chi(G_2)=aleph_1, one can construct or prove the existence of one graph H with chi(H)=4 and embeddings H -> G_1 and H -> G_2. A separate proof is required for the stronger chi(H)=aleph_0 version.

**Negative obligation.** A complete negative resolution is a ZFC construction of a pair G_1,G_2 with chi(G_1)=chi(G_2)=aleph_1 together with a proof that no graph H of chromatic number 4 embeds as a non-induced subgraph into both. A model-specific pair alone establishes at most a relative-consistency result unless the intended conclusion is explicitly an independence theorem and both sides are proved.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution must give a ZFC proof of the canonical quantified statement and verify both embeddings and \(\chi(H)=4\).

A negative resolution must give, in ZFC, explicit graphs \(G_1,G_2\) with \(\chi(G_1)=\chi(G_2)=\aleph_1\), and prove that every graph embedding into both has chromatic number different from 4. A result in a forcing extension or under \(\diamondsuit\), CH, or another extra axiom is not a ZFC disproof; it may instead be part of a rigorously stated independence resolution if the complementary consistency result is also established.

The \(\chi(H)=\aleph_0\) and finite-family variants require their own complete-resolution statements and proofs.

## What does not count as a solution

- A common odd cycle, or any common 3-chromatic graph.
- Separate 4-chromatic subgraphs in \(G_1\) and \(G_2\) without an isomorphism type occurring in both.
- A common homomorphic image, minor, quotient, or induced-subgraph statement unless it is converted into the required non-induced embeddings.
- A proof only for stable graphs, a named construction class, or a larger chromatic threshold.
- A result that silently changes \(\chi=\aleph_1\) to \(\chi>\aleph_0\), or conversely.
- A model-specific forcing construction presented as a theorem of ZFC.
- Finite enumeration with no theorem reducing the universal infinite problem to that enumeration.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State every use of choice, forcing, diamond, CH, or cardinal-arithmetic assumption.
2. Audit the exact quantifier order: \(H\) may depend on the pair, but not separately on an embedding claim that yields different graphs \(H\).
3. Prove \(\chi(H)=4\) exactly. A lower bound \(\chi(H)\ge4\) and a separate colouring bound must be justified.
4. Check that both maps are injective edge-preserving embeddings; do not require or assume preservation of nonedges.
5. Check that each proposed counterexample has chromatic number exactly \(\aleph_1\), not merely an unverified uncountable or large chromatic number.
6. If using the EHS odd-cycle theorem, retain its graph-dependent threshold and explain why any attempted 4-chromatic analogue follows.
7. Before accepting any claimed solution, run an adversarial proof audit aimed at hidden cardinal changes, induced/non-induced confusion, and a switch from relative consistency to ZFC.

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
