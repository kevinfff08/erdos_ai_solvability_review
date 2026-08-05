# Problem 742

## 基本信息

- 原始链接: https://www.erdosproblems.com/742
- LaTeX 页面: https://www.erdosproblems.com/latex/742
- 原始状态: `decidable`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $G$ be a graph on $n$ vertices with diameter $2$, such that deleting any edge increases the diameter of $G$. Is it true that $G$ has at most $n^2/4$ edges?

## AI 完成可能性判断

- 结论: **AI+计算/形式化工具有较高机会完成或显著推进**
- 等级: `high_candidate`
- 分数: `70/100`
- 建议路线: 优先将已有有限化归约转成可复现实验、SAT/ILP/穷举或证明助理验证。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：sufficiently large

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: sufficiently large
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **较高候选。给定备注已经说明该命题对充分大的 n 为真，并有 Füredi 1992 的证明；因此 GPT-5.5 级模型更可能通过文献复现、结构化证明整理、形式化关键引理以及有限小规模反例搜索来完成验证或显著推进，而不是从零发明全新极值图论证明。**
- 等级: `high_candidate`
- 分数: `83/100`
- 信心: `medium`
- 可能路线: 最可行路线是先检索并精读备注中指向的 Füredi 证明，抽取其适用阈值、关键结构引理和极值等号情形；随后把“直径 2 且删任一边后直径增大”的条件形式化为可检查谓词。对充分大 n 部分，尝试将文献证明转写为可审计的证明草图或定理证明器中的核心引理；对剩余有限 n，使用图同构剪枝、SAT/ILP 或 nauty/NetworkX/Sage 枚举所有候选图，验证边数不超过 n^2/4 或定位反例。

### 支持理由

- 问题陈述短，定义清晰，适合形式化和程序化检查：图、直径、删边后直径增大、边数上界都可直接编码。
- 备注已给出强外部线索：命题对充分大 n 已由 Füredi 证明，这显著降低了从零发现主证明的难度。
- 极值例子为完全二分图，给出了明确的目标结构和边界值，便于做稳定性分析、等号情形检查和反例搜索。
- 状态标为 decidable，结合“充分大 n 已证”意味着剩余工作很可能可归约为有限检查，适合工具辅助。

### 主要障碍

- Füredi 证明可能包含较精细的极值图论结构分析，模型需要避免把非严格直觉误写成完整证明。
- “充分大 n”的具体阈值未在给定 JSON 中出现；若阈值很大，穷举剩余 n 可能不可行，需要更强的剪枝或补充理论。
- 边临界直径 2 图的候选空间增长很快，朴素枚举会迅速爆炸。
- 若目标是完全形式化证明，图论库中可能缺少现成的直径临界图、极值边界和相关结构引理，需要大量基础铺垫。

### 需要的验证

- 核对 Füredi 1992 证明的精确命题：是否证明所有充分大 n 的精确上界，以及阈值是多少。
- 建立独立的计算验证脚本，确认候选图满足直径 2 和每条边删除后直径增大的条件，而不是只检查弱条件。
- 对小 n 搜索使用同构去重，并保存可复现实验日志、随机种子、版本信息和反例证书格式。
- 若生成形式化证明，需要把文献中的每个关键不等式和结构分类分别形式化验证。

### 公开版思考摘要

这个问题本身是经典的直径 2 边临界图极值问题。给定信息表明，大 n 情况已有证明，因此 GPT-5.5 级模型最现实的贡献不是直接猜出新定理，而是把已有证明变成可审计、可复现、部分形式化的证明链，并用计算补齐或验证有限小规模情形。主要风险在于缺少阈值和原证明细节，以及小 n 枚举的组合爆炸。

### 免责声明

以上是对 AI 工具辅助可解决性和验证路线的评估，不是该 Erdős 问题的数学证明。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_742.md](../../prompts/problem_742.md)

### 状态结论

Füredi 已证明充分大 n，Fan 证明 n≤24 及 n=26，许多结构类也已解决；2025 年论文仍把完整有限 n 版本称为长期猜想。

### 当前规范陈述

设有限图 G 有 n 个顶点、直径为 2，且删除任一边都会增大直径。证明 e(G)≤⌊n²/4⌋，并刻画等号仅由平衡完全二部图取得。

```text
Let G be a finite graph of order n with diameter 2 such that deleting any edge increases its diameter. Prove that e(G)<=floor(n^2/4), with equality only for a balanced complete bipartite graph.
```

### 陈述、量词与反例审计

- 歧义严重度: `none`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 完全二部图给出等号；非二部特殊图的已知界均未超过猜想值。
- 版本变化: 一般上界从 0.27n² 改进；Füredi 解决充分大 n；后续按补图连通度、支配边、禁 C5 等结构推进。

陈述问题：

- n²/4 对奇 n 应解释为整数上界 floor(n²/4)。
- edge-critical 指每条边删除后直径大于 2 或变为不连通。

需要固定的量词/约定：

- G is finite, simple, connected, and diameter-2-edge-critical.
- The equality characterization is part of the strengthened canonical target.

### 文献与当前边界

已核验的主要结果：

- The conjecture holds for all sufficiently large n.
- It holds for n<=24 and n=26.
- It holds for triangle-free graphs and several classes defined by complement connectivity or dominating edges.

最近相关工作：2025 年关于 C5-free diameter-2-critical 图的论文仍称 Murty--Simon 为 longstanding conjecture，并列出剩余一般情形。

剩余核心：关闭有限但未明确列尽的剩余阶数/结构，给出无条件全 n 证明和等号刻画。

已使用方法：

- complement total domination
- injection from edges to missing pairs
- stability and critical graph structure

争议或不确定性：

- Füredi 的‘充分大’阈值与可执行剩余范围需要从原证明准确提取。
- 部分文献只处理偶数阶或补图特定连通度。

### 证据来源

- [Erdős Problem 742](https://www.erdosproblems.com/742) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 742](https://www.erdosproblems.com/latex/742) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [Strengthening the Murty-Simon conjecture on diameter 2 critical graphs](https://arxiv.org/abs/1812.08420) — Antoine Dailly, Florent Foucaud, and Adriana Hansberg; `preprint`, `peer_reviewed`, reliability=`high`. 综述已知一般进展并证明含支配边的非二部情形。
- [Characterize all C5-free diameter-2-critical graphs with many edges](https://www.sciencedirect.com/science/article/pii/S0166218X25003439) — authors listed by the journal; `primary_paper`, `peer_reviewed`, reliability=`high`. 2025 年仍把一般命题称为长期猜想，并推进 C5-free 情形。

### 完成标准

- 肯定出口: Prove the Murty-Simon bound and equality characterization for every n.
- 否定出口: Construct a diameter-2-edge-critical graph with more than floor(n^2/4) edges.

不构成完成：

- Reproving only the sufficiently-large theorem.
- A proof restricted to triangle-free or dominating-edge graphs.
- A graph that is not edge-critical.

正确性陷阱：

- Check deletion of every edge in a counterexample.
- Use floor(n^2/4) for odd n.
- Keep the equality characterization separate from the inequality.

### 更新后的 AI 可解答性

- 等级: `medium_candidate`
- 分数: `54/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- Füredi 的‘充分大’阈值与可执行剩余范围需要从原证明准确提取。
- 部分文献只处理偶数阶或补图特定连通度。

Proof-first 路线：

- 把 Füredi 的稳定性论证有效化并覆盖全部小 n。
- 在补图的全支配临界结构中构造统一注入。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。

<!-- DEEP_REVIEW:END -->
