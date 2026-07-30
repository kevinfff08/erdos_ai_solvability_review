# Erdős Problem 108 research task

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Work with finite simple graphs. For a graph X, chi(X) is its ordinary vertex chromatic number. Its girth is the length of a shortest cycle; define girth(X)=infinity when X is acyclic.

A subgraph H of G is ordinary, not necessarily induced: vertices and edges may both be deleted. Thus H must satisfy V(H) subseteq V(G) and E(H) subseteq E(G). This convention is essential.

For r>=4 define h_r(G)=max{chi(H): H is a subgraph of G and girth(H)>=r}. Prove or disprove the following canonical target:

For every integers r>=5 and k>=2, there exists F(k,r) such that every finite simple graph G with chi(G)>=F(k,r) has h_r(G)>=k.

The r=4 case is accepted background, so the task is the genuinely remaining r>=5 target. A disproof must fix one r>=5 and one k>=2 and provide graphs G_n with chi(G_n)->infinity but h_r(G_n)<k for every n.

## Frozen mathematical background

- Rödl, "On the chromatic number of subgraphs of a given graph," Proceedings of the American Mathematical Society 64(2), 370-371 (1977), DOI: https://doi.org/10.1090/S0002-9939-1977-0469806-4. Its clique-or-triangle-free theorem yields the r=4 case under the ordinary-subgraph convention.
- Pettie, Tardos, Walczak, "On a Clique Game and the Erdős-Hajnal Problem on High-Chromatic High-Girth Subgraphs," SODA 2026, pp. 2903-2927, DOI: https://doi.org/10.1137/1.9781611978971.108. This is a theorem, not a resolution: it gives a tower-type lower bound via Burling graphs for girth 5.
- Li, "The Erdős-Hajnal High-Girth Subgraph Conjecture Holds in the Polynomial Chromatic-Sparsity Regime," arXiv:2606.17901v1 (2026), https://arxiv.org/abs/2606.17901. This is an unrefereed preprint. Treat only its explicitly verified hypotheses and conclusions as provisional background: it claims the result under fixed bounds e(G)<=C chi(G)^P, not for all graphs.
- The FormalConjectures artifact formalizes a statement but contains sorry and is not a proof: https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB108%C2%BB/.

Do not confuse this problem with the unrelated induced-subgraph Erdős-Hajnal conjecture.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Give a complete proof that for every fixed pair of integers r>=5 and k>=2 there is F(k,r) such that every finite simple G with chi(G)>=F(k,r) has an ordinary subgraph H with girth(H)>=r and chi(H)>=k. The proof must be uniform over all finite G, including arbitrarily dense graphs.

**Negative obligation.** Give a complete counterexample to the quantified statement: exhibit fixed integers r>=5 and k>=2 and finite simple graphs G_n with chi(G_n)->infinity such that every ordinary subgraph H of every G_n with girth(H)>=r has chi(H)<k.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a rigorous proof of the canonical target for every r>=5 and k>=2, with a threshold depending only on (k,r), and with no unadvertised restriction on G.

A negative resolution is a rigorous construction and proof of fixed r>=5, fixed k>=2, and a finite graph family (G_n) with unbounded chromatic number and h_r(G_n)<k.

Either outcome must include a proof audit of all imported theorems and an explicit dependency ledger for every parameter.

## What does not count as a solution

- The r=4 theorem.
- A statement about induced subgraphs, or an argument that forbids edge deletion.
- A result only for sparse, bounded-degree, bounded-order, pseudorandom, Kneser, Burling, or any other special graph class.
- A result only for fractional, list, online, or approximate chromatic number.
- A proof with F depending on G, |V(G)|, e(G), an edge-density exponent, or a host-specific auxiliary object.
- Finding examples of high-girth high-chromatic graphs without embedding them as subgraphs of every high-chromatic host.
- Finite computation without a proved reduction and stopping condition that covers all finite graphs.
- Repeating an unverified claim from a preprint, talk, forum, or database entry.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State every quantifier in order and verify F=F(k,r) is independent of G.
2. At every extraction/deletion step, prove that the output is an ordinary subgraph of G.
3. Check girth exactly: for r=5, eliminate both C_3 and C_4.
4. Establish chi(H)>=k for ordinary chromatic number after all cycle-killing operations.
5. If using randomization, prove a positive-probability simultaneous event and extract a deterministic witness.
6. Separate finite and infinitary claims. Do not claim the stronger infinite-chromatic-subgraph version unless it is independently proved.
7. Audit each external theorem against its original source and state the exact version used.
8. For a proposed counterexample, verify h_r(G_n)<k over all ordinary subgraphs, not merely a chosen subclass.

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
