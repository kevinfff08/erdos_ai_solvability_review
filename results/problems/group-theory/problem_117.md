# Problem 117

## 基本信息

- 原始链接: https://www.erdosproblems.com/117
- LaTeX 页面: https://www.erdosproblems.com/latex/117
- 原始状态: `open`
- 奖金: `no`
- 主类别: `group theory`
- 原始标签: `group theory`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $h(n)$ be minimal such that any group $G$ with the property that any subset of $>n$ elements contains some $x\neq y$ such that $xy=yx$ can be covered by at most $h(n)$ many Abelian subgroups.

Estimate $h(n)$ as well as possible.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `30/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 目前只能依靠通用数学推理、文献归纳和特殊情形探索

### 主要障碍

- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: 无
- 有限/计算线索: 无
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **GPT-5.5 级别模型配合计算群论、图论优化、形式化证明和文献检索工具，较可能对该问题做出局部推进或验证性贡献，例如改进常数、整理等价图论表述、计算小规模极值例子、验证候选构造；但要给出接近最优的总体渐近估计仍很困难。整体判断为低到中等候选。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 把条件解释为非交换图的团数至多 n，把覆盖 Abelian 子群的问题转化为用交换子群覆盖群元素的结构问题；先复核 Pyber 指数上界与 Isaacs 型下界的证明框架，再用 GAP/Magma 枚举有限群和非交换图，寻找小 n 的 h(n) 或下界构造；同时尝试把证明中的 Ramsey 型、中心商有限性、共轭类或中央化子参数常数显式化，争取改进指数底数或提出可验证的中间定理。

### 支持理由

- 问题已有指数上下界，说明核心现象和基本证明框架存在，AI 可从现有框架中做常数优化、形式化拆解和边界案例验证。
- 条件天然适合计算辅助：可对有限群构造非交换图，计算最大两两不交换集合、Abelian 子群覆盖数或其上下界。
- 形式化证明工具可帮助检查从“无大非交换子集”到“有限个 Abelian 子群覆盖”的结构性引理，减少复杂组合群论证明中的漏洞。
- 该问题目标是“尽可能估计”，不一定要求完全精确解；因此局部改进、显式常数、小 n 精确值和新构造都算有意义推进。

### 主要障碍

- 问题属于组合群论中的结构极值问题，现有结果只有指数级夹逼，若要显著缩小指数底数或确定正确增长率，可能需要新的群结构洞察。
- Abelian 子群覆盖数不是单纯的图论覆盖数；候选覆盖必须来自真实子群，导致计算搜索和理论转化都受群结构约束。
- 一般群可能无限，计算实验只能直接覆盖有限群或有限商，需要额外论证说明这些实验对原问题有代表性。
- 下界构造和上界证明可能由不同机制控制，AI 容易分别优化局部参数但难以统一成真正接近最优的渐近估计。

### 需要的验证

- 检索并核对 Pyber 证明中的精确依赖关系，确认当前最好上下界与常数是否仍是该 JSON 所述水平。
- 用 GAP/Magma 对小阶有限群计算最大非交换集大小和 Abelian 子群覆盖数，独立验证小 n 数据。
- 对任何新下界构造，必须证明其满足最大非交换子集大小至多 n，并严格计算所需 Abelian 子群覆盖数。
- 对任何新上界，必须形式化或人工复核关键群论引理，尤其是从有限中央化子结构到 Abelian 子群覆盖的步骤。
- 检查无限群情形是否可安全归约到有限商或有限生成子结构，避免只证明了有限群版本。

### 公开版思考摘要

这个问题有较清晰的工具切入点：非交换图、中央化子、Abelian 子群覆盖和有限群枚举都能被计算与形式化工具辅助。GPT-5.5 级别模型有希望复现并细化已有指数界、发现小规模模式、提出可检验的新构造或改进常数。但问题的主目标是渐近估计，当前信息显示距离精确增长率仍有实质理论缺口，因此不宜评为高候选。

### 免责声明

以上只是对 AI 工具辅助可推进性的审查，不是该 Erdős 问题的解答，也没有声称给出了新的上下界。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `needs_human_clarification`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_117.md](../../prompts/problem_117.md)

### 状态结论

现有直接记录仍将 #117 标为 open，且截至审计日未检得可核验的解决或反例。Pyber 已给出 h(n) 的指数型上下界；但“尽可能好地估计”没有指定要优化的常数、极限、渐近等价式或精确值，故它是仍开放的定量研究纲领，而非有唯一完成判据的单一命题。

### 当前规范陈述

对每个整数 n >= 1，令 alpha(G) 为群 G 中两两不交换的元素集合 S 的最大可能基数（即任意不同 x,y 属于 S 均有 xy != yx）。条件 alpha(G) <= n 等价于 G 的每个多于 n 个元素的子集均含一对不同的可交换元素。令 beta(G) 为以有限个 Abel 子群并覆盖 G 所需的最小个数。定义 h(n) 为满足下述条件的最小整数 H：对每个 alpha(G) <= n 的群 G，都有 beta(G) <= H（在已知其有限后，等价于该类 beta(G) 的上确界）。问题是确定 h(n)，或明确选择并证明 h(n) 的一个尖锐渐近不变量。

```text
For each integer n >= 1, let alpha(G) be the supremum of |S| over subsets S of a group G such that xy != yx for every two distinct x,y in S. Equivalently, alpha(G) <= n means that every subset of G with more than n elements contains two distinct commuting elements. Let beta(G) be the least cardinality of a finite family A of abelian subgroups of G whose union is G. Define h(n) to be the least integer H such that beta(G) <= H for every group G with alpha(G) <= n (equivalently, the supremum of beta(G) over that class, once finiteness is known). Determine h(n), or state and prove a specifically chosen sharp asymptotic invariant of h(n).
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定上述规范化定义的简单构造。特别地，针对无限群的潜在漏洞由 Neumann 1976 的 centre-by-finite 结果消除；而 h(n) 的有限指数上界由 Pyber 1987 及数据库记录支持。此结论不是对所有可能改写的穷尽性检验。
- 版本变化: Erdős Problems 的 #117 历史页仅显示 2025-10-20 的段落格式调整，与当前文本的数学内容相同；未发现把原问题改成不同命题的修订。Erdős 1997 的原始表述亦使用等价的“至多 n 个两两不交换元素”语言。

