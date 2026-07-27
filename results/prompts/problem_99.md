# Erdős Problem 99 — research prompt

## Definitions and canonical target

For every integer \(n\ge 2\), set
\[
D(n)=\min\{\operatorname{diam}(A):A\subset\mathbb R^2,\ |A|=n,\ \|x-y\|\ge1\text{ for all distinct }x,y\in A\},
\]
where \(\operatorname{diam}(A)=\max_{x,y\in A}\|x-y\|\).  Let \(\operatorname{Opt}(n)\) be the sets attaining \(D(n)\).

Prove or disprove:
\[
\exists N\ \forall n\ge N\ \forall A\in\operatorname{Opt}(n)\ \exists\,x,y,z\in A\text{ distinct}:
\|x-y\|=\|y-z\|=\|z-x\|=1.
\]

Thus the triangle is Euclidean, equilateral, and has all three sides exactly \(1\). The universal quantifier is over every exact diameter minimizer. The equivalent original normalization says that the minimum pairwise distance is exactly \(1\): an optimizer under separation \(\ge1\) cannot have all distances \(>1\), since uniform contraction would reduce its diameter.

## Accepted background

- Erdős stated this exact eventual-unit-equilateral-triangle conjecture for minimum-diameter unit-separated planar sets in 1994; he also described the stronger triangular-lattice-intersection expectation as unproved. Read the primary source: [Erdős (1994)](https://mathematica-pannonica.ttk.pte.hu/articles/mp05-2/mp05-2-261-269.pdf).
- The 1995 republication restates the conjecture and historical doubts; it is background, not a solution: [Erdős (1995)](https://revistas.usp.br/resenhasimeusp/en/article/view/74798).
- The current curated record calls the problem open but explicitly says that its label is only the maintainer's belief: [Erdős Problems #99](https://www.erdosproblems.com/99) and its [LaTeX source](https://www.erdosproblems.com/latex/99).
- Bezdek and Fodor determined \(D(8)\), after prior exact small-\(n\) work; this is a finite-case result, not a theorem about all sufficiently large \(n\): [Bezdek–Fodor (1999), DOI 10.1006/jcta.1998.2889](https://doi.org/10.1006/jcta.1998.2889).
- Treat the triangular-lattice/circular-truncation asymptotic picture as motivation only. It does not establish exact finite optimality, uniqueness, a stability theorem, or a unit equilateral triangle in every optimizer.

## Complete resolutions

An affirmative resolution is a rigorous proof of one integer \(N\) for which the displayed statement holds for every \(n\ge N\) and every exact minimizer \(A\).

A negative resolution is a proof that for infinitely many integers \(n\) there exists \(A_n\in\operatorname{Opt}(n)\) with no three points forming a unit equilateral triangle. Each member of the family must be proved globally diameter-minimal, not merely feasible or near-optimal.

## What does not count as a solution

- A configuration with diameter asymptotic to \(D(n)\), or within a bounded/additive/asymptotically negligible error of \(D(n)\).
- A proof for one optimizer, a subsequence of optimizers, a particular lattice truncation, or finitely many values of \(n\).
- The \(n=4\) square: it is a relevant small-case obstruction to an all-\(n\) statement, but it does not refute an eventual statement.
- A result proving only two unit edges, approximate equilateral geometry, or a triangle with another side length.
- A lattice-density, contact-number, or shape theorem that does not force the exact three unit distances.
- Numerical optimization, plots, floating-point equality, or a solver result without a complete exact certificate of global optimality and a declared stopping condition.

## Required correctness checks

1. State which quantifier over minimizers the argument proves; audit every use of “an optimal configuration” versus “every optimal configuration.”
2. Prove that all claimed configurations satisfy pairwise separation \(\ge1\), and check the three target distances exactly.
3. Separate exact \(D(n)\) inequalities from asymptotic estimates, including all boundary terms needed for a contradiction.
4. For any compactness, normalization, or existence step, justify it after quotienting translations and use a closed separation condition.
5. For a proposed counterexample family, supply a matching lower bound on \(D(n)\) for each relevant \(n\), not an empirical comparison.
6. For a proposed positive proof, identify and rule out all triangle-free exact-minimizer contact/degeneracy cases; do not assume lattice membership or generic position.
7. Cite every imported theorem with a stable primary URL and state precisely the version, hypotheses, and conclusion used.

## Required deliverables

- A concise `status.md` stating whether the work has an affirmative proof, an infinite certified counterexample family, a partial lemma, or no resolution.
- A self-contained proof manuscript with numbered lemmas and explicit dependency graph.
- A source log containing stable URLs, bibliographic metadata, exact theorem statements used, and a clear label for theorem/conjecture/heuristic.
- For any proposed construction, exact coordinates or a symbolic parametrization, separation verification, diameter calculation, and global-optimality certificate.
- For any computational aid, a separate certificate document stating the lemma tested, hypotheses, exact arithmetic/model, completeness argument, stopping condition, and independent verification instructions.
- An adversarial audit note that attempts to falsify the final claimed quantifiers and identifies any remaining gap.

## Dynamic Multiagent v2 protocol

Maintain a research root with at most four concurrent agents. Start with independent approaches rather than a fixed mathematical method: each active agent must register its precise target, assumptions, claimed novelty, dependencies, and falsification test in an approach registry before substantial work.

Use multiple waves. In the first wave, assign mutually incompatible perspectives such as exact-optimizer structural analysis, a possible infinite-counterexample program, literature/formalization verification, and hostile examination of boundary and quantifier issues; do not assume any perspective is correct. Reuse slots dynamically as soon as an approach reaches a decisive obstruction, produces a reusable lemma, or is refuted.

At every merge point, run adversarial proof checking by an agent that did not author the argument. Check theorem hypotheses, exact versus asymptotic estimates, universal quantifiers over optimizers, all equality cases, and whether a construction is globally optimal. Register failed approaches and counterexamples to intermediate claims so that later waves do not repeat them.

Allocate resources proof-first. At most one optional computational subtask may run at a time. Before it starts, record the exact lemma or counterexample question, finite hypotheses/search domain, certificate format, and stopping condition. Immediately release and reassign that slot once the stated question is answered; computation may not become an open-ended packing search.

## Persistence and resumability

Maintain `research_state.md` after each meaningful wave. It must record the canonical statement, bibliography checked, live and rejected approaches, lemma dependencies, exact unresolved subclaims, artifacts and hashes/URLs, and the next smallest proof obligation.

If a runtime boundary interrupts an incomplete investigation, write `CHECKPOINT_NOT_FINAL` prominently in `research_state.md`, preserve all negative checks and proof-audit findings, and resume from the registered unresolved obligation. Do not report a solution until the affirmative or negative completion condition above has been met and independently adversarially checked.
