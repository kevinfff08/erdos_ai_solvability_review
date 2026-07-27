# Problem 108

## 基本信息

- 原始链接: https://www.erdosproblems.com/108
- LaTeX 页面: https://www.erdosproblems.com/latex/108
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `chromatic number`, `cycles`
- 形式化状态: `yes`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

For every $r\geq 4$ and $k\geq 2$ is there some finite $f(k,r)$ such that every graph of chromatic number $\geq f(k,r)$ contains a subgraph of girth $\geq r$ and chromatic number $\geq k$?

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `58/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 主要风险是候选证明或计算证书容易存在隐藏漏洞，需要独立复核。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: chromatic number, cycles, graph theory
- 证明密集标签命中: 无
- 有限/计算线索: chromatic, finite, graph
- 渐近/无限线索: 无
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 with computation, formal proof assistants, literature search, and counterexample search tools`
- 结论: **不适合作为“很可能由模型直接解决”的题目，但适合作为模型辅助推进的题目。GPT-5.5 级模型较可能在小参数、等价表述、已知 r=4 情形形式化、候选证明路线筛查、反例搜索和局部引理验证上产生实质价值；要完整证明对所有 r>=4、k>=2 的有限函数 f(k,r) 存在，仍需要新的结构性图论思想，成功概率偏低。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 较可行的路线是把问题拆成有限参数层级：先复现并形式化 r=4 的 Rödl 型论证，再尝试把“删除短环同时保持高色数”的过程表述为可迭代的稀疏化、随机抽样、局部修补或归纳引理；计算上可对小 k,r 搜索极端图，检验短环打击集与剩余色数之间的关系，并用 SAT/ILP/CP-SAT 验证小规模无反例区域。若能提出一个可机器检查的核心引理，例如高色数图中存在高色数子图且每个短环族可被低代价破坏，才可能推进到完整证明。

### 支持理由

- 问题是有限组合命题，且已标注 formalized=yes，适合用证明助手、SAT/ILP 和图搜索做局部验证。
- 目标不是构造特定对象，而是证明任意高色数图含有高 girth 且高色数的子图；这类命题可以被拆成可审计的引理和参数化边界。
- r=4 已有已知正例路线，模型可以围绕该特例做形式化复现、抽象出可推广部件，并检查推广失败点。
- 小参数反例搜索有价值：即使不能证明一般情形，也能约束可能的 f(k,r) 下界、发现极端构造、排除错误猜想。
- 问题陈述短、依赖对象明确，没有大量定义门槛，模型可以把主要工作集中在图论结构和证明搜索上。

### 主要障碍

- 完整命题覆盖所有 r>=4 和 k>=2，短环长度逐步增加时，简单删除三角形的思想未必能保持足够色数。
- 高色数与局部稀疏性之间的张力很强，随机图说明两者可共存，但从任意高色数图中抽取这种子图是更难的结构问题。
- 计算搜索只能覆盖极小规模，难以直接支持全称存在性证明。
- 若需要新的 Rödl 型或概率-结构混合引理，当前模型可能生成许多看似合理但存在量词或依赖关系漏洞的证明草稿。
- 无限版本也仍为开放，提示问题背后可能有深层结构障碍；虽然本题是有限版本，但不能低估其难度。

### 需要的验证

- 核对 r=4 已知证明的精确陈述、依赖条件和可推广部分，避免把三角形情形误套到更大 girth。
- 对模型提出的任何一般引理进行形式化验证，尤其检查参数依赖 f(k,r) 是否真正有限且只依赖 k,r。
- 用独立图算法验证小规模搜索结果，包括色数计算、girth 计算和所有子图候选的覆盖性。
- 对候选证明中的随机选择、删边删点、局部修补步骤做概率界和并合界审计。
- 检索相关文献确认是否已有部分结果、反例性障碍或更强/更弱命题，防止重复已知失败路线。

### 公开版思考摘要

这个问题的优势是形式清晰、有限、可参数化，且有 r=4 的已知成功案例作为锚点，因此 AI 工具链可以可靠地做子问题推进、证明复现和小规模验证。主要困难在于一般 r 的短环消除需要在任意高色数图中保留高色数，这很可能需要深层图论结构定理，而不是单纯搜索或局部优化。因此我评为低到中等候选：可显著辅助研究，但不应预期模型稳定给出完整解决。

### 免责声明

以上是对 GPT-5.5 级模型辅助可解性与推进潜力的审查，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_108.md](../../prompts/problem_108.md)

