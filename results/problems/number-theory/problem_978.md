# Problem 978

## 基本信息

- 原始链接: https://www.erdosproblems.com/978
- LaTeX 页面: https://www.erdosproblems.com/latex/978
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `yes`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $f\in \mathbb{Z}[x]$ be an irreducible polynomial of degree $k>2$ (and suppose that $k\neq 2^l$ for any $l\geq 1$) such that the leading coefficient of $f$ is positive.

Does the set of integers $n\geq 1$ for which $f(n)$ is $(k-1)$-power-free have positive density?

If $k>3$, and for all primes $p$ there exists $n$ such that $p^{k-2}\nmid f(n)$, then are there infinitely many $n$ for which $f(n)$ is $(k-2)$-power-free?

In particular, does\[n^4+2\]represent infinitely many squarefree numbers?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `23/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：asymptotic, density, infinitely many, prime, primes

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: asymptotic, density, infinitely many, prime, primes
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能由 GPT-5.5 级别模型在一次工具增强研究中完全解决；但它有中等价值用于整理已知定理边界、形式化局部条件、做大规模反例/数据检索，并可能在特定低次数或附加假设下给出可验证的推进。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 最现实路线不是直接证明一般情形，而是把问题拆成：确认第一问已由 Hooley 的渐近公式覆盖；复核第二问在 k>=9 的既有解析数论证明框架；对剩余 k=4 到 8 尤其 n^4+2 的平方自由值问题，结合局部可解性检查、p-adic 根计数、筛法常数计算、大规模搜索和形式化验证来排除简单障碍，并尝试在特殊多项式族上改进已有筛界。

### 支持理由

- 题面备注已经给出第一问被 Hooley 解决，因此 AI 可以较可靠地完成文献整理、证明依赖图和形式化陈述校验。
- 第二问对 k>=10 和 k>=9 已有 Heath-Brown 与 Browning 的结果，说明问题有成熟的解析数论路线，AI 可通过文献检索和证明结构重建来显著降低验证成本。
- 问题含有明确局部必要条件，适合用计算工具系统检查 p^{k-2} 对 f(n) 的同余障碍、估计局部密度并生成可审计数据。
- 形式化状态为 yes，说明至少部分陈述已有形式化接口；GPT-5.5 可辅助把局部引理、有限同余检查和计算证据做成更可复验的证明工件。
- 特例 n^4+2 可进行大规模 squarefree 搜索和模素数根统计，这对发现反例模式或验证启发式密度很有帮助。

### 主要障碍

- 剩余核心包含 quartic squarefree values，例如 n^4+2 是否表示无穷多个平方自由数；这是深层筛法/解析数论难题，不能靠有限计算或普通形式化自动化解决。
- 现有高次数结果依赖复杂估计与 determinant method 类型技术；GPT-5.5 即使能复述证明，也很难可靠地产生突破性的新均匀估计。
- 从大量计算数据到无穷性证明存在巨大鸿沟，尤其需要控制大平方因子贡献，而这通常是平方自由值问题的关键困难。
- 一般不可约多项式的低次数情形有许多局部和全局算术细节，自动反例搜索容易漏掉需要严谨处理的 p-adic 或薄集异常。
- 若尝试直接攻击 n^4+2，可能需要新的想法或很强的外部猜想；模型生成的证明草稿误判风险较高。

### 需要的验证

- 逐条核验 Hooley、Heath-Brown、Browning 结果是否确实覆盖题面中相同假设，尤其是局部条件和次数边界。
- 对目标多项式 f 建立可复现的局部障碍检查：对足够多小素数计算 f(n) mod p^a 的根分布，并证明有限检查为何足够或仅作为实验。
- 若模型提出新证明，需要专家复核关键解析估计，特别是大 p^{k-2} 或平方因子贡献的上界。
- 对计算搜索结果，需要独立实现交叉验证，记录区间、筛法、素数界和整数分解策略。
- 若使用形式化证明，需要确认形式化陈述与原数学问题一致，而不是只形式化了弱化版本或有限计算部分。

### 公开版思考摘要

这个问题的一部分已经在题面备注中被标明解决，另一部分在高次数情形已有强结果；因此 GPT-5.5 很适合做文献边界整理、证明结构重建、局部条件验证和计算实验。但开放核心集中在低次数，特别是 n^4+2 的平方自由值无穷性，这类问题需要超出现成工具链的深层解析数论突破。综合看，它不是完全无望的 AI 研究对象，但更适合作为验证和局部推进任务，而不是高概率自动解决任务。

### 免责声明

以上是对 GPT-5.5 工具增强条件下可推进性的审查，不是该 Erdős 问题的数学解答，也不声称证明了 n^4+2 有无穷多个平方自由值。

<!-- MODEL_REVIEW:END -->
