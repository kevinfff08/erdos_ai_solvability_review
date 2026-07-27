# Problem 949

## 基本信息

- 原始链接: https://www.erdosproblems.com/949
- LaTeX 页面: https://www.erdosproblems.com/latex/949
- 原始状态: `open`
- 奖金: `no`
- 主类别: `ramsey theory`
- 原始标签: `ramsey theory`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $S\subset \mathbb{R}$ be a set containing no solutions to $a+b=c$. Must there be a set $A\subseteq \mathbb{R}\backslash S$ of cardinality continuum such that $A+A\subseteq \mathbb{R}\backslash S$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `39/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 主要风险是候选证明或计算证书容易存在隐藏漏洞，需要独立复核。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: 无
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **有希望显著推进，甚至可能完成，但不应评为高把握可解。该题的核心不是计算规模，而是实数集上的无限组合与选择原理；GPT-5.5 级模型可系统尝试独立集/超图、向量空间基、平移避障、forcing 或形式化递归构造等路线，并可验证 Sidon 变体证明，但原题可能涉及精细集合论障碍。**
- 等级: `medium_candidate`
- 分数: `63/100`
- 信心: `medium`
- 可能路线: 把问题改写为在图 G_S 上寻找大小为 continuum 的独立集：顶点为 R\S 中满足必要条件的点，边由 x+y∈S 给出。优先尝试证明该图必有 continuum 独立集，利用 S 为 sum-free 带来的结构限制；并行探索按 Q-向量空间分解、Hamel 基/线性独立集构造、perfect set 或 transfinite recursion。工具侧可用 Lean/Isabelle 检查基础引理，用小型模型搜索反例模式，用自动定理证明器验证 AlphaProof 给出的 Sidon 变体是否可迁移到一般 sum-free 情形。

### 支持理由

- 题面长度短、结构清晰，已经 formalized=yes，适合把目标拆成图论/集合论形式并进行机器辅助证明检查。
- 已知备注中 Sidon 变体有正向证明，说明相邻问题存在可形式化的构造路线；模型可尝试定位 Sidon 条件在证明中的使用点，并判断能否弱化到 sum-free。
- sum-free 条件强烈限制 S 与 S+S 的交集，可能给平移族 S-a 的覆盖行为带来约束，这类覆盖/独立集问题适合由模型生成候选引理再用形式化工具验证。
- 该问题不依赖庞大数值计算，主要依赖抽象构造；GPT-5.5 级模型在提出等价图模型、递归构造和反例搜索框架方面有较大帮助。

### 主要障碍

- 一般 sum-free 明显弱于 Sidon；Sidon 证明中的唯一表示性质可能是关键，不能假设可直接推广。
- 实数集任意子集层面的命题可能与选择公理、基数不变量、perfect set 性质或独立性现象相关，普通有限搜索很难排除病态反例。
- 朴素递归构造会遇到障碍：每一步需避开 S、S/2 以及许多平移 S-b；这些集合都可能有 continuum 大小，不能用简单基数计数完成。
- 若要给否定答案，需要构造 sum-free S 使补集中不存在 continuum 大小的 pairwise S-sum-free 集，这可能需要复杂的几乎覆盖或 Ramsey 型构造。

### 需要的验证

- 检查 Sidon 变体证明的形式化版本，标出每处使用 Sidon 唯一表示的地方，并测试是否只需 sum-free。
- 形式化证明图论等价：A⊆R\S 且 A+A⊆R\S 等价于在由 x+y∈S 定义的图中找 continuum 独立集，同时处理 x=x 的自环条件 2x∉S。
- 尝试证明或反驳关键覆盖引理：对任意小于 continuum 的 B，集合 S∪(S/2)∪⋃_{b∈B}(S-b) 是否必不能覆盖 R，或需要额外假设。
- 若模型提出构造，应在 Lean/Isabelle 中至少验证核心代数与基数步骤；若提出反例，应验证 S sum-free、补集性质和 continuum 阻断条件。

### 公开版思考摘要

该题适合 GPT-5.5 级模型尝试，因为它可以被压缩成一个清晰的无限图独立集问题，并且已有 Sidon 变体的正向证明作为邻近路线提示。真正难点在于 sum-free 条件可能不足以控制 continuum 大小的平移覆盖，因此简单递归和有限实验都不够。综合判断是中等候选：模型很可能找到有价值的等价形式、关键引理、形式化验证或 Sidon 证明弱化尝试；是否能完整解决原题则取决于能否突破集合论/无限 Ramsey 型障碍。

### 免责声明

以上是 AI 可解性与研究路线评估，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->
