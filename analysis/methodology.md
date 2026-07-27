# Assessment Methodology

## Repository scope

The source catalog contains 682 Erdős Problems entries selected from statuses such as `open`, `falsifiable`, `verifiable`, `decidable`, `not provable`, `not disprovable`, and `independent`. These source labels are preserved as historical input, not accepted as current mathematical conclusions.

The repository has two assessment layers:

1. V1 is a historical GPT-5.5 solvability triage and is preserved under `archive/v1/`.
2. V2 is an evidence-backed audit of the statement, current status, open core, and AI research tractability. Its canonical records are under `results/reviews/`.

## One-problem isolation

Each V2 audit was performed from a common protocol plus exactly one compact problem record. The reviewing process could search the web, but did not receive other repository reviews, repository-local skills, or conclusions from neighboring problems. This limits cross-problem anchoring while preserving access to primary literature.

## Evidence policy

For each problem, the audit searches for:

- the Erdős Problems page, displayed statement, LaTeX, history and discussion;
- original references and directly relevant papers;
- exact-statement and formula searches;
- recent papers, preprints, proofs, counterexamples and revised formulations;
- the underlying text of any claimed solution or disproof.

Every material status claim must cite a dated, accessible source and describe what that source supports. Evidence records include URL, title, authors, date, source type, publication status and directness.

“No solution found” is not evidence that a problem is still open. `confirmed_open` requires direct authoritative evidence plus a recent conflict check. If that standard is not met, the audit uses `likely_open` or `insufficient_evidence`.

## Status taxonomy

- `confirmed_open`: direct authoritative evidence supports the precise current target as open, with no later conflicting result found.
- `likely_open`: the available literature strongly suggests openness, but the evidence is not sufficiently direct or complete for confirmation.
- `solved`: a complete positive resolution of the canonical target is supported by verifiable evidence.
- `disproved`: the canonical assertion is false or a decisive counterexample is supported by verifiable evidence.
- `revised_open`: the original form is closed, defective or superseded, while a clearly stated revised target remains open.
- `ambiguous`: materially different readings prevent one canonical target from being selected safely.
- `invalid_or_trivial`: the written target is malformed or collapses under an elementary example or observation.
- `meta_mathematical`: the entry is not an ordinary object-level mathematical problem suitable for a solve prompt.
- `insufficient_evidence`: available evidence does not justify a more specific status.

## Statement and counterexample audit

The V2 record reconstructs the English and Chinese canonical statements with explicit quantifiers and definitions. It also records:

- ambiguous terminology and ambiguity severity;
- boundary cases and degenerate objects;
- easy-example and counterexample checks;
- historical revisions and the difference between the source wording and active research target;
- what a positive or negative resolution must prove;
- tempting partial results that do not count as a full resolution.

Scores for `revised_open` apply only to the explicitly written revised target.

## V2 AI-solvability assessment

The V2 score is assigned only after status and statement auditing. It estimates the suitability of the surviving research target for a long-running AI research agent; it is not a probability that the mathematical statement is true.

The assessment considers the clarity of the target, amount of usable prior work, availability of intermediate obligations and correctness checks, likely need for new theory, and risk that literature or wording uncertainty dominates the task.

The following statuses always receive score 0:

- `solved`
- `disproved`
- `invalid_or_trivial`
- `meta_mathematical`

V1 scores remain only as historical comparison and never override V2.

## Standalone Wang-style prompts

Every completed V2 record produces one prompt under `results/prompts/`. The prompt does not depend on repository context. Its mode follows the audit:

- clear open target: `solve_open_problem`;
- solved or disproved claim: `verify_claimed_solution`;
- material ambiguity or revision: `clarify_or_repair_statement`;
- meta-mathematical or evidential uncertainty: investigation or adjudication.

Each prompt defines the canonical target, accepted background, complete resolutions, non-solutions, correctness checks and deliverables. It specifies a dynamic multi-agent protocol with no more than four concurrent agents including the root agent. Initial routes are independently registered, the root maintains an obligation and evidence state, each round receives adversarial proof audit, and freed capacity is reassigned to the highest-value unresolved obligation.

The prompts are proof-first. Computation is optional, limited to one concurrent computation task, and must declare the lemma, finite range, expected certificate and stopping condition. Numerical evidence cannot replace a universal proof. Interrupted work must emit a non-final checkpoint containing evidence, failed routes and next obligations.

## Publication and lineage

The canonical V2 machine layer is `results/reviews/` plus `results/manifest.json`. Problem pages, prompts, reports, categories and indexes are publication views. The current snapshot has 84 completed V2 records out of 682, so all V2 aggregate statements apply only to that subset.

Historical V1 material is isolated under `archive/v1/`. Local checkpoints, logs, first-pass work products and maintenance scripts are kept under ignored `runtime/` and are not part of the published result surface.
