# Problem 261

## 基本信息

- 原始链接: https://www.erdosproblems.com/261
- LaTeX 页面: https://www.erdosproblems.com/latex/261
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Are there infinitely many $n$ such that there exists some $t\geq 2$ and distinct integers $a_1,\ldots,a_t\geq 1$ such that\[\frac{n}{2^n}=\sum_{1\leq k\leq t}\frac{a_k}{2^{a_k}}?\]Is this true for all $n$? Is there a rational $x$ such that\[x = \sum_{k=1}^\infty \frac{a_k}{2^{a_k}}\]has at least $2^{\aleph_0}$ solutions?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `32/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：infinitely many

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
- 结论: **中等候选。GPT-5.5 级别模型很可能能复现并形式化备注中的无限族证明，建立可审计的精确搜索与证书验证流程，并对有理数无限表示问题提出可检验路线；但“是否对所有 n 成立”的统一证明仍需要新的结构性构造，不能仅靠扩大计算验证完成。**
- 等级: `medium_candidate`
- 分数: `67/100`
- 信心: `medium`
- 可能路线: 把有限等式转化为精确的二进制进位/子集和证书问题：先形式化验证 n=2^{m+1}-m-2 时的恒等式；再用整数 DP、SAT/SMT 或自动机搜索为给定 n 生成可独立校验的表示证书；从证书中挖掘参数化替换规则或可归纳的进位模式。对无限和问题，可尝试用 subsum set、区间重叠和无限独立分支构造，寻找一个显式有理 x 并证明存在连续多个互异表示。

### 支持理由

- 题目核心是 dyadic 有理数恒等式，候选解可通过乘以公共 2 的幂转化为整数等式，适合精确计算和形式化验证。
- 备注已给出一个明确无限族证明，模型可把它作为基准恒等式、单元测试和形式化证明目标。
- 已有 n<=10000 的验证信息说明该问题有可操作的搜索结构，模型可扩展搜索、生成证书并进行模式归纳。
- 有限表示要求 distinct integers，使问题自然落入子集和、进位自动机、SMT、SAT 及证明助手协作的范围。
- 无限级数版本可能可由 subsum/achievement-set 类理论或显式无限分支构造推进，比较适合文献检索加形式化核验。

### 主要障碍

- “对所有 n 成立”需要统一构造、终止证明或强归纳不变量；有限范围验证不能直接外推。
- 搜索空间中最大 a_k 未天然有界；若没有上界定理，反例搜索或验证都只能是条件性的。
- 二进制进位会造成局部模式误导，贪心或短证书规律可能在大 n 处失效。
- 无限级数问题必须先澄清“solutions”的等价关系、是否要求 a_k distinct/递增，以及是否排除有限改写造成的重复计数。
- 备注显示该题已有历史研究背景，任何声称解决开放部分的路线都需要严格查证原始文献和现有结果。

### 需要的验证

- 形式化证明备注中的 Borwein-Loring 恒等式，并检查 t>=2、a_k distinct、a_k>=1 等条件。
- 实现两个相互独立的精确搜索器，并输出可由短程序或证明助手复核的整数证书。
- 若声称验证到更大范围，需要给出搜索上界、剪枝正确性证明和完整失败/成功日志。
- 若提出 all n 的构造，需要证明对任意 n 都能生成有限、互异、正整数的 a_k，且算法必停。
- 若提出有理 x 的连续多表示结论，需要给出显式 x、互异表示族的注入证明、收敛证明和形式化或半形式化核验。

### 公开版思考摘要

本题不是纯猜想型难题：每个有限候选表示都有很短的可验证整数证书，备注中还包含一个已知无限族恒等式，因此模型和工具可以可靠复现、形式化和扩展计算证据。真正困难在于把这些证书提升为任意 n 的统一证明，或为无限级数部分给出无歧义的连续多表示构造。因此它适合 GPT-5.5 显著推进和验证，但不应预期仅凭一次搜索就完整解决全部开放部分。

### 免责声明

以上是 AI 可推进性评估，不是该 Erdős 问题的解答，也不声称证明了“对所有 n 成立”或给出了满足条件的有理 x。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `revised_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_261.md](../../prompts/problem_261.md)

### 状态结论

“无穷多个 n”已解决；原文把全体 n 与连续统表示两个不同问题并列，且历史上弱化成“两种表示”的版本会被简单恒等式平凡化，因此需修订。

### 当前规范陈述

首要目标：证明或否定每个正整数 n 都存在 t≥2 及两两不同的正整数 a_i，使 n/2^n=Σa_i/2^{a_i}。次要且独立的目标：在明确固定序列约定后，判断是否有有理数 x 具有连续统多个表示 x=Σa_k/2^{a_k}。

```text
Primary target: prove or disprove that for every positive integer n there exist t>=2 and pairwise distinct positive integers a_1,...,a_t such that n/2^n=sum_i a_i/2^{a_i}. Secondary separate target: determine whether some rational x has continuum many representations x=sum_{k>=1} a_k/2^{a_k} under an explicitly fixed convention for the sequence (a_k).
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 恒等式 4/2^4=5/2^5+6/2^6 可把共同尾部接到两侧，说明仅要求两个表示的弱版本不能作为研究目标。
- 版本变化: Cusick/Borwein–Loring 已证明无穷多个 n；TUZ 验证到 n≤10000；剩余为全体 n 与经澄清的连续统表示问题。

陈述问题：

- 有限和中的 a_i 必须两两不同。
- 无限级数中的 a_k 是否递增、互异以及重复是否允许必须固定。
- “两种表示”弱版本因拼接恒等式而可能平凡。

需要固定的量词/约定：

- The primary target ranges over every positive integer n.
- For the continuum target, define equality of representations and convergence conventions before proving cardinality.

### 文献与当前边界

已核验的主要结果：

- n=2^{m+1}-m-2 给出无穷多个解例。
- 所有 n≤10000 已被验证。
- 弱化的两表示问题可由简单拆分恒等式处理。

最近相关工作：TUZ 2020 给出大范围有限验证；题目讨论澄清了历史弱版本的平凡化风险。

剩余核心：证明所有 n 的有限互异表示，或找到一个严格反例；连续统问题须单独且按固定约定处理。

已使用方法：

- 局部拆分恒等式与保持互异性的重写系统。
- 二进制估值、有限状态归纳和障碍分类。

争议或不确定性：

- 两个子问题不应在一个完成声明中混淆。
- 历史原文对无限表示的约定不足。

### 证据来源

- [Erdős Problem 261](https://www.erdosproblems.com/261) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 261](https://www.erdosproblems.com/latex/261) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。

### 完成标准

- 肯定出口: For the primary target, give a terminating construction valid for every n and prove positivity, pairwise distinctness, and the exact identity.
- 否定出口: Exhibit a specific n and prove no finite set of at least two distinct positive indices represents n/2^n.

不构成完成：

- The already known infinite family of n.
- Verification for any finite range.
- A construction allowing repeated a_i.
- Solving only the trivial two-representation weakening.

正确性陷阱：

- Preserve pairwise distinctness after every rewrite.
- Do not infer all n from a density-one or unbounded family.
- Keep the continuum target logically separate.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `46/100`
- 信心: `medium`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 构造可终止且保持互异性的局部展开规则。
- 寻找估值或模约束以分类潜在最小反例。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
