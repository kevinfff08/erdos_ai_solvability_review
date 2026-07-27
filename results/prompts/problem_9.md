# Erdős Problem 9: positive upper density of exceptions to p+2^k+2^l

## Definitions and canonical target

Let P be the positive primes. Define

A = { n in N : n is odd and there are no p in P and k,l in Z_{>=0} such that n = p + 2^k + 2^l }.

For X>=1, put A(X)=|A cap [1,X]| and

bar_d(A)=limsup_{X->infinity} A(X)/X.

Prove or disprove the canonical target bar_d(A)>0. Equivalently, prove or disprove that there are a constant c>0 and arbitrarily large X with A(X)>=cX. Density relative only to odd integers is equivalent for this yes/no question, but the denominator convention must be stated in every claim.

## Accepted background

- Crocker proved that infinitely many positive odd integers fail the historical positive-exponent version; see [Crocker, 1971](https://msp.org/pjm/1971/36-1/pjm-v36-n1-p09-p.pdf). This alone does not settle density or automatically cover k,l=0.
- Pan's peer-reviewed theorem treats the nonnegative-exponent setting and proves a sublinear-loss lower bound, hence A(X)>>_epsilon X^(1-epsilon) for each epsilon>0; see [Pan, 2011](https://www.impan.pl/shop/publication/transaction/download/product/83300).
- The most recent located work, [Ding--Sun--Zhao, arXiv:2607.05357 (2026)](https://arxiv.org/abs/2607.05357), improves the quantitative lower bound to, for every eta>0,
  A(X)>>_eta X exp(-(4+eta)(logloglog X/loglog X)log X).
  It is a preprint, not an accepted proof of positive density.
- Chen--Feng--Templier give useful conditional context involving prime powers and Fermat numbers, but not a resolution of the present prime problem; see [their 2008 paper](https://doi.org/10.4064/aa135-1-4).
- The database still lists the problem open; treat that label as a lead, not as proof: [Erdős Problems #9](https://www.erdosproblems.com/9). The associated sequence is [OEIS A006286](https://oeis.org/A006286).

Do not treat any heuristic, database label, forum statement, or unverified preprint claim as a theorem. Distinguish exact quoted theorems, transparent deductions, conjectures, and heuristics.

## Complete resolutions

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

## Required correctness checks

1. Check p=2, k=0, l=0, and k=l separately wherever parity or congruences are used.
2. Every congruence argument that makes n-2^k-2^l divisible by q must handle the exceptional case n-2^k-2^l=q rather than calling it composite.
3. State whether all constants are absolute, depend on eta, or depend on X. A positive-density proof needs one fixed positive c.
4. Keep upper density distinct from lower/natural/logarithmic density and from relative density in a progression.
5. For every imported theorem, verify its exponent domain, prime versus prime-power domain, uniformity, and exceptional sets from the original source.
6. Audit every limiting step: an X-dependent modulus or a bound valid on only a sparse sequence does not automatically give positive upper density.

## Required deliverables

- A self-contained statement of the target and all conventions.
- A source ledger with direct URLs, publication status, theorem numbers/pages, and exact statements actually used.
- A proof manuscript or a disproof manuscript with every imported lemma explicitly mapped to hypotheses.
- A dedicated adversarial audit of the six correctness checks above.
- If incomplete: a precise bottleneck lemma, proof attempts, counterexamples to failed lemmas, and an evidence-based explanation of why the remaining gap is not cosmetic.
- A final status report that says either `RESOLVED_AFFIRMATIVE`, `RESOLVED_NEGATIVE`, or `OPEN_WITH_CHECKPOINT`; never label an incomplete lower-bound improvement a solution.

## Dynamic Multiagent v2 protocol

Establish a research root that owns the canonical statement, source ledger, approach registry, and final synthesis. Use at most four concurrent agents total, including the root.

Begin with independent early waves rather than fixed roles: each active agent must register a falsifiable approach, its exact target lemma, prerequisites, and a failure criterion in the approach registry before substantial work. Avoid duplicated derivations unless they are explicitly assigned as independent verification.

The root dynamically allocates and reuses slots after evidence arrives. Possible approaches may include auditing the newest lower-bound proof, seeking a fixed-density covering lemma, seeking a density-zero theorem, or testing a sharply specified intermediate proposition; none is mandated. At every wave boundary, retire disproved routes, merge reusable lemmas, and launch incompatible alternatives. Reserve an adversarial proof-checking pass for any claimed decisive lemma, and require a fresh agent or the root to inspect it before it enters the shared theorem ledger.

Proof-first allocation is mandatory. At most one optional computational subtask may run at a time. Before it begins, record (i) the exact lemma or construction it tests, (ii) the hypotheses and search domain, (iii) a certificate format, and (iv) a stopping condition. End and reassign that slot immediately once the question is answered. Computation may discover or reject a finite ingredient; it may not be used as evidence for an asymptotic density claim without a proof bridge.

## Persistence and resumability

Maintain `research_state.md` at the research root. At each meaningful checkpoint record: the canonical statement; source URLs and verification state; current theorem ledger; approach registry with active/failed/parked status; exact unresolved lemmas; computation certificates if any; and the next smallest proof obligation.

If a runtime boundary occurs before a complete resolution, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, preserve all failed-route evidence, and resume from the recorded smallest unresolved obligation. Do not convert an interrupted investigation, numerical experiment, or unverified draft into a solution claim.
