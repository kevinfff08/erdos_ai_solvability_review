# Problem 61

## 基本信息

- 原始链接: https://www.erdosproblems.com/61
- LaTeX 页面: https://www.erdosproblems.com/latex/61
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

For any graph $H$ is there some $c=c(H)>0$ such that every graph $G$ on $n$ vertices that does not contain $H$ as an induced subgraph contains either a complete graph or independent set on $\geq n^c$ vertices?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `47/100`
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

- 计算/组合标签命中: graph theory
- 证明密集标签命中: 无
- 有限/计算线索: graph
- 渐近/无限线索: 无
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。完整解决 Erdős-Hajnal 猜想对 GPT-5.5 级别模型仍然不现实，但该问题已形式化、结构清楚、已有若干强特殊情形和闭包工具，因此模型配合计算、形式化证明和文献核查，可能在特定 H 类、证明整理、有限构型归约和反例排除方面产生有价值推进。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 最可行路线不是直接证明全称猜想，而是固定某一小型或结构受限的 H，复现并形式化已知技术，利用诱导子图枚举、Ramsey 型搜索、模块分解和顶点替换闭包寻找可验证的新归约；同时用自动证明或 Lean/Coq 辅助验证局部引理，计算检查小规模极值构型。

### 支持理由

- 问题表述简洁且已形式化，适合把核心命题、有限图操作、诱导子图禁止条件和团/独立集下界编码进证明助手或搜索程序。
- 已有结果显示若干小图、bull、C5、P5、路径类的弱形式以及顶点替换闭包可处理，说明存在可模块化复用的证明技术，而不是完全无结构的开放问题。
- 计算工具可系统枚举小 H-free 图、测试候选分解引理、发现极端例子模式，并帮助验证模型提出的有限归约。
- GPT-5.5 级别模型擅长文献综合、证明草图重构、形式化任务拆解和反例搜索脚本生成，这些能力与该问题的局部推进方式匹配。

### 主要障碍

- 这是 Erdős-Hajnal 猜想的全称形式，覆盖任意固定诱导禁图 H；已开放多年且近期进展仍只覆盖特殊图族或弱下界，说明缺少统一结构定理。
- 目标是多项式规模的团或独立集，下界强于当前备注中给出的次指数型通用结果，跨越较大的定量鸿沟。
- 诱导子图约束比普通子图约束更脆弱，常见极值图论工具不一定直接适用，模型容易生成看似合理但实际不成立的密度增量或正则性论证。
- 任意 H 的归纳或分解策略很容易被小型反例结构破坏，需要非常精细的结构分类和常数跟踪。

### 需要的验证

- 若模型声称证明新特殊情形，必须对每个结构引理做独立形式化或至少机器检查的有限配置验证。
- 需要复现已知结果中的关键定义和闭包操作，确认模型没有把非诱导版本、弱 Erdős-Hajnal 型结论或补图对称性误用为原猜想。
- 需要对小规模 H-free 图进行穷举或 SAT/SMT 搜索，寻找违反候选引理的最小反例。
- 若提出全局证明，必须审查常数依赖 c(H)>0 是否真正只依赖 H，且递归步骤不会把指数退化为次多项式。

### 公开版思考摘要

该问题具备形式化和计算辅助研究的入口，但其核心是著名的全称结构猜想。GPT-5.5 可能帮助推进局部图族、验证归约和发现证明漏洞；直接完成完整猜想的概率较低。综合判断为低到中等候选，而非完全不适合 AI。

### 免责声明

以上只是对 AI 辅助可推进性的评估，不是该 Erdős-Hajnal 猜想的证明，也不声称给出了新的数学结果。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_61.md](../../prompts/problem_61.md)

### 状态结论

