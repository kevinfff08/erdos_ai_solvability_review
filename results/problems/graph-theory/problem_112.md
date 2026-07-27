# Problem 112

## 基本信息

- 原始链接: https://www.erdosproblems.com/112
- LaTeX 页面: https://www.erdosproblems.com/latex/112
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $k=k(n,m)$ be minimal such that any directed graph on $k$ vertices must contain either an independent set of size $n$ or a transitive tournament of size $m$. Determine $k(n,m)$.

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：\ll

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: \ll
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5-level model with computation, formal proof, literature search, and counterexample search tools`
- 结论: **中等候选。完整确定一般的 k(n,m) 很可能超出现阶段模型的一次性能力，因为它同时包含无向 Ramsey 数和多色 Ramsey 型障碍；但该问题结构清晰、有限可计算、可形式化，GPT-5.5 级别系统有现实机会在小参数精确值、m=3 或固定小 m 的改进界、构造搜索、SAT/ILP 验证和已有证明机械化方面取得显著推进。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 可行路线不是直接宣布通式，而是先把问题编码为有限极值搜索：用 SAT/CP-SAT/ILP 枚举避免独立 n 集与传递 m 锦标赛的有向图，生成小参数表；再从极值例子中抽取递推或分层结构；对固定 m，尝试归纳证明上界并用构造族给下界；同时形式化核心归纳引理和计算证书，确保小规模结果可复验。

### 支持理由

- 题面短、对象明确，性质可被直接编码：独立集约束和传递 tournament 约束都是有限子集上的可检查谓词，适合 SAT/ILP、反例搜索和证书验证。
- 已给出多项已知界，说明问题存在可利用的递推和 Ramsey 型包夹，而不是完全缺少入口。
- 对固定小 m，尤其 m=3，约束相对低阶，模型可结合计算实验寻找精确值、极值构造和可证明的改进界。
- 形式化证明的负担可分层处理：先形式化定义与小参数证书验证，再形式化人工可读的归纳上界，适合作为工具增强型 AI 的推进目标。
- 即使不能解决一般式，产生新的小参数表、可验证构造、改进常数或发现已有界的紧性/非紧性，也属于对开放问题的显著推进。

### 主要障碍

- 一般情形至少受普通 Ramsey 数下界 R(n,m) 影响，精确确定很可能继承 Ramsey 理论中难以精确求值的组合爆炸。
- 题目要求 determine k(n,m)，若理解为全参数闭式或精确公式，难度远高于小规模计算与局部上界改进。
- 极值有向图可能没有简单唯一结构；从计算样例归纳出可证明通式存在较高失败风险。
- 需要精确定义 directed graph 是否允许双向边、是否为 oriented graph、独立集按底层无向图还是无弧双向定义；定义差异会改变编码和结论。
- SAT/ILP 搜索的非存在性证明需要可信证书或独立验证，否则容易得到不可审计的经验性结论。

### 需要的验证

- 先固定并记录形式定义：允许的弧类型、独立集定义、transitive tournament 的诱导/非诱导要求。
- 对小参数生成完整可复验表，并保存 SAT UNSAT 证书、模型构造或可检查的极值图文件。
- 将任何猜测公式分别验证上下界：下界要给出显式构造族，上界要给出可形式化的归纳或结构引理。
- 与题面给出的已知界逐项交叉检查，确保新结论不弱于或不矛盾于 Erdos-Rado、Larson-Mitchell 和 Ramsey 包夹界。
- 若声称解决固定 m 或一般 m，需要同行级证明审查，并最好在 Lean/Isabelle 或独立检查器中形式化关键有限归约与证书。

### 公开版思考摘要

这个问题对 AI 有两个相反特征：一方面，它是典型 Ramsey 极值问题，要求全参数精确值，通常非常困难；另一方面，它的违禁结构是有限且局部的，天然适合自动搜索、证书验证和从小例子发现结构。因此 GPT-5.5 级别模型不应被期望直接完成一般解，但很适合系统推进：先澄清定义，计算小参数，抽取构造和递推，再把局部结果形式化。综合来看，它是“可显著推进但完整解决不稳”的中等候选。

### 免责声明

以上是对 AI 工具辅助可解性和推进潜力的审查，不是该 Erdős 问题的数学解答，也未声称给出 k(n,m) 的精确公式。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_112.md](../../prompts/problem_112.md)

### 状态结论

按有向图的标准本意（oriented graph：无自环、无重边、每对顶点至多一条弧）重构后，该问题是精确确定 r(I_a,L_b) 的公开开放问题。Erdős Problems 当前仍标为 open，但其备注遗漏了 2021 年已同行评审的重大进展：r(I_a,L_3)=Theta(a^2/log a)，且 r(I_4,L_3)=15、r(I_5,L_3)=23。已检索精确题名、符号、作者、arXiv 和近三年文献，未发现覆盖所有参数的解答或反例；这种负面检索证据不足以给出“confirmed_open”，故为 likely_open。

### 当前规范陈述

对任意整数 a,b>=2，令 D 遍历有限定向图：无自环，且任意无序顶点对之间至多有一条有向边。I_a 是 a 个顶点的独立集（任意两点间两个方向均无弧）；L_b 是 b 阶传递锦标赛，即某个 b 点导出子图的顶点可排序为 v_1,...,v_b，且恰有 v_i->v_j（i<j）。定义 k(a,b)=r(I_a,L_b) 为使每个 N 点定向图均含 I_a 或 L_b 的最小 N。目标是对所有 a,b>=2 精确确定该整数。采用正整数边界约定时，k(1,b)=k(a,1)=1。

```text
For integers a,b >= 2, let D range over finite oriented graphs: loopless digraphs in which, for every unordered pair {x,y}, at most one of x->y and y->x is present. Let I_a be an independent set of a vertices (no arc in either direction between any two of them). Let L_b be the transitive tournament on b vertices, equivalently an induced b-vertex subdigraph whose vertices can be ordered v_1,...,v_b with exactly the arcs v_i->v_j for i<j. Define k(a,b)=r(I_a,L_b) to be the least N such that every oriented graph on N vertices contains I_a or L_b. Determine this exact integer for every a,b >= 2. With positive-integer boundary conventions, k(1,b)=k(a,1)=1.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `counterexample_found`
- 检查说明: 发现的是措辞歧义下的条件性反例，而非规范定向图版本的反例：若“directed graph”允许每对顶点有双向弧，且“transitive tournament”被理解为诱导的简单锦标赛，则任意大的完全双向图独立数为 1，却不含诱导的简单 L_b（a,b>=2）；因而该读取下不存在有限 k(a,b)。这说明必须采用“定向图”或“非诱导子图”约定。2021 论文的定向图定义消除了该问题。
- 版本变化: Erdős Problems 的可见历史页未显示该命题的实质性数学改写；其将外部 graphs collection 的“有向路”版本明确标为另一版本，并称该版本有 k(a,b)=(a-1)(b-1)。2021 年论文以 oriented graph、I_a 和 L_b 给出了与此条目相符的精确定义，并取得了条目未收录的进展。

