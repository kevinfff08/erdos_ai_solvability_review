# Problem 86

## 基本信息

- 原始链接: https://www.erdosproblems.com/86
- LaTeX 页面: https://www.erdosproblems.com/latex/86
- 原始状态: `open`
- 奖金: `$100`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `no`
- OEIS: `A245762`
- 原站备注字段: 无

## 原问题

Let $Q_n$ be the $n$-dimensional hypercube graph (so that $Q_n$ has $2^n$ vertices and $n2^{n-1}$ edges). Is it true that every subgraph of $Q_n$ with\[\geq \left(\frac{1}{2}+o(1)\right)n2^{n-1}\]many edges contains a $C_4$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `34/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 题面含渐近/无限对象线索：o(
- 原记录含奖金 $100，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 with computation/formalization/literature/反例搜索工具`
- 结论: **不太可能由模型直接完整解决，但有中等偏低概率显著推进：尤其适合做有限维精确计算、整数规划/SDP/旗代数式证书搜索、构造族验证和已知上界证明的形式化重建。要把上界从约 0.60318 推到 1/2+o(1) 仍需要新的极值组合思想，不能主要依赖暴力计算。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 较现实的路线是把问题转化为超立方体二维面上的局部约束优化：C4 对应二维子立方体的完整四边形，因此可建立按坐标层、边方向、局部配置统计的线性/半正定约束；用计算搜索潜在不等式证书，验证小 n 的 f(n)，寻找接近下界的构造模式，并尝试把有限局部证书推广为渐近上界。形式化证明工具可用于核验局部计数恒等式和机器生成证书。

### 支持理由

- 问题结构高度离散且局部：超立方体的 C4 与二维子立方体直接相关，适合编码为整数规划、局部密度约束或证书搜索。
- 已有上界 0.60318 与猜想 0.5 之间仍有明显但不是完全无结构的缺口，模型可尝试复现并改进局部不等式。
- 下界为 1/2 加低阶项，说明猜想常数很可能由精细结构控制；计算实验可能帮助识别极值构造和稳定性现象。
- 形式化证明和可检查证书有用：若得到局部-全局型不等式，可由 proof assistant 或独立验证器降低错误风险。

### 主要障碍

- 从 0.60318 降到渐近 1/2 可能需要新的全局稳定性或容斥/熵型论证，单纯局部约束可能不足。
- n 维超立方体规模指数增长，有限维精确 f(n) 很快不可直接计算，必须利用对称性与可推广证书。
- C4-free 约束虽局部，但极值构造可能利用跨许多坐标的全局相关性，模型容易误把小 n 模式当成渐近规律。
- 当前问题未形式化，任何机器辅助证明都需要先严格定义超立方体、子图、C4-free、渐近 o(1) 语义和计数归一化。

### 需要的验证

- 复现题述中的已知下界和 0.60318 上界框架，确认归一化常数与 f(n) 定义无误。
- 对小 n 建立独立可验证的精确或上下界计算，最好使用多种方法交叉检查，例如 SAT/ILP 与穷举对称化。
- 若产生计算证书，需要给出可审计的有理系数证书、误差界和从有限局部配置到所有 n 的推广证明。
- 需要检查候选证明是否真的排除所有 C4，而不只是排除二维面中的某类局部配置；并验证 o(1) 项处理没有隐藏固定 n 假设。

### 公开版思考摘要

这个问题对 AI 工具并非完全不适合，因为它有清楚的有限组合模型、自然的局部约束和可计算证书入口。GPT-5.5 级模型较可能在复现已有界、搜索新不等式、生成并验证小规模数据、提出稳定性猜想方面有实际价值。但完整证明渐近最优常数 1/2 需要把局部计算提升为统一的全局极值论证，难度明显高于常规自动定理证明或反例搜索。

### 免责声明

以上是对该问题 AI 辅助可推进性的审查，不是问题 86 的证明或反例，也不声称给出了新的上界或确定了 f(n)。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_86.md](../../prompts/problem_86.md)

### 状态结论

该渐近猜想很可能仍然开放：已核实的公开结果给出下界密度趋于 1/2，以及上界 0.60318，但没有找到把上界降至 1/2 的证明或固定正密度反例。2026 年的预印本只改进了 Q7、Q8 的有限维下界，明确不是渐近解决。官方数据库仍标为 open，但其问题页早于该预印本；因此结论为 likely_open 而非绝对确认。

