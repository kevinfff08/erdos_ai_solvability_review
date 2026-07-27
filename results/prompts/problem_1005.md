# Erdős Problem 1005: similarly ordered Farey fractions

## Definitions and canonical target

For each integer \(n\ge 4\), let
\[
F_n=(a_1/b_1,\ldots,a_{N_n}/b_{N_n})
\]
be the Farey sequence of order \(n\): all reduced fractions \(a/b\in[0,1]\) with \(0\le a\le b\le n\) and \(\gcd(a,b)=1\), listed in strictly increasing order, including \(0/1\) and \(1/1\). Two reduced fractions \(a/b\) and \(c/d\) are *similarly ordered* if
\[
(a-c)(b-d)\ge 0.
\]
Define \(f(n)\) as the largest integer \(m\ge0\) for which every pair
\[
1\le k<l\le N_n,\qquad l-k\le m,
\]
has \(a_k/b_k\) and \(a_l/b_l\) similarly ordered.

Primary target: determine whether there is a constant \(c>0\) such that
\[
f(n)=(c+o(1))n,
\]
equivalently whether \(f(n)/n\) converges to a positive limit as \(n\to\infty\) through all integers.

A stronger current conjecture is
\[
f(n)=\lfloor n/4\rfloor+d_n\quad(n\ge92),
\]
where \(d_n=1,2,2,4\) for \(n\equiv0,1,2,3\pmod4\), respectively.

## Accepted background

- Erdős proved that \(f(n)\gg n\) in 1943: [Erdős, *A Note on Farey Series*](https://www.renyi.hu/~p_erdos/1943-01.pdf). This is a theorem, not the requested asymptotic.
- Wouter van Doorn's publicly available 2025 arXiv v1 proves
  \[
  f(n)\ge\frac n{12}(1-4n^{-1/3})
  \]
  and, for every \(n\ge4\),
  \[
  f(n)\le\lfloor n/4\rfloor+d_n.
  \]
  See [arXiv:2509.00121](https://arxiv.org/abs/2509.00121) and its [HTML full text](https://arxiv.org/html/2509.00121v1). These are the strongest verified results located in this audit.
- The same preprint **conjectures**, but does not prove, equality in the latter formula for every \(n\ge92\); its finite calculation through \(n\le5000\) is evidence only.
- The standard consecutive-Farey criterion is available for use: two reduced fractions \(a/b<c/d\) are consecutive in \(F_n\) iff \(bc-ad=1\) and \(\max(b,d)\le n<b+d\).

Treat the 2025 result as a preprint: verify any imported lemma against the actual text and do not describe its conjecture as a theorem.

## Complete resolutions

An affirmative resolution of the primary target is a rigorous proof of \(\lim_{n\to\infty}f(n)/n=c>0\), with the value of \(c\) identified. A proof of the displayed exact formula for every \(n\ge92\) is a stronger complete resolution and gives \(c=1/4\).

A negative resolution is a rigorous proof that \(f(n)/n\) has no limit, for example by proving a strict separation between its liminf and limsup. A negative resolution of the stronger conjecture is a rigorously certified counterexample \(n\ge92\), including the exact relevant Farey indices and a verification of the resulting value or of the failed universal condition.

## What does not count as a solution

- Checking finitely many values, regardless of range.
- Reproving either known linear bound without closing the asymptotic question.
- Establishing a limit only on a subsequence.
- Finding a non-similarly-ordered pair but mishandling the fact that distance \(d\) implies \(f(n)\le d-1\).
- Heuristic density arguments, floating-point evidence, or a proposed recurrence without proof that it controls every valid pair \((k,l)\).
- Claiming the exact formula solely because it matches data or the upper-bound construction.

## Required correctness checks

1. State whether every fraction includes \(0/1\) and \(1/1\), and use reduced numerator-denominator representatives throughout.
2. For every global claim, quantify over all \(1\le k<l\le N_n\), not merely adjacent fractions or one local window.
3. Keep \((a_l-a_k)(b_l-b_k)\ge0\) distinct from its strict negation; audit all equality cases.
4. Audit every conversion between a bad-pair distance and a bound on \(f(n)\) for an off-by-one error.
5. If proving the sharp formula, separately audit the four classes modulo \(4\), the threshold \(92\), and every finite exceptional range needed by the proof.
6. If using an asymptotic \(o(1)\), give its quantifier order and demonstrate that it holds over all sufficiently large integers, not a density-one set.
7. Every citation must link to the primary paper or arXiv record and distinguish theorem, conjecture, and computation.

## Required deliverables

- A concise status memo listing all sources consulted and whether each is peer-reviewed or a preprint.
- A self-contained proof manuscript or disproof certificate, with a lemma dependency graph.
- A separate adversarial audit that checks definitions, endpoint conventions, residue cases, strictness, and every use of a Farey-neighbour criterion.
- If incomplete, a precise gap statement: the strongest proved lemma, its hypotheses, why it does not close the target, and the next falsifiable subclaim.
- If any computation is used, source code/pseudocode, exact-arithmetic certificate format, the lemma it tests, its input range, and its stopping condition.

## Dynamic Multiagent v2 protocol

Create one research root responsible for the canonical definitions, source ledger, approach registry, and final integration. Run at most four concurrent agents total, including the root if it is doing research work.

Begin with an independence wave: agents must register a distinct proposed route or a distinct adversarial task before seeing other agents' detailed derivations. The registry records: claim, exact hypotheses, expected bottleneck, dependencies, evidence status, and whether the route is proof, disproof, verification, or optional computation. Do not assign a fixed mathematical method; permit incompatible approaches to coexist.

Use multiple waves. After each wave, the root removes duplicate routes, promotes only lemmas with explicit proofs, and reuses freed slots for the most informative unresolved dependency. Every nontrivial proof is assigned an adversarial checker who did not author it. The checker must attempt counterexamples, quantifier failures, residue-class failures, and off-by-one errors before the lemma can enter the shared ledger.

Allocate proof work first. At most one optional computational subtask may run at a time, and only after declaring: (i) the exact lemma or candidate counterexample family being tested, (ii) all hypotheses, (iii) exact-arithmetic certificate output, and (iv) a finite stopping condition. Immediately reassign that slot once the stated question is answered; computation must never become an open-ended search or substitute for proof.

## Persistence and resumability

Maintain `research_state.md` at each wave boundary. It must contain the canonical statement, source links and status, approach registry, accepted lemmas with proofs or exact locations, rejected claims and counterexamples, open dependencies, and the next highest-priority task.

If execution ends before a complete proof or certified disproof, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`, preserve all verification notes, and report only the verified partial state. Do not convert an interrupted investigation, finite computation, or promising heuristic into a solution claim.
