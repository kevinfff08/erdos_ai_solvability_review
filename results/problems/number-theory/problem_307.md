# Problem 307

## 基本信息

- 原始链接: https://www.erdosproblems.com/307
- LaTeX 页面: https://www.erdosproblems.com/latex/307
- 原始状态: `verifiable`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `unit fractions`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Are there two finite sets of primes $P,Q$ such that\[1=\left(\sum_{p\in P}\frac{1}{p}\right)\left(\sum_{q\in Q}\frac{1}{q}\right)?\]

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `64/100`
- 建议路线: 优先搜索有限证书；若找到证书，再做独立程序验证和形式化复核。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：prime, primes

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: unit fractions
- 证明密集标签命中: number theory
- 有限/计算线索: finite
- 渐近/无限线索: prime, primes
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **这是一个中等偏高候选问题：GPT-5.5 级模型不应被期待直接给出完整定理级解决，但很可能能在构造搜索、同余剪枝、形式化验证和弱化版本分析上显著推进。若存在较小或结构化例子，工具增强模型有现实机会找到；若答案是否定的，则全局排除会困难得多。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 最可能的有效路线是把问题转成精确有理数/整数约束搜索：枚举候选素数集合的倒数和，用分支定界、模素数约束、分母整除条件和 meet-in-the-middle 搜索缩小空间；对发现的候选等式生成可机器检查证书。若长期无构造，则尝试证明必要条件，例如 P,Q 必须不交、倒数和范围、集合大小下界、局部模障碍，以及能否把无限搜索化为有限区间搜索。形式化证明系统可用于验证剪枝引理和候选等式，但自动发现全局证明仍是主要难点。

### 支持理由

- 问题陈述短、目标等式完全精确，任何正例都可由有限素数集合直接验证，适合计算搜索和形式化证书。
- 备注已经给出强约束：若 P,Q 都是素数集合，则二者不交，且并集倒数和至少为 2，从而总规模至少 60；这说明朴素小规模搜索可排除，但也给了可编码的剪枝条件。
- 弱化的互素版本已有若干例子，说明附近结构不是完全空洞；模型可研究这些例子的生成机制，尝试迁移到素数版本或证明迁移失败。
- 该问题属于有限集合的单位分数/素数倒数方程，适合用精确整数算术、SAT/SMT、CP-SAT、meet-in-the-middle、模筛和自动验证组合推进。
- 由于 status 为 verifiable 且 formalized 为 yes，工具链可以较可靠地检查候选答案、反例搜索日志和局部证明步骤，降低幻觉风险。

### 主要障碍

- 搜索空间极大：已知下界要求至少约 60 个素数参与，直接枚举素数子集不可行。
- 若不存在解，需要排除任意大小、任意大素数集合的可能性，这通常远超单纯计算搜索。
- 倒数素数和可以非常稠密地逼近实数，数值近似几乎无用，必须全程使用精确有理数或同余/分母结构。
- 局部剪枝可能很强但难以完备；模型容易发现很多必要条件，却难以证明这些条件足以排除全部情况。
- 弱化互素版本含有 1 的正例不能直接转化为素数版本；没有 1 的弱化版本也无已知例子这一点提示核心障碍可能很深。

### 需要的验证

- 所有候选 P,Q 必须用精确有理数验证等式，不能接受浮点近似。
- 搜索程序需要记录素数范围、集合大小范围、剪枝规则、完备性声明和未覆盖区域。
- 每个剪枝引理应在证明助手或至少独立脚本中复核，尤其是涉及分母整除、模约束和上下界的步骤。
- 若声称无解，必须说明如何处理任意大素数与任意集合大小；只覆盖有限范围不能算解决原问题。
- 应对弱化互素版本的构造做独立复验，并明确哪些性质在素数版本中失效。

### 公开版思考摘要

这个问题对 AI 的吸引力在于它有清晰的有限证书：找到两个素数集合即可立即验证。因此，GPT-5.5 配合精确搜索和形式化工具，有机会发现正例或大幅扩大排除范围。困难在于已知简单约束已经把最小规模推到很大，导致构造搜索极其庞大；而否定答案需要无限族排除，不是靠有限实验就能完成。因此我把它评为 medium_candidate，而不是 high_candidate。

