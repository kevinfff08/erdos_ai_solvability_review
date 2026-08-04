# Problem 734

## 基本信息

- 原始链接: https://www.erdosproblems.com/734
- LaTeX 页面: https://www.erdosproblems.com/latex/734
- 原始状态: `open`
- 奖金: `no`
- 主类别: `combinatorics`
- 原始标签: `combinatorics`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Find, for all large $n$, a non-trivial pairwise balanced block design $A_1,\ldots,A_m\subseteq \{1,\ldots,n\}$ such that, for all $t$, there are $O(n^{1/2})$ many $i$ such that $\lvert A_i\rvert=t$.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `27/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序

### 主要障碍

- 题面含渐近/无限对象线索：\gg, for all large, o(

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: combinatorics
- 证明密集标签命中: 无
- 有限/计算线索: 无
- 渐近/无限线索: \gg, for all large, o(
- 构造/存在性线索: find

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。GPT-5.5 级别模型配合文献检索、计算搜索和形式化验证，较可能显著推进该构造问题；若能找到或正确适配带有块大小计数控制的现代 PBD/完全图 clique 分解存在定理，则有条件完成。但完整解决并不只是写出一个随机构造，关键在于全体充分大 n 的精确存在性证明。**
- 等级: `medium_candidate`
- 分数: `66/100`
- 信心: `medium`
- 可能路线: 把问题转写为将 K_n 的边分解为若干 clique，并要求每一种 clique 阶数出现次数至多 O(n^{1/2})。先用计算寻找满足边数方程且每个大小重复次数受控的块大小多重集，再检索或建立一个能实现该多重集的 PBD/图分解存在定理；最后用有限例外搜索、算术引理和形式化检查验证 pairwise balanced 条件与 multiplicity 上界。

### 支持理由

- 问题是明确的构造型设计问题，目标 O(n^{1/2}) 与备注中的下界量级相匹配，说明并非需要猜测完全未知的尺度。
- PBD 条件可自然编码为完全图的 clique 分解，适合调用组合设计文献、整数规划、SAT/CP 搜索和小规模实验来发现可推广模式。
- 一旦候选构造或一般存在定理确定，验证条件相对清晰：每对点恰好覆盖一次、块非平凡、每个块大小的出现次数受控。
- 形式化证明工具适合承担后段验证，尤其是块大小多重集的算术、有限例外检查和构造正确性。

### 主要障碍

- 普通 PBD 存在定理通常只控制允许的块大小集合，不一定控制每个块大小的出现次数；这里的计数约束是核心难点。
- 要求对所有充分大 n 成立，需要处理精确边数、余数、同余条件和可能的有限例外，不能只给无限子序列。
- 若使用吸收法或图分解定理，必须确保修补步骤不会引入某个块大小的过多重复。
- 若走有限几何截断路线，需要证明线交大小分布足够分散；随机子集通常可能产生过度集中的块大小频率。

### 需要的验证

- 精确查证是否已有适用于随 n 增长的 clique 阶数、且能规定或近似规定各阶 clique 数量的分解定理。
- 构造一个对每个充分大 n 都满足总边数 C(n,2) 的块大小多重集，并证明每个大小出现 O(n^{1/2}) 次。
- 证明该多重集可实现为真正的 pairwise balanced block design，而不只是满足必要计数条件。
- 对小规模 n 做计算搜索，识别有限例外和构造模式；对最终证明中的有限检查部分做可复现实验或形式化验证。
- 明确“non-trivial”的采用定义，并验证构造不退化为单块设计或大量 2-块近铅笔结构。

### 公开版思考摘要

该题的可攻性来自两个事实：目标阶 n^{1/2} 已由备注暗示为自然下界，且 PBD 可以转化为完全图 clique 分解问题，便于结合现代设计理论和计算搜索。模型最可能的贡献不是直接凭空发明设计，而是找到合适的大小多重集、定位可实现这种多重集的存在定理，并把余数处理和验证自动化。风险在于现有定理可能不足以控制每个块大小的重复次数，导致只能得到弱推进或无限子序列构造。

### 免责声明

本输出只是基于给定 Problem JSON 的可解性审查，不是该 Erdős 问题的证明、反例或完整文献综述。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_734.md](../../prompts/problem_734.md)

### 状态结论

问题陈述清楚且 √n 量级由 de Bruijn–Erdős 下界显示为正确临界量级；2026 评论仅给条件约化，无完整解答。

### 当前规范陈述

证明存在绝对常数 C、N_0，使每个 n≥N_0 都有 [n] 上的非平凡成对平衡设计：每个无序点对恰在一个区块中、没有区块等于整个 [n]，且对每个整数 t，大小为 t 的区块至多 C√n 个。

```text
Prove that there is an absolute constant C and N_0 such that for every n>=N_0 there exists a nontrivial pairwise balanced design on [n] (every unordered pair lies in exactly one block, and no block is all of [n]) for which, for every integer t, at most C sqrt(n) blocks have size t.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 射影平面等特殊 n 构造不能覆盖所有充分大 n；未发现字面简单反例。
- 版本变化: de Bruijn–Erdős 的 m≥n 表明某个块大小至少出现 Ω(√n) 次，因此目标量级最佳。

陈述问题：

- 非平凡至少排除单一全点区块。
- O(√n) 的常数必须对 n 与 t 一致。

需要固定的量词/约定：

- One absolute C must work simultaneously for every block size t and all n>=N_0.
- Every unordered pair of points occurs in exactly one block.

### 文献与当前边界

已核验的主要结果：

- 任意非平凡 PBD 至少有 n 个区块。
- 由块大小计数可推出某个大小的重数为 Ω(√n)。
- 论坛存在带多项失败条件的条件性约化，但非完整证明。

最近相关工作：2026-04-30 论坛笔记讨论条件约化和 13 类失败模式，未声称完整解决。

剩余核心：为每个充分大 n 构造所有块大小重数同时 O(√n) 的 PBD。

已使用方法：

- PBD 递归、组可分设计与填充。
- 设计存在定理的余数类拼接。

争议或不确定性：

- “non-trivial”的标准约定需在证明中固定。
- 条件约化不是可作为黑箱的定理。

### 证据来源

- [Erdős Problem 734](https://www.erdosproblems.com/734) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 734](https://www.erdosproblems.com/latex/734) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。

### 完成标准

- 肯定出口: Give a uniform construction for every n>=N_0 and prove the PBD pair condition, nontriviality, and the simultaneous C sqrt(n) multiplicity bound for every t.
- 否定出口: Prove that for infinitely many n every nontrivial PBD has some block size occurring omega(sqrt(n)) times.

不构成完成：

- Constructions only for prime-power or sparse n.
- An O(sqrt(n)) constant depending on t.
- A linear space that fails exact pair coverage.

正确性陷阱：

- Check every pair exactly once.
- Control multiplicities after all recursive fillings.
- Do not let the hidden O constant depend on n or t.

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

- 用有限种主块大小的 PBD 闭包覆盖所有余数类。
- 把递归填充的重数误差写成可闭合的不等式。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
