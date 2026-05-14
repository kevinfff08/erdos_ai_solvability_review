#!/usr/bin/env python3
"""Run GPT-5.5 one-problem reviews for every missing problem JSON."""

from __future__ import annotations

import argparse
import csv
import subprocess
import sys
import time
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "data" / "index" / "problems_index.csv"
SINGLE_DIR = ROOT / "data" / "single_problem_json"
OUT_DIR = ROOT / "llm_reviews" / "json"
RUN_LOG = ROOT / "llm_reviews" / "run_progress.log"


def read_numbers() -> list[str]:
    with INDEX.open("r", encoding="utf-8-sig", newline="") as f:
        return [row["number"] for row in csv.DictReader(f)]


def review_exists(number: str) -> bool:
    return (OUT_DIR / f"problem_{number.replace('-', '_')}.json").exists()


def problem_path(number: str) -> Path:
    return SINGLE_DIR / f"problem_{number.replace('-', '_')}.json"


def run_one(number: str, force: bool) -> tuple[str, int, float]:
    start = time.time()
    command = [
        sys.executable,
        str(ROOT / "scripts" / "run_single_model_review.py"),
        str(problem_path(number)),
    ]
    if force:
        command.append("--force")
    completed = subprocess.run(command, cwd=str(ROOT), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    elapsed = time.time() - start
    with RUN_LOG.open("a", encoding="utf-8", newline="\n") as f:
        f.write(f"[problem {number}] exit={completed.returncode} elapsed={elapsed:.1f}s\n")
        if completed.stdout:
            f.write(completed.stdout[-4000:] + "\n")
    return number, completed.returncode, elapsed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--limit", type=int, default=0, help="Optional limit for testing.")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    RUN_LOG.parent.mkdir(parents=True, exist_ok=True)

    numbers = read_numbers()
    if not args.force:
        numbers = [number for number in numbers if not review_exists(number)]
    if args.limit:
        numbers = numbers[: args.limit]

    total = len(numbers)
    RUN_LOG.write_text(f"starting total={total} workers={args.workers} force={args.force}\n", encoding="utf-8")
    if total == 0:
        print("no reviews to run")
        return 0

    completed_count = 0
    failed: list[str] = []
    pending = iter(numbers)

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {}
        for _ in range(min(args.workers, total)):
            number = next(pending)
            futures[executor.submit(run_one, number, args.force)] = number

        while futures:
            done, _ = wait(futures, return_when=FIRST_COMPLETED)
            for future in done:
                number = futures.pop(future)
                try:
                    done_number, code, elapsed = future.result()
                except Exception as exc:
                    code = 1
                    elapsed = 0.0
                    done_number = number
                    with RUN_LOG.open("a", encoding="utf-8", newline="\n") as f:
                        f.write(f"[problem {number}] exception={exc!r}\n")
                completed_count += 1
                if code != 0:
                    failed.append(done_number)
                print(f"{completed_count}/{total} problem {done_number} exit={code} elapsed={elapsed:.1f}s")

                try:
                    next_number = next(pending)
                except StopIteration:
                    continue
                futures[executor.submit(run_one, next_number, args.force)] = next_number

    if failed:
        print("failed: " + ", ".join(failed), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
