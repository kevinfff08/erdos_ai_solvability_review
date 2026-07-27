#!/usr/bin/env python3
"""Run one evidence-backed audit for exactly one Erdős problem.

The model receives the common audit protocol plus one compact problem JSON.
It runs in a fresh temporary directory with live web search enabled and cannot
read the review repository. The final structured result is written atomically
to results/reviews/problem_<number>.json.
"""

from __future__ import annotations

# Reference only: the repository publishes results and does not expose an
# operational review service or supported maintenance command.

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

from v2_review_helpers import atomic_write_json, safe_number, validate_schema


ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "analysis" / "deep_review.schema.json"
PROTOCOL = ROOT / "analysis" / "deep_review_protocol.md"
OUT_DIR = ROOT / "results" / "reviews"
LOG_DIR = ROOT / "runtime" / "logs" / "reference"


def compact_problem(problem: dict) -> dict:
    """Retain all decision-relevant fields while bounding pathological records."""

    def clipped(name: str, limit: int) -> str:
        value = problem.get(name) or ""
        if len(value) <= limit:
            return value
        return value[:limit] + f"\n[truncated from {len(value)} characters]"

    return {
        "number": problem.get("number"),
        "url": problem.get("url"),
        "latex_url": problem.get("latex_url"),
        "prize": problem.get("prize"),
        "status": problem.get("status"),
        "status_last_update": problem.get("status_last_update"),
        "status_note": problem.get("status_note"),
        "formalized": problem.get("formalized"),
        "formalized_last_update": problem.get("formalized_last_update"),
        "formalized_note": problem.get("formalized_note"),
        "oeis": problem.get("oeis") or [],
        "tags": problem.get("tags") or [],
        "comments": clipped("comments", 8000),
        "statement": clipped("statement", 30000),
        "remarks": clipped("remarks", 30000),
        "references": clipped("references", 30000),
        "parse_status": problem.get("parse_status"),
    }


def build_prompt(problem: dict) -> str:
    protocol = PROTOCOL.read_text(encoding="utf-8")
    return (
        protocol.replace("{{CURRENT_DATE}}", date.today().isoformat())
        .replace("{{PROBLEM_NUMBER}}", str(problem["number"]))
        .replace(
            "{{PROBLEM_JSON}}",
            json.dumps(compact_problem(problem), ensure_ascii=False, indent=2),
        )
    )


def resolve_codex_cli(explicit: str | None) -> Path:
    """Resolve a runnable CLI, copying the packaged Desktop binary when needed."""

    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit))
    if os.environ.get("ERDOS_CODEX_CLI"):
        candidates.append(Path(os.environ["ERDOS_CODEX_CLI"]))
    found = shutil.which("codex")
    if found:
        candidates.append(Path(found))

    for candidate in candidates:
        if candidate.exists() and "WindowsApps" not in str(candidate):
            return candidate.resolve()

    packaged = [
        path
        for path in Path(r"C:\Program Files\WindowsApps").glob(
            "OpenAI.Codex_*_x64__2p2nqsd0c76g0/app/resources/codex.exe"
        )
        if path.is_file()
    ]
    if not packaged:
        raise FileNotFoundError(
            "No runnable Codex CLI found. Set ERDOS_CODEX_CLI to a codex executable."
        )
    source = max(packaged, key=lambda path: path.stat().st_mtime)
    target = Path(tempfile.gettempdir()) / "codex_cli_erdos_batch.exe"
    if not target.exists() or target.stat().st_size != source.stat().st_size:
        shutil.copy2(source, target)
    return target


def validate_result(data: dict, expected_number: str) -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    schema_errors = validate_schema(data, schema)
    if schema_errors:
        raise ValueError("schema validation failed: " + "; ".join(schema_errors[:20]))
    if data.get("problem_number") != expected_number:
        raise ValueError(
            f"problem mismatch: expected {expected_number}, got {data.get('problem_number')}"
        )
    if data.get("review_type") != "evidence_backed_problem_audit_v2":
        raise ValueError("unexpected review_type")
    prompt = data.get("prompt") or {}
    if prompt.get("filename") != f"problem_{safe_number(expected_number)}.md":
        raise ValueError("prompt filename does not match problem number")
    if len(prompt.get("markdown") or "") < 1200:
        raise ValueError("generated prompt is too short")
    sources = data.get("evidence_sources") or []
    if not sources or any(not source.get("url") for source in sources):
        raise ValueError("evidence source list is empty or contains a missing URL")
    status = data.get("current_status")
    solvability = data.get("ai_solvability") or {}
    if status in {"solved", "disproved", "invalid_or_trivial"}:
        if (
            solvability.get("level") != "not_applicable_closed_or_invalid"
            or solvability.get("score") != 0
        ):
            raise ValueError("closed/disproved/invalid record must have score 0")
    if status == "meta_mathematical":
        if (
            solvability.get("level") != "not_applicable_meta_mathematical"
            or solvability.get("score") != 0
        ):
            raise ValueError("meta-mathematical record must have score 0")


def run_review(
    problem_path: Path,
    model: str,
    reasoning: str,
    force: bool,
    cli_arg: str | None,
    output_dir: Path,
    log_dir: Path,
) -> int:
    problem = json.loads(problem_path.read_text(encoding="utf-8"))
    number = str(problem["number"])
    output_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"problem_{safe_number(number)}.json"
    log_path = log_dir / f"problem_{safe_number(number)}.log"
    if output_path.exists() and not force:
        print(f"skip existing {output_path}")
        return 0

    cli = resolve_codex_cli(cli_arg)
    work_dir = Path(tempfile.mkdtemp(prefix=f"erdos_deep_{safe_number(number)}_"))
    temporary_output = work_dir / "result.json"
    command = [
        str(cli),
        "--search",
        "exec",
        "-m",
        model,
        "-c",
        f'model_reasoning_effort="{reasoning}"',
        "-s",
        "read-only",
        "--ephemeral",
        "--ignore-rules",
        "--skip-git-repo-check",
        "-C",
        str(work_dir),
        "--output-schema",
        str(SCHEMA),
        "-o",
        str(temporary_output),
        "-",
    ]
    completed = subprocess.run(
        command,
        input=build_prompt(problem),
        text=True,
        encoding="utf-8",
        cwd=str(work_dir),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    log_path.write_text(completed.stdout or "", encoding="utf-8", newline="\n")
    if completed.returncode != 0:
        print(
            f"deep review failed for problem {number}: exit={completed.returncode}; "
            f"log={log_path}",
            file=sys.stderr,
        )
        return completed.returncode
    if not temporary_output.exists():
        print(f"model produced no output for problem {number}", file=sys.stderr)
        return 1

    data = json.loads(temporary_output.read_text(encoding="utf-8"))
    data["review_model"] = model
    validate_result(data, number)
    atomic_write_json(output_path, data)
    print(f"deep-reviewed problem {number} -> {output_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("problem_json", type=Path)
    parser.add_argument("--model", default="gpt-5.6-terra")
    parser.add_argument(
        "--reasoning",
        default="high",
        choices=["low", "medium", "high", "xhigh", "max", "ultra"],
    )
    parser.add_argument("--cli")
    parser.add_argument("--output-dir", type=Path, default=OUT_DIR)
    parser.add_argument("--log-dir", type=Path, default=LOG_DIR)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    return run_review(
        args.problem_json.resolve(),
        args.model,
        args.reasoning,
        args.force,
        args.cli,
        args.output_dir.resolve(),
        args.log_dir.resolve(),
    )


if __name__ == "__main__":
    raise SystemExit(main())
