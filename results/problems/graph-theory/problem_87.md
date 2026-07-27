# Problem 87

## 基本信息

- 原始链接: https://www.erdosproblems.com/87
- LaTeX 页面: https://www.erdosproblems.com/latex/87
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`
- 形式化状态: `no`
- OEIS: `A059442`, `possible`
- 原站备注字段: 无

## 原问题

Let $\epsilon >0$. Is it true that, if $k$ is sufficiently large, then\[R(G)>(1-\epsilon)^kR(k)\]for every graph $G$ with chromatic number $\chi(G)=k$?

Even stronger, is there some $c>0$ such that, for all large $k$, $R(G)>cR(k)$ for every graph $G$ with chromatic number $\chi(G)=k$?

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

- 题面含渐近/无限对象线索：\gg, asymptotic, for all large, sufficiently large

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: chromatic, colouring, graph, ramsey
- 渐近/无限线索: \gg, asymptotic, for all large, sufficiently large
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。GPT-5.5 级模型较可能形式化并复核已知的随机着色下界、建立小规模反例搜索流程，并把问题推进到更清晰的极值函数表述；但直接解决任一渐近断言，尤其强形式“存在常数 c 使 R(G)>cR(k)”，很可能需要新的 Ramsey 理论思想，不能主要依赖计算或形式化验证完成。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 将问题重述为 f(k)=min_{χ(G)=k} R(G) 与 R(k) 的比较；先形式化 k-critical 子图给出的边数下界，并验证随机着色证明 R(G) 至少为约 2^{k/2} 量级；再用 SAT/ILP、canonical graph generation 和 Ramsey witness 搜索小 k 的低 Ramsey 数 k-色图，寻找可能的结构模式；最后尝试把模式转化为一般构造或把随机/容器/熵方法强化为相对 R(k) 的下界。

### 支持理由

- 问题陈述短、目标清晰，适合被拆成极值函数、随机下界、有限搜索和形式化验证几个子任务。
- 备注中已经给出可机器复核的基线：任意 k-色图有 R(G) 约大于 2^{k/2}，这为形式化证明和常数优化提供入口。
- 小 k 的反例或近反例可以通过 Ramsey SAT 编码、图生成和证书验证推进，模型可辅助设计搜索空间和解释结构。
- 该问题不要求精确求出 R(k)，因此存在通过相对不等式或条件化框架取得部分推进的可能。

### 主要障碍

- 核心困难是要与未知的对角 Ramsey 数 R(k) 比较；目前备注给出的通用下界只匹配 R(k) 的已知下界量级，而不是实际 R(k) 或最佳上界。
- 命题对所有 χ(G)=k 的图成立，最坏图可能是稀疏、临界、非规则或由特殊构造产生，搜索得到的小规模模式未必能外推。
- 强形式 R(G)>cR(k) 比第一问更刚性；即使证明第一问，也未必能给出固定比例。
- 有限计算很快遇到 Ramsey 数和 k-临界图枚举爆炸，最多提供证据、候选构造或可验证证书，难以单独证明渐近结论。

### 需要的验证

- 明确采用的 R(G) 与 R(k) 定义，并核对是否为二色无向 Ramsey 数。
- 对随机着色下界给出可审计证明，最好形式化到 Lean/Isabelle 或至少生成独立可检查的概率论推导。
- 若做计算搜索，需要保存完整 witness coloring、不可嵌入证书、SAT UNSAT 证书和图同构去重记录。
- 若提出新构造或新下界，需要验证其对所有足够大 k 成立，而不是只覆盖特殊图族。
- 若允许文献检索，需要确认已有关于最小 k-色图 Ramsey 数的结果，避免重复已知定理。

### 公开版思考摘要

这个问题适合 AI 工具链做“结构化推进”：整理等价极值函数、验证基线下界、生成小规模证据、搜索候选最坏图族。但它要求把任意 k-色图的 Ramsey 数同 R(k) 的真实增长联系起来，而 R(k) 本身高度未知，所以完整解决概率偏低。最现实的产出是可信的部分定理、反例搜索报告、形式化的已知下界，以及可能的新猜想或受限图族结果。

### 免责声明

以上只是对 GPT-5.5 级模型可推进性的审查，不是该 Erdős 问题的证明、反例或最终数学结论。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `revised_open`
- 状态信心: `medium`
- 可行动性: `needs_human_clarification`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_87.md](../../prompts/problem_87.md)

### 状态结论

按字面量词，第一问已被一个初等反例否定：取 ε=2、任意充分大的偶数 k 及 G=K_k，则要求 R(k)>R(k)，矛盾。因此“ε>0”不能照字面保留。网页备注“ε≥3/4 时平凡”显示其显然意图是 0<ε<1；在这一修复下，及对独立的常数因子强版本，本次检索未找到已验证的解答，当前 Erdős Problems 讨论页仍标为 Open（2026-01-17 编辑、0 条评论）。故该记录只能作为需人工确认修复后的开放目标处理，而非照原文直接求解。

### 当前规范陈述

字面第一问为：对每个实数 ε>0，是否存在 k_0(ε)，使得对每个 k≥k_0(ε) 和每个满足 χ(G)=k 的有限简单图 G，均有 R(G)>(1−ε)^kR(K_k)？其中 R(H) 是 H 的通常二色对角 Ramsey 数。该字面命题为假。显然意图的修复是将 ε 限定为 0<ε<1。独立的“更强”目标为：是否存在绝对常数 c>0,k_0，使得对所有 k≥k_0 及所有 χ(G)=k 的有限简单图 G，R(G)>cR(K_k)？

```text
Literal first question: for every real ε>0, does there exist k_0(ε) such that for every integer k≥k_0(ε) and every finite simple graph G with χ(G)=k, R(G)>(1−ε)^kR(K_k)? Here R(H) is the ordinary two-colour diagonal Ramsey number of H. This literal proposition is false. The evidently intended repaired question is the same assertion with 0<ε<1. Separately, the stated stronger target is: do there exist absolute constants c>0 and k_0 such that R(G)>cR(K_k) for every k≥k_0 and every finite simple G with χ(G)=k?
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `counterexample_found`
- 检查说明: 取 ε=2。若 k 为偶数且 G=K_k，则 χ(G)=k，且右端为 (1−2)^kR(k)=R(k)，字面不等式成为 R(K_k)>R(k)，即 R(k)>R(k)，矛盾。存在任意大的偶数 k，因此没有任何 k_0(2) 能使字面第一问成立。这不触及修复后 0<ε<1 的问题，也不触及常数因子强版本。
- 版本变化: Erdős 的历史强猜想是 R(G)≥R(K_k)（χ(G)≥k）。Faudree–McKay（1993）证明六顶点轮图 W_6 的 R(W_6)=17，而 R(K_4)=18，从而在 k=4 推翻它。当前 Erdős Problems 页面将研究目标改为两个渐近弱化版本，并于 2026-01-17 仍标 Open；但页面没有显式将“ε>0”修为“0<ε<1”。页面自身关于 ε≥3/4 的备注表明该范围限制是其意图。

