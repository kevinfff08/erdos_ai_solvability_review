# Problem 699

## 基本信息

- 原始链接: https://www.erdosproblems.com/699
- LaTeX 页面: https://www.erdosproblems.com/latex/699
- 原始状态: `falsifiable`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `binomial coefficients`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Is it true that for every $1\leq i<j\leq n/2$ there exists some prime $p\geq i$ such that\[p\mid \textrm{gcd}\left(\binom{n}{i}, \binom{n}{j}\right)?\]

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `63/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：prime

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: binomial coefficients
- 证明密集标签命中: number theory
- 有限/计算线索: counterexample
- 渐近/无限线索: prime
- 构造/存在性线索: counterexample

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **这是一个较强的中高候选题：GPT-5.5 级别模型很可能能做出有价值的计算推进、反例搜索框架和若干范围内的形式化验证，但直接给出完整一般性证明的把握不足。**
- 等级: `medium_candidate`
- 分数: `68/100`
- 信心: `medium`
- 可能路线: 可行路线是把命题改写为素数集合交集问题：对每个二项式系数用 Legendre/Kummer 型 p-adic 判据判定哪些素数 p>=i 整除，然后对所有 1<=i<j<=n/2 搜索是否存在交集。若寻找反例，则目标是构造某个三元组 (n,i,j)，使得所有 p>=i 均不能同时整除 C(n,i) 与 C(n,j)。若尝试证明，则需要把 Sylvester-Schur 的单个系数素因子存在性加强为两个系数之间的大素因子重合结论，可能要结合区间素数、p-adic 进位结构和例外族分类。

### 支持理由

- 题目是明确的有限可判定命题，对给定 n,i,j 可以用精确整数算法或 p-adic 公式快速验证，不依赖数值近似。
- 问题状态标为 falsifiable，说明反例搜索是自然入口；GPT-5.5 配合程序可以系统枚举、压缩搜索空间并生成可复核证书。
- 题目已 formalized，这提高了机器辅助验证局部引理、枚举结果和反例证书的可行性。
- 备注给出 Sylvester-Schur 作为基础定理，说明该问题与已有强结构结果相连；模型可尝试围绕已有定理做局部加强或找出加强失败的机制。
- 备注中的 n=28,i=5,j=14 例子虽然不是当前 >=i 命题的反例，但展示了边界素数 p=i 可能是唯一共同大素因子，这有助于指导搜索危险区。

### 主要障碍

- 从每个 C(n,i) 各自有大素因子，推到两个不同二项式系数有共同大素因子，是质变更强的相关性结论，单靠 Sylvester-Schur 不够。
- 若命题为真，需要处理所有 n 和所有 i<j<=n/2；计算只能覆盖有限范围，必须提炼出可证明的结构性分类。
- 潜在反例可能稀疏，简单枚举容易误导；需要有可审计的搜索界、剪枝正确性和独立复算。
- p=i 的边界很关键，尤其当 i 本身为素数时；证明中必须区分 p=i 与 p>i 的机制。
- 二项式系数的共同素因子条件涉及两个 k 值的 p-adic 进位模式同步，局部分析复杂度高。

### 需要的验证

- 实现独立的精确搜索器，至少用两种方法交叉验证：直接因式分解小范围结果，以及 Legendre/Kummer 判据的大范围结果。
- 若发现反例，需要输出完整三元组 (n,i,j)、gcd 的素因子分解，并证明所有 p>=i 的素数均不整除该 gcd。
- 若提出证明，需要把计算观察转化为可形式化的引理，尤其是关于区间内素数和两个二项式系数共同 p-adic 正性条件的引理。
- 利用已 formalized 的基础定义和定理，在 Lean/Isabelle 等环境中验证关键有限枚举或边界化归，而不是只给自然语言论证。
- 对备注中给出的 n=28,i=5,j=14 边界案例做回归测试，确保工具能识别 p=5 满足当前命题但不满足更强的 p>i 版本。

### 公开版思考摘要

该题适合 AI 工具链推进，因为它有清楚的反例证书格式和高效的 p-adic 判定方法。GPT-5.5 不应被要求直接凭空证明全称命题，但可以可靠地搭建搜索、识别危险结构、验证大量范围、提出候选引理，并把局部结果形式化。完整解决的难点在于从有限计算跨到无限 n 的统一结构证明。

### 免责声明

以上是对 GPT-5.5 级别模型可推进性的评估，不是该 Erdős 问题的解答，也未声称命题为真或为假。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_699.md](../../prompts/problem_699.md)

### 状态结论

Erdős--Szekeres 已知两二项式系数总有非平凡公因子，但素因子下界 p≥i 是额外要求。当前页面仍列为可否证问题；2026 年计算核验到 n≤100000，但没有全称证明。

### 当前规范陈述

对所有整数 n 及 1≤i<j≤n/2，判定是否总存在素数 p≥i 同时整除 C(n,i) 与 C(n,j)。

```text
For all integers n and 1<=i<j<=n/2, determine whether there is a prime p>=i dividing both binom(n,i) and binom(n,j).
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 已记录的 (n,i,j)=(28,5,14) 只反驳某些更强分类，不反驳 p≥i，因为公共因子含 5。
- 版本变化: Sylvester--Schur 只保证每个单独 C(n,i) 有大素因子；本题要求两者共享同一大素因子。

