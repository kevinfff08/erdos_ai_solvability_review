# Erdős Problems AI Solvability Review / Erdős 问题 AI 可完成性审查

Generated: 2026-05-14

## 中文说明

这个仓库整理了 Erdős Problems 数据库中尚未完全解决或处于半开放状态的问题，
并为每个问题生成一份 AI 可完成性评估文档。这里的“AI 可完成性”不是数学证明，
而是判断 GPT-5.5 级别的前沿大模型在配合计算、形式化验证、文献检索和反例搜索工具时，
是否有机会完成、显著推进或验证该问题。

本仓库共审查 `682` 个问题。筛选状态包括：
`open`, `falsifiable`, `verifiable`, `decidable`, `not disprovable`,
`not provable`, `independent`。

### 分类方式

分类遵循原站的 tag 体系。每个问题可能有多个原始标签；为了避免重复文件，
问题文件只按第一个标签放入一个主类别目录：

- `problems/<primary-category>/problem_<number>.md`

同时，所有标签都会进入交叉统计。类别报告位于：

- `categories/<tag>.md`

所以，一个问题即使只存放在主类别目录，也会出现在所有相关标签的类别报告中。

### 重要文件

- 总报告：`reports/overall_repository_report.md`
- 方法说明：`methodology.md`
- 原始快照：`data/source/erdos_problems_full.json`
- 所有问题索引：`data/index/problems_index.csv`
- 类别索引：`data/index/categories_index.csv`
- 每题评估文件：`problems/<primary-category>/problem_<number>.md`
- 一题一调用脚本：`scripts/review_one_problem_with_model.py`

### 每个问题文件包含什么

每个问题文件首先列出原问题、链接、状态、奖金、标签、形式化状态和 OEIS 信息。
然后给出：

- AI 完成可能性结论；
- 分数与等级；
- 建议路线；
- 有利因素；
- 主要障碍；
- 公开版思考过程摘要；
- 触发判断的特征记录。

注意：这些文档不是对开放问题的解答，也不是声称问题已经被 AI 解决。
它们是研究路线筛选工具。

### 关于 GPT-5.5 一题一调用

当前仓库包含完整的首版评估和一个可复跑的一题一调用脚本。
创建本仓库的环境没有可用的 `OPENAI_API_KEY` 或本地 GPT-5.5 代理，
因此没有伪造外部 GPT-5.5 调用记录。若配置 OpenAI 兼容 API，
可以用 `scripts/review_one_problem_with_model.py` 对单题进行真实模型复审。

## English

This repository reviews the unresolved or semi-open entries in the Erdős
Problems database and creates one AI-solvability assessment file per
problem. "AI-solvability" does not mean the problem is solved. It estimates
whether a GPT-5.5-level frontier model, with normal support from computation,
formal verification, literature review, and counterexample search, could
plausibly solve, substantially advance, or verify the problem.

The repository reviews `682` problems with one of these
statuses: `open`, `falsifiable`, `verifiable`, `decidable`,
`not disprovable`, `not provable`, or `independent`.

### Classification

Classification follows the original tag system from erdosproblems.com. A
problem can have multiple tags. To avoid duplicating files, each problem is
stored under its first tag as the primary category:

- `problems/<primary-category>/problem_<number>.md`

Cross-tag membership is still preserved in the category reports:

- `categories/<tag>.md`

Thus a problem has one canonical file but may appear in several category
reports.

### Where To Look

- Overall report: `reports/overall_repository_report.md`
- Methodology: `methodology.md`
- Source snapshot: `data/source/erdos_problems_full.json`
- Problem index: `data/index/problems_index.csv`
- Category index: `data/index/categories_index.csv`
- Per-problem reviews: `problems/<primary-category>/problem_<number>.md`
- One-problem model-call script: `scripts/review_one_problem_with_model.py`

### Repository Contents

Each problem file contains the original statement, source links, status,
prize, tags, formalization metadata, OEIS metadata, an AI-solvability
verdict, score, suggested route, supporting factors, obstacles, public
reasoning summary, and triggered features.

These files are not mathematical solutions. They are a structured research
triage layer for deciding which problems deserve deeper AI-assisted work.

### GPT-5.5 One-Problem Calls

The repository includes a complete first-pass assessment and a script for
live one-problem-per-call review. The creation environment did not expose an
`OPENAI_API_KEY` or a running local GPT-5.5-compatible endpoint, so no
external GPT-5.5 audit is falsely claimed. Configure an OpenAI-compatible API
endpoint and run `scripts/review_one_problem_with_model.py` to replace or
augment individual assessments with live model reviews.
