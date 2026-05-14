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
intended path for live GPT-5.5 review when an API key or local proxy is
available.

## Current First-Pass Assessment

The current files are a conservative Codex-authored first-pass triage, not a
claimed mathematical solution and not a claimed external GPT-5.5 API audit.
The environment used to create this repository did not expose an
`OPENAI_API_KEY` or a running local OpenAI-compatible model endpoint.

The rubric estimates whether a frontier LLM, assisted by normal mathematical
tooling, could plausibly complete or substantially advance the problem. It
considers:

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
