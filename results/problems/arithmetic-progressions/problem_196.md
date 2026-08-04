# Problem 196

## 基本信息

- 原始链接: https://www.erdosproblems.com/196
- LaTeX 页面: https://www.erdosproblems.com/latex/196
- 原始状态: `open`
- 奖金: `no`
- 主类别: `arithmetic progressions`
- 原始标签: `arithmetic progressions`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Must every permutation of $\mathbb{N}$ contain a monotone 4-term arithmetic progression? In other words, given a permutation $x$ of $\mathbb{N}$ must there be indices with either $i<j<k<l$ or $i>j>k>l$ such that $x_i,x_j,x_k,x_l$ are an arithmetic progression?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `32/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：arithmetic progressions
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: arithmetic progressions
- 有限/计算线索: 无
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。这个问题表述短、结构离散、已形式化，适合 GPT-5.5 结合 SAT/CP 搜索、构造搜索和形式化验证来显著推进；但完整解决仍有明显难度，因为核心是无限排列中的全局顺序约束，有限实验到无限结论之间存在非平凡缺口。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 较现实的路线是把排列看作自然数上的位置顺序，对所有 4 项等差数列禁止其位置顺序完全递增或完全递减；先建立有限版本的精确 SAT/CP 编码，搜索大规模有限避免例或最小不可避免规模，再从极值结构中提取递归构造、自动序列式构造或可形式化的有限不可满足证书。若发现有限不可满足边界，需要把 SAT 证书或组合推理压缩成可检查证明；若发现稳定构造族，则需要证明其扩展为真正的自然数排列并保持所有 4 项等差数列非单调。

### 支持理由

- 问题具有很强的可计算化结构：对象是排列，禁忌模式是 4 项等差数列上的两种单调位置顺序，天然适合约束求解、枚举和反例搜索。
- 已标记为 formalized=yes，这降低了语义误读风险，也使得候选证明或反例构造更容易进入 Lean/Isabelle 等形式化验证流程。
- 备注中给出的已知边界显示 3 项必然、5 项不必然，说明 4 项是一个精确临界情形；这类问题常能通过计算实验发现强结构或有限证书。
- GPT-5.5 级模型可以在编码、实验设计、搜索剪枝、结构猜想、证明草图生成和形式化验证之间迭代，比较适合这种离散组合问题的工具增强工作流。

### 主要障碍

- 有限排列搜索结果未必直接推出无限自然数排列的结论；需要严谨处理有限一致性、紧致性、以及排列位置顺序必须是 omega 型枚举这一点。
- 若目标是证明必然存在，可能需要非常大的有限不可满足证书或新的组合不变量，单靠暴力搜索很可能不可扩展。
- 若目标是反例，构造必须是整个自然数的双射，而不只是越来越长的有限避免排列；递归构造还必须保证跨块的等差数列不会产生单调 4 项模式。
- 4 项等差数列约束分布稠密且相互耦合，SAT/CP 搜索可能迅速遇到规模瓶颈，启发式结果也容易产生误导。

### 需要的验证

- 明确形式化定义：x_i,x_j,x_k,x_l 是等差数列时，其项序是否按给出的顺序对应等差数列的自然顺序，并确认单调性是在索引位置上判断。
- 为有限版本建立独立双实现，例如 SAT 编码与 CP-SAT/回溯搜索互相核对，避免编码错误。
- 若得到不可满足结果，需要导出可复查证书，并尽量压缩为人类可读或形式化证明。
- 若得到反例构造，需要证明它是自然数的排列，并对任意起点和公差的 4 项等差数列验证位置顺序不完全递增也不完全递减。
- 把任何实验性结构猜想转化为可验证的引理链，而不是只报告最大规模搜索记录。

### 公开版思考摘要

该问题对 AI 工具链友好，因为它可以被精确编码为排列顺序上的局部禁忌约束，并且形式化状态已存在；GPT-5.5 很可能能产出有价值的有限搜索、候选构造、不可满足证书或形式化辅助证明。不过，问题的真正难点在于从有限计算跨越到无限排列，或构造一个全局双射并控制所有跨尺度等差数列。因此我判断它不是低希望问题，但也不是仅靠当前模型常规推理即可解决的问题。

### 免责声明

以上是对 GPT-5.5 配合工具解决或推进该问题可行性的审查，不是该 Erdős 问题的数学解答，也不声称给出了证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_196.md](../../prompts/problem_196.md)

### 状态结论

三项版本必然出现、五项版本可避免；四项临界情形仍有直接开放记录且题面可规范化。

### 当前规范陈述

每个自然数排列 x:N→N 是否都含有四个递增指标 i1<i2<i3<i4，使对应数值按递增或递减顺序构成四项等差数列？

```text
Does every bijection x:N->N contain four distinct indices i1<i2<i3<i4 such that x_{i1},x_{i2},x_{i3},x_{i4} form a four-term arithmetic progression in increasing or decreasing order?
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 已知可避免五项单调等差数列的排列不自动反驳四项版本。
- 版本变化: DEGS 证明每个排列含单调三项 AP，并构造避免单调五项 AP 的排列。

陈述问题：

- 原题用 i>j>k>l 的写法等价于递增指标下数值递减，应统一表述。
- 四项等差数列公差须非零。

需要固定的量词/约定：

- x is a bijection of positive integers.
- The four values are a nonconstant arithmetic progression in either order.

### 文献与当前边界

已核验的主要结果：

- 单调三项 AP 对所有排列不可避免。
- 存在避免单调五项 AP 的自然数排列。

最近相关工作：未检得关闭四项临界情形的可核验后续工作；题目页无评论解答主张。

剩余核心：决定单调四项 AP 在自然数排列中是否不可避免。

已使用方法：

- 有限避免排列的扩张与紧致性。
- 排列模式、染色和区间分块递归。

争议或不确定性：

- 文献线索主要集中于 1977/78 原论文。
- 形式化陈述存在但不等于证明。

### 证据来源

- [Erdős Problem 196](https://www.erdosproblems.com/196) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 196](https://www.erdosproblems.com/latex/196) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。

### 完成标准

- 肯定出口: Prove that every permutation of N contains a monotone nonconstant four-term arithmetic progression.
- 否定出口: Construct and rigorously verify a permutation of N containing no monotone four-term arithmetic progression.

不构成完成：

- Reproving the three-term theorem.
- Constructing a permutation avoiding only five-term progressions.
- Finite permutations of growing length without a compatible infinite limit.

正确性陷阱：

- Preserve bijectivity in any infinite construction.
- A decreasing progression is tested in increasing index order.
- A compactness argument must preserve all finite avoidance constraints.

### 更新后的 AI 可解答性

- 等级: `medium_candidate`
- 分数: `52/100`
- 信心: `medium`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 抽取有限临界排列的结构并证明不可无限扩张。
- 设计递归块排列并验证跨块四项 AP。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
