# Problem 98

## 基本信息

- 原始链接: https://www.erdosproblems.com/98
- LaTeX 页面: https://www.erdosproblems.com/latex/98
- 原始状态: `open`
- 奖金: `no`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $h(n)$ be such that any $n$ points in $\mathbb{R}^2$, with no three on a line and no four on a circle, determine at least $h(n)$ distinct distances. Does $h(n)/n\to \infty$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `24/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 目前只能依靠通用数学推理、文献归纳和特殊情形探索

### 主要障碍

- 所属标签偏证明密集：distances, geometry
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: distances, geometry
- 有限/计算线索: 无
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选：GPT-5.5 级别模型不太可能直接完整解决该开放问题，但有现实机会在构造搜索、局部结构归纳、已有证明路线形式化、以及候选反例/上界验证方面产生有价值推进。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 最可行路线不是直接证明 h(n)/n 趋于无穷，而是把问题拆成可验证的中间目标：形式化定义极小距离数配置；用 SAT/SMT、代数约束或数值优化搜索小 n 的低距离配置；分析“无三点共线、无四点共圆”如何限制重复距离图；尝试证明某些额外假设下的线性以上下界；并复核已有上界构造是否可被扰动且保持距离种类少。若能找到稳定的结构定理或排除一大类近线性构造，才可能进一步接近主命题。

### 支持理由

- 题目陈述短、约束清晰，适合被转写为组合几何、图论和代数约束问题，便于计算搜索与形式化验证参与。
- 问题目标是渐近下界 h(n)/n -> infinity，不要求精确确定 h(n)，因此存在通过中间增长下界取得显著推进的空间。
- 备注中已有非平凡上界 n exp(c sqrt(log n))，说明存在可分析的接近线性构造族；AI 可围绕这些构造做扰动、验证和结构抽象。
- 无三点共线、无四点共圆是强一般位置条件，可能让重复距离图受到额外限制，适合用自动化枚举和局部禁图分析寻找新引理。

### 主要障碍

- 核心难点是全局渐近下界，而不是有限规模验证；小 n 搜索很难直接推出 h(n)/n -> infinity。
- 重复距离结构可以非常复杂，仅靠一般位置条件未必足以给出容易证明的超线性下界。
- 若已有上界构造接近线性且可满足这些一般位置条件，则任何下界证明都必须非常精细，普通启发式推理风险高。
- 形式化欧氏几何中的圆、距离相等、共线性和一般位置扰动会带来较重的代数复杂度。

### 需要的验证

- 系统检索并核对该问题的最新进展，确认是否仍开放以及 h(n) 的最好已知下界。
- 对小 n 进行精确或高置信度计算搜索，记录最少 distinct distances 的候选配置，并验证一般位置条件。
- 把候选证明中的关键几何引理转写为代数或图论命题，用 Lean/Isabelle 或 CAS 辅助检查。
- 复现备注中的上界构造，确认其是否满足或可调整为满足无三点共线、无四点共圆，同时保持距离种类上界。

### 公开版思考摘要

该问题适合作为 AI 辅助研究对象，因为它有明确的有限配置定义、可计算的搜索空间切片、可形式化的一般位置条件，以及已有上界可供逆向分析。但主命题是开放的渐近组合几何下界，通常需要新的结构性思想；GPT-5.5 更可能先产生局部定理、排除若干构造族、复现和验证已知界，而不是一次性给出完整证明。

### 免责声明

以上是对 AI 辅助可推进性的审查，不是该 Erdős 问题的解答，也不声称证明或反驳 h(n)/n -> infinity。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_98.md](../../prompts/problem_98.md)

### 状态结论

该题的精确定义良好，现有直接证据支持其仍为开放问题：已知下界仅为线性 h(n)≥⌈(n−1)/3⌉，而 Erdős–Füredi–Pach–Ruzsa 给出 h(n)≤n exp(C√log n)。后一个上界仍比线性大一个无界因子，故既不证明也不否定 h(n)/n→∞。截至审计日未找到针对该精确“无三点共线且无四点共圆”命题的完整解答或反例；数据库在 2025 年末仍标为 open。

### 当前规范陈述

对每个整数 n≥2，令 h(n) 为所有满足“任意三点不共线、任意四点不共圆”的 n 点集合 P⊂R² 所确定的不同欧氏距离数 |D(P)| 的最小值，其中 D(P)={||p−q||₂:p,q∈P,p≠q}。问是否有 h(n)/n 当 n→∞ 时趋于 +∞？“无四点共圆”指没有一个欧氏圆含有 P 的四个不同点。

```text
For every integer n >= 2, let h(n) := min{|D(P)| : P is an n-element subset of R^2, no three points of P are collinear, and no four points of P are cocircular}, where D(P) := {||p-q||_2 : p,q in P, p != q}. Is lim_{n->infinity} h(n)/n = +infinity? Here “no four are cocircular” means that no Euclidean circle contains four distinct points of P.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定字面命题的简单构造。规则 n 边形不合格，因为其 n 个顶点共圆；整数格点不合格，因为含有三点共线及四点共圆。直接计数反而给出 h(n)≥⌈(n−1)/3⌉：固定一点时，每个以该点为圆心的距离圆至多含另外三点，因此该点至少看到 ⌈(n−1)/3⌉ 个不同距离。此只给出线性下界，不能处理所问的超线性增长。
- 版本变化: Erdős、Hickerson、Pach 在 1989 年以 G(n) 记同一类一般位置点集的最小不同距离数，并明确提出 lim G(n)/n=∞ 及 G(n)/n²=0 两问；其定理解决了后者。1993 年 EFPR 将上界强化为 n exp(C√log n)。当前 Erdős Problems 页面保持同一主问题，网页历史显示的 2025-10-20 版本未含实质性命题修订。2026 年 Grayzel 预印本解决的是 Erdős #659 的不同局部四点条件；其矩形格构造含三点共线，不能解决本题。

