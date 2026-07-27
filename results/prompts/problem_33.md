# Erdős Problem 33 — revised open target

## Definitions and canonical target

Let \(\mathbb N_0=\{0,1,2,\ldots\}\), \(\mathcal S=\{n^2:n\in\mathbb N_0\}\), and \(A\subseteq\mathbb N_0\).  Say that \(A\) is an additive complement of the squares if
\[
\exists X_0\in\mathbb N_0\ \forall m\in\mathbb N_0,\quad m\ge X_0\Rightarrow\exists a\in A\ \exists n\in\mathbb N_0:\ m=a+n^2.
\]
For real \(x\ge1\), write \(A(x)=|A\cap\{1,\ldots,\lfloor x\rfloor\}|\), and define
\[
 C_*:=\inf_{A}\ \limsup_{x\to\infty}\frac{A(x)}{\sqrt{x}},
\]
where the infimum ranges over all additive complements \(A\) of \(\mathcal S\).

Resolve the revised target: determine \(C_*\) exactly.  If asserting that there is a literal “smallest possible value,” separately prove that some admissible \(A\) attains the infimum.  The historical question \(\liminf A(x)/\sqrt{x}>1\) is already solved and is not the target of this investigation.

Finite modifications preserve both normalized limits.  Thus an eventual complement may be augmented by finitely many small elements to cover every nonnegative integer, but do not confuse this optimization-level equivalence with literal equivalence of the two predicates for a fixed set.

## Accepted background

The following are accepted only with the stated scope; recheck primary sources before relying on finer constants.

- Moser proved in 1965 that every additive complement satisfies \(\liminf A(x)/\sqrt{x}>1.06\).  See https://doi.org/10.1090/pspum/008/0175874.
- Cilleruelo (1993), Habsieger (1995), and Balasubramanian--Ramana (2001) independently give the stronger universal lower bound \(\liminf A(x)/\sqrt{x}\ge4/\pi\).  Relevant primary identifiers are https://doi.org/10.1006/jnth.1993.1049 and https://doi.org/10.1006/jnth.1995.1039; a published accessible historical summary is https://comptes-rendus.academie-sciences.fr/mathematique/item/CRMATH_2020__358_8_897_0/.
- Hence \(C_*\ge4/\pi\).
- The Erdős Problems record and its discussion thread report a construction by Wouter van Doorn with \(A(N)<2\varphi^{5/2}\sqrt N\) for all \(N\), hence \(C_*\le2\varphi^{5/2}\).  The proof is an informal GitHub PDF, not a peer-reviewed theorem: https://github.com/Woett/Mathematical-shorts/blob/main/The%20smallest%20set%20such%20that%20every%20positive%20integer%20is%20the%20sum%20of%20a%20square%20and%20an%20element%20from%20this%20set.pdf.  The current database record and forum are https://www.erdosproblems.com/33 and https://www.erdosproblems.com/forum/thread/33.
- Chen--Fang and later Ding et al. study representation functions and a distinct question of Ben Green.  Ding--Sun--Wang--Xia, Discrete Mathematics 349(2), 114763 (2026), DOI https://doi.org/10.1016/j.disc.2025.114763, proves a representation-excess result.  Ding's preprint https://arxiv.org/abs/2512.15407 rules out exact-on-average complements.  Neither result by itself determines \(C_*\).

Separate every theorem proved in a cited source from a conjecture, heuristic, forum claim, or consequence you derive.

## Complete resolutions

A complete affirmative resolution specifies a real constant \(C\) and proves \(C_*=C\):

1. for every \(\varepsilon>0\), construct an additive complement \(A_\varepsilon\) with \(\limsup A_\varepsilon(x)/\sqrt{x}\le C+\varepsilon\), or construct one attaining \(C\); and
2. prove \(\limsup A(x)/\sqrt{x}\ge C\) for every additive complement \(A\).

If the conclusion says that \(C\) is a minimum, include an admissible extremizer.  A negative resolution of a specific proposed value \(C\) must give either a valid complement with smaller limsup or a universal lower bound strictly larger than \(C\).  A proof of non-attainment resolves only the attainment subquestion.

## What does not count as a solution

