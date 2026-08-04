# Problem 278

## 基本信息

- 原始链接: https://www.erdosproblems.com/278
- LaTeX 页面: https://www.erdosproblems.com/latex/278
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `covering systems`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $A=\{n_1<\cdots<n_r\}$ be a finite set of positive integers. What is the maximum density of integers covered by a suitable choice of congruences $a_i\pmod{n_i}$?

Is the minimum density achieved when all the $a_i$ are equal?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `31/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：density

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: covering systems
- 证明密集标签命中: number theory
- 有限/计算线索: finite
- 渐近/无限线索: density
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 with computation/formalization/literature tools`
- 结论: **中等候选。该题的第一问可被精确转化为有限覆盖优化问题，GPT-5.5 配合 SAT/MILP、穷举剪枝和形式化验证，很可能能给出可靠算法、实例库、上下界和若干特殊情形定理；但若目标是给出任意有限模数集的简洁闭式最大密度公式，则难度明显较高，未必能一次性完成。第二问在题目备注中已由 Simpson 观察解决，因此不应作为主要突破点。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 把所有同余类投影到模 L=lcm(n_i) 的有限循环群上；每个选择 a_i mod n_i 对应选择一个大小 L/n_i 的周期集合。最大密度就是在这些结构化集合族中各选一个集合后，其并集大小除以 L。模型可先实现精确 MILP/SAT/CP-SAT 求解器与对称性约简，再用反例搜索和小规模完全枚举猜测结构定理；同时用 Lean/Isabelle 或可审计脚本形式化有限化、包含排除下界及若干特殊模数族的证明。

### 支持理由

- 问题天然有限化：任意选择的覆盖密度只依赖于模 L=lcm(n_i) 的剩余类，因此计算验证路径清楚。
- 目标函数是集合并大小最大化，可直接编码为 0-1 整数规划、SAT 或最大覆盖模型，适合现代求解器和证书验证。
- 备注已经给出第二问的解决线索，降低了误把已解部分当作开放核心的风险。
- AI 工具链擅长系统枚举小例子、寻找最优配置、发现候选公式或反例，并可把结果整理成可复现实验。
- 若限制模数族，例如两两整除、两两互素、闭包良好的 lcm 格、素数幂模数，可能存在可证明的局部定理。

### 主要障碍

- 第一问可能追求的是结构性最大值公式，而不只是有限算法；这种全一般性公式可能非常复杂。
- lcm L 可能极大，直接在 Z/LZ 上建模会遭遇状态爆炸，需要符号压缩和数论结构利用。
- 不同模数之间的 lcm 交互导致高度非局部依赖，简单贪心或包含排除上界通常不够尖锐。
- 最大覆盖问题的组合复杂性可能使一般情形难以获得漂亮判别准则。
- 从大量计算猜想到严谨通用证明之间仍有显著鸿沟。

### 需要的验证

- 明确题目第一问的期望输出类型：闭式公式、有效算法、复杂度分类，还是特殊族分类。
- 实现独立的精确求解器，并对小 r、小模数全集做完全枚举交叉验证。
- 为求解器输出生成可复核证书，例如最优上界的 LP/MILP 对偶证书或 SAT UNSAT 证书。
- 验证 Simpson 包含排除表达式与“所有 a_i 相等达到最小密度”的证明细节，避免重复解决已知部分。
- 对猜测定理做形式化或至少机器可检查证明，特别是有限化步骤、密度等于周期并集比例、最优性上界。

### 公开版思考摘要

这个问题很适合 AI 工具化推进，因为它可以从整数密度问题降为有限循环群上的结构化最大覆盖问题。GPT-5.5 不应直接声称能解决一般开放形式，但可以可靠地产出精确计算框架、证书化验证、小规模数据库、反例搜索和特殊情形证明。若最终目标只是给出可计算最大密度的算法表达，它很有希望完成；若目标是 Erdős 式的简洁通用公式，则只能评为中等可行。

### 免责声明

以上是对 AI 可推进性的审查，不是该 Erdős 问题的解答；其中的路线和障碍需要进一步计算、文献核验和形式化证明验证。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `revised_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_278.md](../../prompts/problem_278.md)

### 状态结论

Simpson 已用容斥证明所有 a_i 相等取得最小密度；最大密度仍开放，故为 revised_open。

### 当前规范陈述

给定互异正模数 n_1<…<n_r，每个模数选择一个剩余类 a_i mod n_i，求这些剩余类并集的最大自然密度。最小密度问题已解决，不属于目标。

```text
Given distinct positive moduli n_1<...<n_r, determine the maximum natural density of the union of one residue class a_i mod n_i chosen for each modulus. The minimum-density question is already solved and is not part of the target.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 最小密度子问已严格解决，不是反例；未发现使最大密度问题失效的字面漏洞。
- 版本变化: Simpson 1986 解决第二问，当前只保留最大密度。

陈述问题：

- 密度存在，因为有限个剩余类并集是周期集合。
- 只优化每个给定模数恰选一个剩余类。

需要固定的量词/约定：

- The moduli are fixed and pairwise distinct.
- The maximum is over all residue choices a_i modulo n_i.

### 文献与当前边界

已核验的主要结果：

- 并集密度可按 lcm 周期精确计算。
- 全相同剩余取得容斥下界并解决最小值。

最近相关工作：未检得给出任意模数组合最大密度通式的后续结果。

剩余核心：用模数的 gcd/lcm 结构刻画最优剩余选择及最大覆盖密度。

已使用方法：

- 有限循环群上的并集优化。
- 容斥、多项式和冲突图。

争议或不确定性：

- “determine”允许算法、结构定理或闭式表达，prompt 用完整可验收刻画固定。
- 一般模数组合可能包含计算复杂性问题。

### 证据来源

- [Erdős Problem 278](https://www.erdosproblems.com/278) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 278](https://www.erdosproblems.com/latex/278) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。

### 完成标准

- 肯定出口: Give a theorem or exact finite algorithm, proved correct for every finite set of distinct moduli, that returns the maximum density and characterizes an optimal residue assignment.
- 否定出口: Disprove a precisely stated candidate formula or structural characterization with an exact family; the open target itself is an optimisation request rather than a yes/no conjecture.

不构成完成：

- Reproving the minimum-density theorem.
- Brute force for selected modulus sets.
- An upper bound without a matching construction or exact characterization.

正确性陷阱：

- Compute densities over the full lcm period.
- Account for all higher intersections, not just pairwise overlaps.
- Do not assume coprime moduli.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `48/100`
- 信心: `medium`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 把问题转成有限循环群上的带约束最大覆盖。
- 寻找由 gcd 相容性图控制的最优结构或动态规划。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
