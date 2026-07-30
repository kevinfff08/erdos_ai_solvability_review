# Erdős Problem 17: cluster primes

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

A prime $p>2$ is a **cluster prime** if, for every positive even integer $n$ satisfying $2\le n\le p-3$, there exist primes $q_1,q_2\le p$ such that $n=q_1-q_2$. The choices of $q_1,q_2$ may depend on $n$.

Prove or disprove that cluster primes are infinite. Formally, resolve exactly one of the following:

- Positive: for every real $B$, there is a cluster prime $p>B$.
- Negative: there is a real $B$ such that no prime $p>B$ is a cluster prime.

Use the positive-even convention above. Do not use the ambiguous phrase “every even number” without this lower bound. The convention $p>2$ is part of the definition.

## Frozen mathematical background

- Blecksmith, Erdős, and Selfridge, [*Cluster Primes* (1999)](https://www.tandfonline.com/doi/abs/10.1080/00029890.1999.12005005), proved that if $C(x)$ counts cluster primes at most $x$, then $C(x)\ll_A x/(\log x)^A$ for every fixed $A>0$. This is a theorem, not a finiteness result.
- Elsholtz, [*On cluster primes* (2003)](https://www.math.tugraz.at/~elsholtz/WWW/papers/papers13clusteractarith.pdf), proves that for every fixed $0<c<1/8$, $C(x)=O_c\bigl(x\exp(-c(\log\log x)^2)\bigr)$. It uses upper-bound sieve arguments and explicitly states that the infinitude question is open.
- [OEIS A038133](https://oeis.org/A038133) is the sequence of odd **non**-cluster primes. The cluster-prime sequence is [OEIS A038134](https://oeis.org/A038134). Do not propagate the database page's reversed OEIS annotation.
- The [FormalConjectures entry](https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB17%C2%BB/) contains `sorry`; it is a statement formalization, not a verified proof of this problem or its cited bounds.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that for every real B there exists a prime p>B such that, for every positive even integer n with 2<=n<=p-3, there are primes q1,q2<=p satisfying q1-q2=n.

**Negative obligation.** Prove that there exists a bound B such that every prime p>B fails the cluster-prime condition; explicitly, for each such p exhibit or prove the existence of a positive even n<=p-3 for which no pair of primes q1,q2<=p has q1-q2=n.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a rigorous unconditional proof of arbitrarily large primes $p$ satisfying every required difference condition simultaneously.

A negative resolution is a rigorous unconditional proof of an eventual obstruction: a bound $B$ and a proof that every prime $p>B$ has at least one positive even $n\le p-3$ absent from the difference set of primes at most $p$.

Any result conditional on an unproved hypothesis must be labeled conditional and does not resolve the target unless the task is explicitly changed.

## What does not count as a solution

- Checking finitely many primes or extending the numerical range.
- Reproving either known upper bound, improving its constants, or proving any upper bound compatible with $C(x)\to\infty$.
- Showing only that cluster primes have density zero, their reciprocal sum converges, or many primes fail the property.
- Showing infinitely many bounded prime gaps or any fixed finite prime pattern.
- A heuristic, random model, claimed asymptotic without proof, or an argument that covers only most required even differences.
- A proof whose witness pairs exceed $p$, use non-primes, omit a boundary value, or vary $p$ while covering different differences.
- A formal declaration with `sorry`, unchecked axioms, or nonmatching quantifiers.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State the quantifiers before each main claim and preserve the order: choose $p$, then require all admissible $n$, then choose $q_1,q_2$.
2. Verify $n$ is positive, even, and includes the endpoint $p-3$ when applicable.
3. Verify $q_1,q_2$ are both primes and both at most $p$.
4. Distinguish a necessary condition from a sufficient condition; in particular, bounded prime gaps do not imply the cluster-prime property.
5. For an upper-bound lemma, state precisely what is fixed and how every implied constant depends on parameters.
6. For a negative proof, audit the universal “every sufficiently large prime” step; infinitely many failures are insufficient.
7. For an affirmative proof, audit simultaneous coverage of all differences for each produced $p$.
8. Independently adversarially check every imported theorem against a primary source and every formal claim for `sorry` or extra axioms.

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
