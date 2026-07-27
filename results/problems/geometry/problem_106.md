# Problem 106

## 基本信息

- 原始链接: https://www.erdosproblems.com/106
- LaTeX 页面: https://www.erdosproblems.com/latex/106
- 原始状态: `falsifiable`
- 奖金: `no`
- 主类别: `geometry`
- 原始标签: `geometry`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Draw $n$ squares inside the unit square with no common interior point. Let $f(n)$ be the maximum possible sum of the side-lengths of the squares. Is $f(k^2+1)=k$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `54/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- 目前只能依靠通用数学推理、文献归纳和特殊情形探索

### 主要障碍

- 所属标签偏证明密集：geometry
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: geometry
- 有限/计算线索: 无
- 渐近/无限线索: 无
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。这个问题不适合期待模型直接给出完整通用证明，但很适合用 AI+计算几何工具做系统性推进：小 k 的严格验证、旋转方形反例搜索、轴平行结果向一般方向的障碍定位，以及把候选极值配置转成可形式化的不等式证明。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 最可行路线是把问题转成有限维几何优化与证明验证任务：对固定 k，参数化每个小正方形的中心、边长和旋转角，加入位于单位正方形内与两两内点不交的约束，使用全局优化、分支定界、区间算术、CAD/SMT 或 Lean/Isabelle 辅助证明来搜索是否存在总边长超过 k 的配置。若没有反例，再尝试从 Baek-Koizumi-Ueoro 的轴平行证明中抽取可迁移的面积、投影、切片或拓扑不等式，并专门分析旋转带来的松弛空间。

### 支持理由

- 问题是明确的有限维几何极值问题，固定 k 时可被参数化并交给非线性优化、区间验证和反例搜索工具处理。
- status 为 falsifiable，若猜想为假，AI 较可能通过数值优化或启发式布局搜索找到总边长大于 k 的旋转方形配置，然后再做严格认证。
- 备注中已有强结构线索：f(k^2)=k 的 Cauchy-Schwarz 上界、k^2+1 的自然下界、Praton 的等价性结果、轴平行版本 g(k^2+1)=k 的完整解决。这些能给模型提供可复用的证明骨架和反例搜索边界。
- 轴平行版本已被证明，说明该问题的一个重要受限形式可完全解决；AI 可以比较一般旋转情形中哪些步骤失效，从而产生有价值的中间引理或条件化定理。
- 对小 k 的计算验证很有希望，尤其是 k=1,2 已有结果线索，进一步 k 的严格数值证书可能构成实质推进。

### 主要障碍

- 通用情形允许任意旋转，非重叠约束含有三角函数和多项式不等式，导致全局优化和形式化证明复杂度迅速上升。
- 要证明所有 k 的上界 f(k^2+1)<=k，需要统一结构性论证；单纯的数值搜索只能排除有限多个 k。
- 轴平行证明未必能直接推广，因为旋转方形的投影、切片长度、接触图和面积分解都会失去简单网格结构。
- 若最优或近最优配置包含大量退化接触、非常小的间隙或连续族，计算证书会很难稳定。
- 问题历史较长且已有专业研究推进，说明朴素面积法、Cauchy-Schwarz 或局部扰动方法大概率不足以完成通用证明。

### 需要的验证

- 首先明确“no common interior point”应形式化为任意两正方形内部不相交，并确认边界接触是否允许。
- 为固定 k 建立可复现的全局优化模型，输出候选反例或上界证书，并用区间算术验证约束。
- 对小 k 逐一生成机器可检查证书，避免只依赖浮点优化结果。
- 审查轴平行版本 g 的证明，标记每个使用轴平行性的步骤，测试是否能被旋转不变的不等式替代。
- 如果提出通用上界证明，需要形式化关键几何引理，特别是关于投影、覆盖、接触图或切片积分的部分。

### 公开版思考摘要

该问题的 AI 可解性主要来自两个方面：一是固定 k 后可以建模为可搜索、可认证的几何优化问题；二是已有轴平行版本和等价性结果提供了强约束和证明模板。主要风险是任意旋转使结构性上界非常困难，因此完整解决概率不能评为高。但 GPT-5.5 配合全局优化、区间证明和形式化工具，很可能在小规模验证、反例搜索或推广轴平行证明的失败点分析上取得显著推进。

### 免责声明

以上是对 AI 辅助研究可行性的审查，不是该 Erdős 问题的证明、反例或完整解答。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `not_required`
- 独立研究 Prompt: [prompts/problem_106.md](../../prompts/problem_106.md)

### 状态结论

截至 2026-07-27，原命题可重建为一个明确的、允许任意旋转小正方形的几何极值猜想；未发现已核验的证明或反例。2026 年的 Singh 预印本仍明确称其“remains open”，而 2024 年 Baek–Koizumi–Ueoro 的定理只解决了所有小正方形与容器边平行的严格受限版本。故该问题是研究就绪的开放问题；“confirmed”仅表示有近期直接文献支持其仍开放，并非对全球文献不存在解答的逻辑证明。

### 当前规范陈述

对每个正整数 k，令 f(k^2+1) 为所有如下构型的边长和的上确界：在闭单位正方形 [0,1]^2 内放置恰好 k^2+1 个边长为正的欧氏正方形，它们的内部两两不相交。小正方形可任意旋转，并可彼此或与外边界相切。问题是证明或推翻对每个 k>=1 都有 f(k^2+1)=k。等价地，须证明任意此类装填的总边长至多为 k；下界由 k×k 网格中以两个边长 1/(2k) 的小正方形替换一个格子得到。

```text
For every positive integer k, let f(k^2+1) be the supremum, over all families (Q_1,...,Q_{k^2+1}) of k^2+1 Euclidean squares of positive side lengths contained in the closed unit square [0,1]^2 and having pairwise disjoint interiors, of the sum of their side lengths. The squares may have arbitrary orientations and may touch each other or the boundary. Prove or disprove f(k^2+1)=k for every k>=1. Equivalently, prove that every such packing has total side length at most k, since the k-by-k grid with one tile replaced by two squares of side 1/(2k) gives total k.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 已核对标准下界构造：把 k×k 网格中的一个边长 1/k 方格替换为两个边长 1/(2k) 方格，得到 k^2+1 个方格且边长和恰为 k。k=1 时 f(2)=1 是已知小例。没有发现能使任一 k 的总边长严格大于 k 的简单构造；这只是有针对性的检查，不是对所有构型的穷尽证明。
- 版本变化: 1984 年 Halász 给出相邻参数的下界。1995 年 Erdős–Soifer 与 2005 年 Campbell–Staton 提出更一般的精确公式 f(k^2+2c+1)=k+c/k（-k<c<k）；Praton 的工作表明该一般猜想与 c=0 的原猜想等价。2007 年 Staton–Tyler 引入轴平行变体；2024 年 Baek–Koizumi–Ueoro 证明该变体的完整公式，但未解除旋转限制。2026 年 Singh 证明原猜想等价于“对无穷多个 k 成立”，也等价于相应非负级数收敛；这是一种重表述，不是原猜想的解决。

