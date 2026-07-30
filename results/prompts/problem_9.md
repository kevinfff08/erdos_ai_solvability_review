# Erdős Problem 9: positive upper density of exceptions to p+2^k+2^l

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

Let P be the positive primes. Define

A = { n in N : n is odd and there are no p in P and k,l in Z_{>=0} such that n = p + 2^k + 2^l }.

For X>=1, put A(X)=|A cap [1,X]| and

bar_d(A)=limsup_{X->infinity} A(X)/X.

Prove or disprove the canonical target bar_d(A)>0. Equivalently, prove or disprove that there are a constant c>0 and arbitrarily large X with A(X)>=cX. Density relative only to odd integers is equivalent for this yes/no question, but the denominator convention must be stated in every claim.

## Frozen mathematical background

- Crocker proved that infinitely many positive odd integers fail the historical positive-exponent version; see [Crocker, 1971](https://msp.org/pjm/1971/36-1/pjm-v36-n1-p09-p.pdf). This alone does not settle density or automatically cover k,l=0.
- Pan's peer-reviewed theorem treats the nonnegative-exponent setting and proves a sublinear-loss lower bound, hence A(X)>>_epsilon X^(1-epsilon) for each epsilon>0; see [Pan, 2011](https://www.impan.pl/shop/publication/transaction/download/product/83300).
- The most recent located work, [Ding--Sun--Zhao, arXiv:2607.05357 (2026)](https://arxiv.org/abs/2607.05357), improves the quantitative lower bound to, for every eta>0,
  A(X)>>_eta X exp(-(4+eta)(logloglog X/loglog X)log X).
  It is a preprint, not an accepted proof of positive density.
- Chen--Feng--Templier give useful conditional context involving prime powers and Fermat numbers, but not a resolution of the present prime problem; see [their 2008 paper](https://doi.org/10.4064/aa135-1-4).
- The database still lists the problem open; treat that label as a lead, not as proof: [Erdős Problems #9](https://www.erdosproblems.com/9). The associated sequence is [OEIS A006286](https://oeis.org/A006286).

Do not treat any heuristic, database label, forum statement, or unverified preprint claim as a theorem. Distinguish exact quoted theorems, transparent deductions, conjectures, and heuristics.

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Prove that there exists c>0 such that limsup_{X->infinity} A(X)/X >= c; equivalently, exhibit c>0 and arbitrarily large X with A(X)>=cX, with every excluded representation checked for all primes p and k,l>=0.

**Negative obligation.** Prove limsup_{X->infinity} A(X)/X=0, equivalently A(X)=o(X), by showing that for every epsilon>0 all sufficiently large X satisfy A(X)<=epsilon X.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution is a rigorous proof that some fixed c>0 satisfies limsup_{X->infinity} A(X)/X>=c.

A negative resolution is a rigorous proof that A(X)=o(X), equivalently limsup_{X->infinity} A(X)/X=0.

Either resolution must retain p prime, k,l>=0, n odd, and the ambient-density normalization above.

## What does not count as a solution

- Infinitude, a logarithmic lower bound, X^(1-epsilon), or X^(1-o(1)) lower bounds.
- A result only for positive exponents, distinct exponents, prime powers, a different base, or a coefficient-modified variant.
- A conditional implication unless it explicitly proves the stated target unconditionally.
- Numerical searches, finite density estimates, or a finite progression, however large.
- Showing a particular covering-system strategy cannot work; that is method-specific negative evidence, not a negative resolution.
- Showing positive density after restricting to a progression without a rigorous implication to the canonical A.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. Check p=2, k=0, l=0, and k=l separately wherever parity or congruences are used.
2. Every congruence argument that makes n-2^k-2^l divisible by q must handle the exceptional case n-2^k-2^l=q rather than calling it composite.
3. State whether all constants are absolute, depend on eta, or depend on X. A positive-density proof needs one fixed positive c.
4. Keep upper density distinct from lower/natural/logarithmic density and from relative density in a progression.
5. For every imported theorem, verify its exponent domain, prime versus prime-power domain, uniformity, and exceptional sets from the original source.
6. Audit every limiting step: an X-dependent modulus or a bound valid on only a sparse sequence does not automatically give positive upper density.

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
