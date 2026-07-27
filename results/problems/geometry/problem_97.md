# Problem 97

## 基本信息

- 原始链接: https://www.erdosproblems.com/97
- LaTeX 页面: https://www.erdosproblems.com/latex/97
- 原始状态: `falsifiable`
- 奖金: `$100`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`, `convex`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Does every convex polygon have a vertex with no other $4$ vertices equidistant from it?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `49/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：convex, distances, geometry
- 原记录含奖金 $100，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: convex, distances, geometry
- 有限/计算线索: 无
- 渐近/无限线索: 无
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **这是一个中等候选问题：GPT-5.5 级别模型较有希望通过计算搜索、代数验证和形式化辅助显著推进，尤其是寻找反例；但若命题为真，完整证明的难度可能明显高于纯计算可解决范围。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 最可行路线是把问题作为有限反例搜索来攻：枚举或学习“每个顶点至少有 4 个等距邻点”的距离重合模式，用非线性约束求解、SMT/实闭域判定、圆交结构和凸性不等式筛选候选构型；若找到数值候选，再用代数数坐标、区间验证或形式化证明确认凸性与等距关系。另一条路线是尝试把等距四元组产生的圆弧/对角线结构转化为组合几何约束，证明必有一个顶点的距离重数小于 4。

### 支持理由

- 问题是可证伪型：一个满足条件的凸多边形反例即可否定命题，适合计算搜索和形式化验证。
- 条件可以转写为多项式等式与严格不等式：等距关系是平方距离相等，凸性是有向面积符号一致，因此可被 SMT、CAD、区间算术或证明助理处理。
- 已有备注显示 k=3 情形存在显式构造，说明该问题附近有可构造的有限几何对象，AI 可以围绕这些模式做参数扩展或自动发现。
- 问题陈述短、局部结构明确，不需要庞大理论体系才能开始实验；GPT-5.5 可协调枚举、优化、符号化和证明检查。
- formalized=yes 提高了验证上限：即使 AI 只发现候选证明或反例，也可转化为机器可检查目标。

### 主要障碍

- 搜索空间很大：需要同时选择每个顶点的等距四元组、顶点循环顺序、可能的共享距离关系以及凸性约束。
- 数值优化容易产生近似伪解；等距退化、共圆退化、非严格凸性或顶点重合都可能误导搜索。
- 若最小反例需要很多顶点或高次数代数坐标，自动发现和精确化会变难。
- 如果命题为真，证明可能需要新的组合几何思想，而不仅是穷举小规模构型。
- 备注中关于任意 k 构造的说法不可靠，不能直接作为路线依据。

### 需要的验证

- 若输出反例，需要给出顶点坐标、严格凸性的可检查证明、每个顶点对应的 4 个等距顶点索引，以及所有距离等式的精确或区间认证。
- 需要排除数值近似误差：用有理/代数数重构，或用区间算术证明等式与不等式在可接受范围内成立。
- 若输出证明，需要形式化关键引理，尤其是从凸性和等距四元组到必有低重数顶点的组合推导。
- 应对小 n 做完整枚举或 SMT 不可满足性验证，作为反例搜索或证明策略的基准。
- 需要检查是否存在隐藏退化，例如三点共线、重复顶点、非凸排序或同一等距集合计数方式错误。

### 公开版思考摘要

这个问题的 AI 可攻性主要来自它的有限几何和代数约束形态：反例是一组有限点，验证条件非常明确。GPT-5.5 配合程序搜索、非线性求解、实代数验证和形式化工具，可能找到并认证反例，或者至少给出小规模不可满足性证据和结构性猜想。不过完整解决仍不稳，因为 k=4 可能需要较大构型或新的凸几何论证；因此评为 medium_candidate，而不是高候选。

### 免责声明

以上是对 GPT-5.5 级别模型可推进性的审查，不是该 Erdős 问题的证明、反例或最终解答。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_97.md](../../prompts/problem_97.md)

### 状态结论

现有可核验记录支持该题仍是开放问题：已知反例只否定了阈值 3，而非当前的阈值 4；Fishburn–Reeds 的 20 点构造也只保证每个顶点有三个等距顶点。题页提及的“Danzer 对任意常数均有反例”的二手归因被题页自身明确质疑，不能据此把 k=4 判为已否定。未找到可核验的 k=4 解答或反例记录；因此结论为 likely_open，而非 confirmed_open。

### 当前规范陈述

