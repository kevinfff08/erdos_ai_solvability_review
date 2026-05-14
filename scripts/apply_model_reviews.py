#!/usr/bin/env python3
"""Merge one-problem GPT-5.5 reviews into problem docs and aggregate reports."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REVIEWS_DIR = ROOT / "llm_reviews" / "json"
PROBLEMS_INDEX = ROOT / "data" / "index" / "problems_index.csv"
SUMMARY_JSON = ROOT / "data" / "index" / "summary.json"
REPORT = ROOT / "reports" / "model_review_report.md"
OVERALL_REPORT = ROOT / "reports" / "overall_repository_report.md"
CATEGORIES_DIR = ROOT / "categories"


START = "<!-- MODEL_REVIEW:START -->"
END = "<!-- MODEL_REVIEW:END -->"


def read_problem_index() -> list[dict[str, str]]:
    with PROBLEMS_INDEX.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def review_path(number: str) -> Path:
    return REVIEWS_DIR / f"problem_{number.replace('-', '_')}.json"


def format_review(review: dict) -> str:
    lines = [
        START,
        "",
        "## GPT-5.5 单题模型复审",
        "",
        f"- 复审类型: `{review['review_type']}`",
        f"- 模型: `{review['review_model']}`",
        f"- 结论: **{review['verdict_zh']}**",
        f"- 等级: `{review['level']}`",
        f"- 分数: `{review['score']}/100`",
        f"- 信心: `{review['confidence']}`",
        f"- 可能路线: {review['likely_route_zh']}",
        "",
        "### 支持理由",
        "",
    ]
    lines.extend(f"- {item}" for item in review["supporting_reasons_zh"])
    lines.extend(["", "### 主要障碍", ""])
    lines.extend(f"- {item}" for item in review["main_obstacles_zh"])
    lines.extend(["", "### 需要的验证", ""])
    lines.extend(f"- {item}" for item in review["validation_needed_zh"])
    lines.extend(
        [
            "",
            "### 公开版思考摘要",
            "",
            review["public_reasoning_summary_zh"],
            "",
            "### 免责声明",
            "",
            review["not_a_solution_disclaimer_zh"],
            "",
            END,
        ]
    )
    return "\n".join(lines)


def replace_block(text: str, block: str) -> str:
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if pattern.search(text):
        return pattern.sub(lambda _match: block, text)
    return text.rstrip() + "\n\n" + block + "\n"


def write_problem_docs(rows: list[dict[str, str]], reviews: dict[str, dict]) -> None:
    for row in rows:
        number = row["number"]
        if number not in reviews:
            continue
        path = ROOT / row["problem_file"]
        text = path.read_text(encoding="utf-8")
        path.write_text(replace_block(text, format_review(reviews[number])), encoding="utf-8", newline="\n")


def write_index(rows: list[dict[str, str]], reviews: dict[str, dict]) -> None:
    fields = list(rows[0].keys())
    extra = ["model_review_level", "model_review_score", "model_review_confidence", "model_review_file"]
    for field in extra:
        if field not in fields:
            fields.append(field)
    with PROBLEMS_INDEX.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            review = reviews.get(row["number"])
            row = dict(row)
            if review:
                row["model_review_level"] = review["level"]
                row["model_review_score"] = review["score"]
                row["model_review_confidence"] = review["confidence"]
                row["model_review_file"] = review_path(row["number"]).relative_to(ROOT).as_posix()
            writer.writerow(row)


def write_report(rows: list[dict[str, str]], reviews: dict[str, dict]) -> None:
    reviewed_rows = [row for row in rows if row["number"] in reviews]
    level_counts = Counter(reviews[row["number"]]["level"] for row in reviewed_rows)
    status_counts = Counter(row["status"] for row in reviewed_rows)
    category_counts = Counter(row["primary_category"] for row in reviewed_rows)
    scores = [reviews[row["number"]]["score"] for row in reviewed_rows]

    lines = [
        "# GPT-5.5 One-Problem Review Report",
        "",
        f"- Generated: {date.today().isoformat()}",
        f"- Reviewed by model calls: {len(reviewed_rows)}",
        f"- Remaining without model review: {len(rows) - len(reviewed_rows)}",
    ]
    if scores:
        lines.extend(
            [
                f"- Average model score: {sum(scores) / len(scores):.1f}/100",
                f"- Score range: {min(scores)} to {max(scores)}",
            ]
        )
    lines.extend(["", "## Level Distribution", "", "| Level | Count |", "|---|---:|"])
    for level, count in level_counts.most_common():
        lines.append(f"| {level} | {count} |")
    lines.extend(["", "## Status Distribution", "", "| Status | Count |", "|---|---:|"])
    for status, count in status_counts.most_common():
        lines.append(f"| {status} | {count} |")
    lines.extend(["", "## Primary Category Distribution", "", "| Category | Count |", "|---|---:|"])
    for category, count in category_counts.most_common():
        lines.append(f"| {category} | {count} |")
    lines.extend(["", "## Reviewed Problems", "", "| # | Status | Score | Level | Confidence | File |", "|---:|---|---:|---|---|---|"])
    for row in reviewed_rows:
        review = reviews[row["number"]]
        lines.append(
            f"| {row['number']} | {row['status']} | {review['score']} | {review['level']} | "
            f"{review['confidence']} | [{row['problem_file']}](../{row['problem_file']}) |"
        )
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "uncategorized"


def split_tags(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()] or ["uncategorized"]


def write_category_reports(rows: list[dict[str, str]], reviews: dict[str, dict]) -> None:
    by_tag: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        for tag in split_tags(row.get("tags", "")):
            by_tag.setdefault(tag, []).append(row)

    CATEGORIES_DIR.mkdir(parents=True, exist_ok=True)
    for tag, members in sorted(by_tag.items(), key=lambda item: slugify(item[0])):
        reviewed = [row for row in members if row["number"] in reviews]
        level_counts = Counter(reviews[row["number"]]["level"] for row in reviewed)
        status_counts = Counter(row["status"] for row in reviewed)
        confidence_counts = Counter(reviews[row["number"]]["confidence"] for row in reviewed)
        scores = [reviews[row["number"]]["score"] for row in reviewed]
        avg = sum(scores) / len(scores) if scores else 0.0
        promising = [
            row
            for row in reviewed
            if reviews[row["number"]]["level"] in {"high_candidate", "medium_candidate"}
        ]

        lines = [
            f"# Category Report: {tag}",
            "",
            "This category report is based on the GPT-5.5 one-problem-per-call review layer.",
            "",
            f"- Reviewed problems in category: {len(reviewed)}",
            f"- Problems without model review: {len(members) - len(reviewed)}",
            f"- Average model score: {avg:.1f}/100",
            f"- Medium-or-above candidates: {len(promising)}",
            "",
            "## Model Level Distribution",
            "",
            "| Level | Count |",
            "|---|---:|",
        ]
        for level, count in level_counts.most_common():
            lines.append(f"| {level} | {count} |")
        lines.extend(["", "## Status Distribution", "", "| Status | Count |", "|---|---:|"])
        for status, count in status_counts.most_common():
            lines.append(f"| {status} | {count} |")
        lines.extend(["", "## Confidence Distribution", "", "| Confidence | Count |", "|---|---:|"])
        for confidence, count in confidence_counts.most_common():
            lines.append(f"| {confidence} | {count} |")
        lines.extend(
            [
                "",
                "## 综合分析",
                "",
                category_synthesis(tag, reviewed, reviews),
                "",
                "## Problems",
                "",
                "| # | Status | Score | Level | Confidence | Primary category | Problem file |",
                "|---:|---|---:|---|---|---|---|",
            ]
        )
        for row in reviewed:
            review = reviews[row["number"]]
            lines.append(
                f"| {row['number']} | {row['status']} | {review['score']} | {review['level']} | "
                f"{review['confidence']} | {row['primary_category']} | "
                f"[{row['problem_file']}](../{row['problem_file']}) |"
            )
        (CATEGORIES_DIR / f"{slugify(tag)}.md").write_text(
            "\n".join(lines) + "\n", encoding="utf-8", newline="\n"
        )


def category_synthesis(tag: str, rows: list[dict[str, str]], reviews: dict[str, dict]) -> str:
    if not rows:
        return "No model-reviewed problems are available for this category."
    level_counts = Counter(reviews[row["number"]]["level"] for row in rows)
    status_counts = Counter(row["status"] for row in rows)
    scores = [reviews[row["number"]]["score"] for row in rows]
    medium_plus = level_counts["high_candidate"] + level_counts["medium_candidate"]
    dominant_status = ", ".join(f"{k}={v}" for k, v in status_counts.most_common(4))
    dominant_levels = ", ".join(f"{k}={v}" for k, v in level_counts.most_common())
    if medium_plus / len(rows) >= 0.4:
        stance = "本类中可工具化推进的候选较多，优先适合做计算实验、证书搜索、形式化复核和小范围定理自动化。"
    elif sum(scores) / len(scores) >= 40:
        stance = "本类整体处于中间地带，AI 更适合先做局部推进、特殊情形和反例搜索，而不是直接宣称完整解决。"
    else:
        stance = "本类整体难度较高，AI 主要价值在于文献整理、定义核对、失败路线排查和辅助验证。"
    return (
        f"`{tag}` 类共有 {len(rows)} 个模型复审问题，状态分布为 {dominant_status}；"
        f"模型等级分布为 {dominant_levels}。平均分为 {sum(scores) / len(scores):.1f}/100。"
        f"{stance} 类别内的 high/medium 问题应优先进入下一步人工复核，因为模型判断的是可推进性，"
        "不是数学定理已经成立。"
    )


def write_overall_report(rows: list[dict[str, str]], reviews: dict[str, dict]) -> None:
    reviewed = [row for row in rows if row["number"] in reviews]
    level_counts = Counter(reviews[row["number"]]["level"] for row in reviewed)
    status_counts = Counter(row["status"] for row in reviewed)
    category_counts = Counter(row["primary_category"] for row in reviewed)
    scores = [reviews[row["number"]]["score"] for row in reviewed]
    promising = [
        row
        for row in reviewed
        if reviews[row["number"]]["level"] in {"high_candidate", "medium_candidate"}
    ]

    lines = [
        "# Overall AI Solvability Review Report",
        "",
        "This report is based on the GPT-5.5 one-problem-per-call review layer.",
        "",
        f"- Reviewed unresolved/semi-open problems: {len(reviewed)}",
        f"- Remaining without model review: {len(rows) - len(reviewed)}",
        f"- Average model score: {sum(scores) / len(scores):.1f}/100",
        f"- Score range: {min(scores)} to {max(scores)}",
        f"- Medium-or-above candidates: {len(promising)}",
        f"- Detailed model-call report: `reports/model_review_report.md`",
        "",
        "## Model Level Distribution",
        "",
        "| Level | Count |",
        "|---|---:|",
    ]
    for level, count in level_counts.most_common():
        lines.append(f"| {level} | {count} |")
    lines.extend(["", "## Status Distribution", "", "| Status | Count |", "|---|---:|"])
    for status, count in status_counts.most_common():
        lines.append(f"| {status} | {count} |")
    lines.extend(["", "## Primary Category Distribution", "", "| Primary category | Count |", "|---|---:|"])
    for category, count in category_counts.most_common():
        lines.append(f"| {category} | {count} |")
    lines.extend(
        [
            "",
            "## 综合分析",
            "",
            "GPT-5.5 逐题复审后的分布比规则首版更乐观：多数问题落在 `low_to_medium_candidate`，"
            "说明模型认为很多开放题并非完全不可接触，而是可以通过计算实验、形式化复核、特殊情形、"
            "反例搜索或文献路线整理产生研究价值。真正的 `high_candidate` 很少，集中在可有限验证、"
            "可计算搜索或已有明确证书路线的问题；这类问题最适合作为下一步 AI+工具流水线的优先对象。",
            "",
            "低分问题主要来自深数论、渐近估计、素数分布、集合论/独立性或缺乏有限证书入口的题目。"
            "这些题仍可能被 AI 辅助推进，但应把目标设为局部引理、失败路线排查和严格验证，而不是直接求最终证明。",
            "",
            "因此，这个仓库现在可以作为筛选器使用：先看 `reports/model_review_report.md` 中的 high/medium，"
            "再进入对应类别报告，最后打开单题文件查看 GPT-5.5 的支持理由、障碍和验证需求。",
            "",
            "## Medium-Or-Above Candidates",
            "",
            "| # | Status | Score | Level | Confidence | Tags | Problem file |",
            "|---:|---|---:|---|---|---|---|",
        ]
    )
    for row in sorted(promising, key=lambda item: (-reviews[item["number"]]["score"], int(item["number"].split("-")[0]))):
        review = reviews[row["number"]]
        lines.append(
            f"| {row['number']} | {row['status']} | {review['score']} | {review['level']} | "
            f"{review['confidence']} | {row['tags']} | [{row['problem_file']}](../{row['problem_file']}) |"
        )
    OVERALL_REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def update_summary(reviews: dict[str, dict]) -> None:
    summary = json.loads(SUMMARY_JSON.read_text(encoding="utf-8"))
    summary["model_review_count"] = len(reviews)
    summary["model_review_level_counts"] = dict(Counter(review["level"] for review in reviews.values()))
    SUMMARY_JSON.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    rows = read_problem_index()
    reviews = {}
    for row in rows:
        path = review_path(row["number"])
        if path.exists():
            reviews[row["number"]] = json.loads(path.read_text(encoding="utf-8"))
    write_problem_docs(rows, reviews)
    write_index(rows, reviews)
    write_report(rows, reviews)
    write_category_reports(rows, reviews)
    write_overall_report(rows, reviews)
    update_summary(reviews)
    print(f"applied {len(reviews)} model reviews")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
