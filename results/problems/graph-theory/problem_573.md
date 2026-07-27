# Problem 573

## 基本信息

- 原始链接: https://www.erdosproblems.com/573
- LaTeX 页面: https://www.erdosproblems.com/latex/573
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `turan number`
- 形式化状态: `no`
- OEIS: `A006856`
- 原站备注字段: 无

## 原问题

Is it true that\[\mathrm{ex}(n;\{C_3,C_4\})\sim (n/2)^{3/2}?\]

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `44/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 题面含渐近/无限对象线索：o(

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, turan number
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: o(
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。GPT-5.5 配合计算、检索、形式化和反例搜索，较可能整理现有边界、验证小规模极值、提出候选构造或证明路线，但直接解决该渐近常数问题的概率不高。**
- 等级: `low_to_medium_candidate`
- 分数: `36/100`
- 信心: `medium`
- 可能路线: 较现实的路线是：先围绕给定陈述形式化目标，即证明或否定 ex(n;{C3,C4}) ~ (n/2)^{3/2}；再用 SAT/ILP/CP-SAT 搜索小 n 的极值图并与 OEIS A006856 对齐；同时检索和重建给定备注中相关的 C4 与奇圈限制、二部 C4-free 构造、Erdos-Simonovits/KST 类型上界；随后尝试把问题转化为“允许较长奇圈是否能提高主常数”的结构性命题。若有进展，最可能是条件性上界、改进的稀疏稳定性引理、或排除某类非二部候选构造，而不是一次性完成全证明。

### 支持理由

- 问题陈述非常短，目标常数明确，适合自动化检索、计算实验和形式化拆解。
- 给定备注已经指出相邻已知结果：强禁止奇圈时主项为 (n/2)^{3/2}，因此核心难点可以清楚定位为只禁止三角形时是否仍不能增加主常数。
- 该问题属于稀疏极值图论，计算工具可以有效生成小规模极值数据、寻找反例模式、测试代数构造和辅助猜测稳定性结论。
- 形式化证明工具可用于验证局部计数不等式、双计数上界、C4-free 约束下的邻域结构等子引理。

### 主要障碍

- 这是开放的渐近 Turan 数常数问题，若要证明等价式，需要全局稀疏结构定理，而不是有限规模搜索。
- 小 n 极值图可能强烈受有限阶现象影响，难以直接外推到 n^{3/2} 主项常数。
- 如果存在非二部、无 C3/C4 的高密度构造，它可能来自有限几何、代数图或伪随机结构，模型很难凭通用搜索覆盖。
- 常规 flag algebra 更适合稠密图；这里是稀疏 n^{3/2} 标度，需要专门化的归一化和极限对象。
- 文献中的已知边界和构造细节很可能分散在经典极值图论结果中，误读一个常数就会导致错误判断。

### 需要的验证

- 核对 OEIS A006856 与小 n 的 ex(n;{C3,C4}) 数据是否一致，并记录极值图结构。
- 用独立 SAT/ILP/CP-SAT 程序复现实验数据，避免只依赖模型生成的候选图。
- 系统检索并复核给定备注中涉及的 KST 与 Erdos-Simonovits 结果，确认常数、禁止族和误差项。
- 若提出上界证明，需要由人类专家或 Lean/Isabelle 等形式化工具检查关键双计数、稳定性和极限步骤。
- 若提出反例路线，需要构造无限图族，并严格证明其无 C3、无 C4 且边数主常数超过 2^{-3/2}。

### 公开版思考摘要

该问题的可攻性来自目标清晰、已有相近定理和可计算验证空间；主要困难来自它要求确定稀疏极值图的精确渐近主常数。GPT-5.5 级别模型很适合做文献归纳、常数核验、小规模极值搜索、候选结构分类和子引理形式化，但完整解决需要新的图论结构性洞见。因此我评为低到中等候选：可显著辅助推进和排错，但不应预期稳定地产生最终证明。

### 免责声明

以上是基于给定 Problem JSON 的 AI 可解性审查，不是该 Erdős 问题的证明、反例或解决声明。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `not_required`
- 独立研究 Prompt: [prompts/problem_573.md](../../prompts/problem_573.md)

### 状态结论

截至审计日，原命题仍为一个精确定义且未解决的渐近极值问题。Erdős Problems 页面于 2026-01-18 仍标为 open，且 2025 年同行评审论文明确称该同一渐近猜想“widely open”；对精确公式、题号、论文标题及 2025–2026 年 arXiv 的定向检索未发现可核查的解决或反例。2025 年 Ma–Yang 的结果显著改进了下界的低阶项，但其增量为 o(n^{3/2})，并不否定本题的渐近等价。

### 当前规范陈述

记 C_k 为 k 个顶点的简单环。对每个正整数 n，ex(n,{C_3,C_4}) 是所有恰有 n 个顶点、有限、简单、无向且不含 C_3 或 C_4 作为（不要求诱导）子图的图的最大边数。问题是：当 n 沿正整数趋于无穷时，是否有
ex(n,{C_3,C_4})/(n/2)^{3/2} -> 1？
等价地，是否有 ex(n,{C_3,C_4})=(n/2)^{3/2}+o(n^{3/2})？

```text
Let C_k be the simple cycle on k vertices. For each positive integer n, let ex(n,{C_3,C_4}) be the maximum number of edges in a finite simple undirected graph G with |V(G)|=n that contains neither C_3 nor C_4 as a (not necessarily induced) subgraph. Determine whether, as n tends to infinity through the positive integers,
ex(n,{C_3,C_4}) / (n/2)^{3/2} -> 1.
Equivalently, prove or disprove ex(n,{C_3,C_4}) = (n/2)^{3/2}+o(n^{3/2}).
```

### 陈述、量词与反例审计

- 歧义严重度: `none`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定文字命题的简单构造。特别地，Ma–Yang 在无限多个 n 上给出 (n/2)^{3/2}+Omega(n^{5/4}) 的下界，但 n^{5/4}=o(n^{3/2})，故与“~”完全相容；它只否定 O(n) 误差的加强版本。
- 版本变化: 题目页的历史显示当前措辞保持为该渐近问题。文献上出现的实质性分化是：Chung–Graham 曾问更强的 O(n) 误差版本；Ma–Yang（2025）证明其答案为否。原题的渐近主项猜想仍是开放目标，并非需要修复的错误表述。

陈述问题：

- 输入式中的 ex、C_k、渐近符号虽未逐一展开，但当前数据库页及 Ma–Yang 论文采用标准且一致的有限简单无向图/非诱导子图约定；补全后得到唯一的命题。
- “~”必须按 n 沿正整数趋于无穷、两边之比趋于 1 理解；它不是声称存在 O(n) 误差的更强断言。
- 不得把 Chung–Graham 的加强问题 ex(n,{C_3,C_4})=(n/2)^{3/2}+O(n) 与本题混同：该加强问题已被 Ma–Yang 的超线性低阶项下界否定，而本题未被否定。

需要固定的量词/约定：

- The maximization is over finite simple undirected graphs on exactly n vertices; containment is as a subgraph, not an induced subgraph.
- The asymptotic variable is n through positive integers, and f(n)~g(n) means f(n)/g(n)->1.
- A negative resolution requires a fixed positive relative separation on infinitely many n (or another proof that the ratio fails to tend to 1); an additive omega(n) or even Omega(n^{5/4}) term alone is compatible with the target.

### 文献与当前边界

已核验的主要结果：

- 令 z(n,C_4) 为 n 顶点二分 C_4-free 图的最大边数。Ma–Yang 记录 z(n,C_4)=(n/2)^{3/2}+o(n^{3/2})，并给出对任意 n 的显式双边界：(n/2)^{3/2}-c n^{4/3} <= z(n,C_4) <= (n/2)^{3/2}+n/4。因二分图无三角形，ex(n,{C_3,C_4})>=z(n,C_4)。
- Kővári–Sós–Turán 与 Reiman 的经典 C_4-free 上界给出 ex(n,{C_3,C_4})<=ex(n,C_4)=1/2 n^{3/2}+O(n)。这与目标主项 1/(2sqrt(2)) n^{3/2} 之间仍有常数因子 sqrt(2) 的上界缺口。
- Parsons（1976）曾在特定 n 上给出 (n/2)^{3/2}+3n/8 的下界。Ma–Yang（2025，同行评审）证明存在绝对 c>0，使所有 n>=7 满足 ex(n,{C_3,C_4})>=z(n,C_4)+c n^{5/4}；对 n=2(q^2+q+1)、q 为素数幂，推出 ex(n,{C_3,C_4})=(n/2)^{3/2}+Omega(n^{5/4})。
- Erdős–Simonovits 的 C_4,C_5 结果，以及 Keevash–Sudakov–Verstraëte（2013）对所有 C_4,C_{2k+1}（k>=2）的结果，给出 (n/2)^{3/2}+O(n)。但这些禁止的是长度至少 5 的指定奇环，不能替代仅禁止 C_3 的问题。
- Ma–Yang 因而否定了 Chung–Graham 的更强问题 ex(n,{C_3,C_4})=(n/2)^{3/2}+O(n)；这不是对本题的否定，因为 n^{5/4}=o(n^{3/2})。

最近相关工作：最强的渐近相关进展是 Ma 与 Yang 的同行评审论文（Forum of Mathematics, Sigma 13, 2025, e154；在线发表 2025-09-23），其完整证明可访问且明确将原渐近猜想列为仍广泛开放。最新发现的直接相关预印本是 Goedgebeur、Jooken、Joret、Van den Eede（arXiv:2508.05562，2025-08-07），仅改进有限 n=74–198 的构造下界。定向搜索至 2026-07-27 未找到后续解决论文。

剩余核心：证明或反驳统一的主项上界 ex(n,{C_3,C_4}) <= (n/2)^{3/2}+o(n^{3/2})。由于 z(n,C_4) 已给出匹配的渐近下界，这恰等价于原题；问题不是确定 O(n) 或其他低阶项。

已使用方法：

- C_4-free 图的两步路径计数、Kővári–Sós–Turán 型上界与 Zarankiewicz 数。
- 有限射影平面及近极值二分 C_4-free 图的构造和伪随机性。
- Ma–Yang 的局部替换构造：在极值二分 C_4-free 图的若干互不交邻域中删边并嵌入较小的 {C_3,C_4}-free 图，以保持禁图并得到 Omega(n^{5/4}) 增量。
- 有限 girth-5 图的 hill-climbing 搜索仅用于有限阶下界。

争议或不确定性：

- 不存在已核验的解答争议或论坛声称；题目论坛为 0 条评论。
- 关于真正低阶项的直觉并不一致：Ma–Yang 记录 Allen–Keevash–Sudakov–Verstraëte 的相反型猜测 liminf ex(n,{C_3,C_4})/z(n,C_4)>1；该猜测与主项比值趋于 1 并不逻辑矛盾，因为 z(n,C_4) 与目标主项的相对差可趋零。
- “未找到 2026 年解决”是广泛定向检索的证据而非数学上的文献完备性证明。

### 证据来源

- [Erdős Problem #573](https://www.erdosproblems.com/573) — Thomas F. Bloom / Erdős Problems, 2026-01-18; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前条目将该精确命题标为 OPEN；页面注明最后编辑于 2026-01-18，并列出 Erdős、Erdős–Simonovits 等原始来源。数据库自身也提醒其状态并非文献穷尽证明。
- [LaTeX source for Erdős Problem #573](https://www.erdosproblems.com/latex/573) — Thomas F. Bloom / Erdős Problems, 2026-01-18; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 核对当前 LaTeX 题面与输入公式一致：ex(n;{C_3,C_4})~(n/2)^{3/2}。
- [Erdős Problem #573 discussion thread](https://www.erdosproblems.com/forum/thread/573) — Erdős Problems forum, 2026-01-18; `forum`, `informal_claim`, directness=`direct`, reliability=`low`. 该题论坛页显示 0 comments，故未发现需核验的论坛解答或反例声称；其 open 标签仅作辅助证据。
- [On extremal numbers of the triangle plus the four-cycle](https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/on-extremal-numbers-of-the-triangle-plus-the-fourcycle/ED3AF154970DCE68C1EF742401F0A919) — Jie Ma and Tianchi Yang, 2025-09-23; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 定义 ex(n,F) 与 z(n,C_4)，证明 z(n,C_4)~(n/2)^{3/2}，明确称本渐近猜想仍“widely open”，并给出 ex(n,{C_3,C_4})>=z(n,C_4)+c n^{5/4}（所有 n>=7）及在特定无限序列上的 (n/2)^{3/2}+Omega(n^{5/4}) 下界。
- [On extremal numbers of the triangle plus the four-cycle](https://arxiv.org/abs/2112.13689) — Jie Ma and Tianchi Yang, 2021-12-27; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 提供同行评审论文的公开预印本记录与版本链；摘要称其构造是自 1976 年以来对该下界的首次改进。
- [Improved lower bounds on the maximum size of graphs with girth 5](https://arxiv.org/abs/2508.05562) — Jan Goedgebeur, Jorik Jooken, Gwenaël Joret, and Tibo Van den Eede, 2025-08-07; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 近年相关工作：用 hill-climbing 启发式改进 n=74,...,198 中除 96、97 外各 n 的有限下界；不声称也不证明原题的渐近结论。
- [On a conjecture of Erdős and Simonovits: Even cycles](https://doi.org/10.1007/s00493-013-2863-8) — Peter Keevash, Benny Sudakov, and Jacques Verstraëte, 2013; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. Ma–Yang 据此引用：对每个 k>=2，ex(n,{C_4,C_{2k+1}})=(n/2)^{3/2}+O(n)，说明禁止较长奇环的已知结果不能直接处理 C_3。
- [Compactness results in extremal graph theory](https://doi.org/10.1007/bf02579234) — Paul Erdős and Miklós Simonovits, 1982; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 原问题归属及 C_4 加 C_5 的相关结果的历史来源；本次通过 Ma–Yang 的参考文献和讨论间接核对。
- [On a problem of K. Zarankiewicz](https://doi.org/10.4064/cm-3-1-50-57) — Tamás Kővári, Vera T. Sós, and Pál Turán, 1954; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 原始 Kővári–Sós–Turán 文献记录；现代论文将其与 Reiman 的结果用于 ex(n,C_4)=1/2 n^{3/2}+O(n) 的标准上界背景。

### 完成标准

- 肯定出口: Give a complete proof that for every epsilon>0 there exists N such that every integer n>=N satisfies ex(n,{C_3,C_4}) <= (1+epsilon)(n/2)^(3/2). Together with the established bipartite lower bound z(n,C_4)=(1-o(1))(n/2)^(3/2), this proves the required asymptotic equivalence.
- 否定出口: Give a complete proof that the ratio does not tend to 1; for example, exhibit epsilon>0 and infinitely many integers n for which there exists an n-vertex {C_3,C_4}-free graph with at least (1+epsilon)(n/2)^(3/2) edges. A rigorous incompatible liminf/limsup statement would also resolve the question negatively.

不构成完成：

- A bound ex(n,{C_3,C_4}) <= (1/2+o(1))n^(3/2), since it retains the existing factor-sqrt(2) gap.
- Any finite table, heuristic construction, or computational record without a theorem covering asymptotically all n.
- An additive lower bound (n/2)^(3/2)+Omega(n^alpha) for alpha<3/2, including alpha=5/4; it remains compatible with ~.
- A proof of the stronger O(n)-error statement or its negation, unless it also proves or disproves the relative o(n^(3/2)) target.
- An argument for {C_4,C_5}-free or {C_4,C_{2k+1}}-free graphs that does not address triangles.

正确性陷阱：

- Keep C_3 and C_4 forbidden as non-induced subgraphs in simple undirected graphs.
- Track the leading constant: (n/2)^(3/2)=n^(3/2)/(2sqrt(2)), not (1/2)n^(3/2).
- Do not reverse the inequality z(n,C_4)<=ex(n,{C_3,C_4}); bipartite C_4-free graphs supply a lower bound.
- When using a subsequence, distinguish an additive o(n^(3/2)) gain from a fixed relative gain.
- Verify every local modification cannot create either a triangle or a 4-cycle crossing the modified and unmodified parts.
- If invoking projective planes, state the prime-power condition and whether the claimed conclusion concerns all n, an infinite subsequence, or almost all n.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `14/100`
- 信心: `medium`
- 结论: 这是定义清楚、可证伪且有成熟工具链的开放问题，但主项常数的上界缺口很大；在无新结构性思想的前提下，AI 独立解决的概率低。

支持理由：

- 目标可化为一个明确的统一上界，完成与反例条件均可机械核查。
- 已有精确的二分基准、成熟的 C_4-free 计数工具，以及公开的最近构造证明，便于分解和严格审计。
- 近期工作显示非二分构造可系统地超过二分基准，提供了值得分析的结构信号。

主要障碍：

- 最佳通用上界仍是忽略禁三角形得到的 ex(n,C_4) 上界，主项常数相差 sqrt(2)；这不是低阶技术修补。
- Ma–Yang 的局部构造说明“近极值必近二分”一类未经量化的直觉不可直接作为证明前提。
- 有限搜索只能产生有限下界，不能裁定主项；自动化很容易将超线性但次主项的增量误判为反例。

Proof-first 路线：

- 尝试把 C_3-free 条件转化为对近 C_4-extremal 图的稳定性或有效二分化定理，并以明确的误差 o(n^{3/2}) 为终点。
- 发展同时利用无三角形与任意两点至多一个公共邻点的加权两步路径/邻域交叠不等式，目标是直接改进 1/2 的常数。
- 研究若存在密度超过目标常数的极小反例，其局部邻域与补图必须满足的结构；任何归纳或剥离步骤须保留足够的主项精度。
- 最多安排一个计算子任务，且仅用于检验一个明确结构引理或寻找其小阶反例；结果出来即释放该槽位。

需要验证：

- 所有声称的上界必须对全部充分大 n 量化，而非只对素数幂、平衡二分图或稠密子序列。
- 构造必须逐一证明不含跨区域的 C_3 和 C_4，并给出精确边数与顶点数。
- 任何引用的稳定性、伪随机性或素数间隙定理都须核对适用对象、误差大小及是否引入未证猜想。
- 若发现 2026 年以后或未索引的解答声称，应先取得完整手稿并进行独立逐引理审计。

### 审计限制与人工复核理由

- 检索覆盖了当前数据库页、LaTeX 页、专属论坛、精确公式和关键短语、最新直接论文及 2025–2026 arXiv 结果；未发现解决声称。该搜索不能逻辑上排除未索引、延迟发表或私下流传的手稿。
- Kővári–Sós–Turán、Erdős–Simonovits和 Keevash–Sudakov–Verstraëte 的原始全文未逐页重审；其书目信息及所用结论由 Ma–Yang 的同行评审论文交叉支持，故这些历史条目在证据表中标为 indirect。
- 状态“confirmed_open”表示有近期同行评审直接陈述、近期数据库记录和定向更新检索的一致支持，不是对未来或所有隐藏文献的绝对证明。

- 无

<!-- DEEP_REVIEW:END -->