陈述问题：

- “h(n) be minimal” 的作用域未写明；规范化后应是对所有满足 alpha(G) <= n 的群的统一最小上界，而不是对单个 G 的覆盖数。
- 原文未说明 n 的范围；取 n >= 1 可避开 n=0 时“多于 0 个元素的任意子集”包含单元素集而无法含不同元素对的退化问题。
- “群”包括无限群并不造成矛盾：Neumann 的定理将 alpha(G)<无限 的情形归约到中心有限指数的群；但这一归约应在工作中明说。
- “Estimate h(n) as well as possible”未给出唯一完成标准。精确值、最佳常数、limsup/liminf 指数率、Theta 型界或显式可改进界均是不等价目标。
- Erdős 1997 的原始措辞是“at most n elements which do not commute pairwise”；数据库的子集表述与其等价，无实质转录冲突。

需要固定的量词/约定：

- n ranges over integers n >= 1.
- The quantifier over G is universal: one bound H must work simultaneously for every group with alpha(G) <= n.
- A cover is a finite family of abelian subgroups; repetitions are irrelevant and subgroups need not be proper, maximal, normal, or distinct.
- The condition is pairwise: for every distinct x,y in S, xy != yx. It is not a condition on a single noncommuting pair.
- For a nonabelian group, beta(G) equals the chromatic number of its noncommuting graph after central elements are handled; this is an interpretation, not an additional hypothesis.
- The phrase 'as well as possible' must be replaced by a selected target before a resolution can be certified.

### 文献与当前边界

已核验的主要结果：

