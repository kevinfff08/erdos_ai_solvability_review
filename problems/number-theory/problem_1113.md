# Problem 1113

## 基本信息

- 原始链接: https://www.erdosproblems.com/1113
- LaTeX 页面: https://www.erdosproblems.com/latex/1113
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `covering systems`
- 形式化状态: `yes`
- OEIS: `A076336`
- 原站备注字段: Sierpinski numbers

## 原问题

A positive odd integer $m$ such that none of $2^km+1$ are prime for $k\geq 0$ is called a Sierpinski number. We say that a set of primes $P$ is a covering set for $m$ if every $2^km+1$ is divisible by some $p\in P$.

Are there Sierpinski numbers with no finite covering set of primes?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `39/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：density, infinitely many, prime, primes

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: covering systems
- 证明密集标签命中: number theory
- 有限/计算线索: covering system, finite, finitely
- 渐近/无限线索: density, infinitely many, prime, primes
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 tool-augmented`
- 结论: **中等候选。该问题已有具体候选数和已知证明线索，适合用计算、SAT/SMT、代数数论验证和形式化证明来显著推进；但要给出公认的完整存在性证明，核心仍是无限覆盖系统排除问题，不能只靠有限搜索完成。**
- 等级: `medium_candidate`
- 分数: `64/100`
- 信心: `medium`
- 可能路线: 最可行路线不是从零寻找新 Sierpinski 数，而是围绕给出的候选 m=734110615000775^4 重建 Izotov 证明其为 Sierpinski 数的部分，并把“无有限 covering set”的论证改写成可验证的判定框架：对每个可能覆盖素数 p，形式化其能覆盖的 k 的同余类；用 covering-system 判定、SAT/SMT 证书和 Lean/Isabelle 形式化来排除有限并集覆盖所有 k 的可能性；同时对有限范围内的候选素数和周期结构做穷举验证，生成可审计证书。

### 支持理由

- 问题对象非常明确：固定序列 2^k m+1、素数覆盖集、同余周期，适合计算机代数和自动化定理证明介入。
- JSON 中已经给出强线索：Izotov 证明了具体 m 是 Sierpinski 数，Filaseta-Finch-Kozek 对“无 covering set”给出更详细论证或证据，这为模型提供了可复核的目标而不是完全开放的搜索空间。
- covering set 的定义可转化为有限个模周期同余类覆盖非负整数的问题，天然适合 SAT/SMT、精确整数计算、周期证书和形式化验证。
- 问题已标注 formalized=yes，说明至少已有某种形式化入口；GPT-5.5 级别模型有机会把非正式文献证明、计算证据和形式系统连接起来。
- 若目标降低为“验证候选、找出文献论证缺口、产生有限不可覆盖证书或扩大排除范围”，工具增强模型很可能有实质产出。

### 主要障碍

- 完整证明需要排除所有有限素数集合，而不是检查某个给定集合或有限素数上界；有限计算本身不足以解决存在性问题。
- “argument suggests”表明现有候选的无有限覆盖性质可能并非已被完全公认，模型必须识别并修补真正的证明缺口。
- covering systems 可以很复杂；即使每个素数只给出周期性约束，有限并集是否能覆盖所有 k 仍可能出现非局部组合结构。
- 需要严格处理所有可能覆盖素数，而这些素数不预先有简单上界；若不能证明候选覆盖素数族的结构限制，就会卡在无限情形。
- Sierpinski 性和无有限 covering set 是两个不同层次：前者可由代数恒等式或构造性覆盖证明，后者要求证明没有任何有限责任素数集。

### 需要的验证

- 复核 Izotov 对 m=734110615000775^4 为 Sierpinski 数的证明，并把每个 k 的合成性来源写成可检查的分支或证书。
- 精确定义并形式化：某素数 p 覆盖哪些 k，即 2^k m+1≡0 mod p 的可解条件和周期。
- 证明或机器验证候选 m 的所有潜在覆盖素数族不能形成有限 covering system；如果只验证到某个界，需要明确这是证据而非证明。
- 对任何 SAT/SMT 输出生成独立可验证证书，例如覆盖失败的模类证书、CRT 见证或形式证明脚本。
- 检查文献中“无 covering set”相关论证是否依赖未证明假设，例如 Fermat primes、primitive divisors、或对可容许模数集合的分类。

### 公开版思考摘要

这个问题比单纯搜索 Sierpinski 数更难，因为它要证明合成性不能由任何有限素数集合解释。不过它也不是完全无结构的开放猜想：JSON 已给出一个强候选和相关文献线索，且覆盖条件本质上是模周期覆盖问题。GPT-5.5 级别模型最有希望做的是把候选数的证明链机器化、找出并缩小“无有限覆盖”的缺口、生成可独立验证的不可覆盖证书。直接宣称解决存在性问题风险较高，但显著推进或验证具体候选是现实目标。

### 免责声明

以上是对工具增强 GPT-5.5 攻关可行性的审查，不是该 Erdős 问题的数学解答，也不声称 m=734110615000775^4 已被这里证明为无有限 covering set。

<!-- MODEL_REVIEW:END -->
