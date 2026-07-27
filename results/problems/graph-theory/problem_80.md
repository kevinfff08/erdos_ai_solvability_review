# Problem 80

## 基本信息

- 原始链接: https://www.erdosproblems.com/80
- LaTeX 页面: https://www.erdosproblems.com/latex/80
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $c>0$ and let $f_c(n)$ be the maximal $m$ such that every graph $G$ with $n$ vertices and at least $cn^2$ edges, where each edge is contained in at least one triangle, must contain a book of size $m$, that is, an edge shared by at least $m$ different triangles.

Estimate $f_c(n)$. In particular, is it true that $f_c(n)>n^{\epsilon}$ for some $\epsilon>0$? Or $f_c(n)\gg \log n$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `32/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：\gg, \ll, o(

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: \gg, \ll, o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 with computation/formalization/literature-search tools`
- 结论: **低到中等候选。GPT-5.5 级别模型很可能能系统整理已知上界与正则性下界、形式化若干标准推论、用计算搜索小规模构造并验证候选极值图，但独立解决“是否总有对数级书”或给出真正强的新下界的概率不高。该题的核心瓶颈是极端稠密但局部三角覆盖条件下的全局强迫书大小，已知下界依赖正则性而很弱，说明简单局部计数和常规工具大概率不足。**
- 等级: `low_to_medium_candidate`
- 分数: `35/100`
- 信心: `medium`
- 可能路线: 可行路线是先把问题转化为边 codegree 至少 1、总边数至少 cn^2、最大 codegree 最小化的极值问题；分别处理 c>1/4 的线性情形和 c<1/4 的困难区间。模型可用文献检索复核 Fox-Loh 上界构造与正则性下界框架，用计算搜索 blow-up、随机扰动、有限几何或代数图类来寻找低 book-size 例子，并尝试用弱正则性、三角移除、dependent random choice、局部密度增量等技术证明更显式的下界。最现实的产出是改进可读证明、形式化已有定理链、得到有限 n 证据或提出有针对性的中间引理，而不是完整估计 f_c(n)。

### 支持理由

- 问题结构清晰，目标量可直接表示为最大边 codegree 的强迫下界，适合计算搜索、SAT/ILP 建模、随机构造实验和形式化验证。
- 已有备注给出明确技术边界：c>1/4 有线性下界，c<1/4 有亚多项式上界，剩余核心是下界质量，便于模型围绕一个窄瓶颈工作。
- GPT-5.5 级别模型擅长把正则性、三角移除、书大小、密度增量等标准工具重新组合，可能提出可验证的中间命题或简化现有证明。
- 该题不要求立即求精确常数；即便不能完全解决，给出显式增长下界、条件性结果或排除某类构造也算显著推进。

### 主要障碍

- 核心开放点很可能需要新的极值图论思想；已知正则性下界很弱，说明常规紧致性或平均计数很难直接推出对数级下界。
- Fox-Loh 型上界表明多项式下界为假，因此直觉性“密度加三角覆盖应强迫大 book”的路线已经被强烈限制。
- 计算搜索只能覆盖很小 n，且极值构造可能依赖复杂的渐近 blow-up 或 Ramsey 型结构，小规模证据容易误导。
- 形式化证明工具对组合正则性、复杂渐近层级和文献中未完全细化的构造支持有限，主要适合验证局部引理而非发现完整新证明。

### 需要的验证

- 复核 Problem JSON 中列出的 Alon-Trotter、Khadzhiivanov-Nikiforov、Fox-Loh 和正则性下界陈述，确认参数范围和量词没有误读。
- 建立可复现实验框架：对固定 n,c 最小化最大 book size，同时强制每条边属于三角形，并与已知构造对照。
- 若提出新下界，需要逐步验证其是否绕开 Fox-Loh 上界限制，尤其不能隐含推出已知为假的多项式增长。
- 对任何使用正则性或移除引理的证明，必须明确量化依赖关系，确认是否真的给出 log n、迭代对数，还是仅仅给出不可用的趋无穷函数。

### 公开版思考摘要