- Reproving \(\liminf A(x)/\sqrt x\ge4/\pi\), or only answering the already-settled question \(\liminf>1\).
- A new upper construction or a new universal lower bound without matching the other side.
- A result solely about exact-on-average complements, representation multiplicities, or Ben Green's ordered \(w_n\) problem without a proved implication for \(C_*\).
- Finite verification, numerical optimization, or coverage through a bounded cutoff presented as proof of eventual coverage or a limsup statement.
- A formal declaration with `sorry`, `admit`, opaque axioms, or a changed eventual-coverage predicate without a proof that the intended optimization quantity is preserved.

## Required correctness checks

- State the eventual threshold and maintain the quantifier order for every construction and lower bound.
- Verify coverage for every sufficiently large integer, not merely a density-one set or a subsequence.
- Distinguish the number of elements of \(A\) from the number of square-plus-\(A\) representations.
- Check all endpoint and rounding conventions: \(0\in\mathcal S\), \(A(x)\) uses positive elements, and floor/ceiling errors are harmless only after proof.
- A construction bounded on selected scales must have a rigorous interpolation argument for all scales before it gives a limsup bound.
- A universal inequality must apply to arbitrary admissible infinite \(A\), with its threshold allowed to depend on \(A\).
- Audit every claimed bridge from representation-function estimates or ordered-element estimates to the limsup objective.
- Independently inspect the van Doorn construction before using it as a lemma; record whether its claimed strict all-\(N\) inequality is established.

## Required deliverables

1. A concise status report distinguishing the solved liminf question from the open \(C_*\) problem.
2. A definitions-and-quantifiers sheet and a list of every finite-modification step.
3. A source ledger with permanent URLs, theorem numbers/pages where available, publication status, and an explicit theorem/conjecture/inference label.
4. A proof manuscript or counterexample certificate for each new claim, with all constants and asymptotic dependencies tracked.
5. An adversarial proof-audit report listing failed approaches, gaps found, and repairs.
6. If formalization is attempted, a pinned build, a source scan for `sorry`/`admit`/new axioms, and a theorem statement faithful to the canonical target.

## Dynamic Multiagent v2 protocol

Use a research root that maintains an approach registry, evidence ledger, proof dependency graph, and `research_state.md`.  Run at most four agents concurrently.  In the first wave, agents must pursue independent lines of attack rather than divide one unexamined proof: for example, source/construction verification, universal lower-bound mechanisms, structure near a candidate constant, and adversarial auditing.  These are roles for early diversity, not fixed mathematical assignments.

At each merge point, register for every approach: precise target lemma, assumptions, claimed implication for \(C_*\), proof status, reusable artifacts, and a named falsification test.  A coordinator compares approaches, retires routes with a demonstrated obstruction, and dynamically reuses freed slots in later waves.  Every nontrivial proposed lemma receives an adversarial check by an agent that did not author it.  No claim advances merely because two agents repeat the same heuristic.

Allocate resources proof-first.  At most one optional computational subtask may run at any time.  Before it begins, declare the exact lemma or counterexample question, all hypotheses, the finite certificate format, and a stopping condition that makes success or failure informative.  Computation may test a construction invariant or find a finite obstruction; it may not be used as evidence for an eventual theorem.  Immediately reassign its slot when that narrowly stated question is answered.

Use multiple waves: first establish trustworthy background and candidate lemmas; then pursue incompatible proof routes; then audit the strongest surviving chain and attempt formal or independently checkable certification.  The protocol must remain free to change methods in light of evidence and must not impose a static assignment or a preferred mathematical technique.

## Persistence and resumability

After each material result, update `research_state.md` with the canonical target, source URLs, completed checks, exact open lemmas, failed routes, proof dependencies, active approach-registry entries, and the next falsifiable task.  Store enough detail for a new agent to reproduce each estimate without trusting chat history.

If a runtime boundary occurs before a complete resolution, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`, preserve all partial derivations and citations, state precisely what has and has not been verified, and resume from the highest-priority unresolved proof obligation.  Do not convert a checkpoint, numerical pattern, informal forum post, or inaccessible-paper summary into a final mathematical claim.
