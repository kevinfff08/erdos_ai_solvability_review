# Erdős Problem 14 — audited revised target

## Definitions and canonical target

Work in the positive integers \(\mathbb N=\{1,2,\ldots\}\).  For \(A\subseteq\mathbb N\) and \(n\in\mathbb N\), define the **unordered, repetition-allowed** representation function
\[
r_A(n)=\#\{(a,b)\in A^2:a\le b,\ a+b=n\}.
\]
Set
\[
B_A=\{n\in\mathbb N:r_A(n)=1\},\qquad
U_A(N)=|[1,N]\setminus B_A|.
\]
Thus \(U_A(N)\) counts both missing sums (\(r_A(n)=0\)) and sums with at least two unordered representations (\(r_A(n)\ge2\)).

Investigate the following two independent targets, and keep their statuses separate.

- **Q1:** For every \(A\subseteq\mathbb N\) and every \(\varepsilon>0\), prove or disprove that there are \(c=c(A,\varepsilon)>0\) and \(N_0=N_0(A,\varepsilon)\) such that \(U_A(N)\ge cN^{1/2-\varepsilon}\) for every \(N\ge N_0\).
- **Q2:** Prove or disprove the existence of one \(A\subseteq\mathbb N\) with \(U_A(N)=o(\sqrt N)\).

Before substantive work, record whether the problem owner instead intends Q1 with constants uniform in \(A\). Do not silently change between these variants.

## Accepted background

- The current Erdős Problems record states Q1/Q2 and reports an Erdős construction with \(U_A(N)\ll_\varepsilon N^{1/2+\varepsilon}\), plus a lower estimate along infinitely many \(N\). Treat these as historical claims requiring source verification before using their detailed parameters: <https://www.erdosproblems.com/history/14>.
- Erdős and Freud, *On sums of a Sidon-sequence*, J. Number Theory 38(2) (1991), 196–205, DOI: <https://doi.org/10.1016/0022-314X(91)90083-N>, is the primary finite-Sidon reference. The current database reports a finite \(2^{3/2}\sqrt N\) construction, but verify the original theorem before invoking that constant.
- O'Bryant's annotated bibliography describes the finite Sidon/quasi-Sidon context: <https://www.combinatorics.org/ojs/index.php/eljc/article/download/DS11/pdf/>.
- A 2026 LeanGenius artifact fixes the \(a\le b\) convention and formalizes elementary definitions, but lists the main historical estimates as axioms; it is not a formal solution: <https://leangenius.org/proof/erdos-14-unique-sums>.

Do not infer \(\neg\mathrm{Q2}\) from Q1. A function such as \(\sqrt N/\log N\) illustrates why a lower bound \(\gg_\varepsilon N^{1/2-\varepsilon}\) for every fixed \(\varepsilon\) is compatible with \(o(\sqrt N)\).

## Complete resolutions

A complete resolution must identify which question it resolves.

- A **yes** to Q1 is a proof with the exact quantifiers \(\forall A\,\forall\varepsilon\,\exists c,N_0\,\forall N\ge N_0\).
- A **no** to Q1 is an explicit \(A\) and \(\varepsilon>0\) for which no eventual positive lower constant exists.
- A **yes** to Q2 is one explicit infinite \(A\), with a proof that \(U_A(N)/\sqrt N\to0\) for all sufficiently large \(N\), not merely on a subsequence.
- A **no** to Q2 is a universal theorem excluding \(U_A(N)=o(\sqrt N)\) for every \(A\).

## What does not count as a solution

- Treating ordered pairs \((a,b)\) and \((b,a)\) as distinct representations.
- Counting only multiply represented sums and omitting missing sums.
- A finite set \(A_N\) chosen separately for each \(N\).
- An \(N^{1/2+\varepsilon}\) upper bound, an infinite-subsequence lower bound, or numerical data alone.
- A proof of Q1 claimed to settle Q2 without a genuine \(\Omega(\sqrt N)\)-type consequence.
- A citation to a database, forum, search snippet, or an axiomatized formal file in place of a proof.

## Required correctness checks

1. State the representation convention before every use of a representation count; include the diagonal \(a=b\).
2. Audit the dependence of every \(O\), \(o\), \(\ll\), \(\gg\), threshold, and construction parameter on \(A\), \(\varepsilon\), and scale.
3. Separate the counts \(r_A(n)=0\), \(r_A(n)=1\), and \(r_A(n)\ge2\) before applying a counting argument.
4. For an infinite construction, prove compatibility of all stages and control all large \(N\), including gaps between construction scales.
5. For a lower bound, test sparse, dense, periodic, Sidon, and finite-prefix perturbation regimes.
6. Independently verify every imported historical theorem from the primary paper or an equally authoritative accessible source.

## Required deliverables

- A `research_state.md` containing the exact target variant, source log, definitions, active lemmas, failed routes, and unresolved proof obligations.
- A source table distinguishing peer-reviewed papers, preprints, databases, formal artifacts, and informal discussion; include direct URLs and access dates.
- A proof dossier for each claimed lemma: statement, hypotheses, proof, dependency graph, and adversarial check.
- A final status report separately labeling Q1 and Q2 as proved, disproved, or unresolved.
- If a resolution is claimed, provide a compact proof outline and a line-by-line audit of all asymptotic and quantifier transitions.

## Dynamic Multiagent v2 protocol

Create a research root with an approach registry. Use at most four concurrent agents. Begin with independent approaches rather than fixed roles: agents may inspect source verification, seek lower-bound mechanisms, analyze infinite-construction mechanisms, or adversarially test a proposed lemma.

For every approach, register: target (Q1/Q2), precise convention, claimed lemma, dependencies, falsification tests, current evidence, and status. Reuse slots dynamically: when an approach reaches a proved lemma, counterexample, blocked dependency, or completed source audit, immediately assign the freed slot to the most informative unresolved branch. Run multiple waves, with each later wave informed by the registry rather than duplicating completed work.

Every nontrivial proof claim must receive an adversarial check by an agent not responsible for deriving it. The checker must test quantifier order, diagonal representations, missing-versus-multiple sums, all-scale control, and hidden use of a finite set depending on \(N\). A rejected proof returns to the registry with the first invalid inference and a minimal counterexample or missing hypothesis.

Allocate resources proof-first. At most one optional computational subtask may run at a time. Before it runs, declare in the registry: the exact lemma or counterexample question, its finite hypotheses, the certificate to retain, and a stopping condition. End and reassign that slot immediately when the question is answered; computation may not stand in for an asymptotic proof.

## Persistence and resumability

Update `research_state.md` after each wave and before any handoff. It must identify the active canonical variant, citations checked versus merely reported, proof dependencies, counterexamples tested, and next smallest proof obligation.

If a runtime boundary arrives before a complete proof or disproof, do not imply progress equals resolution. Save the current registry and return exactly `CHECKPOINT_NOT_FINAL`, with the next verification action and any unclosed mathematical gap.
