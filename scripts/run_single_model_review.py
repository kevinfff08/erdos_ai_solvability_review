#!/usr/bin/env python3
"""Call Codex/GPT-5.5 on exactly one problem JSON file.

The subprocess receives one prompt containing one problem record. It writes the
model's structured final answer to llm_reviews/json/problem_<number>.json.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "model_review.schema.json"
OUT_DIR = ROOT / "llm_reviews" / "json"
LOG_DIR = ROOT / "llm_reviews" / "logs"


def compact_problem(problem: dict) -> dict:
    """Keep one problem only, but avoid passing bulky bibliography text."""
    remarks = problem.get("remarks") or ""
    return {
        "number": problem.get("number"),
        "url": problem.get("url"),
        "latex_url": problem.get("latex_url"),
        "prize": problem.get("prize"),
        "status": problem.get("status"),
        "status_note": problem.get("status_note"),
        "formalized": problem.get("formalized"),
        "formalized_note": problem.get("formalized_note"),
        "oeis": problem.get("oeis") or [],
        "tags": problem.get("tags") or [],
        "comments": problem.get("comments") or "",
        "statement": problem.get("statement") or "",
        "remarks_excerpt": remarks[:2500],
        "statement_chars": problem.get("statement_chars"),
        "remarks_chars": problem.get("remarks_chars"),
    }


def build_prompt(problem: dict) -> str:
    return (
        "你正在审查 exactly one Erdős problem。"
        "本次调用只能使用下面这一个 problem JSON，不要参考其他问题，不要做横向比较。"
        "任务不是求解问题，而是判断 GPT-5.5 级别模型在配合计算、形式化证明、文献检索、"
        "反例搜索等工具时，是否可能完成、显著推进或验证这个问题。"
        "不要因为人类尚未解决就直接否定。"
        "不要输出原始隐藏推理链；输出可公开审计的判断依据、主要障碍、验证需求和简明思考摘要。"
        "请严格按 JSON schema 返回，不要 Markdown。\n\n"
        "Problem JSON:\n"
        + json.dumps(compact_problem(problem), ensure_ascii=False, indent=2)
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("problem_json", type=Path)
    parser.add_argument("--model", default="gpt-5.5")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    problem_path = args.problem_json
    problem = json.loads(problem_path.read_text(encoding="utf-8"))
    number = problem["number"]
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUT_DIR / f"problem_{number.replace('-', '_')}.json"
    log_path = LOG_DIR / f"problem_{number.replace('-', '_')}.log"

    if output_path.exists() and not args.force:
        print(f"skip existing {output_path}")
        return 0

    command = [
        "codex",
        "exec",
        "-m",
        args.model,
        "-s",
        "read-only",
        "--ephemeral",
        "--ignore-rules",
        "-C",
        str(ROOT),
        "--output-schema",
        str(SCHEMA),
        "-o",
        str(output_path),
        "-",
    ]
    completed = subprocess.run(
        command,
        input=build_prompt(problem),
        text=True,
        encoding="utf-8",
        cwd=str(ROOT),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    log_path.write_text(completed.stdout or "", encoding="utf-8", newline="\n")
    if completed.returncode != 0:
        print(f"codex review failed for problem {number} with exit {completed.returncode}", file=sys.stderr)
        print(f"log: {log_path}", file=sys.stderr)
        return completed.returncode

    data = json.loads(output_path.read_text(encoding="utf-8"))
    if data.get("problem_number") != number:
        raise ValueError(f"model returned problem_number={data.get('problem_number')} for input {number}")
    print(f"reviewed problem {number} -> {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
