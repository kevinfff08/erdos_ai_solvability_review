# Erdős Problem 124 — repaired BEGL high-power target

## Definitions and canonical target

Do **not** work from the literal supplied condition \(\sum_{i=1}^r1/(d_r-1)\ge1\). For strictly increasing integers \(3\le d_1<\cdots<d_r\), it has no instances: \(d_r\ge r+2\), so its left side is at most \(r/(r+1)<1\).

Fix a finite set \(A=\{d_1,\ldots,d_r\}\) of distinct integers \(d_i\ge3\). For \(d\ge1\), \(k\ge0\), define
\[
P(d,k)=\left\{\sum_{j\in F}d^j:F\subseteq\{k,k+1,\ldots\}\text{ finite}\right\},
\]
where the empty sum is \(0\).

The target is the repaired Burr--Erdős--Graham--Li conjecture:
\[
\sum_{i=1}^r\frac1{d_i-1}\ge1,\qquad\gcd(d_1,\ldots,d_r)=1
\]
imply that for every fixed \(k\ge1\) there exists \(N=N(A,k)\) such that every integer \(n\ge N\) lies in
\[
P(d_1,k)+\cdots+P(d_r,k).
\]
Equivalently, \(n=\sum_i c_i a_i\) with \(c_i\in\{0,1\}\), \(a_i\in P(d_i,k)\); if \(0\in P(d_i,k)\) is retained, the \(c_i\) are redundant. The finite exponent sets may depend on \(n\), but \(A,k\) are fixed before \(N\).

## Accepted background

- BEGL96 is the primary source: Burr, Erdős, Graham, and Li, *Complete sequences of sets of integer powers*, Acta Arith. 77 (1996), 133--138, https://matwbn.icm.edu.pl/ksiazki/aa/aa77/aa7722.pdf . It defines \(\operatorname{Pow}(A;s)\) using exponents \(\ge s\ge1\), states the repaired conjecture, and supplies several non-general sufficient conditions.
- BEGL96 records that the finite-family reciprocal condition is necessary when it fails, via Diophantine approximation, and that gcd one is immediately necessary. These are necessary conditions, not a proof of sufficiency.
- BEGL96 explicitly reports that the largest omission for \(\operatorname{Pow}(\{3,4,7\};1)\) is 581. Before using an all-\(k\) \(\{3,4,7\}\) special case, inspect the primary proof or clearly label it as a database-reported result.
- The k=0 version allowing \(1\) is a different, solved statement; the current record and its forum explain the distinction: https://www.erdosproblems.com/124 and https://www.erdosproblems.com/forum/thread/124?order=oldest . Do not infer the target from that solution.
- Melfi's infinite-base construction is outside scope: https://www.rivmat.unipr.it/fulltext/2004-3s/pdf/16.pdf . The target requires finite \(A\).

Every imported result must be labeled theorem, conjecture, observation, or computational evidence, with an inspected direct source link.

## Complete resolutions

An affirmative resolution proves the displayed statement for every finite admissible \(A\), every \(k\ge1\), and every integer beyond a valid \(N(A,k)\).

A negative resolution gives one explicit finite admissible \(A\) and \(k\ge1\), plus a rigorous proof that arbitrarily large integers do not belong to \(\sum_{d\in A}P(d,k)\).

## What does not count as a solution

- Declaring victory from the supplied d_r-only condition: that merely finds the transcription's empty parameter domain.
- Reproving the k=0 theorem, allowing \(d_i^0=1\), or using any exponent below k.
- Proving only a special tuple, k=1, strict reciprocal inequality, an infinite base family, or a base set depending on n.
- Checking any finite interval without a proved finite-to-infinite tail argument.
- Establishing density, an average representation count, or selected residue classes instead of every sufficiently large integer.
- Treating a search snippet, forum assertion, or `sorry`-containing formal statement as a proof.

## Required correctness checks

1. Establish from BEGL96 that the reciprocal condition is \(\sum_i1/(d_i-1)\ge1\), and preserve the audit record of the d_r typo.
2. Check finiteness, distinctness, \(d_i\ge3\), gcd one, and the exact quantifier order in every claimed theorem.
3. Audit every carry, scaling, and residue adjustment: it must not create an exponent \(<k\) or repeat an exponent within a base expansion.
4. For an affirmative route, identify exactly why all n beyond N are covered, including equality cases of the reciprocal sum.
5. For a negative route, prove the omission is unbounded and recheck all hypotheses for the proposed tuple.
6. Independently verify any cited Lean artifact: source imports, theorem statement, absence of `sorry`, and successful typecheck.

## Required deliverables

Produce:

1. a source ledger with stable URLs, access dates, publication status, and exact theorem/lemma/page locations;
2. a statement-repair note proving why the literal d_r condition is empty and documenting the repaired target;
3. an approach registry listing assumptions, dependencies, falsification tests, status, and evidence for every route;
4. either a complete proof/disproof, or a precisely bounded partial result whose first unproved lemma is explicit;
5. an adversarial proof audit covering quantifiers, boundary cases, finiteness, carries, tail coverage, and source scope;
6. for any computation, code/pseudocode, inputs, an exact lemma or obstruction it tests, a stopping condition, and a proof of any finite-to-infinite implication.

## Dynamic Multiagent v2 protocol

Create a research root containing `research_state.md` and an append-only approach registry. Use at most four concurrent agents, including the coordinator. In the first wave, independently verify the primary statement/history, extract the strongest usable theorem boundary, and test a logically independent obstruction or structural route. Do not impose a fixed mathematical method or permanent role assignment.

Before an agent relies on a claim, it must register the exact statement, hypotheses, source/proof location, dependencies, and a falsification check. Keep approaches independent until evidence warrants combination. Use a later wave for adversarial checking of the leading route; duplicate work is permitted only when explicitly designated as verification.

Reassign slots dynamically when a question is answered, refuted, or has low evidence value. Use multiple waves rather than static assignments. Proof work has priority. At most one optional computational subtask may run at once, and only after it records: the exact lemma/invariant sought, tuple/k/modulus hypotheses, expected finite certificate, and a stopping condition. Release that slot immediately once the question is answered.

## Persistence and resumability

Update `research_state.md` after each material transition with the repaired canonical statement, source ledger, verified facts, rejected paths, approach registry, active tasks, first unresolved lemma, and next falsification test.

If a runtime boundary interrupts incomplete work, write the complete checkpoint, mark the report `CHECKPOINT_NOT_FINAL`, state that no resolution has been established, and identify the first unresolved proof obligation. On resumption, audit this checkpoint before starting further work.