陈述问题：

- “ε>0”缺少通常但必需的限制 0<ε<1。若 ε≥1，(1−ε)^k 的符号或大小不再表达“指数损失”，且字面命题可立即失败。
- 输入未定义 R(G)、R(k) 与图类；按原始论文、当前页面和 Ramsey 语境，唯一自然重建是有限简单图的通常二色对角 Ramsey 数，R(k)=R(K_k)。
- “if k is sufficiently large”须理解为：第一问中 k_0 可依赖 ε；强版本中 c、k_0 均不依赖 G、k。
- 旧版 UCSD 问题页的相关条目写成“n sufficiently large”，而当前页面写“k sufficiently large”。前者在量词上是不同且可能退化的目标，不能与当前文本混用。
- 近期文献中的“chromatic Ramsey number”R_χ(G)是宿主图色数参数，不是此处的普通 Ramsey 数 R(G)；符号/术语混淆会造成错误迁移。

需要固定的量词/约定：

- The literal first question quantifies over every ε>0; this is exactly what makes it false.
- For the repaired first question, quantify 0<ε<1, then allow k_0 to depend on ε but not on G.
- The stronger question requires one absolute c>0 and one k_0, both uniform over every finite simple G with χ(G)=k.
- R(H) is the least N such that every red/blue colouring of E(K_N) contains a monochromatic non-induced copy of H.

### 文献与当前边界

已核验的主要结果：

- 字面第一问有完全初等的反例：ε=2、任意偶数 k、G=K_k。这是由定义直接推出，不依赖文献猜测。
- Faudree–McKay（1993，同行评审）证明 r(W_6)=17<18=r(K_4)，推翻 Erdős 原先的非渐近强猜想 r(G)≥r(K_k)。
- 当前 Problem 87 页面记录 R(k)≤4^k，因而在其显然意图的 3/4≤ε<1 范围，修复后的第一问自动成立；它还归属 Yuval Wigderson 一个对任意 χ(G)=k 的 r(G)≫2^{k/2} 的随机着色下界。该归属没有在本轮定位到专门的正式原始发表，故应在研究启动前重建或补充引用。
- Wigderson（2024）证明顶点删除可令普通 Ramsey 数相差超常数因子；其构造和结论不比较 r(G) 与 r(K_{χ(G)})，因此不能推出本题正反任一方向。