### 状态结论

有限图的原命题仍属公开未解问题；已严格解决 r=4（即三角形自由）情形，当前实质剩余目标是所有 r>=5 的无条件情形。2026 年已有一个同行评议的塔高型下界，以及一篇覆盖固定多项式边数-色数密度范围的预印本；两者均未给出一般情形的解决。

### 当前规范陈述

对任意整数 r>=4、k>=2，存在整数 F=F(k,r)，使得每个满足 χ(G)>=F 的有限简单图 G 都含有一个（不要求诱导的）简单子图 H，且 χ(H)>=k、girth(H)>=r。这里子图允许删去顶点和/或边；girth 是最短圈长度，无圈图的 girth 取为无穷。等价地，令 h_r(G)=max{χ(H): H 是 G 的子图且 girth(H)>=r}，则对每个固定 r>=4，当 χ(G) 趋于无穷时 h_r(G) 也趋于无穷。

```text
For every pair of integers r >= 4 and k >= 2, there exists an integer F=F(k,r) such that every finite simple graph G with chi(G) >= F has a (not necessarily induced) simple subgraph H satisfying chi(H) >= k and girth(H) >= r. Here a subgraph may delete vertices and/or edges; girth is the length of a shortest cycle, with girth infinity for forests. Equivalently, with h_r(G):=max{chi(H): H is a subgraph of G and girth(H)>=r}, prove that h_r(G) tends to infinity as chi(G) tends to infinity, for each fixed r>=4.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 已针对完全图作检查。K_n 不是该原命题的反例，因为 H 可为非诱导子图，故可从 K_n 选择任意有限简单图作为子图；这正是“subgraph”不能误作“induced subgraph”的关键。未发现能否定正确非诱导表述的简单构造。
- 版本变化: 未发现原有限命题被正式修订或被完整解决。Rödl（1977）解决 r=4。Pettie、Tardos、Walczak（SODA 2026）给出 r=5 的强下界而非反例。Li（2026 预印本）声称在固定多项式 chromatic-sparsity 范围证明全部 r>=4 的结论，仍未覆盖无条件命题。FormalConjectures 中的条目仅形式化了陈述且使用 sorry，并明确留有 r=4 证明及无限版本的 TODO。

陈述问题：

- “subgraph”必须按通常的非诱导子图理解，允许删边。若误读为“induced subgraph”，完全图族会立刻破坏 r=4、k=3 的版本。
- 原页面所说的“无限版本”是不同的强化问题：要求一个色数无穷且高 girth 的子图；它不是本有限阈值量词的同义改写。
- 原记号 f(k,r) 仅要求存在有限阈值，并未要求最优阈值、显式公式或统一渐近界。Erdős 另问的相邻 girth 阈值之比极限是附带的、非等价问题。

需要固定的量词/约定：

- r and k are fixed natural-number parameters before F is chosen.
- F may depend only on (k,r), never on G, its order, density, clique number, or a chosen representation.
- The universal quantifier ranges over finite simple graphs in the standard finite formulation.
- H is an ordinary subgraph: V(H) is a subset of V(G) and E(H) is a subset of E(G) restricted to V(H); it need not be induced.
- The required inequalities are non-strict: chi(G)>=F, chi(H)>=k, and girth(H)>=r.
- For r=4, the girth condition means triangle-free; 4-cycles are permitted.

### 文献与当前边界

已核验的主要结果：

- Rödl（1977，Proc. Amer. Math. Soc.，同行评议）给出“要么 K_m、要么 n-色无三角形子图”的阈值定理，从而解决 r=4。这里必须保留“子图可删边”的约定。
- Pettie、Tardos、Walczak（2026，SODA，同行评议）在 r=5 的 Burling 图上证明塔高型下界：高色数并不迫使低阈值的 girth-5 高色数子图；这限制了任何正面结果的定量强度，但不是反例。
- Li（2026-06-16，arXiv 预印本）声称在每个固定的 e(G)<=Cχ(G)^P 范围解决该结论，并给出更宽的拟多项式范围；这是条件性进展，而非对任意稠密图的解决。

最近相关工作：最新直接工作是 Eric Li 的 arXiv:2606.17901v1（2026-06-16，51 页，未同行评议）。其公开摘要和 HTML 文本可检查到的主张仅覆盖固定多项式 chromatic-sparsity 参数；应在使用前逐项审稿式核验其随机抽取、稀疏核与自举论证。

剩余核心：证明或反驳：对每个固定 r>=5、k>=2，存在仅依赖 (k,r) 的 F，使所有 χ(G)>=F 的有限简单图都含非诱导子图 H，满足 girth(H)>=r 且 χ(H)>=k；不得附加边数、顶点数、密度、最大度、分数色数或特定图类假设。

已使用方法：

- Rödl 的边划分/归纳式 clique-or-triangle-free 抽取。
- Burling 图与 Builder–Chooser clique game，用于构造塔高型 r=5 障碍和下界。
- Li 预印本提出的 chromatic-defect 随机抽取、紧致/近二次稀疏色数核、peeling/thinning 自举，以及分数色数下的短圈删除框架。

争议或不确定性：

- 当前 OPEN 标签是数据库编辑者的判断且其页面明确提示可能遗漏文献；本审计已检索到 2026 年两项直接工作，但不能把未发现完整解当作逻辑证明。
- SODA 论文的官方摘要和元数据可读，但全文受访问限制，未在本审计中逐行复核其证明。
- Li 的结果是很新的预印本；其范围和论证已根据公开摘要/HTML 记录，但未经过独立同行评审或完全复证。
- FormalConjectures 条目含 sorry，不能作为 r=4 或一般命题的机器验证证据。

### 证据来源

- [Erdős Problems 108: LaTeX source](https://www.erdosproblems.com/latex/108) — Thomas F. Bloom (database editor), 2026-01-23; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 给出当前有限命题、Erdős—Hajnal归属、Rödl 的 r=4 结果，以及附带的无限强化问题和比值极限问题。
- [108 Discussion Thread | Erdős Problems](https://www.erdosproblems.com/forum/thread/108) — Thomas F. Bloom (database editor), 2026-01-23; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 页面在 2026-01-23 仍列为 OPEN，并明确警告数据库状态只是站点所有者的判断、应自行检索；该线程无评论或已声称的部分解。
- [On the chromatic number of subgraphs of a given graph](https://doi.org/10.1090/S0002-9939-1977-0469806-4) — Vojtěch Rödl, 1977-06; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 论文证明：对任意正整数 m,n，色数充分大的图要么含 K_m，要么含一个色数为 n 的无三角形子图。结合足够大的完全图含任意有限三角形自由 n-色图作为非诱导子图，得到本题 r=4 情形。
- [On a Clique Game and the Erdős-Hajnal Problem on High-Chromatic High-Girth Subgraphs](https://epubs.siam.org/doi/10.1137/1.9781611978971.108) — Seth Pettie, Gábor Tardos, Bartosz Walczak, 2026-01-07; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. SODA 2026 论文的官方摘要称其给出该猜想的首个非平凡下界：第 m 个 Burling 图色数为 m，而当 m 是高度与 k 线性相关的 2 的塔时，它没有 girth 5 且色数大于 k 的子图。该结果显示 r=5 的阈值可极大，但没有否定有限阈值存在。
- [The Erdős-Hajnal High-Girth Subgraph Conjecture Holds in the Polynomial Chromatic-Sparsity Regime](https://arxiv.org/abs/2606.17901) — Eric Li, 2026-06-16; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 预印本声称：对固定 r>=4、k>=2、P,C>0，若 χ(G) 足够大且 e(G)<=Cχ(G)^P，则 G 有 girth 至少 r、色数至少 k 的子图；还声称扩展至某个拟多项式边数范围。其摘要明确将无密度限制的一般猜想作为未覆盖对象。
- [FormalConjectures.ErdosProblems.«108»](https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB108%C2%BB/) — Formal Conjectures contributors, 2025-11-24; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 该 Lean 条目将量词化的普通子图表述编码为研究开放问题，但定理声明使用 sorry；注释仍写有 r=4 证明和无限版本的 TODO。因此它确认了形式化陈述的选择，不构成已验证证明。

### 完成标准

- 肯定出口: Give a complete proof that for every fixed pair of integers r>=5 and k>=2 there is F(k,r) such that every finite simple G with chi(G)>=F(k,r) has an ordinary subgraph H with girth(H)>=r and chi(H)>=k. The proof must be uniform over all finite G, including arbitrarily dense graphs.
- 否定出口: Give a complete counterexample to the quantified statement: exhibit fixed integers r>=5 and k>=2 and finite simple graphs G_n with chi(G_n)->infinity such that every ordinary subgraph H of every G_n with girth(H)>=r has chi(H)<k.

不构成完成：

- Proving only r=4, or only one selected value of r>=5 or k, without resolving the stated universal target.
- A theorem restricted to e(G)<=C chi(G)^P, bounded degree, bounded order, a named graph family, fractional chromatic number, induced subgraphs, or another extra hypothesis.
- Finding high-girth high-chromatic graphs in the abstract; the target requires such a graph as a subgraph of every sufficiently high-chromatic host graph.
- A finite computational search without a theorem reducing all host graphs to the checked cases.
- A bound for a particular construction, including Burling graphs, unless it proves the universal affirmative statement or supplies the universal counterexample family.
- An argument that silently changes ordinary subgraph into induced subgraph or treats deleting edges as forbidden.

正确性陷阱：

- Check that H is an ordinary non-induced subgraph and that every retained edge belongs to G.
- Check the exact inequality girth(H)>=r; for r=5 both triangles and 4-cycles must be absent.
- Check that F depends only on (k,r), not on |V(G)|, e(G), clique number, a density exponent, or auxiliary constants selected from G.
- Check that chromatic number, rather than fractional/list/online chromatic number, is preserved at the required level.
- Check all small cases and the use of girth infinity for forests; k>=2 does not make the problem vacuous for arbitrary r.
- If using a probabilistic construction, convert positive probability into a deterministic H and verify all simultaneous events and deletions do not destroy the chromatic lower bound.
- Do not infer a density-free conclusion from a theorem whose constants P or C are allowed to depend on G.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 这是定义良好、可作研究的公开问题，但一般 r>=5 情形的 AI 独立解决前景偏低。

支持理由：

- 命题有明确的全称—存在量词、可机械核验的图论结论和清楚的反例形式。
- 已有 r=4 基例、2026 年 r=5 下界和多项式稀疏范围正面结果，提供了真实的结构信息与可攻击的中间引理。
- 目标仍要求对任意稠密高色数图给出统一抽取，且近年下界显示阈值可极端巨大。

主要障碍：

- 关键缺口是从受控密度/短圈分布推广到无任何密度约束的宿主图；简单随机删边通常会损失色数或无法廉价击杀聚集短圈。
- Burling 图给出 r=5 的塔高型障碍，说明小规模实验和朴素定量猜测很容易误导。
- 预印本中的方法尚未同行评审，不能把其中未验证的技术引理当作可自由调用的黑箱。

Proof-first 路线：

- 把一般反例最小化为色数临界核，并证明其必须违反 Li 预印本中任一可核验的“廉价短圈删除”障碍；随后寻求不依赖密度的结构矛盾。
- 研究短圈高度聚集的极端构型，尤其是 Burling 型递归，尝试证明它们仍包含足够高色数的 girth-5 子图，或将其提升为真正反例。
- 寻找可替代随机边稀释的确定性分解/颜色缺陷抽取引理，其结论直接给出普通子图且对任意密度有效。

需要验证：

- 逐项审计 Li（2026）预印本的主定理假设、常数依赖和从随机对象到确定性子图的步骤。
- 取得并核验 Pettie–Tardos–Walczak 的完整 SODA 论文，精确记录塔高下界中的量词、girth 和色数严格性。
- 在正式宣称状态前再次检索 2026-06-16 后的 arXiv、作者主页和期刊记录，以排除新近完整解或反例。

### 审计限制与人工复核理由

- 本审计未能获得 SODA 2026 正文的开放访问副本，故其结论按官方摘要和书目信息记录，而非逐行复核证明。
- Li 的 2026 预印本可公开读取摘要和 HTML 版，但未完成独立全证明复查，也尚无同行评审状态。
- 网络检索覆盖精确陈述、作者、近期 preprint、期刊页、数据库和形式化页；它不能逻辑上证明不存在尚未索引或 2026-07-27 后发布的完整解决。
- 未把 FormalConjectures 的 sorry 占位、数据库 OPEN 标签或任何非正式页面视为数学证明。

- 应由图论专家获取并审读 Pettie–Tardos–Walczak 的完整 SODA 论文，以核对塔高下界的精确量词和任何可能与目标相关的附加结论。
- 应对 Li 的新预印本进行独立证明审计；其条件性结果目前不能提升为一般命题的已验证进展。
- 在启动高成本研究前，应再进行一次截至启动日的文献检索，因为该领域在 2026 年已有快速的新进展。

<!-- DEEP_REVIEW:END -->
