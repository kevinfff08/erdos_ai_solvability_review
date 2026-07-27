# Problem 100

## 基本信息

- 原始链接: https://www.erdosproblems.com/100
- LaTeX 页面: https://www.erdosproblems.com/latex/100
- 原始状态: `open`
- 奖金: `no`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $A$ be a set of $n$ points in $\mathbb{R}^2$ such that all pairwise distances are at least $1$ and if two distinct distances differ then they differ by at least $1$. Is the diameter of $A$ $\gg n$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `23/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：distances, geometry
- 题面含渐近/无限对象线索：\gg, sufficiently large
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: distances, geometry
- 有限/计算线索: 无
- 渐近/无限线索: \gg, sufficiently large
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选：GPT-5.5 级别模型配合计算、形式化与文献检索工具，较可能对该问题给出有价值的推进或验证框架，但直接证明直径 \(\gg n\) 的成功概率不高。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 最现实路线是围绕已有 \(\gg n/\log n\) 下界寻找能利用“不同距离至少相差 1”这一额外离散性假设的加强版距离计数或能量估计；并行使用计算搜索构造小规模极端配置、验证猜测的结构约束，再把可疑引理形式化或用半代数/优化工具做有限情形排除。若能把 Guth-Katz 型对数损失替换为由距离间隔和点间隔共同给出的 packing 或 incidence 改进，就可能接近目标。

### 支持理由

- 问题表述短、条件清晰，且已 formalized，有利于模型把任务拆成可检验的引理、有限情形和形式化验证目标。
- 已知下界 \(\gg n/\log n\) 与目标 \(\gg n\) 只差一个对数因子，说明现有方法已经接近目标；额外的距离间隔条件可能提供可利用的刚性。
- 几何距离、packing、incidence、能量估计和小规模构型搜索都适合工具辅助：模型可生成候选不等式，计算检查反例，并用形式化系统验证局部推导。
- 已有小规模反例现象说明简单的 \(n-1\) 直径猜想不能从非常小的样本直接判断，这使计算搜索对理解障碍有实际价值。

### 主要障碍

- 核心难点很可能是去除 Guth-Katz 型距离下界中的对数损失；这通常需要新的全局几何组合论想法，而非单纯整理现有技术。
- 距离值相隔至少 1 的条件虽强，但它作用在距离集合上，不直接给出点集结构分类；从数值间隔推出平面构型刚性可能很困难。
- 小规模计算搜索难以外推到任意 \(n\)，并且连续几何变量会导致非凸优化和伪反例问题。
- 形式化证明可验证推导，但不能自动发现关键 incidence/packing 引理；形式化成本可能很高。

### 需要的验证

- 系统检索并复核 Kanold 下界、Piepmeyer 例子以及 Guth-Katz 推出 \(\gg n/\log n\) 的具体推导，确认常数、假设和可加强环节。
- 对候选加强引理进行反例搜索：随机优化、SAT/SMT 或非线性约束求解，尤其检查直径接近 \(n/\log n\) 或低于线性的构型是否可行。
- 若提出新的 incidence 或 packing 引理，需要独立数学审稿，并最好在 Lean/Isabelle 等系统中形式化关键有限组合步骤。
- 构建小规模最优直径数据库，确认模型提出的结构猜想不被 \(n\leq 9\) 或更大计算样本否定。

### 公开版思考摘要

这个问题的 AI 可攻性来自两个方面：一是条件非常明确且已形式化，二是已知结果距离目标只差对数因子，说明可尝试在现有距离问题技术上寻找针对“距离间隔”的增强。但这也正是主要风险：去除对数因子往往代表真正的新数学突破。GPT-5.5 更可信的贡献是发现可验证的中间引理、排除一批潜在构型、改进常数或建立更强的条件性下界；直接完全解决应视为中等偏低概率。

### 免责声明

以上是对 GPT-5.5 级别模型辅助研究可行性的审查，不是该 Erdős 问题的解答，也不声称证明了直径 \(\gg n\)。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_100.md](../../prompts/problem_100.md)

### 状态结论

截至 2026-07-27，未发现 Problem 100 的平面线性下界已有证明或反例。Erdős Problems 当前页仍标为 OPEN，论坛无任何解答声明；形式化文件也把主命题标为 research open，且主命题与已知下界均保留 sorry。2026 年 Ho 的高维反例针对不同的、随维数增长的命题，不能解决本平面问题。由于 Kanold 与 Piepmeyer 的原始论证未能直接取得并逐页核验，且网页本身声明其状态并非完备文献保证，采用 likely_open（中等置信）而非更强结论。

### 当前规范陈述

令有限点集 A⊂R² 的距离值集合为 D(A)={||x−y||:x,y∈A，x≠y}，直径为 diam(A)=max D(A)。称 A 可容许，若：(i) 任意不同 x,y∈A 均有 ||x−y||≥1；(ii) 对任意不同的距离值 a,b∈D(A)，有 |a−b|≥1。目标是存在与 n、A 无关的绝对常数 c>0、n0，使得对所有 n≥n0 及所有 |A|=n 的可容许平面点集，diam(A)≥cn；等价地，最小可能直径为 Ω(n)。

```text
For a finite set A⊂R², let D(A)={||x−y||: x,y∈A, x≠y} and diam(A)=max D(A). Call A admissible if (i) ||x−y||≥1 for all distinct x,y∈A, and (ii) for all distinct a,b∈D(A), |a−b|≥1. The target is: there exist absolute constants c>0 and n0∈N such that, for every integer n≥n0 and every admissible A⊂R² with |A|=n, diam(A)≥cn. Equivalently, the minimum possible diameter over admissible n-point planar sets is Ω(n) as n→∞.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未找到可使 diam(A)/|A|→0 的简单构造或已验证反例。记录中的 9 点、直径 <5 例子只否定了“对所有 n 都有 diam≥n−1”的未经限定版本，不能否定“充分大 n”的强猜想，更不能否定 Ω(n) 主目标。
- 版本变化: Brass（1996）将更强的历史猜想表述为：在其较宽的“不同正距离相差至少 1”框架下，充分大 n 时最小直径应为 n−1；他只在平行半条带中的点集证明了渐近版本。数据库把 n−1 仅列为“Perhaps”的强变体，主目标仍为 Ω(n)。Ho（2026）否定的是维数随 n 增长时、所有点对距离彼此不同且间隔至少 1 的二次尺度高维猜想；这不是本二维命题的修订或反例。

