# Problem 665

## 基本信息

- 原始链接: https://www.erdosproblems.com/665
- LaTeX 页面: https://www.erdosproblems.com/latex/665
- 原始状态: `open`
- 奖金: `no`
- 主类别: `combinatorics`
- 原始标签: `combinatorics`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

A pairwise balanced design for $\{1,\ldots,n\}$ is a collection of sets $A_1,\ldots,A_m\subseteq \{1,\ldots,n\}$ such that $2\leq \lvert A_i\rvert <n$ and every pair of distinct elements $x,y\in \{1,\ldots,n\}$ is contained in exactly one $A_i$.

Is there a constant $C>0$ and, for all large $n$, a pairwise balanced design such that\[\lvert A_i\rvert > n^{1/2}-C\]for all $1\leq i\leq m$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `23/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序

### 主要障碍

- 题面含渐近/无限对象线索：\ll, for all large, prime, primes, sufficiently large

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: combinatorics
- 证明密集标签命中: 无
- 有限/计算线索: 无
- 渐近/无限线索: \ll, for all large, prime, primes, sufficiently large
- 构造/存在性线索: find, is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不宜评为高可解候选。GPT-5.5 级别模型配合工具较可能做出有价值的条件化推进、文献结构化、有限范围验证和构造/反例搜索，但直接给出无条件最终答案的概率偏低；主要原因是题目核心被 remarks 明确连接到射影平面阶是否均为素数幂这类深层组合设计问题。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 较现实的路线不是直接证明存在或不存在常数 C，而是围绕近射影平面结构做三类工作：第一，形式化并复核 Shrikhande-Singhi 型嵌入定理在“所有块大小至少 sqrt(n)-c”条件下的精确适用范围；第二，把问题转化为关于相邻可行射影平面阶、素数幂间隙或 prime gap 的定量命题，检验给定 C 会强迫哪些阶存在；第三，用整数规划、SAT/CP-SAT、PBD 生成算法和有限几何构造搜索小到中等规模样例，寻找可能的反例模式或验证已知构造边界。

### 支持理由

- 题目陈述非常明确，适合被编码为 PBD 约束：每对点恰在一个块中、块大小下界接近 sqrt(n)，因此计算搜索和形式化验证都有清晰入口。
- remarks 已给出强结构信息：Erdos-Larson 已有 h(n) 的次幂级上界，且在 Cramer 型素数间隙假设下可改进到 polylog 级，这说明该问题可以被拆成构造边界与数论间隙两个可审计子问题。
- remarks 还说明在“射影平面阶均为素数幂”猜想下答案为否，并且近最优 PBD 会嵌入到附近阶的射影平面中；这为 AI 提供了可验证的条件性路线，而不是完全无结构的开放题。
- 工具型模型可显著贡献于整理参数、检查不等式常数、验证嵌入定理的边界条件、搜索小规模设计，以及把已有结果形式化为 Lean/Isabelle 或可机检的组合计数引理。

### 主要障碍

- 无条件最终解决很可能需要绕开或推进射影平面阶的经典难题；若要证明否定答案，现有 remarks 暗示会触及 prime-power conjecture 类障碍。
- 若要证明肯定答案，需要为所有充分大的 n 构造块大小统一大于 sqrt(n)-C 的 PBD，这比已知的次幂级或条件 polylog 级误差强很多。
- 常数 C 的存在性是极细的渐近问题，普通有限搜索只能提供证据，难以覆盖“所有大 n”。
- PBD 的可行性约束高度离散，接近 sqrt(n) 的块大小又迫使结构近似射影平面，留给自由构造的空间可能很小。
- 题目中的关键外部结果需要精确版本；仅凭 remarks 无法判断常数、阈值和嵌入结论是否足以推出某个无条件替代命题。

### 需要的验证

- 检索并核对 Erdos-Larson 1982 与 Shrikhande-Singhi 1985 的原文，确认 h(n) 上界、嵌入定理、常数依赖和“充分大 n”的精确表述。
- 形式化基础计数约束，例如块大小下界对块数、点度、 Fisher 型不等式和近等号结构的影响。
- 建立可复现实验：对有限 n 用 SAT/ILP/CP-SAT 搜索满足下界的 PBD，记录不可行证书或构造证书。
- 验证从 prime gap、素数幂间隙到 h(n) 的推导是否只在 prime-power conjecture 下成立，避免把条件结论误当作无条件结论。
- 若声称推进，需要给出机检证明、可复现实验脚本，或明确的新引理及其对原问题 C 常数版本的逻辑贡献。

### 公开版思考摘要

该问题有清晰的组合设计形式，适合计算搜索和形式化检查；同时 remarks 显示它并非孤立难题，而是与近射影平面嵌入、素数间隙和射影平面阶猜想紧密相连。因此，GPT-5.5 级别系统最可能完成的是条件化定理复核、参数 sharpen、有限规模反例搜索和已知路线的形式化，而不是直接无条件解决。总体判断为低到中等候选：有推进空间，但最终突破概率受经典组合设计障碍限制。

### 免责声明

以上是对 AI 工具辅助研究可行性的审查，不是该 Erdős 问题的解答，也不声称证明存在或不存在这样的常数 C。

<!-- MODEL_REVIEW:END -->
