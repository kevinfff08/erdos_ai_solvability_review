# Problem 475

## 基本信息

- 原始链接: https://www.erdosproblems.com/475
- LaTeX 页面: https://www.erdosproblems.com/latex/475
- 原始状态: `decidable`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive combinatorics`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $p$ be a prime. Given any finite set $A\subseteq \mathbb{F}_p\backslash \{0\}$, is there always a rearrangement $A=\{a_1,\ldots,a_t\}$ such that all partial sums $\sum_{1\leq k\leq m}a_{k}$ are distinct, for all $1\leq m\leq t$?

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `59/100`
- 建议路线: 优先将已有有限化归约转成可复现实验、SAT/ILP/穷举或证明助理验证。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索

### 主要障碍

- 所属标签偏证明密集：additive combinatorics, number theory
- 题面含渐近/无限对象线索：prime, primes, sufficiently large

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics, number theory
- 有限/计算线索: finite
- 渐近/无限线索: prime, primes, sufficiently large
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5-with-tools`
- 结论: **中等偏高候选：给定摘录显示该问题已被多个深结果覆盖到“所有充分大的素数”，因此 GPT-5.5 级别模型更可能在工具辅助下完成文献拼接、常数追踪、有限剩余区间的计算验证或形式化局部证明，而不是独立发明完整的新加性组合学证明。若目标是把现有结果整理成可验证的全局定理并处理剩余有限小素数，机会较高；若目标是在缺少精确常数的情况下给出无条件全素数证明，仍然很难。**
- 等级: `medium_candidate`
- 分数: `68/100`
- 信心: `medium`
- 可能路线: 可行路线不是从零证明，而是把题目转化为循环群中的 valid ordering / 无零和连续块排列问题；先复核 Graham 的 t=p-1、t<=12、p-3<=t<=p-1 等已知边界，再对摘录中的四个规模区间做文献级定理抽取，检查 small、medium、large、very large 四段是否真正无缝覆盖所有 t。对未由显式常数覆盖的小 p 或中间有限范围，可用 SAT/ILP/回溯搜索和同构削减验证；对符号部分，可形式化关键组合引理或至少形式化拼接逻辑与有限验证证书。

### 支持理由

- 题目本身是有限域中有限集合的排列存在性问题，具有清晰的可计算反例搜索形式：给定 p 和 A，可以搜索是否存在排列使前缀和两两不同。
- 摘录表明已有强文献基础，并且四类结果已经声称覆盖所有充分大素数的不同 |A| 区间；这很适合模型做定理抽取、范围拼接和证据审计。
- 边界情形已有多项结果：t=p-1、t<=12、p-3<=t<=p-1，这降低了从零探索时的盲区，也给计算验证提供了基准。
- 工具辅助特别有价值：计算可枚举小素数和小集合，反例搜索可验证猜想边界，形式化证明系统可检查区间拼接和有限证书，文献检索可确认摘录中 2024-2026 结果的精确假设。
- 由于问题只涉及 F_p 的加法结构，实验与证书生成相对直接；若剩余只是有限小素数或显式阈值以下范围，AI 可以显著推进验证工作。

### 主要障碍

- 摘录只给出渐近范围和非显式的 c、o(1)、充分大等表述；要完成原问题必须获得并核对每篇结果的精确假设、常数依赖和覆盖关系。
- medium 与 large 区间之间、large 与 very large 区间附近的覆盖可能依赖隐含阈值；若常数不可有效化，计算验证无法直接闭合全素数情形。
- 若仍需证明所有小素数而不是只证明充分大素数，集合数量为 2^(p-1)，朴素枚举很快不可行，需要强剪枝、对称性、证书压缩或新的结构性论证。
- 有效排列存在性与零和子结构密切相关，局部贪心策略可能失败；模型生成的直觉性证明很容易漏掉排列中连续块零和的约束。
- 目前 problem JSON 标注未形式化，因此现有证明链可能尚未被机器检查；AI 给出的综合证明需要额外防止引用误读和区间拼接错误。

### 需要的验证

- 检索并核对摘录中 Kravitz、Bedert-Kravitz、Costa-Della Fiore、Pham-Sauermann、BBKMM、Müyesser-Pokrovskiy 等结果的正式定理陈述、常数、阈值和适用条件。
- 建立覆盖表：对每个 t 范围证明 small/medium/large/very large 结果在 p>=p0 后无缝覆盖，并明确 p0 是否可计算。
- 为 p<p0 或文献未覆盖范围设计可复现实验：枚举 A、搜索 valid ordering、输出可独立检查的排列证书或不可满足性诊断。
- 对计算程序进行双实现交叉验证，例如回溯搜索与 SAT/CP-SAT 编码互验，并利用 F_p 的乘法自同构减少等价集合。
- 若声称完整解决，应将最终拼接证明和有限验证证书形式化到 Lean/Isabelle 或至少生成可审计的 proof-checking 脚本。

