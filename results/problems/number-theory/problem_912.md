# Problem 912

## 基本信息

- 原始链接: https://www.erdosproblems.com/912
- LaTeX 页面: https://www.erdosproblems.com/latex/912
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `factorials`
- 形式化状态: `yes`
- OEIS: `A071626`
- 原站备注字段: 无

## 原问题

If\[n! = \prod_i p_i^{k_i}\]is the factorisation into distinct primes then let $h(n)$ count the number of distinct exponents $k_i$.

Prove that there exists some $c>0$ such that\[h(n) \sim c \left(\frac{n}{\log n}\right)^{1/2}\]as $n\to \infty$.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `27/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：factorials, number theory
- 题面含渐近/无限对象线索：prime, primes
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: factorials, number theory
- 有限/计算线索: 无
- 渐近/无限线索: prime, primes
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 with computation, formal proof assistants, literature search, and counterexample search`
- 结论: **可显著推进但不太可能完整解决。该问题已有阶数量级结果，目标是把 distinct valuations 的阶估计提升为带极限常数的渐近式；这通常需要比 Cramér 启发更强的素数间隔、局部分布和相关性控制。GPT-5.5 级别模型可帮助形式化分解、数值验证常数、检验启发模型、寻找条件性定理，但直接给出无条件证明的概率偏低。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 最现实路线是把 h(n) 转化为素数落入由 v_p(n!) 诱导的短区间族的问题：先分离 p>sqrt(n) 的主贡献区和 p<=sqrt(n) 的误差区；对每个可能指数 k 分析是否存在素数 p 使 floor(n/p)+floor(n/p^2)+...=k；用计算实验估计 h(n)/sqrt(n/log n) 是否趋向 sqrt(2pi)，并尝试在 Cramér 或更强素数分布假设下证明条件性渐近式。无条件方向可能需要把 Erdős-Selfridge 的上下界技术强化为二阶密度估计或极限存在性证明。

### 支持理由

- 问题结构清晰：v_p(n!) 由 Legendre 公式给出，可被精确计算、形式化和实验验证。
- 已有 h(n) asymp sqrt(n/log n) 的上下界，说明尺度已经被锁定，AI 可以围绕常数和极限存在性集中工作。
- Tao 的 Cramér 模型启发给出候选常数 sqrt(2pi)，适合用概率模型、模拟和条件性证明来检验。
- formalized=yes 表明至少定义和部分基础陈述可能已有形式化入口，利于证明检查、边界条件验证和机械化辅助。
- 该问题不像完全无结构的猜想；它与素数短区间命中问题、阶乘 p-adic valuation 和随机覆盖模型有明确连接。

### 主要障碍

- 核心难点不是计算 h(n)，而是证明 distinct exponent 集合的极限密度常数存在。
- 主项依赖许多短区间是否含素数，这触及素数间隔和局部分布的精细统计；现有无条件工具通常难以达到 Cramér 级别。
- 不同 k 对应的区间事件并非独立，Legendre 公式中的高阶 floor(n/p^j) 项还会引入系统性偏移。
- Erdős-Selfridge 已给出正确阶，进一步得到渐近常数可能需要新的平均化或相关性消除思想，而不只是技术整理。
- 计算实验可强烈支持常数，但对无条件证明的转化能力有限。

### 需要的验证

- 实现高精度 h(n) 计算，覆盖尽可能大的 n，检验 h(n)/sqrt(n/log n) 的收敛趋势和有限尺度偏差。
- 独立验证 p>sqrt(n) 主区间与 p<=sqrt(n) 小素数区的贡献量级，确认后者不会改变主常数。
- 在 Cramér 模型或可陈述的素数随机模型下写出完整条件性推导，检查是否真的给出 c=sqrt(2pi)。
- 检索并复核 Erdős-Selfridge 原证明中上下界的关键损失位置，判断是否有可被现代短区间素数结果改进的环节。
- 若声称无条件证明，需要形式化或半形式化核查所有素数区间覆盖、误差项一致性和相关性估计。

### 公开版思考摘要

这个问题的可攻性来自它的明确算术表达式和已知正确数量级；AI 工具可以把问题拆成可计算、可形式化、可概率建模的子问题，并可能产出条件性证明或新的数值证据。但目标渐近常数需要精细素数分布信息，明显超出普通自动推理和 brute-force 搜索能力。因而它适合作为“显著推进/验证启发”的候选，而不是高概率完整解决的候选。

### 免责声明

以上是对 GPT-5.5 级别模型辅助研究可行性的审查，不是该 Erdős 问题的证明，也不声称已经建立所需渐近式。

<!-- MODEL_REVIEW:END -->
