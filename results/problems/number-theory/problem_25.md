# Problem 25

## 基本信息

- 原始链接: https://www.erdosproblems.com/25
- LaTeX 页面: https://www.erdosproblems.com/latex/25
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $1\leq n_1<n_2<\cdots$ be an arbitrary sequence of integers, each with an associated residue class $a_i\pmod{n_i}$. Let $A$ be the set of integers $n$ such that for every $i$ either $n<n_i$ or $n\not\equiv a_i\pmod{n_i}$. Must the logarithmic density of $A$ exist?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `29/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：density
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: density
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5-level model with tools`
- 结论: **有可能显著推进或验证大量候选结构，但直接完整解决的概率偏低；更适合评为中等候选。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 可行路线是把问题转化为对指示函数的对数平均收敛性分析：先形式化有限模数截断的对数密度近似，再研究新增同余类对加权平均的扰动是否形成可控 Cauchy 过程；并用计算搜索构造极端残基选择，尝试让对数密度沿不同尺度振荡。若找不到反例，则证明方向可能需要抽象出“阈值 n_i 与模 n_i 同步增长”带来的稳定性机制。

### 支持理由

- 题目表述短、对象明确，适合形式化建模：集合 A 的成员性可写成有限乘积条件，因为判断 n 只需检查 n_i<=n 的同余类。
- 对数密度比自然密度更适合用调和权重和分块估计处理，计算实验可以可靠测试许多构造性残基策略。
- 工具辅助模型可并行做三类工作：自动搜索振荡反例、证明有限截断稳定性引理、在证明助理中验证纯组合或调和和估计。
- 问题不要求分类所有序列，而是一个存在性问题；若存在通用 martingale/筛法/对数平均紧性论证，AI 可能帮助发现并形式化关键引理。

### 主要障碍

- 量词极强：n_i 和 a_i 完全任意，局部构造可以依赖此前所有选择，常规独立性或随机模型很难直接适用。
- 同余类之间高度相关；模数不要求互素，覆盖效应可能在不同尺度上被精细操控。
- 若答案为否，反例可能需要非常稀疏且自适应的尺度设计，单纯有限搜索难以证明无限振荡。
- 若答案为是，需要证明所有可能构造都不能破坏对数平均收敛，这类全局紧性结论通常比实验验证困难得多。

### 需要的验证

- 建立精确的形式化定义：对数密度采用 lim_{x->infty} (1/log x) sum_{n<=x,n in A} 1/n，并明确只讨论正整数或整数版本的等价处理。
- 对任何提出的正向证明，需要独立检查截断误差、极限交换、以及非互素模数造成的相关项。
- 对任何候选反例，需要证明两条子序列上的对数平均极限确实分离，而不是有限尺度假象。
- 需要用计算生成的猜想反复交叉验证，并最好把核心估计放入 Lean/Isabelle 等证明助理或至少机器可检查的证明脚本中。

### 公开版思考摘要

该问题的核心难点不是计算单个集合 A，而是任意同余排除规则下对数平均是否必然收敛。GPT-5.5 级别模型配合搜索和形式化工具，可以把问题拆成可验证的有限截断、调和权重估计和反例尺度构造，从而有现实机会产生有价值引理或排除大类构造。但由于任意模数和任意残基带来强相关与自适应构造空间，完整证明或反例仍需要一个非平凡的新机制，因此不应评为高候选。

### 免责声明

以上只是 AI 可解性与推进潜力评估，不是该 Erdős 问题的解答，也没有声称证明对数密度存在或不存在。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_25.md](../../prompts/problem_25.md)

### 状态结论

截至审计日，问题 25 的在线条目及其论坛页均明确标为开放，且论坛没有完整或部分解答的声称。2026-03 的 Chojecki 手稿明确只给出两个特殊情形、一个条件归约和障碍，未声称解答。对精确陈述、相关问题 486、近三年论文和 arXiv 的定向检索未发现可检查的解答或反例。因此可将其作为定义良好的当前开放问题处理，但“开放”仍只有中等置信度：站点也明确警告其标签只是维护者的当前判断，且原始 [Er95] 书目信息未能独立恢复。