这个问题对 AI 工具链有一定可操作性，因为定义可计算、已知结果给出了明确边界，且很多候选路线可以被实验或形式化局部验证检验。但真正困难的是把“每条边至少在一个三角形中”提升为“某条边在很多三角形中”的强下界；现有最好下界仍来自正则性方法，说明问题的创新门槛较高。因此我判断它适合作为显著推进或验证候选，不适合作为高概率完整解决候选。

### 免责声明

以上是 AI 可解性与推进潜力评估，不是该 Erdős 问题的解答，也未声称给出新的 f_c(n) 上下界。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `revised_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_80.md](../../prompts/problem_80.md)

### 状态结论

原记录的字面参数域有缺陷：简单图中 c>=1/2 时不存在满足 e(G)>=cn^2 的图，故“最大 m”不定义。将其修复为固定 0<c<1/2、n 足够大后，c>=1/4 的量级已是线性；困难且仍开放的区间是 0<c<1/4。Fox–Loh 已否定原“正幂下界”猜想，但截至本次检索，固定 c<1/4 的对数下界及完整渐近估计仍未见可核验的解决。

### 当前规范陈述

固定实数 0<c<1/2，并令 n 充分大。对所有满足 e(G)>=cn^2、且每条边都属于某个三角形的 n 顶点简单无向图 G，令 bk(G)=max_{xy∈E(G)}|N_G(x)∩N_G(y)|；定义 f_c(n) 为这些 bk(G) 的最小值。等价地，f_c(n) 是必能保证某条边所含不同三角形数至少为 m 的最大整数 m。求 f_c(n) 的渐近增长。真正未解决的区间是固定 0<c<1/4；其明确的残余是/否问题为：对每个这样的 c，是否存在 A_c>0 与 n_0(c)，使一切 n>=n_0(c) 均有 f_c(n)>=A_c log n？

```text
For a fixed real c with 0<c<1/2 and all sufficiently large integers n, define f_c(n) as the minimum, over all simple undirected n-vertex graphs G satisfying e(G)>=c n^2 and such that every edge of G belongs to a triangle, of bk(G), where bk(G):=max_{xy in E(G)} |N_G(x) intersection N_G(y)|. Equivalently, f_c(n) is the greatest integer m forced as the number of distinct triangles through some edge. Determine the asymptotic growth of f_c(n). The nontrivial unresolved regime is fixed 0<c<1/4; its explicit surviving yes/no subproblem is whether, for every such c, there exist A_c>0 and n_0(c) such that f_c(n)>=A_c log n for every n>=n_0(c).
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `counterexample_found`
- 检查说明: 对任意 c>=1/2 及任意 n，简单图均有 e(G)<=n(n-1)/2<n^2/2<=cn^2。因此假设类为空，原定义中的“每个图都必须含有大小 m 的 book”对所有整数 m 都真，没有有限最大值。这直接破坏了原文不加限制的“令 c>0”。
- 版本变化: Erdős–Rothschild 1987 年提出对固定 c 的估计及正幂/对数下界问题。Fox–Loh 的 2011 预印本、2012 年 Combinatorica 论文构造出接近 n^2/4 密度而 booksize 为 n^{O(1/log log n)} 的图，故在每个固定 c<1/4 时原正幂猜想为假。Potechin 2014 年将问题在 Mantel 阈值 n^2/4-nf(n) 的过渡区间细分；这不是固定 c<1/4 情形的解决。故应保留固定 0<c<1/4 的对数下界或完整渐近估计作为修订后的开放目标。

陈述问题：

- 原文写 c>0，但简单 n 顶点图至多有 n(n-1)/2 条边。若 c>=1/2，则满足 e(G)>=cn^2 的图不存在；全称命题对每个 m 都真，因而不存在有限的“最大 m”。
- 即使 0<c<1/2，对有限的小 n 也可能不存在可行图；定义须限制为 n 足够大，或只讨论可行 n。
- “Estimate f_c(n)”本身没有唯一完成标准。应改为指定量级，或选取其明确的对数下界子问题。
- “some epsilon>0”必须明确 epsilon 可依赖于固定 c；Fox–Loh 的结果所否定的是对每个固定 c<1/4 的此类正幂下界。
- “book size”需明确为同一条边所含的不同无序三角形数，即边的共同邻居数。

需要固定的量词/约定：