Problem 61 是标准的 Erdős–Hajnal 猜想。当前问题页（2026-04-10 编辑）仍标为 open；2026 年新论文和预印本仍将其作为未解决的一般猜想，并仅证明新的特定禁图或受限图类。经检索未发现一个覆盖所有有限简单图 H 的完整证明或反例。因此，截至 2026-07-27，最审慎的结论是“很可能仍开放”。

### 当前规范陈述

对每个固定的有限简单图 H，存在常数 c(H)>0，使得对任意满足 n=|V(G)|≥1 的有限简单图 G，若 G 没有任何顶点子集 S 诱导出与 H 同构的图，则 max{ω(G),α(G)}≥n^{c(H)}。其中 ω(G) 为最大团大小，α(G) 为最大独立集（稳定集）大小。因集合大小为整数，该实数不等式等价于至少 ceil(n^{c(H)}) 个顶点。

```text
For every fixed finite simple graph H, there exists a constant c(H)>0 such that for every finite simple graph G with n=|V(G)|>=1, if no vertex subset S⊆V(G) induces a graph isomorphic to H, then max{ω(G),α(G)}>=n^{c(H)}. Here ω(G) is the maximum size of a clique and α(G) is the maximum size of an independent (stable) set. The real-valued inequality means that the relevant integral set has size at least ceil(n^{c(H)}).
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 在标准的“固定有限简单图 H”解释下，针对小参数和量词顺序未找到立即否定命题的构造。若脱离该惯例将 H 允许为无限图，则所有有限 G 都自动不含 H，从而命题退化为对任意有限图给出多项式 Ramsey 下界，显然不成立；这是原句类型约定缺失的后果，并非标准猜想的反例。
- 版本变化: 核心猜想未被改写。一般性下界从 Erdős–Hajnal 的 exp(c_H sqrt(log n)) 提升至 Bucić–Nguyen–Scott–Seymour 的 exp(c_H sqrt(log n log log n))，但仍为 n^{o(1)}。已解决禁图范围持续扩大：全部至多四顶点图、bull、C5、P5，并由顶点替换闭包推出全部五顶点图；2026 年又出现 E-graph（P5 的中间顶点添一条悬挂边）以及无穷多个 prime 图的结果。

陈述问题：

- 输入中的“any graph H”按该领域和原始文献的标准约定应为固定的有限简单图；若允许无限图、环或平行边，则不是标准 Erdős–Hajnal 猜想。
- “does not contain H as an induced subgraph”应同时保持 H 中的边与非边；这不同于通常的非诱导子图禁图。
- c 的量词位置至关重要：c 可依赖 H，但不可依赖 G 或 n。
- 输入未定义“complete graph”，但标准含义是 G 的一个顶点集所诱导的团，而非另行加入的图。

需要固定的量词/约定：

- H is fixed before c(H) is selected.
- The universal quantifier ranges over all finite simple induced-H-free graphs G of every order n>=1.
- The alternative is inclusive: either a clique or a stable set of the required size suffices, and both may exist.
- No exponent uniform in H is asserted.

### 文献与当前边界

已核验的主要结果：

- Erdős–Hajnal（1989，同行评议）提出该一般猜想，并给出 exp(c_H sqrt(log n)) 下界。
- Bucić–Nguyen–Scott–Seymour（2024，IMRN，同行评议）把适用于任意 H 的界提高为 exp(c_H sqrt(log n log log n))；这严格改进但仍是 n^{o(1)}。
- Alon–Pach–Solymosi（2001，同行评议）给出顶点替换闭包/prime 归约。Erdős–Hajnal 覆盖至多四顶点 H；Chudnovsky–Safra 处理 bull；Chudnovsky–Scott–Seymour–Spirkl 处理 C5；Nguyen–Scott–Seymour 处理 P5。最后一篇明确说明这完成了所有五顶点图。
- Nguyen–Scott–Seymour 的 2026 已接收论文证明无穷多个 prime 图及某些 buildable 图的 EH 性质；其路径论文对任意固定路径仅给出接近多项式而尚非多项式的界。
- Nguyen–Scott–Seymour（2025，同行评议）证明有界 VC-dimension 图的 EH 性质；该假设不由诱导 H-自由性普遍推出。

最近相关工作：截至审查日，Huang–Ju–Zhou 于 2026-06-04 发布的 arXiv:2606.06258 证明 E-graph 的特例；Sun–Wang–Zeng 于 2026-07-10 发布的 arXiv:2607.09049 改进有界 VC-dimension 图的指数依赖。两者均不覆盖任意固定 H。一般 H 的最佳已核实界仍是 2024 年 IMRN 的 loglog-step。

剩余核心：仍需证明或反驳：每个固定有限简单 H 都有正指数 c(H)，使每个诱导 H-自由图 G 满足 max{ω(G),α(G)}≥|G|^{c(H)}。现有一般界的指数随 n 趋于零，不能通过常数重命名变成该结论。

已使用方法：

- Rödl/Fox–Sudakov 型稀疏或稠密大诱导子图与纯对（pure pair）框架。
- Bucić–Nguyen–Scott–Seymour 的 blockade、按 |H| 归纳和由“少量诱导副本”得到结构的办法。
- 迭代稀疏化、comb/结构分解以及对 prime 图的顶点替换归约。
- 受限类的 VC-dimension 正则性方法。
- 补图对偶：H 的性质等价于补图 H̄ 的性质。

争议或不确定性：

- 问题页明确称其 open 标签仅为维护者的知识状态，不能单独证明开放性；本结论还依赖 2026 年论文/预印本仍把一般命题称为猜想，以及未发现可审查的一般证明或反例。
- 论坛中有 AI 辅助局部研究和 Lean 文件链接，但发帖者明确未声称证明 EH；其笔记及形式化范围未被本审查逐项编译或验证。
- 2026 年 Huang–Ju–Zhou 工作是预印本，尚未逐页复核其全部证明；它仅作为特例进展而非一般状态的决定性来源。

### 证据来源

- [Erdős Problems — Problem 61](https://www.erdosproblems.com/61) — Thomas F. Bloom / Erdős Problems project, 2026-04-10; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前条目将问题标为 open，给出标准表述、已解决的五顶点情形、一般下界和七条评论；页面也明确提醒其状态仅反映维护者的当前认识。
- [Erdős Problems — LaTeX source for Problem 61](https://www.erdosproblems.com/latex/61) — Thomas F. Bloom / Erdős Problems project, 2026-04-10; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 提供题目、备注和文献列表的 LaTeX 表述，用于核对输入转录。
- [61 Discussion Thread](https://www.erdosproblems.com/forum/thread/61) — Erdős Problems forum contributors, 2026-06-05; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 该线程链接 Huang–Ju–Zhou 的 2026 E-graph 预印本；另有用户明确表示其 AI 辅助笔记并非 EH 的证明，并请人审查若干局部命题。它不构成一般猜想的解答证据。
- [Ramsey-type theorems](https://doi.org/10.1016/0166-218X(89)90045-0) — Paul Erdős, András Hajnal, 1989-10; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原始同行评议论文；给出该猜想并证明一般的 exp(c_H sqrt(log n)) 型保证。
- [Induced Subgraph Density. I. A loglog Step Towards Erdős–Hajnal](https://doi.org/10.1093/imrn/rnae065) — Matija Bucić, Tung Nguyen, Alex Scott, Paul Seymour, 2024-06-01; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明任意固定 H 的诱导 H-自由图存在大小至少 exp(c_H sqrt(log n log log n)) 的团或稳定集；该界仍非多项式。
- [Ramsey-type Theorems with Forbidden Subgraphs](https://doi.org/10.1007/s004930100016) — Noga Alon, János Pach, József Solymosi, 2001-04; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明具有 Erdős–Hajnal 性质的禁图在顶点替换下封闭，并给出相关归约。
- [The Erdős–Hajnal conjecture for bull-free graphs](https://doi.org/10.1016/j.jctb.2008.02.005) — Maria Chudnovsky, Shmuel Safra, 2008-11; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明每个 bull-free n 顶点图都有至少 n^(1/4) 大小的团或稳定集。
- [Erdős–Hajnal for graphs with no 5-hole](https://doi.org/10.1112/plms.12504) — Maria Chudnovsky, Alex Scott, Paul Seymour, Sophie Spirkl, 2023-01-31; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明 H=C5 时 Erdős–Hajnal 猜想成立。
- [Induced subgraph density. VII. The five-vertex path](https://doi.org/10.1112/plms.70133) — Tung Nguyen, Alex Scott, Paul Seymour, 2026-03; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明 H=P5 时猜想成立，并明确说明结合 Alon–Pach–Solymosi 的替换闭包，五顶点图的验证完成。
- [Induced subgraph density. V. All paths approach Erdős-Hajnal](https://arxiv.org/abs/2307.15032) — Tung Nguyen, Alex Scott, Paul Seymour, 2023-07-27; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 对每个固定路径 H，证明近似界 2^((log n)^(1-o(1))；论文明确指出长路径的多项式猜想仍未解决。
- [Induced subgraph density. IV. New graphs with the Erdős–Hajnal property](https://ora.ox.ac.uk/objects/uuid%3Adb84da08-f522-45c5-8691-eb4108f14017) — Tung Nguyen, Alex Scott, Paul Seymour, 2026-04-07; `author_page`, `preprint`, directness=`direct`, reliability=`high`. 作者机构记录称该文已被 Transactions of the American Mathematical Society 接收；其摘要证明无穷多个 prime 图及更广 buildable 图条件下的 EH 性质，而非全体 H。
- [Erdős-Hajnal beyond the five-vertex path](https://arxiv.org/abs/2606.06258) — Shenwei Huang, Yiao Ju, Yidong Zhou, 2026-06-04; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 证明六顶点 E-graph（P5 的中间顶点增添一条悬挂边）满足 EH 性质；摘要仍把一般猜想称为 conjecture。
- [Induced subgraph density. VI. Bounded VC-dimension](https://arxiv.org/abs/2312.15572) — Tung Nguyen, Alex Scott, Paul Seymour, 2023-12-25; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明每个有界 VC-dimension 图类具有多项式 homogeneous-set 界；这是受限类结论而非所有诱导 H-自由图结论。期刊版本为 Advances in Mathematics 482 (2025), 110601。
- [Lean formalizations linked from Erdős Problems 61 forum](https://github.com/SamMausberg/lean-formalizations/tree/main/FormalConjectures/Problems/Erdos/E61) — Sam Mausberg, 2026; `formalization`, `formalized_artifact`, directness=`indirect`, reliability=`low`. 论坛作者称该仓库形式化了其若干有限局部陈述；未提供一般 Erdős–Hajnal 猜想的 Lean 完整证明，因此不能作为解题证据。

### 完成标准

- 肯定出口: Prove: for every finite simple graph H there is a number c(H)>0 such that every finite induced-H-free graph G satisfies max{ω(G),α(G)}>=|V(G)|^{c(H)}. The proof must establish the exponent for all graph orders, not merely asymptotically after choosing c from G.
- 否定出口: Prove the logical negation: exhibit one fixed finite simple graph H such that for every c>0 there exists a finite induced-H-free graph G with max{ω(G),α(G)}<|V(G)|^c. An equivalent sufficient certificate is an unbounded family for one fixed H with max{ω(G_i),α(G_i)}=|V(G_i)|^{o(1)}.

不构成完成：

- A proof for a finite list, or even infinitely many, of individual forbidden graphs without a theorem covering every finite H.
- An improved general lower bound that is still n^{o(1)}, including exp((log n)^a) for a<1.
- A theorem with added hypotheses, such as bounded VC-dimension, not implied by induced-H-freeness.
- A finite computation without an all-order proof, an infinite construction, or a certified induction.
- A proof that treats H-free as ordinary subgraph-free rather than induced-H-free.

正确性陷阱：

- Quantifier order: c may depend only on the fixed forbidden graph H.
- Induced containment requires verifying both edges and nonedges; ordinary subgraph containment is insufficient.
- A subpolynomial lower bound cannot be recast as n^c with fixed c>0.
- Any complement argument must simultaneously replace H by its complement and swap clique with stable set.
- Any substitution or decomposition recursion must preserve induced-H-freeness and retain a strictly positive final exponent.
- A purported counterexample needs one fixed H and arbitrarily large orders; a finite exception cannot refute the conjecture.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 目标定义精确、可审计且有丰富的结构性先例，但一般情形与已知一般界之间存在机制级而非参数级的鸿沟；它是低概率的 AI 研究候选。

支持理由：

- 肯定和否定结论都有明确、互斥且可逐行审计的完成标准。
- 存在可复用的 blockade、迭代稀疏化、替换闭包和补图对偶工具，以及一批近期特例。
- 对候选引理的反例、归约正确性和指数账本可独立检查。

主要障碍：

- 从 exp(c sqrt(log n log log n)) 到 n^{c(H)} 的提升不是微调常数，而需要新的普遍结构机制或反例机制。
- H 任意而且 prime 图情形已有无穷多例外地可解，已知特例的结构无法直接统一。
- 随机图提供小团/小稳定集，却通常含有固定 H 的诱导副本；反例路线同样受强约束。

Proof-first 路线：

- 尝试将一个明确的 blockade 长度、纯对或递归结构引理升级到足以产生固定正幂的形式，并全程记录指数损失。
- 研究最小反例在补图、顶点替换和模块分解下的严格闭包，寻求可证明地把一般 H 归约至更小的不可分解核心。
- 沿 2026 年的 prime/buildable 图和 E-graph 工作抽取一个可验证且可推广的结构条件；只有证明其覆盖所有 prime H 时才构成解法。
- 至多安排一个计算任务：预先固定某个候选结构引理、有限参数范围、同构消除方法、保存证书及停止条件；任务仅用来找反例或验证有限引理，不能替代全称证明。

需要验证：

- 在启动研究前再次检索 2026-07-27 后的 arXiv、期刊早发表和作者主页，以防状态变化。
- 逐页核验 2026 年 E-graph 预印本、已接收的 IV 论文以及其所用的 prime/替换归约。
- 若利用论坛 Lean 产物，必须在固定 commit 上编译并确认被形式化的定理究竟是什么，不能由目录名推断。

### 审计限制与人工复核理由

- 本审查使用公开可访问的页面、摘要、出版社/机构记录与 arXiv；并未逐页重建每篇论文的完整证明。
- 开放性不可能由有限检索逻辑证明；“likely_open”的置信度反映了当前问题页、2026 文献的用语和未发现一般性证明的共同证据。
- Erdős Problems 页面和论坛对直接抓取返回 403，故其内容来自可检索缓存；页面 URL、LaTeX URL 和论坛 URL 已记录但不能视为完整页面审读。
- 论坛链接的 Lean 产物未在本审查中编译；它们只被作为局部、非解答性形式化线索记录。
- 2026 年 7 月末之后可能出现新的预印本、勘误或已接受论文的正式版本。

- 交付给长期研究代理前，应重新检索 2026-07-27 之后的 arXiv 和作者主页，并人工确认没有新的全称解答。
- 若后续工作依赖“所有五顶点图”或 prime/buildable 图的合并归约，应从原论文逐步核验分类与顶点替换的适用条件。
- 如要使用论坛中的局部 Lean 陈述或 AI 辅助笔记，必须固定版本编译并人工核对其数学陈述及其与一般猜想的关系。

<!-- DEEP_REVIEW:END -->
