# Erdős Problem 41: infinite B_3 sequences

## Definitions and canonical target

Let \(\mathbb N_{>0}=\{1,2,\ldots\}\).  For \(A\subseteq\mathbb N_{>0}\), write
\[
A(N)=|A\cap\{1,\ldots,N\}|.
\]

Call \(A\) a \(B_3\) set if for every two sorted triples
\[
a_1\le a_2\le a_3,\qquad b_1\le b_2\le b_3,\qquad a_i,b_i\in A,
\]
we have
\[
a_1+a_2+a_3=b_1+b_2+b_3 \implies (a_1,a_2,a_3)=(b_1,b_2,b_3).
\]
Equivalently, each integer has at most one representation as a sum of three members of \(A\), up to permutation. Repetitions are allowed: \(a+a+b\) and \(3a\) are legitimate representations.

Canonical target: prove that every infinite \(B_3\) set \(A\subseteq\mathbb N_{>0}\) satisfies
\[
\liminf_{N\to\infty}\frac{A(N)}{N^{1/3}}=0.
\]
Equivalently, for each such \(A\) there are integers \(N_j\to\infty\) with \(A(N_j)=o(N_j^{1/3})\).

## Accepted background

- The current Erdős Problems record classifies this target as open and reports no claimed partial or complete solution in its discussion thread: [problem page](https://www.erdosproblems.com/41) and [thread](https://www.erdosproblems.com/forum/thread/41). This is a database assessment, not a proof that no later paper exists.
- The \(h=2\) Sidon-set analogue is reported there as proved by Erdős.
- For every even order \(h=2k\), the analogue is proved in Martin Helm, [On \(B_{2k}\)-sequences (1993)](https://eudml.org/doc/206528). This theorem does not include \(h=3\).
- Martin Helm, [On the distribution of \(B_3\)-sequences (1996)](https://www.sciencedirect.com/science/article/pii/S0022314X96900694), proves that no \(B_3\) sequence can satisfy \(A(N)\sim\alpha N^{1/3}\) for fixed \(\alpha>0\), and gives further necessary conditions. Treat this as a theorem, but inspect the full paper before relying on any condition beyond this verified abstract-level statement. The target above remains a conjecture because positive liminf does not force such an asymptotic.
- Ethan Patrick White, [An optimal \(L^2\) autoconvolution inequality (2024)](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/an-optimal-l2-autoconvolution-inequality/8D109D51F271CC78EBDA2C99FB35612D), improves finite \(B_3[1]\) extremal constants. It is relevant background but is not a resolution of the infinite liminf target.
- The existing [Lean file for #41](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/41.lean) uses cardinality-three `Finset`s and therefore omits repeated summands; do not use it as a formalization of the canonical target without repairing the definition.

Separate all proved facts from conjectures and from deductions made during the investigation. Cite a primary paper or a formal artifact for every imported theorem.

## Complete resolutions

An affirmative resolution is a complete proof, for every infinite repeated-summand \(B_3\) set \(A\), that \(\liminf_{N\to\infty}A(N)/N^{1/3}=0\).

A negative resolution is an explicit infinite \(A\subseteq\mathbb N_{>0}\) with a full proof of the repeated-summand \(B_3\) property and a proof that
\[
\liminf_{N\to\infty}A(N)/N^{1/3}>0.
\]

## What does not count as a solution

- Ruling out only \(A(N)\sim\alpha N^{1/3}\), which is Helm's known partial result.
- A finite \(B_3\) construction, a numerical optimization, or finite bounds for \(R_3(N)\) without a theorem about one fixed infinite set.
- A result about \(\limsup\), upper density, average density, or a logarithmically weakened bound that does not imply the required liminf conclusion.
- Invoking an even-order theorem without proving a valid reduction for order three.
- Verifying only uniqueness for three distinct summands, or relying on the current incomplete Lean encoding.
- A claimed construction whose cross-block three-sum collisions have not been proved absent.

## Required correctness checks

1. State and use the multiplicity-aware \(B_3\) condition exactly. Every collision check must include \(a+a+b\), \(3a\), and all other repeated-summand triples.
2. Normalize triples before comparing them, or work with multisets; permutations are trivial coincidences and only permutations.
3. Audit every asymptotic quantifier. A proof of the affirmative target needs arbitrarily large scales with ratio tending to zero; a disproof needs one fixed infinite set and a uniform eventual positive lower bound in the liminf sense.
4. For each imported result, provide a direct source link, exact theorem/lemma number or page, its hypotheses, and a short explanation of why they apply.
5. If a finite-to-infinite passage is proposed, prove nesting or cross-scale compatibility explicitly. Do not infer it from a sequence of unrelated finite extremizers.
6. If formalization is used, first prove that the encoding permits repeated summands and is equivalent to the sorted-triple definition above. No `sorry`, unchecked axiom, or distinct-elements-only substitute may certify the target.
7. Subject every claimed proof or counterexample to an adversarial independent audit focused on the six preceding checks.

## Required deliverables

- A concise research report distinguishing theorem, conjecture, deduction, failed approach, and open gap.
- A complete proof manuscript or complete counterexample certificate, if a resolution is claimed.
- A dependency ledger listing each nontrivial lemma, its status, and exact dependencies.
- A literature update with URLs, authors, year, publication status, and a note explaining what each source actually proves.
- For any computational work, reproducible code, exact inputs, certificates, and a proof that computation answers its stated lemma rather than merely suggesting a pattern.
- A proof-audit report that explicitly checks repeated summands, permutation conventions, liminf quantifiers, and all finite-to-infinite transitions.
- If unresolved, a precise residual lemma or obstruction and a `CHECKPOINT_NOT_FINAL` state rather than a solution claim.

## Dynamic Multiagent v2 protocol

Use a research root with at most four concurrently active agents. Begin with independently chosen approaches rather than a fixed division of mathematical labor. Maintain an approach registry in the research root; each entry must record the target reformulation, claimed leverage, dependencies, current evidence, failure mode, and whether it has received adversarial checking.

Work in multiple waves. In the first wave, explore incompatible proof directions and audit the exact literature/definition boundary. In later waves, allocate slots dynamically to the most promising unresolved lemmas, counterexample stress tests, source verification, or adversarial proof checking. Reuse a slot immediately when its assigned question has a decisive answer; do not leave agents on obsolete branches. Do not assign agents permanently by role or prescribe a single mathematical method.

Every nontrivial claimed lemma must receive an adversarial review by an agent that did not originate it. The reviewer must attempt counterexamples, inspect all quantifiers, and identify any hidden use of distinct summands or of a limsup statement. Register negative results and failed reductions to prevent duplicate work.

Use proof-first allocation. At most one optional computational subtask may run at a time. Before it starts, the registry must declare: the exact lemma or counterexample-search proposition, finite hypotheses, certificate format, and a stopping condition whose answer changes the proof plan. When that condition is met, terminate or repurpose the computation slot immediately; numerical evidence alone cannot be elevated to a proof.

## Persistence and resumability

Maintain `research_state.md` in the research root. At each material checkpoint record the canonical definition, sources checked, approach registry, lemma dependency graph, proof fragments, failed attempts, outstanding verification, and the next smallest decisive task.

If a runtime boundary interrupts an incomplete investigation, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md` and in the final handoff. Preserve enough detail that a later wave can resume without redoing searches or silently changing the repeated-summand convention. Do not report a resolution until the complete-resolution conditions and the independent correctness audit have both been satisfied.
