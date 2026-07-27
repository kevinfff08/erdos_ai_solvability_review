# Problem 66

## 基本信息

- 原始链接: https://www.erdosproblems.com/66
- LaTeX 页面: https://www.erdosproblems.com/latex/66
- 原始状态: `open`
- 奖金: `$500`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive basis`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Is there $A\subseteq \mathbb{N}$ such that\[\lim_{n\to \infty}\frac{1_A\ast 1_A(n)}{\log n}\]exists and is $\neq 0$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `24/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：density, for all large, liminf, limsup
- 原记录含奖金 $500，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: additive basis
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: density, for all large, liminf, limsup
- 构造/存在性线索: construct, is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5-level model with computational/formal/literature tools`
- 结论: **不太可能直接完全解决，但有现实机会做出可审计的显著推进，尤其是在有限模型、随机构造去异常集、以及已知不可能结果的形式化强化方向上。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 较可能的推进路线是把问题转化为表示函数 r_A(n)=1_A*1_A(n) 的全局误差控制问题：先复现并形式化给定摘要中的 Erdős-Sárközy 与 Horváth 型障碍，再对随机稀疏集合的“密度零异常集”构造做精细化，尝试用分块、依赖随机化、Lovasz local lemma/熵压缩、或有限区间约束搜索来消除异常点；并用计算搜索生成有限前缀反例或候选模式，反向抽取可证明的结构性障碍。若走否定方向，则重点尝试证明 r_A(n)/log n 的 liminf 与 limsup 必有固定间隔。

### 支持理由

- 问题表述非常短且可形式化，目标对象明确，适合计算实验、有限前缀约束搜索和证明助手验证局部引理。
- 给定备注显示随机集合已经能在忽略密度零异常集时达到类似性质，说明存在接近目标的概率模型，AI 可系统探索去异常集的改造。
- 已有障碍结果聚焦在 sqrt(log n) 量级误差，给出了清晰的可复现技术边界；模型可尝试强化这些边界或发现它们不能排除较大波动下的极限。
- 该问题有明确的正反两条路线：构造 A 使所有 n 上收敛到非零常数，或证明任何 A 的归一化表示函数都有不可消除振荡。

### 主要障碍

- 核心难点正是“无异常集”的全体 n 控制；随机方法通常给出高概率或几乎处处结论，但要同时控制所有整数会遇到强依赖和极端偏差问题。
- 已知结果已经排除了过强的 sqrt(log n) 级均匀逼近，因此若存在正例，其误差必须比直觉上的强集中更粗糙；这使候选构造很难验证。
- 若答案为否，需要证明所有集合 A 的表示函数都存在归一化振荡，这是全局结构定理，通常比有限计算或局部估计难得多。
- 计算搜索只能覆盖有限前缀；从有限模式外推出无限构造或无限障碍需要新的数学压缩原则。
- 题目属于经典开放数论/加性组合问题，仅凭工具增强的大模型不太可能稳定产生完整原创证明。

### 需要的验证

- 严格确认卷积计数约定、自然数起点、是否计有序表示等形式化细节，因为常数极限会受规范影响。
- 若提出构造，需要证明 r_A(n)/log n 对所有充分大 n 收敛，而不是只在密度一子集或高概率意义下成立。
- 若提出否定证明，需要检查是否真正排除了任意非零常数极限，而不只是排除极限为 1 或过小误差项。
- 所有概率论步骤都需验证依赖性处理、Borel-Cantelli/局部引理条件和无限阶段极限交换。
- 计算发现必须转化为可证明引理，并用独立脚本或形式化系统复核有限搜索边界。

### 公开版思考摘要

这个问题对 AI 友好的一面是定义清楚、已形式化、已有接近目标的随机模型和明确的已知障碍；不友好的一面是关键差距正落在最难的地方：从“除密度零异常集外成立”提升到“所有充分大 n 成立”，或证明任何集合都必须有固定振荡。GPT-5.5 级别模型更可能在复现文献证明、发现有限模型规律、验证候选构造失败点、或提出可检查的新引理方面有价值；完整解决的概率仍偏低。

### 免责声明

以上是对 AI 辅助可推进性的评估，不是该 Erdős 问题的解答，也未声称存在或不存在满足条件的集合 A。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_66.md](../../prompts/problem_66.md)

### 状态结论

截至 2026-07-27，题库仍将第 66 题列为 open，且形式化项目也把它作为 research-open 命题收录；未找到可检查的完整证明或反例。2026-07-18 的 Kuang–Wang 预印本解决的是“允许密度零例外集”的相关问题，并不去除例外集，也不实现 \(r_A(n)\sim c\log n\)。因此它不是本题的解答。

### 当前规范陈述

令 \(\mathbb N=\{1,2,\ldots\}\)。对 \(A\subseteq\mathbb N\)，定义有序加法表示函数 \(r_A(n)=(1_A*1_A)(n):=\sum_{a=1}^{n-1}1_A(a)1_A(n-a)=|\{(a,b)\in A^2:a+b=n\}|\)。是否存在 \(A\subseteq\mathbb N\) 及有限实常数 \(L\ne0\)，使 \(r_A(n)/\log n\to L\)？必有 \(L>0\)。\(\log\) 为自然对数，极限须沿全部整数 \(n\) 成立，不允许密度零或任何其他例外集。

```text
Let \(\mathbb N=\{1,2,\ldots\}\). For \(A\subseteq\mathbb N\), define the ordered additive representation function \(r_A(n)=(1_A*1_A)(n):=\sum_{a=1}^{n-1}1_A(a)1_A(n-a)=|\{(a,b)\in A^2:a+b=n\}|\). Does there exist \(A\subseteq\mathbb N\) and a finite real constant \(L\ne0\) such that \(\lim_{n\to\infty}r_A(n)/\log n=L\)? Necessarily \(L>0\). Here \(\log\) is the natural logarithm and the limit is required along every integer \(n\), with no exceptional set.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 在有限实极限的规范解释下，未找到可立即否定或肯定命题的简单构造。唯一明显的“退化”来自把极限误作扩展实数：\(A=\mathbb N\) 给出 \(+\infty\)，因此必须明确有限性；这不是规范问题的解答。
- 版本变化: Erdős 的 1980 调查文献中提出常数 1 的版本，并表示不相信存在这种序列。现题库的措辞放宽为“某个非零有限极限”。1985–1986 年 Erdős–Sárközy 的结果及 Horváth 2007 年改进只排除了远小于 \(\sqrt{\log n}\) 的逐点误差，未排除 \(o(\log n)\) 误差。2026 年 Kuang–Wang 给出仅在密度一集合上逼近某个 \(O(\log\log n)\) 单调函数的构造；它确认例外集条件实质重要，却未修订或解决本题。

