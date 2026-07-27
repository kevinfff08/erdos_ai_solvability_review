# Problem 85

## 基本信息

- 原始链接: https://www.erdosproblems.com/85
- LaTeX 页面: https://www.erdosproblems.com/latex/85
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `yes`
- OEIS: `A006672`, `possible`
- 原站备注字段: 无

## 原问题

Let $n\geq 4$ and $f(n)$ be minimal such that every graph on $n$ vertices with minimal degree $\geq f(n)$ contains a $C_4$. Is it true that, for all large $n$, $f(n+1)\geq f(n)$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `43/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 题面含渐近/无限对象线索：for all large, o(

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory
- 证明密集标签命中: 无
- 有限/计算线索: graph, ramsey
- 渐近/无限线索: for all large, o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **这个问题是中等候选：GPT-5.5 级别模型配合计算、SAT/ILP 反例搜索、形式化验证和文献检索，较可能显著推进或验证大量有限范围与等价表述，但直接给出最终的“充分大 n 单调性”证明把握不高。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 把 f(n) 改写为 C4-free 图的最大可能最小度加 1：令 g(n) 为 n 点无 C4 图的最大最小度，则问题等价于问 g(n) 是否最终非降。可行路线是先用 SAT/CP-SAT/ILP 精确计算小中等 n 的 g(n)，寻找下降点或稳定模式；再把候选极值图与已知 C4-free 构造、Ramsey 数 R(C4,K_{1,n}) 表述和形式化证明库连接起来，尝试证明一种“扩点保持最小度”或“下降只能有限次”的结构性引理。

### 支持理由

- 问题陈述短、对象明确，可以自然转化为有限图搜索和 Ramsey 数阈值问题，适合模型生成可验证的程序、SAT 编码和形式化陈述。
- f(n)=(1+o(1))sqrt(n) 且已有上界 f(n)<sqrt(n)+1，说明问题的主阶已知；剩余难点集中在整数级别的单调性，而这类问题可以通过精确计算和结构猜想获得实际进展。
- “formalized=yes”降低了验证门槛：模型若提出等价定义、有限检查或引理，可以用证明助手或独立程序核查。
- 模型可以系统搜索 C4-free 图的最大最小度，生成证书：存在性由图本身证明，不存在性可由 SAT unsat certificate 或穷举/ILP 证明辅助验证。
- 若存在反例序列，计算搜索有现实机会先发现小型或模式化反例；若长期无反例，也能形成可审计的数据支持和候选结构定理。

### 主要障碍

- 最终命题是渐近的全称命题，不能靠有限计算完成，除非找到可证明的结构性递推或有限归约。
- C4-free 图的高最小度构造高度依赖有限几何、正则性和数论参数；n 增加 1 时能否保持最小度可能受构造空缺影响，简单补点或删点论证不够。
- 已知 f(n) 的主项约为 sqrt(n)，但单调性只关心整数级波动；渐近上下界通常太粗，难以直接推出 f(n+1)>=f(n)。
- Ramsey 数 reformulation 有帮助，但也可能把问题转移到同样困难的星与 C4 Ramsey 数精确行为上。
- 自动图搜索规模会迅速爆炸；无 C4 加最小度约束虽可编码，但证明不存在性需要强剪枝、同构消除和可复核证书。

### 需要的验证

- 独立实现 g(n)=max minimum degree over C4-free n-vertex graphs 的精确搜索，并交叉验证 f(n)=g(n)+1。
- 对计算得到的每个下界保存具体图证书；对上界保存 SAT/ILP 不可满足证书或可复现穷举日志。
- 检查与给定 Ramsey reformulation 的变量对应是否完全一致，避免 n 与 m 的索引偏移错误。
- 如果提出扩点、删点或正则化引理，需要在证明助手中形式化核心陈述，或至少给出机器可检查的图论证明脚本。
- 对所有发现的下降点候选做独立程序复核，并测试是否由边界小 n、非连通图、孤立构造或编码 bug 导致。

### 公开版思考摘要

我把问题视为无 C4 图最大最小度函数的最终单调性问题。它很适合 AI 工具链做精确计算、证书生成、等价表述检查和结构猜想挖掘；这些工作能显著推进问题，尤其能验证大量有限范围并暴露潜在反例模式。但从已有信息看，主阶渐近估计不足以控制相邻整数的波动，最终证明仍需要新的结构性图论引理。因此它不是低难度可直接解决题，也不是纯粹不可碰的元问题，而是中等可攻候选。

### 免责声明

以上不是该 Erdős 问题的解答，也没有声称证明或否定最终单调性；只是评估 GPT-5.5 级别模型在工具辅助下可能完成的推进与验证工作。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_85.md](../../prompts/problem_85.md)

### 状态结论

截至审计日，题库当前页仍将 #85 标作开放，Formal Conjectures 也将其标为 research open；针对精确命题、C4–星图 Ramsey 数、作者与近年文献的检索没有发现可检查的证明或反例。2024 年 Boza 预印本推进了相关 Ramsey 数的小值和上界，但明确只给出有限值/特殊参数结果，未解决最终单调性。因此把此题作为定义良好的开放问题是合适的，但“开放”结论仍是基于有范围的文献检索而非逻辑穷尽。

### 当前规范陈述

对每个整数 n>=4，令 f(n) 为最小整数 d，使得每个恰有 n 个顶点、最小度 delta(G)>=d 的有限简单图 G 都含有一个 C4（作为非诱导子图）。等价地，f(n)=1+max{delta(G): G 是 n 顶点的 C4-自由有限简单图}。问题是：是否存在 N>=4，使所有 n>=N 都有 f(n+1)>=f(n)？

```text
For every integer n >= 4, let f(n) be the least integer d such that every finite simple graph G with |V(G)| = n and minimum degree delta(G) >= d contains C4 as a (not necessarily induced) subgraph. Equivalently, f(n) = 1 + max{delta(G) : G is a C4-free finite simple graph on n vertices}. Determine whether there exists an integer N >= 4 such that, for every integer n >= N, f(n+1) >= f(n).
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 已针对定义、n=4 基例、C4 是否诱导、以及题库所列 Ramsey 关系检查；未发现能否定主命题的简单构造。有限个下降或有限计算也不能否定“最终”单调性。备注中的第二个反解式疑有记号/索引问题，但这不是主命题的反例。
- 版本变化: 题库的 2025-10-20 修订记录显示，较早文字把 f(n)<sqrt(n)+1 归于 Erdos 1993、把渐近式归于 Erdos 1996，并提到 f(n)=sqrt(n)+O(1) 可能“过于乐观”；当前版本将这些表述汇总为问题 552 的已知界。主命题本身未被改写。

