# Problem 628

## 基本信息

- 原始链接: https://www.erdosproblems.com/628
- LaTeX 页面: https://www.erdosproblems.com/latex/628
- 原始状态: `falsifiable`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `chromatic number`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: Erdős-Lovász Tihany Conjecture

## 原问题

Let $G$ be a graph with chromatic number $k$ containing no $K_k$. If $a,b\geq 2$ and $a+b=k+1$ then must there exist two disjoint subgraphs of $G$ with chromatic numbers $\geq a$ and $\geq b$ respectively?

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `69/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 主要风险是候选证明或计算证书容易存在隐藏漏洞，需要独立复核。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: chromatic number, graph theory
- 证明密集标签命中: 无
- 有限/计算线索: chromatic, graph
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能直接完成一般情形，但有较现实的机会在小参数、特殊图类、反例搜索和形式化验证方面显著推进。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 较可行的路线不是从零给出完整证明，而是把问题转化为关于 k-临界无 K_k 图的有限/半有限搜索与结构归纳：先用 SAT/ILP/图生成器检验小 k 和固定 a,b 的极小反例；再结合已知部分结果中暗示的图类，如准线图和独立数为 2 的图，尝试抽取可形式化的可约构型；最后用 Lean/Isabelle 或专用图论证明脚本验证小定理、归纳步骤和计算证书。

### 支持理由

- 命题形式清楚，参数有限，天然适合最小反例、k-临界图和禁止团约束的机器搜索。
- 目标是存在两个不交子图且色数分别达到阈值，可被编码为染色不可满足性、顶点划分约束或证书搜索问题。
- 备注显示已有非平凡部分结果，包括 a=b=3、准线图、独立数为 2 的图，这为 AI 提供了可复用的证明模板和局部结构线索。
- 问题没有形式化，GPT-5.5 配合证明助手可在定义、等价改写、已知小情形验证和计算证书检查方面产生实际价值。
- 即使不能解决一般猜想，模型也可能发现新的小参数验证、特殊图类扩展、错误候选反例排除或可约配置库。

### 主要障碍

- 这是 Erdős-Lovász Tihany 猜想的一般形式，长期只有部分结果，说明核心结构障碍很强。
- 色数约束本身计算复杂，极小反例搜索会迅速受到图规模、同构去重和染色判定复杂度限制。
- 存在性结论涉及两个不交高色数子图，比单纯找染色或团结构更难编码和抽象。
- 已知部分结果可能依赖深图论结构定理，GPT-5.5 容易在归纳或极小反例论证中产生不可验证的跳步。
- 如果反例不存在，纯计算只能给出有限范围验证，难以自动外推到一般 k。

### 需要的验证

- 明确把问题限制到 k-临界且无 K_k 的图，并证明该归约不损失一般性。
- 为固定 k,a,b 建立可复现实验：图生成、无 K_k 检查、色数验证、不可分割性检查和同构去重。
- 对任何声称的新反例给出机器可检查证书，包括 chromatic number 为 k、clique number 小于 k、以及不存在所需两不交子图。
- 对任何声称的新证明步骤进行形式化或至少独立证明审查，尤其是极小反例删除、收缩和分裂操作。
- 与备注中提到的已知部分结果保持一致，避免重复证明已知情形或错误覆盖已知例外。

### 公开版思考摘要

该问题对 AI 友好的地方在于定义短、有限、可计算，并且反例搜索和小情形验证有明确入口；不利之处在于它是著名开放图论猜想的一般形式，核心难点并非缺少计算，而是需要深结构证明。GPT-5.5 级模型更可能作为计算实验、形式化验证和局部定理生成的工具，而不是独立完成完整猜想。

### 免责声明

以上只是对 AI 可推进性的审查，不是该 Erdős 问题的证明、反例或解答。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_628.md](../../prompts/problem_628.md)

### 状态结论

该规范形式仍是 Erdős--Lovász Tihany 猜想。2026 年最新预印本证明 even-hole-free 图等新类别，但没有覆盖一般图。

### 当前规范陈述

设有限图 G 满足 ω(G)<χ(G)=a+b-1，且 a,b≥2。证明可把 V(G) 分为不交的 A,B，使 χ(G[A])≥a、χ(G[B])≥b。

```text
Let G be a finite graph with clique number omega(G)<chi(G)=a+b-1, where a,b>=2. Prove that V(G) can be partitioned into disjoint sets A,B such that chi(G[A])>=a and chi(G[B])>=b.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 已知 (3,3) 及若干参数/图类成立；这些不构成一般反例或一般证明。
- 版本变化: Brown--Jung 处理 (3,3)；quasi-line、α=2、若干 forbidden-hole 和 claw-free 情形已知。

陈述问题：

- 题面写‘disjoint subgraphs’可等价规范为顶点划分，因为剩余顶点可任意分配且染色数不会下降。
- 条件应写 ω(G)<χ(G)，等价于不含 K_{χ(G)}。

需要固定的量词/约定：

- Graphs are finite and simple.
- The chromatic thresholds concern induced subgraphs on a vertex partition.

### 文献与当前边界

已核验的主要结果：

- The conjecture holds for quasi-line graphs and graphs with independence number 2.
- Several fixed parameter pairs and forbidden-hole classes are known.
- A July 2026 preprint proves the conjecture for all even-hole-free graphs.

最近相关工作：Song, arXiv:2607.20376，利用 even-hole-free 图的 bisimplicial vertex 结构证明该大类，但摘要仍明确一般命题为猜想。

剩余核心：从特殊图类推广到任意不完美图，或找到一个有限不可分图作为反例。

已使用方法：

- critical graph reductions
- bisimplicial vertices and decomposition theorems
- double-critical colouring structure

争议或不确定性：

- 最新结果是很新的预印本。
- 一般猜想包含多个著名困难图着色问题的结构。

### 证据来源

- [Erdős Problem 628](https://www.erdosproblems.com/628) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 628](https://www.erdosproblems.com/latex/628) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [Erdős Problem 628 discussion](https://www.erdosproblems.com/forum/thread/628?order=newest) — Thomas F. Bloom and contributors; `forum`, `preprint`, reliability=`medium`. 记录 2022 综述及 2024 年新特例，主状态仍开放。
- [The Erdős-Lovász Tihany Conjecture holds for all even-hole-free graphs](https://arxiv.org/abs/2607.20376) — Zi-Xia Song; `preprint`, `preprint`, reliability=`high`. 证明 even-hole-free 图情形，并明确一般命题仍为猜想。

### 完成标准

- 肯定出口: Prove the stated splitting theorem for all finite graphs.
- 否定出口: Construct a finite graph and parameters a,b satisfying the hypotheses but admitting no such partition.

不构成完成：

- Proofs for claw-free, quasi-line, even-hole-free, or alpha=2 graphs only.
- A relaxed result using colouring number instead of chromatic number.
- Two subgraphs that overlap in vertices.

正确性陷阱：

- Preserve the equality chi(G)=a+b-1.
- Verify both induced chromatic lower bounds.
- Do not assume a bisimplicial vertex exists in arbitrary graphs.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- 最新结果是很新的预印本。
- 一般猜想包含多个著名困难图着色问题的结构。

Proof-first 路线：

- 研究最小反例的双临界结构与可分顶点。
- 寻找可替代 bisimplicial vertex 的一般分解。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。

<!-- DEEP_REVIEW:END -->
