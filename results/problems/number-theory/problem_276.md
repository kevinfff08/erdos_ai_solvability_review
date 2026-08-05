# Problem 276

## 基本信息

- 原始链接: https://www.erdosproblems.com/276
- LaTeX 页面: https://www.erdosproblems.com/latex/276
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `covering systems`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Is there an infinite Lucas sequence $a_0,a_1,\ldots$ where $a_{n+2}=a_{n+1}+a_n$ for $n\geq 0$ such that all $a_k$ are composite, and yet no integer has a common factor with every term of the sequence?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `44/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: covering systems
- 证明密集标签命中: number theory
- 有限/计算线索: covering system, finite
- 渐近/无限线索: 无
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选：GPT-5.5 级别模型配合计算与形式化工具，较可能对候选 Lucas 序列做出强验证、发现有限覆盖结构或排除大量可能的“共同因子覆盖”证据；但要完整证明存在一个全项合数且无任何整数与每项都有公因子的无限序列，仍需要处理无限素因子与覆盖系统的全局障碍，完成概率不宜评为高。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 最可行路线是围绕 Ismailescu--Son 给出的显式候选序列建立机器可检验验证框架：先用递推矩阵与模周期性证明所有项合数的覆盖证书；再把“存在某整数与每项都有公因子”转化为有限素集合覆盖所有指标的问题，进行 SAT/SMT、模周期搜索、素因子轨道分析与形式化排除。若能证明任何有限素集合都不能覆盖全部项，或给出可扩展的不可覆盖判据，就能显著推进问题。

### 支持理由

- 题目已有显式构造线索和“conjecturally solved”状态，AI 不必从零发明候选对象，更适合做证书化、反例搜索和缺口补全。
- Lucas 递推在模 m 下具有周期性，适合计算枚举、覆盖系统搜索、SAT 编码和形式化验证。
- “所有项合数”通常可由有限覆盖同余类证书验证，这类证书很适合自动证明检查。
- 题目已标记 formalized=yes，说明至少部分陈述或相关结构可以进入形式化环境，降低验证路线的工程门槛。
- AI 工具链可系统搜索有限素集合覆盖、检验候选序列的素因子分布，并生成可公开审计的计算证据。

### 主要障碍

- 核心难点不是找出许多合数项，而是证明不存在任何整数与每一项都有公因子；这等价于排除所有有限素因子集合的覆盖，量化范围无限。
- 即使计算上没有发现覆盖系统，也不能直接推出无覆盖系统；需要一个一般性结构定理或可形式化的不可覆盖证明。
- 候选序列若依赖大整数与复杂素因子模式，完整分解、周期计算和证书压缩可能很重。
- “没有 underlying covering congruences responsible”的直觉描述需要精确定义成可证明命题，否则容易只得到经验性证据。
- 覆盖系统问题常有稀疏、长周期、非显然组合结构，AI 搜索可能错过大周期或大素数参与的覆盖。

### 需要的验证

- 精确定义“某整数与每项都有公因子”：需确认是存在 d>1 使得对所有 k 都有 gcd(d,a_k)>1，而非固定公共因子整除所有项。
- 对候选序列建立独立可复现的计算证书：初值、递推、模周期、每个覆盖类的合数因子。
- 对任意有限素集合覆盖的否定给出数学证明，而不只是有限搜索；若使用搜索，需说明搜索边界为何充分。
- 将关键引理形式化，至少包括 Lucas 序列模 p 的周期性、指标集合覆盖判定，以及候选序列满足所需性质。
- 由独立实现复核大整数分解、周期长度、SAT/SMT 不可满足证书或其他计算证据。

### 公开版思考摘要

这个问题对 AI 的吸引力在于它有明确的递推结构、显式候选构造线索和可计算的模周期性质，因此很适合用程序搜索、证书生成和形式化证明来推进。GPT-5.5 级别模型很可能能把“候选序列是否真的避开有限覆盖”拆成可验证子问题，并产生有价值的计算证据或局部定理。但完整解决需要从有限实验跃迁到无限排除，这仍是实质性的数论与组合覆盖难点。因此评为中等候选，而不是高候选。

### 免责声明

以上是对 AI 辅助可解性与推进潜力的审查，不是该 Erdős 问题的解答，也未声称给出了满足条件的 Lucas 序列或证明了其不存在覆盖整数。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `revised_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_276.md](../../prompts/problem_276.md)

