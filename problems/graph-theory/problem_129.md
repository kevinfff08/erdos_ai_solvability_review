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
