# Evidence-backed per-problem audit protocol

You are auditing exactly one Erdős problem. The current date is
`{{CURRENT_DATE}}`. The only repository input you may use is the single problem
JSON appended to this protocol. Do not inspect the surrounding repository and
do not compare the problem with other repository entries.

This is not a request to solve the problem. It is a due-diligence task whose
output will decide whether and how a later research agent should attempt it.
Use public web search extensively and return only JSON matching the supplied
schema.

## 1. Mandatory current-status search

Perform a targeted search rather than trusting the input status.

1. Open the current Erdős Problems page, its LaTeX page when useful, and its
   forum thread if one exists.
2. Follow the cited primary papers or preprints that establish the strongest
   known results.
3. Search the exact statement, distinctive mathematical phrases, problem
   number, named conjecture, and principal authors.
4. Search for recent work, especially from the last three years, using arXiv,
   journal pages, author pages, and formalization repositories as appropriate.
5. Investigate solution or counterexample claims found in forums or secondary
   databases. A claim is not a solution until a proof, paper, formal artifact,
   or sufficiently detailed argument can be inspected.

The database label is evidence, not ground truth. Conversely, failure to find a
solution is not a logical proof that none exists. Calibrate the status and
confidence to the directness and completeness of the search evidence.

Record the actual search queries and every source that materially affects the
conclusion. Prefer primary papers and official records. Distinguish
peer-reviewed publications, preprints, database records, formal artifacts, and
informal claims.

## 2. Statement and counterexample audit

Reconstruct a canonical current statement with explicit definitions,
quantifiers, boundary conditions, asymptotic conventions, player order, and
equality/strictness conventions.

Check for:

- omitted or ambiguous quantifiers;
- undefined terminology or multiple conventions in the literature;
- transcription errors;
- hidden small-parameter exceptions;
- a simple construction or counterexample that kills the literal statement;
- later papers that add a condition, replace the conjecture, or split it into
  several non-equivalent variants;
- a primary question that has been solved while a stronger or residual question
  remains open;
- a broad request such as “estimate” or “describe” whose completion criterion
  is not unique.

Do not silently repair a defective problem. Document the original defect,
revision history, and the exact corrected or residual target. If no targeted
easy counterexample is found, say so without claiming exhaustive proof.

Classify the truth status of the literal, canonically reconstructed statement
separately from uncertainty about the authors' intended repair. In particular:

- if the literal statement is precise enough to formalize and a complete
  solution or counterexample is verified, use `solved` or `disproved` even when
  the historical intended variant is ambiguous;
- record uncertainty about intent under statement ambiguity, revision history,
  limitations, and human-review reasons;
- use `ambiguous` as the primary status only when no unique literal proposition
  can be reconstructed well enough to receive a truth value;
- never give a nonzero solvability score to a literal statement classified as
  solved or disproved merely because a different repaired conjecture might be
  open.

## 3. Literature synthesis

State the strongest verified prior results, the most recent relevant work, the
methods already used, and the precise remaining core. Include authors, year,
publication status, and direct links in the evidence records.

Separate:

- what a source actually proves;
- what it conjectures;
- what follows by a short transparent deduction;
- what remains uncertain or disputed.

## 4. Actionability and solvability assessment

Classify the current record as one of:

- a research-ready open problem;
- a revised open target whose original form is no longer suitable;
- a solved/disproved problem needing proof verification only;
- an ambiguous/invalid problem needing clarification or repair;
- a meta-mathematical record needing a different audit.

Reassess AI solvability only after the status and statement audit. Reward
well-defined proof targets, substantial prior work, narrow remaining gaps,
independently checkable lemmas, and rigorous certificates. Penalize ambiguous
completion criteria, reliance on unknown theorem-strength inputs, uncontrolled
asymptotics, and misleadingly easy finite computation.

The score measures the chance of resolving a genuinely current open
mathematical target, not the ease of verifying that an old statement is already
closed or broken. Therefore:

- if `current_status` is `solved`, `disproved`, or `invalid_or_trivial`, set
  `ai_solvability.level` to `not_applicable_closed_or_invalid` and its score to
  `0`;
- if `current_status` is `meta_mathematical`, set the level to
  `not_applicable_meta_mathematical` and its score to `0`;
- a revised open target may receive a nonzero score, but the score must refer
  only to the explicit surviving target.

Computation must not dominate the proposed route. It is useful only when tied
to a precise lemma, counterexample search, or exact certificate with a stopping
condition.

## 5. Completion test

Write explicit affirmative and negative completion conditions that are genuine
logical alternatives whenever the mathematical task permits. For verification,
clarification, or meta-mathematical records, adapt these fields to the two
decisive audit outcomes.

List results that would still be partial, and list the problem-specific traps a
proof auditor must check.

## 6. Independent Wang-style research prompt

Produce a complete standalone Markdown prompt in `prompt.markdown`.

Choose the mode honestly:

- `solve_open_problem` for a well-posed current open problem;
- `resolve_revised_problem` for the precise surviving target;
- `verify_claimed_solution` when a complete solution/disproof is claimed;
- `clarify_or_repair_statement` when the statement is materially defective;
- `meta_mathematical_audit` for independence or similar records.

The prompt must contain:

1. self-contained definitions and the canonical target;
2. accepted background with source links and clear separation of theorem and
   conjecture;
3. exact completion conditions;
4. a detailed “what does not count” section;
5. problem-specific correctness checks;
6. concrete deliverables and citation requirements;
7. a dynamic Multiagent v2 section with a research root, at most four
   concurrent agents, early independence of approaches, an approach registry,
   adversarial proof checking, dynamic slot reuse, and multiple waves;
8. proof-first resource allocation: at most one optional computational subtask,
   declared lemma/hypotheses and stopping condition before computation, and
   immediate reassignment of that slot when the question is answered;
9. `research_state.md` checkpointing and `CHECKPOINT_NOT_FINAL` behavior if a
   runtime boundary interrupts an incomplete investigation.

Use these standard section headings, adapting their contents to the chosen
mode:

- `## Definitions and canonical target`
- `## Accepted background`
- `## Complete resolutions`
- `## What does not count as a solution`
- `## Required correctness checks`
- `## Required deliverables`
- `## Dynamic Multiagent v2 protocol`
- `## Persistence and resumability`

Do not prescribe a fixed mathematical method or static agent assignment.
Suggestions derived from the literature may be recorded as background, but the
research system must remain free to explore incompatible approaches.

For solved, disproved, invalid, or ambiguous records, do not write a fake
open-problem prompt. Write the corresponding proof-verification or statement-
repair prompt instead.

Set `prompt.filename` to `problem_{{PROBLEM_NUMBER}}.md`.

## 7. Evidence discipline

- Do not invent citations, publication dates, theorem statements, or URLs.
- Do not treat search snippets as proof of a mathematical claim.
- Do not call an informal forum claim peer-reviewed.
- Mark uncertainty and request human review when sources conflict, a paper is
  inaccessible, the current statement cannot be reconstructed, or a claimed
  solution has not been independently checked.
- The final JSON is an evidence-backed audit, not a mathematical solution.
- Do not emit provisional, placeholder, or partial JSON before using the
  required search tools. Return exactly one complete final JSON object after
  the audit.

## Single problem JSON

```json
{{PROBLEM_JSON}}
```