对欧氏平面中的每个有限凸多边形 P，设其顶点集为 V(P)。是否总存在顶点 v∈V(P)，使得对任意 r>0，至多有三个其他顶点 w∈V(P)\{v} 满足 |v-w|=r？等价地，是否不可能存在一个凸多边形，使其每个顶点 v 都有四个不同的其他顶点 w1,w2,w3,w4 与 v 距离相同？该共同距离允许随 v 改变。

```text
For every finite convex polygon P in the Euclidean plane, with vertex set V(P), does there exist a vertex v in V(P) such that, for every r>0, at most three vertices w in V(P) minus {v} satisfy |v-w|=r? Equivalently, is it impossible that every vertex v has four distinct other vertices w1,w2,w3,w4 at one common distance from v (where the common distance may depend on v)?
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 题页记载的 Danzer 9 点例子和 Fishburn–Reeds 20 点例子均只给出每个顶点有三个等距顶点，不能否定本题。题页给出的单位距离图论证仅在删除凸性要求后适用。未发现一个可核验的凸多边形，其中每个顶点均有至少四个等距其他顶点；这不是不存在该构造的证明。
- 版本变化: Erdős 1946 年提出较强的 k=3 猜想。Danzer 的 9 顶点凸多边形使每个顶点具有三个等距顶点，从而否定该猜想；该距离可随中心顶点改变。Fishburn 与 Reeds（1992）构造了 20 顶点凸多边形，其中每个顶点亦有三个等距顶点，且可采用同一距离。当前题目因此询问 k=4。Erdős 1975 年曾将“对任意 k 均有反例”归于 Danzer，但当前题页说明此说法未在后续文献重述并怀疑其有误；它不能作为 k=4 已否定的证据。

陈述问题：

- 英文“no other 4 vertices equidistant from it”应理解为：不存在四个不同顶点到该顶点的距离相同；并非“四个顶点彼此两两等距”。
- 逻辑上应读作“不存在四元组”，因此禁止距离重数至少为 4，而不是仅禁止距离重数恰为 4。
- “convex polygon”应按通常的非退化凸多边形理解：有限顶点、顶点互异，按边界循环顺序排列；研究者应声明是否采用严格凸约定。

需要固定的量词/约定：

- The outer quantifier ranges over all finite Euclidean convex polygons P.
- The selected vertex v may depend on P.
- For each fixed v, the radius r is quantified after v and may depend on v.
- The four vertices are distinct and different from v.
- The prohibition is a distance class of cardinality at least 4; hence the desired vertex has all distance multiplicities at most 3.

### 文献与当前边界

已核验的主要结果：

- Erdős（1946）提出的阈值 3 版本已被 Danzer 构造否定；当前题页将该构造描述为 9 顶点凸多边形，且每个顶点有三个等距顶点。
- Fishburn 与 Reeds（1992，同行评审）给出 20 顶点凸多边形；题页称每个顶点有三个等距顶点，且共同距离可取相同。该结果仍只处理阈值 3。
- 若去掉凸性，任意最小度 d 的单位距离图可导出非凸多边形反例；这不适用于凸多边形。

最近相关工作：本次核验未取得 2023–2026 年直接解决 k=4 版本的可核验论文、预印本或形式化证明。题页的“formalized=yes”说明应理解为已有某种命题形式化记录，而非该命题已被证明；由于未能定位公开工件链接，不能把它作为实质性数学证据。

剩余核心：构造一个严格凸多边形，使每个顶点的某个距离类至少含 4 个其他顶点；或证明任意凸多边形总有一个顶点的所有距离类大小至多为 3。允许半径随顶点改变。

已使用方法：

- 从凸位置点集的单位距离/等距关系构造具有高局部距离重数的图。
- 利用凸多边形的圆-边界交点、距离图与组合几何限制，尝试推出存在低距离重数顶点。
- 历史上，显式坐标构造与单位距离图思想均已出现；任何计算应服务于可精确认证的构造或引理。

争议或不确定性：

- Erdős 1975 年关于 Danzer 已处理任意 k 的归因未获得独立核验，且当前题页明确表示怀疑。
- 未定位数据库“formalized=yes”对应的公开形式化工件，故无法核对其精确陈述、依赖和是否仅为定义性形式化。
- 没有检索到 k=4 的解答不构成不存在解答的逻辑证明；因此状态保守标为 likely_open。

### 证据来源

- [Erdős Problems, Problem 97](https://www.erdosproblems.com/97) — Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 给出当前 k=4 问题、Danzer 9 点与 Fishburn–Reeds 20 点的历史说明、对 1975 年“任意常数”归因的保留意见，以及非凸版本的反例说明。
- [Erdős Problems, LaTeX source for Problem 97](https://www.erdosproblems.com/latex/97) — Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 核对当前页面的数学措辞、参考文献键及历史备注。
- [Unit distances between vertices of a convex polygon](https://doi.org/10.1016/0925-7721(92)90008-2) — Peter C. Fishburn and James A. Reeds, 1992; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 该文是题页所引 Fishburn–Reeds 20 顶点构造的主要文献；其相关性和题名可由出版记录核验。完整构造细节仍应由后续研究代理人逐页检查。

### 完成标准

- 肯定出口: Prove that for every finite convex polygon P there is a vertex v such that every set {w in V(P) minus {v} : |v-w|=r} has cardinality at most 3 for every r>0.
- 否定出口: Give a finite convex polygon P and, for every v in V(P), exhibit four distinct vertices w1,w2,w3,w4 different from v and a number r_v>0 with |v-w_i|=r_v for i=1,2,3,4; prove that the listed cyclic order is convex and that all asserted equalities are exact.

不构成完成：

- Showing the property for only some vertices of a proposed counterexample.
- Giving a non-convex polygon, a self-intersecting cycle, or an unverified point order.
- Giving four globally equal lengths that do not emanate from each individual vertex.
- Establishing a common-distance construction only with three neighbours per vertex.
- Numerical plots or floating-point coordinates without an exact certificate of convexity and all distance equalities.

正确性陷阱：

- Do not confuse four vertices equidistant from v with four vertices mutually equidistant.
- Do not replace ‘at least four’ by ‘exactly four’.
- The radius may depend on v; a common-radius counterexample is stronger but not required.
- A point set in convex position must be supplied with, or proved to have, a valid convex cyclic order.
- For an affirmative proof, quantify over all radii at the chosen vertex, not merely a designated distance.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `28/100`
- 信心: `medium`
- 结论: 这是定义清楚、可由有限精确证书检验的开放构造/极值几何问题；但已知 k=3 构造显示其并非局部容易问题，且当前文献链和形式化条目尚需人工补核。

支持理由：

- 正反两方向均有明确、有限且可独立验证的完成标准。
- 历史构造提供了具体的结构线索和可检验的基准，而非纯粹宽泛的“估计”请求。
- 凸性施加了实质约束，避免了非凸单位距离图带来的直接反例。

主要障碍：

- 从每点三重距离类提升至四重距离类可能需要新的全局几何设计或新的结构定理。
- 有限坐标搜索很容易产生近似共圆、近似等距或非凸伪例，不能自行解决一般问题。
- 历史上关于任意 k 反例的未核实归因可能隐藏已知但难以定位的结果。

Proof-first 路线：

- 首先逐页核实 Fishburn–Reeds 构造和 Danzer 构造的距离图结构，判断可否以严格保持凸性的操作增加一层距离重数。
- 并行探索反向结构引理：对凸位置点集的距离类/圆交边界模式证明必有一个顶点的最大距离重数至多 3。
- 最多进行一次有停止条件的精确计算：在预先指定的参数化凸构造族内，搜索满足每顶点四重距离类的有理或代数坐标证书；若该族被穷尽或找到证书，立即结束该计算线。

需要验证：

- 取得并检查 1992 论文的完整文本及其构造验证。
- 查阅 Erdős 1946、1975、1987 原文，特别是 Danzer 归因。
- 定位“formalized=yes”的公开工件、形式化系统、提交版本和定理陈述。
- 由人工或后续代理人复查 2023–2026 年 arXiv、MathSciNet/zbMATH、作者主页与论坛。

### 审计限制与人工复核理由

- 当前环境未能提供可检查的题目论坛页面、完整历史论文文本或“formalized=yes”对应的公开形式化链接；因此没有把这些未检验材料当作已证实结论。
- 未发现 k=4 解决方案是检索证据而非不存在性的证明，故状态为 likely_open 且要求后续人工复核。
- Fishburn–Reeds 的出版记录可定位，但其完整构造的逐项验证应在获取全文后完成。

- 需要人工取得并审阅 Erdős 1946、1975、1987 文本及 Fishburn–Reeds 全文，以核实构造和 Danzer 归因。
- 需要定位并核查数据库标记的形式化工件，确认它是命题形式化还是已完成的证明。
- 在使用“当前开放”作研究立项依据前，应以实时的 arXiv、期刊索引、作者主页和题目论坛检索再做一次复核。

<!-- DEEP_REVIEW:END -->
