# Problem 885

## 基本信息

- 原始链接: https://www.erdosproblems.com/885
- LaTeX 页面: https://www.erdosproblems.com/latex/885
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `divisors`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

For integer $n\geq 1$ we define the factor difference set of $n$ by\[D(n) = \{\lvert a-b\rvert : n=ab\}.\]Is it true that, for every $k\geq 1$, there exist integers $N_1<\cdots<N_k$ such that\[\lvert \cap_i D(N_i)\rvert \geq k?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `29/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：divisors, number theory
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: divisors, number theory
- 有限/计算线索: 无
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **这是一个中等偏高候选问题：GPT-5.5 级别模型不应被预期直接给出完整无条件证明，但有现实机会通过计算搜索、代数曲线/丢番图系统化、以及形式化验证来显著推进若干新的 k 或构造族。**
- 等级: `medium_candidate`
- 分数: `66/100`
- 信心: `medium`
- 可能路线: 把公共差值集合固定为 d_1,...,d_k 后，将条件 d_j \in D(N_i) 改写为 N_i=x_{ij}(x_{ij}+d_j)，或等价地 4N_i+d_j^2 为平方。AI 可先用 SAT/SMT、枚举、椭圆曲线/超椭圆曲线工具寻找小 k 的新构造和参数族；再尝试把多重因子差问题转成若干平方差同时成立的丢番图系统，寻找可无限生成至少 k 个 N_i 的结构性模板。已有 k=2,3,4 的正例说明低维情形存在可验证构造，适合模型从形式化条目和计算证据中反推一般机制。

### 支持理由

- 问题陈述短、定义离散且可完全计算，D(n) 的成员判定可化为简单平方条件，适合自动枚举、反例搜索和形式化校验。
- 目标是存在性构造而非全称分类；若能找到可参数化的构造族，就可能绕开对所有 n 的困难结构分析。
- 已知 k=2,3,4 成立，提示问题至少在小规模上有可扩展的代数模式可挖掘，AI 工具链可用于模式发现。
- 形式化状态为 yes，意味着已有机器可读表述或相关形式化基础，便于验证有限构造、辅助定理和搜索输出。
- 该问题与因子对差值、平方差、同时二次表示直接相关，现有计算数论工具可对候选系统做曲线化简、局部可解性检查和有理点搜索。

### 主要障碍

- 从任意固定 k 推到所有 k 需要统一构造；小 k 的偶然代数恒等式可能无法自然推广。
- 公共交集要求同一批差值同时出现在 k 个不同整数的因子差集中，本质上是高维丢番图约束，维数随 k 增长而迅速变复杂。
- 计算搜索容易发现零散样例，但从样例提炼出可证明的无限或任意 k 构造需要较强的人类式结构洞察。
- 若一般情形需要深层椭圆曲线、代数簇有理点、或组合数论输入，当前模型可能会产生看似合理但难以闭合的证明。
- 形式化验证能检查候选证明局部步骤，但很难替代发现核心构造的过程。

### 需要的验证

- 对 k=2,3,4 的已知构造进行独立复现，确认工具链和等价改写没有偏差。
- 建立可审计搜索程序：给定 k 和范围，输出 N_i、公共 d 值、对应因子对，并由独立脚本验证所有等式。
- 若提出参数族，需要用计算代数系统验证恒等式，并检查参数取值下 N_1<...<N_k、正整数性、差值互异性和交集大小。
- 对任何归纳或递归构造，需形式化证明递推不会引入退化项，例如重复 N_i、重复差值、负因子或非整数因子。
- 最终证明若声称解决全体 k，应在 Lean/Isabelle 或等价证明检查环境中至少形式化核心构造与 D(n) 成员性验证。

### 公开版思考摘要

我将该问题视为适合 AI 显著推进但不稳妥保证解决的候选。核心原因是定义可计算、存在性目标可能由显式构造完成，并且平方条件提供了清晰的代数入口；同时，任意 k 的统一构造很可能隐藏在高维丢番图结构中，超出单纯枚举和局部形式化验证的能力。

### 免责声明

以上是对 GPT-5.5 级别模型可推进性的审查，不是该 Erdős 问题的解答，也未声称给出了新的构造或证明。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_885.md](../../prompts/problem_885.md)

### 状态结论

k=2,3,4 已有同行评议构造；一般 k 仍有直接开放记录，且存在明确代数化入口。

### 当前规范陈述

对 n≥1 定义 D(n)={|a−b|: a,b 为正整数且 ab=n}。证明或否定：每个 k≥1 都存在互异 N_1<…<N_k，使 D(N_1)∩…∩D(N_k) 至少含 k 个元素。

```text
For n>=1 define D(n)={|a-b|: a,b are positive integers and ab=n}. Prove or disprove that for every k>=1 there exist distinct integers N_1<...<N_k with |D(N_1)∩...∩D(N_k)|>=k.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 小 k 构造支持而非解决一般命题；未发现一般 k 的简单障碍。
- 版本变化: Erdős–Rosenfeld、Jiménez-Urroz、Bremner 依次解决 k=2,3,4。

陈述问题：

- 因子 a,b 取正整数。
- D(n) 是集合，交换因子不重复计数，0 可在平方数时出现。

需要固定的量词/约定：

- The assertion is for every positive integer k.
- The N_i are pairwise distinct and strictly increasing.

### 文献与当前边界

已核验的主要结果：

- k=2 成立。
- k=3 成立。
- k=4 成立。

最近相关工作：Bremner 2019 给 k=4 的同行评议结果；题目页当前无进一步解答主张。

剩余核心：建立对任意 k 可扩展的共同因子差构造，或证明某个 k 不可能。

已使用方法：

- 等价平方条件 4N_i+d_j^2 为平方。
- 联立二次曲线、椭圆曲线与参数化。

争议或不确定性：

- 已有低 k 构造未显现统一递归。
- 本地实验中的来源外推导不能作为全球新颖性或开放状态证据。

### 证据来源

- [Erdős Problem 885](https://www.erdosproblems.com/885) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 885](https://www.erdosproblems.com/latex/885) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。

### 完成标准

- 肯定出口: Give a construction valid for every k and prove all N_i are distinct positive integers and at least k explicitly identified differences lie in every D(N_i).
- 否定出口: Give a specific k and prove that no k integers can have k common factor differences.

不构成完成：

- Another isolated construction for fixed small k.
- Numerical examples without a scalable proof.
- Counting repeated or signed differences as distinct.

正确性陷阱：

- Require positive integer factor pairs.
- Verify the same k distinct differences work for every N_i.
- Do not infer global novelty from absence in the frozen sources.

### 更新后的 AI 可解答性

- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 把 d_j∈D(N_i) 统一转写为 4N_i+d_j^2 平方。
- 寻找能随 k 扩张的二次曲面或递归参数族。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
