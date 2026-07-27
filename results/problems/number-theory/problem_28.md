# Problem 28

## 基本信息

- 原始链接: https://www.erdosproblems.com/28
- LaTeX 页面: https://www.erdosproblems.com/latex/28
- 原始状态: `open`
- 奖金: `$500`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive basis`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

If $A\subseteq \mathbb{N}$ is such that $A+A$ contains all but finitely many integers then $\limsup 1_A\ast 1_A(n)=\infty$.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `29/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：\gg, for all large, limsup
- 原记录含奖金 $500，说明该题被长期视为高价值难题；这不是否定依据，但提高验证门槛。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: additive basis
- 证明密集标签命中: number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: \gg, for all large, limsup
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低候选：GPT-5.5 级别模型配合计算、形式化和检索工具，较可能给出有价值的局部验证、等价改写、反例搜索框架或特殊情形证明，但直接完成该开放猜想的概率很低。**
- 等级: `low_candidate`
- 分数: `22/100`
- 信心: `medium`
- 可能路线: 可尝试反证：假设表示函数 1_A*1_A(n) 最终有统一上界，同时 A+A 余有限；先形式化基本计数不等式和密度下界，再用生成函数、区间分解、模结构或稀疏基构造分析寻找矛盾。计算工具适合搜索有限前缀上的低表示数二阶渐近基模型，形式化工具适合验证候选引理，但核心无限组合论突破仍是瓶颈。

### 支持理由

- 命题表述短且已形式化，适合被证明助手拆成精确定义、有限引理和反证目标。
- 假设 A+A 覆盖所有充分大整数，本身提供强覆盖性约束；模型可系统挖掘计数、密度和表示数之间的必要条件。
- 反例搜索和 SAT/SMT/ILP 可用于有限窗口内探索“低表示数但高覆盖”的极端结构，帮助发现模式或排除错误证明。
- 备注中给出的更强形式提示了自然路线：研究表示函数增长下界，尤其是与对数级增长或 |A∩[1,N]| 下界相关的强化命题。

### 主要障碍

- 这是经典开放型加性数论猜想；有限计算只能测试截断版本，不能直接证明余有限覆盖下的无界性。
- 单纯计数给出的平均表示数信息可能不足，因为 A 可以很稀疏且表示分布高度不均匀。
- 若假设表示数有界，需要从全局覆盖推出局部或结构性矛盾；这通常需要新的组合或解析思想，而不是机械枚举。
- 模型容易产生看似合理但实际存在边界项、重复计数、密度量词或无限极限漏洞的证明草稿。

### 需要的验证

- 任何候选证明都需形式化检查关键量词：A+A 含所有但有限多整数、limsup 无界、以及卷积表示数的定义。
- 需要独立验证所有从覆盖性到密度下界、从密度到表示数下界的推导，防止只证明平均意义或有限区间版本。
- 若产生计算证据，应明确窗口大小、边界条件、搜索编码和不可满足证书，并说明其不能替代无限证明。
- 若使用文献检索，应只用于定位已知等价形式、已证明特殊情形或已有反例边界，避免把已知未完成的强化猜想误当作引理。

### 公开版思考摘要

这个问题的优势是定义清楚、形式化状态良好、可被工具化拆解；模型可以围绕有界表示数假设进行反证探索，并用计算搜索极端有限模型来辅助发现结构。但问题的难点正是从余有限二重和覆盖推出表示数必然无界，这不是有限验证或标准密度计数可直接解决的。综合看，AI 有望显著整理路线、排除伪证、证明特殊情形或提出可检验引理，但直接给出完整可靠证明的可能性较低。

### 免责声明

以上是对 AI 工具辅助可推进性的审查，不是该 Erdős 问题的证明或反证。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_28.md](../../prompts/problem_28.md)

### 状态结论

该题是自然数上二阶渐近加法基的 Erdős–Turán 猜想。截至审计日，Erdős Problems 的近期状态记录、未填补的正式 Lean 陈述，以及 2026 年仍将其作为未解猜想研究的论文共同支持其仍为开放问题。发现了 Agama 与 Smpokos 的非同行评审“证明”声明，但未找到可核验的同行评审发表、形式化证明或独立详细验证；它们不能改变开放状态。

### 当前规范陈述

对任意集合 A⊆ℕ，定义有序表示函数 r_A(n)=(1_A*1_A)(n)=#{(a,b)∈A×A:a+b=n}。若存在 N0∈ℕ，使每个 n≥N0 都属于 A+A（等价地 r_A(n)≥1），则 limsup_{n→∞}r_A(n)=∞。等价地，对任意 M,X∈ℕ，存在 n≥X 使 r_A(n)≥M。

