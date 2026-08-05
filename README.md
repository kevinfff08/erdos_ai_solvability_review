# Erdős Problems AI Solvability Review

这是一个以**研究结果发布**为中心的仓库。它收录 682 道 Erdős 问题的题目页，并发布证据化状态核验、AI 可解答性 V2 评估，以及可独立交给研究 Agent 的任务 prompt。

## 当前快照

- 题目目录：682 题
- 已完成 V2 深度核验：124 题
- 已生成独立研究 prompt：113 份
- 尚未完成 V2 核验：558 题
- 快照日期：2026-08-05

当前快照是**部分覆盖**，不能被解释为 682 题已经全部完成深度核验。旧数据库中的 `open` 标签也不被直接视为“目前仍未解决”的证据。

## 从哪里开始

- [逐题深度核验导航](results/reports/problem_review_index.md) — 已完成 V2 核验的题目及其报告、Prompt 和 JSON 入口
- [本批 20 题筛选与核验结果](results/reports/candidate_selection_2026-08-05.md) — 改进后的三轮筛选及逐题结论
- [当前结果说明](results/README.md)
- [逐题页面](results/problems/)
- [V2 规范 JSON](results/reviews/)
- [独立研究 prompts](results/prompts/)
- [汇总报告](results/reports/)
- [分类报告](results/categories/)
- [可检索索引](results/index/)
- [当前快照清单](results/manifest.json)

其中，`results/reviews/` 与 `results/manifest.json` 是当前 V2 结果的机器可读权威来源；题目页、报告、分类页和索引是便于阅读的发布视图。

## 目录

```text
results/       当前发布结果
source/        题目与索引的来源快照
analysis/      方法说明、schema 与少量参考代码
archive/v1/    旧版 GPT-5.5 评估结果
runtime/       本地运行状态、日志和维护材料（Git 忽略）
```

`archive/v1/` 仅用于保留历史比较，不代表当前问题状态。`analysis/code/` 中的代码用于展示分析方法的实现轮廓，不作为受支持的运行工具。批处理状态、日志、中间结果和维护脚本统一位于本地 `runtime/`，不随仓库发布。

## 如何理解这些结果

V2 会分别审计题面、量词、边界情形、简单反例、历史修订、直接相关论文和当前开放核心。“没有搜索到解答”不会被写成“已经证明仍未解决”；证据不足时使用 `likely_open` 或 `insufficient_evidence`。

AI 可解答性分数只针对核验后仍成立、且被清楚写出的研究目标。`solved`、`disproved`、`invalid_or_trivial` 和 `meta_mathematical` 的 V2 分数固定为 0。分数是研究排序信号，不是数学证明，也不是问题已经被 AI 解出的声明。

独立研究 prompt 只为 `confirmed_open`、`likely_open` 和 `revised_open` 目标发布；关闭、否证、无效、元数学、歧义或证据不足的记录保留审计结果，但不发布 prompt。因此 prompt 数量可以小于 V2 核验数量。

完整的方法、状态定义和证据标准见 [analysis/methodology.md](analysis/methodology.md)。

## 数据来源

基础题目快照来自 [Erdős Problems](https://www.erdosproblems.com/)。每份 V2 记录另外保存了检索日期、来源 URL、作者、日期、来源类型、发表状态、证据直接性及其支持的具体结论。外部网页和论文状态会变化，使用时应以记录中的截止日期为准。
