# Current published results

This directory contains the current V2 publication snapshot.

- [`reports/problem_review_index.md`](reports/problem_review_index.md): clickable reader-facing index of every completed V2 problem report.
- [`reports/candidate_selection_2026-08-05.md`](reports/candidate_selection_2026-08-05.md): three-pass selection record and the latest 20-problem batch outcome.
- `reviews/`: canonical machine-readable review records.
- `manifest.json`: coverage, lineage and missing-problem manifest.
- `prompts/`: standalone proof-research prompts for open and revised-open targets only.
- `problems/`: 682 human-readable problem pages; 124 currently include a V2 block.
- `reports/`: repository-wide summaries for the completed V2 records.
- `categories/`: cross-category summaries for the completed V2 records.
- `index/`: compact CSV and JSON indexes.

## Authority and coverage

`reviews/` together with `manifest.json` is the authoritative V2 layer. The other files are publication views derived from it.

The snapshot dated 2026-08-05 contains 124 canonical V2 reviews and 113 prompts out of a 682-problem catalog. Reports and category counts therefore describe the completed subset, not all 682 problems. Closed, disproved, invalid, meta-mathematical, ambiguous, and insufficient-evidence records do not receive a published research prompt.

Each review records its evidence cutoff. A status such as `confirmed_open` is a dated research conclusion under the evidence policy, not a timeless guarantee.