### 公开版思考摘要

这个问题对 AI 的吸引力在于它既有深组合学文献支撑，又有明确的有限计算验证接口。给定摘录已经说明充分大素数情形由四类结果覆盖，所以 GPT-5.5 级别模型最现实的贡献是做严谨的文献整合、范围覆盖检查、显式常数追踪和剩余有限案例验证。最大风险不是问题无法计算，而是渐近定理中的隐含常数和 o(1) 可能无法直接转成完整的全素数证明。

### 免责声明

以上是对 GPT-5.5 级别模型可解决性与推进潜力的审查，不是该 Erdős 问题的证明，也未断言原命题已被完整解决。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `likely_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_475.md](../../prompts/problem_475.md)

### 状态结论

2024–2026 的四类结果覆盖所有充分大素数，原站标为 DECIDABLE；尚未见有限残余的完整公开证书，因此映射为 likely_open，而不是一般未解猜想。

### 当前规范陈述

对每个素数 p 及 A⊆F_p\{0}，证明存在排序 a_1,…,a_t，使所有非空部分和两两不同。充分大 p 已解决；剩余义务是从论文中提取显式阈值并完整认证有限范围。

```text
For every prime p and every subset A of F_p\{0}, prove that A has an ordering a_1,...,a_t whose nonempty partial sums are pairwise distinct. The theorem is already known for all sufficiently large p; the unresolved obligation is the remaining finite range, with its explicit bound recovered from the proofs and then completely certified.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 题面无简单反例；现状是有限可判定残余，而不是发现反例。
- 版本变化: 小、中、大、极大 |A| 的不同结果合起来证明所有充分大素数。

陈述问题：

- 部分和只要求彼此不同，不额外要求避开 0，除非由两部分和相等导出。
- 集合元素非零且排序使用每个元素一次。

需要固定的量词/约定：

- The claim is universal over every prime p and every subset A of nonzero residues.
- The remaining check must include every prime below an explicit proved threshold.

### 文献与当前边界

已核验的主要结果：

- t≤12 与 p-3≤t≤p-1 已知。
- Kravitz、Bedert–Kravitz、Costa–Della Fiore 推进小集合范围。
- Pham–Sauermann 与 BBKMM/Müyesser–Pokrovskiy 覆盖中大范围，合并后得到充分大 p。

最近相关工作：Costa–Della Fiore 与 Pham–Sauermann 2026 预印本完成渐近范围覆盖，使问题只剩有限检查。

剩余核心：提取所有有效常数，确定有限剩余素数，并给出可独立验证的全覆盖证书。

已使用方法：

- 组合零和与多项式方法。
- 有限约束求解及可检查证书。

争议或不确定性：

- 各预印本中的常数可能未优化或未显式。
- 原站 DECIDABLE 不表示有限检查已经实际完成。

### 证据来源

- [Erdős Problem 475](https://www.erdosproblems.com/475) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 475](https://www.erdosproblems.com/latex/475) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。
- [Graham's rearrangement conjecture beyond the rectification barrier](https://arxiv.org/abs/2409.07403) — B. Bedert and N. Kravitz; `preprint`, `preprint`, reliability=`high`. 覆盖小集合的扩展范围。
- [On Graham's rearrangement conjecture](https://arxiv.org/abs/2602.15797) — H. T. Pham and L. Sauermann; `preprint`, `preprint`, reliability=`high`. 覆盖中等大小集合并参与充分大素数的完整覆盖。

### 完成标准

- 肯定出口: Derive an explicit finite cutoff from the cited theorems and supply a rigorous proof or independently checkable exhaustive certificate for every remaining prime and subset.
- 否定出口: Produce a specific prime p and subset A for which every ordering has two equal partial sums, with a complete certificate.

不构成完成：

- Restating that sufficiently large primes are covered.
- Testing an unspecified finite range.
- A search log without a complete, independently checkable certificate.

正确性陷阱：

- Extract theorem constants without replacing effective statements by asymptotic notation.
- Cover every subset size for each remaining prime.
- Validate certificate completeness, not only positive examples.

### 更新后的 AI 可解答性

- 等级: `high_candidate`
- 分数: `72/100`
- 信心: `high`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 从四类范围定理中严格拼接出显式阈值。
- 为有限残余建立对称性约化和完备证书。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