陈述问题：

- 原文只写“directed graph”，未说明是否允许双向边；2021 年论文明确研究的是 oriented graph（无双向边），这应作为可研究的规范版本。
- 原文未说明“contains transitive tournament”是子图还是诱导子图。对定向图而言，L_b 的存在要求每对顶点均有唯一弧，二者在此目标上等价；对允许双向边的一般有向图则不等价。
- “Determine”没有限定为精确值、固定参数还是渐近量；当前及原始措辞最自然的完成标准是所有参数的精确值，而非单一上界或固定 b 的渐近式。
- Erdős Problems 112 当前备注没有列出 2021 年 Ihringer--Rajendraprasad--Weinert 的同行评审结果，因此不能把该条目的文献表当作完整现状。

需要固定的量词/约定：

- Quantify over every finite oriented graph D on exactly N vertices and all integer parameters a,b >= 2.
- An independent set means no arc in either direction between each pair of its vertices.
- L_b is a complete, acyclic orientation on b vertices; the vertex order is existential, not fixed in advance.
- k(a,b) is the least positive integer N with the universal property; the task requests exact values for every parameter pair, not merely asymptotics.
- If arbitrary digraphs with opposite arcs are admitted, containment must mean a non-induced subgraph or the class must first be reduced to oriented graphs.

### 文献与当前边界

已核验的主要结果：

- Erdős--Rado（1967，同行评审）给出固定 b 时的多项式上界；Erdős Problems 转述的显式形式为 k(a,b)<= [2^(b-1)(a-1)^b+a-2]/(2a-3)，其数量级为 O_b(a^(b-1))。
- Larson--Mitchell（1997，同行评审）将该对象明确称为 digraph Ramsey number，并改进估计；后续论文明确转述其 r(I_a,L_3)<=a^2。
- Ihringer、Rajendraprasad、Weinert（2021，同行评审）证明 r(I_4,L_3)=15、r(I_5,L_3)=23，并将 Larson--Mitchell 的通用 m=3 上界改进为 r(I_a,L_3)<=a^2-a+3。
- 同一 2021 论文证明 r(I_a,L_3)=Theta(a^2/log a)。下界由通常 Ramsey 数 r(I_a,K_3) 的已知下界导出；上界采用局部可染邻域的独立集界。
- 对每个固定 b>3，2021 论文证明存在只依赖 b 的常数 C_b，使 r(I_a,L_b)<=C_b a^(b-1)/(log a)^(b-2)。这只是上界，不是精确确定，也不自动给出匹配下界。
- 已知边界/小参数包括 k(a,2)=a、k(2,b)=2^(b-1)，以及 k(3,3)=9、k(4,3)=15、k(5,3)=23；后面三个由 2021 论文汇总或证明。

