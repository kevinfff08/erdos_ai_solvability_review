# Problem 940

## 基本信息

- 原始链接: https://www.erdosproblems.com/940
- LaTeX 页面: https://www.erdosproblems.com/latex/940
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `yes`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $r\geq 3$. A number $n$ is $r$-powerful if for every prime $p$ which divides $n$ we have $p^r\mid n$.

Are there infinitely many integers which are not the sum of at most $r$ many $r$-powerful numbers? Does the set of integers which are the sum of at most $r$ $r$-powerful numbers have density $0$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `29/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：density, infinitely many, prime

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: density, infinitely many, prime
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5-level model with computation, proof assistant, literature search, and counterexample search tools`
- 结论: **低到中等候选。该题可以被模型显著推进为结构化的计算实验、形式化定义与有限验证、以及若干可审计的条件性或局部结果，但完整解决尤其是密度为 0 的断言很不适合作为 GPT-5.5 级别模型的高把握目标。**
- 等级: `low_to_medium_candidate`
- 分数: `32/100`
- 信心: `high`
- 可能路线: 较现实的路线是把问题拆成三个可验证方向：第一，形式化 r-powerful 数与 r 项和集，建立计数上界、表示数与碰撞数之间的关系；第二，对固定 r，尤其 r=3，做大规模枚举和模约束搜索，寻找无限反例可能需要的局部或筛法结构；第三，检索并复核关于 powerful numbers、三立方和、稀疏序列和集、circle method 与 additive energy 的文献，尝试得到比朴素 O(N) 计数更强的 o(N) 覆盖上界。

### 支持理由

- 题目定义简洁且已形式化，适合 proof assistant 中精确编码、有限范围验证和机器检查引理。
- r-powerful 数本身是稀疏序列，模型可用计算和解析数论工具建立启发式、实验数据和候选上界。
- 该问题有明确的失败点可审查：Erdős 所称的简单计数论证存在错误，模型可尝试定位并形式化说明为什么朴素计数不足。
- 工具辅助可以系统搜索模障碍、覆盖缺口、表示数分布和小 r 的数据，这些结果即使不是证明，也可能显著澄清问题结构。

### 主要障碍

- 对 r=3，备注指出连“至多三个立方数之和的集合密度为 0”都未知；而三立方和是三重 3-powerful 和集的子问题方向上的核心障碍信号。
- 朴素计数只给出至多 r 个 r-powerful 数和的数量级可能为 O(N)，不足以推出密度 0；需要非平凡的碰撞、筛法或指数和节省。
- 模障碍未必存在或很可能不足以解决密度问题，因为 r-powerful 数在许多模数上的可达残基可能很丰富。
- 完整证明可能需要当前解析数论中仍困难的少变量 Waring 型问题技术，超出纯自动推理和有限搜索的可靠范围。

### 需要的验证

- 用程序验证固定 r 和大范围 N 下的可表示集合规模、缺口数量、表示数分布和增长趋势。
- 在 Lean/Isabelle 等系统中形式化 r-powerful 定义、和集定义、基本计数引理以及任何候选筛法引理。
- 复核 Erdős、Baker-Brüdern、Heath-Brown 等相关结果在本题语境中的确切适用范围，避免把 r=2 或 r+1 项结果误用于本题。
- 若发现模障碍或筛法候选证明，需要独立验证其对所有整数而非有限样本成立，并检查是否处理了“至多 r 项”和包含 1 的边界情况。

### 公开版思考摘要

该问题的主要难点不是定义复杂，而是朴素稀疏性不足以推出密度为 0。对 r-powerful 数，单个集合很稀疏，但取 r 重和后计数指数正好达到线性量级，因此必须证明大量和发生碰撞或存在深层限制。备注中特别指出 r=3 已触及三立方和的长期困难，这强烈降低了自动完整求解的可能性。GPT-5.5 级别模型更可能贡献的是系统化实验、形式化框架、错误计数论证的审计，以及局部或条件性推进。

### 免责声明

以上不是该 Erdős 问题的解答，也不声称证明了无限多不可表示整数或密度为 0；它只是对 GPT-5.5 级别工具增强模型处理该单一问题的可行性评估。

<!-- MODEL_REVIEW:END -->