### 当前规范陈述

对 n>=1，令 Q_n 的顶点集为 {0,1}^n；当且仅当两个顶点恰在一个坐标不同，它们相邻。因此 e(Q_n)=n2^(n-1)。令 f(n)=max{e(G)：G 是 Q_n 的生成子图且不含简单四环 C_4（不要求为诱导四环）}。规范目标是：对任意 epsilon>0，存在 N，使得所有 n>=N 均有 f(n)<= (1/2+epsilon)e(Q_n)。等价地，对每个 epsilon>0，当 n 足够大时，Q_n 的任一边数严格大于 (1/2+epsilon)e(Q_n) 的子图都含 C_4。由标准平均论证该密度极限存在，且已知构造给出极限下密度 1/2；故亦等价于 pi_e(C_4)=lim f(n)/e(Q_n)=1/2。

```text
For n>=1 let Q_n have vertex set {0,1}^n, with xy an edge iff x and y differ in exactly one coordinate; hence e(Q_n)=n2^(n-1). Let f(n)=max{e(G): G is a spanning subgraph of Q_n containing no (not necessarily induced) copy of the simple cycle C_4}. Prove that for every epsilon>0 there is N such that, for every n>=N, f(n)<= (1/2+epsilon)e(Q_n). Equivalently, every subgraph G of Q_n with e(G)>(1/2+epsilon)e(Q_n) contains a C_4, for all sufficiently large n (depending on epsilon). Since f(n)/e(Q_n) has a limit by the standard averaging argument and known constructions give limiting lower density 1/2, this is equivalently pi_e(C_4):=lim_{n->infinity} f(n)/e(Q_n)=1/2.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 针对字面中的渐近版本，已核对 BHN95 的较密下界：其相对密度为 1/2+Theta(n^-1/2)，仍是 1/2+o(1)，故不是反例。未找到固定 delta>0 的 C_4-free 子图族，从而否定 pi_e(C_4)=1/2。有限维 Q7、Q8 的新构造同样不能构成渐近反例。
- 版本变化: 历史上 Erdős 的相关更强版本曾被 BHN95 的下界否定；1991 年综述所记录的“略多于一半边强迫 C4”的 epsilon-渐近版本仍是此处的规范目标。BHN95 改进了下界；Thomason–Wagner、BHLL14 和 Baber 依次改进上界。2026 年 Minamoto 预印本给出 Q7、Q8 的可复核有限下界，但没有替换或解决渐近目标。

陈述问题：

- 原句“至少 (1/2+o(1))n2^{n-1} 条边”没有量化 o(1)，也未说明临界处的严格/非严格不等号；孤立地读并不是一个唯一的有限 n 命题。
- 原句的“子图”通常可理解为任意边子集（顶点集可补全为 Q_n 的全顶点集），但应明说；“含 C_4”指非诱导的简单 4-环。
- 原输入 remarks 已以 f(n)<= (1/2+o(1))e(Q_n) 的形式给出意图，足以唯一恢复上述标准渐近命题；没有发现会推翻该规范版本的简单反例。
- BHN95 摘要所说“disproves one version”指向 Erdős 的另一种更强表述；其 1/2+Theta(n^-1/2) 下界仍与本题的 1/2+o(1) 渐近猜想相容。

需要固定的量词/约定：

- Interpret f(n)<= (1/2+o(1))e(Q_n) as: for every epsilon>0, there exists N such that for all n>=N, f(n)<= (1/2+epsilon)e(Q_n).
- The forcing formulation must use a strict edge threshold > (1/2+epsilon)e(Q_n); equality conventions at a finite n are irrelevant to the asymptotic claim but must not be silently reversed.
- C_4-free means no subgraph isomorphic to C_4, not merely no induced C_4 and not merely no selected coordinate-square under an unstated convention.
- Because every 4-cycle in Q_n is a coordinate square, checking all coordinate pairs and base vertices is equivalent to checking all C_4 copies.

### 文献与当前边界

已核验的主要结果：

- Erdős 的 1991 综述将该问题表述为：对每个 epsilon>0，略多于 Q_n 一半的边应强迫 C4；这是当前规范目标的历史来源。
- Brass–Harborth–Nienborg（J. Graph Theory, 1995，同行评审）构造了 C4-free 子图：当 n=4^r 时 f(n)>=1/2(n+sqrt(n))2^(n-1)，并对所有 n>=9 给出 1/2(n+0.9sqrt(n))2^(n-1)。归一化后均为 1/2+o(1)，所以支持而非反驳本渐近猜想。
- Thomason–Wagner（Discrete Mathematics, 2009，同行评审）把已知渐近上界降至 0.62256。
- Balogh–Hu–Lidický–Liu（European Journal of Combinatorics, 2014，同行评审）以改造的 flag algebra 方法证明 C4-free 边 Turán 密度至多 0.6068。
- Baber（arXiv:1201.3587v2，2012，未同行评审）用扩展的 flag algebra / partially defined hypercube 技术把上界进一步降至 0.60318。
- Minamoto（arXiv:2603.29127v4，2026-05-13，预印本）给出可逐个检验的有限维构造 ex(Q7,C4)>=304 和 ex(Q8,C4)>=680；它们不改变已知的渐近密度区间。

最近相关工作：截至审计日，最直接的新工作为 Minamo Minamoto 的 2026 预印本 arXiv:2603.29127v4。其边表和脚本可验证有限下界，但论文和配套仓库都没有给出 Q7/Q8 的上界证明，更没有给出 f(n)<= (1/2+o(1))e(Q_n) 的渐近证明。

剩余核心：证明 pi_e(C4)<=1/2，即排除任意固定正密度裕量：对每个 epsilon>0，所有充分大的 Q_n 的 C4-free 子图都至多有 (1/2+epsilon)e(Q_n) 条边。已知 BHN 下界意味着这将精确确定 pi_e(C4)=1/2。相反，若构造无穷维序列使密度至少 1/2+delta（某个固定 delta>0），则可否定该猜想。

已使用方法：

- 代数/组合构造及对坐标方向的编码式安排，用于超过 1/2 的次主项下界。
- 对超立方体局部配置的 flag algebra 与半正定规划；Baber 的改进使用 partially defined hypercubes，并提供可核对的数据/源码。
- 有限维的整数线性规划、穷举 C4 检验和启发式搜索；2026 预印本用模拟退火产生 Q7、Q8 的边表。
- 标准平均限制论证：f(n)/e(Q_n) 的极限存在，可把问题写为边 Turán 密度的精确求值。

争议或不确定性：

- 没有发现已发表或可审查的渐近解答/反例；但“未找到”并非逻辑上排除未被索引的新稿。
- Baber 的 0.60318 是有可验证数据支持的预印本结果，不是同行评审发表；作者明确说明其刻意未发表。
- Minamoto 的有限维下界是预印本结果。其 C4-free 性有边表和脚本可复核，但本审计没有独立运行代码，且启发式未找到更大图绝不是上界证明。
- 问题 #86 的论坛线程存在，但本次网页接口无法读取其两则帖文；因此无法排除其中有需要人工检查的非正式主张。

### 证据来源

- [Erdős Problem #86](https://www.erdosproblems.com/86) — Thomas F. Bloom / Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 数据库将题目列为 open，并给出 f(n) 的标准表述及 BHN95、BHLL14、Baber 的结果。该数据库标签仅作当前记录证据，不单独作为开放性的证明。
- [Erdős Problem #86 LaTeX source](https://www.erdosproblems.com/latex/86) — Thomas F. Bloom / Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`low`. 按协议访问以核对公式源；本次网页抓取返回内部错误，未从该端点取得额外文本。
- [Discussion Thread for Erdős Problem #86](https://www.erdosproblems.com/forum/thread/86?embed=1) — Erdős Problems forum contributors, date unknown; `forum`, `informal_claim`, directness=`direct`, reliability=`low`. 搜索索引显示该线程存在且有两帖；直接抓取未返回帖文正文，故未将任何论坛数学主张作为结论依据。
- [Publication record for Erdős, Problems and results in combinatorial analysis and combinatorial number theory](https://www.maths.tcd.ie/EMIS/classics/Erdos/cit/84005094.htm) — Paul Erdős; Zentralblatt record, 1991; `secondary_index`, `database_record`, directness=`indirect`, reliability=`high`. 索引的评论记录了 Erdős 的 epsilon-渐近 C4 强迫猜想，并称其当时仍开放；用于核对历史表述。
- [On the maximum number of edges in a C4-free subgraph of Q_n](https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.3190190104) — Peter Brass, Heiko Harborth, Hauke Nienborg, 1995-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明 n=4^r 时 f(n)>=1/2(n+sqrt(n))2^(n-1)，并证明所有 n>=9 时 f(n)>=1/2(n+0.9sqrt(n))2^(n-1)。这些均只给出趋于 1/2 的下界，未否定规范渐近猜想。
- [Upper bounds on the size of 4- and 6-cycle-free subgraphs of the hypercube](https://experts.illinois.edu/en/publications/upper-bounds-on-the-size-of-4-and-6-cycle-free-subgraphs-of-the-h/) — József Balogh, Ping Hu, Bernard Lidický, Hong Liu, 2014-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 同行评审论文以适用于超立方体的 flag algebra 方法得到 C4-free 边密度上界 0.6068。
- [Turán densities of hypercubes](https://arxiv.org/abs/1201.3587) — Rahil Baber, 2012-01-17; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 给出 C4-free 超立方体边 Turán 密度上界 0.60318；arXiv 记录附有验证所需源码与数据，作者主页说明该稿刻意未正式发表。
- [Rahil Baber — publications](https://www.rahilbaber.com/) — Rahil Baber, date unknown; `author_page`, `unknown`, directness=`direct`, reliability=`high`. 作者明确将 Turán densities of hypercubes 标作 arXiv:1201.3587v2 (2012) 且“Deliberately unpublished”；因此不能把 Baber 结果误标为同行评审论文。
- [New Lower Bounds for C4-Free Subgraphs of the Hypercubes Q6, Q7, and Q8: Constructions, Structure, and Computational Method](https://arxiv.org/abs/2603.29127) — Minamo Minamoto, 2026-05-13; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 最新相关预印本：给出 ex(Q7,C4)>=304、ex(Q8,C4)>=680 的有限维下界；其自身没有声称渐近问题已解决。
- [c4free-hypercube supplementary code and edge-list certificates](https://github.com/minamominamoto/c4free-hypercube) — Minamo Minamoto, 2026; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`medium`. 仓库提供 Q7/Q8 边表与无依赖验证脚本；README 明确把 Q7、Q8 等式称为猜想而不是上界证明。此审计未自行运行脚本，故只据此记录可复核性与作者的范围声明。
- [Bounding the size of square-free subgraphs of the hypercube](https://www.sciencedirect.com/science/article/pii/S0012365X08001234) — Andrew Thomason, Peter Wagner, 2009-04-06; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 用计算考察 Q4、Q5，将先前 C4-free 密度上界改进至 0.62256；用于追踪 Baber 所改进的直接前身。

### 完成标准

- 肯定出口: A complete affirmative resolution is a rigorous proof that for every epsilon>0 there exists N(epsilon) such that every n>=N(epsilon) and every C4-free subgraph G subseteq Q_n satisfy e(G)<= (1/2+epsilon)n2^(n-1). Together with the established BHN lower bounds, this proves pi_e(C4)=1/2.
- 否定出口: A complete negative resolution is a rigorous construction of a constant delta>0, infinitely many dimensions n_j->infinity, and C4-free G_j subseteq Q_(n_j) with e(G_j)>=(1/2+delta)n_j2^(n_j-1). This proves limsup f(n)/e(Q_n)>1/2 and contradicts the canonical claim.

不构成完成：

- An improved constant upper bound 1/2+delta for a fixed delta>0, including 0.60318, does not settle the conjecture.
- A construction of density 1/2+o(1), including a surplus c/sqrt(n), is compatible with the conjecture.
- Exact values, lower bounds, local maximality, or unsuccessful searches for any fixed finite list of dimensions do not establish either asymptotic alternative.
- A numerical SDP output without an exact rational/interval certificate and a proof that the finite configuration inequality transfers to all n is not a proof.
- Proving a statement only for induced C4-free subgraphs, or only for a restricted class of subgraphs, does not settle the stated problem.

正确性陷阱：

- Do not reverse the extremal/forcing quantifiers: C4-free upper bounds are equivalent to forcing only with the correctly strict threshold.
- Normalize by e(Q_n)=n2^(n-1), not by 2^n or by an incorrectly counted number of squares.
- Every C4 in Q_n is a coordinate square, but the target forbids non-induced C4 subgraphs; retain all four selected edges regardless of diagonal/non-edge language.
- Any proposed asymptotic recursion, random restriction, or averaging step must preserve C4-freeness in the required direction and track dimension-dependent errors uniformly.
- For computer-assisted flag-algebra work, audit the local configuration enumeration, symmetry factors, PSD/rational certificate, and the passage from finite sampled configurations to the asymptotic inequality.
- Do not mistake a finite ILP certificate for Q_k, or failure of a heuristic search, for an upper bound in arbitrary dimension.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `18/100`
- 信心: `medium`
- 结论: 这是定义清楚但长期未解的渐近极值图论问题；AI 可协助寻找可检验的局部引理或证书，但目前没有狭窄的、已知只差技术细节的缺口，因此直接解决的可能性低。

支持理由：

- 目标可精确量化，正反两种完成条件清晰，且 f(n)/e(Q_n) 的极限存在。
- 已有多种独立方法及可复核的 flag-algebra/有限维计算材料，可为证明辅助和反例筛查提供结构化切入点。
- 然而最好的上界仍为 0.60318，与 1/2 有固定常数差距；公开记录未显示一个可直接填补的关键引理。

主要障碍：

- 需要把局部无 C4 约束转化为几乎一半的全局边密度上界，现有局部/半正定方法尚未达到该阈值。
- 有限维优化和启发式搜索不能控制 n→∞；它们很容易造成“看似精确”的误导。
- 预印本、论坛和计算证书需要区分：可验证的有限下界不等于渐近结论，更不等于上界。

Proof-first 路线：

- 先尝试证明一个明确的结构定理：任何密度至少 1/2+epsilon 的 C4-free 子图必须在某个坐标限制、层级或局部类型中违反可计数的不等式；只有当该命题能被准确陈述时再发展证明。
- 审计并尝试加强现有 flag-algebra 不等式为严格的解析/有理证书，重点是识别为何现有局部配置上界停在 0.60318，而不是单纯增大 SDP。
- 把已知近 1/2 的构造抽象为必要结构，寻找稳定性/逆定理：若密度为 1/2+o(1)，其方向分布和 2-面约束必须具备何种模式。
- 唯一可选计算任务应是针对一个预先陈述的有限局部引理，产生精确可核验的反例或证书；不能以无终止条件的搜索代替证明。

需要验证：

- 人工复核 2026 预印本边表和 verify.py 的输出，以及它是否在论坛中已有实质讨论或勘误。
- 如将 Baber 上界作为正式背景，应复跑或审查其 arXiv 附带的证明证书，并明确其可接受的计算机辅助证明标准。
- 对任何声称改进 0.60318 或解决问题的新论文，必须审查完整证明而非仅凭摘要、搜索片段或论坛转述。

### 审计限制与人工复核理由

- 按要求未检查任何仓库内容，除用户提供的单一问题 JSON 外未使用本地问题条目。
- 问题页、LaTeX 页和论坛线程均已尝试直接打开；本次网页接口对它们返回内部/安全错误。搜索索引仍提供了问题页状态摘要和论坛“有两帖”的元数据，但未能读取论坛帖文正文。
- 对 2026 预印本的有限维边表与程序只进行了网页级可用性审查，未在本审计中执行代码或独立重建其 ILP/穷举。
- 检索覆盖了精确表述、作者、主要常数、arXiv、近三年文献和作者页，但不能从“未发现”演绎出世界范围内不存在未索引的证明。

- 应由人类审阅者直接阅读问题 #86 论坛的两则帖文；当前接口未能取得其内容。
- 2026 年预印本及其软件证书值得独立运行和数学复核，尤其应避免把其有限维搜索证据误作上界证明。
- 若后续研究依赖 Baber 的 0.60318 作为严格计算机辅助定理，应人工复核其 arXiv 附带的数据和证明验证链。

<!-- DEEP_REVIEW:END -->