最近相关工作：检索到的最直接且最新的实质性成果是 Ihringer--Rajendraprasad--Weinert 的 2021 年 Discrete Mathematics 论文（预印本 2017）。对 2023--2026 年的精确题名、符号 r(I_m,L_n)、r(I_3,L_4)、arXiv 和作者页检索未找到宣称解决所有参数或改写该核心渐近结果的可核验论文。

剩余核心：仍须精确确定 r(I_a,L_b) 的一般值；即使在固定 b=3，虽然渐近数量级已知，所有 a 的精确值也未知。对 b>=4，现有结果主要是上界，且 r(I_3,L_4) 被 2021 论文特别列为可行的下一精确实例。

已使用方法：

- 把问题置于定向图 Ramsey 数与序数 partition relation 的对应中。
- 度数递推、入/出邻域分解和小型极值构造。
- 将底图与普通 Ramsey 数比较；特别是利用无三角图 Ramsey 下界。
- 概率法、三角形计数/稀疏化，以及 Alon 的“局部可染邻域”独立集下界。
- 对 b>3 使用 Ajtai--Komlós--Szemerédi 型递归论证。

争议或不确定性：

- 数据库页面仍写 open，但其文献备注遗漏 2021 论文；因此其状态标签支持而不能单独证明当前现状。
- 未能访问 Erdős Problems 的 forum 路由，且没有在公开检索结果中发现可核验的论坛解答或反例。
- “directed graph”与“transitive tournament”原句的约定不足；本审计以 2021 同行评审论文的 oriented-graph 定义作为可操作的规范目标。
- 近三年未找到论文是检索结果，不是不存在新进展的证明。

### 证据来源

