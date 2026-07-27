# Problem 84

## 基本信息

- 原始链接: https://www.erdosproblems.com/84
- LaTeX 页面: https://www.erdosproblems.com/latex/84
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `cycles`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

The cycle set of a graph $G$ on $n$ vertices is a set $A\subseteq \{3,\ldots,n\}$ such that there is a cycle in $G$ of length $\ell$ if and only if $\ell \in A$. Let $f(n)$ count the number of possible such $A$.

Prove that $f(n)=o(2^n)$.

Prove that $f(n)/2^{n/2}\to \infty$.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `35/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：\ll, o(

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: cycles, graph theory
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: \ll, o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。该题的上界部分在题目备注中已给出已有解，因此 GPT-5.5 级模型较可能通过文献检索、证明重构和形式化检查来复现或验证 f(n)=o(2^n)。真正开放且更有价值的是下界 f(n)/2^{n/2}\to\infty；模型有机会通过构造搜索和组合结构分析给出显著推进，但直接完成的把握不高。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 可行路线应分成两部分：第一部分检索并重构 Verstraete 与 Nenadov 型上界，把循环长度集合的稀疏约束转化为可计数的结构限制，再用形式化或半形式化证明检查关键不等式。第二部分针对下界，从 Erdős-Faudree 的 2^{n/2} 构造出发，系统搜索能独立控制更多循环长度的图块拼接、theta 图、耳分解或带受控长度和的构造，并用程序枚举小 n 的可实现 cycle set 来猜测可扩展族。

### 支持理由

- 题目备注明确说明第一问已经被解决且有更强上界，因此 AI 工具链可以把这一部分作为文献复现、证明压缩和验证任务，而不是从零突破。
- 对象定义清晰：每个图对应一个循环长度集合，适合用计算枚举、SAT/ILP 搜索、图生成和 OEIS 式序列检查来发现小规模模式。
- 第二问是渐近下界构造问题，比任意图计数问题更可能通过构造模板、参数化搜索和自动反例/例证生成获得增量进展。
- 已有下界 2^{n/2} 给出可分析的基线；AI 可以尝试寻找额外自由度，使可实现集合数多出一个趋于无穷的因子，而不必一次性达到指数底数改进。

### 主要障碍

- 第二问需要证明存在足够多互不相同的循环长度集合，而不只是生成很多图；不同构造可能产生相同的 cycle set，去重和注入证明是核心难点。
- 控制图中恰好出现哪些循环长度很困难，因为新增边或拼接块会产生非预期长度的组合循环。
- 小规模计算容易误导：有限 n 中可实现集合的增长模式未必能推广为渐近构造。
- 若要复现已有上界，原论文中的极值图论引理可能较深，形式化成本可能高于普通组合计数证明。

### 需要的验证

- 核对题目备注中 Verstraete 2004 与 Nenadov 2025 的具体定理、假设和符号是否确实直接推出 f(n)=o(2^n)。
- 对任何下界构造，需要给出明确的 n 顶点图族、可选择参数族、cycle set 的互异性证明，以及顶点数与可实现集合数的精确渐近关系。
- 用穷举或规范图生成在小 n 上验证构造不会产生未声明的循环长度，并检查计数注入是否成立。
- 若声称解决第二问，需要独立人工审阅或形式化证明验证关键结构引理，尤其是排除非预期组合循环的部分。

### 公开版思考摘要

从给定 JSON 看，本题包含一个已解决上界目标和一个仍开放的下界目标。AI 对已解决部分很适合作为文献重构与验证；对开放下界，问题形态偏构造性，工具辅助搜索有实际价值，但核心障碍是精确控制循环长度集合和证明大量集合互异。因此评为中等候选：较可能显著推进或验证部分内容，直接完整解决开放部分的概率有限。

### 免责声明

以上只是对 GPT-5.5 级模型可解性与推进潜力的审查，不是该 Erdős 问题的数学解答或证明。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `revised_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_84.md](../../prompts/problem_84.md)

### 状态结论

原记录把两个独立断言并列：上界断言 f(n)=o(2^n) 已由 Verstraëte（2004）证明，且被 Nenadov（2026）加强；尚存的精确定义良好的目标是证明 f(n)/2^{n/2}→∞。Nenadov 的同行评审论文明确称 Faudree 的 2^{n/2} 构造为“best known lower bound”，并称任何固定正指数改进都很有意义，支持该较弱剩余断言截至审计日仍未解决。

### 当前规范陈述

对每个整数 n≥3，令 C(G)={ell∈{3,…,n}: 恰有 n 个顶点的有限简单无向图 G 含有长度为 ell 的简单圈}，并令 f(n)=|{C(G): |V(G)|=n}|。现存开放目标是证明当 n→∞ 时 f(n)/2^{n/2}→+∞；等价地，对每个实数 M>0，存在 N，使每个整数 n≥N 都有 f(n)≥M2^{n/2}。