陈述问题：

- 原句未显式量化 k；文献和历史猜想均表明应为“对所有正整数 k”。
- “inside”“no common interior point”和“maximum”未说明边界接触、旋转和极值是否取到。2024 年论文把平行边版本另记为 g，反向确认原 f 允许非平行取向；本审计以闭容器、内部不交、允许接触和上确界作稳健表述。
- “maximum”与“supremum”的技术差异不是已知反例来源；使用上确界避免尚未在此审计中单独证明的极值取到问题。若坚持历史术语 maximum，后续工作应补写紧致性/退化边长处理。
- 原问题附带的“for which n is f(n+1)=f(n)”是不同的广泛问题，不能误当作本题的完成条件。

需要固定的量词/约定：

- k ranges over all positive integers.
- The packing contains exactly k^2+1 squares, each of strictly positive side length.
- Each square is a Euclidean square contained in [0,1]^2; arbitrary orientation is permitted.
- Only interiors must be pairwise disjoint. Boundary contacts, including contacts with the unit-square boundary, are permitted.
- The target is an exact equality for every k, not an asymptotic estimate and not merely an upper or lower bound.

### 文献与当前边界

已核验的主要结果：

- 精确基线：由面积不等式 sum s_i^2<=1 和 Cauchy–Schwarz，f(k^2)<=k；k×k 网格达等，故 f(k^2)=k。该论证不能给出 k^2+1 的上界。
- 标准构造给出 f(k^2+1)>=k。Halász（1984，同行评审）还给出邻近参数的构造下界；其论文摘要给出的奇偶形式与题页所记 c-参数下界一致。
- Erdős–Soifer（1995）及 Campbell–Staton（2005，同行评审）提出并给出下界：对 -k<c<k，f(k^2+2c+1)=k+c/k。Praton（2005 预印本；2008 发表版）证明此一般猜想若对一个 c 成立即对所有 c 成立，故其与 c=0 原猜想等价。
- Baek、Koizumi、Ueoro（2024 预印本）证明受限函数 g 的完整公式 g(k^2+2c+1)=k+c/k，其中所有小正方形必须轴平行；这是重要的正结果，但不控制旋转方形。
- Singh（2026 预印本）证明原问题的传播/级数等价：若 f(n^2+1)>n 一次，则以后缺口至少为常数/k；因此“对无穷多个 k 等号成立”“对所有 k 等号成立”和 sum_{k>=1}(f(k^2+1)-k) 收敛等价。

