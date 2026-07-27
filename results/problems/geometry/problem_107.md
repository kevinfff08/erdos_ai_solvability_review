# Problem 107

## 基本信息

- 原始链接: https://www.erdosproblems.com/107
- LaTeX 页面: https://www.erdosproblems.com/latex/107
- 原始状态: `falsifiable`
- 奖金: `$500`
- 主类别: `geometry`
- 原始标签: `geometry`, `convex`
- 形式化状态: `yes`
- OEIS: `A000051`
- 原站备注字段: 'Happy Ending' problem

## 原问题

Let $f(n)$ be minimal such that any $f(n)$ points in $\mathbb{R}^2$, no three on a line, contain $n$ points which form the vertices of a convex $n$-gon. Prove that $f(n)=2^{n-2}+1$.

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `57/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：convex, geometry
- 题面含渐近/无限对象线索：o(
- 原记录含奖金 $500，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: convex, geometry
- 有限/计算线索: graph, ramsey
- 渐近/无限线索: o(
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低候选。GPT-5.5 级别模型配合计算、形式化证明和文献检索，较可能在小规模情形、已有证明重构、形式化核查、反例搜索框架方面产生可靠进展；但要直接证明一般式 f(n)=2^{n-2}+1，成功概率很低。**
- 等级: `low_candidate`
- 分数: `25/100`
- 信心: `high`
- 可能路线: 最现实路线不是直接攻克完整猜想，而是把任务拆成可验证模块：形式化下界构造；复现 Erdős-Szekeres 上界与后续改进的关键组合几何引理；对小 n 做 SAT/SMT/几何顺序型搜索；尝试把凸位置、杯帽分解、抽象 order type 等结构转成可机器验证的证明对象。若要真正完成问题，需要发现一个能把当前 2^{n+O(√(n log n))} 型上界压到精确 2^{n-2}+1 的新结构性论证。

### 支持理由

- 问题陈述短、对象明确，且已 formalized=yes，适合形式化验证、有限实例搜索和证明片段审计。
- 下界 2^{n-2}+1≤f(n) 属于经典构造型内容，模型配合证明助手较可能重构并验证。
- 问题是 falsifiable：若猜想错误，可通过有限点集或抽象顺序型给出反例；模型可辅助设计反例搜索、剪枝和证书验证。
- 备注给出当前最好上界仍为 2^{n+O(√(n log n))}，说明已有技术距精确值仍有显著差距；这降低了直接完成完整证明的可能性。
- 几何 Ramsey 型问题有较强的可计算表示，例如 order types、凸包层、杯帽结构，适合 AI+搜索做局部探索。

### 主要障碍

- 核心难点是一般 n 的精确上界，需要证明任意 2^{n-2}+1 个一般位置平面点必含凸 n 边形；这远强于目前备注中给出的最好上界。
- 有限搜索不能直接替代一般证明，除非能抽取出可推广的结构引理。
- 顺序型数量随点数急剧增长，反例搜索或小 n 验证会遭遇严重组合爆炸。
- 几何直觉与组合编码之间存在落差，模型生成的证明很容易漏掉退化情形、归纳条件或“任意点集”量词。
- 已有形式化虽降低验证门槛，但把前沿组合几何证明完整形式化仍可能非常昂贵。

### 需要的验证

- 核查 formalized=yes 对应的形式化库覆盖范围：只是问题陈述、经典界，还是包含可复用的几何 Ramsey 引理。
- 对模型提出的任何新上界证明，必须用证明助手或逐引理审查验证所有归纳步骤和几何配置分类。
- 若提出反例，需给出精确坐标或 order-type 证书，并由独立程序验证无三点共线且不存在凸 n 边形。
- 对计算搜索结果，需要记录枚举空间、同构消除、剪枝规则和可复现代码，以避免漏搜。
- 若模型声称改进当前上界，应与 problem JSON 中给出的 Suk 与 Holmsen-Mojarrad-Pach-Tardos 型界逐项比较其依赖的关键引理。

### 公开版思考摘要

这个问题结构清楚、可形式化、可计算化，因此很适合 GPT-5.5 做辅助验证、有限实例搜索、证明片段重构和反例证书检查。但完整目标是著名 Happy Ending 猜想的精确公式；根据给定 JSON，已知最好上界仍比目标多出 2^{O(√(n log n))} 因子。AI 工具链可能帮助发现局部模式或验证候选证明，但单次完成一般证明的可信度较低。

### 免责声明

以上是对 GPT-5.5 级别模型可解性与推进潜力的审查，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `not_required`
- 独立研究 Prompt: [prompts/problem_107.md](../../prompts/problem_107.md)

### 状态结论

截至 2026-07-27，命题的规范版本仍为开放问题。Baek–Balko 的同行评议 SoCG 2025 论文及其 2026 年 JCTA 版本均明确称该猜想仍开放，并指出首个未解决的具体情形是 ES(7)=33。检索到的 2025 年预印本只给出若干锚定子族的 SAT 不可满足证书，没有宣称解决 ES(7)，更没有解决全称命题；未发现可核验的证明或反例。

### 当前规范陈述

对每个整数 n >= 3，令 ES(n) 为满足下述性质的最小正整数 N：平面 R^2 中任意 N 个点组成的有限集合 P，只要其中任意三点不共线，就含有一个 n 点子集 Q 处于凸位置；等价地，Q 的每一点都是 conv(Q) 的顶点，因此 Q 是某个凸 n 边形的顶点集。证明对所有 n >= 3，ES(n)=2^(n-2)+1。

```text
For every integer n >= 3, let ES(n) be the least positive integer N such that every finite set P of N points in R^2 with no three collinear contains an n-element subset Q in convex position; equivalently, every point of Q is a vertex of conv(Q), so Q is the vertex set of a convex n-gon. Prove ES(n) = 2^(n-2) + 1 for every n >= 3.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 对规范化后的 n >= 3 命题未发现简单反例。已知 Erdős–Szekeres 构造仅给出 2^(n-2) 个点且无凸 n 边形，正是下界 ES(n)>=2^(n-2)+1，不能反驳目标。字面式若错误地允许 n=2 则术语未定义，而非一个标准的反例。
- 版本变化: 1935 年 Erdős–Szekeres 证明存在性及经典上界；1960/61 年给出 2^(n-2)+1 下界并提出该值应精确。Szekeres–Peters（2006）证明 ES(6)=17。Suk（2017）与 Holmsen–Mojarrad–Pach–Tardos（2020）将一般上界降至 2^(n+O(sqrt(n log n)))，但未给出精确值。Baek–Balko（2025；JCTA 2026）证明“split k-gon”松弛版本的精确阈值，并对 decomposable 点集证明原猜想；这些是严格较弱/受限目标，不是原命题的修订或解答。

