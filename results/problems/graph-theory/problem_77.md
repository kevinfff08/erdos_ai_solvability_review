# Problem 77

## 基本信息

- 原始链接: https://www.erdosproblems.com/77
- LaTeX 页面: https://www.erdosproblems.com/latex/77
- 原始状态: `open`
- 奖金: `$250`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`
- 形式化状态: `no`
- OEIS: `A059442`
- 原站备注字段: 无

## 原问题

If $R(k)$ is the Ramsey number for $K_k$, the minimal $n$ such that every $2$-colouring of the edges of $K_n$ contains a monochromatic copy of $K_k$, then find the value of\[\lim_{k\to \infty}R(k)^{1/k}.\]

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `43/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 题面含渐近/无限对象线索：liminf, limsup
- 原记录含奖金 $250，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: chromatic, colouring, ramsey
- 渐近/无限线索: liminf, limsup
- 构造/存在性线索: find

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5 级别模型 + 计算/形式化/检索/反例搜索工具`
- 结论: **完整解决的可能性很低；可用于整理和验证既有上下界证明、形式化局部论证、搜索小规模结构与候选策略，但不太可能直接给出极限存在性或精确值。**
- 等级: `low_candidate`
- 分数: `18/100`
- 信心: `high`
- 可能路线: 较现实的路线不是直接求出极限，而是把任务拆成可验证子目标：形式化 Ramsey 数基本递推、随机下界与已知上界框架；复现并检查现有 $4-c$ 型上界思路中的关键不等式；用计算搜索小 $k$ 或特定构造族以测试候选启发；尝试发现可推广的次乘性、近次乘性或容器/熵方法引理。若有贡献，更可能是证明验证、局部改进、简化证明或提出可检验的新中间命题。

### 支持理由

- 问题目标是确定或证明 $R(k)^{1/k}$ 的极限行为，属于对角 Ramsey 数的核心渐近问题；给出的备注显示即使极限存在性本身也是 Erdős 单独悬赏的目标。
- 已知结果只给出很宽的夹逼区间：下极限至少 $\sqrt{2}$，上极限至多约 $3.7992\cdots$；这表明当前理论距离确定极限值仍很远。
- 模型配合工具能系统化已有证明、检查大量代数和概率估计、生成形式化草案、搜索小规模反例或构造，但这些能力主要覆盖验证和探索，不等同于突破核心渐近障碍。
- 问题没有现成形式化版本，形式化证明工具可帮助降低错误率，但首先需要把高度复杂的组合证明转写成机器可检查的中间库，工作量很大。

### 主要障碍

- 核心障碍是缺少能控制 $R(k)$ 指数增长率的结构性原理；现有上下界来自非常不同的方法，二者之间差距巨大。
- 证明极限存在通常需要某种强近次乘性或可拼接机制，但 Ramsey 数的自然递推并不直接给出所需的指数级收敛结论。
- 计算搜索只能覆盖很小的 $k$，对 $k\to\infty$ 的极限问题证据有限，且容易误导。
- 近期上界改进依赖精细组合、概率和图结构论证，模型生成的新证明很容易出现隐藏量词、误用独立性或常数损失问题。
- 若目标是精确值，例如猜测为 2，则还需要根本性改进下界或上界技术，远超常规自动化推理能力。

### 需要的验证

- 对任何新引理做逐步形式化或至少进行人工可审计证明检查，尤其检查渐近量词、常数依赖和概率事件相关性。
- 将候选上界或下界路线与已知区间 $\sqrt{2}$ 到约 $3.7992$ 对齐，确认是否真的改善指数底数而非只改善低阶项。
- 对计算搜索结果明确记录图规模、颜色编码、SAT/ILP 证书或反例证书，并区分有限规模现象与渐近结论。
- 若声称极限存在，需要验证是否已经证明 $\limsup$ 与 $\liminf$ 相等，或给出足够强的近次乘/超次乘结构。
- 需要由 Ramsey 理论专家审查模型提出的关键创新点，因为该问题的错误证明风险极高。

### 公开版思考摘要

这个问题适合 AI 做辅助研究和证明审计，但不是很适合期待端到端解决。判断依据是：目标触及对角 Ramsey 数的指数增长常数；给定材料显示连极限存在性都被单独悬赏；已知上下界仍相距很大。GPT-5.5 级别系统可以在文献整理、证明形式化、常数检查、有限搜索和生成中间猜想方面有价值，但完整确定极限需要新的深层组合思想，当前可预期成功率很低。

### 免责声明

以上是对 AI 辅助攻关可行性的评估，不是该 Erdős 问题的解答，也不声称给出了新的 Ramsey 数上下界或极限存在性证明。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_77.md](../../prompts/problem_77.md)

### 状态结论

截至 2026-07-27，标准对角 Ramsey 数序列 R(k)^{1/k} 是否收敛仍是开放问题。Erdős Problems 页面在 2026-02 仍标为 open，且 2025 年直接讨论该极限的论文仍将其作为条件性假设；核验的 2023–2026 工作仅改进指数上界或给出相关条件性联系，未证明极限存在或不存在。

### 当前规范陈述

对每个整数 k >= 1，令 R(k)=R(k,k) 为最小整数 n，使得完全图 K_n 的每个红蓝边染色都含有红色 K_k 或蓝色 K_k。判定完整序列 R(k)^(1/k)（k 趋于无穷）是否收敛；若收敛，确定其极限值。

```text
For every integer k >= 1, let R(k)=R(k,k) be the least integer n such that every colouring c:E(K_n)->{red,blue} contains a red copy of K_k or a blue copy of K_k. Determine whether the full sequence (R(k)^(1/k))_{k>=1} converges as k->infinity. If it converges, determine its limit.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现针对该精确定义的简单反例。有限 Ramsey 数值、有限计算或单个子序列的行为均不能否定或证明完整序列的收敛性。
- 版本变化: 未发现原问题被修订、拆分或替换。近年工作只改进了 R(k) 的指数上界。输入称“未形式化”不意味着没有相关形式化：Archive of Formal Proofs 已形式化 CGMS 的 4-epsilon 型上界，但并未形式化或解决本题所问的极限存在性。

