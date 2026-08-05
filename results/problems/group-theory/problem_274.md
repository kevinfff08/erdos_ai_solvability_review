# Problem 274

## 基本信息

- 原始链接: https://www.erdosproblems.com/274
- LaTeX 页面: https://www.erdosproblems.com/latex/274
- 原始状态: `open`
- 奖金: `no`
- 主类别: `group theory`
- 原始标签: `group theory`, `covering systems`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: Herzog-Schönheim conjecture

## 原问题

If $G$ is a group then can there exist an exact covering of $G$ by more than one cosets of different sizes? (i.e. each element is contained in exactly one of the cosets)

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `45/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 主要风险是候选证明或计算证书容易存在隐藏漏洞，需要独立复核。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: covering systems
- 证明密集标签命中: 无
- 有限/计算线索: finite, finitely
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **这是一个中等候选问题：GPT-5.5 级别模型配合计算和形式化工具，较可能显著推进局部情形、验证大范围有限群实例、整理等价归约与已有证明，但直接给出完整 Herzog-Schönheim 猜想证明的概率不高。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 较现实的路线是把问题转化为有限商群上的 coset partition 搜索与约束满足问题，结合 GAP/Sage 对有限群和置换表示做穷举或反例排除；同时形式化已知归约、Sun 的次正规子群情形和 Margolis-Schnabel 的小阶验证框架。若要产生新进展，最有希望的是自动发现可推广的局部判据，例如对某些非次正规子群配置、最小反例结构、或特定单群/几乎单群扩张的排除。

### 支持理由

- 题面已经有形式化标记，说明至少部分定义、命题或验证目标适合交给 Lean/Isabelle/Coq 等证明工具检查。
- 问题具有明确的有限组合结构：exact covering、cosets、indices distinct，这类条件可编码为集合分割、整数约束或群作用约束，适合计算搜索和最小反例分析。
- 已有结果覆盖 abelian/subnormal 情形以及所有阶小于 1440 的群，给模型提供了可复现的验证基线和可能的归纳结构。
- GPT-5.5 可在文献检索、GAP 脚本生成、证明草案提炼、反例搜索和形式化补洞之间循环，因而不只是在自然语言层面猜测。

### 主要障碍

- 这是一般群论中的开放猜想，非交换、非次正规子群的结构空间很大，现有局部结果未必暗示一条短证明。
- 有限群计算验证容易受群阶爆炸、子群共轭类数量、coset 组合数量影响，单纯暴力搜索很快不可行。
- 从小阶计算中抽取可证明的一般结构定理是核心难点，模型可能发现模式但难以保证其可推广。
- 形式化证明可验证局部命题，但若缺少新的数学不变量或强归约，形式化本身不会自动产生完整证明。

### 需要的验证

- 复现已知小阶验证：至少确认对所有 |G| < 1440 的计算编码与题意一致。
- 检查是否可严格归约到有限群或有限商群情形，并明确无限群情形中每个 coset/subgroup index 的处理。
- 对模型提出的任何新判据，用 GAP 生成覆盖配置搜索测试，并在多个群族上寻找反例。
- 若声称证明新情形，需要形式化关键引理，尤其是 coset partition、distinct indices、subnormal/normal core 等步骤。
- 文献检索需确认 Sun 2004 与 Margolis-Schnabel 2019 的确切命题范围，避免把已知结果误表述为新结果。

### 公开版思考摘要

该问题不像纯解析数论中依赖极深估计的猜想那样完全脱离计算实验；它有清晰的代数-组合编码，并且已有小阶计算与特殊群类证明可作为校验点。因此 GPT-5.5 加工具有较好的推进空间，尤其适合做有限群排除、最小反例结构分析、形式化已有结果和自动生成候选引理。不过，一般 Herzog-Schönheim 猜想仍需要新的群论思想，模型直接完成全证明的可期待性有限。

### 免责声明

以上是对 AI 辅助可推进性的评估，不是该 Erdős 问题的解答，也不声称已经证明或否定 Herzog-Schönheim 猜想。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_274.md](../../prompts/problem_274.md)

### 状态结论

这是 Herzog--Schönheim 猜想的规范形式。2025 年预印本解决了有限单群和对称群，既强化了开放性证据，也表明一般群情形尚未解决。

### 当前规范陈述

设群 G 被有限多个有限指数子群的左陪集 x_iH_i（k>1）恰好分割。证明或否证至少两个指数 [G:H_i] 相等。

```text
Let G be a group and let x_1H_1,...,x_kH_k be a finite partition of G into left cosets of finite-index subgroups, with k>1. Prove or disprove that two indices [G:H_i] must be equal.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 循环群/阿贝尔群、次正规子群、若干小群及简单群等正面结果不构成一般证明。
- 版本变化: Sun 处理次正规子群；Margolis--Schnabel 处理小群；Garonzi--Margolis 处理有限单群和对称群。

陈述问题：

- “different sizes”必须规范为子群指数两两不同，而不是陪集基数在无限群中的比较。
- 覆盖必须是恰好一次的分割，且只需考虑有限指数子群。

需要固定的量词/约定：

- The family of cosets is finite and pairwise disjoint with union G.
- The conclusion concerns equality of subgroup indices.

### 文献与当前边界

已核验的主要结果：

- The conjecture holds for uniform covers by subnormal subgroups.
- It holds for groups of order below 1440.
- A 2025 preprint proves it for finite simple groups and symmetric groups.

最近相关工作：Garonzi--Margolis, arXiv:2509.25118，证明简单群和对称群情形，但陈述仍把一般版本列为猜想。

剩余核心：证明任意群的有限陪集分割不可能具有两两不同的有限指数，或构造一个真正的反例。

已使用方法：

- group actions and permutation representations of coset partitions
- group algebra, character-theoretic, and divisibility obstructions

争议或不确定性：

- 有限群与无限群之间的约化必须显式证明。
- 新结果覆盖重要群类但并未覆盖所有有限群。

### 证据来源

- [Erdős Problem 274](https://www.erdosproblems.com/274) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 274](https://www.erdosproblems.com/latex/274) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [On the Herzog-Schönheim conjecture for uniform covers of groups](https://arxiv.org/abs/math/0306099) — Zhi-Wei Sun; `preprint`, `peer_reviewed`, reliability=`high`. 证明次正规子群的一大类情形。
- [The Herzog-Schönheim conjecture for simple and symmetric groups](https://arxiv.org/abs/2509.25118) — M. Garonzi and L. Margolis; `preprint`, `preprint`, reliability=`high`. 证明有限单群和对称群情形，同时直接把一般命题称为猜想。

### 完成标准

- 肯定出口: Prove that every finite coset partition of a group repeats a subgroup index.
- 否定出口: Construct a group with a finite exact coset partition whose finite subgroup indices are pairwise distinct.

不构成完成：

- A proof restricted to abelian, solvable, subnormal, simple, or symmetric groups.
- A covering with overlaps instead of a partition.
- Repeated subgroups with equal index.

正确性陷阱：

- Separate left/right coset conventions only where non-normality matters.
- Verify finite index and exact one-fold coverage.
- Do not infer the general conjecture from classification of simple groups alone.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `36/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- 有限群与无限群之间的约化必须显式证明。
- 新结果覆盖重要群类但并未覆盖所有有限群。

Proof-first 路线：

- 把最小反例约化到有限群并分析其最小正规子群。
- 利用陪集指标的算术约束和置换表示排除不同指数。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。

<!-- DEEP_REVIEW:END -->