- Neumann（1976，同行评审）证明：不存在无限两两不交换子集，当且仅当 |G:Z(G)| 有限。这使原题中无限群的研究可约至有限中心商。
- Pyber（1987，同行评审）证明：若 alpha(G) <= n，则 |G:Z(G)| <= c^n，其中 c 为绝对常数。原问题数据库及 Erdős 1997 的扫描本进一步明确记录：存在 c2>c1>1，使 c1^n < h(n) < c2^n；扫描本将下界归于 Isaacs，但本审计未找到可直接核对该归属的原始论文。
- 对任意中心有限指数群，按 G/Z(G) 的每个陪集选代表元 g；子群 <Z(G),g> 是 Abel 的并覆盖该陪集。因此 beta(G) <= |G:Z(G)|，解释了 Pyber 的中心指数定理如何提供 h(n) 的指数上界。
- Brown（1988、1991）对对称群的 Abel 覆盖数和最大两两不交换集合给出最佳渐近界，并显示两种参数在 n>=15 时并不总相等；这说明不能把 h(n) 不加证明地替换成最大 clique 数。
- Azad–Iranmanesh–Praeger–Spiga（2010 预印本，后有期刊版本）对 GL_n(q) 构造覆盖所有元素的 Abel 子群族，并在 q>n 时给出 alpha(GL_n(q)) 的精确公式；这是特定家族进展，不是 h 的全局优化。

最近相关工作：检得 Yang–Zarrin（2025，Bull. Aust. Math. Soc.）研究高阶 r-非交换集合与群结构。它引用 Pyber，但其可查摘要没有给出 h(n) 的改进界。结合截至 2026-07-27 的针对性检索，未发现 2023–2026 年可核验的论文、预印本、作者主页或形式化工件声称确定 h(n)、改进其全局指数率，或推翻已知界。

剩余核心：已知 h(n) 仅在“某个底数的指数函数”意义下确定。剩余核心必须由委托方选定，例如：确定 h(n) 的精确值；确定 limsup/liminf (log h(n))/n 并证明二者相等；给出明确的改进底数；或对一个指定的群类求尖锐界。原文“尽可能好”本身不选择其中任何一个。

已使用方法：

- 中心有限指数归约及对 G/Z(G) 的结构控制。
- 将两两不交换集合视为非交换图 clique，将 Abel 覆盖视为图着色/独立集分割；必须注意该图论翻译和中心元素的处理。
- 有限群的结构论、中心化子与最大 Abel 子群计数。
- 在具体群族中构造显式 Abel 覆盖，或构造两两不交换见证集以夹逼参数。
- 使用对称群、一般线性群、p-群等测试家族来建立下界或检验候选常数。

争议或不确定性：

- Erdős 1997 对下指数界的“already known to Isaacs”归属没有给出本 JSON 可核验的具体引文；不得将其升级为已验证的 Isaacs 定理陈述。
- Pyber 原文的可访问出版商摘要直接陈述中心指数界；完整论文正文未在本审计中开放逐页检查。h(n) 的指数双边界由当前问题页和原章扫描本共同报告，因而可信但对其最佳常数不能作更强断言。
- 未检得解答不是不存在解答的逻辑证明；当前开放状态依赖 2026 年更新的数据库记录与多轮定向检索。
- 没有检得 #117 的 Lean/Mathlib/FormalConjectures 工件；这只是检索结果，不是对所有代码托管平台的穷尽证明。

### 证据来源