陈述问题：

- 孤立地看，星号 \(1_A*1_A\) 可能被误读为 Dirichlet convolution；本题标签、题页备注及所有引用结果均讨论 \(a+b=n\) 的加法表示，故规范陈述采用加法卷积。Formal Conjectures 的 issue 标题误称 “Dirichlet self-convolution”，但其正文仍复述了原符号；这不能作为改变数学含义的依据。
- “limit exists and is \(\ne0\)”应理解为有限实数极限。若允许扩展实数 \(+\infty\)，取 \(A=\mathbb N\) 即有 \(r_A(n)=n-1\) 且比值趋于 \(+\infty\)，问题会退化。
- 有序与无序表示函数相差约两倍但并不相同；尤其不能把只计 \(a\le b\) 或要求两项不同的文献结论未经换算直接当作本题结论。
- Erdős 1980 年明确问的是常数为 1 的特例；当前题库把目标写成任意非零有限常数。尚未发现两种存在性问题等价的证明。

需要固定的量词/约定：

- The existential quantifiers are \(\exists A\subseteq\mathbb N\,\exists L\in\mathbb R\setminus\{0\}\).
- The convergence means: for every \(\varepsilon>0\) there is \(N\) such that for every integer \(n\ge N\), \(|r_A(n)/\log n-L|<\varepsilon\).
- Representations are ordered and allow \(a=b\); changing either convention changes the displayed function by diagonal and/or factor-of-two effects.
- The limit is finite and real; no exceptional subsequence or density-one qualification is permitted.