最近相关工作：最晚直接相关工作是 Anshul Raj Singh 的 arXiv:2601.22163（2026-01-10，3 页预印本）。它明确把原猜想称为仍开放，并提供缩放拼接不等式和上述等价性；没有给出 f(k^2+1)<=k。所检索到的 2024–2026 资料中，没有可检查的原命题证明或反例。

剩余核心：证明或反驳：每个由 k^2+1 个任意取向、内部不交正方形组成的单位正方形装填，其边长和都不超过 k。关键未解障碍是把轴平行情况下可用的水平/竖直随机切线或区间计数控制，推广到任意旋转的正方形。

已使用方法：

- 面积加 Cauchy–Schwarz 给出满平方数 k^2 的精确值，但在 k^2+1 时过弱。
- 显式局部替换和 Halász 型构造给出系统性下界。
- Praton 及 Singh 使用将一个最优装填缩放嵌入网格的“blow-up/拼接”不等式，得到参数间传播关系与等价重述。
- 轴平行情形使用投影、随机平行网格线和交叉计数；该方法目前依赖轴平行性。

争议或不确定性：

- “f”在历史写法中称 maximum，但边界和退化约定并未逐项写明；本审计将其规范为 supremum，避免将此技术问题误判成数学反例。
- 没有检索到 Problem 106 的专门论坛线程；站点的直接 thread/106 地址不可读，故不存在论坛结论可作为解答证据。
- 近期 Singh 结果为 arXiv v1，尚无所见同行评审记录；它的等价性论证可检查，但不应被描述为原猜想的证明。
- 开放状态的结论依赖近期直接作者陈述、问题数据库和针对性检索；“未发现解答”不等于穷尽世界文献的证明。

### 证据来源

