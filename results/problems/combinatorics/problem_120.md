# Problem 120

## 基本信息

- 原始链接: https://www.erdosproblems.com/120
- LaTeX 页面: https://www.erdosproblems.com/latex/120
- 原始状态: `open`
- 奖金: `$100`
- 主类别: `combinatorics`
- 原始标签: `combinatorics`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: Erdős similarity problem

## 原问题

Let $A\subseteq\mathbb{R}$ be an infinite set. Must there be a set $E\subset \mathbb{R}$ of positive measure which does not contain any set of the shape $aA+b$ for some $a,b\in\mathbb{R}$ and $a\neq 0$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 原记录含奖金 $100，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: combinatorics
- 证明密集标签命中: 无
- 有限/计算线索: finite
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。GPT-5.5 级别模型配合计算、形式化证明和文献检索，较可能在特殊序列、已知证明整理、反例/构造搜索和形式化验证上取得可审计进展；但直接解决完整 Erdős similarity problem 的概率仍低，尤其因为连很规则的收敛序列情形仍在备注中标为开放。**
- 等级: `low_to_medium_candidate`
- 分数: `34/100`
- 信心: `medium`
- 可能路线: 较现实的路线不是直接攻击任意无限集，而是利用备注中的归约，集中到严格单调并收敛到 0 的可数序列 A。模型可尝试把问题转化为正测度集 E 对所有仿射拷贝 aA+b 的避免条件，系统检索并形式化已有特殊情形；随后对特定序列建立随机删点、厚 Cantor 集、密度点、能量估计或树状构造，并用计算搜索验证有限截断的可行模式。形式化证明工具可用于检查归约、测度论引理和特殊构造的无误性。

### 支持理由

- 题目陈述短，结构清楚，且备注给出关键归约：只需考虑收敛到 0 的严格单调可数序列，这使自动化探索有明确入口。
- 该问题已有不少特殊情形结果和综述脉络，模型可通过文献检索重建方法谱系，避免从零开始。
- 形式化状态为 yes，说明至少存在适合机器检查的表达或框架；这有利于验证局部引理、归约和候选证明。
- 有限截断、稀疏序列、几何型序列、Cantor 型正测度集等方向适合计算搜索和自动反例排除，可能产生新猜想或特殊定理。

### 主要障碍

- 完整问题要求对任意无限 A 构造一个正测度 E，同时排除所有非零缩放和平移 aA+b，量词结构很强。
- 有限集情形为假，说明不能简单从有限截断稳定性推出无限情形；有限计算证据可能误导。
- 备注指出即使 A={1,1/2,1/4,...} 这样的高度规则序列仍开放，表明核心困难不是仅由复杂 A 引起。
- 正测度条件与避免所有仿射拷贝之间存在强测度论约束，通常需要精细的密度点、概率或构造性分析，自动证明难度高。
- 模型容易把“避免长有限模式”误认为“避免整个无限仿射拷贝”，需要严格区分有限近似与无限包含。

### 需要的验证

- 核对已形式化版本的精确定义，特别是正测度、子集、仿射拷贝和无限包含的量词顺序。
- 系统复现备注中已知情形：A 无界、A 在某区间稠密、以及归约到单调收敛序列的证明。
- 对任何候选构造 E，必须证明其 Lebesgue 测度为正，并证明对所有 a≠0,b 都不含 aA+b，而不是只检查可数参数网格。
- 若得到特殊序列结果，需要与已知特殊情形综述逐条比对，确认不是已有定理的弱化或重述。
- 计算搜索只能作为猜想生成；最终需解析证明或可机检证明来排除连续参数空间中的所有仿射拷贝。

### 公开版思考摘要

这个问题对 AI 有一定可操作性，因为陈述简洁、归约明确、已有形式化基础，并且特殊情形适合结合文献、计算和证明检查推进。但完整命题的障碍很硬：它涉及任意收敛序列、正测度集合的构造以及连续族仿射拷贝的全局排除。综合判断，GPT-5.5 更可能产出可验证的特殊情形、方法统一或形式化验证，而不是一次性解决原问题。

### 免责声明

以上只是对 GPT-5.5 级别模型可推进性的审查，不构成该 Erdős 问题的解答或证明。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_120.md](../../prompts/problem_120.md)

### 状态结论

Problem 120 的原命题仍是一个定义良好且确认开放的问题。2025 年同行评审综述、2026 年两篇直接相关预印本以及 Erdős Problems 当前页均明确将其列为未解；尤其几何序列 {2^{-n}} 仍未解决。发现的 2020 年预印本曾声称完整证明，但其后的同作者 2022 预印本和后续文献明确称猜想仍开放；该旧声明不能视为解答。

### 当前规范陈述

