# Problem 617

## 基本信息

- 原始链接: https://www.erdosproblems.com/617
- LaTeX 页面: https://www.erdosproblems.com/latex/617
- 原始状态: `falsifiable`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $r\geq 3$. If the edges of $K_{r^2+1}$ are $r$-coloured then there exist $r+1$ vertices with at least one colour missing on the edges of the induced $K_{r+1}$.

## AI 完成可能性判断

- 结论: **AI+计算/形式化工具有较高机会完成或显著推进**
- 等级: `high_candidate`
- 分数: `70/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 题面含渐近/无限对象线索：infinitely many

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory
- 证明密集标签命中: 无
- 有限/计算线索: colouring, finite, finitely
- 渐近/无限线索: infinitely many
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。这个问题有清晰的有限组合结构、已形式化、且可被计算反例搜索和小参数验证强力辅助；但原命题是全体 r 的开放型极值图着色断言，已知 r^2 顶点版本在无限多 r 失败，说明临界边界附近存在强代数/设计结构，单靠现有大模型很难直接完成一般证明。GPT-5.5 更可能显著推进结构化归约、验证小 r、排除若干构造族，或把人类证明草稿形式化，而不是独立给出完整通解。**
- 等级: `medium_candidate`
- 分数: `55/100`
- 信心: `medium`
- 可能路线: 最可行路线是把“每个 r+1 点集都见到全部 r 种颜色”的假设转化为强局部覆盖约束：对每种颜色的缺色超图必须没有大小 r+1 的团；再结合颜色类的度数、共同邻域、极值界和设计论结构分析，尝试证明在 r^2+1 个顶点时约束不可同时满足。计算上可用 SAT/CP-SAT/ILP 对小 r 和有对称性的候选构造做穷举，抽取不可满足证书或模式；形式化方面可把归约、计数不等式和小规模证书接入 Lean/Isabelle 作为验证层。

### 支持理由

- 命题表述短且完全有限化：固定 r 后是有限图边着色存在性问题，适合 SAT、约束规划、反例搜索和不可满足证书验证。
- 问题已标记为 formalized=yes，说明至少存在可机检表达或形式化基础，利于 GPT-5.5 辅助补全证明脚本、检查边界条件和验证计算证书。
- 已知 r=3、r=4 成立，且 r^2 顶点版本在无限多 r 失败，这给出明确的临界结构线索；模型可围绕这些极端构造寻找“加一个顶点为何崩溃”的机制。
- 这是图论/设计论风格问题，局部约束强、对象对称性高，适合让模型与计算工具交替生成猜想、搜索最小障碍、提炼结构性引理。

### 主要障碍

- 需要证明所有 r≥3，而不是固定小 r；SAT 或穷举只能覆盖有限参数，除非能提炼出可推广的结构证书。
- r^2 顶点版本对无限多 r 失败，表示临界附近存在高度规则的构造；一般证明必须精确利用 r^2+1 的额外顶点，而粗糙 Ramsey 或 Turán 型界很可能不够。
- 颜色类之间的约束是多色、局部覆盖型，不一定能直接转化为单色图的经典极值问题。
- 若完整证明需要有限几何、设计论或稀疏极值理论中的深引理，模型容易产出看似合理但缺口很大的计数论证。

### 需要的验证

- 对 r=3、r=4 的已知证明做独立复现或形式化核查，确认模型使用的归约没有改变命题。
- 对 r=5、r=6 等小参数运行 SAT/CP-SAT 搜索；若不可满足，应保存 DRAT/LRAT 或等价证书，避免只依赖搜索器结论。
- 系统检查 r^2 顶点反例构造在加入第 r^2+1 个顶点时失败的具体原因，区分偶然小参数现象与可推广障碍。
- 任何一般性计数引理都需要形式化或至少逐行审校，特别是涉及平均度、缺色子集、交集大小和整除条件的步骤。
- 若使用文献检索，应只围绕 Erdős-Gyárfás balanced colouring 及相关设计构造核对最新进展，避免把相邻 Ramsey 问题误当作本命题结果。

### 公开版思考摘要

该问题不像纯存在性反例题那样只需一次搜索即可结束；它要求全参数证明。但它的有限约束形式非常适合机器参与：固定 r 可编码，局部缺色条件可自动检查，小参数和对称构造可被系统探索，形式化状态也降低了验证成本。真正困难在于把临界 r^2 与 r^2+1 的差异提升成一般定理。综合来看，GPT-5.5 有现实机会给出可审计的中间成果或验证人类证明片段，但独立完成完整证明的把握只属中等。

### 免责声明

以上是 AI 可推进性评估，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_617.md](../../prompts/problem_617.md)

### 状态结论

Erdős--Gyárfás 已证明 r=3,4，且 r^2 版本对无穷多个 r 失败。当前题目页仍把 r^2+1 的全体 r≥3 版本列为可否证开放问题，未发现一般解。

### 当前规范陈述

对每个整数 r≥3，以及 K_{r^2+1} 边的任意 r 着色，证明存在 r+1 个顶点，使其诱导完全图中至少缺少一种颜色。

```text
For every integer r>=3 and every r-colouring of the edges of K_{r^2+1}, prove that some set of r+1 vertices has at least one colour absent from its induced complete graph.
```

### 陈述、量词与反例审计

- 歧义严重度: `none`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: r=2 的失败被明确排除；r^2 个顶点的反例不能直接扩张到 r^2+1。
- 版本变化: 原论文建立 split/balanced coloring 框架并处理 r=3,4；规范阈值 r^2+1 的一般情形未关闭。

陈述问题：

- “balanced colouring”在本题专指每个 r+1 顶点集都出现全部 r 种颜色的反例着色。
- 结论只要求缺少至少一种颜色，不要求出现单色 K_{r+1}。

需要固定的量词/约定：

- The assertion is universal over all integers r>=3 and all edge colourings.
- The selected r+1 vertices induce all binom(r+1,2) edges.

### 文献与当前边界

已核验的主要结果：

- The conjecture is true for r=3 and r=4.
- Replacing r^2+1 by r^2 fails for infinitely many r.

最近相关工作：2026 年检索到同名 balanced colouring 的其他问题，但未发现直接解决该局部缺色猜想的论文。

剩余核心：排除 K_{r^2+1} 上每个 r+1 点集都看到全部 r 色的边着色。

已使用方法：

- covering designs and local colour incidence
- double counting over colour neighbourhoods
- finite geometry obstruction analysis

争议或不确定性：

- ‘balanced colouring’术语在其他文献中常指全局各色边数相等，容易误检。

### 证据来源

- [Erdős Problem 617](https://www.erdosproblems.com/617) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 617](https://www.erdosproblems.com/latex/617) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [Split and balanced colorings of complete graphs](https://www.sciencedirect.com/science/article/pii/S0012365X98003239) — Paul Erdős and András Gyárfás; `primary_paper`, `peer_reviewed`, reliability=`high`. 提出该平衡着色问题并证明 r=3,4。
- [Erdős Problem 617 LaTeX record](https://www.erdosproblems.com/latex/617) — Thomas F. Bloom; `problem_page`, `database_record`, reliability=`medium`. 当前精确题面仍列为开放，且无已登记完整解答。

### 完成标准

- 肯定出口: Prove the missing-colour conclusion for every r>=3.
- 否定出口: Give one r>=5 and an explicit r-colouring of K_{r^2+1} for which every r+1 vertices see all r colours.

不构成完成：

- Checking only r=5 by an uncertified search.
- A construction on r^2 vertices.
- Global colour balance without the local r+1-vertex property.

正确性陷阱：

- Verify every r+1-subset in a counterexample certificate.
- Track labelled colours and unordered edges.
- Do not import results about a different notion of balanced colouring.

### 更新后的 AI 可解答性

- 等级: `medium_candidate`
- 分数: `64/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- ‘balanced colouring’术语在其他文献中常指全局各色边数相等，容易误检。
- 完整结论仍要求逐项核验全部量词、边界条件和外部定理假设。

Proof-first 路线：

- 把每种颜色的补图视为覆盖 r+1 子集的设计并做交叉计数。
- 分析 r=5 的结构性不可行证书以寻找一般归纳。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。

<!-- DEEP_REVIEW:END -->