陈述问题：

- 原文的 “minimal degree” 应按图论惯例解释为 minimum degree（最小度），而不是极小度概念。
- C4 必须解释为普通子图而非诱导 C4；否则命题会改变。
- “for all large n”须量化为“存在单一 N，使每个 n>=N 成立”。
- 题库备注中第二个反解式 f(n)=min{m:m>=R(C4,K_{1,n-m})} 的变量和边界不清；以 n=4、f(4)=2 直接代入也不能可靠地使用该式。它不影响首行定义的精确性，故不应作为研究中的等价变换。
- 第一条 Ramsey 数关系可由补图中不存在 K_{1,t} 等价于原图最小度至少 m-t 验证；使用时必须保留其不等号方向和索引。

需要固定的量词/约定：

- All graphs are finite, simple, undirected graphs, and C4 is a non-induced subgraph.
- The phrase "for all large n" means: there exists N >= 4 such that for every integer n >= N, f(n+1) >= f(n).
- The least threshold d exists for n >= 4; indeed d <= n-1 since K_n contains C4.
- The equivalent extremal formulation is f(n)-1 = max delta(G) over n-vertex C4-free simple graphs.

### 文献与当前边界

已核验的主要结果：

- Burr、Erdős、Faudree、Rousseau、Schelp（1989，同行评议）提出/研究了 C4–星图 Ramsey 数问题；这给出了 #85 的 Ramsey 背景，但没有解决最终单调性。
- 由 C4-自由图的共同邻点双计数可得 delta(G)(delta(G)-1)<=n-1，因而 f(n)<sqrt(n)+1；结合射影平面/极性图构造可得 f(n)=(1+o(1))sqrt(n)。这些仅给出增长尺度，并不控制相邻 f 值的符号。
- Parsons（1975；由问题 552 汇总）在素数幂平方附近给出无穷多个精确 R(C4,K_{1,n}) 值；2017 年 Zhang–Chen–Cheng 继续通过极性图给出 q^2-t 参数的一族精确值。
- Chen（1997）证明 R(C4,K_{1,n+1})<=R(C4,K_{1,n})+2。这是 Ramsey 数的局部增量上界，不能自动转成 f(n+1)>=f(n)。
- Boza（2024，预印本）确定了 n<=37 的所有遗留小值，并给出特殊参数上界及相邻参数关系；其文中明确说更大参数的相关不等式尚无反例，但并未证明本题的最终全称命题。

