# Erdős Problem 86: C4-free subgraphs of the hypercube

## Definitions and canonical target

For each integer \(n\ge 1\), let \(Q_n\) be the graph with vertex set \(\{0,1\}^n\), where two vertices are adjacent exactly when their Hamming distance is one. Thus \(e(Q_n)=n2^{n-1}\).

A \(C_4\) is a simple four-cycle. Let
\[
f(n)=\max\{e(G):G\subseteq Q_n\text{ and }G\text{ contains no subgraph isomorphic to }C_4\}.
\]
Here \(G\subseteq Q_n\) may be taken spanning; the prohibition is not an induced-subgraph condition. Equivalently in a hypercube, it forbids every coordinate square.

Prove the canonical Erdős conjecture
\[
\forall\epsilon>0\ \exists N\ \forall n\ge N:\quad
f(n)\le (1/2+\epsilon)n2^{n-1}.
\]
Equivalently, for every \(\epsilon>0\), every sufficiently large \(Q_n\)-subgraph with more than \((1/2+\epsilon)e(Q_n)\) edges contains a \(C_4\). The desired conclusion is \(\pi_e(C_4)=\lim_{n\to\infty}f(n)/e(Q_n)=1/2\).

## Accepted background

- Erdős's 1991 problem record states the epsilon-form asymptotic conjecture: [publication index and review](https://www.maths.tcd.ie/EMIS/classics/Erdos/cit/84005094.htm).
- Brass, Harborth, and Nienborg proved \(f(n)\ge \tfrac12(n+\sqrt n)2^{n-1}\) when \(n=4^r\), and \(f(n)\ge\tfrac12(n+0.9\sqrt n)2^{n-1}\) for all \(n\ge9\): [J. Graph Theory 19 (1995), 17--23](https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.3190190104). This is compatible with the target because its relative excess is \(o(1)\).
- Balogh, Hu, Lidický, and Liu proved the asymptotic upper bound \(\pi_e(C_4)\le0.6068\) using an adaptation of flag algebras: [European J. Combin. 35 (2014), 75--85](https://experts.illinois.edu/en/publications/upper-bounds-on-the-size-of-4-and-6-cycle-free-subgraphs-of-the-h/).
- Baber improved this to \(\pi_e(C_4)\le0.60318\): [arXiv:1201.3587](https://arxiv.org/abs/1201.3587). This is a preprint, not a peer-reviewed paper; the author describes it as deliberately unpublished on [his publication page](https://www.rahilbaber.com/).
- The most recent directly relevant work found is Minamoto's finite-dimensional preprint, which proves \(\operatorname{ex}(Q_7,C_4)\ge304\) and \(\operatorname{ex}(Q_8,C_4)\ge680\): [arXiv:2603.29127](https://arxiv.org/abs/2603.29127). Its companion [edge lists and verifier](https://github.com/minamominamoto/c4free-hypercube) provide finite certificates; they do not prove an asymptotic upper bound, and its heuristic nonexistence searches are not theorems.

Treat the preceding bullets as established results only to the extent stated. Do not convert the finite 2026 results, an unsuccessful search, or a numerical SDP result into an asymptotic theorem.

## Complete resolutions

An affirmative resolution must give a complete rigorous proof that, for every \(\epsilon>0\), all sufficiently large \(C_4\)-free \(G\subseteq Q_n\) satisfy
\[
e(G)\le(1/2+\epsilon)e(Q_n).
\]

A negative resolution must give a fixed \(\delta>0\), infinitely many \(n_j\to\infty\), and rigorously verified \(C_4\)-free \(G_j\subseteq Q_{n_j}\) such that
\[
e(G_j)\ge(1/2+\delta)e(Q_{n_j}).
\]

The latter is the genuine logical negation because the density limit exists by the standard averaging argument.

## What does not count as a solution

- A bound \(f(n)\le(1/2+\delta)e(Q_n)\) for one fixed \(\delta>0\), including 0.60318.
- A construction whose relative density is only \(1/2+o(1)\), including the BHN construction.
- Exact values, local optimality, or failed searches for finitely many dimensions.
- A proof for induced-\(C_4\)-free graphs, a restricted family of subgraphs, or a different ambient graph.
- A floating-point SDP, a heuristic, or code output without an auditable exact/rational or rigorously bounded certificate and a proof of its asymptotic transfer.
- A claim that a finite witness implies a fixed-density asymptotic counterexample without an explicit dimension-lifting argument preserving C4-freeness and density.

## Required correctness checks

1. State all epsilon, N, n, and subgraph quantifiers explicitly; retain the strict forcing threshold \(>\), not an unjustified \(\ge\).
2. Normalize every density by \(e(Q_n)=n2^{n-1}\).
3. Prove that the forbidden configuration is every simple \(C_4\). If using coordinate squares, prove or cite the elementary equivalence with all four-cycles of \(Q_n\).
4. Check that every restriction, random projection, averaging step, or recursion preserves the relevant no-\(C_4\) hypothesis in the claimed direction and has errors uniform in \(n\).
5. For a computer-assisted inequality, provide the exact list of local configurations, symmetry/multiplicity convention, PSD or interval/rational certificate, verifier, and a proof that the local inequality yields the stated global asymptotic bound.
6. For a proposed counterexample family, verify every edge belongs to \(Q_n\), every coordinate square is checked, the claimed edge count is exact, and \(\delta\) is independent of dimension.
7. Adversarially test any claimed use of the BHN lower bound: \(n^{-1/2}\to0\), so it is not a disproof of this problem.

## Required deliverables

- A self-contained proof manuscript or a precise counterexample-family construction.
- A one-page claim ledger separating proved lemmas, conjectural observations, failed approaches, and externally cited results.
- A dependency graph showing exactly where each nontrivial theorem is used.
- If computation is used, source code, immutable input data, commands, expected hashes/output, and an independent minimal verifier.
- A bibliography with direct URLs and a publication-status label for every external result; distinguish peer-reviewed papers, preprints, formal artifacts, and forum claims.
- An adversarial audit report that tries to falsify the main inference, the normalization, all asymptotic quantifiers, and all computer-assisted steps.

## Dynamic Multiagent v2 protocol

The research root maintains an approach registry containing: approach identifier, precise target lemma, assumptions, status, evidence location, and the reason for stopping or continuing. Run at most four agents concurrently.

Use multiple waves. In the first wave, select independent approaches dynamically from the registry rather than assigning a fixed method or fixed personnel. Before two agents pursue similar ideas, record what makes their target lemmas genuinely different. At every wave boundary, the root reviews evidence, kills duplicated or unsupported routes, and reallocates slots to the most discriminating next lemmas.

Every substantive proof claim is sent to an adversarial checker who did not author that route. The checker must inspect quantifiers, C4 conventions, constants, lifting/restriction steps, and any computation. A route is not promoted merely because no objection was immediately found.

Proof-first allocation is mandatory. At most one optional computational subtask may run at once. Before it starts, its owner must state the exact lemma or counterexample question, hypotheses, certificate format, and a stopping condition that determines what answer the computation can establish. Immediately reassign that slot once the finite question is answered; do not run open-ended optimization as evidence of truth.

The root may add, merge, pause, or retire agents dynamically, subject to the four-agent cap. It must preserve independent lines of attack early, schedule adversarial proof checking before synthesis, and maintain the approach registry across waves.

## Persistence and resumability

Maintain `research_state.md` from the first step. It must record the canonical target, citations checked, active and retired approaches, exact claims with proof status, computation specifications and hashes, checker objections, and the next smallest decisive tasks.

At any runtime boundary, write a checkpoint before yielding. If the investigation is incomplete, return `CHECKPOINT_NOT_FINAL` together with the path/state of `research_state.md`, the active claim ledger, and the next verification tasks. Never present an unverified partial route as a solution after a checkpoint interruption.