- [Erdős Problems 117](https://www.erdosproblems.com/117) — Thomas F. Bloom / Erdős Problems, 2026-01-23; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前数据库仍标记为 OPEN，无评论中的解答声明，并记录 Pyber 的指数型上下界和未形式化状态。该记录是当前状态证据而非解答证明。
- [Erdős Problems 117 LaTeX source](https://www.erdosproblems.com/latex/117) — Thomas F. Bloom / Erdős Problems, unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 核对了数据库的 LaTeX 版本；其问题与给定 JSON 一致。
- [Revision history of Erdős Problem 117](https://www.erdosproblems.com/history/117) — Thomas F. Bloom / Erdős Problems, 2025-10-20; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 显示可见修订仅为排版，当前陈述和指数型界的说明未发生数学性改变。
- [The Number of Pairwise Non-Commuting Elements and the Index of the Centre in a Finite Group](https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/jlms/s2-35.2.287) — László Pyber, 1987-04; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 摘要直接证明：若有限群至多有 n 个两两不交换元素，则 |G:Z(G)| <= c^n（某绝对常数 c）。这是 #117 指数上界的核心结构性输入；结合每个中心陪集由一个含 Z(G) 的循环扩张 Abel 子群覆盖，可得到指数型 Abel 覆盖上界。
- [A problem of Paul Erdős on groups](https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/problem-of-paul-erdos-on-groups/43D46201BABB2E6319B72C008DC3F42B) — B. H. Neumann, 1976-06; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明“没有无限两两不交换集合”的群恰为中心有限指数群，为处理原题允许无限群提供归约。
- [Paul Erdős: Some Unsolved Problems](https://www.cambridge.org/core/books/abs/combinatorics-geometry-and-probability/paul-erdos-some-unsolved-problems/3B3C2C2B6FBE588B0E5C36C8598003FF) — Paul Erdős, 1997; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原始问题出处及其 1997 年书章元数据。
- [Combinatorics, Geometry and Probability: A Tribute to Paul Erdős](https://rexresearch1.com/ErdosMath/Combinatorics%2C%20Geometry%20and%20Probability%20A%20Tribute%20to%20Paul%20Erd%C3%B6s.pdf) — Béla Bollobás and Andrew Thomason (editors); chapter by Paul Erdős, 1997; `other`, `unknown`, directness=`direct`, reliability=`medium`. 可检阅的扫描本给出第 26 个群论问题的原始措辞：以两两不交换集合的大小定义 h(n)，并称 Pyber 已给出某些正指数界、下界已为 Isaacs 所知。作为原章的可访问副本使用；Isaacs 下界的具体原始出处尚未核实。
- [Abelian coverings of finite general linear groups and an application to their non-commuting graph](https://arxiv.org/abs/1004.3402) — A. Azad, M. A. Iranmanesh, C. E. Praeger, P. Spiga, 2010-04-20; `preprint`, `preprint`, directness=`indirect`, reliability=`medium`. 给出 alpha(G) 的图论解释、Neumann 的有限归约、Pyber 型 |G:Z(G)| 与 alpha(G) 的指数关系，并对 GL_n(q) 构造 Abel 覆盖及精确 clique 结果。它提供已用方法与代表性家族结果，但不解决 h(n) 的全局最优估计。
- [The Number of Pairwise Noncommuting Sets in a Finite Group](https://doi.org/10.1017/S0004972724001370) — Yong Yang and Mohammad Zarrin, 2025-02-17; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 这是检索到的近期相邻研究：研究 r-非交换集合及其对群结构的影响。其摘要没有声明 h(n) 的更优全局界或解答，因此不能作为 #117 已解决的证据。

### 完成标准

- 肯定出口: After the sponsor selects one target, a complete affirmative resolution must prove that target for the canonically defined h(n): for example, give an exact formula for every n; or prove a stated sharp asymptotic h(n)=exp((lambda+o(1))n) with a specified lambda; or prove an explicitly stated universal upper/lower bound that strictly improves the previously certified one, together with all quantifiers over groups.
- 否定出口: For the present broad wording, the decisive negative audit outcome is to demonstrate that no single proposed theorem follows from the phrase 'estimate as well as possible': at least two inequivalent candidate completion criteria remain compatible with all accepted facts, and no source specifies one. The statement must then be repaired by selecting a target rather than declared solved or disproved.

不构成完成：

- Reproving only that h(n) is finite, or only restating Neumann's centre-by-finite theorem.
- Reproving Pyber's unspecified exponential-order estimate without a sharper selected result.
- Calculating beta(G) or alpha(G) for finitely many groups without a theorem connecting those computations to a universal bound for h(n).
- Proving a result only for finite groups without explaining the reduction from arbitrary groups.
- Showing a cover by arbitrary subsets, cosets, cyclic sets, or nonabelian subgroups rather than abelian subgroups.
- Treating alpha(G) and beta(G) as equal merely because alpha(G) <= beta(G).

正确性陷阱：

- Quantifier inversion: h(n) is a uniform worst-case parameter, not beta(G) for one chosen group.
- A maximal-by-inclusion noncommuting set need not have maximum cardinality; use alpha(G) correctly.
- A set of elements that each fail to commute with a fixed element is not necessarily pairwise noncommuting.
- A cover of G/Z(G) by abelian subgroups does not automatically lift to an abelian cover of G without checking commutators; the safe elementary cover used above is by <Z(G),g> over coset representatives.
- Central elements must not be accidentally deleted when translating to the usual noncommuting graph on G minus Z(G).
- Bounds on |G:Z(G)|, alpha(G), and beta(G) are distinct parameters; every implication and exponential conversion needs proof.
- Any asserted optimal base requires both matching global upper and lower bounds under the same n normalization.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `15/100`
- 信心: `medium`
- 结论: 在未选定完成标准前，不应将其交给求解代理作为单一“已良定的开放命题”。若人类将目标收窄为明确的指数率或特定群类上的尖锐定理，它是低概率但可开展的结构群论项目；当前总体解决概率低。

支持理由：

- 对象 h(n) 可精确定义，且 Neumann/Pyber 给出了坚实的归约和指数级基线。
- 存在可独立核验的中间引理与代表性群族，适合以证明为先的探索。
- 近期文献仍在研究相关非交换参数，说明方法生态并未停滞。

主要障碍：

- 原请求没有唯一的成功条件；任何“更好”的界都可能是进展而非终局。
- 最坏情形跨越所有有限群，可能需要深层有限群结构而非局部计算。
- 已知结果已有四十年历史而仍未见全局锐化的可核验证据，提示存在真实技术障碍。
- 小群枚举对全局指数常数缺乏可靠外推能力。

Proof-first 路线：

- 先由人类选定精确命题，例如存在并确定指数率 lambda，或针对指定群类的最优 beta–alpha 关系；随后审计 Pyber 证明中损失最大的步骤。
- 并行寻找能给出 beta(G) 相对 alpha(G) 大比值的结构家族，以及可降低通用上界的覆盖构造；两条路线只能在同一 n 规范下比较。
- 可选计算仅用于一个预先声明的引理：在明确的有限群族和参数范围内，验证候选覆盖/见证集并生成可复查证书；达到设定范围后立即停止。

需要验证：

- 获取并逐项审读 Pyber 1987 正文，以区分其对中心指数与 Abel 覆盖数的所有显式常数和构造。
- 定位或修正 Isaacs 下界的原始出处。
- 在选定目标前，检索 MathSciNet/zbMATH、arXiv 和主要作者近年论文目录，以排除未被通用搜索索引的改进。
- 若声称新界，须由独立证明审计者检查无限群归约、覆盖确为 Abel 子群及全部指数常数。

### 审计限制与人工复核理由

- 本审计严格只使用给定问题 JSON 作为仓库输入，并使用公共网络来源；未读取任何其他仓库问题。
- Pyber 1987 的出版商摘要可直接检查，但全文在本次浏览条件下未逐页获得；关于 h(n) 双指数界依赖当前问题页与可访问的 Erdős 章节扫描本的共同记录。
- 未能定位 Erdős 所称 Isaacs 下界的原始书目，因此没有把该归属作为已独立验证的定理。
- 公共搜索、arXiv 检索和可见形式化搜索不能逻辑排除未索引的新稿、私人通信或未公开形式化；故状态置信度为 medium 而非 high。
- “尽可能好”没有客观停止条件；本审计能确认函数与已知量级，不能替人类选择未来项目的成功标准。

- 需要人类选择精确的后续研究目标（精确 h、指数率、显式常数或受限群类），否则不存在唯一的“解决”判据。
- 应由具有数据库或全文访问权限的专家复核 Pyber 1987 的完整证明、具体常数和 Isaacs 下界的原始出处。
- 若后续代理声称近年解决或改进，须在提交前进行独立文献检索及严格证明审计。

<!-- DEEP_REVIEW:END -->