陈述问题：

- 原文的“两个不同距离”应理解为两个不同的距离数值，而非两对不同点；相同距离可以由许多点对重复实现。
- 符号“≫n”未显式写出量词；审计中将其固定为存在绝对 c>0、对所有充分大 n 及所有可容许 A 的 Ω(n) 下界。
- “所有 pairwise distances 至少为 1”须限定为不同点对；否则零距离会干扰通常表述。
- Formal Conjectures 的定义允许端点相同，但因此会将零距离与任何正距离比较，从而隐含所有不同点距离至少为 1；其主命题以严格 >Cn 写出，和上述 Ω(n) 版本仅差常数调整。

需要固定的量词/约定：

- The constants c and n0 must be independent of both n and A.
- Condition (ii) quantifies over distinct values in D(A), not over distinct unordered pairs of points; multiplicities are unrestricted.
- The asymptotic assertion ranges over every sufficiently large integer n and every admissible n-point set, not merely an infinite subsequence.
- diam(A) is the ordinary Euclidean maximum distance and no post hoc rescaling is permitted after imposing unit separation.

### 文献与当前边界

已核验的主要结果：

- Kanold（1981）的 n^(3/4) 下界由数据库记录，但本审计只核对到论文书目信息，未能检查原文；它已被下述 Ω(n/log n) 渐近下界严格改进。
- Guth–Katz（2015，同行评审）证明 n 个平面点有 Ω(n/log n) 个不同距离。对本题，将不同距离依序写为 d1<⋯<dm；d1≥1 且相邻差至少 1，故 diam(A)=dm≥m=Ω(n/log n)。这是透明推论，而非 Guth–Katz 原文直接研究本题。
- Brass（1996，同行评审）研究同类平面最小直径函数，记载强猜想 δ(n)=n−1，并在点集位于平行半条带这一受限几何类别中证明该强猜想的渐近版本。
- Harborth–Piepmeyer（1991）是与数据库所述 9 点整数距离构造关联的可核对书目来源；具体“9 点且直径 <5”尚未由可访问原文或坐标证书独立复核。

最近相关工作：Ho（2026，arXiv:2604.15305）是最近直接涉及“距离值间隔约束与直径”的工作：它给出维数随 n 增长的高维反例，并附带 Lean 工件。该论文将 Brass 的平面工作视为最接近的先前结果，不能推出二维主目标的正面或负面结论。

剩余核心：证明或反驳：在固定维数 2 中，任意 n 点可容许集的直径是否必须为 Ω(n)。已知 Ω(n/log n) 与所求线性下界之间仍差一个对数因子；更强的“充分大 n 时直径至少 n−1”也未被该审计验证为已解。

已使用方法：

- Elekes–Sharir 框架、三维直线关联、分割多项式与代数曲面方法（Guth–Katz）用于控制不同距离数。
- 对距离值排序后，用相邻间隔至少 1 将“不同距离数”转换为直径下界。
- Brass 的受限位置（平行半条带）几何分析。
- 高维相关工作使用 Singer 差集、循环距离轮廓、Fourier 型构造及缩放；这些技术目前没有给出二维反例。

