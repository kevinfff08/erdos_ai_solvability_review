# Problem 78

## 基本信息

- 原始链接: https://www.erdosproblems.com/78
- LaTeX 页面: https://www.erdosproblems.com/latex/78
- 原始状态: `open`
- 奖金: `$100`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`
- 形式化状态: `no`
- OEIS: `A059442`
- 原站备注字段: 无

## 原问题

Let $R(k)$ be the Ramsey number for $K_k$, the minimal $n$ such that every $2$-colouring of the edges of $K_n$ contains a monochromatic copy of $K_k$.

Give a constructive proof that $R(k)>C^k$ for some constant $C>1$.

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `46/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 题面含渐近/无限对象线索：\gg, o(
- 原记录含奖金 $100，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: chromatic, colouring, graph, ramsey
- 渐近/无限线索: \gg, o(
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选：GPT-5.5 级别模型很难直接给出满足 R(k)>C^k 的全新显式构造证明，但有现实机会在该问题上做出显著推进，例如系统化整理并验证现有构造的参数、尝试优化近年显式 Ramsey 图构造、形式化某些伪随机性到 clique/independent-set 上界的推导，或通过计算反例搜索发现可推广的构造模式。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 最可能的路线不是从零发明完整构造，而是围绕显式 Ramsey 图与伪随机对象展开：首先把题目等价转化为构造 n 点图且 clique/independent set 均为 O(log n)；然后复核备注中提到的 Cohen 和 Li 型构造，抽取其代数、有限域、谱图或加性组合结构；接着用自动化证明检查关键引理的参数损失，寻找能把已知多对数级上界推进到常数倍 log n 的瓶颈；并辅以 SAT/SMT、MILP、有限域搜索和启发式局部搜索生成小规模候选图，验证其 clique/independence 数和可扩展规律。

### 支持理由

- 题目目标有清晰的等价形式：显式构造 n 点图，使最大 clique 或 independent set 至多 c log n；这使计算验证、形式化证明和构造搜索都有明确判定指标。
- 备注显示已有显式构造已从较弱目标推进到多对数级别，说明问题附近存在可研究的具体技术路线，而非完全没有结构。
- GPT-5.5 级别模型适合做文献链梳理、参数追踪、证明重写、自动化实验设计和小规模构造验证，这些任务正好对应该问题的推进瓶颈。
- 该问题表述明确，且候选构造一旦给出，可用独立工具验证 clique/independence 数、谱性质和参数推导，降低了纯主观判断空间。
- 可计算部分相对明确：给定候选图族，可用 clique/independent-set 求解器、SAT 编码、谱界、半正定界或有限域枚举来验证有限规模证据。

### 主要障碍

- 核心目标要求显式构造达到真正指数 Ramsey 下界，即最大齐性集合 O(log n)；这与备注中的多对数级进展仍可能有本质差距。
- 已知随机图证明极其短，但去随机化该性质是长期困难问题；模型容易复述概率法而不能提供建设性对象。
- 若路线依赖有限域、加性组合、谱图、提取器或伪随机生成器，关键参数通常非常脆弱，少量 log 因子损失就会导致不能达到 C^k。
- 自动搜索只能覆盖小 n，容易产生不可推广的偶然构造；从实验图族抽象出无限族证明是主要难点。
- 形式化证明能验证候选构造的局部推导，但如果缺少新数学引理，形式化本身不能弥补核心构造缺口。

### 需要的验证

- 逐条复核备注中 Cohen 与 Li 构造的实际参数，确认它们离 O(log n) 的差距在哪里，以及是否存在可组合或可优化的参数环节。
- 对任何候选显式图族，必须给出多规模计算验证：最大 clique 数、最大 independent set、构造时间、边密度、谱特征和随机图基线对照。
- 关键不等式需要机器可检查的参数审计，特别是所有 log、常数、域大小、维度和递归层数的依赖关系。
- 若声称解决原题，必须明确给出常数 C>1、无限 k 范围的构造算法，以及严格证明该构造避免单色 K_k。
- 最好将候选证明中的组合引理、谱界或代数计数引理拆成可独立验证的 lemma，并用 Lean/Isabelle 或轻量证明检查脚本验证边界条件。

### 公开版思考摘要

这个问题对 AI 来说不是低价值的纯猜谜题，因为它有明确的等价构造目标、已有接近方向的线索和可计算的验证指标。GPT-5.5 级别模型配合工具，很可能能整理技术路线、定位参数瓶颈、验证现有构造、产生实验候选并形成部分推进；但直接完成完整构造性指数下界仍需要真正新的去随机化或显式伪随机图思想，因此不能评为高候选。

### 免责声明

以上是对 GPT-5.5 级别模型在该单一 Erdős 问题上的可推进性评估，不是该 Ramsey 构造问题的解答，也未声称给出了满足 R(k)>C^k 的构造性证明。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `revised_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_78.md](../../prompts/problem_78.md)

### 状态结论

题库当前页面及其论坛索引仍将第78题列为 open，且针对精确目标的检索未发现可核查的解决或反例。最新已核实的决定性进展是 Li 在 FOCS 2023 给出的显式 K-Ramsey 图，其中 K=log^{O(1)}N；这仍未达到 K=O(log N)。不过原文的“constructive proof”未规定算法模型：若只要求可计算而不要求效率，穷举图可把已知存在性结论机械化，因而会使题意失真。以下将尚存的、文献中通常意指的强显式版本作为修订后的开放目标。

### 当前规范陈述

修订后的标准目标（强显式版本）：存在绝对常数 c>0、N0，以及一个统一的确定性算法 A，使得对每个 N>=N0 和任意不同的 u,v∈[N]，A(N,u,v) 能在 poly(log N) 时间内判定简单图 G_N 中 uv 是否为边，并且 max{ω(G_N),α(G_N)}<c log₂N。等价地，对某个 C>1 及所有充分大的整数 k，该构造给出一个顶点数大于 C^k、且既无 k-团也无大小为 k 的独立集的图，从而 R(k)>C^k。α、ω 分别为独立数和团数。原题并未说明“constructive/explicit”究竟要求整张邻接矩阵的多项式时间输出、局部邻接关系的 polylog 时间判定，还是其他模型。

```text
Revised standard target (strongly explicit form). There exist absolute constants c>0 and N0, and a uniform deterministic algorithm A, such that for every N>=N0 and every distinct u,v in [N], A(N,u,v) decides whether uv is an edge of a simple graph G_N in time poly(log N), and max{omega(G_N), alpha(G_N)} < c log_2 N. Equivalently, for some C>1 and all sufficiently large integers k, this construction yields a graph on more than C^k vertices with neither a k-clique nor an independent k-set, hence R(k)>C^k. Here alpha and omega denote independence and clique number. The original wording does not state whether merely global polynomial-time output of the adjacency matrix, local polylogarithmic-time adjacency, or another notion of constructive/explicit is required.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `not_applicable`
- 检查说明: 未找到反驳强显式修订目标的简单图构造。相反，发现了原措辞的模型缺口：若不对“constructive”施加效率或简洁表示限制，有限穷举会把随机存在性结论转成可计算的家族，从而使字面请求不再表达公认开放问题。这是陈述修复问题，不是对标准强显式目标的反例。
- 版本变化: 1947 年 Erdős 用概率法证明了指数级存在性下界。2015/2016 年 Cohen 将显式 Ramsey 图的界推进到 K=2^{(log log N)^c}，其期刊版为 SIAM J. Comput. 2021。Li 的 FOCS 2023 工作进一步给出 K=log^{O(1)}N 的显式 Ramsey 图。没有检索到把指数 O(1) 降到 1、即 K=O(log N) 的可核查结果。原题的历史表述一直使用“constructive”，而现代文献已细分 explicit 与 strongly explicit；本审计将后者明示为可研究的修订目标。

陈述问题：

- “constructive proof”不是一个自足的复杂度定义。文献明确区分 explicit（可在 poly(N) 时间输出邻接矩阵）与 very/strongly explicit（可在 poly(log N) 时间判定邻接关系）；原题未选定其中之一。
- 原句省略“对所有充分大的 k”的量词，以及 C 必须是与 k 无关的绝对常数。
- 所谓“等价”的图表述也应明确图为有限简单无向图，且“没有大小至少 c log N 的团或独立集”表示 max{α,ω}<c log N；对整数阈值的取整只会改变常数。
- 若“constructive”仅表示存在某个可终止的确定性算法、没有资源限制，则可枚举所有 N 顶点图并检测 α、ω，以 Erdős 的存在性结果为终止保证。这不是该领域所称的显式 Ramsey 图构造，显示必须补充有效性模型。

需要固定的量词/约定：

- There must exist fixed absolute constants c>0 and N0; neither may depend on N, u, v, or k.
- The family/algorithm must work uniformly for every N>=N0 (or an explicitly specified cofinal size sequence with a padding reduction).
- For the Ramsey-number formulation, the lower bound is required for all sufficiently large integers k, not merely infinitely many k.
- The output graph is finite, simple, undirected, and loopless; alpha(G) and omega(G) are maximum cardinalities of an independent set and a clique.
- The repaired strong-explicit convention requires local adjacency computation in poly(log N) time. A weaker global-output convention must be explicitly approved if intended.

### 文献与当前边界

已核验的主要结果：

- Erdős（1947，同行评审）用概率法证明对角 Ramsey 数存在指数级下界；这给出存在性而非所需的显式家族。
- Cohen（STOC 2016；SIAM J. Comput. 2021，同行评审）构造 K=2^{(log log N)^c}-Ramsey 图，其中 c>0 为绝对常数。
- Li（FOCS 2023，同行评审）构造 K=log^{O(1)}N 的显式 Ramsey 图。该结果来自 O(log n) 最小熵双源提取器；O(log n) 中隐藏的常数会转化为 log N 的固定幂，故不等同于 K=O(log N)。
- Kocbek（2025，预印本）给出涉及 R(3,t) 的显式几何图构造，但其摘要所给结果属于非对角三角形自由情形，不能推出本题的对角强显式目标。

最近相关工作：就本问题的核心参数而言，最后一个已核实的直接改进是 Li 的 FOCS 2023 结果（预印本 arXiv:2303.06802）。检索了 2024–2026 的精确措辞、双源提取器和显式 Ramsey 图；发现的 2025 几何预印本不处理该对角 O(log N) 障碍，未发现可检查的解决声明。

剩余核心：在明确的统一有效性模型下，把已知显式家族的齐次数从 log^{O(1)}N 降至 O(log N)。在强显式版本中，邻接关系还必须能由顶点标签在 poly(log N) 时间内判定。若认可较弱的 explicit 模型，则必须先明确其复杂度与允许的表示；不能把无界穷举当成解决。

已使用方法：

- 概率法：证明典型随机图具有 O(log N) 级齐次数，但不能直接给出显式家族。
- 双源 disperser/extractor 到（双部再到非双部）Ramsey 图的归约；Cohen 和 Li 的主线方法。
- 代数/交集构造与伪随机对象；这些给出较早的显式界。
- 针对 R(3,t) 的有限几何和三角形自由构造；与本题相关但不直接解决对角情形。

争议或不确定性：

- 题目数据库的“open”是强证据但不是证明；页面和论坛正文因 403 无法直接抓取，状态部分依赖当期搜索索引。
- “constructive/explicit”没有单一跨文献定义。强显式、全局多项式时间显式、以及无复杂度限制的可计算性不可混用。
- 没有对 Li 的完整技术证明做逐引理复核；本审计只把其公开摘要与发表元数据所直接支持的 K=log^{O(1)}N 结论作为已核实事实。

### 证据来源

- [Erdős Problem 78](https://www.erdosproblems.com/78) — Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前题库检索结果将问题标为 OPEN，并给出目标、Cohen 与 Li 的进展摘要。直接打开页面及 LaTeX 页均受 403 限制，故页面正文以当前搜索索引为证据。
- [General Erdős Discussion](https://www.erdosproblems.com/forum/thread/General%20Erd%C5%91s%20Discussion) — Erdős Problems forum, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 论坛索引的 Ramsey theory 列表写有“3.49 - [78], open”。这是当前状态的辅助证据，不是数学证明。
- [A problem on constructive Ramsey bounds](https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/ConstructiveRamsey.html) — Paul Erdős problem collection; hosted by Fan Chung, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 历史问题页将目标表为 r(k)>(1+c)^k，并将其改述为构造无 c' log n 级团和独立集的图；它也记录了早期构造史。
- [Two-Source Dispersers for Polylogarithmic Entropy and Improved Ramsey Graphs](https://epubs.siam.org/doi/10.1137/16M1096219) — Gil Cohen, 2021; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 经同行评审的 Cohen 结果构造 K=2^{(log log N)^c}-Ramsey 图，严格改进此前显式界，但没有达到 K=O(log N)。
- [Two Source Extractors for Asymptotically Optimal Entropy, and (Many) More](https://arxiv.org/abs/2303.06802) — Xin Li, 2023-03-13; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 预印本摘要明确声称由 O(log n) 熵的双源提取器得到 N 顶点、K=log^{O(1)}N 的显式 Ramsey 图；页面显示最后修订为 2023-05-30。
- [Two Source Extractors for Asymptotically Optimal Entropy, and (Many) More](https://doi.org/10.1109/FOCS57990.2023.00075) — Xin Li, 2023-11-06; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. FOCS 2023 论文（页 1271–1281）是 Li 结果的同行评审发表版本；DBLP 和 IEEE 元数据交叉确认了发表身份。
- [Explicit geometric construction of Ramsey graphs](https://arxiv.org/abs/2507.09235) — Matija Kocbek, 2025-07-12; `preprint`, `preprint`, directness=`indirect`, reliability=`medium`. 2025 年相关预印本研究的是几何构造及特别的 R(3,t) 构造性界；摘要没有声称解决对角显式 O(log N)-Ramsey 图问题。
- [Some Remarks on the Theory of Graphs](https://doi.org/10.1090/S0002-9904-1947-08785-1) — Paul Erdős, 1947; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. Erdős 1947 的原始论文是概率法指数 Ramsey 下界的历史来源，说明存在性与显式构造之间的差距。
- [Ramsey Graphs from Boolean Function Representations](https://www.cs.umd.edu/~gasarch/TOPICS/CRT/GopRam.pdf) — Parikshit Gopalan, 2014; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 该文清楚区分 explicit：poly(|V|) 时间得到邻接矩阵，和 very explicit：poly(log |V|) 时间计算邻接关系；这直接支持原题“constructive”的模型歧义。

### 完成标准

- 肯定出口: For the repaired strong-explicit target: exhibit absolute constants c>0 and N0 and prove that a single deterministic local algorithm constructs, for every N>=N0, a simple graph G_N with max{alpha(G_N),omega(G_N)}<c log_2 N and the declared poly(log N) adjacency runtime. Derive explicitly that this implies R(k)>C^k for a fixed C>1 and every sufficiently large k.
- 否定出口: For the repaired target, give a rigorous impossibility theorem in the declared construction model showing that no uniform strongly explicit family can have max{alpha(G_N),omega(G_N)}=O(log N), or show that the target/model is inconsistent. For the audit itself, a decisive alternative is a source-backed determination that the intended model was only unbounded computability, in which case exhaustive search plus the probabilistic existence theorem settles that weaker reading.

不构成完成：

- A probabilistic existence proof without a uniform deterministic construction.
- A family that works only for finitely many N or has constants depending on N or k.
- A construction with K=log^d N for an unspecified fixed d>1; this is existing-type progress, not K=O(log N).
- An algorithm that brute-forces all graphs unless the approved statement explicitly permits unbounded running time.
- A bipartite monochromatic-submatrix construction without a correct, parameter-preserving reduction to an undirected graph.
- Empirical clique/independent-set searches on finite instances without a uniform proof.

正确性陷阱：

- Verify both omega(G_N) and alpha(G_N); bounding only one is insufficient because complementation swaps them.
- Track the base and constants in every logarithm and in the conversion from N to k.
- Check that the construction is uniform and that adjacency is symmetric, loopless, and defined for every claimed N.
- If using an extractor/disperser, prove the exact source-entropy, error, and rectangle-to-clique/independent-set implication; O(log n) entropy generally yields log^{O(1)}N, not automatically O(log N).
- Do not confuse an explicit global adjacency-matrix algorithm with a strongly explicit local adjacency algorithm.
- Check the quantifier 'for all sufficiently large k', rather than an infinite subsequence.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `5/100`
- 信心: `high`
- 结论: 对经明确化的强显式剩余目标，AI 独立完成解决的可能性很低；它更适合做精确定义审计、参数追踪、归约复核和候选引理验证。

支持理由：

- 目标一旦固定为强显式形式，结论可精确核验：给出算法、运行时间、以及对 α 和 ω 的统一上界即可。
- 已有深厚的提取器/分散器文献提供了可比较的基线和可审计的参数链。
- Li 的结果将问题压缩为从 log^{O(1)}N 到 O(log N) 的明确但极具挑战性的参数缺口。

主要障碍：

- 这是一项长期著名开放问题；已知进展依赖先进的双源提取器、非可篡改提取器及复杂伪随机性技术。
- 隐藏在 O(log n) 与 log^{O(1)}N 中的常数是核心障碍，而不是可由有限计算外推的现象。
- 若未先固定 explicit/strongly-explicit 模型，任何“解答”都可能只是语义规避。

Proof-first 路线：

- 先从 Li 的已发表/公开版本抽取完整的“提取器参数→双部 Ramsey→非双部 Ramsey”定理链，定位恰好造成 log^{O(1)}N 的损失。
- 独立寻找不经双源提取器的强显式候选，并首先证明一个能同时控制团和独立集的可检验引理。
- 审查是否存在能把仅在特定 N 的构造推广到全部充分大 N 的无损填充或乘积引理；必须保留 O(log N) 阈值。

需要验证：

- 人工确认本题奖励方接受的“constructive/explicit”运行时间模型；该选择决定是否采用强显式目标。
- 逐定理检查 Li 的 FOCS 2023 版本的构造性、误差和 Ramsey 参数，而非只依赖摘要。
- 在正式研究前补做 2026 年余下月份及作者主页/会议论文的状态刷新。

### 审计限制与人工复核理由

- 网页工具无法直接打开 Erdős Problems 的主页面、LaTeX 页面和论坛页面（403）；对它们的当前状态使用了同日搜索索引，因而状态置信度为中等而非绝对。
- 没有下载并逐行审计 Cohen、Li 的完整证明；对其结果只报告公开摘要、出版元数据和明确可见的定理摘要所支持的范围。
- 2026-07-27 后的工作不在审计范围内；且任何未被主流检索索引的私人稿件都可能遗漏。
- “强显式”是为使问题可形式化而采用的保守修订。奖励方若接受较弱的 global-explicit 定义，需人工调整规范和完成测试。

- 需由题目维护者或领域专家确认“constructive proof”所要求的计算模型：global explicit、strongly explicit，或其他定义。
- 在把 Li 2023 作为严格基线前，应由人工阅读全文核对其显式性、常数和从提取器到非双部 Ramsey 图的归约。
- 由于当前题库与论坛正文无法直接获取，若此审计将用于正式状态变更，应人工打开页面复核其最新标签与讨论。

<!-- DEEP_REVIEW:END -->
