# Problem 819

## 基本信息

- 原始链接: https://www.erdosproblems.com/819
- LaTeX 页面: https://www.erdosproblems.com/latex/819
- 原始状态: `open`
- 奖金: `no`
- 主类别: `additive combinatorics`
- 原始标签: `additive combinatorics`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $f(N)$ be maximal such that there exists $A\subseteq \{1,\ldots,N\}$ with $\lvert A\rvert=\lfloor N^{1/2}\rfloor$ such that $\lvert (A+A)\cap [1,N]\rvert=f(N)$. Estimate $f(N)$.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `24/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 目前只能依靠通用数学推理、文献归纳和特殊情形探索

### 主要障碍

- 所属标签偏证明密集：additive combinatorics
- 题面含渐近/无限对象线索：o(
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics
- 有限/计算线索: 无
- 渐近/无限线索: o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **有显著推进潜力，但不应评为高概率可完全解决。该问题目标简洁、可计算化强，且已有上下界常数区间较宽；GPT-5.5 配合搜索、整数规划、随机构造和形式化验证，可能找到更好的显式构造、排除某些候选极值结构，或验证有限规模渐近猜想。但要把常数从已知区间收敛到真正渐近值，需要新的加性组合结构定理或 quasi-Sidon 型极值理论，难度较高。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 可行路线是把问题归约为有限但可扩展的极值搜索：设 |A|≈sqrt(N)，优化不同分层位置的元素比例，使尽可能多的无碰撞和落在 [1,N] 内。模型可先生成参数化构造族，例如低区间 quasi-Sidon 部分加高区间隔离部分，再用 SAT/ILP/CP-SAT、随机贪心、局部搜索和有限域 Sidon 构造测试常数；同时尝试把搜索发现的结构抽象为可证明的下界。上界方面可尝试用能量、受限和集、双计数、图匹配或容器式论证，把“很多小和且很少碰撞”的要求转化为 quasi-Sidon 密度约束。

### 支持理由

- 问题陈述短，核心对象是有限集合 A 与受限和集 (A+A)∩[1,N]，适合计算实验、精确搜索和可视化结构发现。
- 目标是渐近估计 f(N)，而当前给出的上下界为 (3/8-o(1))N 到 (1/2+o(1))N，常数间隙较大，存在被工具辅助方法改进的空间。
- 上界 1/2N 来自无碰撞对数的自然极限，说明问题的困难集中在碰撞控制与和落入 [1,N] 的比例之间的折中，这种折中可被优化建模。
- 与 quasi-Sidon 集相关，暗示已有理论框架可作为脚手架；模型不必从零发明整个领域，较可能在已知工具之间做组合。
- 有限 N 的最优或近优结构可以通过 ILP、SAT、局部搜索、遗传算法等产生数据，为猜测渐近常数或构造模板提供证据。

### 主要障碍

- 完全解决可能需要新的加性组合极值定理，而不仅是计算搜索；从有限 N 模式外推到渐近证明是主要瓶颈。
- 集合大小正好为 floor(N^{1/2})，处在 Sidon 型问题的临界尺度，小的常数损失会直接影响主项常数。
- 受限到 [1,N] 的和集使问题不是标准 Sidon 最大和集问题；元素位置分布、碰撞数和越界和之间强耦合。
- 若最优构造不是单一规则族，而是多尺度或随机化 quasi-Sidon 结构，模型生成简洁可证明构造会更困难。
- 上界改进需要证明所有可能的 A 都必须付出碰撞或越界损失，这类全局排除通常比找到新下界更难。

### 需要的验证

- 对中小 N 进行精确 ILP/SAT 求解，并与启发式搜索结果交叉验证，避免被局部最优误导。
- 生成最优或近优 A 的结构统计：元素分布、有效配对比例、重复和数量、越界和数量、低区间/高区间比例。
- 将模型提出的任何构造写成参数化族，并严格证明 |A|=floor(N^{1/2}) 及 |(A+A)∩[1,N]| 的渐近下界。
- 将任何上界论证拆成可检查引理，最好用 Lean/Isabelle 或至少机器可验证的符号推导验证关键不等式。
- 如果使用文献检索，需要核对 quasi-Sidon 相关结果是否真的适用于这个受限和集版本，而不是只适用于标准 Sidon 或 B_2 集。

### 公开版思考摘要

这个问题对 AI 友好的部分在于：对象有限、目标函数清楚、自然上界和构造搜索都容易程序化；因此 GPT-5.5 级模型很可能通过实验数学发现更优构造或形成有价值猜想。困难在于从搜索和启发式构造升级为渐近定理，尤其是证明全局上界。综合看，它不是低价值或纯元数学不可操作的问题，但也不像只需整合已知工具即可关闭的题目；更合理的判断是中等候选，偏向可显著推进而非高可信完全解决。

### 免责声明

以上是对 AI 工具辅助可解性和推进潜力的审查，不是该 Erdős 问题的解答，也未声称给出了新的 f(N) 渐近估计。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_819.md](../../prompts/problem_819.md)

### 状态结论

经典界为 3/8 与 1/2；2026 论坛声称把下界提高到约 0.469，但尚未同行评议或独立正式核验，故 likely_open。

### 当前规范陈述

令 f(N)=max{|(A+A)∩[1,N]|: A⊆[1,N], |A|=⌊√N⌋}，其中 A+A 允许两个加数相同。求 f(N) 的渐近行为，尤其判断 f(N)/N 是否收敛及其极限。

```text
Let f(N)=max{|(A+A)∩[1,N]|: A subset [1,N], |A|=floor(sqrt(N))}, where A+A allows equal summands. Determine the asymptotic behaviour of f(N), in particular whether f(N)/N has a limit and its value.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现题面反例；最新下界主张不决定极限也不达到上界 1/2。
- 版本变化: Erdős–Freud 给 3/8-o(1)≤f(N)/N≤1/2+o(1)；论坛新稿声称 liminf≥(16√2−17)/12≈0.469。