陈述问题：

- 输入中的“2-colouring”按标准 Ramsey 数约定应指每条边恰被赋予红、蓝两色之一；规范表述已明确该函数和单色团的含义。
- “find the value”隐含先证明极限存在；若证明 liminf 与 limsup 不同，则是对字面命题的决定性否定结论。
- 有限个初始 k 的约定不影响极限。

需要固定的量词/约定：

- The universal quantifier is over every red-blue colouring of E(K_n), and R(k) is the least such n.
- The target is convergence of the full integer-indexed sequence, not convergence along a subsequence.
- An affirmative solution must establish equality of liminf and limsup; a proposed numerical value or improved bounds alone are insufficient.

### 文献与当前边界

已核验的主要结果：

- 经典结果给出 sqrt(2) <= liminf R(k)^(1/k) <= limsup R(k)^(1/k) <= 4；这些界本身不蕴含极限存在。
- Campos–Griffiths–Morris–Sahasrabudhe（2023 预印本，2025 修订）证明存在 epsilon>0，使 R(k) <= (4-epsilon)^k。
- Gupta–Ndiaye–Norin–Wei（2024 预印本）将该框架优化为 R(k,k) <= (3.8)^(k+o(k))；后续文献将其对应的根式上界写为 4 exp(-0.14/e) 约为 3.7992。
- Balister 等的 JAMS 2026 论文对任意固定 r 给出 R_r(k) 的指数改进；二色情形提供 CGMS 上界的另一证明，不是极限存在性结果。
- Paulson 的 AFP/ITP 形式化核验了 CGMS 型 4-epsilon 上界，证明该大技术结果可机器检验；它不涉及 liminf=limsup。

最近相关工作：直接涉及该极限的最新可核验工作是 Araujo–Filipe–Miyazaki，arXiv:2512.16062（2025-12）：其定理把 log R(k,k)/k 的极限存在性作为假设来推导另一问题的结论，因而不是解决方案。最新已发表的相邻上界结果为 Balister 等，JAMS 2026；其 arXiv v2 于 2026-01 修订。定向检索未找到 2025–2026 年证明该极限存在或不存在的可核验论文、形式化工件或论坛证明。

剩余核心：证明 liminf_{k→∞} R(k)^(1/k)=limsup_{k→∞} R(k)^(1/k)，或证明二者严格不等。等价地，须控制完整序列的指数率，而非仅在无穷子序列上或仅给出单侧界。

已使用方法：

- 随机染色、Lovász 局部引理及其改进所给出的概率下界。
- 经典 Ramsey 递推及近年来的密度/准随机性方法所给出的上界。
- CGMS 的 book algorithm，及 GNNW 的简单归纳式、参数优化和 off-diagonal/multicolour 延伸。
- Balister 等的多色 book 方法和几何负相关引理。
- Isabelle/HOL 形式化与已验证实代数，可用于审计具体上界引理，但尚未产生极限存在性机制。

