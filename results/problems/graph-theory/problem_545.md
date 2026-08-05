# Problem 545

## 基本信息

- 原始链接: https://www.erdosproblems.com/545
- LaTeX 页面: https://www.erdosproblems.com/latex/545
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`
- 形式化状态: `no`
- OEIS: `A059442`, `possible`
- 原站备注字段: 无

## 原问题

Let $G$ be a graph with $m$ edges and no isolated vertices. Is the Ramsey number $R(G)$ maximised when $G$ is 'as complete as possible'? That is, if $m=\binom{n}{2}+t$ edges with $0\leq t<n$ then is\[R(G)\leq R(H),\]where $H$ is the graph formed by connecting a new vertex to $t$ of the vertices of $K_n$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `45/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 题面含渐近/无限对象线索：o(

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: graph, ramsey
- 渐近/无限线索: o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **按给定 JSON 的字面命题看，已有备注指出小 m 存在反例，因此 GPT-5.5 配合小规模 Ramsey 数计算、图枚举和形式化核验，很可能能够完成“字面命题为假”的验证；但若研究目标改成排除小例外后的大 m 结构性最大化命题，则仍是高难度开放问题，只能期望显著推进局部范围或生成可验证猜想。**
- 等级: `high_candidate`
- 分数: `82/100`
- 信心: `medium`
- 可能路线: 最可行路线是把字面命题转化为有限反例验证：对给定 m 枚举无孤立点图 G，构造对应的“尽量完全”图 H，使用 Ramsey 数精确搜索或 SAT/SMT 编码验证 R(G)>R(H) 的小规模反例，并给出可独立复核的证书。若进一步研究修正版，则可用计算搜索寻找例外边界、归纳候选极值图，并结合已知 Ramsey 上下界技术尝试证明大 m 情形。

### 支持理由

- 问题的 JSON 备注已经明确说该断言在若干小 m 区间失败，所以字面问题不需要突破全新理论即可被反例处理。
- 小边数图的枚举、同构去重、Ramsey 数上下界搜索和 SAT 证书验证都属于现有工具可覆盖的任务，适合 GPT-5.5 级模型组织自动化流程。
- H 的构造非常明确：m=binom(n,2)+t 时由 K_n 加一个与 t 个旧顶点相连的新顶点组成，便于程序化生成和比较。
- 该问题若转向“除小反例外是否成立”或“渐近最大化是否成立”，模型仍可通过系统实验提出边界猜想、候选反例族和证明路线，构成显著推进。

### 主要障碍

- 一般图 Ramsey 数计算增长极快，超过小 m 后精确验证会迅速变得困难。
- 字面命题已被备注中的小反例否定，但问题状态仍为 open，说明真正关心的可能是修正后的版本；JSON 没有给出精确定式。
- 要证明大范围结构性最大化，需要统一控制所有 m 边无孤立点图的 Ramsey 数，而不是只验证有限图表。
- 若依赖计算反例，必须提供可复核证书，否则难以作为数学完成。

### 需要的验证

- 明确审查目标是字面命题、排除小 m 后命题，还是某个渐近/修正版命题。
- 对备注中提到的 m 区间进行独立图枚举，列出具体反例 G、对应 H、以及 R(G)>R(H) 的证据。
- 用至少两种独立方法核验小规模 Ramsey 数，例如精确搜索加 SAT 证书，或枚举程序加形式化 checker。
- 若提出大 m 猜想，需要给出搜索覆盖范围、同构去重方法、下界染色证书和上界证明/证书。

### 公开版思考摘要

该问题的关键不是直接求 R(G) 的一般公式，而是判断“边数固定时最稠密团状图是否总是最坏”。给定 JSON 已说明小 m 有失败案例，因此 GPT-5.5 最有希望完成的是对字面命题的反例核验与可复现证书生成。若把问题解释为去除小例外后的开放结构命题，则难度显著上升，但模型仍可能通过计算实验和候选定理形式化显著推进。

### 免责声明

这不是该 Erdős 问题修正版的数学解答；这里只评估 GPT-5.5 级模型在工具辅助下对字面命题或可能修正版进行完成、推进与验证的可行性。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `revised_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_545.md](../../prompts/problem_545.md)

### 状态结论

原始对所有 m 的断言已有小 m 反例，不能继续作为开放猜想。较自然的现行目标是充分大 m 的版本或完整极值分类；一般上界 2^{O(sqrt m)} 已由 Sudakov 证明，但远弱于确定极值图。

### 当前规范陈述

对充分大的 m，写 m=C(n,2)+t（0≤t<n），令 H_m 为 K_n 加一个与其中 t 个顶点相邻的新顶点。判定每个无孤立点、恰有 m 条边的图 G 是否满足 R(G)≤R(H_m)，并更一般地确定固定边数下 Ramsey 数的极大图。

```text
For each sufficiently large m, write m=binom(n,2)+t with 0<=t<n and let H_m be K_n plus one new vertex adjacent to t clique vertices. Determine whether every graph G with m edges and no isolated vertices satisfies R(G)<=R(H_m); more generally determine the maximizers of R(G) at fixed m.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `counterexample_found`
- 检查说明: 题目页记录 2≤m≤5 及 7≤m≤9 的反例，因此原始全称断言为假。
- 版本变化: Sudakov 解决了相关的统一指数上界；固定边数下精确极大者的原断言需排除小 m 或改为分类。

陈述问题：

- 必须明确 Ramsey 数为二色对角 Ramsey 数。
- 小 m 反例迫使目标加‘充分大’或改为分类问题。

需要固定的量词/约定：

- G is finite, simple, and has no isolated vertices.
- The revised asymptotic target quantifies over all sufficiently large edge counts m.

### 文献与当前边界

已核验的主要结果：

- Sudakov proved R(G)<=2^{O(sqrt(m))} for every m-edge graph without isolated vertices.
- The proposed almost-complete maximizer fails for several small edge counts.

最近相关工作：2024 年 ordered Ramsey 论文仍以 Erdős--Graham 的无序固定边数问题为动机；未发现充分大 m 极值分类。

剩余核心：证明 almost-complete 图从某个阈值起极大，或识别无限反例族并给出正确极值结构。

已使用方法：

- Ramsey stability around cliques
- comparison inequalities under edge compression and symmetrization

争议或不确定性：

- R(H_m) 本身通常未知，使直接比较困难。
- 充分大版本是合理修订，但未必是文献中唯一公认的修订。

### 证据来源

- [Erdős Problem 545](https://www.erdosproblems.com/545) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 545](https://www.erdosproblems.com/latex/545) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [A conjecture of Erdős on graph Ramsey numbers](https://arxiv.org/abs/1002.0095) — Benny Sudakov; `preprint`, `peer_reviewed`, reliability=`high`. 证明固定边数图的 2^{O(sqrt m)} 统一上界，但不确定精确极值图。
- [Erdős Problem 545](https://www.erdosproblems.com/545) — Thomas F. Bloom; `problem_page`, `database_record`, reliability=`medium`. 记录原猜想、相关上界以及若干小 m 反例。

### 完成标准

- 肯定出口: Prove the revised eventual extremal statement and identify an explicit or effective threshold.
- 否定出口: Construct infinitely many m and m-edge graphs G with R(G)>R(H_m), or give a corrected extremal family.

不构成完成：

- Reproving only the bound 2^{O(sqrt(m))}.
- Ignoring the recorded small counterexamples.
- Comparing only orders or clique numbers instead of Ramsey numbers.

正确性陷阱：

- Keep the edge count exactly m.
- Exclude isolated vertices consistently.
- Do not assume Ramsey number is monotone under degree sequence majorization.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `28/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- R(H_m) 本身通常未知，使直接比较困难。
- 充分大版本是合理修订，但未必是文献中唯一公认的修订。

Proof-first 路线：

- 建立接近团图的 Ramsey 稳定性定理。
- 寻找边压缩是否单调提高 Ramsey 数的可证替代命题。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态涉及题面修订、解答声明、低覆盖文献或较新预印本，建议专家重点抽查。

<!-- DEEP_REVIEW:END -->