- c is fixed independently of n; constants A_c, epsilon_c, and implicit constants may depend on c.
- Graphs are finite, simple, and undirected, on exactly n vertices.
- The intended asymptotic definition is meaningful for 0<c<1/2 and sufficiently large n.
- A triangle through xy is specified by a distinct common neighbor z; no multiplicities are counted.
- The hard regime is 0<c<1/4. For c>=1/4 the order is linear, while c>=1/2 is vacuous under the literal edge threshold.

### 文献与当前边界

已核验的主要结果：

- Fox–Loh（2012，同行评议；预印本可读）证明：对充分大的 n，存在边数为 n^2/4(1-exp(-(log n)^(1/6))) 的图，每条边都在三角形中，但每条边至多在 n^(14/log log n) 个三角形中。固定任意 c<1/4 后，该密度最终至少 cn^2，故 f_c(n)<=n^{O(1/log log n)}=n^{o(1)}。这是对原正幂下界猜想的完整否定。
- Fox–Loh 的引言从 triangle removal lemma 推出固定 c>0 时 f_c(n)→∞；采用 Fox 的改进 removal-lemma 定量界得到至少 2^{Omega_c(log* n)} 的下界。2025 年文献仍称 Fox 的一般 triangle-removal 定量界为最佳已知。
- 对 c>1/4，Edwards（未发表）及 Khadzhiivanov–Nikiforov（1979）的经典结果给出至少 n/6 个三角形共享一条边；结合平凡 O(n) 上界，f_c(n)=Theta(n)。在 c=1/4 的边界，Potechin 的阈值结果也给出线性下界，因此其量级同为 Theta(n)。
- Alon–Trotter 早先对每个固定 c<1/4 给出 O_c(sqrt n) 上界，已被 Fox–Loh 的次多项式上界严格加强。
- Potechin（2014 预印本）给出 n^2/4-nf(n) 密度下的下界 min{n/sqrt(f(n)),n^2/f(n)^2}（在其条件内）。该结果刻画部分接近 1/4 的过渡区，但对固定 c<1/4 只给出常数级信息，不能解决当前残余。

最近相关工作：本次定向检索中，最晚直接涉及该定量瓶颈的同行评议来源是 Gishboliner–Shapira–Wigderson（2025），其仍称 Fox 的 triangle-removal 界为最佳已知。未找到 2023–2026 年关于此精确 f_c(n) 问题的可核验解决论文、预印本或形式化证明。Erdős Problems 页面于 2026-04-07 编辑后仍标 OPEN，论坛亦无可审查的解答声明。

剩余核心：固定任意 0<c<1/4 时，当前经核验的缺口为 2^{Omega_c(log* n)}<=f_c(n)<=n^{O(1/log log n)}。完整渐近量级未知；原文中特别提出而尚未被上述证据解决的明确问题是 f_c(n)>>_c log n 是否成立。

已使用方法：

- Triangle removal lemma、Ruzsa–Szemerédi/(6,3) 对应及其定量依赖；它们产生当前很弱的强制性下界。
- Fox–Loh 的高维格点/欧氏距离构造、集中不等式、随机抽稀及后续删去不在三角形中的边；它们产生次多项式上界构造。
- Mantel 阈值附近的稳定性、度数分层和三角形计数（Potechin）；适用于 c 接近 1/4 的过渡窗口。
- 超过 Mantel 阈值时的 booksize 超饱和结果，给出线性区间。

争议或不确定性：

- “最佳已知下界来自正则性引理”的数据库措辞应宽松理解：Fox–Loh 已说明用 Fox 的非正则性证明可改进其定量形式；两者都属于 triangle-removal 路线，并不构成结论冲突。
- 没有发现近三年解决文献不是不存在的逻辑证明；本审计未访问 MathSciNet、zbMATH 的完整引文索引或付费全文数据库。
- “Erdős–Rothschild problem”也常指边着色避免单色团的不同问题；检索中已排除该同名主题。

### 证据来源