### 免责声明

以上只是对 GPT-5.5 工具增强环境下可推进性的审查，不是该 Erdős 问题的解答，也未声称存在或不存在这样的素数集合。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_307.md](../../prompts/problem_307.md)

### 状态结论

题面明确，当前题目页仍列为可验证开放问题。2026 年结构性预印本给出必要条件和唯一性约束，但没有构造解或证明不可能。

### 当前规范陈述

判定是否存在两个有限素数集合 P,Q，使 (Σ_{p∈P}1/p)(Σ_{q∈Q}1/q)=1。

```text
Determine whether there exist two finite sets of primes P and Q such that (sum_{p in P} 1/p)(sum_{q in Q} 1/q)=1.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 已知弱化例允许 1 或互素合数，不能满足原题；分母约分给出强结构约束但不造成直接矛盾。
- 版本变化: Barbeau 的相关单位分数构造处理半素数分母；当前问题要求两组素数倒数和的乘积恰为 1。

陈述问题：

- P,Q 是集合，素数不重复；方程本身会推出 P∩Q=∅。
- 不应把允许合数或允许 1 的弱化版本当成原题。

需要固定的量词/约定：

- Both P and Q are finite sets of primes.
- The equality is exact over the rationals.

### 文献与当前边界

已核验的主要结果：

- Any solution must have P and Q disjoint and at least 60 primes in their union.
- Writing A(S)/M(S) for the reduced reciprocal sum forces A(P)=M(Q) and A(Q)=M(P).

最近相关工作：2026 年 Bado 预印本系统整理 forcing identities、交叉同余和搜索约束，但明确未解决存在性。

剩余核心：利用精确算术约束构造一对 P,Q，或证明 forcing equations 对有限素数集合无解。

已使用方法：

- squarefree numerator-denominator forcing
- exact-cover/backtracking with proof certificates
- congruence descent on extremal primes

争议或不确定性：

- 最新直接工作是未同行评议预印本。
- 大规模搜索的无解范围不能替代不存在性证明。

### 证据来源

- [Erdős Problem 307](https://www.erdosproblems.com/307) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 307](https://www.erdosproblems.com/latex/307) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [Erdős Problem 307 LaTeX record](https://www.erdosproblems.com/latex/307) — Thomas F. Bloom; `problem_page`, `database_record`, reliability=`medium`. 给出精确题面、弱化版本和已知至少 60 个素数的约束。
- [Structural constraints for an Erdős unit-fraction problem over primes](https://www.researchgate.net/publication/404719794_STRUCTURAL_CONSTRAINTS_FOR_AN_ERDOS_UNIT-FRACTION_PROBLEM_OVER_PRIMES) — Idriss Olivier Bado; `preprint`, `preprint`, reliability=`medium`. 给出 A(P)=M(Q)、A(Q)=M(P) 等必要条件，并仍把存在性列为开放。

### 完成标准

- 肯定出口: Exhibit explicit finite prime sets P,Q and verify the exact rational identity.
- 否定出口: Prove no finite prime sets P,Q satisfy the identity.

不构成完成：

- Solutions using 1 or composite denominators.
- Approximate products close to 1.
- Necessary congruences without existence or impossibility.

正确性陷阱：

- Reduce every rational sum to lowest terms before comparing numerators.
- Verify primality and absence of repeated elements.
- A negative computation needs a mathematically complete finite reduction.

### 更新后的 AI 可解答性

- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- 最新直接工作是未同行评议预印本。
- 大规模搜索的无解范围不能替代不存在性证明。

Proof-first 路线：

- 从最大素数的整除关系建立无穷下降。
- 把 forcing equations 转化为可验证的有限搜索边界或直接构造。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态涉及题面修订、解答声明、低覆盖文献或较新预印本，建议专家重点抽查。

<!-- DEEP_REVIEW:END -->