陈述问题：

- 原文“Let h(n) be such that any n points … determine at least h(n)”未明说 h(n) 取最大保证值（等价于上述最小值）；标准极值函数解释使其唯一化。
- “circle”应明确为非退化欧氏圆；共线限制与共圆限制均针对集合中不同点。
- 原文的“→∞”应按 n 经过整数趋于无穷理解。
- 备注“Erdős could not even prove h(n)≥n”是历史性描述，不应误读为当前最佳下界为非线性未知；已知直接的线性下界为 ⌈(n−1)/3⌉。

需要固定的量词/约定：

- h(n) is the minimum over all admissible n-point sets, equivalently the largest integer guaranteed for every such set.
- The target is a limit along positive integers n, not merely an assertion for selected n.
- A negative resolution is the existence of C < infinity and arbitrarily large n admitting an admissible P with |D(P)| <= Cn.
- All distances are positive Euclidean pairwise distances; repeated equal lengths count once in D(P).

### 文献与当前边界

已核验的主要结果：

- Erdős–Hickerson–Pach（1989，同行评审）明确提出本题的超线性问题，并给出/记录一般位置下 h(n)≥(n−1)/3；取整后有 h(n)≥⌈(n−1)/3⌉。该下界亦可由“以任一点为圆心的每个距离层至多含三点”的直接计数得到。
- Erdős–Füredi–Pach–Ruzsa（1993，同行评审）构造一般位置平面点集，使距离数 o(n^(1+ε))，任意 ε>0；当前题目页给出的定量版本为 h(n)<n exp(C√log n)。这排除了从一般位置条件直接推出 n^{1+δ} 下界的任何固定 δ>0。
- Dumitrescu（2008，同行评审）进一步表明即使再禁止平行四边形，也存在一般位置点集有 O(n²/√log n) 个距离；此结果涉及更强的禁构型变体，但对 P98 的 EFPR 上界不构成改进。
- Guth–Katz 对无约束平面点集的 Ω(n/log n) 下界当然适用，但弱于本题的线性下界，因而不是 P98 当前的决定性下界。

最近相关工作：未发现 2023–2026 年直接改进 P98 的已核实论文。最近可核实的相邻进展包括 Tao（2024 预印本、2025 接收发表）解决 Erdős #135 的 Φ(4,5) 问题，以及 Grayzel（2026 预印本）解决 #659；两者条件均不同，不能迁移为 P98 的结论。当前 P98 数据库记录仍为 open。