陈述问题：

- A+A 采用通常定义，允许 a=a'。
- 交 [1,N] 后再计不同和的个数。

需要固定的量词/约定：

- The maximum is over sets of exactly floor(sqrt(N)) elements.
- Any asymptotic claim ranges over all integers N.

### 文献与当前边界

已核验的主要结果：

- 经典下界常数 3/8。
- 经典上界常数 1/2。
- 2026 非正式主张下界常数提高到约 0.469。

最近相关工作：论坛中的 GPT 辅助笔记使用反射 Sidon 集、随机平移和 Pikhurko 型引理，尚无正式发表验证。

剩余核心：确认并利用新下界，继续闭合到 1/2，或证明不同极限/更低上界。

已使用方法：

- 准 Sidon 集与受截断的无碰撞和。
- 随机平移、反射构造和加法能量。

争议或不确定性：

- 最新关键改进仅为论坛主张。
- 极限存在性仍未建立。

### 证据来源

- [Erdős Problem 819](https://www.erdosproblems.com/819) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 819](https://www.erdosproblems.com/latex/819) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。
- [Problem 819 discussion thread](https://www.erdosproblems.com/forum/thread/819) — forum contributors; `forum`, `informal_claim`, reliability=`medium`. 记录 liminf≥(16√2−17)/12 的新下界主张。

### 完成标准

- 肯定出口: Prove an exact asymptotic f(N)=(c+o(1))N with c identified, including a matching construction and upper bound.
- 否定出口: Prove that f(N)/N has distinct liminf and limsup, or rigorously refute a stated candidate constant with an infinite family.

不构成完成：

- Only improving one side without determining the asymptotic, unless clearly labelled partial progress.
- Finite optimisation data.
- Assuming every Sidon sum lies in [1,N].

正确性陷阱：

- Apply the [1,N] truncation exactly.
- Respect |A|=floor(sqrt(N)).
- Distinguish ordered representations from distinct sums.

### 更新后的 AI 可解答性

- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 独立重证 0.469 下界并寻找参数最优化。
- 从受截断和集的能量/边界损失推导匹配上界。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
