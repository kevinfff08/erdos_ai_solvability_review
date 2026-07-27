# Problem 81

## 基本信息

- 原始链接: https://www.erdosproblems.com/81
- LaTeX 页面: https://www.erdosproblems.com/latex/81
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $G$ be a chordal graph on $n$ vertices - that is, $G$ has no induced cycles of length greater than $3$. Can the edges of $G$ be partitioned into $n^2/6+O(n)$ many cliques?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `34/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：o(

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
- 模型: `GPT-5.5 + 计算/形式化证明/文献检索/反例搜索工具`
- 结论: **低到中等候选。该问题结构非常明确，且 chordal graph 有强结构工具，模型有希望做出有价值推进，例如重构已知上界、验证若干归约、系统搜索极值构型、或把 split graph/特殊 chordal 类的常数往 n^2/6 推近。但要完整证明 n^2/6+O(n) 对所有 chordal graph 成立，仍像是需要新的极值结构论证，不能仅靠常规计算或形式化验证直接完成。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 最现实路线是利用 chordal graph 的完美消除序、最大团树或 split graph 子类，把边团划分问题转化为按顶点邻域递推的组合优化问题；再用整数规划/SAT 搜索小规模极值例子，猜测局部归约或势函数；随后尝试证明每一步消除只需摊还不超过目标常数。形式化证明工具更适合验证已经发现的归约和计数不等式，而不是独立发现核心不等式。

### 支持理由

- 问题陈述短且对象单一：chordal graph、边划分为 cliques、目标常数 n^2/6+O(n)，适合模型与计算工具建立清晰的实验框架。
- chordal graph 有强结构：无长诱导圈、存在递归消除结构，这给自动化归约、动态规划式搜索和证明草图提供了入口。
- 备注中已经给出下界构造和两个上界层级：一般 chordal graph 有约 1/4 常数的上界，split graph 有 3/16 常数的上界；这些信息足以指导模型围绕常数差距设计实验。
- 目标是渐近上界而非精确公式，允许 O(n) 误差，这通常让摊还计数、异常小结构处理和计算辅助验证更可行。
- 即便不能解决全问题，模型可显著推进：检查特殊子类、发现潜在极值族、生成反例搜索证据、形式化已有或新归约。

### 主要障碍

- 核心难点是把一般 chordal graph 的局部团结构压到 n^2/6 常数；现有备注显示已知上界与目标仍有明显常数差距。
- split graph 已是 chordal 的重要子类，但已知上界仍为 3/16 n^2+O(n)，高于 1/6；因此即使处理 split graph 也可能需要新想法。
- 边划分为 cliques 要求每条边恰好归入一个 clique，不只是覆盖；这会让局部选择相互牵制，简单贪心或最大团分解未必接近最优。
- 反例搜索只能覆盖有限 n，且 O(n) 误差会掩盖小规模行为；计算证据难以直接证明渐近常数。
- 形式化证明系统可以降低错误率，但前提是已有清晰的人类可读证明路线；它不太可能单独弥补缺失的极值论证。

### 需要的验证

- 实现 chordal graph 生成与边团划分最优化模型，计算小 n 的最优值并记录极值构型。
- 单独验证备注中的下界构造确实需要 n^2/6+O(n) 个 clique，并分析其唯一性或稳定性。
- 重建已知一般 chordal 上界和 split graph 上界的证明框架，确认模型理解的归约没有误读。
- 对 split graph、interval graph、block graph、有限最大团大小等子类分别测试是否能达到 n^2/6+O(n)。
- 若提出新证明，应将关键递推、摊还不等式和边划分构造形式化或至少用独立程序检查大量随机/极值实例。

### 公开版思考摘要

这是一个适合 AI 做结构化推进但不适合轻易宣称可完全解决的问题。给定 JSON 显示它有明确的极值常数、已知下界构造、以及仍有常数级差距的上界。GPT-5.5 级模型可利用 chordal graph 的递归结构和计算搜索建立候选证明路线，尤其适合发现局部归约、特殊类证明和极值构型证据；但把这些证据提升为全体 chordal graph 的 n^2/6+O(n) 上界，仍需要关键新不等式或稳定性分析。

### 免责声明

以上是对 AI 辅助可攻性的审查，不是该 Erdős 问题的解答，也没有声称证明或反驳 n^2/6+O(n) 上界。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_81.md](../../prompts/problem_81.md)

### 状态结论

截至审计日，原问题仍很可能开放。当前 Erdős Problems 页面及其讨论帖均明确标为 open；检索到的 2026 年新材料包括条件性结果、对旧上界的 Lean 形式化，以及与分数三角形打包/覆盖有关的形式化预印本，但它们都明确不推出整数边-团分割上界。一个 LinkedIn 帖曾声称解决了问题，但其关联的公开 GitHub 仓库后来明确写明“#81 remains open”，并说明完整稿件尚不构成解答。

### 当前规范陈述

对有限简单图 G，令 cp(G) 为满足下列条件的最小 k：存在 G 的若干含边完全子图 C_1,...,C_k，使 E(G[C_i]) 两两不交且并集恰为 E(G)。弦图指不含长度至少 4 的诱导圈的图。是否存在绝对常数 C，使得对每个 n≥1 以及每个 n 顶点弦图 G，均有 cp(G)≤n²/6+Cn？

```text
For a finite simple graph G, let cp(G) be the least number k for which there are cliques C_1,...,C_k of G, each with at least one edge, such that the edge sets E(G[C_i]) are pairwise disjoint and their union is E(G). A graph is chordal if it has no induced cycle of length at least four. Does there exist an absolute constant C such that, for every integer n >= 1 and every n-vertex chordal graph G, cp(G) <= n^2/6 + Cn?
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未找到否定字面命题的简单构造。相反，Chen–Erdős–Ordman 的作者托管论文给出 complete-split 图 G_n=K_n-\overline{K}_{2n/3}（6|n）并陈述 cp(G_n)=n²/6+n/6；这只显示主项 1/6 及线性误差的必要性。
- 版本变化: 未发现将原命题正式改写为非等价版本的已发表修订。2026 年的分数三角形打包/覆盖工作和 wCDH 条件结果均是相关但更弱的目标；其作者或发布者明确说明它们不建立整数 clique-partition 结论。

