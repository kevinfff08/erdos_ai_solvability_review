# Problem 616

## 基本信息

- 原始链接: https://www.erdosproblems.com/616
- LaTeX 页面: https://www.erdosproblems.com/latex/616
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $r\geq 3$. For an $r$-uniform hypergraph $G$ let $\tau(G)$ denote the covering number (or transversal number), the minimum size of a set of vertices which includes at least one from each edge in $G$.

Determine the best possible $t$ such that, if $G$ is an $r$-uniform hypergraph $G$ where every subgraph $G'$ on at most $3r-3$ vertices has $\tau(G')\leq 1$, we have $\tau(G)\leq t$.

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `40/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

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
- 有限/计算线索: graph, hypergraph
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **有希望显著推进，但不宜评为高概率完整解决。该问题结构清晰、参数线性、已有上下界非常接近，适合用模型配合极值组合、有限结构搜索和证明助理来检验候选常数与局部反例；但要确定“best possible t”很可能需要新的超图极值构造或稳定性定理。**
- 等级: `medium_candidate`
- 分数: `63/100`
- 信心: `medium`
- 可能路线: 较现实的路线是把条件改写为：任意边集只要并集大小不超过 3r-3，就有公共顶点；然后围绕 tau(G)=k 的最小反例做结构压缩。模型可尝试生成并验证小 r 的整数规划/ SAT / CP-SAT 搜索，寻找达到大覆盖数的超图模式；同时把 EHT91 的上下界证明形式化拆解，检查常数 3/16 和 1/5 是否来自可优化的局部计数不等式。若搜索显示稳定构型，可反向猜测一般构造或改进上界证明。

### 支持理由

- 问题表述短且局部条件强，便于形式化为有限组合约束：边大小固定为 r，局部小并集边族必须有公共交点。
- 目标 t 只有线性级别，且已知上下界常数非常接近，说明可能存在可优化的计数或构造空间，而不是完全开放的巨大参数区间。
- GPT-5.5 级模型可有效承担文献追踪、旧证明重构、局部引理枚举、SAT/ILP 建模、小规模反例搜索和形式化验证脚手架。
- 该问题属于极值超图论，许多关键步骤可被工具辅助：最小反例、核/阻塞集、覆盖数对偶、有限配置排除等都适合半自动探索。

### 主要障碍

- 要确定最优 t 需要同时给出全局上界和匹配构造；已有上下界差距虽小，但常数级差距可能隐藏深的极值结构。
- 局部条件涉及所有小顶点数子超图，直接枚举随 r 急剧爆炸，需要非常好的对称化、压缩或证书抽象。
- 覆盖数大的 r-一致超图构造通常与设计、有限几何或概率方法相关，模型可能能猜到模式，但严格证明其局部性质并推广到所有 r 较难。
- 如果最优答案依赖 r 的同余类、低阶项或特殊小 r 例外，纯经验搜索很容易给出误导性猜想。

### 需要的验证

- 重新核对 EHT91 原文中上下界方向、常数和假设，确认题目摘要没有排版或转录误差。
- 对小 r 建立精确搜索：最大化 tau(G)，约束所有至多 3r-3 顶点诱导/边子结构满足 tau<=1，并输出可验证证书。
- 将任何候选构造验证为 r-一致、满足局部交点条件，并证明其覆盖数达到声称下界。
- 将任何候选上界证明拆成可机器检查的引理，尤其检查极小反例、双计数和不等式优化步骤。
- 测试 t 是否应理解为整数函数，例如 floor/ceiling 形式，而不仅是线性渐近常数。

### 公开版思考摘要

这个问题对 AI 来说不是“直接求解型”，但很适合工具增强推进：它有明确的有限约束、强局部性质和接近的已知线性上下界。GPT-5.5 可能在重建旧证明、发现小规模极值例子、优化计数不等式或形成可验证猜想方面有实质贡献。完整解决的主要风险在于需要新的全局极值思想，而这通常不是靠枚举或形式化检查自然推出的。

### 免责声明

以上是对 GPT-5.5 级模型可解性和推进潜力的审查，不是该 Erdős 问题的数学解答，也未声称给出了最优 t。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_616.md](../../prompts/problem_616.md)

### 状态结论

Erdős–Hajnal–Tuza 给出线性上下界，常数仍有缺口；题面需把 best possible t 明确为函数 t(r)。

### 当前规范陈述

对每个 r≥3，令 t(r) 为满足下述性质的最小整数：若 r-一致超图 G 的每个至多由 3r−3 个顶点支撑的子超图横截数至多 1，则 τ(G)≤t(r)。求 t(r) 或至少其尖锐渐近常数。

```text
For each integer r>=3, let t(r) be the least integer such that every r-uniform hypergraph G whose every subhypergraph supported on at most 3r-3 vertices has transversal number at most 1 satisfies tau(G)<=t(r). Determine t(r), or at least its sharp asymptotic constant.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现局部条件的低阶反例；文献构造正是下界而非对题面的否定。
- 版本变化: EHT91 证明 3r/16+7/8≤t(r)≤r/5（按整数解释）。

陈述问题：

- “on at most 3r-3 vertices”按支撑顶点数解释。
- t(r) 是整数，文献线性不等式需处理取整。

需要固定的量词/约定：

- The local condition ranges over every subhypergraph with support size at most 3r-3.
- t(r) is the least universal integer bound for each r.

### 文献与当前边界

已核验的主要结果：

- 存在约 3r/16 的构造下界。
- 一般上界约 r/5。

最近相关工作：当前题目页未列出 1991 年后关闭常数缺口的结果。

剩余核心：确定 t(r) 的精确值或把 3/16 与 1/5 的渐近常数缺口闭合。

已使用方法：

- 局部横截条件的结构分解。
- 覆盖数、匹配与代表集的双计数。

争议或不确定性：

- 原论文的 t 记号和取整需核对。
- 较旧问题存在术语漂移检索风险。

### 证据来源

- [Erdős Problem 616](https://www.erdosproblems.com/616) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 616](https://www.erdosproblems.com/latex/616) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。

### 完成标准

- 肯定出口: Prove an exact formula for t(r) for all r>=3 or matching asymptotic upper and lower bounds with the same leading constant.
- 否定出口: Disprove a proposed formula or constant by an explicit infinite family satisfying the local hypothesis and having larger transversal number.

不构成完成：

- Reproducing either side of the 1991 gap.
- Treating only finitely many r.
- Checking only induced subhypergraphs when the theorem requires all subhypergraphs.

正确性陷阱：

- Distinguish edge-induced and arbitrary subhypergraphs.
- Count support vertices, not edges.
- Respect integer rounding in finite-r claims.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `30/100`
- 信心: `medium`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 刻画最小反例的边交结构。
- 改进局部到全局横截数的压缩或核化论证。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
