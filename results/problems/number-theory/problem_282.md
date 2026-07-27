# Problem 282

## 基本信息

- 原始链接: https://www.erdosproblems.com/282
- LaTeX 页面: https://www.erdosproblems.com/latex/282
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `unit fractions`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $A\subseteq \mathbb{N}$ be an infinite set and consider the following greedy algorithm for a rational $x\in (0,1)$: choose the minimal $n\in A$ such that $n\geq 1/x$ and repeat with $x$ replaced by $x-\frac{1}{n}$. If this terminates after finitely many steps then this produces a representation of $x$ as the sum of distinct unit fractions with denominators from $A$.

Does this process always terminate if $x$ has odd denominator and $A$ is the set of odd numbers? More generally, for which pairs $x$ and $A$ does this process terminate?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: unit fractions
- 证明密集标签命中: number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 with computational, formalization, literature-search, and counterexample-search tools`
- 结论: **低到中等候选。该问题的核心公开子问涉及受限分母贪心埃及分数算法是否必定终止，属于开放的数论/单位分数动力系统问题。GPT-5.5 级模型不宜被判断为很可能直接解决主命题，但有现实机会在有限状态归约、计算反例搜索、形式化验证局部不变量、以及特定同余类或特定有理数族的终止性证明上取得显著推进。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 较可行的路线不是直接证明全体奇分母情形，而是把贪心过程视为有理数迭代：对固定 A 或同余类 A，分析余数分子分母的递推、单调量、p 进制或模约束，并用计算搜索寻找循环、极慢终止轨道或可证明的下降势函数。形式化证明工具可用于验证递推、终止证书和小参数穷举；反例搜索可尝试发现非终止循环或无限逃逸模式；若发现结构性族，则再转化为人类可审计的定理。

### 支持理由

- 问题定义清晰，贪心算法可精确实现，适合大规模有理数实验、轨道统计、极端样例搜索和证书化验证。
- 奇分母限制保留了足够强的算术结构：若当前 x 有奇分母，选择奇数 n 后余数仍可被精确追踪，这给模运算、不变量和势函数分析留下空间。
- 给定备注表明相关表示存在性已有判别结果，但贪心终止性仍悬而未决；这使得 AI 工具可以专注于算法轨道本身，而不是先解决表示存在性。
- 形式化状态空间和局部引理较自然：每一步的最小允许分母、余数正性、分母奇偶性、终止证书、以及有限区间穷举都可以机器检验。
- 即使不能解决主问题，模型仍可能产出有价值成果，例如新的可验证终止族、失败候选轨道、复杂度增长实验、或对 Graham 型同余条件下贪心终止性的子情形归约。

### 主要障碍

- 主问题要求排除所有可能的无限贪心轨道；余数分母通常会快速增长，单纯计算无法覆盖无限情形。
- 存在性结果不等于贪心算法成功；即使某个 x 可表示为允许分母的有限互异单位分数，贪心选择仍可能走入难以控制的轨道。
- 若非终止行为不是简单循环，而是分母无限增长的逃逸轨道，反例搜索很难给出有限可验证证书。
- 经典 Fibonacci/Sylvester 贪心终止论证对 A=自然数依赖强，限制到奇数或更一般集合 A 后，关键下降结构可能失效。
- 一般化问题‘哪些 x 与 A 会终止’范围很宽，缺少额外限制时更像分类纲领而非单一定理。

### 需要的验证

- 建立精确的有理数贪心实现，并用形式化或独立程序交叉验证每一步最小允许分母选择。
- 对大量奇分母 x 运行搜索，记录终止步数、最大分母、异常增长轨道，并检查是否存在候选循环或准循环结构。
- 将任何发现的终止族写成明确引理，并用 Lean/Isabelle/Coq 或等价证明检查器验证递推与下降量。
- 若提出反例，需要给出有限可审计证书；若只是无限逃逸猜想，则需要证明轨道永不命中 0，而不能只依赖数值趋势。
- 对更一般 A 的结论必须明确假设，例如 A 是同余类、平方数、有限并同余类或具有密度条件，避免把实验规律误报为完整分类。

### 公开版思考摘要

这个问题对 AI 的可操作性较强，因为算法本身完全离散、精确且可自动化；但主命题的困难在于需要全局终止性或非终止性证明。GPT-5.5 级模型最可能的贡献是形成严谨的计算实验框架、发现可证明子族、验证候选不变量或缩小反例搜索空间，而不是一次性解决完整开放问题。因此评为 low_to_medium_candidate，而非 high_candidate。

### 免责声明

以上是对 AI 辅助可推进性的审查，不是问题 282 的解答，也不声称已经证明奇分母贪心算法总会终止或找到非终止反例。

<!-- MODEL_REVIEW:END -->
