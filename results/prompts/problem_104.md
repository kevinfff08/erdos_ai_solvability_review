# Erdős Problem 104 — proof-first investigation

## Definitions and canonical target

Let \(P\subset\mathbb R^2\) be a finite set of \(n\) distinct points. Let
\[
U(P)=\{C\subset\mathbb R^2:C\text{ is a Euclidean circle of radius }1\text{ and }|C\cap P|\ge3\}.
\]
Circles are counted as distinct geometric circles (equivalently, by distinct centres), not once per contained triple. Define
\[
f(n)=\max_{|P|=n}|U(P)|.
\]

Canonical target: prove \(f(n)=o(n^2)\), namely
\[
\forall\varepsilon>0\ \exists N(\varepsilon)\ \forall n\ge N(\varepsilon)\ \forall P\subset\mathbb R^2,\ |P|=n:\quad |U(P)|\le\varepsilon n^2.
\]

A valid disproof instead consists of a constant \(c>0\) and point sets \(P_j\) with \(|P_j|\to\infty\) and \(|U(P_j)|\ge c|P_j|^2\).

## Accepted background

- The current [Erdős Problems page](https://www.erdosproblems.com/104) records the problem as open, gives the elementary \(O(n^2)\) bound, and reports Elekes's \(\Omega(n^{3/2})\) construction.
- The elementary sharp form of the pair-counting bound is \(|U(P)|\le n(n-1)/3\): each counted circle contains at least three unordered pairs of \(P\), while each pair lies on at most two radius-1 circles. The historical source is Harborth--Mengersen, [*Point sets with many unit circles*](https://www.sciencedirect.com/science/article/pii/0012365X86900117), Discrete Mathematics 60 (1986), 193--197.
- Elekes, [*n points in the plane can determine \(n^{3/2}\) unit circles*](https://dblp.org/rec/journals/combinatorica/Elekes84), Combinatorica 4 (1984), p.131, gives the lower bound \(f(n)=\Omega(n^{3/2})\).
- The related fixed-anchor problem is not this problem: if three families of \(n\) unit circles each pass through one prescribed point, Raz--Sharir--Solymosi proved \(O(n^{11/6})\) triple intersections; see [arXiv:1407.6625](https://arxiv.org/abs/1407.6625) and the 2015 peer-reviewed publication. Do not silently apply that theorem to an arbitrary two-parameter family of unit circles.
- Elekes--Szabó methods remain potentially relevant background. Solymosi--Zahl's [2022 preprint](https://arxiv.org/abs/2211.13294) proves a general real Cartesian-product estimate with structural exceptions, but does not claim to settle this target.

## Complete resolutions

An affirmative resolution is a complete, uniform proof of \(f(n)=o(n^2)\) with all quantifiers stated.

A negative resolution is an explicit infinite quadratic-density construction with a rigorous proof of distinctness, exact radius 1, and at least three input points on every counted circle.

A proof of the stronger \(f(n)=O(n^{3/2})\) is welcome but is not required for completion.

## What does not count as a solution

- Reproving \(O(n^2)\), \(n(n-1)/3\), or \(f(n)\le c n^2\) for any fixed \(c>0\).
- Reporting improved finite-n records or an empirical exponent without a uniform asymptotic theorem.
- Counting triples instead of distinct circles, especially when one circle contains four or more input points.
- Solving only a general-position variant, a lattice case, a fixed-anchor three-family problem, or another restricted family.
- Treating a theorem about unit-distance edges as a theorem about 3-rich points of arbitrary unit-circle arrangements without a proved reduction.
- A computational claim without a declared finite search space, independently checkable certificate, and a proof that the certificate resolves one of the stated asymptotic alternatives.

## Required correctness checks

1. State whether each object is a point, a circle centre, a circle, a triple, an incidence, or a 3-rich intersection point.
2. If using the self-duality \(p\mapsto\{x:|x-p|=1\}\), prove the exact correspondence between circles in \(U(P)\) and 3-rich intersection points, including higher multiplicity and distinctness.
3. For every asymptotic estimate, show constants are independent of \(P\) and \(n\), and identify the threshold after which it applies.
4. If extracting subfamilies or random colour classes, give the retention bound and prove that all required anchor/parameter hypotheses survive.
5. If invoking an Elekes--Szabó, incidence, polynomial-partitioning, or extremal-hypergraph theorem, cite the precise theorem and verify every hypothesis rather than citing the method by name.
6. For a proposed counterexample, list a symbolic or exact-coordinate certificate for every circle and prove that no duplicate circles were counted.

## Required deliverables

- `research_state.md` containing the canonical target, source links, an approach registry, every proved lemma, failed lemma, open dependency, and the next falsifiable subgoal.
- A concise literature log separating direct results on Problem 104 from restricted analogues.
- A proof manuscript or a counterexample manuscript with numbered claims, full references, and a one-page dependency graph.
- An adversarial audit report that attempts to invalidate every reduction, quantifier exchange, asymptotic summation, and counting convention.
- If no complete resolution is obtained, a checkpoint report identifying the strongest fully proved statement and explicitly marked `CHECKPOINT_NOT_FINAL`.

All substantive mathematical and historical claims must cite a primary paper, an arXiv version, or an authoritative bibliographic record with a direct URL.

## Dynamic Multiagent v2 protocol

Use a research root that owns `research_state.md` and the approach registry. Run at most four concurrent agents.

Begin with multiple genuinely independent proof-first approaches. Record each approach before substantial work: target lemma, hypotheses, intended implication to \(o(n^2)\), known obstruction, and a clear falsification test. Do not prescribe a fixed mathematical method or permanent agent assignment.

At each wave boundary, the research root compares the approaches, retires routes contradicted by a checked example or theorem, and dynamically reuses freed slots for the narrowest surviving bottleneck. Every proposed lemma receives adversarial proof checking by an agent not responsible for deriving it. The adversary must inspect hidden restrictions such as fixed anchors, one- versus two-parameter families, multiplicity, and uniformity.

Use several waves: first establish reductions and identify obstruction classes; next pursue incompatible structural routes; then audit any candidate global saving. Maintain an approach registry with status `active`, `blocked`, `refuted`, `proved`, or `merged`, plus evidence and handoff notes.

Proof-first resource allocation is mandatory. At most one slot may perform computation, and only after `research_state.md` declares: (i) the exact lemma or counterexample property under test, (ii) all hypotheses and finite search domain, (iii) the required certificate, and (iv) a stopping condition. Immediately return that slot to proof work once the stated question is answered. Computation may not be used as evidence of an asymptotic conclusion absent a proved bridge.

## Persistence and resumability

Update `research_state.md` after each material result, failed route, source check, or adversarial objection. Preserve exact theorem statements, URLs, assumptions, and proof dependencies so that a later run can resume without redoing source triage.

If a runtime boundary occurs before a complete proof or disproof, do not present a solution. Write `CHECKPOINT_NOT_FINAL` at the top of the current checkpoint, state the unresolved logical gap, list the next smallest verifiable tasks, and retain the active approach registry for the next wave.