剩余核心：证明任意满足无三点共线、无四点共圆的 n 点集都确定 ω(n) 个不同距离，或构造无界 n 序列的一般位置点集使不同距离数 O(n)。已知线性下界与 n·exp(O(√log n)) 上界之间仍有巨大缺口。

已使用方法：

- 高维离散立方体/格点集后作泛型正交投影，以保留少量距离模式并强制一般位置。
- 用 Behrend 型无三项等差集及高维格点/球面切片控制距离类型。
- 以等腰三角形或同心圆层进行双重计数，得到线性下界。
- 禁四点模式、无平行四边形构造及概率变换；现有结果显示这些局部禁构型单独不足以自动产生所需超线性结论。

争议或不确定性：

- “general position”在某些文献只指无三点共线；本审计严格采用题目明确给出的双条件。
- 网页数据库给出的是近期、直接的开放标签，但开放状态无法仅由未检索到解答逻辑证明；因此状态标为 likely_open 而非 confirmed_open。
- Grayzel 2026 的“每四点至少三种距离”结果容易与本题混淆；该条件不排除三点共线，且其格点构造确实不满足 P98。

### 证据来源

- [Erdős Problem 98](https://www.erdosproblems.com/98) — Thomas F. Bloom / Erdős Problems project, 2025-10-20; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 当前数据库仍将该精确问题标为 open，并记录 EFPR93 的 n exp(c√log n) 上界及原始表述。
- [Erdős Problem 98, LaTeX source](https://www.erdosproblems.com/latex/98) — Thomas F. Bloom / Erdős Problems project, 2025-10-20; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 核对了题目、一般位置条件及 EFPR93 参考文献的逐字数学表述。
- [A problem of Leo Moser about repeated distances on the sphere](https://www.renyi.hu/~p_erdos/1989-02.pdf) — Paul Erdős, D. G. Hickerson, János Pach, 1989; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 该文以 G(n) 定义一般位置平面 n 点集的最少不同距离数，明确提出 G(n)/n→∞，记录 Szemerédi 的 G(n)≥(n−1)/3，并证明 G(n)/n²→0。
- [The grid revisited](https://doi.org/10.1016/0012-365X(93)90155-M) — Paul Erdős, Zoltán Füredi, János Pach, Imre Z. Ruzsa, 1993-02-22; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 论文构造平面一般位置 n 点集，距离数为 o(n^(1+ε))（每个 ε>0）；题目页记录其定量化上界 h(n)<n exp(C√log n)。
- [On distinct distances among points in general position and other related problems](https://doi.org/10.1007/s10998-008-8165-4) — Adrian Dumitrescu, 2008; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 给出一般位置且无平行四边形的点集、距离数 O(n²/√log n)，说明额外禁止平行四边形不足以导出二次距离下界；该上界本身不优于 EFPR 对本题的上界。
- [Distinct Distances: Open Problems and Current Bounds (part 1)](https://adamsheffer.wordpress.com/2013/05/04/distinct-distances-open-problems-and-current-bounds-1/) — Adam Sheffer, 2013-05-04; `author_page`, `informal_claim`, directness=`direct`, reliability=`medium`. 综述性地将本题记为 D_gen(n)，说明 EFPR 的一般位置构造给出 n·2^{O(√log n)} 上界，并称线性与超线性之间的问题未知。
- [Solution to a Problem of Erdős Concerning Distances and Points](https://arxiv.org/abs/2601.09102) — Benjamin Grayzel, 2026-01-14; `preprint`, `preprint`, directness=`indirect`, reliability=`medium`. 该预印本解决的是“每个四点子集至少产生三种距离”且 O(n/√log n) 距离的 #659；文中构造为截断的 Z×√2Z 格，故含三点共线，不能满足本题的一般位置条件。

### 完成标准

- 肯定出口: Prove that for every M>0 there is N(M) such that every n>=N(M) and every n-point P⊂R² with no three collinear and no four cocircular satisfies |D(P)|>=Mn. Equivalently, prove h(n)/n→+∞.
- 否定出口: Exhibit a constant C<∞ and an unbounded sequence n_j together with admissible n_j-point sets P_j⊂R² such that |D(P_j)|<=C n_j. This is exactly enough to show that h(n)/n does not tend to +∞.

不构成完成：

- A bound h(n)>=c n for one fixed constant c>0.
- A construction with n exp(O(sqrt(log n))) distances; it is compatible with the affirmative target.
- A construction that has collinear triples or cocircular quadruples, even if it has O(n) distances.
- A result for every four points determining at least three or five distances unless the proof also verifies the two general-position conditions.
- Finite-n optimisation or numerical evidence without a uniform asymptotic certificate.
- An argument proving only the ordinary, unrestricted distinct-distance theorem.

正确性陷阱：

- Check the construction against every collinear triple and every cocircular quadruple; generic-looking perturbations normally destroy distance equalities.
- Keep the minimax quantifier order straight: h(n) is a minimum over admissible P, whereas a counterexample needs admissible constructions for arbitrarily large n.
- For a negative result, O(n) must have one constant uniform along an unbounded sequence, not a constant depending on n.
- For a positive result, an improvement from c n to (c+o(1))n is still not enough.
- If using projection, prove both that the exceptional projection set is avoided and that the claimed upper bound on distinct distances survives projection.
- Do not transfer a theorem about no isosceles triangles, Φ(4,3), Φ(4,5), no parallelograms, convex position, or no-four-cocircularity alone without verifying logical implication to this exact hypothesis.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `18/100`
- 信心: `medium`
- 结论: 这是定义清楚、可严格核验但缺口极大的开放问题；适合长期、多路线的证明优先研究，不适合期待短期计算或局部技巧解决。

支持理由：

- 目标可明确表述为 ω(n) 下界或 O(n) 构造，正反完成条件互斥且可审计。
- 已有构造和线性计数提供了具体的可复核基线，便于对新引理做增量验证。
- 一般位置约束与距离重数之间的相互作用已被长期研究，仍没有已知的临界结构分类。

主要障碍：

- 需要跨越从固定常数倍 n 到任意无界倍数 n 的质变；现有 EFPR 构造仍允许 n 的无界次多项式倍数。
- 微小泛型扰动通常消灭大量相等距离，故“先造格点再扰动”不能自动给出反例。
- 局部禁构型的近期进展针对的条件与本题不等价，存在错误迁移结论的高风险。

Proof-first 路线：

- 寻找能将无三点共线、无四点共圆转化为“许多距离层不能同时高重数”的全局结构引理，并检验其是否能累计出 ω(n)。
- 反向分析 EFPR 的高维投影构造：定位其距离数损失的来源，并尝试在不破坏一般位置的前提下压缩至线性。
- 研究近线性距离集必然具有的加法/格结构，证明这种结构迫使共线三元组或共圆四元组出现。

需要验证：

- 对任何声称的 O(n) 构造，给出所有 n 的大小、一般位置和距离数的统一证明。
- 对任何超线性下界，核查量词为任意 admissible P 及任意增长阈值 M，而非固定常数。
- 在正式启动研究前，由人工再检索 MathSciNet/zbMATH、作者主页与引用链，以排除 2026 年尚未被网页索引的直接进展。

### 审计限制与人工复核理由

- 本审计进行了定向网页、arXiv、出版社、作者页和形式化仓库检索，但不能逻辑证明不存在尚未公开、未索引或 2026 年极近期的解答。
- EFPR 的精确 n exp(C√log n) 形式由当前题目页记录；出版社摘要直接确认较弱但一致的 o(n^(1+ε)) 结论。
- 未发现 P98 专属论坛讨论；页面导航中的 Forum 是站点级入口而非可核实的该题线程。
- 未检索受限订阅数据库的全文引文网络；任何启动研究前应由人工用 MathSciNet/zbMATH 和作者主页复核 2026 年更新。

- 开放状态依赖近期数据库记录与广泛但非穷尽的未发现检索，应由领域专家进行最终的文献更新核验。
- 需人工确认 EFPR 原文中定量常数/对数底数的准确规范化，尽管这不影响本题状态。
- 相邻的 2024–2026 禁四点模式结果很容易被误当作 P98 解答，正式后续研究应先复核其假设不等价性。

<!-- DEEP_REVIEW:END -->
