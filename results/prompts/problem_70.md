# Erdős Problem 70: audit-driven research task

## Definitions and canonical target

Work in ZFC. Let \(\mathfrak c=2^{\aleph_0}\), identified with the initial ordinal of that cardinality. For an ordinal \(\kappa\), \([\kappa]^3\) is the set of unordered three-element subsets of \(\kappa\). For a coloring \(d:[\mathfrak c]^3\to\{0,1\}\), write
\[
\mathfrak c\to(\beta,n)^3_2
\]
when every such \(d\) has either:

1. a color-0 homogeneous set \(A\subseteq\mathfrak c\) with inherited ordinal order type \(\operatorname{otp}(A)=\beta\), or
2. a color-1 homogeneous set \(B\subseteq\mathfrak c\) with \(|B|=n\).

Canonical target: prove or refute in ZFC that \(\mathfrak c\to(\beta,n)^3_2\) for every countable ordinal \(\beta<\omega_1\) and every finite \(n\ge2\).

The cases \(n=2\) and \(n=3\) are trivial for triple colorings. Substantive work begins at \(n=4\). Do not replace \(\mathfrak c\), the initial ordinal, by the ordinary ordered real line unless an explicitly proved reduction justifies it.

## Accepted background

- Erdős and Rado introduced the partition calculus in [A Partition Calculus in Set Theory (1956)](https://www.renyi.hu/~p_erdos/1956-02.pdf). Their real-order theorem gives the historical \(\omega+m\), finite-4 level; a modern accessible statement and proof discussion is in [Jones (2000)](https://doi.org/10.37236/1502). This is a theorem, not the desired all-countable-ordinal result.
- Milner and Prikry proved in ZFC that \(\omega_1\to(\omega\cdot2+1,4)^3\), using a forcing model and absoluteness; see [their 1991 paper](https://doi.org/10.1016/0012-365X(91)90336-Z). This is a theorem.
- Jones proved \(\omega_1\to(\omega+m,n)^3\) for all finite \(m,n\); see [Jones (2007)](https://doi.org/10.1090/S0002-9939-06-08538-8). This is a theorem.
- Jones proved \(\omega_1\to(\omega\cdot2+1,n)^3\) for every finite \(n\); see [Jones (2018)](https://doi.org/10.1090/proc/13503). This is the strongest directly verified result in this audit.
- Since \(\omega_1\le\mathfrak c\), restriction of a coloring proves the left-monotonic implication \(\omega_1\to(\beta,n)^3_2\Rightarrow\mathfrak c\to(\beta,n)^3_2\). Hence the 2018 theorem settles the canonical target for \(\beta\le\omega\cdot2+1\).
- The general assertion is still treated as open by the current [Erdős Problems entry](https://www.erdosproblems.com/70). A 2025 expert discussion also describes the stronger \(\omega_1\)-version as a conjecture, but that forum source is not a proof: [MathOverflow](https://mathoverflow.net/questions/448855/are-infinite-ramsey-numbers-completely-known/488725).

## Complete resolutions

An affirmative resolution requires a complete ZFC proof of the canonical target for every countable \(\beta\) and every finite \(n\ge2\), explicitly covering the presently unverified range beyond \(\omega\cdot2+1\) for \(n\ge4\).

A negative resolution requires a specific countable \(\beta\), a finite \(n\ge4\), and a ZFC-defined coloring \(d:[\mathfrak c]^3\to2\) for which neither stipulated homogeneous alternative exists, with a proof of both failures.

An independence resolution is complete only if it precisely concerns the canonical initial-ordinal statement and rigorously gives opposite models (or otherwise establishes the exact metamathematical status). A one-sided relative-consistency theorem is not, by itself, a resolution of the ZFC question.

## What does not count as a solution

- Reproving any case already covered by \(\beta\le\omega\cdot2+1\), or treating only \(n\le3\).
- A theorem about a real order, a separable linear order, an arbitrary set of reals, or a different ordering, without a proved transfer to the initial ordinal \(\mathfrak c\).
- A coloring of pairs, ordered triples rather than the intended unordered triples without an equivalence proof, a symmetric Ramsey relation, or a different color assignment.
- A result conditional on MA, CH, PFA, large cardinals, or another additional hypothesis unless it is converted into the claimed ZFC conclusion or used in a complete independence proof.
- Finite computation, random experiments, pattern matching, or a literature citation without reconstructing the exact theorem hypotheses and conclusion.

## Required correctness checks

1. State every arrow relation in expanded quantifier form before using it.
2. Distinguish the cardinal \(\mathfrak c\), its initial ordinal, and the usual linear order on \(\mathbb R\).
3. For a \(\beta\)-homogeneous set, verify exact inherited order type \(\beta\), not merely countable cardinality.
4. Verify the asymmetric color roles: color 0 produces \(\beta\), color 1 produces \(n\).
5. When using monotonicity, write the restriction/embedding map explicitly and preserve the relevant order type.
6. For any forcing argument, state the forcing extension, the formula being transferred, all parameters, and the absoluteness principle used.
7. Independently adversarial-check every purported counterexample against both alternatives.
8. Before declaring a new boundary case open or solved, inspect the relevant primary paper rather than relying on a survey snippet.

## Required deliverables

- `statement_audit.md`: exact formal statement, notation choices, and an explicit treatment of the \(\mathfrak c\)/real-order ambiguity.
- `literature_matrix.md`: one row per material source with theorem statement, hypotheses, proof status, direct relevance, and a stable URL/DOI.
- `known-results-map.md`: a dependency map from Erdős–Rado through Milner–Prikry and Jones, with separately proved monotonicity deductions to \(\mathfrak c\).
- `attempts.md`: every approach, lemma, proof attempt, failure point, and adversarial objection; retain failed attempts.
- `proof.md` only if a complete proof or counterexample is obtained; otherwise give a precise frontier report.
- `references.bib` or equivalent machine-readable bibliography. Every mathematical claim beyond elementary definitions must cite a primary source or be proved in the deliverable.

## Dynamic Multiagent v2 protocol

Create a research root and maintain an approach registry recording: identifier, exact target, assumptions, dependency on sources, current status, falsification test, and owner. Use at most four concurrent agents total, including any coordinator.

Start with independent first-wave investigations rather than a fixed division of one method: one may audit statement/source equivalence, another may reconstruct known proofs, another may investigate the next uncovered ordinal, and another may search for negative/independence mechanisms. These are roles for initial diversification, not permanent assignments; agents may choose incompatible proof strategies.

At each synchronization point:

1. merge only claims with a written proof or source-level evidence;
2. assign an adversarial agent to test every claimed lemma, transfer, or counterexample;
3. retire duplicated approaches and immediately reuse freed slots on the sharpest unresolved sublemma;
4. launch a new wave only after updating the registry and recording why the previous wave did or did not narrow the target.

Do not exceed four concurrent agents. Do not let literature search consume all slots once the bibliography is stabilized. Any computational slot is optional and there may be at most one: before it runs, register a single lemma/question, explicit hypotheses, an exact stopping condition, and the certificate format. Reassign that slot immediately after the question is answered. Computation may test finite encodings or check a formal certificate; it cannot substitute for the infinitary proof.

## Persistence and resumability

Maintain `research_state.md` after every material event. It must contain the canonical target, source ledger, approach registry, proved lemmas with dependencies, rejected claims, open obligations, and the exact next verification action.

If a runtime boundary occurs before a complete resolution, do not imply success. Save all evidence and end the state file with `CHECKPOINT_NOT_FINAL`, followed by the current strongest verified theorem, the unproved gap, and restart instructions. On resumption, first audit the state file and adversarial objections before beginning new work.
