# Problem 119

## 基本信息

- 原始链接: https://www.erdosproblems.com/119
- LaTeX 页面: https://www.erdosproblems.com/latex/119
- 原始状态: `open`
- 奖金: `$100`
- 主类别: `analysis`
- 原始标签: `analysis`, `polynomials`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $z_i$ be an infinite sequence of complex numbers such that $\lvert z_i\rvert=1$ for all $i\geq 1$, and for $n\geq 1$ let\[p_n(z)=\prod_{i\leq n} (z-z_i).\]Let $M_n=\max_{\lvert z\rvert=1}\lvert p_n(z)\rvert$.

Is it true that $\limsup M_n=\infty$?

Is it true that there exists $c>0$ such that for infinitely many $n$ we have $M_n > n^c$?

Is it true that there exists $c>0$ such that, for all large $n$,\[\sum_{k\leq n}M_k > n^{1+c}?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `28/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：analysis
- 题面含渐近/无限对象线索：\ll, for all large, infinitely many, limsup
- 原记录含奖金 $100，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: polynomials
- 证明密集标签命中: analysis
- 有限/计算线索: finite, finitely
- 渐近/无限线索: \ll, for all large, infinitely many, limsup
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5-level model with computation/formalization/literature tools`
- 结论: **这是一个低到中等候选问题：模型很可能能整理并验证已知的前两部分、复现若干计算实验、探索第三问的可行路线和潜在反例结构；但要独立解决第三个仍公开的问题，成功概率不高。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 可行路线应聚焦第三问：把问题转化为单位圆上对数势或三角多项式的下界问题，结合已知的 Wagner/Beck 型最大值增长结果，尝试证明大峰值会在足够多的相邻 k 上产生可累积贡献；同时用计算搜索构造低 M_k 序列，检验是否可能存在长期接近线性和的反例。形式化证明工具可用于验证辅助引理，例如 Jensen 公式、L^p 到 L^∞ 估计、乘上一个线性因子后 M_k 的局部变化界等。

### 支持理由

- 题面已说明前两问已有非平凡正向结果，因此该问题不是完全无入口；模型可复现并组织这些路线，作为第三问的基线。
- 对象定义清晰且已形式化，适合把局部不等式、范数估计和有限计算搜索接入证明检查器或数值验证流程。
- 第三问是关于 \sum_{k\le n}M_k 的平均增长，可能比逐点最大值结果更适合通过能量分布、峰值传播或分块论证推进。
- 计算工具可以搜索极小化 M_k 的根序列，帮助发现 Linden 型构造的行为是否接近第三问障碍。

### 主要障碍

- 第三问仍标注为似乎公开，且已有构造能让 M_n 显著低于线性增长，说明简单的系数、Mahler 测度或最大模原理估计远远不够。
- Beck 的 \max_{n\le N}M_n>N^c 只保证稀疏峰值，不能直接推出部分和超过 n^{1+c}；核心缺口是把稀疏大值转化为足够密集的贡献。
- 根序列完全任意且可自适应选择，反例搜索空间很大，数值优化容易产生误导性有限样本。
- 即使找到强实验规律，也需要非渐近常数、无限序列紧致性或递推稳定性论证，形式化成本较高。

### 需要的验证

- 核对 formalized 版本是否覆盖三问以及已知定理引用，而不是只形式化定义或较弱命题。
- 复现 Beck 型下界与 Linden 型上界构造的关键引理，确认第三问不能由现有结果直接推出。
- 进行针对第三问的数值优化：最小化 \sum_{k\le n}M_k 或平均 M_k，并检查最优序列的结构是否稳定。
- 若提出证明路线，需要用独立证明检查或严密手稿验证峰值传播、分块累积和极限过渡步骤。

### 公开版思考摘要

该问题的已解决部分给了模型可利用的理论脚手架，但真正剩余的是第三个平均增长问题。它看起来不像纯计算即可攻破的问题，因为必须处理任意无限单位圆根序列并获得渐近下界。GPT-5.5 级别系统更现实的贡献是复现文献、发现等价命题、测试极端构造、验证局部引理，并可能给出有价值的部分推进；完整解决第三问属于低概率但非零概率事件。

### 免责声明

以上是对 AI 辅助可解性和推进潜力的审查，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->
