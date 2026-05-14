# Problem 14

## 基本信息

- 原始链接: https://www.erdosproblems.com/14
- LaTeX 页面: https://www.erdosproblems.com/latex/14
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `sidon sets`, `additive combinatorics`
- 形式化状态: `yes`
- OEIS: `A143824`, `possible`
- 原站备注字段: 无

## 原问题

Let $A\subseteq \mathbb{N}$. Let $B\subseteq \mathbb{N}$ be the set of integers which are representable in exactly one way as the sum of two elements from $A$.

Is it true that for all $\epsilon>0$ and large $N$\[\lvert \{1,\ldots,N\}\backslash B\rvert \gg_\epsilon N^{1/2-\epsilon}?\]Is it possible that\[\lvert \{1,\ldots,N\}\backslash B\rvert =o(N^{1/2})?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `26/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：additive combinatorics, number theory, sidon sets
- 题面含渐近/无限对象线索：\gg, \ll, infinitely many, o(

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics, number theory, sidon sets
- 有限/计算线索: finite, finitely
- 渐近/无限线索: \gg, \ll, infinitely many, o(
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **这是一个低到中等候选问题：GPT-5.5 级别模型配合计算、形式化证明和文献检索，较可能给出有限模型验证、构造实验、证明片段或把已知有限 analogue 与无限问题之间的障碍梳理清楚；但直接解决原问题的概率不高。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 可行路线是把问题重写为表示函数 r_A(n) 的约束优化：要求大量 n 满足 r_A(n)=1，并估计 r_A(n)=0 或 r_A(n)>=2 的数量。模型可以先形式化有限版本，搜索小 N 的极值构造，尝试用 SAT/ILP/CP-SAT 验证最优或近最优样例，再把计数恒等式、加性能量、Sidon 型约束和边界效应组合成可机检的引理。更现实的成果是证明若干附加假设下的 N^{1/2-o(1)} 下界，或验证 Erdős-Freud 有限 analogue 常数与构造模式，而不是一次性解决完整无限问题。

### 支持理由

- 问题陈述短、对象明确，可直接转化为有限区间上的布尔选择变量和表示计数约束，适合计算搜索与形式化验证。
- 它有明确的有限 analogue：存在 A subset {1,...,N} 使非唯一表示数小于 2^{3/2}N^{1/2}，这给了模型可复现、可检验的目标尺度。
- 问题与 Sidon sets、加性组合和表示函数相关，已有工具链能处理部分计数不等式、能量估计、极值小例和自动化反例搜索。
- 要判断 o(N^{1/2}) 是否可能，计算实验可以帮助排除简单构造、发现周期或分块构造模式，并形成可证明猜想。

### 主要障碍

- 核心难点是无限集合的全局结构控制：有限区间最优或近最优并不自动给出所有大 N 的渐近下界。
- r_A(n)=1 是非常刚性的局部条件，但 complement 同时包含无表示和多重表示，两类坏点可相互抵消计数压力，简单能量法可能只给弱界。
- 备注中提到的上界构造接近 N^{1/2+epsilon}，说明目标下界若真为 N^{1/2-o(1)}，很可能需要接近最优的结构理论。
- 存在形式化版本并不意味着证明容易；Lean/Isabelle 更可能验证人工设计的引理，而难以自动发现关键组合结构。
- 若要排除 o(N^{1/2})，需要处理所有稀疏、分块、随机化或递归构造的 A，这超出纯计算枚举能力。

### 需要的验证

- 建立有限版本的精确定义：和是否有序、是否允许同一元素使用两次、A subset {1,...,N} 与 sums <=N 的边界处理必须固定。
- 对小到中等 N 运行 ILP/SAT/CP-SAT，记录最小 complement、极值 A 的结构，并与 2^{3/2}N^{1/2} 尺度比较。
- 把任何模型生成的不等式证明翻译为形式化证明或至少逐引理检查，尤其检查从有限区间到渐近大 N 的量词转换。
- 检索并核对备注中 Erdős-Freud 有限 analogue 以及 Erdős 所称构造的原始证明细节，避免基于不完整摘要误推。
- 测试候选反例构造在长区间、多尺度 N 和偏移区间上的表现，确认不是只在少数 N 上降低 complement。

### 公开版思考摘要

这个问题适合 AI 工具介入，因为它有清楚的表示函数表述、有限极值版本和可计算实验入口。GPT-5.5 很可能能搭建搜索程序、发现样例结构、形式化若干计数引理，并帮助判断哪些证明策略失败。但完整命题要求对任意无限集合 A 给出接近平方根级别的下界，且已知构造接近该尺度上界，因此关键步骤很可能是深的加性组合结构定理，而不是单纯枚举或常规能量估计。

### 免责声明

以上是对 GPT-5.5 加工具在该单一问题上的可推进性评估，不是该 Erdős 问题的解答，也不声称证明或反驳了原命题。

<!-- MODEL_REVIEW:END -->
