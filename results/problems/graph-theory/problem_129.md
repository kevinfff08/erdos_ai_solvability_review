# Problem 129

## 基本信息

- 原始链接: https://www.erdosproblems.com/129
- LaTeX 页面: https://www.erdosproblems.com/latex/129
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: ambiguous statement

## 原问题

Let $R(n;k,r)$ be the smallest $N$ such that if the edges of $K_N$ are $r$-coloured then there is a set of $n$ vertices which does not contain a copy of $K_k$ in at least one of the $r$ colours. Prove that there is a constant $C=C(r)>1$ such that\[R(n;3,r) < C^{\sqrt{n}}.\]

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `43/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：\gg

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: colouring, ramsey
- 渐近/无限线索: \gg
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 + computation/formalization/literature tools`
- 结论: **按给定 JSON 中的文字，本题不适合作为“证明原命题”的候选，因为备注已经给出 r=2 情形的指数级下界思路，直接反驳所要求的 C^{sqrt(n)} 上界。GPT-5.5 级别模型更可能完成的是：把该反例论证写成严格概率证明、检查定义歧义、给出可形式化版本，并说明原始 Erdős-Gyárfás 可能意图无法仅从本 JSON 恢复。**
- 等级: `not_applicable_meta_mathematical`
- 分数: `18/100`
- 信心: `high`
- 可能路线: 先固定 r=2。对 K_N 的边独立均匀红蓝染色。对任意 n 点集合，利用其含有很多边不交三角形，估计该集合缺少红三角或缺少蓝三角的概率呈 exp(-c n^2) 或足够快下降；再对至多 N^n 个 n 点集合做并合界，得到当 N <= C^n 时仍存在一种染色，使每个 n 点集合同时含红三角和蓝三角。因此 R(n;3,2) >= C^n，和所要求的 R(n;3,r) < C(r)^{sqrt(n)} 在 r=2 时矛盾。模型可进一步把常数、边不交三角形数量、并合界条件写清楚并形式化验证。

### 支持理由

- 题目本身的 remarks_excerpt 明确指出“as written is easily disproved”，且给出 r=2 的随机染色反例路线。
- 原命题量化覆盖 r=2；只要 r=2 情形有 R(n;3,2) >= C^n，就不可能存在所称的 C^{sqrt(n)} 普遍上界。
- 所需反驳路线是标准概率方法：随机染色、固定 n 点集坏事件估计、并合界；这类推导很适合由模型配合符号计算或形式化证明助手逐步核验。
- 模型不需要解决未知的真正意图问题；它可以可靠地判断“当前陈述为假或至少不适合作为证明任务”。

### 主要障碍

- 核心障碍不是证明难度，而是题目陈述歧义和可能错误；仅凭本 JSON 无法恢复 Erdős 原本想问的正确版本。
- 随机反例证明仍需补齐细节：每个 n 点集内可取多少边不交三角形、坏事件概率的精确上界、并合界允许的 C 的范围。
- 若尝试形式化，需要先固定定义：‘does not contain a copy of K_k in at least one colour’ 的逻辑范围、R(n;k,r) 的最小性、颜色类子图的表述。
- 如果存在另一个 intended formulation，则本 JSON 不足以判断该替代问题的可解性。

### 需要的验证

- 写出完整的 r=2 反例证明，并检查所有量词与常数依赖是否正确。
- 验证 n 点完全图中边不交三角形数量下界足以支撑并合界。
- 形式化或半形式化随机染色论证，尤其是坏事件独立性如何由边不交三角形保证。
- 明确报告：被反驳的是 problem JSON 中的原文陈述，而不是未知的可能修正版。

### 公开版思考摘要

该问题按文字不是一个可直接证明的开放命题。因为 r=2 是命题覆盖的特例，而给定备注已给出随机红蓝染色构造，说明在 N 指数于 n 的范围内仍可让每个 n 点集同时含红三角和蓝三角，从而 R(n;3,2) 至少为 C^n。这与所要求的 C^{sqrt(n)} 上界冲突。因此 GPT-5.5 最有价值的工作是验证并严密化这个反例、定位歧义、提出需要澄清的替代命题，而不是尝试证明原命题。

### 免责声明

这不是对某个修正后 Erdős 问题的解答；它只是基于给定 problem JSON 对原陈述的 AI 可处理性和有效性作出的审查。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `disproved`
- 状态信心: `high`
- 可行动性: `closed_verification_only`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_129.md](../../prompts/problem_129.md)

### 状态结论

按可自然重建的字面命题，结论是假的。取 r=2，随机红蓝边染色可在 N=exp(cn) 个顶点上保证每个 n 顶点集同时含红三角形和蓝三角形，故 R(n;3,2)≥exp(cn)，与任何 C^{√n} 上界矛盾。Erdős Problems 页面及其论坛线程也明确记录了 Antonio Girão 的这一反驳。原始作者可能另有意图，但尚无可核验的修订题面；这不改变字面命题已被否定的状态。

### 当前规范陈述

