# Assessment Methodology

Generated: 2026-05-14

## Scope

This repository reviews the unresolved or semi-open records from the Erdős
Problems snapshot: `open`, `falsifiable`, `verifiable`, `decidable`,
`not disprovable`, `not provable`, and `independent`.

## One-Problem Discipline

Each problem file is generated from one problem record at a time. The
repository also includes `scripts/review_one_problem_with_model.py`, whose
prompt accepts exactly one problem JSON file per model call. This is the
legacy OpenAI-compatible API path. The completed GPT-5.5 review layer was run
with `scripts/run_single_model_review.py` and `scripts/run_all_model_reviews.py`;
each `codex exec -m gpt-5.5` invocation received exactly one problem JSON file.

## GPT-5.5 Review Layer

The repository contains `682` completed one-problem GPT-5.5 reviews in
`llm_reviews/json/`. These reviews are not claimed mathematical solutions. They
are structured judgments about whether a GPT-5.5-level system, assisted by
computation, formal verification, literature search, and counterexample search,
could plausibly complete, substantially advance, or verify each problem.

The earlier rule-based first-pass triage is still visible in some index fields,
but the per-problem `GPT-5.5 单题模型复审` blocks, category reports,
`reports/model_review_report.md`, and `reports/overall_repository_report.md`
are based on the GPT-5.5 one-problem review outputs.

The review prompt asked the model to consider:

- status: open, falsifiable, verifiable, decidable, or meta-mathematical;
- original tags and whether they suggest finite computation or proof-heavy
  theory;
- statement cues such as finite search, asymptotics, density, primes, and
  existence/construction language;
- formalized-statement availability;
- OEIS/data availability;
- prize level, used only as a risk signal and never as an automatic
  rejection.

## Levels

- `high_candidate`: AI plus computation/formalization has a strong candidate
  route.
- `medium_candidate`: AI-assisted completion is plausible, but requires
  tools and independent verification.
- `low_to_medium_candidate`: AI may produce partial progress or useful
  experiments; full resolution is uncertain.
- `low_candidate`: current general AI alone is unlikely to complete the
  problem.
- `not_applicable_meta_mathematical`: the record is about independence or
  non-provability/non-disprovability rather than an ordinary ZFC proof goal.

## Reasoning Disclosure

The per-problem "公开版思考过程摘要" is a public audit summary. It is not a raw
hidden chain of thought. It records the criteria used for the judgment:
problem type, AI strengths, obstacles, and required validation route.