最近相关工作：最直接的近期可检查来源是 Luis Boza 的 2024 arXiv 预印本（2409.12770），它补齐 n<=37 的八个未知 R(C4,K_{1,n}) 值，并在特殊同余类/平方附近建立上界。2025 年 Chen、Xuemei Zhang、Yanbo Zhang 的《Star-quadrilateral Ramsey Number and Beyond》为相关方向的同行评议专题工作；公开摘要不支持把它当作 #85 的解决。

剩余核心：仍需证明或否证：是否存在一个统一阈值 N，使每个 n>=N 的 n 顶点 C4-自由图最大可能最小度不随 n 增加而下降；等价地，f(n) 从某点起是否非递减。已知渐近量级、无穷多特殊精确 Ramsey 值、有限精确表和相邻 Ramsey 数至多加 2 都不足以给出该符号结论。

已使用方法：

- C4-自由图的共同邻点双计数、度数求和和极值上界。
- 有限射影平面、极性图及其删点/删边子图构造。
- 在 Ramsey 表达中转到补图的最大度约束。
- 小参数图枚举、极值边数数据库和精确 Ramsey 计算；这些只能支撑有明确停止条件的有限引理。

争议或不确定性：

- 题库 #85 与 #552 的 open 标签是维护者判断而非完备文献证明；本审计未发现相反的论文或可审计解答。
- Boza 2024 是预印本，虽然其具体陈述可阅读，仍应在依赖其小值/新引理前独立核对证明或后续发表状态。
- #85 备注中的第二个 Ramsey“反解式”变量范围不清，不能作为可靠等价式；应由主定义重新推导所需关系。
- 2025 年中文专题论文的公开英文摘要不足以逐条核验其全部定理，故只把它作为相关而非决定性证据。

### 证据来源