```text
For every integer n>=3, let C(G):={ell in {3,...,n}: the finite simple undirected graph G on exactly n vertices contains a simple cycle of length ell}, and let f(n):=|{C(G): |V(G)|=n}|. The surviving open target is to prove lim_{n->infinity} f(n)/2^{n/2}=+infinity; equivalently, for every real M>0 there is N such that f(n)>=M2^{n/2} for every integer n>=N.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 该剩余断言是渐近计数下界，不能由单个小 n 的图构成反例。已核对的 Faudree 构造仅给出约 2^{n/2} 个不同集合，未否定趋于无穷；未发现针对该精确剩余断言的已验证反例。
- 版本变化: 2004 年 Verstraëte 已证明原条目的第一项，给出比 o(2^n) 更强的上界。2026 年 Nenadov 将该上界改进为 2^{n-Ω(√n/log^{3/2}n)}。因此条目应从“双目标开放问题”修订为仅保留下界极限问题；这不是对第二项的措辞修补，而是删除已闭合的第一项。

陈述问题：

- 原条目以两个“Prove that”并列，容易被误读为一个尚未解决的合取命题；其中第一项已解决，研究目标应只保留第二项。
- 原文未明说图是否为简单无向图；但长度范围从 3 开始及所引文献的标准语境要求采用有限简单无向图。
- 必须区分“有至少 2^{n/2} 个不同的圈长度集合”与所要求的比值趋于无穷：前者及其固定常数倍均不足以推出后者。

需要固定的量词/约定：

- Graphs are finite, simple, undirected, and have exactly n vertices; cycle means a simple graph-theoretic cycle.
- f(n) counts distinct subsets C(G), not labelled graphs and not graph isomorphism classes.
- The limit is over every integer n tending to infinity, not merely an infinite subsequence or even n.
- The first displayed request in the database is already a theorem; the canonical open target is only the second displayed request.

### 文献与当前边界

已核验的主要结果：

- Faudree 的构造：n 为偶数时，对 A⊆{n/2+1,…,n}，取 Hamilton 路径并加入从一个端点到 A 中顶点的边；不同 A 给出至少 2^{n/2} 个不同圈长度集合。Nenadov（2026）将此称为最佳已知下界。
- Verstraëte（Combinatorica, 2004）证明存在绝对常数 c≥0.1，使 f(n)=o(2^{n-n^c})，故 f(n)=o(2^n) 已解决。
- Nenadov（Combinatorial Theory, 2026）证明 f(n)≤2^{n-Ω(√n/log^{3/2}n)}，即数据库所写 2^{n-n^{1/2-o(1)}} 的明确版本。

最近相关工作：Nenadov 的《Improved bound on the number of cycle sets》于 2026-04-20 在 Combinatorial Theory 发表（2025 年 arXiv 预印本，v2 于 2025-09-22）。截至审计日，未检得此后直接改进该下界极限问题的论文或可核验解决声明。

剩余核心：证明对任意 M>0，所有充分大的 n 都有 f(n)≥M2^{n/2}。更强但非必需的目标是找 c>0 使 f(n)≥2^{(1+c)n/2}；Nenadov 明确将后者称为有意义的未达进展，不能把它误当作已知等价结论。

已使用方法：

- 下界：从 Hamilton 路径和一颗星形弦集进行显式编码，确保高半区的圈长恰好编码 A。
- 上界：Verstraëte 将问题归约到含许多弦或大最大度的诱导 Hamilton 子图。
- Nenadov：对弦构造小 fingerprint，并以容器型引理产生每个圈长度集合必须包含的较大集合；再将图分为长圈、稀疏、较大最大度和较多弦四类计数。
- Nenadov 指出，沿该上界路线进一步改进的瓶颈是“有长圈但只有线性条边”的图族。

争议或不确定性：

- Erdős Problems 页面仍以一个整体 OPEN 标签展示两个请求；这与其备注“第一问题已解”并不矛盾，但需要按本审计拆分。
- 开放性不是由检索失败逻辑证明的；其置信度来自 2026 年直接论文对“最佳已知下界”的说明、数据库记录和针对性近期检索。
- Verstraëte 的全文受订阅限制，本审计核验了出版社摘要和书目信息，而非逐行复核其 2004 年证明。

### 证据来源

- [Erdős Problem 84](https://www.erdosproblems.com/84) — Thomas F. Bloom / Erdős Problems, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 给出原始双断言、数据库的开放标签、Verstraëte 与 Nenadov 的上界摘要；页面同时报告该题没有论坛中的解答或部分解答声明、没有形式化条目。
- [Improved bound on the number of cycle sets](https://escholarship.org/uc/item/4k75b3z7) — Rajko Nenadov, 2026-04-20; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 同行评审论文的定理 1.1 给出 f(n)≤2^{n-Ω(√n/log^{3/2}n)}；导言称 Faudree 的 2^{n/2} 是最佳已知下界，并指出将其提高到 2^{(1+c)n/2} 已属有意义进展。该文还说明其方法及现有上界路线的瓶颈。
- [Improved bound on the number of cycle sets](https://arxiv.org/abs/2501.09904) — Rajko Nenadov, 2025-01-17; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 预印本记录了 v2（2025-09-22）及与后续期刊版一致的摘要：改进 Verstraëte 的上界，并使用 Hamilton 图、弦和容器引理。
- [On The Number Of Sets Of Cycle Lengths](https://link.springer.com/article/10.1007/s00493-004-0043-6) — Jacques Verstraëte, 2004-09; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 期刊页确认 Verstraëte 证明存在常数 c≥0.1，使圈长度集合的数目为 o(2^{n-n^c})；这严格蕴含原条目的第一项 f(n)=o(2^n)。

### 完成标准

- 肯定出口: Give a rigorous proof that for every M>0 there exists N such that, for every integer n>=N, at least M·2^(n/2) pairwise distinct subsets of {3,...,n} occur as C(G) for n-vertex finite simple graphs G.
- 否定出口: Give a rigorous proof of the logical negation: there exists a finite M>0 such that for every N there is an integer n>=N with f(n)<=M·2^(n/2). An explicit infinite sequence n_j→∞ with this uniform upper bound suffices.

不构成完成：

- Reproving f(n)=o(2^n), or improving its upper bound, does not resolve the surviving lower-bound target.
- Constructing at least 2^(n/2) cycle sets, or c·2^(n/2) for one fixed c>0, does not prove divergence.
- A construction only for a sparse subsequence, or only for even n without a valid extension to every sufficiently large n, is insufficient.
- Proving a stronger exponential bound only conditionally, or for a restricted graph class, is not a resolution unless the condition/restriction is removed.

正确性陷阱：

- Count distinct cycle-length sets, not the number of graphs or labelled edge sets; an injection into graphs need not be an injection into C(G).
- For every proposed encoding, prove both inclusion and exclusion of cycle lengths; unplanned cycles created by several chords are the central risk.
- Track the exact vertex count. Adding isolated vertices preserves a spectrum but changes the normalization 2^(n/2), so parity transfer requires a quantitative argument.
- All asymptotic constants and thresholds must be uniform in n and must establish the full limit, not merely an unbounded limsup.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `18/100`
- 信心: `high`
- 结论: 这是定义清楚且有近期结构性进展的开放下界问题，但现有最佳下界与所需结论之间仍有实质性构造缺口；对 AI 而言适合以严格证明探索为主，短期完整解决概率低。

支持理由：

- 目标可形式化，正反完成条件明确，并可逐一审查候选构造是否产生额外圈长。
- 2026 年论文提供了精确的当前基线、Faudree 构造和与该领域相邻的结构工具。
- 一个固定正指数改进会强力解决问题，说明存在清晰的充分里程碑。

主要障碍：

- 目标要求对所有充分大 n 的不同圈长度集合数量做超常数因子改进；不能从有限计算或单一参数族自动推出。
- 构造中不同弦之间会生成额外圈，通常破坏以 A 为参数的精确可逆编码。
- 近期工作主要推进上界而非下界，且其所述瓶颈并未直接给出下界机制。

Proof-first 路线：

- 探索能把两个或多个独立可控的长圈区间编码进同一 n 顶点图的构造，并先证明编码到 C(G) 的单射及没有干扰圈长。
- 寻找可组合的图操作：在严格追踪顶点数、所有新旧圈长及谱碰撞的前提下，将多个基础构造的谱参数相乘。
- 研究受控 Hamilton 路径加弦家族的精确圈谱，目标是可验证的局部引理，而不是直接穷举 f(n)。

需要验证：

- 对任何声称的新构造，独立枚举其所有简单圈的分类证明，特别是使用多条弦的圈。
- 核对构造在奇偶 n、端点、区间重叠和小参数时是否仍保持单射。
- 若声称解决，复核是否证明了全体充分大 n 的极限定义，而非只证明 limsup 或固定常数因子下界。

### 审计限制与人工复核理由

- 已按精确题述、作者、问题编号和近三年文献检索，但“没有后续解答”只能是基于所查来源的高置信状态判断，而非逻辑上的全世界文献完备证明。
- Erdős Problems 的论坛链接可识别为 /forum/discuss/84，但网页抓取未能载入该页；主问题页明确显示 0 comments 和无解答/部分解答声明。
- Verstraëte（2004）正文受订阅限制；其期刊出版社摘要直接确认足以关闭第一项的定理，但本审计未逐行复核该旧证明。

- 若要将“likely_open”升级为数据库级最终状态，应由领域专家或数据库维护者复核 2026-07-27 之后可能未被检索索引的预印本、报告或私人声明。
- 应由人工复核原始 Erdős/Faudree 文献中第二项的历史表述及其是否另含未在本条目显示的变体。
- 任何未来声称解决第二项的文本都必须独立检查其对所有充分大 n、完整圈谱与不同谱计数的证明。

<!-- DEEP_REVIEW:END -->