### 当前规范陈述

对任意严格递增正整数序列 n_1<n_2<⋯，以及任意剩余类 a_i (mod n_i)，定义 A⊆N：当且仅当对每个 i≥1，均有 n<n_i 或 n 不同余 a_i (mod n_i) 时 n∈A。是否总有极限 δ_log(A)=lim_{x→∞}(1/log x)∑_{n≤x,n∈A}1/n？若存在，采用 n<x 或 n≤x 的定义等价。

```text
For every strictly increasing sequence of positive integers n_1<n_2<⋯ and every choice of residue classes a_i mod n_i, define A⊆N by n∈A iff, for every i≥1, either n<n_i or n is not congruent to a_i modulo n_i. Does the limit δ_log(A)=lim_{x→∞}(1/log x)∑_{n≤x, n∈A}1/n exist? The use of n<x instead of n≤x gives the same limit when it exists.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能使字面命题失败的简单构造。边界例 n_1=1 必有 A=∅，其对数密度为 0，故不是反例；它也说明无需排除 n_1=1。此结论只是针对性检查，不是对所有构造的穷尽排除。
- 版本变化: 站点将本题列为 Erdős [Er95]，并称其为问题 486 的单一剩余类特例；问题 486 至少在 2026-04-08 仍标为开放。2026-01-20 页面更新时问题 25 仍为开放。2026-03-19 出现 Chojecki 的非同行评议手稿，给出特殊情形、条件性归约及障碍而非修订或闭合。本题的 Lean 文件仅形式化了带 `sorry` 的命题，未机械证明。

陈述问题：

- 原文的 “integers n” 应规范为正整数；这是对数密度的标准域，且与 n<n_i 的阈值条件一致。
- 必须明确第 i 个同余类从 n_i 开始生效，包括 n=n_i；不能把 A 误作固定同余类并集的普通补集。
- a_i 是模 n_i 的类，代表元不影响问题。
- 问题 486 的页面使用条件 m>n，而本题使用 n≥n_i；站点称 486 是一般化，但把本题嵌入 486 时须核对这一端点差异（尤其 a_i≡0 时），不得无证明地视为逐点相同。

需要固定的量词/约定：

- The assertion is universal over both the infinite strictly increasing modulus sequence and all residue-class choices.
- For every fixed n, only finitely many conditions are active, since n_i≤n can hold for only finitely many i.
- Logarithmic density means a genuine limit, not only equality of limsup and liminf, and no natural-density assertion is requested.

### 文献与当前边界

已核验的主要结果：

- Davenport–Erdős（1936，同行评议）证明了“禁去某集合中任一模数的倍数”所形成集合的对数密度存在；问题 486 页面将此表述为 X_n={0} 的肯定答案。它不能直接覆盖任意非零剩余类。
- Chojecki（2026-03-19，未同行评议手稿）证明/给出完整论证：若 ∑_i 1/n_i<∞，则 A 甚至有自然密度；若 n_i 两两互素，则 A 也有自然密度。前者可由尾部并集的密度上界完成；后者在倒数和发散时由有限前缀 CRT 乘积趋于 0 完成。
- 对每个有限前缀 A^(k)，其成员资格最终以 lcm(n_1,…,n_k) 为周期，因而自然和对数密度 δ_k 都存在；δ_k 单调下降至候选值 δ。困难在于不能自动把 k→∞ 与 x→∞ 的调和加权极限交换。

最近相关工作：检索到的最新直接工作是 Przemyslaw Chojecki 于 2026-03-19 发布的 13 页手稿《Truncated Congruence Sieves and Erdős Problem 25》。它明确将“全问题”留作未解，并将其归约到有限 quotient sieves 的统一调和误差及全局次对数 charge 控制；未找到同行评议或 arXiv 预印本形式的完整解答。

剩余核心：证明或构造反例：任意阈值激活的单个同余类删去系统 A 都有对数密度。等价地，需证明实际 A 的调和质量收敛到有限前缀密度 δ_k 的极限，或给出一组递增模数和类，使该调和平均沿两个趋于无穷的截断序列有不同极限。

已使用方法：

- Davenport–Erdős 的倍数集/对数密度方法（零类特例）。
- 有限前缀的最终周期性与中国剩余定理。
- first-kill 分解：把 N\A 分解为首次被第 i 个约束删除的互不交集合 E_i。
- Chojecki 的 quotient-sieve 重参数化和熵型总误差控制；该手稿将关键统一调和估计列为条件而非定理。
- 覆盖系统与区间筛的相关文献只能作为启发：该手稿没有从这些结果推出本题结论。

争议或不确定性：

- 站点明确提醒其开放状态不是文献完备性保证；本次检索未发现解答不构成不存在解答的证明。
- 论坛中的“full problem resolution is a question of time”是作者意见，不是定理；同帖也链接了指出小问题的 AI 审阅，不能视为解答。
- 问题 25 的 [Er95] 原始书目信息未能从可访问页面恢复，需人工图书馆检索补全。
- 问题 25 与 486 的端点约定不同；其“特殊情形”关系应在任何正式约化中单独证明。

### 证据来源

- [25 Discussion Thread | Erdős Problems](https://www.erdosproblems.com/forum/thread/25) — Thomas F. Bloom / Erdős Problems; forum commenters, 2026-01-20; `forum`, `database_record`, directness=`direct`, reliability=`medium`. 页面逐字给出问题陈述，标为 OPEN，称不能以有限计算解决；声明该开放标签只是站点维护者的当前判断；并显示“评论中没有完整或部分解答声称”。该页还链接问题 486、2026 年形式化文件和 Chojecki 的手稿。
- [Erdős Problems — LaTeX source for Problem 486](https://www.erdosproblems.com/latex/486) — Thomas F. Bloom / Erdős Problems, 2026-04-08; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 给出问题 486 的一般形式、其开放标签、Davenport–Erdős 零剩余类结果、Besicovitch 的自然密度反例背景，并称 486 一般化了 25。
- [A survey of problems in combinatorial number theory](https://combinatorica.hu/~p_erdos/1980-03.pdf) — Paul Erdős, 1980; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原始综述提出与问题 486 对应的任意多个剩余类版本，并记述当时该问题尚未被认真研究；它是历史来源，不是当前开放状态的证据。
- [On sequences of positive integers](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/all/2/1/93274/on-sequences-of-positive-integers) — Harold Davenport; Paul Erdős, 1936; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 核实 Davenport–Erdős 1936 年论文的作者、期刊、页码和 DOI。结合问题 486 的精确说明，它支持“当每个禁类为 0 时，对数密度存在”的已知特殊结果。
- [Truncated Congruence Sieves and Erdős Problem 25](https://www.ulam.ai/research/erdos25.pdf) — Przemyslaw Chojecki, 2026-03-19; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 作者明确说该手稿没有完整证明；其中给出 ∑1/n_i<∞ 与两两互素模数的肯定特殊情形、first-kill/quotient-sieve 分解、一个依赖新局部调和估计的条件归约，以及两个对朴素路线的障碍。
- [FormalConjectures/ErdosProblems/25.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/25.lean) — Google DeepMind Formal Conjectures contributors, 2026; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 文件精确形式化了全称命题，但主定理以 `by sorry` 结束。因此“formalized”在此仅表示陈述已编码，绝不表示 Lean 已验证其证明。

### 完成标准

- 肯定出口: Prove, for every allowed (n_i,a_i), that lim_{x→∞}(log x)^{-1}∑_{n≤x,n∈A}1/n exists. The proof must control the infinite tail uniformly enough to justify the limit; identifying a candidate δ=lim_k δ_k is not sufficient by itself.
- 否定出口: Give one explicit strictly increasing modulus sequence and residue choices for which the displayed harmonic averages do not converge, with a rigorous certificate of two subsequences X_j,Y_j→∞ whose limiting values differ (or an equally rigorous nonconvergence argument).

不构成完成：

- A proof only for summable reciprocal moduli, pairwise-coprime moduli, or zero residue classes.
- A finite-prefix periodicity calculation, or numerical values up to finite cutoffs without a certified tail bound.
- A conditional proof whose quotient-sieve hypothesis or global-charge estimate remains unproved.
- Evidence that natural density need not exist; the target asks for logarithmic density.
- An appeal to Problem 486 without verifying its hypotheses and its strict threshold convention.

正确性陷阱：

- Keep the activation condition n≥n_i, including equality.
- Do not interchange k→∞ and x→∞ merely from monotonicity of A^(k).
- Treat harmonic mass, not cardinality on selected intervals, when proving convergence or oscillation.
- If using first-kill sets, prove that accumulated local errors are o(log X); a bounded error for each fixed i is insufficient.
- Separate the coded Lean statement containing `sorry` from a verified formal proof.
- Check the m>n versus m≥n endpoint before importing a result from Problem 486.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `24/100`
- 信心: `medium`
- 结论: 这是一个定义明确、可审计且仍开放的目标；近期手稿给出了有价值的结构化归约和可证伪的障碍，但关键统一调和估计仍远超有限计算可直接解决的范围。适合以证明优先的多路线研究进入，不适合以大规模数值实验作为主线。

支持理由：

- 全称命题、肯定结论和反例结论均可精确验证。
- 有限前缀、first-kill 集和 quotient sieves 提供了可分解的中间对象，而不是完全无结构的密度问题。
- 近期手稿明确指出候选极限与一个具体未解决的局部—全局误差机制。

主要障碍：

- 任意非互素模数和任意类允许强相关性；有限前缀极限并不自动控制无限尾。
- prime-power tower 例显示单个 first-kill 集能产生远大于其最终密度损失的短暂调和峰。
- 已知零类定理和自然密度失败例都不能直接处理任意平移类的阈值筛。

Proof-first 路线：

- 寻求一个不依赖未证假设的、对有限 quotient sieve 的统一调和误差界，并证明其误差可全局求和为 o(log X)。
- 改从反例路线出发：设计分块的相关模数/剩余类，并以精确调和区间估计证明不同对数尺度上的行为分离。
- 研究何种额外结构（例如 gcd 图、模数增长、局部冗余）足以保证收敛，再判断其能否通过分解或归纳推广。

需要验证：

- 补全和检查问题 25 所引 [Er95] 的原文、页码和准确历史表述。
- 对 Chojecki 手稿中的所有“无条件”论证进行独立逐步审查；不得把其条件归约当作完整定理。
- 若利用问题 486，单独证明或查证 m>n 与 n≥n_i 的端点处理。
- 定期重跑精确陈述、作者名和 arXiv/期刊的状态搜索。

### 审计限制与人工复核理由

- Erdős Problems 的主页面及 LaTeX URL 对直接抓取返回 403；审计改用可访问的官方论坛页和搜索索引的 LaTeX 内容。
- 未能恢复问题 25 标注的原始 [Er95] 的完整书目信息，故不能声称已审阅该原始出处。
- 未发现完整解答是经过多组定向查询后的搜索结果，不是数学上对未发表结果不存在的证明。
- Chojecki 手稿为作者托管的未同行评议文稿；其特殊情形和归约不应提升为已被独立验证的完整文献结论。

- 需要图书馆或人工书目工具补全并审阅 [Er95] 原始来源。
- 若研究依赖 486 的一般化关系，需由审阅者严格解决 m>n 与 n≥n_i 的端点差异。
- 在投入长期研究前，建议由数论专家独立核对 2026 手稿的特殊情形证明和条件归约。

<!-- DEEP_REVIEW:END -->