- [Erdős Problems – Problem 85](https://www.erdosproblems.com/85) — Thomas F. Bloom (database editor), 2025-12-06 (last edited, as displayed); `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前数据库记录把 #85 标为 open；给出主陈述、与问题 552 的关系、渐近备注，并显示没有论坛中的完整或部分解答声明。
- [Erdős Problems – LaTeX source for Problem 85](https://www.erdosproblems.com/latex/85) — Thomas F. Bloom (database editor), date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 直接核对了当前主陈述和备注的 LaTeX 文本；其中第二个“反解”式的变量范围未说明。
- [Revision history of Erdős Problem 85](https://www.erdosproblems.com/history/85) — Thomas F. Bloom (database editor), 2025-10-20 (shown prior revision); `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 记录了 2025 年的文字修订，并保留关于 Erdos 1993/1996 对界与更强估计的历史表述。
- [Erdős Problems – Problem 552](https://www.erdosproblems.com/552) — Thomas F. Bloom (database editor), 2026-02-01 (last edited, as displayed); `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前记录把确定 R(C4,K_{1,n}) 及一个更强的无穷多参数问题标为开放；总结 Parsons 及后续特殊参数精确值，并称所有已知情形只出现 n+ceil(sqrt(n))+{0,1}。
- [Some Complete Bipartite Graph–Tree Ramsey Numbers](https://www.sciencedirect.com/science/article/pii/S0167506008704527) — S. A. Burr, P. Erdős, R. J. Faudree, C. C. Rousseau, R. H. Schelp, 1989; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 该论文是 C4 对星图 Ramsey 数问题的原始联合来源之一；后续题库和历史页面据此定位问题。
- [A result on C4-star Ramsey numbers](https://doi.org/10.1016/0012-365X(95)00340-3) — Guantao Chen, 1997-01-15; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明 R(C4,K_{1,n+1}) <= R(C4,K_{1,n})+2；这是相关 Ramsey 数的已验证相邻参数控制，不能推出本题所问 f 的最终单调性。
- [Polarity graphs and Ramsey numbers for C4 versus stars](https://research.polyu.edu.hk/en/publications/polarity-graphs-and-ramsey-numbers-for-csub4subversus-stars/) — Xuemei Zhang, Yaojun Chen, Edwin Tai Chiu Cheng, 2017-04-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 利用有限域射影平面的极性图，证明了一族 q^2-t 参数的精确 R(C4,K_{1,q^2-t}) 值，扩展 Parsons 的特殊参数结果。
- [Some values of Ramsey numbers for C4 versus stars](https://dblp.org/rec/journals/ffa/ZhangCC17.html) — Xuemei Zhang, Yaojun Chen, T. C. Edwin Cheng, 2017; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 书目记录确认 2017 年 Finite Fields and Their Applications 论文及 DOI；它是题库列出的特殊参数精确值文献之一。
- [Exact Values and Bounds for Ramsey Numbers of C4 Versus a Star Graph](https://arxiv.org/abs/2409.12770) — Luis Boza, 2024-09-19; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 确定 n<=37 的八个先前未知值，给出若干特殊参数上界和关系式，并指出大参数下没有已知反例；未声称解决最终单调性。
- [Star-quadrilateral Ramsey Number and Beyond](https://ccj.pku.edu.cn/article/info?id=679227200979013) — Yaojun Chen, Xuemei Zhang, Yanbo Zhang, 2025; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`medium`. 2025 年关于星图–四边形 Ramsey 数及推广的专题工作，表明该研究线近期仍活跃；公开摘要未给出本题最终单调性的解决声明。
- [Formal Conjectures – ErdosProblems/85.lean](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/85.lean) — Formal Conjectures Authors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. Lean 文件形式化了 f(n) 的阈值定义和 eventually (f n <= f(n+1))，类别为 research open；该文件以 sorry 结束，故是陈述形式化而非证明。

### 完成标准

- 肯定出口: Prove that there is an explicit or existential N >= 4 such that for every integer n >= N, every n-vertex C4-free simple graph has minimum degree at most f(n+1)-1; equivalently prove f(n+1) >= f(n) for every n >= N.
- 否定出口: Prove that for every N there is an integer n >= N with f(n+1) < f(n); equivalently construct or certify infinitely many strict descents of the C4-free minimum-degree threshold.

不构成完成：

- Computing f(n), R(C4,K1,n), or candidate extremal graphs for any finite range, without a theorem covering all later n.
- Showing f(n)=(1+o(1))sqrt(n), or even proving a bounded-drop estimate f(m)>f(n)-c for m>n.
- Proving only R(C4,K1,n+1)<=R(C4,K1,n)+2, or another Ramsey increment inequality not rigorously shown equivalent to eventual monotonicity of f.
- Establishing monotonicity only on a subsequence such as prime-power-square parameters.
- Using an induced-C4 statement, an average-degree bound, or an edge-extremal result in place of the required minimum-degree threshold without a valid reduction.

正确性陷阱：

- The target is eventual monotonicity: the proof must supply one threshold N and cover every subsequent integer n.
- C4 means a non-induced subgraph. A graph with chords can still contain C4.
- Keep f(n) distinct from the Ramsey number R(C4,K1,n); their arguments and index shifts differ.
- When using complements, absence of K1,t in the complement is a maximum-degree condition there and a minimum-degree condition in the original graph. Check every off-by-one.
- A construction with many edges need not have large minimum degree; deleting low-degree vertices or proving regularity requires justification.
- Do not rely on the ambiguous second inverse formula in the database remark; derive any conversion from the definitions.
- A finite computer search cannot decide an eventually quantified statement unless embedded in a proved finite-reduction theorem.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `24/100`
- 信心: `medium`
- 结论: 这是一个定义清楚、可被形式化的开放问题，但其核心是对所有足够大 n 的精确相邻阈值比较，现有结果主要是渐近界、特殊无穷子列和有限表。对 AI 而言可审计的局部引理很多，但从这些引理到统一最终单调性仍有实质结构缺口。

支持理由：

- 主命题具有明确的存在—全称量词结构，且已有 Lean 陈述可用作形式审计基准。
- C4-自由图的局部共同邻点限制、极性图构造和 Ramsey 等价提供多个可独立验证的理论入口。
- 2024 年工作留下可检查的具体不等式与小值，但没有表明问题已接近机械收尾。

主要障碍：

- 渐近 f(n)~sqrt(n) 允许无限次小幅下降，因而不能推导最终单调性。
- 极性图只在高度算术化的参数子列上给出极值或近极值结构，难以控制每一个相邻 n。
- 最小度极值函数比边数 extremal number 更敏感；高边数构造和平均度估计不能直接比较 f(n)、f(n+1)。
- 题库备注中的一个逆向 Ramsey 公式不宜无审计使用。

Proof-first 路线：

- 先建立严格的桥梁引理：将任何潜在下降 f(n+1)<f(n) 转译为 n 或 n+1 顶点 C4-自由近正则图的可证结构约束，再寻求用共同邻点计数排除该结构。
- 研究极值/近极值 C4-自由最小度图的加点、删点或局部交换原理；只有能处理所有大 n 的结构定理才构成路线。
- 在 Ramsey 表述中使用 Chen 的相邻增量界与 Boza 的参数关系，但每一步须重新证明其对 f 单调性确有蕴涵。
- 可选的一次计算仅可用于验证一个精确定义的有限结构引理或寻找最小反例模式；不能把扩展数表当作主路线。

需要验证：

- 在任何论文或预印本声称解决前，检索 arXiv 新版本、期刊发表、作者主页及题库论坛更新。
- 逐行核对 Boza 2024 中拟使用的具体引理及其适用的 n、奇偶和同余条件。
- 若采用 Ramsey 转换，独立从补图定义复核每个参数、阈值与不等号。
- 若使用 Lean 文件，注意其是含 sorry 的陈述而不是已验证证明。

### 审计限制与人工复核理由

- 题库 #85 主页面在直接打开时出现访问限制；通过搜索缓存、LaTeX 页面与修订史交叉核对了陈述和状态。
- 没有发现 2025–2026 年解决本题的论文或形式化证明，但这种检索结果不是不存在证明的逻辑证明。
- 2025 年《Star-quadrilateral Ramsey Number and Beyond》的公开摘要主要描述推广主题，未能逐页审计其全部定理；没有据此作任何强的未解决性推断。
- Boza 2024 仍标为预印本，本审计只使用了其可公开检查的摘要和正文陈述，不把它当作已同行评议的终局来源。

- 建议专家复核 #85 备注中第二个 Ramsey 反解式的原始排版/意图；该式不应用于后续证明。
- 若研究计划将依赖 Boza 2024 的新引理或 2025 专题论文，应逐条复核原文证明与发表状态。
- 最终开放性判断虽有当前题库、形式化记录和定向检索支持，仍应在启动长期攻关前再检索最新 arXiv、作者主页和题库论坛。

<!-- DEEP_REVIEW:END -->
