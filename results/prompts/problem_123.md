## Definitions and canonical target

Audit the literal statement presently displayed for Erdős Problem #123, not an silently repaired variant. For pairwise coprime integers \(a,b,c\ge 1\), put
\[
S(a,b,c)=\{a^k b^l c^m:k,l,m\in\mathbb Z_{\ge0}\}.
\]
It asserts that for every such triple there is \(N\) such that every integer \(n\ge N\) is a sum of a finite set \(F\subseteq S(a,b,c)\) of distinct numerical terms, with no two distinct selected terms dividing one another.

The required task is to verify the proposed disproof of this literal statement using \((a,b,c)=(1,5,7)\). Also document, separately, whether the intended repaired target is the statement with \(a,b,c>1\). Do not attempt to solve that repaired target unless a new task explicitly authorizes it.

## Accepted background

- Erdős–Lewin, [d-Complete Sequences of Integers](https://www.brand.site.co.il/riddles/201507a_files/2153618.pdf), Mathematics of Computation 65 (1996), 837–840, proves the two-base classification: for positive integers \(p,q\), \(\{p^\alpha q^\beta\}\) is d-complete iff \(\{p,q\}=\{2,3\}\). Independently verify the exact theorem and its hypotheses from the paper.
- The current [Erdős Problems page](https://www.erdosproblems.com/123) displays \(a,b,c\ge1\) and labels the record open; the [forum thread](https://www.erdosproblems.com/forum/thread/123?order=oldest) flags the lower-bound typo.
- Chen–Yu, [On d-complete sequences of integers, II](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/207/2/115065/on-d-complete-sequences-of-integers-ii), Acta Arithmetica 207 (2023), proves substantial cases for bases greater than one, but does not by itself prove the universal repaired target.
- The [FormalConjectures record](https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB123%C2%BB/) uses \(a,b,c>1\), but contains `sorry`; it is not an accepted formal proof.

Keep theorem statements, conjectures, database labels, and forum claims explicitly separate.

## Complete resolutions

A complete verification of the literal disproof must provide all of the following:

1. Parse the displayed quantifiers and prove that \((1,5,7)\) satisfies them.
2. Prove exactly, as sets of numerical integers, \(S(1,5,7)=\{5^l7^m:l,m\ge0\}\).
3. Quote with theorem/page-level precision, or independently reproduce, the Erdős–Lewin two-base classification and verify that its definition of d-complete matches the target definition.
4. Deduce that \(S(1,5,7)\) is not d-complete, hence that the literal universal proposition is false. State the logical consequence correctly: for every proposed threshold there is a larger nonrepresentable integer.
5. Give a separate repair memo: evidence for \(a,b,c>1\) as the intended restriction, and an explicit statement that this does not settle the repaired target.

The decisive contrary audit outcome is an authoritative source showing that the operative problem already imposed \(a,b,c>1\), or a failure of the cited two-base theorem to cover \(p=5,q=7\) under the same definition. If either occurs, stop the disproof conclusion and reopen the status audit for the repaired statement.

## What does not count as a solution

- A finite search for missing representations.
- A missing small integer only.
- A claim that pairwise coprime integers are automatically greater than one.
- Replacing \(\ge1\) by \(>1\) without a documented erratum or repair decision.
- A proof for a finite family of triples, a modulo-\(l\) result, or the snug \((2,3,5)\) variant.
- A `sorry`-containing Lean declaration or a database label as proof.
- A conclusion about the repaired target based solely on the literal counterexample.

## Required correctness checks

- Check that 1 is coprime to 5 and 7 and that 5 and 7 are coprime.
- Check that duplicate exponent descriptions caused by \(1^k\) do not create additional numerical summands.
- Check that “distinct” and “no summand divides another” are conditions on selected terms.
- Verify every direction of the reduction from three displayed bases to the two-base set.
- Verify that non-d-completeness means unbounded failures, not a finite initial failure.
- Inspect the cited original theorem rather than relying only on a modern abstract or search snippet.
- Label the website/forum/formalization conflict and the Ma–Chen 5-versus-3 background transcription inconsistency; do not use either as an unverified theorem statement.

## Required deliverables

Deliver `audit_report.md` containing: the formalized literal proposition; a short proof of the reduction \(S(1,5,7)=\{5^l7^m\}\); a precise cited theorem extract; the resulting proof/disproof verdict; and a repair-status memo.

Deliver `source_log.md` with stable URLs, access dates, publication status, exact claims supported, and page/theorem locations for the primary paper. Deliver a minimal machine-readable `verdict.json` stating separately `literal_status`, `intended_repair_status`, and whether any Lean artifact is sorry-free. Cite primary sources directly; label all secondary or informal sources as such.

## Dynamic Multiagent v2 protocol

Create a research root and maintain an approach registry before substantive convergence. Use at most four concurrent agents. In the first wave, pursue independently: source-theorem verification, literal-logic/set-reduction verification, and statement-history/formalization audit. Do not assign permanent roles or prescribe a mathematical method; dynamically choose later work from the registry.

After each wave, record claim, evidence, dependencies, counterarguments, and status in the registry. Require an adversarial proof check by an agent that did not originate the argument. Reuse a freed slot immediately for the highest-risk unresolved claim, source inspection, or contradiction check. Run multiple waves until the decisive proof path and all credible contrary paths have been checked.

Use proof-first allocation. Default to zero computation. At most one optional computational subtask may be opened only after declaring its precise lemma, hypotheses, expected certificate, and stopping condition in `research_state.md`; no finite computation can certify non-d-completeness here, so terminate that slot immediately if it cannot contribute to a cited symbolic reduction.

## Persistence and resumability

Maintain `research_state.md` after every material source inspection and wave. It must contain the canonical literal statement, the repair candidate, source URLs, exact verified theorem locations, approach registry, completed checks, unresolved risks, and next actions.

If a runtime boundary occurs before direct inspection of the Erdős–Lewin theorem or before adversarial checking is complete, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md` and in the interim report. Do not present a final mathematical verdict until the checkpoint record establishes the full reduction and source verification.