最近相关工作：检索至 2026-07-27 未发现直接解决修复后第一问或常数因子版本的论文/预印本。Axenovich–Gaa–Liu 的 arXiv:2409.07535 于 2026-06-23 更新，但研究的是不同的 chromatic Ramsey number R_χ(G)，仅作为术语辨析相关；不能当作本题进展。当前页面最后编辑于 2026-01-17 且无论坛评论，仍列 Open，但它自己声明该标签非完备文献保证。

剩余核心：在明确限定 0<ε<1 后，证明或反驳：对所有充分大 k 及每个 χ(G)=k 的有限简单图，r(G)>(1−ε)^k r(K_k)；或证明/反驳更强的统一 c>0 比例下界。任何研究还须先由问题维护者确认该修复确为授权目标。

已使用方法：

- 小图 Ramsey 数的精确计算/证书（Faudree–McKay 的 W_6 反例）。
- 随机二色边着色与 k-临界子图的边密度下界，可产生只依赖 χ(G) 的指数型 r(G) 下界；须完整核对其常数和量词。
- 与 r(K_k) 的已知粗上下界进行比较；这种路线目前无法控制相对于实际 r(K_k) 的固定比例。
- 相邻的 Ramsey-number robustness/vertex-deletion 方法可用作构造灵感，但没有已知归约到本题。

争议或不确定性：

- 当前数据库把问题标 Open，但有明确免责声明；负检索不是不存在解答的证明。
- 原始 Erdős 1995 论文的可访问 PDF 在本轮提取超时，因而未独立逐字核对第 14 页的 ε 范围。
- 网站原文的 ε>0 与其备注及标准渐近用法不一致；必须由维护者或领域专家确认是否修为 0<ε<1。
- 旧 UCSD 页面中的“n sufficiently large”表述与当前“k sufficiently large”不同，不能静默当作同一命题。

### 证据来源

