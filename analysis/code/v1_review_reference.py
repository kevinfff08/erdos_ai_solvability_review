#!/usr/bin/env python3
"""Run one live model review for exactly one Erdos problem JSON record.

Environment:
  OPENAI_API_KEY must be set.
  OPENAI_BASE_URL is optional and defaults to https://api.openai.com/v1.
  OPENAI_MODEL is optional and defaults to gpt-5.5.

The prompt is deliberately constructed from exactly one problem record. This
file is retained as a historical reference, not as a supported command.
"""

from __future__ import annotations

# Historical reference only. Published V1 records live under archive/v1/.

import json
import os
import sys
import urllib.request
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: review_one_problem_with_model.py <single_problem_json>", file=sys.stderr)
        return 2

    problem_path = Path(sys.argv[1])
    problem = json.loads(problem_path.read_text(encoding="utf-8"))

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("OPENAI_API_KEY is not set.", file=sys.stderr)
        return 2

    base_url = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    model = os.environ.get("OPENAI_MODEL", "gpt-5.5")

    prompt = f"""
You are reviewing exactly one Erdős open problem. Do not use any other problem
as context. Judge whether a GPT-5.5-level AI system, possibly with computation,
formal verification, literature search, and code execution, could plausibly
complete or substantially advance this problem. Do not reject only because it is
human-unsolved. Do not try to solve it. Return JSON with keys:
verdict, level, score, reasons, likely_route, obstacles, validation_needed,
public_reasoning_summary.

Problem JSON:
{json.dumps(problem, ensure_ascii=False, indent=2)}
""".strip()

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Return only valid JSON. Review exactly one problem."},
            {"role": "user", "content": prompt},
        ],
    }
    request = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        print(response.read().decode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
