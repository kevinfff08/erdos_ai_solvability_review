# Problem 1082

## 基本信息

- 原始链接: https://www.erdosproblems.com/1082
- LaTeX 页面: https://www.erdosproblems.com/latex/1082
- 原始状态: `falsifiable`
- 奖金: `no`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`
- 形式化状态: `yes`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $A\subset \mathbb{R}^2$ be a set of $n$ points with no three on a line. Does $A$ determine at least $\lfloor n/2\rfloor$ distinct distances? In fact, must there exist a single point from which there are at least $\lfloor n/2\rfloor$ distinct distances?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `53/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：distances, geometry
- 题面含渐近/无限对象线索：\gg
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
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 with computation/formalization/literature/counterexample-search tools`
- 结论: **中等候选。这个问题不适合期待模型直接给出完整证明，但很适合由 GPT-5.5 级别模型做结构化推进：提取并形式化命题、验证已知的单点版本反例、对小规模点集做反例搜索、把 Szemerédi 的 n/3 思路整理成可审计证明框架，并尝试寻找通向 n/2 的加强条件。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 最可能的有效路线不是直接证明一般情形，而是分成两支：第一，针对第二个“存在一个点有至少 floor(n/2) 个不同距离”的加强命题，利用备注中的 8 点 Harborth 构造，恢复坐标或等价约束并用符号/数值程序验证无三点共线、且每点到其余点只有 3 种距离，从而形成可形式化的反例证书；第二，针对第一个全局 distinct distances 命题，把它转化为组合几何约束搜索与半形式证明任务，先复现 Szemerédi 的 n/3 证明，再尝试通过局部结构分类、圆-线 incidence 限制、有限小 n 搜索和极端构型分析推进 n/2。

### 支持理由

- 题目状态是 falsifiable，且备注已给出第二个更强单点命题的负例线索；这类任务非常适合模型结合图像/文献/坐标恢复和计算验证来完成可审计反例证书。
- 命题已经 formalized，这降低了把问题输入定理证明器、SMT/代数验证器或组合搜索程序的成本。
- 核心对象是有限平面点集、共线性约束和距离等值关系；对小 n 反例搜索、距离矩阵约束、圆交结构枚举等，工具增强模型可以给出有价值的实验性推进。
- 备注中说明已有 n/3 的未出版证明线索；模型有机会把该证明重建、清理、形式化，并识别从 n/3 到 n/2 缺失的关键瓶颈。

### 主要障碍

- 第一个全局问题看起来属于经典组合几何中的 distinct distances / inverse distinct distances 范畴，完整证明可能需要新的结构性洞察，而不只是计算枚举。
- 无三点共线是强但仍然较宽的条件；极端构型可能连续变形，导致有限枚举不能直接覆盖一般实数坐标情形。
- 从 n/3 提升到 n/2 需要非常精细地控制多点共圆、重复距离和局部距离分布，简单 incidence bound 很可能不够。
- 备注只给出第二问的反例描述而非坐标；若仅凭图片恢复构造，仍需严格验证坐标精度、非共线性和距离类别数。

### 需要的验证

- 若主张第二问已被反例否定，需要给出 8 点构造的精确坐标或代数定义，并逐点列出距离分组。
- 需要机器验证所有三点行列式非零，排除退化共线。
- 需要验证每个点到其余 7 点的 distinct distances 数量确实为 3，小于 floor(8/2)=4。
- 若尝试推进第一问，需要把任何计算搜索结果转化为可复现脚本、参数范围、排除条件和独立验证日志。
- 若声称证明了第一问，必须给出形式化或近形式化证明，明确说明如何处理任意实数坐标和所有 n。

### 公开版思考摘要

这个问题包含两个层级：全体点集是否至少给出 floor(n/2) 个不同距离，以及是否存在一个单点看到这么多不同距离。给定 JSON 已说明第二个更强命题有 8 点反例，因此模型较可能完成的是恢复、验证、形式化这个反例，并围绕第一个较弱命题做计算搜索和证明框架整理。第一问本身仍显著困难，GPT-5.5 更可能提供局部进展、反例排查、已有 n/3 证明重构，而不是可靠地产生完整新证明。

### 免责声明

以上是对工具增强 GPT-5.5 处理该 Erdős 问题的可行性评估，不是该问题的证明或反例构造。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `revised_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [problem_1082.md](../../prompts/problem_1082.md)