对整数 n,k,r≥2，令 R(n;k,r) 为最小的 N，使得 K_N 的每个 r-边染色都存在一个 n 顶点集 S 及一种颜色 i∈{1,…,r}，使颜色 i 在 S 上诱导的子图不含 K_k。题面显示断言的自然量词解释为：对每个固定 r≥2，存在 C_r>1 与 n_0(r)，使得对所有 n≥n_0(r)，R(n;3,r)<C_r^{√n}。该字面断言在 r=2 时为假。

```text
For integers n,k,r≥2, let R(n;k,r) be the least N such that every r-colouring of E(K_N) has an n-vertex set S for which there exists a colour i∈{1,…,r} such that the colour-i subgraph induced by S contains no K_k. The displayed assertion naturally means: for every fixed r≥2, there are constants C_r>1 and n_0(r) such that R(n;3,r)<C_r^{√n} for every n≥n_0(r). This literal assertion is false, already for r=2.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `counterexample_found`
- 检查说明: 取 r=2。随机独立、公平地红蓝染 K_N 的每条边。任一固定 n 顶点集 S 含有 m≥c_0n^2 个两两边不交三角形：可用贪心法，因为一个三角形至多与 O(n) 个其他三角形共边，而 K_n 有 Θ(n^3) 个三角形。对其中固定一种颜色，所有这 m 个三角形均非该色单色三角形的概率为 (7/8)^m；对红、蓝并合，S 未同时含红三角形和蓝三角形的概率至多 2(7/8)^m≤2e^{-c_1n^2}。再对至多 N^n 个 n 集合并合。取 N=⌊e^{c_1n/2}⌋，期望坏集合数小于 1（n 充分大），故存在一个二染色，其中每个 n 集合均含两种颜色的三角形。该染色没有满足定义结论的 S，所以 R(n;3,2)>N≥e^{c_2n}。这否定 R(n;3,2)<C^{√n}。
- 版本变化: 当前数据库条目仍显示 open，但其 LaTeX 页、历史页和论坛线程均载有 Girão 指出的 r=2 反例；论坛还明说原始来源含糊。论坛页只出现来源标签 [Er97b]，本审计未能从可访问的公开记录恢复并核验其完整原始书目信息或一份正式修订。因此不存在已证实的“修订后残余开放题”。

陈述问题：

- 题面没有把“对每个固定 r”及渐近阈值 n_0(r) 写出；这是 C=C(r) 的标准自然解释。
- 题面与备注将 r,k≥2 作为参数范围，因此 r=2 是字面命题的一个实例；不允许事后无来源地改成 r≥3。
- “在至少一种颜色中不含 K_k”必须是“存在一种颜色 i，使 S 的 i 色图不含 K_k”，而非“每一种颜色都不含 K_k”。
- 页面的泛化式写成 n^{1/k-1}，其指数按字面为负，且与相邻的 C^{√n} 叙述不一致；这进一步说明历史记录/转录需要原始来源核验。
- Erdős Problems 的论坛页明确说“原始来源对于问题为何物是含糊的”；但当前显示命题本身仍足够精确，且可被 r=2 反例否定。

需要固定的量词/约定：

- r is fixed before choosing C_r and n_0(r).
- The assertion must hold for all sufficiently large n, not merely along a subsequence.
- The existential quantifier over colours is inside the conclusion for S: ∃S∃i such that S has no colour-i K_3.
- For a disproof it suffices to give one admissible r; r=2 is admissible under the literal recorded domain.

### 文献与当前边界

已核验的主要结果：

- 当前条目把“Erdős–Gyárfás 证明过 R(n;3,r)>C^{√n}”作为数据库叙述，但没有提供可核验的完整原始引文；本审计不把它当作已独立核验的原始定理。
- 字面题面已由 r=2 的概率构造反驳，且构造实际上给出指数级下界 R(n;3,2)≥e^{cn}。这是一个完整的负面结论，不是仅有的数值证据。
- Conlon–Fox–Lee–Sudakov（2015）及 Bennett–Dudek–English（2022/2023）研究常被称作 Erdős–Gyárfás generalized Ramsey problem 的不同函数 f(n,p,q)。它们不为本条 R(n;k,r) 提供状态证据。

最近相关工作：未找到 2023–2026 年直接以本题精确定义 R(n;k,r) 和 C^{√n} 目标给出正式修订、证明或反例的新论文。对同名但不同的 f(n,p,q) 问题，Bennett、Dudek、English 的 2023 修订预印本是近期相关但不等价的工作。

剩余核心：无：字面命题已被否定。唯一未完成的是文献/史料核验工作——找出 [Er97b] 的完整原文并确定它是否陈述了一个不同且明确的命题；在此之前不存在可诚实指定为“第129题残余核心”的开放问题。

已使用方法：

- 概率法：固定 n 集合中打包 Θ(n^2) 个边不交三角形，利用独立性及对全部 n 集合的并合界。
- 文献辨析：区分固定颜色数下的“每一色均含三角形”问题 R(n;k,r)，与 f(n,p,q) 的局部多色问题。

争议或不确定性：

- 数据库标签为 open 与其自身记录的 r=2 反例不一致；字面状态应以可验证反例为准。
- 原始出处 [Er97b] 的完整书目信息和原文未被本审计直接取得，因此不能判定作者的预期修订。
- 没有证据支持把题目自动改为 r≥3，或改为 f(n,p,q) 问题。

### 证据来源

- [Erdős Problems — LaTeX source for Problem 129](https://www.erdosproblems.com/latex/129) — Erdős Problems project, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 直接给出当前题面、r=k=2 的说明、Girão 所指出的 r=2 随机染色反例，以及“原意不清楚”的备注。
- [Erdős Problem #129 — discussion thread](https://www.erdosproblems.com/forum/thread/129) — Erdős Problems project; discussion note credits Antonio Girão, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 确认该站的当前讨论页保留 open 标签但同时明确记录题面已被 r=2 反例否定，并称原始来源含糊；可见评论未提供可审计的替代题面或证明。
- [The Erdős–Gyárfás problem on generalized Ramsey numbers](https://arxiv.org/abs/1403.0250) — David Conlon, Jacob Fox, Choongbum Lee, Benny Sudakov, 2014-03-02; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 该论文的摘要定义的是另一参数化 f(n,p,q)：使每个 K_p 使用至少 q 种颜色所需的最少颜色数。它不能用来证明或修复本题的 R(n;k,r) 断言，因而是避免名称混淆的直接证据。相关期刊版本为 Proc. London Math. Soc. (2015), DOI 10.1112/plms/pdu049。
- [A random coloring process gives improved bounds for the Erdős–Gyárfás problem on generalized Ramsey numbers](https://arxiv.org/abs/2212.06957) — Patrick Bennett, Andrzej Dudek, Sean English, 2022-12-14; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 近期文献继续研究的同样是 f(n,p,q) 的“每个 K_p 使用至少 q 色”问题，不是本条记录的 R(n;k,r)；不能作为第129题的已知结果或修订来源。

### 完成标准

- 肯定出口: For the verification task, give a fully quantified random-colouring construction for r=2 showing R(n;3,2)≥e^{cn} for all sufficiently large n, and verify that this contradicts every proposed C^{√n} upper bound.
- 否定出口: If a primary source is located, show that it explicitly states a different parameter range or a different definition; then the present record must be split, with the literal record remaining disproved and the separately stated target audited anew.

不构成完成：

- A proof about the distinct f(n,p,q) Erdős–Gyárfás function does not address this R(n;k,r) statement.
- Checking finitely many n, or producing a random sample without a union-bound certificate, does not prove an exponential lower bound.
- Replacing r≥2 by r≥3 without an inspected source is not a repair or a resolution.

正确性陷阱：

- The construction must prove R(n;3,2)>N: every n-set must contain both a red and a blue triangle.
- Use an edge-disjoint triangle packing of size Θ(n^2), not merely Θ(n), before claiming the required exponential N.
- For each fixed n-set, apply independence only to edge-disjoint triangles.
- Do not confuse an r-colouring with at most r colours and a colouring required to use every colour; the random construction uses both colours.
- Do not infer an open problem from the database’s open label after a literal counterexample is supplied.

### 更新后的 AI 可解答性

- 等级: `not_applicable_closed_or_invalid`
- 分数: `0/100`
- 信心: `high`
- 结论: 字面断言已被可短证、可独立复核的概率反例否定，故没有可评分的当前开放证明目标。

支持理由：

- r=2 在记录的自然参数域中，且指数下界与 C^{√n} 上界直接冲突。
- 反例的独立性、并合界和 R 的不等式方向均可明确审计。

主要障碍：

- 历史原始题面的意图仍不明，但这只影响可能的新条目，不影响字面命题的否定。
- 同名 f(n,p,q) 文献容易造成错误迁移。

Proof-first 路线：

- 只做闭合核验：写出完整概率论证并追溯 [Er97b] 原文。
- 若找到不同的正式题面，将其作为新目标独立进行状态审计，而不把它视为本题的未解决部分。

需要验证：

- 人工/馆藏检索 [Er97b] 原文，核验原始定义、r 的范围及页面泛化式的指数。
- 复核三角形贪心打包常数和并合界；不需要计算机枚举。

### 审计限制与人工复核理由

- 未能直接取得并检查来源标签 [Er97b] 的完整原始文本，故历史归属、原始下界及作者意图均不能视为已独立确认。
- 未发现正式修订题面；“未发现”不是其不存在的证明。
- 论坛线程的当前页面仅见一条不含数学论证的评论；未据此作出任何额外结论。
- 本结论只关闭自然字面重建；若未来得到不同的原始明确陈述，该陈述须作为新目标重新审计。

- 需要馆藏或专家协助恢复并逐页检查 [Er97b] 的原文及完整书目信息。
- 应人工复核数据库泛化式中的异常指数 n^{1/k-1} 是否为转录错误，以及它与第129题的关系。

<!-- DEEP_REVIEW:END -->