陈述问题：

- 输入陈述未写明 n 的取值范围；按通常“凸 n 边形”约定，应取整数 n >= 3。若允许 n=2，则“凸 2-边形”并无统一的通常定义。
- “n 点形成凸 n 边形”必须理解为该 n 点子集全部为其自身凸包顶点；这不要求该多边形为空，原点集其余点可以位于多边形内部。
- “minimal”量词应展开为：对每个 n，取满足全称强制性质的最小正整数 N；目标是对所有 n 的等式，而不是只对固定但未量化的 n。

需要固定的量词/约定：

- Quantify universally over every integer n >= 3.
- For each n, ES(n) is the minimum N such that every finite general-position P subset R^2 with |P| = N has an n-point subset in convex position.
- A counterexample to the equality at n is a general-position set of exactly 2^(n-2)+1 points containing no n points in convex position; the known lower-bound construction with 2^(n-2) points is not such a counterexample.
- No emptiness condition is present: this is not the empty-convex-polygon or k-hole problem.

### 文献与当前边界

已核验的主要结果：

- Erdős–Szekeres 的 cap-cup 定理给出 ES(n)<=binom(2n-4,n-2)+1；1960/61 的构造给出 ES(n)>=2^(n-2)+1。
- 已知精确小值包括 ES(3)=3、ES(4)=5、ES(5)=9、ES(6)=17。Szekeres–Peters 的同行评议计算论文直接证明了 ES(6)=17 的上界；Baek–Balko 明确指出首个开放具体情形为 ES(7)=33。
- Suk（JAMS 2017）证明 ES(n)=2^(n+o(n))，更具体地给出 2^(n+O(n^(2/3)log n)) 上界。
- Holmsen、Mojarrad、Pach、Tardos（JEMS 2020）将误差项改进为 ES(n)<=2^(n+O(sqrt(n log n)))；这仍远不足以推出精确常数/加法项。
- Baek–Balko（SoCG 2025，JCTA 2026）证明 ES_split(n)=2^(n-2)+1，并证明原猜想在 decomposable 点集上成立；二者均不蕴含任意一般位置点集上的原命题。

最近相关工作：Baek–Balko 的 2026 JCTA 文章是本次检索到的最新同行评议直接工作：它仍明确称原猜想开放，给出 split polygon 的精确松弛结论、抽象弱/强多边形的 SAT 反例现象，以及 decomposable 点集上的正面结果。Dumitru（2025-12，预印本）针对 ES(7)=33 只给出部分锚定子族的 SAT 证书，未改变状态。