对每个无限集 A⊆ℝ，存在一个 Lebesgue 可测集 E⊆ℝ，满足 λ(E)>0，且对任意 a,b∈ℝ、a≠0，都有 aA+b⊄E；其中 aA+b={ax+b:x∈A}。等价地，不存在无限的“测度普遍”集合：所谓测度普遍，是指它的每个正 Lebesgue 测度可测集都包含其一个非退化仿射拷贝。

```text
For every infinite set A ⊆ ℝ, there exists a Lebesgue-measurable set E ⊆ ℝ with λ(E) > 0 such that, for every a,b ∈ ℝ with a ≠ 0, aA+b is not a subset of E, where aA+b := {ax+b : x ∈ A}. Equivalently, no infinite subset of ℝ is measure universal, where “measure universal” means that every Lebesgue-measurable positive-measure subset of ℝ contains a nonconstant affine copy of it.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能推翻字面无限集命题的简单构造。有限集的相反现象由 Steinhaus 证明，但有限性被原命题明确排除。检索还确认最基本的快速衰减候选 A={2^{-n}:n≥1} 仍未解，因此不能把任何有限近似、零测度回避构造或“几乎所有参数”结果误作反例或解答。
- 版本变化: 没有发现原问题被后续文献改写为非等价的主问题。术语上，现代文献把它表述为“没有无限 measure-universal set”。近年工作同时研究 topological、bi-Lipschitz、full-measure 与“in the large”等变体；这些变体必须与原问题区分。2025 年 Shmerkin–Yavicoli 的“不 full-measure universal”结果在其适用类别中确实蕴含原问题的肯定答案，但对任意 Cantor 集的较弱结论并不蕴含原问题。

陈述问题：

- 原文“positive measure”未明说 Lebesgue 可测性。当前文献将其标准化为“positive Lebesgue measure”，Formal Conjectures 的陈述也显式要求 E 可测；本审计采用这一标准读法。
- “does not contain any set of the shape aA+b”必须读作对所有 a≠0、b，整个集合 aA+b 都不是 E 的子集，而不是只排除某些有限子构型。
- A 不要求可测、闭、可数或有界；缩放 a 允许为负，平移 b 任意。

需要固定的量词/约定：

- The logical order is ∀ infinite A ⊆ ℝ, ∃ measurable E with λ(E)>0, ∀ a,b ∈ ℝ, a≠0 ⇒ aA+b ⊄ E.
- E may depend on A, but must work simultaneously for every permitted scale and translation.
- A itself has no measurability or cardinality restriction beyond infinitude.
- The condition a≠0 excludes collapsed constant images; both orientations are allowed.

### 文献与当前边界

已核验的主要结果：

- Steinhaus（1920，同行评审）通过 Lebesgue 密度论证显示有限集 measure universal；这解释了为何无限性是必要边界，而不构成原问题的反例。
- Falconer（1984）与 Eigen（1985）独立证明：对递减到 0 且 a_{n+1}/a_n→1 的 sublacunary 序列，存在正测度回避集。Jung–Lai–Mooroogen 的 2025 综述给出此结果及其在问题约化中的作用。
- Shmerkin–Yavicoli（Advances in Mathematics, 2026）证明若 Borel 集的对数 Hausdorff 维大于 1 或对数 packing 维大于 2，则它不是 full-measure universal；full-measure 非普遍性蕴含 measure 非普遍性，故这是原猜想在大类零维或正维集合上的肯定结果。
- Iosevich–Yavicoli（2026 预印本）以改造的 Falconer lattice set 与 Bourgain 三重和结果，覆盖另一类对数维很小的薄集合；其机制不是慢衰减序列条件。
- Mora Cuellar–Iosevich–Kulkarni–Rojas Aravena–Yavicoli（2026 预印本）对两个 lacunary 子序列的和/差给出有限网格和近加性能量方法；特别证明 {2^{-n}}±A 对任意无限 A 都非 measure universal。

最近相关工作：截至审计日最新的直接文献是 2026-07-03 的 Mora Cuellar 等预印本 arXiv:2607.03584。它明确重申总猜想开放，并推进的是两个集合和/差的情形，不解决单个几何序列 {2^{-n}} 是否 measure universal。

剩余核心：仍须排除任意无限集合的 measure universality；按标准约化，核心难点包括真正 lacunary、快速衰减的递减零序列，最典型的具体未解例是 A={2^{-n}:n≥1}。一般 Cantor 集（尤其同时具有零 Hausdorff 维和零 Newhouse thickness 的情形）亦未由当前结果覆盖。

已使用方法：

- Lebesgue 密度点与 Cantor 型删区构造。
- 按相邻项比率的慢衰减/次 lacunary 判据。
- 以零测度集 B 使 f(A)+B 覆盖全空间或有内点，从而构造正测度回避集的和集对偶。
- 离散有限块、最小间隙准则与近加性能量估计。
- 对数 Hausdorff/packing 维、Fourier 衰减与多尺度归纳。
- Falconer lattice 构造加 Bourgain 关于三重和的非普遍性结论。

争议或不确定性：

- arXiv:2001.02395 的摘要仍显示“proof”声明，但没有经核验的解决物；其后同作者和独立的较新文献均称问题开放。本审计据此不接受该声明，同时建议人工追查其撤回、错误或替代历史。
- Erdős Problems 的 LaTeX 页面在本次访问中返回 403；问题页的缓存内容和 Formal Conjectures 文件与输入陈述一致，但无法直接核验该 LaTeX 源。
- “positive measure”的标准解释为 Lebesgue 可测且正 Lebesgue 测度；若项目需要外测度版本，应另行指定，尽管对本存在性问题采用可测构造已足以满足通常表述。

### 证据来源

- [Erdős Problem 120](https://www.erdosproblems.com/120) — Thomas F. Bloom / Erdős Problems, 2026-01-23; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前页将问题列为 open，说明无评论区的完整或部分解答声明，并记录几何序列示例仍开放；该站也提醒其状态不能代替文献核验。
- [Fifty years of the Erdős similarity conjecture](https://arxiv.org/abs/2412.11062) — Yeonwook Jung, Chun-Kit Lai, Yuveshen Mooroogen, 2025; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 同行评审综述（Research in the Mathematical Sciences 12, Article 9）明确称原猜想仍开放，特别指出指数衰减序列及零 Hausdorff 维且零 Newhouse thickness 的 Cantor 集未解；给出 Falconer–Eigen 等既有结果和变体边界。
- [Full measure universality for Cantor sets](https://www.sciencedirect.com/science/article/pii/S0001870826002008) — Pablo Shmerkin, Alexia Yavicoli, 2026-06; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明具有 dim_H^log(A)>1 或 dim_P^log(A)>2 的 Borel 集不是 full-measure universal，故在这些类别中原猜想成立；同时明确指出一般问题仍广泛开放，{2^{-n}} 是否 measure universal 未知。
- [Falconer lattice sets and the Erdos similarity problem](https://arxiv.org/abs/2604.01493) — Alex Iosevich, Alexia Yavicoli, 2026-04-02; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 为一类极薄、含有快速衰减序列的 Falconer lattice/Cantor 型集合证明原猜想；作者同时明确称快速衰减序列的一般情形仍开放。
- [Non-universality of sumsets of lacunary sequences and arbitrary sets](https://arxiv.org/abs/2607.03584) — N. Mora Cuellar, A. Iosevich, N. Kulkarni, I. Rojas Aravena, A. Yavicoli, 2026-07-03; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 最新直接相关预印本明确说猜想仍开放；它证明若干两个集合和/差的非普遍性，包括 {2^{-n}}+A 与 {2^{-n}}−A 对任意无限 A 的情形，但不是对 {2^{-n}} 本身的解答。
- [Large sets avoiding affine copies of infinite sequences](https://arxiv.org/abs/2204.12720) — Angel Cruz, Chun-Kit Lai, Malabika Pramanik, 2022-04-27; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 同一作者组明确称猜想对大多数快速衰减序列（包括 {2^{-k}}）仍开放；该文仅构造 Hausdorff 维为 1 但 Lebesgue 零测度的回避集。它是对 2020 完整证明声明不可采信的直接后续证据。
- [A proof of the Erdös similarity conjecture](https://arxiv.org/abs/2001.02395) — Angel Cruz, Chun-Kit Lai, Malabika Pramanik, 2020-01-08; `preprint`, `preprint`, directness=`direct`, reliability=`low`. 该预印本摘要声称完整证明，但未找到可供本审计核验的完整论证或同行评审出版物；其后的同作者文献及 2025–26 文献明确仍称问题开放，因此只能作为未证实且已被后续记录否定的声明处理。
- [Formal Conjectures: ErdosProblems/120.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/120.lean) — Formal Conjectures Authors / Google DeepMind repository contributors, 2026; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 该 Lean 文件精确形式化了可测正测度 E 与所有非零仿射参数的陈述，但主定理和有限集变体均使用 sorry；它是陈述形式化，不是经内核验证的解决证明。

### 完成标准

- 肯定出口: Prove that for every infinite A ⊆ ℝ there is a Lebesgue-measurable E ⊆ ℝ with λ(E)>0 such that ∀a,b∈ℝ, a≠0 implies {ax+b:x∈A} is not a subset of E. The proof must cover arbitrary infinite A, or rigorously reduce all such A to cases already covered plus a complete treatment of the residual decreasing-zero-sequence case.
- 否定出口: Exhibit one specified infinite A ⊆ ℝ and prove that every Lebesgue-measurable E ⊆ ℝ with λ(E)>0 contains a nonconstant affine copy aA+b for some a,b∈ℝ with a≠0.

不构成完成：

- Handling only finite sets, unbounded sets, dense-in-an-interval sets, sublacunary sequences, positive/logarithmic-dimension classes, or a selected Cantor family.
- Constructing an avoidance set of Hausdorff dimension 1 but Lebesgue measure zero.
- Showing avoidance for almost every (a,b), for a positive-measure set of parameters, or for each scale using an E that depends on that scale.
- Proving a topological, bi-Lipschitz, full-measure, or “in the large” variant without a valid implication back to the original target.
- A result about {2^{-n}}+B or {2^{-n}}−B for B infinite; it does not settle the singleton-sequence target {2^{-n}}.
- A finite computation, a finite truncation of A, or an unverified preprint claim.

正确性陷阱：

- Audit the quantifier order: E is chosen after A but before all a,b, and it must exclude every copy of the whole infinite A simultaneously.
- Do not accidentally allow the degenerate scale a=0 or restrict to a>0 without separately handling reflection.
- State whether E is Lebesgue measurable and establish λ(E)>0, not merely nonempty, full Hausdorff dimension, residual, or positive outer-content at finite stages.
- When using a subset B⊆A, use the inclusion in the correct direction: an E avoiding B automatically avoids A.
- When invoking a full-measure/non-universality or sumset theorem, verify its exact family of maps and the logical implication to positive-measure avoidance.
- For any purported resolution, reconcile it explicitly with the still-open {2^{-n}} case and the 2020 unverified arXiv claim.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `8/100`
- 信心: `high`
- 结论: 这是适合长期、严格证明探索的开放问题，但不是当前 AI 高概率可解决的目标；评分仅针对原始全称命题。

支持理由：

- 目标具有明确的一阶量词结构和可机械核查的最终条件。
- 已有多条强而互不相同的部分结果路线，能产生可验证的中间引理或新特殊类结果。
- 近期工作精确暴露了快速衰减、一般 Cantor 集与两个集合和问题之间的边界。

主要障碍：

- 剩余目标是对任意无限集的全称断言，最基本的几何快速衰减序列仍未解，说明现有方法未跨越核心障碍。
- 全局正测度构造必须同时控制不可数参数族 (a,b) 和整个无限模式；有限截断或数值实验几乎不能逼近该量词难度。
- 2020 年未证实完整证明声明是文献噪声风险，任何新路线必须先通过强对抗性审计。

Proof-first 路线：

- 首先把任何候选新原理表述为一个明确的充分条件：例如对快速衰减序列构造统一零测度障碍集 B，使所有非零缩放的 A+B 具有所需覆盖性质；在证明该引理前不扩大为计算搜索。
- 尝试识别覆盖 {2^{-n}} 的中间类别，并严格检查它不只是已知的 sumset、topological 或 full-measure 变体。
- 将现有离散间隙/能量框架与多尺度回避构造作概念性比较，优先寻找可证明的桥接引理而非拟合增长率。

需要验证：

- 人工读取并追踪 arXiv:2001.02395 的版本历史、撤回或错误说明，以及其与 2022 同作者论文的关系。
- 核对 2025–26 各定理的全部正则性假设、维数阈值、映射族与从 full-measure 变体回到原命题的逻辑。
- 若出现声称解决 {2^{-n}} 的新稿，要求逐项对照上述量词、正测度和全部仿射参数。

### 审计限制与人工复核理由

- 本审计进行了针对性网页与 arXiv 检索，但不能从“未找到新解”逻辑推出不存在新解；结论依赖截至 2026-07-27 可访问的当前记录与原始文献。
- Erdős Problems 的问题页可由搜索缓存核验，但其 LaTeX URL 的直接抓取返回 403。
- 未能取得 arXiv:2001.02395 的可审读正文或明确撤回/错误声明；因此没有对其证明作数学性反驳，只以同作者及后续权威文献的公开状态判断其不能作为已接受解答。
- 2026 年两篇最新结果均为预印本，尚未同行评审；其定理范围依据作者摘要与可访问 HTML 文本概述。

- 应由领域专家追踪并审读 2020 “proof”预印本的版本/撤回/错误历史，防止将未证实声明误登记为解答。
- 若后续研究系统以外测度而非通常的 Lebesgue 可测正测度解释原文，应先确认所需正式版本；本审计采用当前文献和 Lean 文件的一致标准读法。

<!-- DEEP_REVIEW:END -->
