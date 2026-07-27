# Erdős Problem 87: statement repair before research

## Definitions and canonical target

All graphs are finite and simple. For a graph H, let R(H) be the least N such that every red/blue colouring of E(K_N) contains a monochromatic, non-induced copy of H. Write R(k)=R(K_k), and let χ(G) be the chromatic number.

The page currently asks whether, for every ε>0 and all sufficiently large k,

\[
R(G)>(1-\epsilon)^kR(k)
\]

for every G with χ(G)=k. Taken literally, this is **false**: set ε=2, let k be any even positive integer, and take G=K_k. Then the asserted strict inequality is R(k)>R(k).

Do not treat this as an open problem. First determine, from the original source or an authoritative correction, whether the intended first target is

\[
0<\epsilon<1,\qquad \forall\epsilon\ \exists k_0(\epsilon)\ \forall k\ge k_0(\epsilon)\ \forall G\,[\chi(G)=k\Rightarrow R(G)>(1-\epsilon)^kR(k)].
\]

The page also states an independent stronger target:

\[
\exists c>0\ \exists k_0\ \forall k\ge k_0\ \forall G\,[\chi(G)=k\Rightarrow R(G)>cR(k)].
\]

The threshold in the repaired first target may depend on ε, but never on G. In the stronger target c and k_0 are absolute.

## Accepted background

- The current [Problem 87 discussion page](https://www.erdosproblems.com/forum/thread/87) still labels the record Open but also explicitly says this reflects only the website owner's knowledge. It writes ε>0, not 0<ε<1.
- The literal counterexample above is a complete direct deduction from the displayed formula; it requires no external theorem.
- Erdős's historical claim R(G)≥R(k) is false. Faudree and McKay proved r(W_6)=17<18=r(K_4); see the peer-reviewed [1993 article](https://combinatorialpress.com/jcmcc-articles/volume-013/a-conjecture-of-erdes-the-ramsey-number-rw_6/). This bounded-k example does not settle either repaired asymptotic target.
- The page attributes an r(G)≫2^{k/2} random-colouring lower bound to Yuval Wigderson. Before relying on it, locate a citable proof or reproduce it with exact hypotheses and uniform constants.
- Do not confuse ordinary R(G) with the different host-chromatic parameter R_χ(G) studied by [Axenovich, Gaa, and Liu](https://arxiv.org/abs/2409.07535).

## Complete resolutions

The literal first question is resolved negatively by ε=2, G=K_k, and arbitrarily large even k.

A complete statement-repair outcome is either:

1. authoritative confirmation that the intended domain is 0<ε<1, together with an exact corrected statement and source; or
2. confirmation that the literal wording is intentional, in which case record the problem as disproved and do not invent a repaired conjecture.

Only after outcome 1 is verified may research address the repaired target. A proof must establish its stated quantifiers uniformly over every finite simple k-chromatic graph. A disproof must give a fixed ε∈(0,1), infinitely many k_i→∞, and graphs G_i with χ(G_i)=k_i and rigorously certified inequalities R(G_i)≤(1−ε)^{k_i}R(k_i). The constant-factor target needs its own proof or a family with R(G_i)/R(k_i)→0.

## What does not count as a solution

- Silently changing ε>0 to 0<ε<1.
- Calling the W_6 example a disproof of an eventual repaired statement.
- Treating a website Open label or an unsuccessful search as proof of openness.
- Proving a claim only for a selected graph family without a reduction from all k-chromatic graphs.
- Using R(G)≫2^{k/2} without comparing it in the required direction with the actual R(k).
- Confusing R_χ(G), off-diagonal, induced, multicolour, or vertex-deletion Ramsey numbers with R(G).

## Required correctness checks

1. Verify the ε-domain from an authoritative source before any repaired-target work.
2. For the literal counterexample, check ε=2, k even, χ(K_k)=k, R(K_k)=R(k), and the strict inequality.
3. Keep the ordinary two-colour diagonal Ramsey convention throughout.
4. Audit every asymptotic quantifier: k_0(ε) must be independent of G, and c,k_0 in the stronger target must be absolute.
5. For any counterexample family, certify both chromatic number and the Ramsey-number comparison.
6. Require an adversarial proof audit to test sign changes in (1−ε)^k, strictness, and accidental substitution of χ(G)≤k or ω(G)=k.

## Required deliverables

1. A source log with exact queries, access dates, direct links, and publication-status labels.
2. A one-page statement audit that separates the literal disproof, the historical W_6 counterexample, and any confirmed repaired target.
3. A source-backed decision: `literal_disproved_no_repair` or `repair_confirmed_0<epsilon<1`, with quoted or precisely located supporting evidence.
4. If repair is confirmed, a theorem ledger separating proved facts, conjectures, deductions, and unverified claims, followed by either a complete resolution or a sharply delimited partial-progress report.
5. A line-by-line adversarial check of every claimed proof and a bibliography of direct stable links.

## Dynamic Multiagent v2 protocol

Create a research root and an approach registry. The registry must record each approach's exact target, dependencies, evidence, status, and retirement reason. Use at most four concurrent agents total.

First wave: independently verify the original Erdős source and current page history; audit the literal counterexample; and search current literature for direct solutions of the repaired and constant-factor targets. Do not begin mathematical solution work on a repaired target until the statement-repair decision is recorded.

Use multiple waves and dynamically reuse slots when an audit question is decided. Every claimed source interpretation, lemma, or complete resolution receives an adversarial checking pass by an agent not responsible for its initial derivation. The checker must test ε-domain, quantifier order, strictness, Ramsey convention, and dependence on G.

Allocate resources proof-first. At most one optional computational subtask may run at once. Before it starts, register the exact lemma/hypothesis, input family, certificate sought, and a finite stopping condition. Reassign that slot immediately once the stated question is answered.

## Persistence and resumability

Maintain `research_state.md` in the research root. At each checkpoint record the literal statement, counterexample, authoritative-source status, source ledger, approach registry, proved lemmas, rejected claims, and next falsifiable tasks.

If execution ends before the statement-repair decision or a complete repaired-target investigation, put `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`. State exactly whether the blocker is source confirmation, a mathematical gap, or a proof-audit failure; never describe the repaired target as resolved without the required evidence.
