# Problem 647

## 基本信息

- 原始链接: https://www.erdosproblems.com/647
- LaTeX 页面: https://www.erdosproblems.com/latex/647
- 原始状态: `verifiable`
- 奖金: `£25`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `yes`
- OEIS: `A062249`, `A087280`
- 原站备注字段: 无

## 原问题

Let $\tau(n)$ count the number of divisors of $n$. Is there some $n>24$ such that\[\max_{m<n}(m+\tau(m))\leq n+2?\]

## AI 完成可能性判断

- 结论: **AI+计算/形式化工具有较高机会完成或显著推进**
- 等级: `high_candidate`
- 分数: `72/100`
- 建议路线: 优先搜索有限证书；若找到证书，再做独立程序验证和形式化复核。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：infinitely many
- 原记录含奖金 £25，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: infinitely many
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **这是一个较强的高候选问题：GPT-5.5 级别模型未必能证明最终结论，但很可能能把问题显著推进，尤其是通过高性能搜索、候选构造、筛选条件推导和形式化验证来寻找或排除大范围内的见证 n。若存在不太离谱大小的例子，该问题对 AI+计算工具非常友好；若例子极稀有或需要深层解析数论，则会迅速变难。**
- 等级: `high_candidate`
- 分数: `82/100`
- 信心: `medium`
- 可能路线: 把条件改写为对所有 j>=1 有 tau(n-j)<=j+2，并优先处理小 j 的强约束；用筛法和快速约数函数计算寻找 n-1 为素数或素数平方、n-2 的约数数不超过 4 等局部候选，再用前缀最大值 M(N)=max_{m<=N}(m+tau(m)) 做 O(1) 验证。计算路线可以先生成 tau(m) 和记录值 m+tau(m)，寻找满足 M(n-1)<=n+2 的 n>24；若发现候选，可给出简短证书并用 Lean/Isabelle 或独立程序验证。若没有发现，则产出大范围排除证据、启发式密度估计和更强必要条件。

### 支持理由

- 问题是存在性问题，且状态为 verifiable；一个具体 n 的证书可以通过有限计算检查，不需要完整解决无穷族。
- formalized=yes 表明至少命题或相关定义已有形式化入口，适合 AI 配合证明助手做独立验证或证书检查。
- tau(n) 可用筛法大规模计算，条件等价于前缀最大值比较，算法结构清晰，容易并行化和交叉验证。
- 局部约束很强：例如 n-1 的约数数必须不超过 3，n-2 的约数数必须不超过 4，这给候选生成和剪枝提供了直接路线。
- 备注中指出 Schinzel 假设 H 可推出相关局部版本，说明启发式和素数模式搜索可能有用；AI 可以把这些启发式转化为实际筛选策略。

### 主要障碍

- 若最小的 n>24 极大，朴素筛法即使正确也可能达不到所需范围，需要复杂的分布式搜索、压缩证书或更深的候选构造。
- 全局条件不是只检查固定长度窗口；虽然远处 m 通常安全，但严格证明某个搜索区间之外的截断边界仍需可靠上界或完整前缀记录。
- tau(m) 的极端峰值由高度合成结构驱动，候选 n 必须避开此前所有 m+tau(m) 记录，随机启发式可能低估稀有障碍。
- 若目标是证明不存在或证明 Erdős 猜测式的极限发散，当前解析数论方法可能远超 GPT-5.5 能力。
- 形式化验证有限证书可行，但形式化高性能搜索结果、筛法正确性和大整数区间覆盖仍需要工程化证书设计。

### 需要的验证

- 实现至少两个独立的 tau 筛法或候选验证器，并比较所有记录值 m+tau(m) 与候选 n。
- 对找到的候选 n，保存可审计证书：前缀最大达到位置、tau 值、以及所有可能违反 m+tau(m)>n+2 的附近 m 的检查记录。
- 若只得到排除结果，需要明确搜索上界、硬件环境、算法版本、哈希校验和边界处理，避免 off-by-one 错误。
- 用形式化证明助手验证命题定义、有限列表证书和关键不等式，或至少用第三方语言重写验证器交叉检查。
- 为搜索策略建立启发式报告：候选密度、局部约束通过率、记录点分布，以及失败原因是否集中在某些 j。

### 公开版思考摘要

