# Problem 89

## 基本信息

- 原始链接: https://www.erdosproblems.com/89
- LaTeX 页面: https://www.erdosproblems.com/latex/89
- 原始状态: `open`
- 奖金: `$500`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`
- 形式化状态: `yes`
- OEIS: `A186704`, `A131628`
- 原站备注字段: Erdős distance problem

## 原问题

Does every set of $n$ distinct points in $\mathbb{R}^2$ determine $\gg n/\sqrt{\log n}$ many distinct distances?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `28/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：distances, geometry
- 题面含渐近/无限对象线索：\gg
- 原记录含奖金 $500，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: distances, geometry
- 有限/计算线索: 无
- 渐近/无限线索: \gg
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 + 计算实验 + 形式化证明 + 文献检索 + 反例/构型搜索工具`
- 结论: **低到中等候选。该问题有清晰的形式化对象、已知接近结果和可计算的极值构型，因此 GPT-5.5 级别模型很可能能复现、形式化、验证和组织现有路线，并可能在局部引理、特殊情形或常数/条件版本上推进；但完成完整的 n/sqrt(log n) 下界大概率需要新的 incidence geometry 或组合几何突破，不能预期由当前模型直接解决。**
- 等级: `low_to_medium_candidate`
- 分数: `34/100`
- 信心: `high`
- 可能路线: 最现实路线不是直接证明完整猜想，而是把 Guth-Katz 型框架、距离四元组计数、圆/线关联结构和格点极端例子形式化成可检查模块；用计算搜索测试潜在反例和特殊构型；尝试寻找能把已知 n/log n 改进到更强对数因子的额外结构性命题。若有推进，可能来自证明某类高重合距离图或近格点构型必须满足更强约束，而不是纯数值实验。

### 支持理由

- 问题陈述短、对象明确，且已 formalized=yes，适合把定义、计数恒等式、已有定理依赖和证明义务拆成形式化子目标。
- 已知结果距离目标只差 sqrt(log n) 因子，说明已有技术框架非常接近；模型可在该框架内系统检查瓶颈和尝试局部强化。
- 整数格给出最优阶的障碍构型，便于计算实验和自动化验证候选命题是否被格点或近格点例子击穿。
- 工具增强模型可做文献梳理、证明依赖图、有限构型搜索、符号推导和 Lean/Isabelle 风格验证，这些都能显著提高审查和局部推进效率。

### 主要障碍

- 完整结论是著名 Erdős distinct distances conjecture 的最优对数级版本，核心难点不是计算规模，而是缺少能跨越剩余 sqrt(log n) 因子的结构性思想。
- 现有 n/log n 级结果依赖深的 incidence geometry 和代数几何工具；模型若只是重组已知证明，很难自动产生关键新引理。
- 有限点集搜索不能直接证明渐近下界，也很难排除连续平面中的复杂退化构型。
- 形式化已有证明本身工作量很大，且形式化完成不等于获得更强定理。

### 需要的验证

- 核对形式化库中已经覆盖哪些基础结果：欧氏距离、有限点集、关联定理、四元组计数、渐近记号。
- 复现已知 n/log n 证明的关键不等式链，确认模型没有把条件、例外集或常数依赖误用。
- 对任何候选强化引理，用整数格、扰动格、圆上点集、乘积型集合等构型做自动反例搜索。
- 若声称达到 n/sqrt(log n)，需要独立专家审稿与机器形式化双重验证，尤其检查对高重合距离、零距离排除、退化直线/圆族和渐近量词的处理。

### 公开版思考摘要

这个问题对 AI 的有利点是结构极清楚、已有接近结果、极端例子明确且可形式化；不利点是剩余差距代表真实的理论瓶颈。GPT-5.5 配合工具更可能成为强力证明工程和猜想筛选助手，而不是直接给出完整突破。合理预期是验证现有理论、发现错误候选命题、整理可能的强化方向，或证明受限版本。

### 免责声明

以上是 AI 可推进性评估，不是该 Erdős 问题的解答，也不声称已经证明或反驳该猜想。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_89.md](../../prompts/problem_89.md)

### 状态结论

截至审计日，原命题仍属公开的 Erdős 不同距离猜想：问题页（2026-01 编辑）和 2026 年同行评议论文都将其描述为未解，并把 Guth–Katz 的 Ω(n/log n) 作为最佳通用下界。发现的 Yazici 2020 arXiv 预印本声称证明该猜想，但没有找到可核验的同行评议发表或独立证明核查；后续权威资料仍明确称猜想未解，因此该预印本不足以改变状态。

### 当前规范陈述

存在绝对常数 c>0 和 n0，使得对每个整数 n≥n0 及每个满足 |A|=n 的有限点集 A⊂R²，非零欧氏距离集合 Δ(A)={||x-y||₂:x,y∈A,x≠y} 满足 |Δ(A)|≥c n/√(log n)。取自然对数；换底只改变常数 c。常数不得依赖于 n 或 A。

```text
There exist absolute constants c>0 and n0 such that, for every integer n>=n0 and every finite set A⊂R² with |A|=n, the nonzero Euclidean distance set Δ(A):={||x-y||₂ : x,y∈A, x≠y} satisfies |Δ(A)|≥c n/sqrt(log n). Here log may be the natural logarithm (a change of base only changes c), and the constants are independent of n and A.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未找到能否定规范化命题的简单构造。相反，平方整数格给出 |Δ(A)|=O(n/√log n) 的匹配量级上界，说明目标若成立即为量级最优；它不是反例。
- 版本变化: 未发现原全局命题被后文改写为非等价版本。Guth–Katz（2015）将通用下界提升至 Ω(n/log n)，但未达到猜想的 √log 因子。题注所列单点、很多点及平均 pinned-distance 猜想均为更强的独立目标。2025 年起的 Formal Conjectures 文件把原命题编码为一个含 `sorry` 的开放定理，未构成证明或状态修订。