- [Erdős Problem #112](https://www.erdosproblems.com/112) — Thomas F. Bloom / Erdős Problems project, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前数据库将该题标为 open，给出 Erdős--Rado 上界、Larson--Mitchell 的 m=3 上界，以及与多色 Ramsey 数的比较；并警示其文献可能不完整。
- [Erdős Problems #112 LaTeX source](https://www.erdosproblems.com/latex/112) — Thomas F. Bloom / Erdős Problems project, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 核对当前命题的 LaTeX 表述。
- [Revision history of Erdős Problem #112](https://www.erdosproblems.com/history/112) — Thomas F. Bloom / Erdős Problems project, 2025-10-20; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 核对可见修订史，并确认条目将有向路版本列为不同问题。
- [Partition Relations and Transitivity Domains of Binary Relations](https://londmathsoc.onlinelibrary.wiley.com/doi/10.1112/jlms/s1-42.1.624) — P. Erdős; R. Rado, 1967; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 原始来源；书目信息确认，并由问题页转述其有限组合上界。
- [On a problem of Erdős and Rado](https://link.springer.com/article/10.1007/BF02558478) — Jean A. Larson; William J. Mitchell, 1997-12; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 摘要直接定义 digraph Ramsey number 为任一有向图含 n 点独立集或 m 阶传递锦标赛的最小阶，并称给出了改进估计。
- [New bounds on the Ramsey number r(I_m, L_n)](https://arxiv.org/abs/1707.09556) — Ferdinand Ihringer; Deepak Rajendraprasad; Thilo V. Weinert, 2017-07-29; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 给出定义、r(I_4,L_3)=15、r(I_5,L_3)=23、r(I_m,L_3)=Theta(m^2/log m) 及一般 n 的上界；全文还说明 oriented graph 的无双向边约定。
- [New bounds on the Ramsey number r(I_m, L_n)](https://ucrisportal.univie.ac.at/en/publications/new-bounds-on-the-ramsey-number-rim-ln/) — Ferdinand Ihringer; Deepak Rajendraprasad; Thilo V. Weinert, 2021-03; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 确认上述预印本已作为 Discrete Mathematics 344(3), Article 112268, DOI 10.1016/j.disc.2020.112268 同行评审发表，并概述其精确小参数值和渐近结论。
- [Forcing large directed paths or independent sets](https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/DirectedPaths.html) — Erdős Problems graphs problem collection, date unknown; `secondary_index`, `database_record`, directness=`direct`, reliability=`medium`. 确认旧问题集实际陈述的是“有向路”替代版本，故不能把该版本的简单精确公式移植到 L_b 版本。

### 完成标准

- 肯定出口: For the canonical oriented-graph problem, prove an exact all-parameter theorem: give a formula, recurrence with proved base cases and a terminating exact evaluation procedure, or another unambiguous characterization that yields k(a,b) for every a,b>=2; prove both the universal upper bound and matching oriented-graph lower-bound constructions for every parameter pair.
- 否定出口: For the literal unqualified wording only, a decisive negative audit outcome would be a proof that its graph/containment conventions admit arbitrary bidirected complete digraphs while requiring induced simple tournaments; then k(a,b) is infinite for a,b>=2. This does not refute the canonical oriented-graph target.

不构成完成：

- An upper bound, lower bound, or asymptotic estimate without equality for every parameter pair.
- Solving only k(a,3), only finitely many small pairs, or only a special family of oriented graphs.
- A computation of candidate values without a complete exhaustive certificate and a theorem extending it to all parameters.
- A proof for the directed-path variant k(a,b)=(a-1)(b-1), which is a different target.
- Treating a bidirected graph as a counterexample after silently changing the canonical oriented-graph convention.

正确性陷阱：

- Check that every extremal construction is an oriented graph, not a digraph with anti-parallel arcs.
- Check that a claimed L_b has all binomial arcs and a single acyclic total order; a directed path is insufficient.
- Check independent sets against the underlying undirected graph: no arc in either direction is allowed.
- Separate exact equality from Theta notation and from constants depending on b.
- When using Ramsey comparisons, preserve the direction of each inequality and state the Ramsey-number convention.
- For induction, verify parameter base cases, strict inequalities, and that every recursive call is within its stated range.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `20/100`
- 信心: `medium`
- 结论: 规范版本是清晰、可检验的开放组合问题，但“对所有参数精确确定”极宽，且已经包含困难的普通 Ramsey 型现象；AI 直接完整解决的前景偏低。较合理的研究产出是一个明确固定参数的新精确值、可审计的新界，或改进现有递归，而不是把有限计算误报为通解。

支持理由：

- 定义、反例证书和小参数构造均可形式化或独立核验。
- 2021 年工作给出具体的下一小参数靶点和可复用的结构性工具。
- 固定 b 的上界与 b=3 的渐近数量级为提出受限引理提供了清楚基线。

主要障碍：

- 完整目标要求无限多个参数对的精确值；已知一般 Ramsey 数嵌入为下界，表明其难度并不局限于有限搜索。
- b=3 的 Theta 结果仍有未知常数和精确值；b>=4 甚至缺乏一般匹配渐近结构。
- 题面术语若未先锁定为 oriented graph，容易把不同的有向路或一般双向图问题混入。

Proof-first 路线：

- 先选择一个严格受限、但可能发表的子命题，例如 r(I_3,L_4) 的精确值，或固定 b 下改进上界中的对数因子；明确其与全参数问题的关系。
- 从极小 (I_a,L_b)-free 定向图的入/出邻域、非邻域和传递三角形计数导出可证的结构引理，再决定是否需要构造。
- 将任何候选构造转化为独立的禁 I_a、禁 L_b 证书，并与普通 Ramsey 下界作一致性检查。

需要验证：

- 复核 2021 正式版本与 arXiv v1 的定理编号、常数和所有小值，尤其在引用改进上界时。
- 在启动研究前再次检索 2026 年数据库、arXiv、MathSciNet/zbMATH 和作者页面。
- 由人工确认项目所采用的“contains”约定是否确为定向图中的诱导 L_b；否则先修复命题。

### 审计限制与人工复核理由

- 无法独立访问 Springer 1997 全文，因此其具体递推和常数仅在官方摘要及 2021 论文的转述范围内采用。
- Erdős Problems forum 链接端点在本次检索中返回内部错误；未能把“无论坛解答”作为强证据。
- 近三年检索覆盖精确题名、符号、arXiv、作者页和公开搜索索引，但没有 MathSciNet/zbMATH 的完整订阅式引文追踪；仍可能遗漏新近或标题不同的工作。
- 将原题规范为 oriented graph 是基于 2021 论文和问题传统的有根据解释；若项目采用一般双向 digraph 的诱导子图语义，必须先进行人工澄清。

- 确认任务接受的“directed graph”及“contains”语义，并明确采用规范定向图版本。
- 在投入大量研究前，对 2021--2026 的 MathSciNet、zbMATH、Google Scholar 引文和作者近期论文作一次人工补充检索。
- 如需引用 Larson--Mitchell 的精确递推或最优性主张，应取得并核读 1997 全文。

<!-- DEEP_REVIEW:END -->