这个问题的核心优势是证书短且可验证：只要找到一个 n>24，就能通过有限的 tau 计算和前缀最大值检查确认。GPT-5.5 级别模型可以较好地设计筛法、发现等价条件、生成验证代码，并把结果转成形式化或半形式化证书。因此它不是纯粹依赖新理论突破的问题。主要风险在于例子可能极端稀有，导致搜索范围巨大；而证明不存在或证明极限发散则明显更接近深层数论难题。综合看，它很适合作为 AI+计算推进的高候选，但最终成功依赖最小见证的大小。

### 免责声明

以上是对 AI 可推进性的审查，不是该 Erdős 问题的解答；没有声称存在或不存在这样的 n>24，也没有给出候选 n。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_647.md](../../prompts/problem_647.md)

### 状态结论

这是纯存在/否定型可验证问题。题目页 2026 年仍列为开放且无解答声明；形式化仓库只有局部模约束，没有给出无条件见证或不存在性证明。

### 当前规范陈述

寻找整数 n>24，使每个 1≤m<n 都满足 m+τ(m)≤n+2（τ 为正因子个数）；或者证明这样的 n 不存在。

```text
Find an integer n>24 such that for every integer m with 1<=m<n, m+tau(m)<=n+2, where tau(m) is the number of positive divisors of m; or prove that no such n exists.
```

### 陈述、量词与反例审计

- 歧义严重度: `none`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 有限扫描若发现 n 可直接验证；目前公开结果只给必要模条件和局部约束，没有可核验 n>24。
- 版本变化: Erdős 怀疑有无穷多个的说法极不可信，但也没有断言不存在第二个例；Schinzel H 只支持局部窗口变体。

陈述问题：

- max_{m<n} 包含所有正整数 m，从 1 开始。
- n=24 是已知边界例，但题目严格要求 n>24。

需要固定的量词/约定：

- The witness n is a positive integer greater than 24.
- The inequality must hold simultaneously for every m<n.

### 文献与当前边界

已核验的主要结果：

- n=24 satisfies the inequality.
- The offset +2 is best possible from m=n-1,n-2.
- Recent formal work derives divisibility constraints such as 840|n beyond a range, but does not close existence.

最近相关工作：题目页最后编辑于 2026-04-07；2026 年形式化 PR 报告 n>54 时的模阶梯约束，仍无完整解答。

剩余核心：把无限搜索约化为可证明的有限候选并检查，找到一个见证，或建立所有 n>24 都失败的理论障碍。

已使用方法：

- covering congruences for large divisor counts near n
- CRT constructions
- certified exhaustive search after a proven cutoff

争议或不确定性：

- Lean 页面显示‘complete’可能只是含 sorry/公理的形式陈述，不能当作数学证明。
- 存在性搜索若不附完整验证证书不能关闭问题。

### 证据来源

- [Erdős Problem 647](https://www.erdosproblems.com/647) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 647](https://www.erdosproblems.com/latex/647) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [Erdős Problem 647](https://www.erdosproblems.com/647) — Thomas F. Bloom; `problem_page`, `database_record`, reliability=`medium`. 当前列为 verifiable open，记录 n=24、奖金及无解答声明。
- [Erdős Problem 647 modular ladder](https://github.com/google-deepmind/formal-conjectures/pull/3959) — formal-conjectures contributors; `formalization`, `preprint`, reliability=`medium`. 给出 n>54 时 840|n 的局部形式化约束，不是完整解答。

### 完成标准

- 肯定出口: Produce a specific n>24 and an independently checkable table or proof covering every m<n.
- 否定出口: Prove that for every n>24 there exists m<n with m+tau(m)>n+2.

不构成完成：

- The known witness n=24.
- Necessary congruence conditions alone.
- A search that omits a range of m or relies on unverified arithmetic.

正确性陷阱：

- Use exact divisor counts.
- For a positive witness, verify all m<n, not only those close to n.
- For a negative theorem, handle every residue class and all n.

### 更新后的 AI 可解答性

- 等级: `high_candidate`
- 分数: `78/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- Lean 页面显示‘complete’可能只是含 sorry/公理的形式陈述，不能当作数学证明。
- 存在性搜索若不附完整验证证书不能关闭问题。

Proof-first 路线：

- 继续强化模阶梯直到候选被有限化或产生 CRT 构造。
- 把最危险的 m=n-j 转化为对连续整数因子数的覆盖条件。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。

<!-- DEEP_REVIEW:END -->