陈述问题：

- 原文的“\gg”未明说常数和“充分大 n”的量词；若按逐个 n 或允许常数依赖于点集理解，命题会失去标准渐近含义。
- 原文未定义“distinct distances”；规范化为无序不同的正欧氏距离值，而不是距离对的数目、平方距离的重数或包含零距离的集合。
- 题注中的 pinned/average stronger forms 是不同命题；它们既不修正也不替代本题的全局距离集下界。
- 数据库的“formalized=yes”不能理解为已形式化证明：可检查的 Lean 文件中主定理和 Guth–Katz 变体均以 `by sorry` 占位。

需要固定的量词/约定：

- Interpret \gg as: there are universal c>0 and n0 such that the inequality holds for every n>=n0 and every n-point set A.
- Count the cardinality of the set of positive Euclidean distance values, not the number of pairs realizing them.
- The assertion is asymptotic; n=1 and the singularity of log n are outside the intended range.
- The square-grid construction supplies an upper bound on the extremal minimum; it does not establish the universal lower bound.

### 文献与当前边界

已核验的主要结果：

- Erdős（1946，同行评议）提出该问题；平方整数格给出 O(n/√log n) 的构造性上界，故所求下界若成立即为量级最优。
- Guth–Katz（2015，Annals of Mathematics，同行评议）证明所有 n 点集都有 Ω(n/log n) 个不同距离。这是对本题直接适用且经本审计核验的最强通用定理。
- Guth–Katz 之前的渐进下界改进包括 Moser、Chung–Szemerédi–Trotter、Solymosi–Tóth、Tardos、Katz–Tardos；这些是历史背景，不应误报为当前最强结果。
- Yazici（2020，arXiv v3）声称达到猜想界，但没有找到同行评议发表、可检查的独立验证或纠错记录；鉴于 2026 资料继续明确称该猜想未解，当前只能把它列为未验证的声称，不能列为结果。

最近相关工作：Pach、Raz、Solymosi（SoCG 2026，同行评议）的导言明确重申全局不同距离问题的已知 Ω(n/log n) 与仍缺的 √log n 因子。其新结果针对单位距离/刚性而非证明本题，但它是截至审计日关于该经典问题状态的近期同行评议佐证。

剩余核心：证明存在绝对 c>0，使任意 n 点平面集的不同正欧氏距离数至少 c n/√log n；等价地，消除 Guth–Katz 下界相对于格点量级所剩的 √log n 损失。

已使用方法：

- Elekes–Sharir 框架：把等距离四元组/部分刚体运动转化为 R³ 中一族直线的关联问题，再以 Cauchy–Schwarz 从能量界导出距离集下界。
- Guth–Katz 的 polynomial partitioning、低度代数曲面、flecnode/ruled-surface 几何和 rich-point 关联界。
- 格点端依赖平方和表示数的数论估计；它解释上界构造的量级，但不提供任意点集的下界。

