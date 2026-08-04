# Problem 158

## 基本信息

- 原始链接: https://www.erdosproblems.com/158
- LaTeX 页面: https://www.erdosproblems.com/latex/158
- 原始状态: `open`
- 奖金: `no`
- 主类别: `sidon sets`
- 原始标签: `sidon sets`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $A\subset \mathbb{N}$ be an infinite set such that, for any $n$, there are most $2$ solutions to $a+b=n$ with $a\leq b$. Must\[\liminf_{N\to\infty}\frac{\lvert A\cap \{1,\ldots,N\}\rvert}{N^{1/2}}=0?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `32/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：sidon sets
- 题面含渐近/无限对象线索：liminf

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: sidon sets
- 有限/计算线索: finite
- 渐近/无限线索: liminf
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **可作为中等候选问题：GPT-5.5 级别模型配合工具有希望做出有价值推进，例如系统化检索 B_2[2] / generalized Sidon set 文献、重建并形式化 Sidon 情形证明、做有限极值搜索并提出可验证引理；但直接完整解决该开放问题的概率不高。**
- 等级: `medium_candidate`
- 分数: `52/100`
- 信心: `medium`
- 可能路线: 最可能的路线不是直接凭空证明，而是把问题转化为 B_2[2] 集的有限密度障碍：假设存在 c>0 使 A(N) 在所有大 N 上至少约 c sqrt(N)，再尝试通过表示函数 r_A(n)≤2、区间分解、差集/和集能量计数、稀疏化为 Sidon 子集或局部结构定理导出矛盾。工具层面可先自动检索相关 generalized Sidon set 结果，再用 SAT/ILP/CP 搜索有限 B_2[2] 极值构型，最后把候选有限引理交给 Lean/Isabelle 或定理证明脚本验证。

### 支持理由

- 问题陈述短、约束清晰，属于可被精确编码的加法组合问题；形式化标记为 yes，说明至少有可形式化入口。
- B_2[1] 的已知 Sidon 情形给出明确参照路线：若能找到从 B_2[2] 降到 Sidon 型稀疏子结构的强引理，AI 工具可帮助枚举、验证和形式化。
- 有限版本很适合计算实验：可搜索最大 B_2[2] 子集、近极值构型、局部周期结构或反例候选，从而生成可检验猜想。
- 文献检索工具可能迅速定位 generalized Sidon sets、B_h[g] sets、liminf 密度和 Erdős-Turán 型问题中的已有边界，避免重复已知路线。

### 主要障碍

- 核心难点是无限集合的全局 liminf 结论；有限搜索只能提供证据，除非抽象出可推广的结构性引理。
- 允许每个和有 2 个表示会破坏 Sidon 集许多刚性性质，简单的唯一表示计数或差集注入不再直接适用。
- 若存在高密度的随机型或构造型 B_2[2] 集，局部有限模式可能很迷惑，计算反例搜索不容易区分真障碍和有限尺度噪声。
- 已知 Sidon 情形证明未必可机械推广；关键可能需要新的组合压缩、能量递推或结构-随机分解思想。

### 需要的验证

- 检索并核对 generalized Sidon / B_2[g] 文献中是否已有等价命题、部分结果或反例构造；不能只依赖题目备注。
- 建立有限 extremal 搜索基准：对多个 N 计算满足 r_A(n)≤2 的最大规模和近极值样本，并验证搜索器无误。
- 若提出证明路线，需要把关键有限或递推引理独立形式化，尤其是表示数计数、区间切分和极限 liminf 推理。
- 若尝试反例方向，需要给出无限构造及严格证明每个和的表示数不超过 2，并证明 A(N) 的下界对所有大 N 成立。

### 公开版思考摘要

这个问题对 AI 来说有较好的工具接口：约束可编码、已有 Sidon 情形可作为模板、计算实验和形式化验证都有用。但它的开放性集中在一个真正困难的无限组合结构问题上，不能期待模型仅靠模式迁移完成证明。合理评估是：有机会产生可发表级别的辅助结果、反例搜索证据或形式化验证框架；完整解决则需要发现新的结构性想法。

### 免责声明

以上只是对 GPT-5.5 级别模型可推进性的审查，不是该 Erdős 问题的解答，也未声称证明或否定原命题。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_158.md](../../prompts/problem_158.md)

### 状态结论

这是清晰的 B_2[2] 临界密度问题；Sidon 的至多一次表示版本已知，但至多两次版本仍被直接记录为开放。

### 当前规范陈述

设 A 为正整数的无限子集，且每个整数 m 至多有两个表示 m=a+b（a,b∈A，a≤b）。是否必有 liminf_{N→∞}|A∩[1,N]|/√N=0？

```text
Let A be an infinite subset of positive integers such that every integer m has at most two representations m=a+b with a,b in A and a<=b. Must liminf_{N->infinity} |A∩[1,N]|/sqrt(N)=0?
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 针对有限周期构造和重复表示边界未发现推翻题面的简单例子；开放性证据仍主要来自题目页。
- 版本变化: 把表示上限 2 改为 1 得到 Sidon 集，Erdős 已证明相应 liminf 结论。

陈述问题：

- 表示按 a≤b 计数，因此 a=b 的表示计一次。
- 结论是 liminf=0，不是密度本身收敛。

需要固定的量词/约定：

- The representation bound holds for every integer m.
- The liminf is over all positive integers N.

### 文献与当前边界

已核验的主要结果：

- Sidon（每个和至多一种表示）版本的 liminf 结论成立。
- 题目页未列出 B_2[2] 版本的实质进展。

最近相关工作：当前题目页无解答主张；未定位到直接解决该精确 liminf 问题的后续论文。

剩余核心：排除一个 B_2[2] 集在所有充分大尺度上保持正的 √N 归一化下密度。

已使用方法：

- 受限表示函数与加法能量。
- Sidon 集密度论证的稳定化或分解。

争议或不确定性：

- 原始引用信息稀少。
- “未检得”不是无人解决的证明，因此置信度为中。

### 证据来源

- [Erdős Problem 158](https://www.erdosproblems.com/158) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 158](https://www.erdosproblems.com/latex/158) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。

### 完成标准

- 肯定出口: Prove that every infinite B_2[2] set A satisfies the displayed liminf equality.
- 否定出口: Construct an explicit infinite B_2[2] set and prove a uniform lower bound |A∩[1,N]|>=c sqrt(N) for all sufficiently large N.

不构成完成：

- The known Sidon B_2[1] case.
- A bound only along a selected subsequence.
- A finite B_2[2] construction.

正确性陷阱：

- Count a+b and b+a as one representation.
- Do not replace liminf by limsup.
- Uniform positive lower density at the sqrt scale is required for a counterexample.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 寻找把 B_2[2] 分解或稀疏化为 Sidon 子集的定量机制。
- 从表示函数二阶矩推导跨尺度下降。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
