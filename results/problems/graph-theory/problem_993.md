# Problem 993

## 基本信息

- 原始链接: https://www.erdosproblems.com/993
- LaTeX 页面: https://www.erdosproblems.com/latex/993
- 原始状态: `falsifiable`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

The independent set sequence of any tree or forest is unimodal.

In other words, if $i_k(G)$ counts the number of independent sets of vertices of size $k$ in a graph $G$, and $T$ is any tree or forest, then for some $m\geq 0$

$$i_{0}(T)\leq i_{1}(T)\leq\cdots\leq i_{m}(T)\geq i_{m+1}(T)\geq i_{m+2}(T)\geq\cdots.$$

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `62/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 主要风险是候选证明或计算证书容易存在隐藏漏洞，需要独立复核。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。该问题有明确的有限反例证书，适合计算搜索、动态规划验证和形式化校验；若命题为假，工具增强模型有现实机会找到或缩小反例范围。若命题为真，完整证明难度明显更高，模型更可能产出特殊情形证明、可验证搜索边界和结构性猜想，而不是可靠地一次性完成全局证明。**
- 等级: `medium_candidate`
- 分数: `64/100`
- 信心: `medium`
- 可能路线: 优先走反例搜索与验证路线：用树的递归结构计算独立集多项式，枚举非同构树或用约束搜索直接优化非单峰系数模式；对发现的候选树生成可复查的证书。并行推进结构化证明尝试，例如按叶子删除、根树动态规划、最大独立数附近的系数不等式、特殊树类和森林乘积情形。若搜索无反例，则形成大规模验证结果和可形式化的归纳引理候选。

### 支持理由

- 问题对象是树或森林，具有强递归结构，独立集计数可通过动态规划精确计算。
- 命题若为假，一个具体树及其独立集序列就是短证书，适合程序搜索和独立复验。
- 森林情形可由连通分量的独立集多项式乘积处理，计算验证路径清晰。
- JSON 中状态为 falsifiable，说明从审查角度可优先考虑有限反例发现，而不是只依赖开放式证明。
- 模型可结合枚举、SAT/ILP/CP 搜索、随机生成、局部变换和形式化验证，产出可审计进展。

### 主要障碍

- 非同构树数量随顶点数快速增长，朴素枚举很快不可承受。
- 如果最小反例很大或不存在，计算搜索只能给出下界，不能直接解决全称命题。
- 独立集序列的单峰性不是简单局部性质，叶子递归可能难以保持全局系数不等式。
- 完整证明可能需要新的结构定理，而不仅是高强度计算。
- 若生成搜索程序有去重、整数溢出或剪枝错误，容易产生错误的反例缺失结论。

### 需要的验证

- 对任何候选反例，至少用两套独立实现重新计算独立集序列并检查非单峰位置。
- 搜索程序需要记录树编码、生成规则、去重方法、顶点数范围和完整日志。
- 若声称验证到某个 n，需要证明枚举覆盖所有非同构树或所有相关有标号树。
- 对提出的归纳引理，应在证明助手或小型形式化框架中验证关键递推不等式。
- 文献检索可用于确认该命题当前状态和已有特殊情形，但本次判断未依赖 JSON 之外材料。

### 公开版思考摘要

这个问题对工具增强模型较友好的一面是：对象离散、可精确计算，并且反例证书明确。GPT-5.5 级别模型很适合组织动态规划、反例搜索、结果复验和形式化小引理验证，因此有较大机会显著推进问题或发现反例。较不利的一面是：若命题为真，证明所有树的独立集序列单峰很可能需要强结构洞察，单靠枚举无法闭合。因此评为中等候选，而非高候选。

### 免责声明

这不是该 Erdős 问题的证明或反例，只是基于所给 problem JSON 对 GPT-5.5 工具增强求解可行性的审查判断。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_993.md](../../prompts/problem_993.md)

### 状态结论

2026 年多份直接工作明确说单峰猜想仍开放：一份证明两类非对数凹树族仍单峰，另一份核验所有至多 29 顶点的树并给出结构约化。

### 当前规范陈述

对每个有限森林 T，证明按大小 k 计数的独立顶点集数列 i_k(T) 是单峰的。

```text
For every finite forest T, prove that the sequence i_k(T) counting independent vertex sets of size k is unimodal.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 26 顶点树只反驳对数凹加强版，其独立集数列仍可能单峰；枚举到 29 顶点未发现反例。
- 版本变化: 一般图可实现任意升降模式；树的对数凹猜想已失败；单峰性仍保留。

陈述问题：

- 森林版本可由树版本通过独立多项式乘积性质处理，但该闭包性质应证明。
- 单峰弱于对数凹；已知非对数凹树不反驳本题。

需要固定的量词/约定：

- i_k counts vertex-independent sets, not matchings.
- Unimodality allows equality and an arbitrary plateau.

### 文献与当前边界

已核验的主要结果：

- Two trees on 26 vertices first violate log-concavity.
- All trees through 29 vertices have been exhaustively verified as unimodal.
- Two infinite non-log-concave tree families were proved unimodal in 2026.

最近相关工作：Li, arXiv:2603.03025，以及 Reynolds 的 2026 Zenodo 手稿都直接声明一般树单峰猜想仍开放。

剩余核心：建立适用于所有树的系数比较/递推，或构造第一棵非单峰树并精确计算其独立多项式。

已使用方法：

- real-rootedness or ratio inequalities for restricted tree decompositions
- leaf recursion and minimal-counterexample reductions
- computer-assisted structural certification

争议或不确定性：

- 计算核验虽巨大，仍只覆盖有限阶。
- 对数凹失败意味着不能依赖常见的强性质路线。

### 证据来源

- [Erdős Problem 993](https://www.erdosproblems.com/993) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 993](https://www.erdosproblems.com/latex/993) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [Unimodality of independence polynomials of two family of trees](https://arxiv.org/abs/2603.03025) — Grace M. X. Li; `preprint`, `preprint`, reliability=`high`. 证明两类非对数凹树仍单峰，并明确一般猜想开放。
- [Mean bounds, structural reductions, and exhaustive verification for tree independence polynomial unimodality](https://zenodo.org/records/19100781) — Brett Reynolds; `other`, `preprint`, reliability=`high`. 核验 n≤29、给出结构约化并明确一般猜想开放。

### 完成标准

- 肯定出口: Prove unimodality of the independence polynomial for every finite tree or forest.
- 否定出口: Give an explicit finite tree whose exact independence sequence is not unimodal.

不构成完成：

- Proving only log-concavity for a subclass.
- Verification through a fixed order.
- Counting independent edges rather than vertices.

正确性陷阱：

- Use exact integer coefficients in any counterexample.
- Distinguish unimodality from log-concavity.
- Prove closure steps when passing from trees to forests.

### 更新后的 AI 可解答性

- 等级: `high_candidate`
- 分数: `70/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- 计算核验虽巨大，仍只覆盖有限阶。
- 对数凹失败意味着不能依赖常见的强性质路线。

Proof-first 路线：

- 把叶删除递推与峰位置区间结合，证明递归保持单峰。
- 利用 29 阶枚举得到的极小反例结构约束做归纳。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。

<!-- DEEP_REVIEW:END -->