### 状态结论

原题字面只要求不存在一个整数同时与所有项有非平凡公因子；2014 年论文已经构造 gcd(x_0,x_1)=1 且全为合数的序列，从而解决该字面版本。文献真正尚未证明的是“不存在有限素数覆盖”的加强版。

### 当前规范陈述

构造互素正整数 x_0,x_1，使 x_{n+2}=x_{n+1}+x_n 的每一项都合数，并且不存在有限素数集 S 能逐项覆盖该序列（每一项都被 S 中某个素数整除）。

```text
Construct relatively prime positive integers x_0,x_1 such that x_{n+2}=x_{n+1}+x_n, every x_n is composite, and no finite set of primes S has the property that every term x_n is divisible by at least one p in S.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `counterexample_found`
- 检查说明: Ismailescu--Son 的 Theorem 3 给出互素初值且每项合数；互素初值立即排除一个非平凡整数整除所有项，因此原字面问法已肯定解决。
- 版本变化: 研究目标从已解决的共同因子条件修订为“没有有限素数覆盖”，后者在论文中仅以大规模计算和启发式支持。

陈述问题：

- “an integer has a common factor with every term”与“a finite set of primes covers all terms”不是同一条件。
- 规范研究目标采用 2014 年论文明确讨论但只给计算证据的有限素数覆盖版本。

需要固定的量词/约定：

- The recurrence holds for every n>=0.
- The no-cover condition quantifies over every finite set of primes, not over one common divisor.

### 文献与当前边界

已核验的主要结果：

- Classical constructions use a finite covering system of residue classes and primes.
- Ismailescu--Son construct a composite Fibonacci-like sequence with relatively prime initial terms.
- Their odd and even terms are made composite by different mechanisms.

最近相关工作：2014 年论文证明全合数与初值互素，但明确说无法证明最小素因子无界，因此没有证明不存在有限素数覆盖。

剩余核心：对一个显式或新构造的全合数 Fibonacci-like 序列，证明其项的素因子集合不能由有限集合覆盖。

已使用方法：

- primitive prime divisors and ranks of apparition
- periodicity of linear recurrences modulo primes

争议或不确定性：

- 对前 200000 项的因子检验不是全称证明。
- 最小素因子无界甚至对更简单序列也可能困难。

### 证据来源

- [Erdős Problem 276](https://www.erdosproblems.com/276) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 276](https://www.erdosproblems.com/latex/276) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [A New Kind of Fibonacci-Like Sequence of Composite Numbers](https://cs.uwaterloo.ca/journals/JIS/VOL17/Ismailescu/ism8.pdf) — Dan Ismailescu and Jaesung Son; `primary_paper`, `peer_reviewed`, reliability=`high`. Theorem 3 构造互素初值且所有项合数；末节仅以计算支持不存在有限素数覆盖。

### 完成标准

- 肯定出口: Construct such a sequence and prove that every finite prime set misses at least one term.
- 否定出口: Prove that every all-composite Fibonacci-like sequence is covered by some finite set of primes.

不构成完成：

- Merely proving gcd(x_0,x_1)=1.
- A large finite search for new prime factors.
- A construction that still comes with a finite covering system.

正确性陷阱：

- Distinguish a common divisor from a finite prime cover.
- Prove compositeness for every term independently of the no-cover claim.
- Control repeated prime divisors through exact recurrence periodicity.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `46/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- 对前 200000 项的因子检验不是全称证明。
- 最小素因子无界甚至对更简单序列也可能困难。

Proof-first 路线：

- 为奇数项显式分解、偶数项新素因子机制建立统一的本原因子论证。
- 反向研究所有全合数递推序列是否必有有限模覆盖。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态涉及题面修订、解答声明、低覆盖文献或较新预印本，建议专家重点抽查。

<!-- DEEP_REVIEW:END -->
