# Problem 396

## 基本信息

- 原始链接: https://www.erdosproblems.com/396
- LaTeX 页面: https://www.erdosproblems.com/latex/396
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `binomial coefficients`
- 形式化状态: `yes`
- OEIS: `A375077`
- 原站备注字段: 无

## 原问题

Is it true that for every $k$ there exists $n$ such that\[\prod_{0\leq i\leq k}(n-i) \mid \binom{2n}{n}?\]

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `40/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：density, infinitely many

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: binomial coefficients
- 证明密集标签命中: number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: density, infinitely many
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。GPT-5.5 级别模型配合精确计算、p-adic 估值搜索、形式化验证和文献检索，较有希望对有限范围作出可靠验证、发现结构性构造或把问题化约为更清晰的数论条件；但直接给出全称证明的把握不高。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 可行路线是把整除条件改写为对每个素数 p 的估值不等式：sum_{i=0}^k v_p(n-i) <= v_p(binomial(2n,n))，并用 Legendre/Kummer 型公式计算右侧。先用精确搜索复现 A375077 的小 k 数据，提取 n 附近连续因子的素因子和进位模式；再尝试用 CRT、筛法或构造性同余条件制造一族 n，使所有 n,n-1,...,n-k 的素因子都被中心二项式系数的 p-adic 估值覆盖。若得到候选构造，可用形式化证明系统验证估值恒等式和最终整除推导。

### 支持理由

- 问题结构非常离散，核心条件可完全转化为有限个素数的精确估值检查，适合程序搜索和形式化验证。
- 给定 JSON 显示该问题已有 formalized=yes，说明至少题面或相关表达已经进入形式化环境，降低了后续机器检查候选证明的门槛。
- OEIS A375077 给出每个 k 的最小 n，暗示存在可对照的计算数据源，便于测试搜索器、发现模式和排除错误构造。
- 备注中提到 Pomerance 已证明单个移位因子 n-k 的无限多整除结果，以及正向乘积的密度 1 结果；这些是相邻但不等价的强工具，可能为构造或化约提供入口。

### 主要障碍

- 目标要求同一个 n 同时覆盖 k+1 个连续因子，比逐个因子 n-k 的结果强很多，交集结构可能很稀薄。
- 备注中特别指出 n 整除 binomial(2n,n) 已经相当罕见，而本问题还要同时加入 n-1 到 n-k，稀有性是主要难点。
- n-i 的大素因子随 n 变化，不能只处理固定有限模条件；搜索发现的模式未必能外推到任意 k。
- Pomerance 的两个已知结果从 JSON 看都不能直接推出本题：一个是单因子，另一个是正向区间 n+1,...,n+k，而本题是反向区间并包含稀有的 n。
- 若需要全称证明，可能涉及筛法、素因子分布、中心二项式系数的进位结构等较深数论，而不只是大整数计算。

### 需要的验证

- 明确约定 n>k，避免乘积中出现 0 的边界歧义。
- 用两个独立实现验证小 k 的最小 n 或可行 n，并逐素数输出估值证书。
- 若提出构造族，需要证明所有可能素因子 p 的估值不等式，而不只是验证出现在样例中的素数。
- 候选证明应拆成可形式化的 Legendre/Kummer 估值引理、连续乘积估值界、以及最终整除定理。
- 需要检查是否存在从已知 Pomerance 结果到本题的合法推论；不能把单因子或正向乘积结果误用为反向连续乘积结果。

### 公开版思考摘要

这个问题对 AI 工具友好的一面是：每个固定 k,n 的真伪可以用完全精确的 p-adic 估值证书验证，搜索和形式化都很自然；并且 JSON 中已有相邻定理、OEIS 数据和形式化标记。困难在于全称存在性需要控制随 n 变化的多个连续整数的全部素因子，尤其包含罕见条件 n | binomial(2n,n)。因此我判断 GPT-5.5 较可能显著推进计算证据、模式发现、局部定理和验证框架；完整解决有可能但不应高估。

### 免责声明

以上是 AI 可解性与推进潜力评估，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_396.md](../../prompts/problem_396.md)

### 状态结论

当前题目页仍将该全称存在性命题列为开放，并给出 Pomerance 关于单个因子及另一方向连续乘积的结果。未定位到直接关闭全部 k 的论文。

### 当前规范陈述

对每个整数 k≥0，判定是否存在 n≥k，使 n(n-1)⋯(n-k) 整除中央二项式系数 C(2n,n)。

```text
For every integer k>=0, determine whether there exists an integer n>=k such that the product n(n-1)...(n-k) divides the central binomial coefficient binom(2n,n).
```

### 陈述、量词与反例审计

- 歧义严重度: `none`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 小 k 的 OEIS 数据提供候选 n，但不能推出全部 k；单个 n-i 各自可整除也不足以保证乘积整除。
- 版本变化: Pomerance 证明每个固定偏移量 n-k 整除 C(2n,n) 的 n 有无穷多个，并证明正向乘积 ∏(n+i) 的密度 1 结果。

陈述问题：

- 乘积包含 k+1 个因子 n,n-1,...,n-k。
- 每个 k 可选择不同的 n；不要求无穷多个 n。

需要固定的量词/约定：

- The outer quantifier is for every fixed nonnegative integer k.
- Divisibility is integer divisibility of the full product, including repeated prime powers.

### 文献与当前边界

已核验的主要结果：

- For every fixed shift j there are infinitely many n with n-j dividing binom(2n,n).
- The product of forward shifts n+1,...,n+k divides binom(2n,n) for a density-one set of n.

最近相关工作：未发现 2015 年 Pomerance 之后直接解决后向 k+1 个连续因子同时整除的工作；因此只能给 likely_open。

剩余核心：同时控制 n,n-1,...,n-k 的全部素数赋值，构造适用于任意 k 的 n。

已使用方法：

- Kummer/Legendre valuations for binomial coefficients
- Chinese remainder constructions and smoothness of consecutive integers

争议或不确定性：

- ‘未检得’不是确认开放的证明。
- 逐因子整除与乘积整除之间存在共享素因子的赋值障碍。

### 证据来源

- [Erdős Problem 396](https://www.erdosproblems.com/396) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 396](https://www.erdosproblems.com/latex/396) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [Divisors of the middle binomial coefficient](https://math.dartmouth.edu/~carlp/catalan4.pdf) — Carl Pomerance; `primary_paper`, `peer_reviewed`, reliability=`high`. 证明单偏移及正向连续乘积结果，但未给出本题的后向全乘积结论。

### 完成标准

- 肯定出口: For arbitrary k, construct n and prove v_p(n(n-1)...(n-k)) <= v_p(binomial(2n,n)) for every prime p.
- 否定出口: Find a specific k and prove that no n satisfies the divisibility.

不构成完成：

- Checking only finitely many values of k.
- Proving each factor divides separately.
- Using the known forward-product theorem.

正确性陷阱：

- Track p-adic valuations, not only prime supports.
- Handle n=k and zero-factor conventions by requiring n>k when necessary.
- Do not reverse the direction of the consecutive product.

### 更新后的 AI 可解答性

- 等级: `medium_candidate`
- 分数: `60/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- ‘未检得’不是确认开放的证明。
- 逐因子整除与乘积整除之间存在共享素因子的赋值障碍。

Proof-first 路线：

- 选择 n 的同余类使每个小素数的进位数充足。
- 寻找把正向密度一结果迁移到后向乘积的对称或平移机制。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态涉及题面修订、解答声明、低覆盖文献或较新预印本，建议专家重点抽查。

<!-- DEEP_REVIEW:END -->