剩余核心：证明或反驳：对每个 n>=7，任意 2^(n-2)+1 个一般位置平面点都包含 n 个凸位置点。一个反驳只需给出某个 n>=7 的 2^(n-2)+1 点一般位置构造且没有凸 n 点子集；一个证明必须覆盖全部 n>=3（实际未决部分为 n>=7）。

已使用方法：

- 以 x 坐标排序后的 cups/caps 与组合递推。
- Ramsey 型/伪线配置、正比例 Erdős–Szekeres 引理和凸聚类；Suk 与 HMPT 的渐近上界论证。
- 定向拟阵或三元 orientation 变量的 SAT 编码、对称破除、凸层约束和 UNSAT 证书。
- Baek–Balko 的 split polygon、整数分拆/有序 3-一致超图关联及 decomposable 点集结构。

争议或不确定性：

- Baek–Balko 的抽象弱/强多边形反例只表明某些推广失败，不能作为平面点集原猜想的反例。
- Dumitru 预印本的证书只覆盖锚定子族，且没有给出全局 ES(7) 结论；必须避免将其视为解答。
- 本次未能通过接口读取 #107 具体论坛帖内容；但没有找到任何可检验的论坛解答主张。
- “formalized=yes”数据库标记不等于一般猜想已有机器核验的证明；已核验文献只支持至 n=6 的有限形式化相关结果。

### 证据来源

