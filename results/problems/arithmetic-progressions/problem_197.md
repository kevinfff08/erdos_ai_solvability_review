# Problem 197

## 基本信息

- 原始链接: https://www.erdosproblems.com/197
- LaTeX 页面: https://www.erdosproblems.com/latex/197
- 原始状态: `open`
- 奖金: `no`
- 主类别: `arithmetic progressions`
- 原始标签: `arithmetic progressions`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Can $\mathbb{N}$ be partitioned into two sets, each of which can be permuted to avoid monotone 3-term arithmetic progressions?

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
- 结论: **中等候选：GPT-5.5 级别模型配合 SAT/SMT 搜索、有限模型实验和形式化证明工具，较可能显著推进该问题的有限版本、构造障碍和候选策略，但直接给出完整无限情形解答的把握不高。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 可行路线是先把问题转化为有限前缀上的二染色加两个可重排线性序约束：每个颜色类都需要存在一个排列，使其中不存在按排列顺序单调出现的三项等差数列。随后用 SAT/CP-SAT 搜索最大可行前缀、不可行证书、极值构型和潜在递推结构；若发现稳定模式，再尝试抽象成无限构造。反方向则可用有限不可满足证书、密度/结构引理和形式化证明辅助，尝试证明任意二划分中至少有一类无法避免。

### 支持理由

- 问题陈述短、结构明确，适合编码为有限组合搜索问题；“formalized: yes”也说明已有形式化入口，利于机器验证局部引理。
- 三集合情形已知可行这一备注暗示二集合是临界边界，有限实验可能揭示为什么二色失败或如何接近三色构造。
- 重排条件把普通等差数列问题转成“集合是否存在避开模式的线性序”问题，适合用 SAT、约束规划、MILP 或反例搜索探索。
- GPT-5.5 可在工具协作下生成编码、搜索小规模实例、提取模式，并把实验结果转成可验证猜想或 Lean/Isabelle 风格引理。

### 主要障碍

- 无限自然数划分需要全局构造或全局不可能性证明，有限前缀可行性不一定能外推。
- “存在一个排列避免单调三项等差数列”是二阶性质，同时涉及划分和两个排列，搜索空间增长很快。
- 若答案为否，可能需要新的 Ramsey 型或偏序维数型结构定理；若答案为是，则需要非常精细的无限递推构造。
- 三色可行并不直接给出二色策略，临界情形可能对小规模计算模式非常不稳定。

### 需要的验证

- 精确定义“monotone 3-term arithmetic progression”在形式化版本中的含义，并确保有限编码完全一致。
- 对有限前缀搜索结果生成可独立复查的 UNSAT 证书或可验证排列证书。
- 测试候选构造在递增长度上的稳定性，避免只拟合小规模实例。
- 若提出无限证明，需要在证明助手中形式化核心归纳、紧致性或极限论证，并检查是否从有限版本合法推出原问题。
- 需要单独验证三集合可行备注是否被正确理解，避免把已知三色构造错误压缩成二色构造。

### 公开版思考摘要

这个问题对 AI 友好的部分在于约束清晰、形式化状态已存在，并且可以自然拆成有限搜索、证书验证和结构猜想提取。但核心难点是从有限前缀和实验模式跨越到自然数全集上的二划分定理。GPT-5.5 级别系统较可能产出可靠的有限边界、候选构造、不可行证书或辅助引理；完整解决仍需要强组合洞察，因此评为中等候选而非高候选。

### 免责声明

以上是对 GPT-5.5 配合工具推进该问题可能性的审查，不是该 Erdős 问题的解答，也不声称给出了二划分或不可能性证明。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_197.md](../../prompts/problem_197.md)

### 状态结论

三集合版本已知可行，两集合版本仍被直接记录为开放；关键是“每个集合存在某种排列”，不是所有排列。

### 当前规范陈述

能否把自然数分成互不相交的 A、B，使 A 与 B 各自都存在一个双射排列，且不含单调非平凡三项等差数列？

```text
Can N be partitioned into two disjoint sets A and B such that each of A and B admits a bijective ordering with no monotone nonconstant three-term arithmetic progression?
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 三色构造不能通过简单合并推出二色；未发现显然的二色反例或构造。
- 版本变化: 已知允许三个部分时可以做到。

陈述问题：

- 必须区分集合分拆与随后对各部分选择排列。
- 避免条件只针对所选排列中的单调三项 AP。

需要固定的量词/约定：

- There exists a partition and, independently for each part, there exists a bijective ordering.
- The arithmetic progression has nonzero common difference.

### 文献与当前边界

已核验的主要结果：

- 三部分分拆版本可行。
- 没有列出的二部分完整构造或不可能性定理。

最近相关工作：题目页当前无解答主张；后续精确检索未发现关闭二色版本的直接来源。

剩余核心：构造二分及两套避免排列，或证明任意二分至少一部分不可如此排列。

已使用方法：

- 递归分块与跨块 AP 控制。
- 把可排列性转译为有向约束图的拓扑排序。

争议或不确定性：

- 原题缺少参考文献细节。
- 三色结果的具体构造需要在使用时回查。

### 证据来源

- [Erdős Problem 197](https://www.erdosproblems.com/197) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 197](https://www.erdosproblems.com/latex/197) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。

### 完成标准

- 肯定出口: Give an explicit partition N=A disjoint-union B and explicit bijective orderings of both parts, with a proof that neither ordering contains a monotone three-term progression.
- 否定出口: Prove that for every two-colouring of N, at least one colour class has no ordering avoiding monotone three-term progressions.

不构成完成：

- The known partition into three sets.
- A finite partition or non-surjective enumeration.
- Avoiding only consecutive-index progressions.

正确性陷阱：

- Quantify over every triple of positions, not only adjacent positions.
- Verify each ordering uses every element exactly once.
- Cross-block progressions must be audited in recursive constructions.

### 更新后的 AI 可解答性

- 等级: `medium_candidate`
- 分数: `50/100`
- 信心: `medium`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 建立可避免排列的集合刻画或充分条件。
- 尝试兼容的二进制分层构造并逐类排除跨层 AP。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