### 状态结论

题目原含两个层次：全局距离种数下界，以及更强的单点距离下界。Harborth 的 8 点配置已否证单点加强版，但不否证全局下界；因此把规范开放核心修订为第一问。

### 当前规范陈述

对平面中任意 n 点集 A（无三点共线），证明或否证它至少确定 ⌊n/2⌋ 种不同的正点间距离。

```text
For every n-point set A in R^2 with no three points collinear, prove or disprove that A determines at least floor(n/2) distinct positive pairwise distances.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `counterexample_found`
- 检查说明: Harborth 的 8 点配置使每个点只看到 3<floor(8/2) 种距离，否证第二个加强问；全局配置仍可能有至少 4 种距离。
- 版本变化: 修订后只保留 Szemerédi 的全局 floor(n/2) 猜想；旧 n/3 下界仍是主要通用结果。

陈述问题：

- 必须把全局距离集合与某个顶点看到的 pinned distances 区分。
- 点互异，无三点共线；正距离自动排除 0。

需要固定的量词/约定：

- The distance set is formed from all unordered pairs of distinct points.
- The target is the global first question only.

### 文献与当前边界

已核验的主要结果：

- A regular n-gon gives the upper-bound construction floor(n/2).
- Szemerédi proved a lower bound about n/3.
- The pinned-distance strengthening is false by an 8-point configuration.

最近相关工作：题目历史页在 2026-04 加入 Harborth/Erdős--Fishburn 文献反例；未发现关闭全局第一问的新结果。

剩余核心：把无三点共线条件下的全局距离下界从约 n/3 提升到精确 floor(n/2)，或构造低于该值的点集。

已使用方法：

- counting isosceles triangles
- incidence bounds for distance graphs
- extremal structure near regular polygons

争议或不确定性：

- Szemerédi 的 n/3 证明最初未正式发表，需从二手书/原文核对常数。
- 相关凸位置 pinned-distance 问题不是本题。

### 证据来源

- [Erdős Problem 1082](https://www.erdosproblems.com/1082) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 1082](https://www.erdosproblems.com/latex/1082) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [Revision history of Erdős Problem 1082](https://www.erdosproblems.com/history/1082) — Thomas F. Bloom; `problem_page`, `database_record`, reliability=`medium`. 明确记录第二加强问的 8 点反例并保留第一问。
- [Distinct Distances: Open Problems and Current Bounds](https://adamsheffer.wordpress.com/2013/05/04/distinct-distances-open-problems-and-current-bounds-1/) — Adam Sheffer; `other`, `unknown`, reliability=`medium`. 记录无三点共线版本的 n/3 下界和 floor(n/2) 猜想。

### 完成标准

- 肯定出口: Prove that every no-three-collinear n-point set determines at least floor(n/2) distances.
- 否定出口: Give exact coordinates for a no-three-collinear set determining fewer than floor(n/2) distances, with exact distance-equality certificates.

不构成完成：

- Proving the false pinned-distance strengthening.
- A result only for convex position.
- A configuration with three collinear points.

正确性陷阱：

- Count global distinct distances, not per-vertex maxima.
- Verify no-three-collinear exactly.
- Use exact algebraic comparisons for any counterexample.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `46/100`
- 信心: `medium`
- 结论: 评分只针对核验后的规范开放核心，反映定义清晰度、可验证中间义务、已有方法入口和剩余理论跨度。

支持理由：

- 规范目标和完成标准可以明确写出。
- 已有结果提供可核验的技术入口或边界。

主要障碍：

- Szemerédi 的 n/3 证明最初未正式发表，需从二手书/原文核对常数。
- 相关凸位置 pinned-distance 问题不是本题。

Proof-first 路线：

- 改进等腰三角形计数以压低同一距离的总重数。
- 证明接近 n/3 极值的配置必须接近规则多边形并获得额外距离。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态涉及题面修订、解答声明、低覆盖文献或较新预印本，建议专家重点抽查。

<!-- DEEP_REVIEW:END -->