陈述问题：

- “将边 partitioned into cliques”按 EOZ93/CEO94 的术语应理解为完全子图的边集恰好分割 E(G)，而不是允许重叠的 edge clique cover，也不是将顶点集分割成团。
- “n²/6+O(n) many”须作统一量词解释：存在与 n、G 无关的绝对常数 C；通常语义是“至多”该数目。
- 原始页面所举构造在 n 被 6 整除时的精确值为 n²/6+n/6；它证明线性余项一般不可省去，但不是对 n²/6+O(n) 的反例。

需要固定的量词/约定：

- The selected cliques may share vertices but may not share edges.
- The O(n) is uniform: there must be one absolute constant C valid simultaneously for all n and all n-vertex chordal graphs.
- Cliques of order zero or one are irrelevant and may be omitted; all graph edges must occur exactly once.

### 文献与当前边界

已核验的主要结果：

- Erdős–Ordman–Zalcstein（1993，同行评审）证明：存在绝对 c>0，使每个 n 顶点弦图可作至多 (1-c)n²/4 个团的边分割；其摘要同时把 1/6 阈值表述为未知。
- Chen–Erdős–Ordman（1994，已发表会议论文集，同行评审状态未由可访问页面确认）证明每个 split graph 有 (3/16)n²+O(n) 的边-团分割；并处理 K_n-\overline{K}_m 的特殊情形。
- 对于 complete-split 下界族 K_n-\overline{K}_{2n/3}（6|n），CEO94 陈述精确 cp=n²/6+n/6。这既给出主项 1/6 的必要性，也显示一般情况下不能把线性项替换成 o(n)。
- 2026 年公开 Lean 文件自称把 EOZ93 的正 c 上界具体化为 c≥1/133；其源码未含 sorry/axiom 文本匹配，但本审计未在本地重建该项目，故应作为可复查形式化工件而非独立同行评审结果。
- Traverso 的公开预印本/Lean 工件给出 split graph 的分数三角形打包不等式 |E|-2ν₃*≤n²/6+n，以及弦图上的分数三角形覆盖泛函极值；仓库明确否认它们已推出整数边-团分割上界。

最近相关工作：所找到的最新直接相关材料为 2026 年论坛中的 wCDH 条件性说明、旧 EOZ 上界的 Lean 文件，以及 Traverso 的未同行评审分数目标/Lean 工件。它们提供潜在结构信息，但均没有可验证地关闭原问题；另有 2026 年初公开声称解答的社交媒体帖，关联仓库现明确写作问题仍开放。

剩余核心：证明或否证统一整数不等式 cp(G)≤n²/6+Cn。分数三角形打包/覆盖估计、只针对 split graph 的结果、以及假设 wCDH 的结果都不能自动转化为这一结论；关键剩余障碍是从局部/分数信息获得无重边的整数团分割，并在一般弦图上保持精确主项。

已使用方法：