- [Erdős Problems #107](https://www.erdosproblems.com/107) — Erdős Problems database, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 记录给出当前问题陈述、历史下界、Suk 与 HMPT 上界及形式化标记；其状态标签本身未被当作开放性的决定性证据。
- [The Erdős-Szekeres Conjecture Revisited](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2025.13) — Jineon Baek; Martin Balko, 2025-06-20; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 直接称原猜想仍开放，说明其对所有 k>=7 仍未解决；回顾 ES(6)=17、下界、Suk 及 HMPT 上界，并证明 split k-gon 的精确阈值以及对 decomposable 点集的受限结论。
- [The Erdős-Szekeres conjecture revisited](https://www.sciencedirect.com/science/article/pii/S0097316526000385) — Jineon Baek; Martin Balko, 2026; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 2026 年期刊版本仍将原猜想称为开放；它还明确区分弱/强多边形抽象化中的反例与平面点集原猜想，并证明 decomposable 点集上的受限结论。
- [On the Erdos-Szekeres convex polygon problem](https://arxiv.org/abs/1604.08657) — Andrew Suk, 2016-04-29; `primary_paper`, `preprint`, directness=`direct`, reliability=`high`. 给出 ES(n)<=2^(n+O(n^(2/3) log n))，从而证明 ES(n)=2^(n+o(n))，但不证明精确猜想。期刊版本为 JAMS 30 (2017), 1047-1053。
- [Two extensions of the Erdős-Szekeres problem](https://arxiv.org/abs/1710.11415) — Andreas F. Holmsen; Hossein Nassajian Mojarrad; János Pach; Gábor Tardos, 2017-10-31; `primary_paper`, `preprint`, directness=`indirect`, reliability=`high`. 其改进经 Baek–Balko 的同行评议综述明确为 ES(n)<=2^(n+O(sqrt(n log n)))；该工作还延伸到伪线配置与凸体问题。期刊版本为 JEMS 22 (2020), 3981-3995。
- [Computer solution to the 17-point Erdős-Szekeres problem](https://www.cambridge.org/core/journals/anziam-journal/article/computer-solution-to-the-17point-erdosszekeres-problem/0EC7876789232266D60439A4C00D86D9) — George Szekeres; Lindsay Peters, 2006; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明每个 17 点一般位置平面配置含凸 6 点子集，故与下界一起给出 ES(6)=17；论文描述三套独立可复现的计算实现。
- [Fast Formal Proof of the Erdős-Szekeres Conjecture for Convex Polygons with at Most 6 Points](https://doi.org/10.1007/s10817-017-9423-7) — Filip Marić, 2019; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 为至多 6 点的已知有限情形提供形式验证相关工作；这不能被误读为一般 Erdős–Szekeres 猜想已经形式化证明。
- [Notes on the 33-point Erdős--Szekeres problem](https://arxiv.org/abs/2512.24061) — Bogdan Dumitru, 2025-12-30; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 将 ES(7)=33 称为首个开放具体情形，并只报告若干锚定子族的 SAT UNSAT 证书及运行时困难；不是完整 ES(7) 证明。
- [107 Discussion Thread](https://www.erdosproblems.com/forum/thread/107) — Erdős Problems forum participants, date unknown; `forum`, `informal_claim`, directness=`indirect`, reliability=`low`. 论坛索引显示该问题有讨论帖；审计时该具体页面无法由检索接口读取，因此其中的内容没有用于支持状态结论。

### 完成标准

- 肯定出口: Provide a complete proof that for every integer n >= 3, every general-position set P subset R^2 with |P| = 2^(n-2)+1 has an n-element subset in convex position. Together with the established lower-bound construction, this proves ES(n)=2^(n-2)+1 for all n >= 3.
- 否定出口: Provide one explicit integer n >= 7 and a finite general-position P subset R^2 with |P| = 2^(n-2)+1 such that every n-element subset of P has a point in the convex hull of the other n-1 points. This proves ES(n)>2^(n-2)+1 and disproves the universal conjecture.

不构成完成：

- Proving ES(n)=2^(n+o(n)), improving the O(sqrt(n log n)) term, or obtaining any asymptotic bound without the exact threshold.
- Proving the threshold for split polygons, caps/cups, decomposable sets, pseudoline configurations, or an abstract hypergraph model without a valid implication to arbitrary realizable planar point sets.
- Checking finitely many values, including ES(7), unless the claimed result is explicitly only that finite case; even ES(7)=33 would not prove the all-n conjecture.
- A SAT outcome without a fully specified encoding, symmetry argument, trusted/certified UNSAT evidence, and proof that the encoding covers all relevant realizable order types.

正确性陷阱：

- Do not confuse convex position with an empty convex polygon: other points of P may lie inside conv(Q).
- Keep the lower-bound and disproof directions straight: a 2^(n-2)-point avoiding set proves only ES(n)>=2^(n-2)+1; a disproof needs an avoiding set with 2^(n-2)+1 points.
- A cap or cup is sufficient for convex position but not equivalent to an arbitrary convex n-gon; arguments that replace one by the other need proof.
- If using orientation signs, enforce all realizability/allowable-sequence conditions required by the claimed geometric conclusion; an abstract oriented structure need not be a planar point set.
- State n>=3, finiteness, general position, and whether perturbations preserve every order-type property used.
- Do not infer the exact formula from 2^(n+O(sqrt(n log n))) or from the split/decomposable restricted theorems.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `4/100`
- 信心: `high`
- 结论: 这是定义清楚、可严格核验的开放问题，但其全称精确断言已抵抗近百年方法；对当前 AI 而言属于低概率研究候选，不应把渐近接近或有限 SAT 搜索误认为接近完整解决。

支持理由：

- 目标、反例门槛和已知下界均精确，任何局部引理、构造或可核验证书都有明确价值。
- 近期工作给出了可区分的结构性边界（split、decomposable、抽象弱/强多边形），可支持独立路线的严格筛选。
- ES(7)=33 提供了一个有限、可证书化的子目标，但它不替代全称命题。

主要障碍：

- 核心命题要求对任意 n 的精确阈值；目前最强一般上界仍有 2^(O(sqrt(n log n))) 的指数误差。
- 已有抽象化反例并不自动可实现为平面点集，且从有限定向数据到几何可实现性是高风险环节。
- 纯计算的状态空间、SAT 性能波动和证书覆盖范围均可能造成“部分搜索即解决”的错觉。

Proof-first 路线：

- 先寻找极小反例或紧配置必须满足的可证明结构性质，并测试该性质能否将其归入已解决的 decomposable 类；只有完整蕴含链才有价值。
- 独立研究对 cup-cap 紧构造的扰动、组合骨架及可实现性约束，目标是给出可泛化的强迫引理或一个真正的 n=7 反例候选。
- 可选的唯一计算路线只能针对预先声明的有限引理，例如经严格对称约简后的 ES(7) 某类 order type；必须有 CNF、覆盖论证、可检查证书与停止条件。

需要验证：

- 对任何新证明逐项核对一般位置、凸位置定义、全部 n 的量词和与已知下界的拼接。
- 对任何 SAT/枚举结论核对编码等价性、几何可实现性、对称破除完备性、求解器版本及独立证书检查。
- 若主张更新当前状态，须检索并审阅 2026-07-27 之后的正式论文、预印本修订、作者页及问题页更新。

### 审计限制与人工复核理由

- 开放状态的“确认”基于截至审计日可访问的当前同行评议 2025/2026 文献、问题页和定向检索；它不是对未来或未被索引材料不存在的逻辑证明。
- #107 论坛具体页面在审计接口中返回内部错误，故未依赖其内容；论坛索引显示其存在但不构成数学证据。
- HMPT 的可访问预印本摘要主要强调其扩展；其对原函数误差项的准确表述由 Baek–Balko 的同行评议回顾交叉核验。
- 数据库的“formalized=yes”未附带可审计的一般命题证明链接；本审计仅能确认已知至 n=6 的形式化相关文献，不能据此判断一般猜想已形式化。

- 无

<!-- DEEP_REVIEW:END -->
