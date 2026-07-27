# Problem 190

## 基本信息

- 原始链接: https://www.erdosproblems.com/190
- LaTeX 页面: https://www.erdosproblems.com/latex/190
- 原始状态: `open`
- 奖金: `no`
- 主类别: `additive combinatorics`
- 原始标签: `additive combinatorics`, `arithmetic progressions`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $H(k)$ be the smallest $N$ such that in any finite colouring of $\{1,\ldots,N\}$ (into any number of colours) there is always either a monochromatic $k$-term arithmetic progression or a rainbow arithmetic progression (i.e. all elements are different colours). Estimate $H(k)$. Is it true that\[H(k)^{1/k}/k \to \infty\]as $k\to\infty$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `36/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索

### 主要障碍

- 所属标签偏证明密集：additive combinatorics, arithmetic progressions

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics, arithmetic progressions
- 有限/计算线索: chromatic, colouring, finite, ramsey
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **有一定推进潜力，但完整解决概率偏低。GPT-5.5 配合 SAT/CP-SAT 搜索、构造生成、形式化验证和文献检索，较可能改进小 k 数据、发现或验证新的下界构造、整理现有 canonical Ramsey 理论给出的上界框架；但要证明所问极限 H(k)^{1/k}/k -> infinity 或给出尖锐估计，仍需要新的渐近构造或结构定理，难度明显高于常规工具化推导。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 最现实路线是把问题转化为避免两类坏事件的有限着色构造：一方面用 SAT/约束规划/局部搜索为小 k 搜索最长无单色 k-AP 且无彩虹 k-AP 的着色，提取可扩展模式；另一方面用 canonical Ramsey、Szemeredi 型密度结果和反彩虹约束建立可机检的上下界证明。若发现递归或代数构造，可用证明助理或独立程序验证其避免性质，再尝试推广为渐近下界。

### 支持理由

- 问题定义清晰，有限形式适合计算搜索：给定 k,N，可直接编码是否存在一种着色同时避免单色与彩虹 k 项等差数列。
- 小规模数据和极值构造很适合由模型驱动的 SAT、MIP、CP-SAT、局部搜索、同构约简与证书验证共同推进。
- 题目属于 canonical Ramsey theory，已有存在性和弱增长结论可作为上界/基线框架，模型可通过文献检索整合相关定理而不是从零开始。
- 目标不是单个反例，而是渐近估计；若计算发现稳定构造族，AI 有机会把模式转化为可验证的递归下界。
- 形式化证明可用于验证有限证书、递推构造的避免性质，以及把若干组合引理做成可靠的检查链。

### 主要障碍

- 核心问题是渐近强下界 H(k)^{1/k}/k -> infinity，需要构造长度远超 (Ck)^k 的着色族或证明相反上界；这通常不是小规模搜索可直接外推的。
- 颜色数任意，导致状态空间和结构空间很大；需要同时控制单色 AP 与彩虹 AP，两种约束方向相反。
- Szemeredi 定理只给存在性和很粗的上界，未必接近该问题的真实量级。
- 计算搜索容易产生仅适用于小 k 的偶然模式，推广证明可能失败。
- 若要证明否定方向，则需构造通用强上界，可能涉及深层 canonical Ramsey 或高阶正则性工具，自动化程度有限。

### 需要的验证

- 对固定 k,N 的搜索编码必须有独立验证器，检查所有 k 项等差数列均非单色且非彩虹。
- 需要与已知 canonical Ramsey、anti-Ramsey、Van der Waerden/Szemeredi 相关结果核对，避免重新发现弱结论或错误引用。
- 任何计算发现的构造族都需要给出参数化定义，并证明对所有 k 或无限多个 k 成立。
- 若提出上界，需要明确依赖的密度定理常数和颜色类/彩虹约束转化是否无漏洞。
- 应形式化或至少机器验证关键有限归纳步骤，尤其是递归构造的边界条件和 AP 保持性质。

### 公开版思考摘要

这个问题的可工具化程度较高，因为有限版本能被精确搜索和验证，且已有 canonical Ramsey 背景可提供理论入口。GPT-5.5 级模型很可能能生成有价值的数据、证书、候选构造和部分上下界整理；但题目真正询问的是强渐近增长，要求把有限实验提升为一般构造或结构定理。综合判断，它适合作为 AI 辅助推进对象，而不是高概率一次性解决对象。

### 免责声明

以上只是对 GPT-5.5 级别模型辅助研究可行性的审查，不是该 Erdős 问题的解答，也不声称证明或否定所给极限命题。

<!-- MODEL_REVIEW:END -->
