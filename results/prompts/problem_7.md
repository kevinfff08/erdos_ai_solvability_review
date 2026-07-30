# Erdős Problem 7: odd distinct covering systems

## Primary mathematical objective

**Task mode: mathematical proof research**

The statement and status audit was completed on 2026-07-27. Treat the canonical target and frozen background below as settled inputs to this run. Do not investigate whether the problem is open, and do not produce a general literature survey or status report.

The canonical target stated below is the sole target for this run. Work directly on its mathematics. The task is complete only when a rigorous proof or rigorous disproof of that target has been produced and independently audited. Intermediate lemmas, computations, failed approaches, and checkpoints are research material, not completion.

Inspect an external source only if an active proof step requires the exact hypotheses of a named theorem. Keep such inspection local to that proof obligation and return immediately to mathematical work.

## Definitions and canonical target

A **covering system** is a finite nonempty family of congruences
\[
 a_i \pmod {n_i}\qquad (i=1,\ldots,k)
\]
with integers \(n_i>1\), such that for every \(x\in\mathbb Z\), at least one \(i\) satisfies \(x\equiv a_i\pmod {n_i}\). It is **distinct** when \(n_i\ne n_j\) for \(i\ne j\). It is an **odd distinct covering system** when every \(n_i\) is odd.

Canonical target: determine whether an odd distinct covering system exists.

Equivalent finite formulation for a proposed construction: set \(L=\operatorname{lcm}(n_1,\ldots,n_k)\). The family covers \(\mathbb Z\) if and only if it covers every residue class in \(\mathbb Z/L\mathbb Z\).

Boundary conventions are mandatory: the family must be finite; every modulus must exceed 1; moduli, not merely residue classes, must be pairwise distinct; no disjointness or exact-cover condition is assumed. If modulus 1 were allowed, \(0\pmod 1\) would make the question trivial, so it is excluded.

## Frozen mathematical background

- Hough and Nielsen proved that every distinct covering system has a modulus divisible by 2 or 3: [arXiv:1703.02133](https://arxiv.org/abs/1703.02133), published in *Duke Mathematical Journal* 168 (2019), 3261–3295. Thus an odd candidate must contain a modulus divisible by 3.
- Balister, Bollobás, Morris, Sahasrabudhe, and Tiba proved that a finite distinct covering with square-free moduli has an even modulus: [arXiv:1901.11465](https://arxiv.org/abs/1901.11465), *Algebra & Number Theory* 15 (2021), 609–626. This proves only the square-free strengthening, not the canonical target.
- Their sieve/probabilistic-measure framework and further progress are in [arXiv:1811.03547](https://arxiv.org/abs/1811.03547), *Inventiones Mathematicae* 228 (2022), 377–414; a later overview is Balister’s [2024 survey](https://doi.org/10.1017/9781009490559.003).
- A 2025 preprint / 2026 *Discrete Mathematics* paper studies a different variant in which one odd modulus may repeat and explicitly describes the original odd-covering problem as open: [arXiv:2507.16135](https://arxiv.org/abs/2507.16135).
- The elementary necessary condition \(\sigma(L)\ge2L\) for the LCM \(L\) is useful but not decisive; see the transparent discussion at [MathOverflow](https://mathoverflow.net/questions/74644/on-integer-covering-systems-with-all-moduli-distinct).

Treat the above as theorems only to the extent stated. In particular, do not infer the general result from the square-free theorem. A 2026 candidate Lean proof is not accepted: its source declares a key `HoughNielsenGoodFibre` as an axiom ([source](https://raw.githubusercontent.com/spicylemonade/erdos-007/main/main.lean)); the associated forum discussion records a separate failed sieve formalization ([thread](https://www.erdosproblems.com/forum/thread/7?order=newest)).

## Exact unresolved core

The frozen background does not establish either of the following resolution obligations.

**Affirmative obligation.** Exhibit a finite k, pairwise distinct odd integers n_i>1, and residues a_i, and prove that for every residue r modulo L=lcm(n_1,...,n_k), at least one congruence r≡a_i (mod n_i) holds. This finite verification is equivalent to coverage of all integers.

**Negative obligation.** Prove that every finite family of congruences with pairwise distinct odd moduli greater than 1 leaves at least one integer uncovered; equivalently, prove no object satisfying the canonical existential statement exists.

Close this exact gap. Rechecking the database status, extending the bibliography, or describing the gap again does not address it.

## Complete resolution criteria

An affirmative resolution must provide an explicit finite list \((a_i,n_i)\) satisfying all canonical conditions and a rigorous certificate that every class modulo \(L=\operatorname{lcm}(n_i)\) is covered.

A negative resolution must prove that every finite family with pairwise distinct odd \(n_i>1\) has an uncovered integer. The proof may use established theorems, but every reduction must preserve finiteness, coverage, distinctness, and the full non-square-free range.

## What does not count as a solution

- Solving only square-free, primitive, antichain, bounded-prime, bounded-exponent, bounded-LCM, or bounded-cardinality cases.
- Establishing only necessary divisibility, density, reciprocal-sum, or abundance conditions.
- A numerical search without a theorem reducing all possible systems to the searched finite region.
- A repeated-modulus construction, a modulus-1 construction, an infinite covering, or a cover only of a finite interval or density-one set.
- A Lean/Coq/Isabelle artifact with `axiom`, `sorry`, `admit`, unverified external code, or a formal theorem not equivalent to the canonical target.

- A literature survey, open-status assessment, publication-status report, or source catalogue.
- A research plan, list of promising methods, or explanation of why the problem is difficult.
- An intermediate lemma, computation, proof sketch, or failed route presented as if it completed the canonical target.
- A voluntary `CHECKPOINT_NOT_FINAL` issued while execution resources remain available.

## Required correctness checks

1. State all quantifiers and prove that every modulus is an odd integer greater than 1 and that all moduli are pairwise distinct.
2. For an affirmative construction, verify coverage of **all** residues modulo the exact LCM. Supply machine-readable residue data or a short symbolic partition argument.
3. For a negative proof, identify every place where square-freeness, bounded exponents, minimality, irredundancy, or a divisibility-antichain condition might have been introduced; prove it is justified or remove it.
4. Audit all uses of Hough–Nielsen and BBMST results against their original statements. Do not substitute a qualitative theorem for a required quantitative sieve bound.
5. For every numerical inequality, give rational/interval bounds, rounding direction, parameter domains, source code, and a reproducible command. A computation is admissible only after its precise lemma, hypotheses, and finite stopping condition are written down.
6. Use adversarial checking: try to construct a small counterexample to each new reduction and independently rederive its key implication.

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