- [Erdős Problems — Problem 80, LaTeX source](https://www.erdosproblems.com/latex/80) — Thomas F. Bloom / Erdős Problems database, 2026-04-07; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 给出当前题目文字、Fox–Loh 上界、c>1/4 的线性下界线索，并将题目列为开放。
- [Erdős Problems — Discussion Thread 80](https://www.erdosproblems.com/forum/thread/80) — Erdős Problems database and forum contributors, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 页面当前标为 OPEN；可见评论仅指出 Potechin 的部分改进，且页面明示尚无评论声称完整或部分解答。该状态是网站维护者的判断而非证明。
- [On a problem of Erdős and Rothschild on edges in triangles](https://arxiv.org/abs/1106.0290) — Jacob Fox and Po-Shen Loh, 2011-06-01; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 原文给出定义；Theorem 1.1 构造所有边均在三角形中、边数为 n^2/4(1-exp(-(log n)^(1/6)) ) 且每条边至多在 n^(14/log log n) 个三角形中的图。由此直接推出每个固定 c<1/4 的 f_c(n)<=n^{O(1/log log n)}，从而否定正幂下界猜想。文中还说明 triangle-removal 路线给出指数型 log* 下界。
- [DBLP record: On a problem of Erdös and Rothschild on edges in triangles](https://dblp.org/rec/journals/combinatorica/FoxL12.html) — Jacob Fox and Po-Shen Loh, 2012; `secondary_index`, `database_record`, directness=`indirect`, reliability=`high`. 交叉核对 Fox–Loh 论文已作为 Combinatorica 32(6), 619–628 (2012) 发表，DOI 为 10.1007/s00493-012-2844-3。
- [A note on a problem of Erdos and Rothschild](https://arxiv.org/abs/1412.1838) — Aaron Potechin, 2014-12-04; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 证明当边数为 n^2/4-nf(n) 时的 booksize 下界，并说明其结果针对 Mantel 阈值附近的过渡尺度；它不关闭固定 c<1/4 的主缺口。
- [Number on the Forehead Protocols yielding dense Ruzsa–Szemerédi graphs and hypergraphs](https://cris.tau.ac.il/en/publications/number-on-the-forehead-protocols-yielding-dense-ruzsaszemer%C3%A9di-gr/) — Noga Alon and Adi Shraibman, 2020-08-01; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 该 2020 年同行评议论文的引言仍将固定 c 的问题表述为待确定/估计，并复述 Fox–Loh 的次多项式上界与基于 removal lemma 的很弱下界；其自身结果是稠密 Ruzsa–Szemerédi 图/超图，未解决本题。
- [A new proof of the graph removal lemma](https://annals.math.princeton.edu/2011/174-1/p17) — Jacob Fox, 2011-07-01; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 验证用于改进 triangle-removal 定量界的基础论文及其同行评议发表信息。
- [An efficient asymmetric removal lemma and its limitations](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F5E7BAF97A98F8228054413823888C62/S2050509424000689a.pdf/an-efficient-asymmetric-removal-lemma-and-its-limitations.pdf) — Lior Gishboliner, Asaf Shapira, and Yuval Wigderson, 2025; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 该近年论文明确称 Fox 的 tower-height O(log(1/epsilon)) 仍是 triangle removal lemma 的最佳已知一般定量上界；这支持“removal-lemma 路线仍未产生对数级 f_c 下界”的文献背景，但不单独证明本题开放。
- [Graphs covered by triangles](https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/CoveredInTriangles.html) — Fan Chung and Ronald Graham graph-problem collection, date unknown; `secondary_index`, `unknown`, directness=`direct`, reliability=`medium`. 独立旧问题集记录了 Erdős–Rothschild 的原问题、Alon–Trotter 上界、Szemerédi 发散下界和原正幂猜想，支持历史重建。
- [Erdős Problems — Problem 905](https://www.erdosproblems.com/latex/905) — Thomas F. Bloom / Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 交叉记录 Khadzhiivanov–Nikiforov 的经典结论：超过 n^2/4 条边的图有一条边属于至少 n/6 个三角形。

### 完成标准

- 肯定出口: For the explicit residual logarithmic target: prove that for every fixed c in (0,1/4) there are constants A_c>0 and n_0(c) such that every n-vertex simple graph G with n>=n_0(c), e(G)>=c n^2, and every edge in a triangle has bk(G)>=A_c log n. A stronger determination f_c(n)=Theta_c(g_c(n)) with matching upper and lower bounds also resolves the original repaired estimation request.
- 否定出口: Disprove the logarithmic target by giving one fixed c in (0,1/4) and graphs G_i with |V(G_i)|=n_i→infinity, e(G_i)>=c n_i^2, every edge in a triangle, and bk(G_i)/log n_i→0 (or otherwise proving that no positive A_c can work).

不构成完成：

- Reproving only f_c(n)→∞, or a bound no stronger than the existing removal-lemma lower bound.
- Reproducing the Fox–Loh upper construction, which does not decide a logarithmic lower bound.
- A result only for c=c(n), for a density tending to 1/4, or under minimum-degree/regularity hypotheses not present in the target.
- Finite computations without an exact finite certificate that implies the asymptotic statement.

正确性陷阱：

- Use the repaired domain 0<c<1/2; c>=1/2 makes the literal family empty.
- Keep c fixed before letting n tend to infinity, and state every dependence of constants on c.
- Check every edge of a proposed upper-bound graph, including retained auxiliary edges, lies in at least one triangle.
- Count common neighbors of an edge, not total triangles, average codegree, or triangles through a vertex.
- Do not infer a logarithmic lower bound from an n^{o(1)} upper bound or from qualitative divergence.
- At c=1/4 distinguish >= from > and account for rounding; the fixed-c hard regime is strictly below 1/4.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 修订后的对数下界是定义清楚、可独立审计的开放命题，但当前上下界间隔极大，且下界瓶颈与 triangle removal lemma 的困难定量问题紧密相关；适合进行证明优先的探索，不适合预期短期由计算解决。

支持理由：

- 目标可用边共同邻居数精确定义，正反两种完成条件均可检验。
- 存在明确的成熟构造和结构性工具，可产生可证伪的中间引理。
- c=1/4 以上已闭合，研究可集中在固定 c<1/4。

主要障碍：

- 已知下界仅为迭代对数级指数，而上界为次多项式，差距很大。
- 任何实质性普适下界可能需要超越当前 triangle-removal 定量框架的结构信息。
- 原“estimate”语言宽泛；只有选定对数下界等明确残余命题后才有二值完成标准。

Proof-first 路线：

- 寻找能把“每边至少一个三角形”和常数密度转化为更强局部重叠、可打包三角形或可删除边结构的精确引理；先证明引理的全称形式。
- 分别探索与 Fox–Loh 型稠密构造不兼容的下界路线，例如稳定性、局部覆盖/打包不等式或强化 removal 参数；每条路线须记录其对现有上界构造的兼容性。
- 唯一可选计算任务是针对预先写明的有限结构引理搜索反例，并给出顶点数界、枚举规范、证书和停止条件；不得把数值趋势当作渐近证明。

需要验证：

- 在开始新研究前，人工复核 2025–2026 的 MathSciNet、zbMATH、Google Scholar 引文链及 Fox、Loh、Potechin 作者主页。
- 若主张 c=1/4 的精确常数或严格不等式，须检查 Potechin 定理的整除/取整假设及 Khadzhiivanov–Nikiforov 原文。
- 任何声称改进下界的证明都须由独立审计者逐边检查量词、密度和三角形覆盖条件。

### 审计限制与人工复核理由

- 本审计进行了题号、精确标题、作者、近三年关键词、arXiv、作者/期刊页面和形式化关键词的定向公开检索，但公开检索不能证明不存在未索引、付费墙后或刚提交的解决。
- Khazhiivanov–Nikiforov 1979 原文未在本次审计中直接取得；其 c>1/4 结论由 Fox–Loh 原文及两个 Erdős Problems 记录交叉支持，且不决定 c<1/4 的开放状态。
- c=1/4 的线性量级结论依赖 Potechin 的阈值表述和取整处理；本审计不主张其最佳常数。
- “是否存在对数下界”作为残余目标由当前记录和检索结果支持，但仍应在正式攻关前用专业引文数据库做一次人工更新核查。

- 开放状态是基于近期数据库记录、可访问文献和定向未命中检索的高可信判断，而非穷尽性证明；建议人工查询 MathSciNet 和 zbMATH 的 Fox–Loh/Potechin 前向引文。
- 若研究要把 c=1/4 纳入精确常数结论，需人工核对 Potechin 与 1979 原文中的严格不等式、取整和有限 n 条件。

<!-- DEEP_REVIEW:END -->