陈述问题：

- p≥i 允许 p=i（当 i 为素数）；更强 p>i 已知有例外。
- n/2 表示 j≤floor(n/2)。

需要固定的量词/约定：

- The assertion is universal over all admissible integer triples (n,i,j).
- The same prime p must divide both binomial coefficients.

### 文献与当前边界

已核验的主要结果：

- Erdős--Szekeres proved gcd(binomial(n,i),binomial(n,j))>1.
- The stronger p>i version has special exceptions.
- A 2026 exact computation reports no counterexample for n<=100000.

最近相关工作：近期 SciNet 记录提供大范围精确枚举和强版本例外清单，但属于计算性 finding，不是同行评议的全称结果。

剩余核心：用 Kummer/Lucas 型进位结构证明公共素因子中必有 p≥i，或找到一个明确反例。

已使用方法：

- p-adic valuations via Kummer carries
- prime distribution in short intervals
- minimal-counterexample residue analysis

争议或不确定性：

- 公开直接文献稀少，开放置信度只能给 medium。
- 有限 10^5 核验不能排除更大反例。

### 证据来源

- [Erdős Problem 699](https://www.erdosproblems.com/699) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 699](https://www.erdosproblems.com/latex/699) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [Erdős Problem 699](https://www.erdosproblems.com/699) — Thomas F. Bloom; `problem_page`, `database_record`, reliability=`medium`. 给出精确题面、Sylvester--Schur 背景及更强版本的已知例外。
- [Erdős 699 verified for n<=100000](https://api.scinet.pub/f/76626b5c-caf4-4c69-bb03-4507e376a274) — SciNet contributor; `other`, `preprint`, reliability=`medium`. 报告 41.7 万亿对的精确核验和零反例，但不提供全称证明。

### 完成标准

- 肯定出口: Prove the shared-prime assertion for every admissible n,i,j.
- 否定出口: Give explicit n,i,j and factor both binomial coefficients to prove that every common prime is <i.

不构成完成：

- Proving only gcd>1.
- Finding separate large prime factors for the two binomial coefficients.
- Finite verification without a universal reduction.

正确性陷阱：

- Distinguish p>=i from p>i.
- Use exact prime factorizations in a counterexample.
- Track floor(n/2) boundary cases.

### 更新后的 AI 可解答性

- 等级: `medium_candidate`
- 分数: `66/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- 公开直接文献稀少，开放置信度只能给 medium。
- 有限 10^5 核验不能排除更大反例。

Proof-first 路线：

- 把公共素因子集合用两组进位位置的交集描述。
- 研究最小反例时 n 的素数区间与 i,j 的相对位置。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态涉及题面修订、解答声明、低覆盖文献或较新预印本，建议专家重点抽查。

<!-- DEEP_REVIEW:END -->
