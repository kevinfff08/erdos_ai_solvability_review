# Problem 1189

## 基本信息

- 原始链接: https://www.erdosproblems.com/1189
- LaTeX 页面: https://www.erdosproblems.com/latex/1189
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `covering systems`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Call a set of distinct integers $1<n_1<\cdots<n_k$ a covering set if there is a choice of $a_i\pmod{n_i}$ for $1\leq i\leq k$ such that every integer satisfies at least one of these congruences. A set is an irreducible covering set if no proper subset is a covering set.

How many irreducible covering sets of size $k$ are there?

What is the minimum and maximum that $n_k$ can be?

Determine or estimate $\max \sum\frac{1}{n_i}$, where the maximum ranges over all irreducible covering sets of size $k$.

Are there infinitely many $n$ such that the divisors of $n$ (which are $>1$) form an irreducible covering set?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `28/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：asymptotic, infinitely many, o(, prime

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: covering systems
- 证明密集标签命中: number theory
- 有限/计算线索: covering system, finite, finitely
- 渐近/无限线索: asymptotic, infinitely many, o(, prime
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5-level tool-augmented model`
- 结论: **中等偏低候选：该问题不太像可由一次模型调用完整解决的开放问题，但很适合被 GPT-5.5 级别模型用 SAT/ILP 搜索、覆盖系统文献检索、形式化验证和小 k 枚举来显著推进。最有希望的不是直接给出全部渐近答案，而是建立可复现的枚举框架，验证若干 k 的 I(k)、最小/最大 n_k 与最大倒数和，并把已知上界和构造统一成可审计的证据。**
- 等级: `low_to_medium_candidate`
- 分数: `48/100`
- 信心: `medium`
- 可能路线: 可行路线是把“给定模数集合是否存在覆盖剩余类、且不可约”编码为有限周期上的 SAT/ILP/精确覆盖问题：周期取 lcm(n_i)，变量表示每个模数选择的剩余类，约束要求每个整数类被至少一个同余类覆盖，并对每个 proper subset 加入非覆盖证据或用逐子集判定过滤。结合 Simpson 的 n_k <= 2^{k-1} 可对固定 k 做有限枚举；再用剪枝、支配关系、倒数和上界、lcm 分解和同余覆盖密度过滤搜索空间。对于“divisors of n”子问题，可将给定 n 的除数集合判定为覆盖/不可约，并验证题述 Sun 构造族。形式化证明方面，比较适合先形式化判定器正确性、有限搜索证书和小 k 结论，而不是直接形式化整个开放问题。

### 支持理由

- 题目本身包含可计算的有限判定结构：给定有限模数集合，是否存在覆盖剩余类可化为有限周期上的组合搜索。
- remarks 给出 Simpson 上界 n_k <= 2^{k-1}，这使固定 k 的最大模数搜索原则上有限，适合工具辅助枚举。
- 不可约性可以通过对子集重复判定或通过覆盖证书/非覆盖证书验证，适合生成可复查证据。
- 倒数和最大化、最小/最大 n_k、小 k 的 I(k) 都天然适合整数规划、SAT、分支限界和证书化计算。
- 最后一个关于 divisors of n 的无限性问题在题述 remarks 中已有 Sun 的构造结论；模型可帮助复核、形式化或扩展计算实验，而不是把它当作仍需解决的核心难点。
- 与 minimal covering system 的关系提示已有理论入口；模型可通过文献检索整理已知上界、构造和差异，避免重复证明已知结论。

### 主要障碍

- 完整求出 I(k) 的一般公式或精确渐近很可能非常困难，因为 remarks 已显示它与 minimal covering systems 的深层计数结果相连。
- 枚举空间随 k 快速爆炸；即使有 n_k <= 2^{k-1}，模数子集、lcm 周期和剩余类选择仍会造成严重组合爆炸。
- “irreducible covering set”与“minimal covering system”的差别细微，容易在理论归约中误把系统层面的极小性当成模数集合层面的不可约性。
- 最大倒数和问题可能需要非平凡结构定理；纯搜索只能覆盖小 k，难以直接给出一般 k 的最优表达式。
- 若要证明全局最大 n_k 或倒数和界，必须排除所有潜在覆盖集合，证书规模和理论剪枝都可能成为瓶颈。

### 需要的验证

- 为 SAT/ILP 判定器证明正确性：有限周期判定必须等价于整数全集上的覆盖判定。
- 对每个声称的小 k 枚举结果，保存覆盖证书、不可约证书和排除证书，并由独立实现交叉验证。
- 对使用 Simpson 上界的任何有限搜索，明确证明搜索范围确实包含所有 irreducible covering sets of size k。
- 对倒数和最大化结果，需要同时提供达到下界的构造和排除更大值的可检查证明或完整搜索日志。
- 对 divisor-set 构造的验证，需要区分已知 Sun 族的复核与新构造，避免把已知定理误报为新进展。
- 如输出理论命题，应由 Lean/Isabelle 或至少独立人工检查其关键引理，尤其是不可约性和 minimal-covering-system 之间的转换。

### 公开版思考摘要

这个问题含有多个层次：固定 k 的判定和枚举是高度工具友好的，GPT-5.5 级别模型可望把它转化为可复现计算、找出小规模数据、验证已知构造并提出猜想；但一般 k 的计数、极值和渐近问题明显接近当前覆盖系统研究前沿。因而它不是高概率“直接解决”题，而是一个较好的“显著推进/证书化计算/局部定理验证”候选。

### 免责声明

以上是对工具增强模型可推进性的评估，不是该 Erdős 问题的解答，也不声称给出了新的定理或完整分类。

<!-- MODEL_REVIEW:END -->