争议或不确定性：

- Erdős Problems 明确说明其 OPEN 标签只是维护者信念，可能遗漏文献。
- Kanold 的原始定理文本及其是否恰与当前假设完全一致未被本次直接检查。
- Piepmeyer 的 9 点主张未取得显式坐标、原论文论证或可编译的独立形式化证书；它不影响 Ω(n) 的当前状态判定。
- Formal Conjectures 主文件包含 sorry；数据库的“formalized=yes”不应被误读为主命题已有形式化证明。

### 证据来源

- [Erdős Problem #100](https://www.erdosproblems.com/100) — Thomas F. Bloom / Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 当前条目明确标记 OPEN，给出本题陈述、Kanold 的 n^(3/4) 记录、Piepmeyer 的 9 点记录，以及由 Guth–Katz 推出 Ω(n/log n) 的说明；页面同时警告其开放状态只是站点维护者的判断。
- [Erdős Problem #100 — LaTeX source](https://www.erdosproblems.com/latex/100) — Thomas F. Bloom / Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 直接核对输入中的题面、备注和唯一列出的 Guth–Katz 参考文献，未发现后续修订文字。
- [Erdős Problem #100 Discussion Thread](https://www.erdosproblems.com/forum/thread/100) — Erdős Problems forum, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 论坛显示 OPEN、0 条评论，并明确写明没有任何部分或完整解答声明；这只支持“未见论坛解答”，不构成开放性的证明。
- [On the Erdős distinct distances problem in the plane](https://annals.math.princeton.edu/2015/181-1/p02) — Larry Guth; Nets Hawk Katz, 2015-01-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明任意 N 个平面点确定至少 cN/log N 个不同距离。结合本题距离值彼此至少相隔 1，排序后最大距离至少等于不同距离数，故给出 diam(A)=Ω(n/log n)。
- [On the Erdős-diameter of sets](https://www.sciencedirect.com/science/article/pii/0012365X9500208E) — Peter Brass, 1996-04-06; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 摘要定义平面 Erdős-diameter，记载 Erdős 的充分大 n 时 δ(n)=n−1 猜想，并称只在位于平行半条带的点集情形证明其渐近版本。
- [Points Sets with Small Integral Distances](https://dblp.org/rec/conf/dimacs/HarborthP90) — Heiko Harborth; Lothar Piepmeyer, 1991; `primary_paper`, `unknown`, directness=`indirect`, reliability=`medium`. 核对到 Piepmeyer 与 Harborth 的相关 DIMACS 论文书目信息；本次无法直接取得全文来独立确认数据库所述特定 9 点、直径 <5 构造。
- [Applied Geometry and Discrete Mathematics, DIMACS Series Volume 4](https://archive.dimacs.rutgers.edu/Volumes/Vol04.html) — DIMACS, 1991; `secondary_index`, `database_record`, directness=`indirect`, reliability=`medium`. 确认 Harborth–Piepmeyer 论文位于该卷第 319 页起。
- [Hans-Joachim Kanold author profile](https://zbmath.org/authors/?q=Kanold+H%2A) — zbMATH Open, date unknown; `secondary_index`, `database_record`, directness=`indirect`, reliability=`medium`. 确认 Kanold 的 1981 年论文《Über Punktmengen im k-dimensionalen euklidischen Raum》存在；未能取得其原文以独立核验 n^(3/4) 命题和精确假设。
- [FormalConjectures — Erdős Problem 100](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/100.lean) — Formal Conjectures Authors, 2026; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 给出与主目标、n−1 强变体、Kanold/Guth–Katz 下界和 Piepmeyer 有限构造对应的 Lean 陈述；但主文件中这些定理体均含 sorry，故它是精确陈述工件而非已机器验证的证明。
- [Erdős's diameter conjecture for separated distances fails in high dimensions](https://arxiv.org/abs/2604.15305) — Boon Suan Ho, 2026-04-16; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 构造维数约 n² 的高维反例，否定维数无关的二次下界；论文明确将 Brass 1996 识别为最接近的平面 Erdős-diameter 工作。该结果不适用于固定二维的 Problem 100。
- [DiameterConstruction Lean formalization](https://github.com/boonsuan/erdos670) — Boon Suan Ho, 2026; `formalization`, `formalized_artifact`, directness=`indirect`, reliability=`medium`. 项目 README 声称高维反例开发可 lake build、无 sorry，并说明其精确高维结论；此形式化只验证不同的高维问题，不是 Problem 100 的解答。

### 完成标准

- 肯定出口: Prove that there exist absolute constants c>0 and n0 such that every admissible A⊂R² with |A|=n≥n0 satisfies diam(A)≥cn.
- 否定出口: Construct admissible planar sets A_j with |A_j|=n_j→∞ and diam(A_j)/n_j→0; equivalently, for every c>0 and N there exist n≥N and an admissible n-point set A with diam(A)<cn.

不构成完成：

- Reproving or slightly improving the existing Ω(n/log n) bound without reaching Ω(n).
- Checking finitely many values of n, or presenting a numerical construction without an exact certification of every distance and every separation inequality.
- Finding one finite counterexample to diam(A)≥n−1, since that does not negate the eventual Ω(n) target.
- Proving the result only for collinear sets, half-strips, convex sets, or another restricted family without reducing arbitrary admissible sets to that family.

正确性陷阱：

- Do not replace the condition on distinct distance values by pairwise distinct distances: repeated lengths are allowed.
- Verify the minimum-distance condition and the unit gap between every two distinct realized values separately.
- Track uniformity: c and n0 cannot depend on the configuration, a subsequence, or an auxiliary geometric parameter.
- If using sorted distance values, justify that the largest value is diam(A) and that all gaps—not merely consecutive selected gaps—meet the stated threshold.
- A purported counterexample family must have n→∞ and sublinear diameter after the same normalization that establishes unit separation.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `24/100`
- 信心: `medium`
- 结论: 这是定义清楚、可独立验证但难度高的开放几何问题；适合以证明优先的多路线研究进行审查，不适合把有限搜索当作主要解法。

支持理由：

- 主目标有精确的全称量词、明确的正反完成条件和成熟的 Ω(n/log n) 基线。
- Guth–Katz 与 Brass 提供两条可检查的既有路线，且对数缺口被明确定位。
- 二维限制排除了 2026 高维构造对命题的直接终结作用，仍存在真正的数学剩余目标。

主要障碍：

- 从不同距离数的 Ω(n/log n) 提升到线性需要消除对数损失，现有一般关联几何结果并未做到。
- 允许距离重复，使“所有点对距离值都不同”的较强模型的技术或反例不能直接转移。
- 有关 Kanold、Piepmeyer 的原始细节尚未完全取得，可能隐藏更精确的历史限制或构造。

Proof-first 路线：

- 寻找可容许条件所强加的额外结构，以将一般不同距离定理中的对数损失排除；任何此类结构引理须先独立、定量地表述。
- 分析短直径情形中距离谱、重复距离图与平面几何约束是否强制出现间隔违反或给出线性尺度增长。
- 把 Brass 的半条带定理视为受限模型，寻求可证明的结构性归约，而不是假设任意点集可归约。
- 可选的唯一计算任务只能是精确代数/区间证书搜索某个明述结构引理的最小反例，预先固定停止条件；它不能替代渐近证明。

需要验证：

- 取得并审读 Kanold 1981 原文，核对 n^(3/4) 的定量形式、维数与最小距离假设。
- 取得 Harborth–Piepmeyer 原文或坐标证书，独立核验 9 点例子的精确条件。
- 在开展研究前再次检索 2026-07-27 后的 arXiv、作者主页和期刊数据库，以排除刚出现的平面结果。
- 若将任何 Lean 工件作为证据，实际运行其锁定版本的构建并检查目标定理是否无 sorry。

### 审计限制与人工复核理由

- 本审计遵守“仅使用给定问题 JSON 作为仓库输入”，未读取其他仓库条目；网络检索不能逻辑证明全世界不存在未索引的新论文。
- ScienceDirect 的 Brass 页面可核对摘要与书目信息，但本次抓取被 403 限制，未逐页审读全文。
- Kanold 1981 与 Harborth–Piepmeyer 1991 的原始正文未成功取得；相关历史结论因此被清楚降级为数据库/书目支持，而非已独立复核的定理。
- Formal Conjectures 的主文件已直接检查到 sorry；链接的 Piepmeyer 分支未能完整展开为可审查的无 sorry 证明，不能作为已验证证书。
- Ho 2026 仍是预印本；其高维结论附有作者维护的 Lean 项目，但该项目的实际构建未在本审计中运行，且无论如何不对应二维 Problem 100。

- 建议人工取得 Kanold（1981）原文，以确认 n^(3/4) 下界的精确量词和假设。
- 建议人工取得 Harborth–Piepmeyer（1991）全文或精确坐标，验证 9 点例子及其是否完全符合主题的单位间隔规范化。
- 如需把形式化状态列为实质证据，应在锁定版本上运行 Lean 构建，而非仅依据 README 或带 sorry 的主文件。
- 在委派长期研究前应做一次新的当日 arXiv、MathSciNet/zbMATH 和作者主页检索，因为该主题在 2026 已出现相邻高维工作。

<!-- DEEP_REVIEW:END -->
