# Problem 887

## 基本信息

- 原始链接: https://www.erdosproblems.com/887
- LaTeX 页面: https://www.erdosproblems.com/latex/887
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `divisors`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Is there an absolute constant $K$ such that, for every $C>0$, if $n$ is sufficiently large then $n$ has at most $K$ divisors in $(n^{1/2},n^{1/2}+C n^{1/4})$.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `31/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：divisors, number theory
- 题面含渐近/无限对象线索：infinitely many, sufficiently large

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: divisors, number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: infinitely many, sufficiently large
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **GPT-5.5 级别模型配合计算、形式化证明和文献检索，较可能对该问题给出显著推进或验证局部情形，但不宜判断为高概率完整解决。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 可行路线是把每个接近 sqrt(n) 的除数写成一个接近平方的因子分解 n=(N-a_i)(N+b_i)，把多个除数转化为若干小参数之间的二次型或差平方关系；随后用格点、丢番图近似、gcd 结构、椭圆曲线/高亏格曲线搜索以及形式化不等式验证来排除超过固定数量的配置。模型适合系统化重建 Erdős-Rosenfeld 与 Chan 的参数化方法，自动搜索多除数模式，尝试把“依赖 C 的上界”压缩成“绝对上界”，并验证大量边界配置。

### 支持理由

- 问题陈述短、结构明确，核心对象是 sqrt(n) 附近长度 C n^{1/4} 的除数簇，适合代数参数化和计算搜索。
- 已有结果已经给出 1+C^2 的上界、平方 n 情形的常数上界，以及若 n 接近两小偏移因子的情形的常数上界，说明问题存在可分解的局部结构，而不是完全无抓手。
- “formalized: yes”降低了验证门槛：若模型提出关键引理或有限配置归约，Lean/Isabelle 等工具可用于检查不等式、整除关系和归约步骤。
- 反例搜索也很有价值：若不存在绝对 K，必须构造固定 C 下任意多的接近 sqrt(n) 除数；这种结构可用 SAT/SMT、数论搜索和代数曲线工具进行系统排查。
- 模型可对已有文献中的 Chan 型证明做机械化拆解，寻找哪些步骤只在平方或近平方结构下使用，从而定位可推广的瓶颈。

### 主要障碍

- 完整解决很可能需要新的数论思想，而不只是更强计算；绝对 K 要求消除对 C 的依赖，这是现有 1+C^2 上界的关键缺口。
- 多个接近 sqrt(n) 的因子会产生高度耦合的整除和差平方条件，但参数数量随候选除数数目增加，容易进入难以控制的丢番图系统。
- 已有平方和特殊近平方结果暗示一般 n 的非对称因子结构是主要困难，模型可能只能重现特殊情形而难以跨过一般情形。
- 即使计算没有发现大簇，也不能直接证明绝对上界；需要把搜索转化为可证明的有限归约或通用不等式。
- 若真实最优 K 较大，证明可能需要复杂的分类，AI 生成的分类论证存在遗漏配置的风险。

### 需要的验证

- 先形式化等价变换：除数 d in (sqrt(n), sqrt(n)+C n^{1/4}) 与接近平方因子对之间的精确不等式关系。
- 复现 remarks 中提到的 1+C^2 上界和 Chan 的平方情形核心引理，确认模型没有误用已知结论。
- 对 k=5,6,7 等多除数配置做符号消元和大规模搜索，记录是否出现无限族候选或只出现有限小 n 例外。
- 若提出常数 K，必须给出覆盖所有 n 的分类证明，并用形式化证明工具检查每个分支的不等式、整除和大小条件。
- 独立验证任何计算辅助结论：固定随机种子、保存搜索范围、证明搜索范围之外由解析估计覆盖。

### 公开版思考摘要

这个问题适合 AI 工具链推进，因为它有清晰的代数结构、已有局部常数上界、可形式化验证的短陈述，以及天然的计算反例搜索入口。关键挑战是把随 C 增长的已知上界变成与 C 无关的绝对常数；这通常需要新的全局结构定理，而不是单纯扩大搜索。因此我评为中等候选：有现实机会显著推进、验证局部情形或发现新归约，但完整解决的概率仍受主要数论瓶颈限制。

### 免责声明

以上只是对 GPT-5.5 级别模型可推进性的审查，不是该 Erdős 问题的证明、反例或解答。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_887.md](../../prompts/problem_887.md)

### 状态结论

现有一般上界依赖 C，平方数和近平方数有绝对界；去掉 C 依赖的一般命题仍直接记录为开放。

### 当前规范陈述

是否存在绝对整数 K，使每个实数 C>0 都存在 N_0(C)，且所有 n≥N_0(C) 在开区间 (√n,√n+C n^{1/4}) 内至多有 K 个正因子？

```text
Does there exist an absolute integer K such that for every real C>0 there is N_0(C) with the property that every integer n>=N_0(C) has at most K positive divisors d satisfying sqrt(n)<d<sqrt(n)+C n^{1/4}?
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 无穷多个 n 在 C=1 时有四个因子，说明 K 至少为 4；不否定绝对 K。
- 版本变化: Erdős–Rosenfeld 给 ≤1+C^2；Chan 对平方数给 5、对一类近平方数给 18，且在更宽区间成立。

陈述问题：

- 量词顺序是 ∃K ∀C ∃N_0(C) ∀n。
- 区间是开区间且只计正因子。

需要固定的量词/约定：

- K is independent of C.
- The threshold N_0 may depend on C.

### 文献与当前边界

已核验的主要结果：

- 对固定 C，一般上界 1+C^2。
- C=1 时无穷多个 n 有四个相关因子。
- 平方数及部分近平方数有绝对界。

最近相关工作：Chan 2014/2015 的特殊类结果仍是题目页所列最新实质进展。

剩余核心：对任意整数 n 建立与 C 无关的绝对局部因子数上界。

已使用方法：

- 互补因子与平方差参数化。
- 近平方因子对应圆锥/格点的间距。

争议或不确定性：

- 特殊近平方分类尚未覆盖一般 n。
- 区间端点和 log 扩大因子易被误用。

### 证据来源

- [Erdős Problem 887](https://www.erdosproblems.com/887) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 887](https://www.erdosproblems.com/latex/887) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。

### 完成标准

- 肯定出口: Prove one explicit absolute K and, for each C>0, a valid threshold N_0(C) giving the stated bound for every n beyond it.
- 否定出口: For every K construct some fixed C>0 and arbitrarily large n with more than K divisors in the interval.

不构成完成：

- A bound depending on C.
- A proof only for square or near-square n.
- Examples with four divisors.

正确性陷阱：

- Preserve the quantifier order.
- Use the open one-sided interval.
- Do not import Chan's wider symmetric interval theorem as a general-n theorem.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `36/100`
- 信心: `medium`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 把多个近 √n 因子转成受控的平方差方程族。
- 证明过多因子迫使 n 落入可由特殊类定理覆盖的近平方结构。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