- EOZ93 的全体弦图上界，以及 CEO94 的 split/threshold 图构造和估计。
- 利用 complete-split 图和完美匹配分解构造、分析极值下界族。
- 弦图的诱导圈定义、完美消除序、极大团与团树/团粘合结构所支持的归纳或摊还分解。
- 近期形式化工作中的分数三角形打包/覆盖泛函与可机检的有限不等式。

争议或不确定性：

- EOZ93 全文并未从出版商页面开放；其主要摘要结论已直接核验，但未据此重建其证明细节。
- wCDH 笔记的链接已被记录在论坛，但本审计无法打开其 Zenodo 条目，因此只按论坛作者的“条件性且不解原题”自述处理。
- LinkedIn 的解答声称没有附可审阅的全体弦图证明，且同一研究计划的可访问仓库现明确称 #81 开放；应视为未证实且被后续澄清的声称。
- 未找到 2023–2026 年 arXiv 或期刊中直接证明或反驳原整数命题的论文；这是积极检索结果而非不存在此类工作的逻辑证明。

### 证据来源

- [Erdős Problems — Problem 81](https://www.erdosproblems.com/81) — Thomas F. Bloom / Erdős Problems, 2025-12-28; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 当前记录将问题标为 open，并给出 EOZ93 的 (1/4-ε)n² 上界、CEO94 的 split graph 上界及下界构造说明；该数据库标签不是单独的解决性证明。
- [81 Discussion Thread | Erdős Problems](https://www.erdosproblems.com/forum/thread/81) — Thomas F. Bloom / forum contributors, 2026-06-20; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 讨论帖仍标注 OPEN；帖内明确警告评论未经核验。它记录了 wCDH 条件性结果的自述以及 EOZ93 明确常数上界的形式化链接，均不声称解决原问题。
- [Clique Partitions of Chordal Graphs](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/clique-partitions-of-chordal-graphs/CEA1F929F2A88B5A4C7C8E23DFD0DD29) — Paul Erdős, Edward T. Ordman, Yechezkel Zalcstein, 1993-12; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 摘要直接陈述：存在弦图需要 n²/6 个团，未知这是否总足够；并证明对某个 c>0，(1-c)n²/4 个团总足够。
- [Clique Partitions of Split Graphs](https://ordman.net/MathResearch/CEOClique_Parts.pdf) — Guan-Tao Chen, Paul Erdős, Edward T. Ordman, 1994; `primary_paper`, `unknown`, directness=`direct`, reliability=`high`. 论文定义 edge clique partition 与 cp(G)，其摘要给出任意 split graph 的 (3/16)n²+O(n) 上界；并陈述当 6|n 时 G_n=K_n-\overline{K}_{2n/3} 的精确值 cp(G_n)=n²/6+n/6。
- [ErdosProblem81.lean](https://github.com/Woett/Lean-files/blob/main/ErdosProblem81.lean) — Woett / Lean-files contributors, 2026-06-19; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`medium`. 源码注释将目标表述为把 EOZ93 的 c₀ 提升到 1/12+o(1)，并声称形式化了旧的显式上界 cp(G)≤(1/4-c₀)n²、c₀≥1/133；这不是原问题的形式化解答。
- [Erdős Problem #81 — Chordal Clique Partitions](https://github.com/jtraverso/erdos-81-chordal-clique-partitions) — Juan Pablo Traverso Gianini, date unknown; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`medium`. 仓库明确称 #81 remains open。其 Paper I/II 是未外部同行评审的、带 Lean 工件的分数三角形打包/覆盖结果；仓库明确声明它们不建立整数 cp(G)≤n²/6+O(n) 或所有弦图的结论。
- [Rebecca Whitman — Research](https://sites.google.com/view/rebeccawhitman/research) — Rebecca Whitman, date unknown; `author_page`, `informal_claim`, directness=`direct`, reliability=`medium`. 作者页面列有与 Henderson、Koerts、Roberge、Spirkl 合作的“Clique Partitions of Split Graphs”处于 in preparation 状态；未提供可检查定理，因而不改变状态。
- [Juan Pablo Traverso LinkedIn announcement concerning Erdős Problem 81](https://es.linkedin.com/posts/jtraverso_github-jtraversoerdos-81-chordal-clique-partitions-activity-7477779073935732736-eg9K) — Juan Pablo Traverso Gianini, date unknown; `other`, `informal_claim`, directness=`direct`, reliability=`low`. 该帖曾宣称常数为 1/6，但同时说明完整稿件仍在润色和形式验证阶段；后续可访问的关联 GitHub 仓库明确撤回解决性表述并称问题开放。因此该帖不是可接受的解答证据。

### 完成标准

- 肯定出口: Give a proof with an absolute constant C such that every finite n-vertex chordal graph G has an edge clique partition of cardinality at most n^2/6 + Cn.
- 否定出口: Prove that no such absolute C exists; equivalently, exhibit chordal graphs G_i with n_i vertices and (cp(G_i)-n_i^2/6)/n_i unbounded.

不构成完成：

- A clique edge cover in which an edge is allowed to belong to more than one clique.
- A bound with quadratic leading constant greater than 1/6.
- A theorem restricted to split, threshold, interval, bounded-clique-number, or any other proper subclass without a valid reduction to all chordal graphs.
- A fractional triangle packing or fractional triangle cover inequality without an integral rounding theorem that yields an edge partition.
- A conditional theorem, including one assuming wCDH, without proving the condition for every chordal graph.
- Finite computation, a finite list of extremizers, or a formalization of EOZ93's older (1/4-c)n^2 bound.

正确性陷阱：

- Every edge must occur in exactly one clique; vertex overlap is allowed, edge overlap is not.
- Do not confuse an edge clique partition with a vertex partition into cliques or with a clique cover.
- The constant in O(n) must be absolute and uniform over G and n.
- Any fractional-to-integral step must control its integrality loss by O(n), not o(n^2) with an uncontrolled coefficient.
- A reduction by clique-sums, deletion, or a perfect elimination ordering must preserve or quantitatively bound cp, including edges in separators.
- Check small orders and all rounding terms; the lower family has an exact n^2/6+n/6 value only under its stated divisibility convention.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `28/100`
- 信心: `medium`
- 结论: 这是一个定义清晰、可审计但长期未解的极值问题；AI 可协助探索结构归约和可验证引理，但目前没有显示出接近完整解答的窄缺口。

支持理由：

- 目标可以精确写成 cp(G) 的统一不等式，正反完成条件明确。
- 弦图具有完美消除序和团树结构，适合把候选引理写成有限、可反驳的归纳或摊还命题。
- 下界极值族、已有全局上界、split graph 改进和近期分数形式化结果为研究提供了可比较基准。

主要障碍：

- 从约 1/4 主项精确降至 1/6 的差距很大，且原问题已公开数十年。
- 近期分数结果明确不提供整数边分割或一般弦图上的渐近转移；整性损失是核心而非技术性细节。
- 弦图的团可重叠顶点，局部选择易造成边重复或使分离团上的会计失效。
- 有限实验不能证明统一 O(n) 误差，也不能排除稀有的非 split 弦图极值族。

Proof-first 路线：

- 研究是否存在以极大团、极小分离团或完美消除序为单位的递归不变量，其每一步成本可摊还到 n²/6+O(n)。
- 尝试严格证明最坏例可归约到 complete-split 或受控 clique-sum 结构；若不能，构造可量化的归约失败族。
- 把分数三角形打包/覆盖工件视为启发式下界/势函数，优先寻找 O(n) 整数舍入定理或明确的整性缺口反例。
- 将任何反例搜索限定为一个具体结构引理，例如“给定规模和团树形状是否存在违反候选局部不等式的图”，并要求可检查证书。

需要验证：

- 在依赖 EOZ93 证明机制前，取得并逐段核读论文全文。
- 对 Woett 与 Traverso 的 Lean 工件在固定版本依赖下独立运行 lake build，并核对实际形式化陈述是否等于文中声称的命题。
- 持续检查 Whitman 等人的 in-preparation 工作是否公开为预印本或同行评审论文。
- 若任何新解答声称出现，要求其给出全体弦图的完整整数边分割证明，而非时间戳、哈希、分数结果或待公开草稿。

### 审计限制与人工复核理由

- 本审计未能获得 EOZ93 出版商全文，因而只把其出版商摘要所直接支持的结论列为已核验，不声称重建了其证明。
- wCDH 相关 Zenodo 条目无法在本次浏览会话中打开；其内容仅按论坛帖作者的说明记录，未作为独立定理使用。
- 公开 Lean 项目和分数预印本的仓库文本已被检查，但本审计在只读环境中未实际运行其依赖安装与 lake build。
- 尽管进行了精确短语、作者、问题号、arXiv、近期文献和形式化仓库检索，未发现解决论文并不能逻辑证明不存在未索引、未公开或将来出现的解答。

- 近期出现过社交媒体解答声称、条件性论坛材料和未同行评审的形式化预印本；在启动大规模研究前，应由人工再次检查它们的版本、提交记录和可能新公开的完整稿件。
- 若研究路线需要 EOZ93 的具体结构引理或常数，应先取得原论文全文并核对原命题、量词和证明依赖。

<!-- DEEP_REVIEW:END -->