- [Erdős Problems, Problem 106](https://www.erdosproblems.com/106) — Thomas Bloom / Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 给出本题的历史陈述、引用链、一般化猜想、轴平行结果及 2026 年等价性结果的数据库记录；该站当前标签为 falsifiable，不能单独视为开放性的证明。
- [Erdős Problems, Problem 106 LaTeX page](https://www.erdosproblems.com/latex/106) — Thomas Bloom / Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 可检索页面文字明确区分 f 与轴平行的 g，列出 Halász、Erdős–Soifer、Campbell–Staton、Praton、Baek–Koizumi–Ueoro 和 Singh 的结果，并记录一般猜想与原猜想的等价关系。
- [Some problems in number theory, combinatorics and combinatorial geometry](https://eudml.org/doc/232764) — Paul Erdős, 1994; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 核验 Erdős 1994 年论文的存在、作者、期刊、卷期和页码；它是该问题的主要历史来源之一。
- [Packing a convex domain with similar convex domains](https://www.sciencedirect.com/science/article/pii/0097316584900244) — Sylvia Halász, 1984-07-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 摘要直接给出对正方形、平行四边形和三角形的相邻参数下界，支撑历史下界而非原猜想的上界。
- [A Square-Packing Problem of Erdős](https://www.tandfonline.com/doi/abs/10.1080/00029890.2005.11920180) — Connie M. Campbell and William Staton, 2005; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 核验 Campbell–Staton 论文的题名、作者、期刊页码和 DOI；其提出的更一般公式是后续等价性讨论的对象。
- [Packing Squares in a Square](https://www.tandfonline.com/doi/abs/10.1080/0025570X.2008.11953576) — Iwan Praton, 2008; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 核验 Praton 2008 年发表版本的存在和 DOI；其较早 arXiv 版本说明：若 Campbell–Staton 公式对一个 c 成立，则对所有 c 成立，因而 c=0 原猜想与一般公式等价。
- [The Erdos and Campbell-Staton conjectures about square packing](https://arxiv.org/abs/math/0504341) — Iwan Praton, 2005-04-16; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 摘要直接陈述一般公式，并说明证明了“对一个 c 成立则对所有 c 成立”；把 c=0 代入即得到与原猜想的等价性。
- [A note on the Erdős conjecture about square packing](https://arxiv.org/abs/2411.07274) — Jineon Baek, Junnosuke Koizumi, and Takahiro Ueoro, 2024-11-11; `preprint`, `preprint`, directness=`direct`, reliability=`high`. v2 摘要和正文定理直接证明：若所有小正方形边均平行于单位正方形边，则 g(k^2+2c+1)=k+c/k（-k<c<k），特别 g(k^2+1)=k；论文未声称解决允许旋转的 f。arXiv 页面未列期刊发表信息。
- [On a square packing conjecture of Erdős](https://arxiv.org/abs/2601.22163) — Anshul Raj Singh, 2026-01-10; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 正文引言明确称原猜想仍开放；论文证明若某个 ε(n)=f(n^2+1)-n>0，则之后 ε(k)=Omega(1/k)，从而原猜想等价于对无穷多个 k 成立，也等价于 sum ε(k) 收敛。arXiv 页面未列期刊发表信息。
- [Geombinatorics Quarterly, Volume XVII](https://geombina.uccs.edu/past-issues/volume-xvii) — Geombinatorics Quarterly, 2007; `secondary_index`, `database_record`, directness=`indirect`, reliability=`medium`. 核验 Staton–Tyler 2007 年论文《On the Erdös Square-Packing Conjecture》的存在；2024 预印本据此归属轴平行 g 的引入。

### 完成标准

- 肯定出口: A complete affirmative resolution is a proof that for every positive integer k and every packing of exactly k^2+1 positive-side-length, arbitrarily oriented squares with pairwise disjoint interiors in [0,1]^2, the total side length is at most k. Together with the explicit grid-splitting construction, this proves f(k^2+1)=k for all k.
- 否定出口: A complete negative resolution is one explicit positive integer k and a rigorously verified packing of exactly k^2+1 such squares in [0,1]^2 whose total side length is strictly greater than k. The certificate must give exact or rigorously bounded coordinates, orientations, side lengths, containment, and pairwise interior-disjointness checks.

不构成完成：

- Proving the result only when every small square is axis-parallel, i.e. for g rather than f.
- Verifying finitely many k numerically or by an uncertified optimization search.
- Giving the standard lower-bound construction of value k without a universal upper bound.
- Showing an equivalent series statement without proving its convergence or producing a counterexample.
- Using an area bound alone, which proves f(k^2)=k but does not exclude a total side length greater than k when there are k^2+1 squares.

正确性陷阱：

- Do not silently impose axis parallelism, congruence, tiling, non-touching boundaries, or a fixed ordering of the squares.
- Count exactly k^2+1 positive-area squares; zero-size padding and a packing with fewer squares are not a counterexample certificate.
- For rotated squares, containment in [0,1]^2 must be checked for all four vertices and non-overlap must mean disjoint interiors, not merely distinct centers or non-overlapping axis-aligned bounding boxes.
- An upper-bound proof must cover every k>=1 and preserve strict/equality cases; an asymptotic o(1) loss is insufficient.
- Any use of a maximum-attaining configuration must justify compactness/limiting arguments or be phrased in terms of suprema.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `24/100`
- 信心: `medium`
- 结论: 这是定义清楚且可证伪的开放几何不等式，适合开展证明优先的研究，但目前没有显示出可直接推广到任意旋转方形的机制；AI 独立解决的短期概率偏低至中低。

支持理由：

- 目标是精确的全称不等式，正反完成证书均清楚，且已有强下界和轴平行完整定理可供压力测试。
- Praton/Singh 的缩放传播表明：任何一个反例会在无穷多个尺度留下定量痕迹，这可能帮助构造反证或归约。
- 问题很具体，局部几何引理、投影不等式或极值构型分类都可被独立验证。

主要障碍：

- 面积法恰好在 k^2+1 参数失效；仅知 sum s_i^2<=1 无法禁止 sum s_i>k。
- 最佳已知完整结果 g 强烈依赖轴平行；任意旋转会破坏其离散网格交叉计数。
- 全称 k 与连续位置/角度空间相结合，有限数值实验不能替代证明。
- 历史悠久且近期论文仍只得到受限版本和等价重述，表明核心缺口并不窄。

Proof-first 路线：

- 尝试把任意取向方形的投影、宽度或积分几何量与边长和联系起来，并明确寻找足以替代轴平行交叉计数的统一上界。
- 研究极值/近极值装填的接触图和边界饱和性质；任何归约到有限组合类型前必须严格处理退化和极限。
- 利用 Singh 的拼接不等式反向测试：若存在超额 ε(k)>0，则其在大尺度的必然传播是否与新的几何上界矛盾。
- 唯一可选计算任务：在预先声明的角度/接触图引理下，搜索小 k 的经认证反例或验证该引理；若问题已判定，立即释放计算槽。

需要验证：

- 逐行复核 Singh 预印本的缩放拼接不等式及其适用于任意旋转方形的条件。
- 若依赖 Praton 的一般化等价性，核对发表版中 c 的端点、开区间和符号约定。
- 任何声称推广 Baek–Koizumi–Ueoro 的证明都必须定位并消除其轴平行性使用点，而不能只替换术语。
- 对任何计算辅助结果要求精确/区间算术证书、完整搜索域覆盖和可独立复核代码。

### 审计限制与人工复核理由

- 当前问题页与其 LaTeX 页可由搜索索引读取，但直接页面抓取返回内部错误；其内容已由题目给定 JSON、搜索索引和所列原始/预印本文献交叉核对。
- 没有逐页取得 1995 年 Geombinatorics 原文及 2008 年付费全文；对其具体数学作用依赖可访问的 Praton arXiv 摘要、出版商元数据和 2024 论文的文献回顾，故未把未直接检验的细节当作新定理。
- 开放性只能由截至截止日的针对性检索和近期直接文献支持；无法从“未找到”演绎出全球范围没有未收录解答。
- 未进行正式化仓库的穷尽检索；问题页标为未形式化，且所检索的 2024/2026 工作均未给出形式化工件链接。

- 无

<!-- DEEP_REVIEW:END -->
