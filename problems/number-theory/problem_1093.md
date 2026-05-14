# Problem 1093

## 基本信息

- 原始链接: https://www.erdosproblems.com/1093
- LaTeX 页面: https://www.erdosproblems.com/latex/1093
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `binomial coefficients`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

For $n\geq 2k$ we define the deficiency of $\binom{n}{k}$ as follows. If $\binom{n}{k}$ is divisible by a prime $p\leq k$ then the deficiency is undefined. Otherwise, the deficiency is the number of $0\leq i<k$ such that $n-i$ is $k$-smooth, that is, divisible only by primes $\leq k$.

Are there infinitely many binomial coefficients with deficiency $1$? Are there only finitely many with deficiency $>1$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `30/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：\ll, infinitely many, prime, primes

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: binomial coefficients
- 证明密集标签命中: number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: \ll, infinitely many, prime, primes
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。GPT-5.5 配合计算与形式化工具，较可能在该问题上做出显著推进，例如扩大无例区间、验证已知例子、自动化条件化证明、提出可检验的构造或筛法；但直接无条件解决两个全局问题的可能性不高，尤其是“deficiency 1 是否无限多”可能需要新的深层数论输入。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 最可行路线是把条件“所有 p<=k 均不整除 binom(n,k)”转化为 p 进赋值等式或 Kummer 进位条件，然后对固定 k 建立严格的可验证搜索与剪枝；结合 k-smooth 数分布、光滑数间隔、覆盖同余、线性/整数约束和 SAT/SMT 搜索，系统验证 deficiency >1 的有限性在大范围内是否可推出。对于 deficiency 1 的无限性，较可能先寻找参数化族或半参数化族，并用计算发现同余模式，再尝试用筛法或条件性素数/光滑数 conjecture 证明。

### 支持理由

- 问题定义离散且可计算，核心条件可用 p-adic valuation、Kummer 定理或 Legendre 公式精确表达，适合程序化验证和形式化证明。
- 已给出上界 n << 2^k sqrt(k)，说明对固定 k 的搜索空间虽大但有限；结合剪枝、同余约束和光滑数预处理，工具型模型能有效扩大验证范围。
- 已存在少量 deficiency >1 例子和 58 个 n<=10^5 的 deficiency 1 例子，给模型提供了可回归测试的数据点，便于校验实现和寻找结构。
- 第二问已有强猜想条件下的正向结果，这表明问题可能能被拆成明确的可验证子命题；GPT-5.5 可帮助重构、形式化和弱化这些条件性路线。
- 该题已经 formalized=yes，因此至少部分定义或定理环境可进入 proof assistant，降低了验证计算证明、边界检查和等价变换的风险。

### 主要障碍

- 无限多 deficiency 1 需要构造无限族或证明某类稀有组合条件无限发生；这通常涉及光滑数、素因子分布和二项系数局部整除条件的深层耦合。
- deficiency >1 的有限性若要无条件证明，需要排除所有大 k 的多重 k-smooth 命中；现有 n 上界仍呈指数级，单纯穷举不足以完成全局证明。
- 光滑数在短区间中的分布很细，当前通用定理可能不足以处理这里长度为 k、位置约为最高 2^k sqrt(k) 的特殊窗口。
- 工具搜索容易产生强经验规律，但把规律提升为无条件定理可能需要新的筛法或对相关 Diophantine 结构的深刻分析。
- 条件性结果依赖两个强猜想，说明无条件路线可能卡在当前数论知识边界，而不是仅卡在计算规模。

### 需要的验证

- 先独立实现 deficiency 判定，并用题目列出的 deficiency 1、2、3、4、9 例子全部回归验证。
- 对固定 k 的搜索需给出可审计证书：光滑数列表、p-adic 条件检查、剪枝正确性证明以及边界 n << 2^k sqrt(k) 的使用方式。
- 若声称排除某范围内 deficiency >1，需要形式化或至少可复现地证明没有遗漏 n>=2k、没有遗漏小素数整除情形。
- 若发现 deficiency 1 的候选无限族，需要验证其二项系数小素数不整除条件，而不只是验证窗口内恰有一个 k-smooth 数。
- 任何基于猜想的结论必须明确列出猜想形式、依赖位置，以及无条件可保留的部分。

### 公开版思考摘要

这个问题对 AI 工具友好的一面是定义精确、可计算、已有有限上界和已知样例，适合把数论条件转成可验证的同余与 p 进约束，并由搜索生成证据或反例候选。难点在于两个核心问题都是全局性陈述：一个要求无限构造，另一个要求最终排除所有大参数。GPT-5.5 很可能能显著推进计算验证、条件证明整理、形式化检查和模式发现，但要无条件完整解决，仍需要突破光滑数短区间分布与二项系数整除结构之间的深层障碍。

### 免责声明

以上是对 GPT-5.5 级别模型辅助攻关可行性的审查，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->