- [Erdős Problem #87 — Discussion thread](https://www.erdosproblems.com/forum/thread/87) — Thomas F. Bloom / Erdős Problems, 2026-01-17; `forum`, `informal_claim`, directness=`direct`, reliability=`medium`. 当前页面逐字给出两问，仍标记 Open，显示 0 comments、无已声明解答，并明确警告 Open 标签仅反映网站维护者的当前认知。也给出 ε≥3/4 的备注和 Wigderson 下界归属。
- [Revision history of Erdős Problem 87](https://www.erdosproblems.com/history/87) — Erdős Problems, 2026-01-17; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 核对当前文本、该页显示的 2025-10-20 修订快照，以及未显式写出 0<ε<1 的事实。
- [A Conjecture of Erdős and the Ramsey Number r(W_6)](https://combinatorialpress.com/jcmcc-articles/volume-013/a-conjecture-of-erdes-the-ramsey-number-rw_6/) — Ralph J. Faudree; Brendan D. McKay, 1993-04-30; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原始期刊页摘要明确陈述历史猜想，并说明以 r(W_6)=17、r(K_4)=18 在 k=4 反驳它。
- [Some of my Favourite Problems in Number Theory, Combinatorics, and Geometry](https://revistas.usp.br/resenhasimeusp/pt_BR/article/view/74798) — Paul Erdős, 1995-05-10; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 确认当前问题页所引 [Er95,p.14] 的原始文献书目信息、卷期、页码和 DOI；本轮未能可靠提取该 PDF 第 14 页的公式，故不以其全文证明当前转录完全相同。
- [r(G) is bounded by r(χ(G)) (1)](https://mathweb.ucsd.edu/~erdosproblems/erdos/newproblems/RGLowerBoundByChromaticNumber1.html) — Erdős problems / UCSD archive, date unknown; `secondary_index`, `database_record`, directness=`indirect`, reliability=`medium`. 记录相关旧问题页使用图阶 n 的“sufficiently large”表述，并给出 R(G,H)、R(k) 和 χ(G) 的定义；该旧表述不能当作当前 k-渐近问题的同义版本。
- [Ramsey numbers upon vertex deletion](https://arxiv.org/abs/2208.11181) — Yuval Wigderson, 2022-08-23; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 核对 Wigderson 关于普通二色图 Ramsey 数的定义和一个不同但相邻的 2022/2024 研究方向；其无限族结果不解决本题。
- [Ramsey numbers upon vertex deletion](https://onlinelibrary.wiley.com/doi/10.1002/jgt.23093) — Yuval Wigderson, 2024-03-18; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 确认上述 Wigderson 论文的同行评审发表状态及其结果是顶点删除的 Ramsey 数比例问题，而非 Problem 87 的解答。
- [Chromatic Ramsey numbers and two-color Turán densities](https://arxiv.org/abs/2409.07535) — Maria Axenovich; Simon Gaa; Dingyuan Liu, 2026-06-23; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. v2 明确定义不同参数 R_χ(G)，并强调它与普通 R(G) 不同；用于排除术语混淆，未宣称解决 Problem 87。

### 完成标准

- 肯定出口: For the literal first question, the decisive negative audit outcome is already complete: ε=2, G=K_k, and arbitrarily large even k force the false inequality R(k)>R(k). For a repaired record, obtain an authoritative confirmation that the intended range is 0<ε<1, then an affirmative resolution must prove the repaired assertion with k_0(ε) uniform over every finite simple G with χ(G)=k; the stronger target additionally requires absolute c and k_0.
- 否定出口: For the repaired first target, give a fixed ε in (0,1), infinitely many k_i→∞, and finite simple G_i with χ(G_i)=k_i and R(G_i)≤(1−ε)^{k_i}R(k_i), certified by rigorous Ramsey bounds. For the stronger target, give such a family with R(G_i)/R(k_i)→0. If the owner declines the repair, retain the literal statement as disproved rather than pursuing a new conjecture.

不构成完成：

- Assuming without documentation that “ε>0” means “0<ε<1”.
- The W_6 counterexample: it concerns only k=4 and only the historical comparison R(G)≥R(k).
- A result for a selected graph class without a proved reduction from arbitrary k-chromatic graphs.
- An absolute lower bound such as R(G)≫2^{k/2} without the required comparison to the actual R(k).
- Finite computations or numerical evidence at bounded k.

正确性陷阱：

- Check the ε-domain before every argument; ε=2 is a decisive literal counterexample, while 0<ε<1 is a repaired convention.
- Do not confuse strict > with ≥ when taking G=K_k.
- Keep k even in the literal counterexample, since (−1)^k changes sign.
- Separate ordinary diagonal R(G) from the distinct chromatic Ramsey parameter R_χ(G).
- For any repaired proof, audit uniformity over all G after ε and k are chosen.
- Do not transplant results about vertex deletion, off-diagonal, induced, or multicolour Ramsey numbers without a proved reduction.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `12/100`
- 信心: `medium`
- 结论: 字面第一问已关闭，不应尝试“解决”它。12 分只评估经人工确认后的 0<ε<1 修复版本及独立常数因子目标；它们是清楚但处在对角 Ramsey 数核心比较缺口中的低概率研究目标。

支持理由：

- 修复后的命题量词清楚，正反两种证书可独立审查。
- 可分解为统一下界、结构归约和无限反例族三类明确子任务。
- 历史反例和随机着色下界给出可验证的边界条件。

主要障碍：

- 目前只知依赖色数的粗指数界，无法与实际 r(K_k) 作所需比例比较。
- 必须对图阶和结构均无界的全部 k-色图一致成立。
- r(K_k) 的精确指数增长仍有重大缺口；小 k 反例阻止朴素极值原则。

Proof-first 路线：

- 先获得对 ε 域的书面确认；未确认前不对修复目标做主张。
- 重建并严格审计 r(G)≫2^{k/2} 的随机着色论证，明确是否可强化为相对 r(K_k) 的比较。
- 研究极小 k-临界子图归约是否保留所需的 Ramsey 数不等式方向；若否，记录精确失败点。
- 反向搜索具有可认证 Ramsey 上界的无限高色数图族，但只有在给出有限停止条件的具体比较引理下才使用计算。

需要验证：

- 由 Erdős Problems 维护者或原始 Er95 第 14 页确认 ε 的预期范围。
- 补充 Wigderson 随机着色观察的正式出处，或写出完整自足证明。
- 以 MathSciNet、zbMATH、arXiv 和作者主页复查 2025–2026 是否已有直接解决修复目标的工作。

### 审计限制与人工复核理由

- 公开检索与当前问题页均不能逻辑证明不存在未索引、付费墙后或尚未发表的修复目标解答。
- 原始 Er95 PDF 可定位但本轮无法稳定抽取其第 14 页，故 ε 域的作者原文意图未被直接验证。
- 数据库页面最后编辑日早于审计日，且其 Open 标签有明确免责声明。
- 本审计对字面第一问的否定是确定的；对修复后版本和常数因子版本的开放性仅为证据支持下的中等置信判断。

- 必须由原始 Er95 第 14 页或 Erdős Problems 维护者确认 ε 的预期限定；这是是否可把记录作为开放问题研究的决定性前提。
- 应由具备 MathSciNet、zbMATH 等完整索引权限的审阅者做最终 2025–2026 文献查新。
- 若要引用 Wigderson 的随机着色下界，应补充可审计原始证明或正式发表来源。

<!-- DEEP_REVIEW:END -->
