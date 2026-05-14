# Problem 837

## 基本信息

- 原始链接: https://www.erdosproblems.com/837
- LaTeX 页面: https://www.erdosproblems.com/latex/837
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `hypergraphs`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $k\geq 2$ and $A_k\subseteq [0,1]$ be the set of $\alpha$ such that there exists some $\beta(\alpha)>\alpha$ with the property that, if $G_1,G_2,\ldots$ is a sequence of $k$-uniform hypergraphs with\[\liminf \frac{e(G_n)}{\binom{\lvert G_n\rvert}{k}} >\alpha\]then there exist subgraphs $H_n\subseteq G_n$ such that $\lvert H_n\rvert \to \infty$ and\[\liminf \frac{e(H_n)}{\binom{\lvert H_n\rvert}{k}} >\beta,\]and further that this property does not necessarily hold if $>\alpha$ is replaced by $\geq \alpha$.

What is $A_3$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `41/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：liminf

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, hypergraphs
- 证明密集标签命中: 无
- 有限/计算线索: graph, hypergraph
- 渐近/无限线索: liminf
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能完整解决，但有中等偏低概率显著推进或严谨验证局部结论。该题本质上是在问 3-一致超图的 Erdős-Simonovits jump 集合 A_3，属于极值超图密度结构问题；现有 JSON 已表明 A_2 有完整刻画而 A_3 仍 open，说明三元超图情形很可能缺少统一结构定理。GPT-5.5 配合计算、SAT/Flag algebra、形式化证明和文献检索，较可能产出候选区间、有限构型证书、反例搜索结果或把问题转化为可验证的有限优化问题，但不应预期一次性给出完整 A_3。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 较现实的路线是把题目重述为 3-一致超图密度 jump 问题，先形式化“> alpha”和“>= alpha”之间的临界差异；随后用 flag algebra/半定规划搜索证明若干 alpha 为 jump，或用 blow-up、随机/伪随机构造、有限模板搜索证明若干 alpha 非 jump。对候选临界密度，可让模型生成有限 forbidden family 或 extremal construction，再用计算机辅助 SDP 证书、SAT/ILP 小规模穷举和 Lean/Isabelle 局部形式化来验证。

### 支持理由

- 问题定义清晰，适合被拆成“证明某个 alpha 属于 A_3”和“构造某个 alpha 不属于 A_3”的可验证子任务。
- 3-一致超图极值问题常可通过 blow-up 模板、拉格朗日量、flag algebra 和有限构型搜索获得实质性进展，工具增强型模型可以参与生成猜想和证书。
- 题目只要求 A_3，但完整集合刻画可能需要识别临界密度族；模型可先推进有限区间、特殊有理点或已知构造类。
- “> alpha 与 >= alpha 的差别”提供了一个可形式化的边界条件，便于检查候选证明是否真正满足题意。

### 主要障碍

- 三元超图没有类似图情形 Erdős-Stone-Simonovits 的完整通用结构定理，完整刻画 A_3 可能需要新理论。
- 非 jump 方向通常需要无限序列构造，既要全局密度趋近 alpha，又要排除所有大子图密度超过 beta，这比有限反例搜索困难得多。
- flag algebra/SDP 证书只能覆盖具体密度或有限模式，难以直接给出整个集合 A_3。
- 题目中的 liminf、任意超图序列和任意大子图量词很强，容易产生看似合理但量词不闭合的伪证明。

### 需要的验证

- 把 A_3 的定义严格形式化，明确 alpha 属于 A_3 时 beta(alpha) 的存在量词和 >= alpha 失败条件。
- 对每个声称属于 A_3 的密度，提供可复查的解析证明或计算机辅助证书，并验证证书误差界。
- 对每个声称不属于 A_3 的密度，给出无限超图序列构造，并证明任意趋于无穷的子图密度不能统一超过 alpha。
- 用小规模穷举、ILP/SAT 和 flag algebra 独立复核候选 extremal examples，避免仅凭数值优化输出下结论。
- 若提出完整 A_3 刻画，需要证明候选集合两侧的覆盖性，而不仅是若干样例点。

### 公开版思考摘要

该问题的核心难度不在定义理解，而在三元超图极值密度的全局刻画。GPT-5.5 级别模型可以有效承担文献定位、等价表述整理、构造搜索、flag algebra 证书生成和局部形式化验证，因此有机会显著推进若干候选密度或发现反例模式。但完整回答“什么是 A_3”很可能需要新的理论结构，超出当前模型稳定独立解决的范围。

### 免责声明

以上是对工具增强型 GPT-5.5 解决潜力的审查判断，不是 Problem 837 的数学解答，也未声称给出了 A_3 的刻画。

<!-- MODEL_REVIEW:END -->