```text
For every set A ⊆ ℕ, define the ordered representation function r_A(n)=(1_A*1_A)(n):=#{(a,b)∈A×A:a+b=n}. If there exists N0∈ℕ such that every integer n≥N0 belongs to A+A (equivalently, r_A(n)≥1), then limsup_{n→∞} r_A(n)=∞. Equivalently, for every M∈ℕ and every X∈ℕ, there exists n≥X with r_A(n)≥M.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未找到能满足自然数上最终覆盖而使有序表示函数全局有界的简单构造。检索到的整数群 ℤ 上唯一表示基及有限循环群构造均不满足本题的单侧自然数结论，不能构成反例。该结论仅表示已做针对性检查，不是对所有构造的穷尽证明。
- 版本变化: 原始目标未见被后续文献替换或拆分为非等价的“修订题”。Erdős–Turán 另提出更强的定量猜想 limsup r_A(n)/log n>0；题页还提到仅假设 |A∩[1,N]|≫N^{1/2} 的更强变体。这些是独立强化目标，不能当作本题已解决后的残余版本。

陈述问题：

- 输入陈述未展开卷积、limsup 及“all but finitely many integers”的量词；标准解释如 canonical statement 所示。
- ℕ 是否包含 0 在文献中不统一；改变有限多个元素不影响“最终覆盖”与无界 limsup，故不是实质歧义。
- 表示数必须按输入中的卷积解释为有序对数。若改用无序表示数，只会在对角项和常数因子上不同，但审计和证明中不得混用。
- A⊆ℤ 的类似命题是假的（存在唯一表示基）；这不是本题的反例，因为本题关键地限制 A⊆ℕ。

需要固定的量词/约定：

- The outer quantifier is universal over every A⊆ℕ.
- “A+A contains all but finitely many integers” means ∃N0 ∀n∈ℕ, n≥N0 ⇒ ∃a,b∈A, a+b=n.
- The convolution counts ordered pairs, including a=b when 2a=n.
- The conclusion is a limsup statement: it requires arbitrarily large values along a subsequence, not r_A(n)→∞.

### 文献与当前边界

已核验的主要结果：

- Erdős–Turán（1941，同行评审）提出该问题，并构造了表示数为 O(log n) 的稀疏二阶基背景，因此对数级别是自然但未证实的强猜想尺度。
- Dirac（1951，同行评审；由后续综述引用）证明表示函数不能从某处起恒等于常数，这是远弱于无界性。
- Borwein–Choi–Chu（2006，Mathematics of Computation，同行评审）通过计算密集型方法排除了最终覆盖基的全局有序表示数上界 7；这给出了确定的有限阈值障碍，而非任意阈值。
- Dowd（1988，SIAM J. Discrete Math.，同行评审）研究了有限问题、整数版本和编码论关联；相关有限模型有其自身的性质，不能直接同自然数单侧结论等同。
- Sándor–Yang（2018，European Journal of Combinatorics，同行评审）对循环群中的 Ruzsa 数及低表示数时缺失和的比例给出结果；这是有限群障碍的结构信息。
- Ding–Zhao（2024，International Journal of Number Theory，同行评审）将任意循环群的 Ruzsa 数统一上界由 288 改进为 192。

最近相关工作：截至 2026-07-27，最直接的近期自然数结果是 Li–Zhang 的 arXiv:2605.30922（2026-05-29，预印本）：当 E=ℕ\(A+A) 的上密度小于 7/32 时，limsup r_A>5；在本题 E 有限时该结论只给出有限下界。最新的相关有限群进展是 Ding–Sun–Zhao 的 arXiv:2607.06167（2026-07-07，预印本），证明 R_m≤128；它不解决本题。

剩余核心：对每个固定 C，排除存在 A⊆ℕ 使 A+A 最终覆盖且 r_A(n)≤C 对所有 n 成立；等价地，统一排除任何有界有序表示函数的渐近二阶基。已知排除小常数和稠密缺失集条件都不能推进到任意 C。

已使用方法：

- 生成函数与表示函数的解析/组合关系。
- 有限循环群、Ruzsa 数及从局部模构造获得的障碍或类比。
- 有限情形的穷举和可认证计算（Borwein–Choi–Chu 的小上界排除）。
- 密度型表示函数不等式，按 E=ℕ\(A+A) 的上密度量化缺失和。
- 有限域二次图与加法构造，用于相关循环群覆盖问题。

争议或不确定性：

- Agama（arXiv:1707.05679）和 Smpokos（OSF 预印本）均声称证明，但本次未找到独立核验、同行评审或无 sorry 的形式化工件；应视为未经证实声明而非反例或定理。
- Erdős Problems 页面与论坛线程在本次直接抓取中分别出现内部错误和 403；但 2026-07-13 的独立记录及正式猜想文件均仍标注 open。
- 循环群 Ruzsa 数的统一上界并不自动产生自然数上的有界表示基；任何声称由此推出反例或解决的论证都必须给出并验证明确的极限/转移定理。

### 证据来源

- [Erdős Problem 28](https://www.erdosproblems.com/28) — Erdős Problems community database, 2025-08-31; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 给出本题原始陈述、奖金额与“open”数据库状态。直接抓取页面及 LaTeX 页在本次审计中返回服务内部错误，故状态还由后述近期独立记录交叉核验。
- [Erdős–Turán conjecture: must an additive basis of order 2 have unbounded representation function? (Erdős #28)](https://api.scinet.pub/p/c24c8b25-cb70-48da-a5b8-87a128d5992f) — SciNet Acquisition, 2026-07-13; `secondary_index`, `informal_claim`, directness=`indirect`, reliability=`medium`. 明确记录其于 2026-07-13 从 erdosproblems.com/28 读取到 open 状态，并准确重述有序表示版本；该记录本身不是数学证明。
- [On a problem of Sidon in additive number theory, and on some related problems](https://doi.org/10.1112/jlms/s1-16.4.212) — Paul Erdős; Pál Turán, 1941; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 该猜想的原始来源；提出了二元表示函数的无界性问题及对数尺度的背景。
- [An old conjecture of Erdős–Turán on additive bases](https://www.ams.org/mcom/2006-75-253/S0025-5718-05-01777-1/) — Peter Borwein; Kwok-Kwong Stephen Choi; Frank Chu, 2006; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明在最终可表示的情形下表示函数不能全局被 7 控制；并给出计算密集型算法。它没有证明表示函数无界。
- [Questions Related to the Erdős–Turán Conjecture](https://epubs.siam.org/doi/10.1137/0401016) — Martin Dowd, 1988; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 给出与有限问题、整数版本及编码论联系的严格研究框架；不构成原猜想的解决。
- [An Improvement of Konstantoulas' Density Constant](https://arxiv.org/abs/2605.30922) — Huixi Li; Zihan Zhang, 2026-05-29; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 对 E=ℕ\(A+A) 的上密度条件给出部分结论：上密度小于 7/32 时 limsup r_A>5，并给出其他有限阈值及条件性结论；仍把原命题称为猜想。
- [An improved upper bound on the Ruzsa number](https://arxiv.org/abs/2607.06167) — Yuchen Ding; Yu-Chen Sun; Lilu Zhao, 2026-07-07; `preprint`, `preprint`, directness=`indirect`, reliability=`medium`. 证明循环群 Ruzsa 数 R_m≤128，改进 2024 年的 192；这是有限循环群相关问题的最新进展，不推出自然数上猜想。
- [A new upper bound on Ruzsa's number on the Erdős–Turán conjecture](https://arxiv.org/abs/2307.12311) — Yuchen Ding; Lilu Zhao, 2023-07-23; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 预印本及其 2024 年期刊版本证明所有 m 有 R_m≤192，改进 Chen 的 288；说明有限模型的有界构造持续存在。
- [FormalConjectures.ErdosProblems.28](https://raw.githubusercontent.com/google-deepmind/formal-conjectures/main/FormalConjectures/ErdosProblems/28.lean) — Formal Conjectures Authors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. Lean 文件准确形式化 A 的最终和集覆盖蕴含 sumRep 的 limsup 为 ⊤，但定理证明仍为 sorry，并标注 research open；它是陈述形式化而非证明。
- [An extension of the Erdős–Turán additive base conjecture via generalized circles of partition](https://arxiv.org/abs/1707.05679) — Theophilus Agama, 2017-07-16; `preprint`, `preprint`, directness=`direct`, reliability=`low`. 作者摘要声称证明该猜想；未找到同行评审发表、形式化证明或独立验证。其 arXiv HTML 当前还显示异常的版本标题内容，不能视作已核验解决。
- [A Proof of the Erdos-Turan Conjecture on Asymptotic Additive Bases](https://sciety.org/articles/activity/10.31219/osf.io/mxgbu) — Konstantinos Smpokos, 2024; `preprint`, `informal_claim`, directness=`direct`, reliability=`low`. OSF 预印本摘要声称完整证明，且有 2026-07-10 的版本活动；未找到同行评审、正式验证或可独立确认的接受记录，故不能据此关闭问题。

### 完成标准

- 肯定出口: A complete proof that for every A⊆ℕ and every N0 with [N0,∞)∩ℕ⊆A+A, for every M,X∈ℕ there is n≥X with #{(a,b)∈A²:a+b=n}≥M.
- 否定出口: An explicit set A⊆ℕ (with a mathematically precise membership rule) and a finite C such that A+A contains every sufficiently large natural number and #{(a,b)∈A²:a+b=n}≤C for every n∈ℕ, together with complete proofs of both properties.

不构成完成：

- Proving the conclusion only for dense bases, random bases, structured bases, or a fixed subclass.
- Ruling out only one further bound C, or reproducing the known C=7 exclusion.
- Showing limsup r_A(n)>K for one fixed K, even under the exact eventual-coverage hypothesis.
- Proving an averaged representation lower bound without converting it to arbitrarily large pointwise values.
- A finite search over initial segments or cyclic groups without a proved reduction and exhaustive certificate.
- An argument for A⊆ℤ, or an unordered-representation statement without a valid transfer to the ordered ℕ version.
- Treating an unreviewed preprint claim as a proof.

正确性陷阱：

- Keep A⊆ℕ; unique representation bases in ℤ are irrelevant counterexamples.
- Count ordered pairs and handle diagonal pairs a=b correctly.
- Do not replace limsup=∞ by the stronger and unrequired limit r_A(n)=∞, nor by eventual monotonicity.
- The hypothesis is eventual coverage, not coverage only on a density-one set or on a subsequence.
- A finite cyclic construction or a uniform bound for R_m does not by itself pass to an infinite one-sided basis.
- Any compactness, lifting, or limiting step must preserve both eventual coverage and a uniform pointwise representation bound.
- If computation is used, state its finite domain, isomorphism reductions, certificate, and the theorem converting that finite result into the infinite claim.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `8/100`
- 信心: `high`
- 结论: 这是陈述精确且可形式化的真正开放问题，但已公开近一个世纪，现有进展主要仅排除小的有限上界或增加附加条件；在没有实质新理论输入时，AI 在一次研究运行中完全解决它的机会很低。

支持理由：

- 目标有清晰的全称量词、正反两类可验证完成条件，并已有忠实的 Lean 陈述。
- 已有有限阈值、密度型和循环群工作，能为可审计的局部引理提供具体基线。
- 反例方向可要求显式成员规则和统一常数，理论上可被逐步核查。

主要障碍：

- 需从“排除有限个小 C”跨越到任意 C；这不是简单扩大计算范围。
- 自然数单侧性至关重要，有限群/整数群类比不能自动传递。
- 缺乏将平均、密度或模信息提升为点态无界性的已知一般机制。
- 近期非同行评审证明声明增加了先做严苛错误审查的必要性，但不提供已验证工具。

Proof-first 路线：

- 先建立一个严格的桥梁引理：在假设 r_A≤C 下，推出可量化的结构、缺失和密度或有限商约束；只有该引理明确后再探索其后果。
- 独立审计所有声称的证明，定位可形式化的关键断言；若发现可修补的有效引理，将其与原结论严格区分。
- 研究对固定 C 的可认证排除能否产生随 C 增长的归纳、紧致性或单调推进机制；不能把“更多 C 的计算”误报为一般证明。
- 用生成函数、表示函数累计误差和一侧边界效应寻找直接矛盾，但每步必须保留点态有界假设。

需要验证：

- 核验 Agama 与 Smpokos 全文证明中每个从密度/能量到无界表示数的关键推理；除非获得完整可检查论证，不得采纳。
- 复核 Borwein–Choi–Chu 的常数、其有序/无序约定以及从全覆盖到最终覆盖的准确版本。
- 若使用 2026 预印本结果，核查版本、定义的密度及其是否真的适用于 E 有限。
- 任何 Lean 进展必须消除 erdos_28 文件中的 sorry，并检查 sumRep、Pointwise A+A 和 limsup 的语义吻合自然语言目标。

### 审计限制与人工复核理由

- Erdős Problems 的问题页和 LaTeX 页在本次直接抓取时返回内部错误；论坛 thread/28 返回 403。因此官方当前状态由输入记录、2026-07-13 的独立抓取记录和仍为 sorry 的正式声明交叉支持，而非由本次成功渲染的官方页面正文单独支持。
- 未能取得 Agama 或 Smpokos 声称证明的独立同行评审反驳或逐行审稿；结论只是这些声明尚未达到可接受证明标准，不能断言它们已被正式证伪。
- 2026 年预印本在审计日后仍可能修订或撤回；其结果按预印本而非已定论文献处理。
- “最强已知结果”的措辞限于本次定向检索可直接核验的文献；不存在从未发现解决方案逻辑推出“绝无解决方案”的结论。

- 应由具有加性数论专长的人逐行审计 Agama 与 Smpokos 的未经验证证明声明，尤其是任何从密度、能量或有限模型推到点态无界性的步骤。
- 若后续研究要依赖 Borwein–Choi–Chu 的精确常数、表示数约定或其针对最终覆盖的变体，应直接阅读正式论文全文核对。
- 官方页面和论坛的抓取限制意味着最终发布前宜由人工再次打开页面确认状态与讨论线程。

<!-- DEEP_REVIEW:END -->