### 文献与当前边界

已核验的主要结果：

- Erdős–Sárközy（1986，同行评审）明确记录了该 \(\log n\) 渐近常数猜想，并证明更强误差尺度的逼近不可能：对合适单调 \(F\)，\(\max|R(n)-F(n)|=o(\sqrt{F(n)})\) 不可能。该结论不能从 \(R(n)=L\log n+o(\log n)\) 推出矛盾。
- Horváth（2007，同行评审）把上述点态障碍定量化为：最终误差不可能处处至多 \((1-\epsilon)\sqrt{g(n)}\)。对 \(g(n)=\log n\) 而言，仍远弱于排除 \(o(\log n)\) 误差。
- Erdős–Tetali（1990，同行评审）以概率方法构造表示数 \(\Theta(\log n)\) 的渐近基，说明正确数量级不是障碍；上下常数界不蕴含比值有极限。
- Fang（2022，同行评审）和 Kuang–Wang（2026，预印本）表明一旦允许密度零例外集，表示函数的可控性会显著增强；两者的集合、函数或表示约定均与本题逐点目标不同。

最近相关工作：Kuang–Wang，arXiv:2607.16613（2026-07-18，预印本）是检索到的最新直接相关工作。其定理 1.4 在密度一整数上构造 \(|r_1(A,n)-f(n)|=1\)、\(f(n)=O(\log\log n)\)；这支持“无例外集”是实质难点，但不构成第 66 题进展的完整证明。

剩余核心：对每个 \(A\subseteq\mathbb N\)，是否能排除存在有限 \(L>0\) 使有序加法表示函数 \(r_A(n)=L\log n+o(\log n)\) 对所有充分大整数同时成立；或反过来构造一个满足此逐点渐近式的集合。历史上的 \(L=1\) 版本只是当前“存在某个 \(L>0\)”目标的特例，不能擅自等同。

已使用方法：

- Erdős–Sárközy 的均方/表示函数正则性障碍与生成函数分析。
- Horváth 的 Erdős–Fuchs 型振荡下界和单调目标函数比较。
- 概率构造经济加法基，给出 \(\Theta(\log n)\) 而非极限。
- 针对密度一版本的数字展开、例外集计数及生成函数/组合方法。

争议或不确定性：

- 本次未能通过可公开读取的题库 forum 页面检查两条评论，因页面返回 403；搜索结果没有显示任何可检验的解答主张。
- Formal Conjectures 的 issue 标题中的 “Dirichlet” 与题目实际加法语境不一致；应以定义和原始文献为准，不应把标题当作数学定义。
- Kuang–Wang 是发表仅九天的预印本，尚非同行评审；其与本题的关系已由正文范围核对，而不是由摘要标题推断。

### 证据来源

