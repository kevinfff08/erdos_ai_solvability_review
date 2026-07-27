# Erdős Problem 122 — statement repair and evidence audit

## Definitions and canonical target

Do not treat the database sentence as a theorem. Its phrase “there are infinitely many \(x\) such that \(A(x)\to\infty\)” has a free-limit-variable defect.

The literal text is at [Erdős Problems #122](https://www.erdosproblems.com/122) and the source form is [its LaTeX page](https://www.erdosproblems.com/latex/122). First reconstruct a source-supported target. Record all of the following explicitly:

- the class and codomain of the arithmetic function \(f\), including any slow-growth condition;
- the domain, positivity, and integrality/real-valuedness of \(F\);
- the meaning of “for almost all \(n\)” and the density notion;
- whether \(x\) is integral or real, whether \(n\) is restricted relative to \(x\), and the interval convention;
- the intended reading of the conclusion: a sequence \(x_j\to\infty\), a limsup, or another quantified assertion.

A candidate repair, not an accepted assumption, is
\[
\limsup_{x\to\infty}\frac{\#\{n\in\mathbb N:n+f(n)\in(x,x+F(x))\}}{F(x)}=\infty
\]
for every admissible positive \(F\) with \(F(n)/f(n)\to0\) outside a natural-density-zero exceptional set. Do not proceed to solve this candidate until a primary-source check or explicit human editorial decision approves it.

## Accepted background

[Erdős–Pomerance–Sárközy (1997)](https://math.dartmouth.edu/~carlp/PDF/paper112.pdf), *On Locally Repeated Values of Certain Arithmetic Functions, IV*, Ramanujan Journal 1, 227–241, is peer-reviewed and directly accessible. It defines
\[
g(t)=\#\{m\in\mathbb N:m+\omega(m)=t\},\qquad h(n)=n+\omega(n),
\]
and proves local repeated-value results for \(h\), using a Turán–Kubilius type inequality for additive functions on arithmetic progressions with large modulus. Its Theorems 1–3, and the proof of Theorem 1, are accepted background only in their stated form.

The database reports that Erdős's 1997 papers *Problems in number theory* and *Some of my favourite unsolved problems* say more about \(\tau\), \(\omega\), \(\phi\), and \(\sigma\). Treat that report as unverified until the relevant pages of the primary papers are inspected. In particular, “probably fails” is a conjectural statement, not a disproof.

The recent preprint [Tao–Teräväinen, arXiv:2512.01739](https://arxiv.org/abs/2512.01739) proves results on \(\omega(n)=\omega(n+1)\), \(\Omega\), and \(\tau\). It is relevant context, but it does not by itself resolve the \(n+f(n)\), universal-\(F\) target.

## Complete resolutions

This audit task has two decisive outcomes.

1. **Repair confirmed.** Provide a unique, formalization-ready canonical statement supported by exact pages of Er97/Er97e or another primary source. Then give a current-status result supported by a targeted literature search. If an exact open residual target remains, state its affirmative and negative mathematical completion conditions.
2. **Repair not confirmed.** If the sources give non-equivalent statements or do not resolve the malformed limit, document each formulation and identify the exact human editorial choice required. Do not label the problem mathematically open, solved, or disproved.

For any approved repaired target, an affirmative resolution requires either a proof for the named \(f\) and every admissible \(F\), or a necessary-and-sufficient classification in the declared class. A negative resolution requires an admissible \(F\) and a proof that the exact conclusion fails.

## What does not count as a solution

- Repeating the database's `open` label or a search snippet.
- Treating the EPS97 \(\omega\)-specific local result as a proof for every \(F\) without a quantifier-preserving derivation.
- Verifying only one convenient \(F\).
- Treating an authorial prediction about \(\phi\) or \(\sigma\) as a counterexample.
- Replacing density-one control of \(F(n)/f(n)\) with control at selected interval locations without proof.
- Numerical evidence for collisions or clustering without a theorem/certificate matching the repaired statement.

## Required correctness checks

1. Open the live problem page, LaTeX page, revision history, and forum thread. Treat forum material as informal until linked to a complete proof.
2. Obtain and inspect the relevant pages of Er97 and Er97e. Record page number, exact source URL, publication status, and whether each claim is theorem, report, or conjecture.
3. Read EPS97 around its definitions and Theorems 1–3. State precisely what it proves and what is merely inferred from its construction.
4. Search exact phrases, formulas, author names, \(n+\omega(n)\), \(n+\tau(n)\), \(\phi\), \(\sigma\), arXiv, journal databases, author pages, and formalization repositories, emphasizing 2023–2026.
5. Check every proposed reading of the outer conclusion against its quantifiers, domains, density condition, and endpoint conventions.
6. If a current solution/disproof is claimed, require an independently inspectable paper, proof, or formal artifact and assign an adversarial verifier before accepting it.

## Required deliverables

Return an evidence dossier with:

- literal text and a formal defect log;
- all source-supported candidate statements, in symbolic quantified form;
- a table of sources with authors, dates, URLs, publication status, exact pages/theorem numbers, directness, and claim type;
- a search log, including negative-search scope and date;
- a calibrated status/actionability decision;
- if a repaired open target is confirmed, exact positive and negative completion tests, partial-result exclusions, and proof-audit traps;
- an explicit statement of any human editorial decision still required.

## Dynamic Multiagent v2 protocol

Maintain a research root and a `research_state.md` file. Use at most four concurrent agents. Begin with independent evidence routes, not a fixed mathematical method: agents may separately inspect primary sources, reconstruct formal quantifiers, search later literature, or adversarially check a claimed implication.

Before substantial work, place every active approach in an approach registry in `research_state.md`: question, sources, expected decisive evidence, stop condition, and conflict risks. Each report must give URLs, access dates, publication status, page/theorem anchors, and a clear theorem/conjecture/inference label.

Work in multiple waves. After the first evidence wave, compare the readings, assign an adversarial reviewer to every decisive status claim and every proposed quantifier repair, and dynamically reuse free slots for the largest unresolved issue. Do not duplicate routes merely for convenience.

Use proof-first allocation. At most one computational subtask may run, and only after the registry states its exact lemma, hypotheses, finite stopping condition, and the evidence it can and cannot supply. Immediately reassign that slot when the finite question is answered. Computation cannot establish a universal classification.

## Persistence and resumability

Update `research_state.md` after each evidence wave with inspected sources, source locations, rejected readings, status rationale, and next checks. Preserve exact URLs and page/theorem anchors.

If the run ends before a unique statement and status are established, write `CHECKPOINT_NOT_FINAL` at the top of `research_state.md`, list the exact uninspected primary pages and unfinished searches, and stop without assigning a mathematical open/solved/disproved status. A later root must resume from this checkpoint rather than convert uncertainty into a conclusion.