争议或不确定性：

- Erdős Problems 明确说明其 open 标签反映维护者所知文献，不能单独作为完备性证明；本审查以近年预印本、同行评审记录和定向检索交叉核验。
- CGMS 的 arXiv 记录仍显示预印本；2025 的 Araujo–Filipe–Miyazaki 参考文献称其为 Annals of Mathematics 'to appear'。本审查不把未独立核验的最终卷期当作已发表书目信息。
- 检索中出现了非同行评审、未给出可核验极限证明的“框架”式材料；其片段仍假设相关极限存在，故未被视为解决声明。

### 证据来源

- [Erdős Problems — Problem 77](https://www.erdosproblems.com/77) — Thomas F. Bloom / Erdős Problems, 2026-02-08; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 页面将问题标为 open，说明评论中没有已提出的部分或完整解答，并列出当前相关上界进展及历史背景。
- [Erdős Problems — Problem 77 LaTeX source](https://www.erdosproblems.com/latex/77) — Thomas F. Bloom / Erdős Problems, 2026-02-08; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 用于核对输入题面、参考文献和备注的原始 LaTeX 记录；该记录不是极限存在性的证明。
- [An exponential improvement for diagonal Ramsey](https://arxiv.org/abs/2303.09521) — Marcelo Campos, Simon Griffiths, Robert Morris, Julian Sahasrabudhe, 2023-03-16; revised 2025-08-04; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 摘要证明存在 epsilon>0，使 R(k) <= (4-epsilon)^k；这是指数上界改进，不证明 R(k)^(1/k) 收敛。
- [Optimizing the CGMS upper bound on Ramsey numbers](https://arxiv.org/abs/2407.19026) — Parth Gupta, Ndiame Ndiaye, Sergey Norin, Louis Wei, 2024-07-26; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 摘要给出 R(k,k) <= (3.8)^(k+o(k)) 的优化上界及相关 off-diagonal/multicolour 结果；没有声称极限存在或不存在。
- [Upper bounds for multicolour Ramsey numbers](https://arxiv.org/abs/2410.17197) — Paul Balister, Béla Bollobás, Marcelo Campos, Simon Griffiths, Eoin Hurley, Robert Morris, Julian Sahasrabudhe, Marius Tiba, 2024-10-22; revised 2026-01-21; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 对每个固定颜色数 r 给出 R_r(k) 的指数改进；r=2 时给出 CGMS 结果的另一较短证明。该工作不比较本题序列的 liminf 与 limsup。
- [Upper bounds for multicolour Ramsey numbers](https://ora.ox.ac.uk/objects/uuid%3A18dfcd97-a793-407e-a375-0de18d094646) — Paul Balister, Béla Bollobás, Marcelo Campos, Simon Griffiths, Eoin Hurley, Robert Morris, Julian Sahasrabudhe, Marius Tiba, 2026-01-16; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. Oxford Research Archive 记录该文发表于 Journal of the American Mathematical Society 39(3), 765–780，DOI 10.1090/jams/1069；它确认近期多色上界进展的同行评审版本，而非本题的解答。
- [On the maximum ratio between chromatic number and clique number](https://arxiv.org/abs/2512.16062) — Igor Araujo, Rafael Filipe, Rafael Miyazaki, 2025-12-18; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 将 log R(k,k)/k 的极限明确作为条件性假设，并给出与另一 Erdős 问题的条件性联系；同时记录由 CGMS/GNNW 导出的当前指数上界。这是近期直接证据，表明该极限仍未被证明。
- [An Exponential Improvement for Diagonal Ramsey](https://isa-afp.org/entries/Diagonal_Ramsey.html) — Lawrence C. Paulson, 2024-09-02; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. Isabelle/HOL 形式化了 CGMS 的 R(k) <= (4-epsilon)^k 型结果；该正式工件不包含本题极限存在性结论。
- [Formalising New Mathematics in Isabelle: Diagonal Ramsey](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITP.2025.18) — Lawrence C. Paulson, 2025-09-22; `formalization`, `peer_reviewed`, directness=`direct`, reliability=`high`. 同行评审 ITP 论文说明上述形式化针对 CGMS 的主要新上界结果，并链接 AFP 工件；这澄清“相关上界已形式化”与“问题77已形式化/已解”之间的区别。

### 完成标准

- 肯定出口: Prove that there is a real L such that for every epsilon>0 there exists K with |R(k)^(1/k)-L|<epsilon for every integer k>=K; equivalently prove liminf_{k->infinity} R(k)^(1/k)=limsup_{k->infinity} R(k)^(1/k). Determine L to meet the full wording of the problem.
- 否定出口: Prove liminf_{k->infinity} R(k)^(1/k)<limsup_{k->infinity} R(k)^(1/k), for example by rigorously producing two infinite subsequences with separated exponential rates.

不构成完成：

- A better universal upper bound or lower bound without equality of liminf and limsup.
- A result only for off-diagonal, multicolour, ordered, induced, or otherwise modified Ramsey numbers without a proved transfer.
- Convergence on a subsequence, finite exact computations, or numerical extrapolation.
- A conditional conclusion based on the Ramsey Diagonal Conjecture or another unproved comparison principle.
- A formalization of a one-sided upper bound.

正确性陷阱：

- Quantifiers must hold for every sufficiently large integer k, not merely infinitely many k.
- Track all o(k) terms after taking kth roots and under any iteration.
- Do not infer convergence from monotonicity of R(k), or from a common interval containing liminf and limsup.
- Verify every product, substitution, or gluing construction in both colours and with exact clique-size indices.
- Do not import a theorem for R(s,t) or R_r(k) as a same-parameter inequality for R(k,k) without a proved reduction.
- A Fekete-style conclusion requires an actually proved approximate subadditive/submultiplicative relation with an iterably negligible error.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `8/100`
- 信心: `high`
- 结论: 题目定义和完成条件非常清楚，但它是长期未解的核心 Ramsey 渐近问题；现阶段 AI 独立完成完整证明的前景很低。

支持理由：

- 可将目标精确化为 liminf 与 limsup 的相等或分离，结论可严格审计。
- 近期有细致、公开、部分已形式化的上界技术，局部不等式和参数误差可以逐项验证。
- 存在明确的反向目标：若能构造严格分离的无穷子序列，也构成完整否定解。

主要障碍：

- 数十年的进展主要是收紧单侧指数上界，尚无连接不同 k 的足够强结构。
- 已知 Ramsey 递推、CGMS/GNNW 及多色方法均不自动给出同一序列的近似次乘性。
- 有限计算无法控制极限，极易产生无法外推的经验模式。

Proof-first 路线：

- 严格寻找并审计能够在同一对角参数上迭代的近似次加性或次乘性不等式；先证明误差为 exp(o(k)) 且可迭代，再尝试极限定理。
- 研究已知上、下界框架是否能导出共同的变分/熵率对象，并将“极限存在”还原为一个具体的紧性或稳定性引理。
- 独立探索不收敛的严格路线，但只有能够产生全无限子序列的分离证书才继续。
- 可选择一个已发表或 AFP 形式化的 CGMS 子引理作机器化复核；不得以程序实验替代渐近证明。

需要验证：

- 逐页阅读 GNNW，核对 3.7992 常数、所有 o(k) 的量词及其与对角情形的转换。
- 在正式启动研究前复查 2026-07 之后的 arXiv、期刊和作者主页；本审查结论只截至给定日期。
- 对任何声称的乘积/替换 Ramsey 不等式，独立检查颜色数、取整、clique 尺寸、方向和迭代次数。

### 审计限制与人工复核理由

- AnySearch 技能因 API 连接失败而不可用；审查改用可访问的公开网页检索和原始 arXiv/档案页面。
- 未对付费数据库、所有语言的期刊、私人手稿或未来索引更新作穷尽检索；“未发现解决”是高置信的当前记录判断，而非逻辑排除。
- Erdős Problems 的页面正文可由检索结果读取，但直接打开受到 403 限制；页面的状态、最后编辑日期和无论坛解答记录据搜索索引核对。
- 未逐页重建经典下界及其最早出处；这些只用作已知背景界，不影响对当前开放状态的判断。

- 研究开始前应由人工或后续代理再查 2026-07-27 后的 arXiv、MathSciNet、zbMATH 和作者主页。
- 若正式引用 3.7992 的全部有效范围或 CGMS 的最终出版状态，应直接核对 GNNW/CGMS 全文及出版社记录。
- 应人工确认 Erdős Problems 的三条论坛评论内容；搜索索引显示没有解答声明，但网页直接访问受限。

<!-- DEEP_REVIEW:END -->
