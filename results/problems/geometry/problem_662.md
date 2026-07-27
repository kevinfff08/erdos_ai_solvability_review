# Problem 662

## 基本信息

- 原始链接: https://www.erdosproblems.com/662
- LaTeX 页面: https://www.erdosproblems.com/latex/662
- 原始状态: `open`
- 奖金: `no`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: ambiguous statement

## 原问题

Consider the triangular lattice with minimal distance between two points $1$. Denote by $f(t)$ the number of distances from any points $\leq t$. For example $f(1)=6$, $f(\sqrt{3})=12$, and $f(3)=18$.

Let $x_1,\ldots,x_n\in \mathbb{R}^2$ be such that $d(x_i,x_j)\geq 1$ for all $i\neq j$. Is it true that, provided $n$ is sufficiently large depending on $t$, the number of distances $d(x_i,x_j)\leq t$ is less than or equal to $f(t)$ with equality perhaps only for the triangular lattice?

In particular, is it true that the number of distances $\leq \sqrt{3}-\epsilon$ is less than $1$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `21/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 目前只能依靠通用数学推理、文献归纳和特殊情形探索

### 主要障碍

- 所属标签偏证明密集：distances, geometry
- 题面含渐近/无限对象线索：sufficiently large
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: distances, geometry
- 有限/计算线索: 无
- 渐近/无限线索: sufficiently large
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **按给定 JSON 的字面陈述，这不是一个可直接判定的良构数学问题；GPT-5.5 级别模型最可能完成的是澄清、形式化候选版本、发现字面反例或内部矛盾，并为后续修订版建立计算与证明框架，而不是直接解决原题。**
- 等级: `not_applicable_meta_mathematical`
- 分数: `18/100`
- 信心: `high`
- 可能路线: 可行路线是先把题面中的对象类型分开：f(t) 到底计数的是三角晶格中某点半径 t 内的邻点数、距离值种类数、还是有限点集中的短边数；再检查给出的数值 f(1)=6、f(sqrt(3))=12、f(3)=18 与三角晶格距离壳层是否一致。随后枚举若干可能修订版，例如最大短边度数、平均短边度数、单位距离图边数或 distinct distances 版本，并对每个版本做小规模反例搜索、packing 约束建模、圆盘图/接触图分析和可形式化证明尝试。

### 支持理由

- 题面和 remarks 已明确标注 ambiguous statement，并说明按字面解释不合理，因此首要任务是判定和修复命题，而非证明。
- 给出的样例数值暗示 f(t) 更像是晶格某点邻点计数而不是距离种类数；但正文又说有限点集中“number of distances d(x_i,x_j) <= t”，这在字面上可能表示边数、距离值数或局部邻点数，三者结论完全不同。
- 字面版本很可能很快出现反例或类型错误：若计数总短边数，它通常随 n 增长，不可能被常数 f(t) 统一上界；若计数 distinct distances，则“少于 1 个距离 <= sqrt(3)-epsilon”也与允许单位距离点对相冲突。
- GPT-5.5 配合计算工具适合做该题的清理工作：三角晶格壳层枚举、有限 packing 反例搜索、MILP/SAT/SMT 建模、形式化定义检查，以及把每个候选命题转成可验证子命题。

### 主要障碍

- 原题没有唯一数学含义；在未确定 intended statement 前，任何“证明”都可能证明了错误版本。
- f(3)=18 与常见三角晶格欧氏距离壳层解释存在明显张力，可能有 t 的 typo 或距离平方/距离本身混用。
- “number of distances”缺少全局、局部、平均、无序点对数、distinct values 等限定，导致上界量级从常数到线性甚至二次都可能不同。
- “equality perhaps only for the triangular lattice”对有限点集也需要精确定义：是局部极值、渐近密度、周期 packing，还是极限构型。

### 需要的验证

- 需要先恢复原始意图：核对题面中 f(t)、t_n、f(3)=18 和“less than 1”的可能 typo，但本次审查不能依赖 JSON 之外材料。
- 需要为每个候选修订版写出严格形式化定义，包括计数对象、是否按点取最大值或平均值、是否考虑 distinct distances、以及 n 足够大时的量词顺序。
- 需要用程序枚举小规模 packing 或距离图，寻找候选版本的反例，尤其是 t < sqrt(3)、t=1、t=sqrt(3) 附近。
- 若形成可信修订版，还需要结合平面 packing、kissing number、Delaunay/Voronoi 分解或单位圆图极值理论给出可审计证明，最好再用 Lean/Isabelle 或独立脚本验证关键有限配置。

### 公开版思考摘要

这个条目的核心难点不是高阶技巧暂时缺失，而是题面本身没有定义清楚。GPT-5.5 很可能能显著推进“问题修复”：指出字面解释的矛盾，提出少数合理候选命题，并通过计算搜索排除或支持这些候选。但在只允许使用当前 JSON 的条件下，不能把它评为一个可直接求解的开放问题。

### 免责声明

以上不是对 Erdős problem 662 的证明或反证；由于原陈述含混甚至可能有 typo，本审查只评估 AI 对澄清、形式化、反例搜索和验证工作的潜在贡献。

<!-- MODEL_REVIEW:END -->