争议或不确定性：

- Yazici 2020 arXiv 声称解决问题，但本审计无法逐行审查其证明或找到专家判定其错误的文献；它与后续同行评议文献及数据库的开放叙述冲突，故必须在任何研究启动时作为单独的证明审计对象。
- 公开检索不能逻辑排除未索引的新稿、私人通讯或未来勘误；“confirmed_open”是基于截至审计日可访问、彼此一致的高质量来源，而非全称的文献完备性证明。

### 证据来源

- [Erdős Problems — Problem 89](https://www.erdosproblems.com/89) — Thomas F. Bloom / Erdős Problems contributors, 2026-01-23; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前数据库将第 89 题标为 OPEN，给出原命题、平方格最优性说明及 Guth–Katz 的 Ω(n/log n) 结果；页面本身也提醒该状态只是维护者判断，须独立检索。
- [89 Discussion Thread | Erdős Problems](https://www.erdosproblems.com/forum/thread/89) — Thomas F. Bloom / Erdős Problems contributors, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 论坛线程显示 0 条评论、没有完整或部分解答声称，并重述维护者的开放状态免责声明；该页面因 403 无法全文直接打开，使用搜索索引内容。
- [On Sets of Distances of n Points](https://users.renyi.hu/~p_erdos/1946-03.pdf) — Paul Erdős, 1946-05; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原始论文：提出平面不同距离问题，并给出格点构造所对应的 O(n/√log n) 上界背景。
- [On the Erdős distinct distances problem in the plane](https://annals.math.princeton.edu/2015/181-1/p02) — Larry Guth; Nets Hawk Katz, 2015-01-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明任意 N 个平面点确定至少 cN/log N 个不同距离；摘要说明所用 Elekes–Sharir 刚体运动归约、三维点线关联、polynomial partitioning 和 ruled surfaces。
- [On the Erdos distinct distance problem in the plane](https://arxiv.org/abs/1011.4105) — Larry Guth; Nets Hawk Katz, 2010-11-17; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 可访问的预印本正文明确陈述 Erdős 猜想、\gg 的常数约定、主定理 Ω(N/log N)，并解释距离四元组到三维直线关联的归约。
- [Erdős’s Unit Distance Problem and Rigidity](https://drops.dagstuhl.de/storage/00lipics/lipics-vol367-socg2026/html/LIPIcs.SoCG.2026.83/LIPIcs.SoCG.2026.83.html) — János Pach; Orit E. Raz; József Solymosi, 2026; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 该 2026 年论文的导言将“最少不同距离”与单位距离问题区分开，并明确说 Guth–Katz 得到 cn/log n，这与平方格所达到的猜想最小量级相差 √log n；因此提供近期同行评议的开放状态佐证。
- [FormalConjectures/ErdosProblems/89.lean](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/89.lean) — Formal Conjectures Authors, date unknown; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 主猜想被编码为 Big-O 形式，但证明为 `by sorry`；标为 solved 的 Guth–Katz 和格点变体也含 `sorry`。因此它只形式化了陈述，不能作为定理的机器核验。
- [Erdős Distance Problem in R^d](https://arxiv.org/abs/2002.01248) — Esen Aksoy Yazici, 2020-02-04; `preprint`, `preprint`, directness=`direct`, reliability=`low`. 该单作者 arXiv 预印本声称证明平面 Ω(n/√log n) 及高维版本；检索未发现同行评议版本、独立验证或得到后续文献接受，且 2026 年来源仍称猜想开放。
- [A186704 — The minimum number of distinct distances determined by n points in the Euclidean plane](https://oeis.org/A186704) — OEIS Foundation / Michael Somos, date unknown; `oeis`, `database_record`, directness=`indirect`, reliability=`medium`. 给出极值函数定义，并在 2026-07 更新的注释中并列记录格点 O(n/√log n) 与 Guth–Katz Ω(n/log n) 界。

### 完成标准

- 肯定出口: Produce a complete proof of universal constants c>0 and n0 such that every finite A⊂R² with |A|=n>=n0 has |Δ(A)|>=c n/sqrt(log n), with every reduction and asymptotic constant independent of A and n.
- 否定出口: Produce a rigorous infinite counterexample family A_j⊂R² with n_j=|A_j|→∞ and |Δ(A_j)|/(n_j/sqrt(log n_j))→0; equivalently, refute every proposed universal c,n0 by arbitrarily large examples.

不构成完成：

- Reproving or slightly rephrasing the Guth–Katz Ω(n/log n) bound.
- Showing the desired bound only for grids, Cartesian products, convex sets, general-position sets, random sets, or another restricted class.
- Giving a construction with O(n/sqrt(log n)) distances: that is consistent with, and motivates, the conjecture.
- Checking finitely many n or relying on numerical optimization without a uniform lemma and a proof of its hypotheses.
- Treating a Lean declaration containing `sorry`, or an unreviewed preprint assertion, as a verified proof.

正确性陷阱：

- Keep the direction of the distance-energy/Cauchy–Schwarz inequality correct: an upper bound on equal-distance quadruples is needed to force many distance values.
- Audit all hidden constants and thresholds through polynomial-partitioning, induction, and dyadic summation; none may depend on the point set.
- Do not count ordered pairs or multiplicities in place of |Δ(A)|, and exclude x=y consistently.
- A result expressed with n^{1-o(1)} or with an unspecified nonuniform constant does not imply the exact n/sqrt(log n) lower bound.
- If relying on a claimed 2020 resolution, identify the exact theorem, verify every cited input and all dimension/range hypotheses, and obtain an independent adversarial proof check.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `8/100`
- 信心: `high`
- 结论: 这是定义清楚、可被严格审计但难度极高的开放问题；对自主 AI 而言是低概率候选，不应因其表述简短或可做有限搜索而提高评分。

支持理由：

- 目标是单一、精确的渐近不等式，正反两种完成条件都可检验，且有成熟的主线文献与明确的 √log 缺口。
- Guth–Katz 的归约把成功所需的改进定位在可陈述的关联/能量控制问题，便于逐引理审计。
- 存在一个必须首先处理的具体风险项：Yazici 2020 的未验证声称可被独立逐步核查。

主要障碍：

- 该猜想在 1946 年提出，Guth–Katz 后十余年仍无通用改进；剩余因子很小却可能要求本质新的结构定理，而不是常数优化。
- 现有方法的对数损失来自多重尺度/富关联控制；局部或特殊构型估计通常不能推广到任意点集。
- 连续实坐标和渐近量词使有限计算无法认证核心结论；形式化文件也尚未提供可复用的完成证明。

Proof-first 路线：

- 先进行文献与证明审计：逐项核验 Yazici 2020 的主引理、引用定理的适用范围和可能失效处；若成立才改变主任务状态。
- 以 Guth–Katz 的距离四元组框架为基线，寻找能将总能量的对数损失压缩到 √log 的严格新引理，并先证明该引理确实蕴含目标。
- 研究近极值点集的结构性替代：将“距离数少”转化为可分类的高对称/高关联结构；任何候选结构结论须同时覆盖格点型退化情形。

需要验证：

- 对 Yazici 2020 预印本进行独立专家级逐行核查，或找到其作者、期刊、MathSciNet/zbMATH 或后续论文对该稿的处理。
- 在研究开始和提交前再次检索 2026-07-27 之后的 arXiv、作者主页与期刊记录。
- 任何新证明均需由未参与主路线的审稿代理复算所有渐近量词、能量不等式方向及退化几何情形。

### 审计限制与人工复核理由

- 数据库与论坛对开放状态的声明本身不是证明；其价值在于当前记录和未出现评论声称，状态结论还依赖 2026 年同行评议文献的独立一致叙述。
- Yazici 2020 预印本的全文数学正确性未在本审计中逐行验证，也未找到公开的错误定位或同行评议采纳记录；这正是需要人工专家复核的具体项目。
- 检索覆盖了精确命题、题号、论坛、原始论文、Guth–Katz、2023–2026 arXiv 定向查询及形式化仓库，但不能保证发现所有未索引、付费墙后或未公开的材料。
- 当前状态只审计题 89 的全局平面命题；没有把题注中的 pinned/average 变体或高维问题当作该题的解答。

- 应由离散几何专家独立审查 Yazici 2020 的声称，或确认其在学术记录中的处理；在此之前不能把它排除为已知错误，也不能把它视为解答。
- 任何真正的新证明都需对 Guth–Katz 关联几何、渐近量词和退化构型进行专家级逐引理审计。

<!-- DEEP_REVIEW:END -->