- [Erdős Problem 66 — LaTeX source](https://www.erdosproblems.com/latex/66) — Thomas F. Bloom / Erdős Problems contributors, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 给出当前题目、Erdős 的否定预期、Erdős–Sárközy 与 Horváth 的已知障碍，并将问题列作未解记录。
- [A Survey of Problems in Combinatorial Number Theory](https://combinatorica.hu/~p_erdos/1980-03.pdf) — Paul Erdős, 1980; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`medium`. 历史来源：题库称 Erdős 在该文中明确提出极限为 1 的版本。该可访问扫描件确认文献题名、作者、期刊卷页与年份；本次未将不可定位的页面文字当作额外定理证据。
- [Problems and Results on Additive Properties of General Sequences, II](https://users.renyi.hu/~p_erdos/1986-12.pdf) — Paul Erdős, András Sárközy, 1986; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 该文直接陈述：存在表示数在 \(\log n\) 量级的序列；并称不存在 \(R(n)/\log n\to c\in(0,\infty)\) 是 Erdős 的旧猜想。其定理还给出在单调 \(F(n)=o(n/(\log n)^2)\) 下，表示函数不能以 \(o(\sqrt{F(n)})\) 量级逐点逼近 \(F\)。
- [An Improvement of a Theorem of Erdős and Sárközy](https://doi.org/10.1556/Pollack.2.2007.S.14) — Gábor Horváth, 2007; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明：若 \(g\) 单调、趋于无穷且 \(g=o(n/(\log n)^2)\)，则对任意 \(\epsilon>0\)，\(|R_2(n)-g(n)|\le(1-\epsilon)\sqrt{g(n)}\) 不可能最终处处成立。取 \(g=\log n\) 是本题的相关但不足以解决的障碍。
- [Representations of Integers as the Sum of k Terms](https://onlinelibrary.wiley.com/doi/10.1002/rsa.3240010302) — Paul Erdős, Prasad Tetali, 1990; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 给出每个固定 \(k\) 的渐近基，其表示数为 \(\Theta(\log n)\)。这说明 \(\log n\) 尺度可达，但不提供逐点收敛到常数的结论。
- [Solutions to Two Problems of Sárközy and Sós on Additive Representation Functions](https://arxiv.org/abs/2607.16613) — Peiru Kuang, Yan Wang, 2026-07-18; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 证明存在 \(A\) 和递增 \(f=O(\log\log n)\)，使 \(|r_1(A,n)-f(n)|=1\) 除一个显式密度零例外集外成立；作者明确称其解决的是 Sárközy–Sós 1997 的密度一问题。它不去除例外集，也不证明本题极限。
- [Representation Functions Avoiding Integers with Density Zero](https://www.sciencedirect.com/science/article/pii/S0195669821001840) — Jin-Hui Fang, 2022; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 在允许指定密度零集合且集合可取于整数的不同设置下，构造无序表示函数在例外集外为 1。该结果只能说明例外集版本具有不同性质，不能用于 \(A\subseteq\mathbb N\) 的逐点问题。
- [Formal Conjectures issue #278: Erdős Problem 66](https://github.com/google-deepmind/formal-conjectures/issues/278) — Formal Conjectures contributors, 2025-06-30; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`medium`. 该 issue 将命题标为 research open 并复述题目；其关闭关联形式化工作流，而非数学证明。Formal Conjectures 项目声明其用途包括收录尚无证明的开放猜想陈述。

### 完成标准

- 肯定出口: Exhibit an explicitly defined or rigorously proved-to-exist set A⊆N and a finite L>0, and prove that for every ε>0 there is N such that every integer n≥N satisfies |r_A(n)/log n−L|<ε, where r_A counts ordered pairs (a,b)∈A² with a+b=n.
- 否定出口: Prove that for every A⊆N and every finite L>0, the sequence r_A(n)/log n does not converge to L; equivalently, show that no A has r_A(n)=L log n+o(log n) simultaneously for all integers n→∞.

不构成完成：

- A construction with r_A(n)=Θ(log n), bounded limsup, or the right behavior only on a subsequence.
- A density-one or almost-all-n construction, even with a quantitative density-zero exceptional set.
- An obstruction only to o(sqrt(log n)) error, or any result compatible with an o(log n) error.
- Numerical evidence on a finite interval, randomized sampling without a uniform proof, or a result for a different representation convention.
- A proof only for L=1 unless it also establishes the stated existential-any-L alternative or proves a justified reduction.

正确性陷阱：

- Verify that * is additive convolution, not Dirichlet convolution, and state whether pairs are ordered.
- Keep the target limit finite and real; otherwise A=N gives a vacuous extended-limit reading.
- Do not replace 'for every sufficiently large n' by density one, a subsequence, an average, or Cesàro convergence.
- Track diagonal representations a=a and the factor-of-two relation between ordered and unordered representation functions.
- Check every use of a monotonic target-function theorem: r_A(n) itself need not be monotone, and its hypotheses may be stronger than asymptotic equivalence.
- Do not infer convergence from Θ(log n), nor an all-n result from a zero-density-exception result.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `18/100`
- 信心: `medium`
- 结论: 这是定义清楚、可审计的开放证明目标，但已有四十余年障碍结果且已知方法与所需的 \(o(\log n)\) 级别之间仍有很大缺口；适合谨慎的证明优先研究，不适合以有限计算或表面概率直觉为主导。

支持理由：

- 目标可精确形式化，正反两种完成条件清晰，并有可直接核查的表示函数定义。
- 存在明确的已知边界：\(\Theta(\log n)\) 构造、\(\sqrt{\log n}\) 级别的不规则性障碍，以及密度一构造。
- 近期预印本使“例外集为何不能简单删除”成为可具体检验的结构问题。

主要障碍：

- 现有逐点不可能性仅控制远小于 \(\log n\) 的误差，不能直接排除极限。
- 概率模型天然容易只给出高概率或密度一结论；将其提升为全部整数需要新的统一机制。
- 有序/无序、正整数/非负整数和例外集版本之间的迁移很容易造成伪进展。

Proof-first 路线：

- 先尝试从假设 \(r_A(n)=L\log n+o(\log n)\) 推出一个新的、可与 Erdős–Sárközy或 Horváth 振荡定理冲突的加权均方或短区间结论；每一步必须写出误差损失。
- 独立研究生成函数 \(F(z)^2\) 在 \(z\to1^-\) 与单位圆其他点的约束，目标是导出定量振荡而非仅平均阶。
- 独立审计概率/数字构造：确定是否存在可消除全部例外点的局部修补引理；若修补改变无穷多其他表示，须给出严格停止理由。

需要验证：

- 人工复核 Erdős 1980 原文中 \(L=1\) 的精确措辞及其与数据库宽化版本的关系。
- 在投入求解前，复核 Kuang–Wang 预印本的全部证明和其集合是否可适配正整数、有序表示及 \(\log n\) 尺度。
- 若使用 Formal Conjectures，下载并编译具体第 66 题文件，确认其仅形式化陈述且其卷积定义没有误译。

### 审计限制与人工复核理由

- 题库主页面和 forum 页面在本次浏览中返回 403；通过可访问的 LaTeX 页面核对题干和备注，但未能读取 forum 的两条评论。
- 没有发现解答并不是不存在解答的逻辑证明。当前“confirmed_open”主要依赖 2026 年仍标为 open 的题库记录、开放命题形式化记录，以及对精确短语、作者、近三年 arXiv 和相关文献的定向检索。
- Erdős 1980 扫描件可访问，但本次工具未可靠定位其中特例 \(L=1\) 的具体页码；该历史归因同时由当前题库备注和 1986 Erdős–Sárközy 论文的“old conjecture”表述交叉支持。
- 2026 Kuang–Wang 工作是极新的未审稿预印本；本审计仅据其公开全文核对其定理范围，未做逐行证明验证。

- 若要据此投入长期研究，应由人工复核 Erdős 1980 年原文的精确常数版本，以及当前题库从 \(L=1\) 到“任意非零 \(L\)”的历史关系。
- 应人工获取并审阅 Formal Conjectures 中实际第 66 题 Lean 文件，确认卷积编码及其只形式化陈述而非给出证明。
- 应复核最新 Kuang–Wang 预印本的证明和后续版本状态；它很新，可能在审计日期之后迅速更新。

<!-- DEEP_REVIEW:END -->
