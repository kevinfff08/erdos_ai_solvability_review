# Problem 122

## 基本信息

- 原始链接: https://www.erdosproblems.com/122
- LaTeX 页面: https://www.erdosproblems.com/latex/122
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

For which number theoretic functions $f$ is it true that, for any $F(n)$ such that $F(n)/f(n)\to 0$ for almost all $n$, there are infinitely many $x$ such that\[\frac{\#\{ n\in \mathbb{N} : n+f(n)\in (x,x+F(x))\}}{F(x)}\to \infty?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `24/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：for all large, infinitely many, prime

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: for all large, infinitely many, prime
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能由 GPT-5.5 级别模型一次性完整解决，但有中等机会对可验证子类作出实质推进，尤其是重建并推广已知的 τ(n)、ω(n) 情形，提出可检验的充分条件，或为 φ(n)、σ(n) 型函数寻找失败机制与反例候选。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 较现实的路线不是直接回答“所有数论函数 f”的完整分类，而是把问题重写为关于移位值集 n+f(n) 的短区间聚集现象。模型可尝试抽取 EPS97 类型证明中的核心输入，例如 f 的慢增长、正常阶、局部可调性、在短区间内的值域压缩能力，然后给出一个抽象充分条件并验证它适用于 ω(n)、τ(n) 或若干相近函数。另一条路线是对 φ(n)、σ(n) 建立启发式或条件性障碍：这些函数通常量级较大且乘法结构刚性更强，n+f(n) 的短区间异常聚集可能缺少必要的压缩机制。计算实验可用于搜索聚集现象、测试 F(x) 选择、定位可能的反例序列，但难以单独构成证明。

### 支持理由

- 题目已有明确线索：τ(n)、ω(n) 被报告可处理，φ(n)、σ(n) 被怀疑失败，这给模型提供了可逆向工程的证明目标和反例目标。
- 问题核心涉及经典解析数论与概率数论中的正常阶、短区间、乘法函数取值分布；GPT-5.5 配合文献检索和符号/数值实验，可能重建局部引理并形成可审计的充分条件。
- 对特定函数的验证比完整分类更可行，例如证明某些慢增长、值域可压缩、在短区间内波动受控的函数满足该聚集性质。
- 形式化证明工具可用于校验组合计数、极限量词和抽象充分条件，但主要解析数论估计仍需人工级洞察或文献级定理输入。

### 主要障碍

- 题目要求“for which number theoretic functions f”，范围过宽；若不预先限定函数类别，完整分类可能接近元问题而不是单一定理。
- 量词很强：对任意满足 F(n)/f(n) -> 0 almost all n 的 F，都要得到无限多 x 上的异常高密度聚集，这比证明某个自然 F 的聚集强得多。
- 已知备注只给出 τ、ω 的正例和 φ、σ 的失败猜测，没有提供统一判别准则；模型需要发明或恢复深层结构。
- 短区间中 n+f(n) 的聚集依赖 f 的细粒度分布，而乘法函数在短区间的精确行为通常是困难解析数论问题。
- 若要证明 φ(n) 或 σ(n) 失败，必须构造某个 F 并证明所有足够多 x 上都没有所需爆发式聚集，这类反向结论通常更难。

### 需要的验证

- 检索并核对 Er97、Er97e、EPS97 中原始命题、量词和已证明范围，确认当前 JSON 中的表述没有省略关键限制。
- 把极限表达式形式化：应明确是沿无限 x 序列使比值无界，还是存在无限多 x 满足某种趋于无穷的序列性陈述。
- 复现 τ(n)、ω(n) 情形的证明框架，分离出可复用的充分条件，并逐条检查条件是否真正推出题目中的任意 F。
- 对候选失败函数 φ(n)、σ(n) 做计算实验与启发式建模，寻找合适的 F(x) 以及可能的上界策略。
- 若提出新分类或充分条件，需要同行级审查，尤其检查 almost all 条件、短区间端点 x 与 n 的尺度替换、以及异常集合处理。

### 公开版思考摘要

这个问题对 AI 的主要可行性在于“局部推进”而不是“完整解决”。题目已有正例和疑似负例，说明存在结构性分界；GPT-5.5 级别模型可以利用文献检索、计算实验和形式化校验，把已知正例抽象成若干充分条件，并测试更多函数。但完整回答所有数论函数 f 需要一个统一分类理论，还要处理强量词和短区间乘法函数分布，这明显超出现阶段模型可靠独立完成的范围。

### 免责声明

以上是对 GPT-5.5 级别模型可推进性的审查，不是该 Erdős 问题的解答，也不声称给出了新的定理或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `ambiguous`
- 状态信心: `high`
- 可行动性: `needs_human_clarification`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_122.md](../../prompts/problem_122.md)

### 状态结论

字面记录不是一个可唯一赋值真假的命题：它说“有无穷多个 x 使得一个仍依赖 x 的量趋于无穷”，但没有定义该极限沿何变量/子序列取得。因此不能把数据库的 open 标签直接转为一个可求解的开放题。1997 年 EPS 论文确实证明了关于 h(n)=n+ω(n) 的局部重复值和集中现象；数据库还报告 Erdős 称 τ、ω 满足更一般断言、φ、σ“probably fails”，但本审计未能取得 Er97/Er97e 正文来核对其精确量词。未发现 2023–2026 年解决该“任意 F 的分类”版本的可检查证明。

### 当前规范陈述

数据库字面文字不是良定义命题，因为它写成“存在无穷多个 x 使 A(x)→∞”。最自然但必须经编辑确认的修复是：对算术函数 f:N→(0,∞)，定义 P(f)：对每个定义在允许区间位置 x 上的正辅助函数 F，若 F(n)/f(n) 在自然密度为零的例外集外趋于 0，则 limsup_{x→∞} #( {n∈N:n+f(n)∈(x,x+F(x))} )/F(x)=∞。还必须说明 x 为整数还是实数、x 为实数时 F(x) 如何定义，以及 F 是整数值还是一般正实值。

```text
Literal database wording is not a well-formed proposition because it says “there are infinitely many x such that A(x)→∞”. The most natural repair, which must be explicitly approved rather than silently assumed, is: for an arithmetic function f:N→(0,∞), say P(f) holds if for every positive auxiliary function F defined on the admissible locations x, satisfying F(n)/f(n)→0 outside a set of natural density zero, one has limsup_{x→∞} #( {n∈N : n+f(n)∈(x,x+F(x))} )/F(x)=∞. One must additionally specify whether x is integral or real, how F is evaluated when x is real, and whether F is integer-valued or merely positive real-valued.
```

### 陈述、量词与反例审计

- 歧义严重度: `fatal`
- 简单反例检查: `not_applicable`
- 检查说明: 由于字面陈述没有唯一的逻辑解析，不能诚实地给出“字面反例”。对任何修复版本，必须首先排除 F(x)≤0、F(x)<1（若 x、n 为整数）和 f(n)=0 等病态情形；这是一项定义审计，不是已验证的数学反例。
- 版本变化: Erdős Problems 的历史页显示，2025-10-20 的版本曾把关键比值误排为 f(n)/F(n)→0；2026-04-01 修正为 F(n)/f(n)→0，并把“τ、ω 已证、φ、σ 可能失败”的旧概括改为当前更谨慎的说明。当前页面仍保留同一未解析的“infinitely many x ... →∞”措辞。EPS97 的可读原文定义 h(n)=n+ω(n)，证明其局部重复值性质；它不是该数据库语句的逐字量词版本。

陈述问题：

- “there are infinitely many x such that A(x)→∞”把满足条件的点 x 与极限变量混为一体；它至少可能意指 limsup 为无穷、某序列 x_j→∞ 上发散，或其他量词结构。
- F 只写作 F(n)，但结论使用 F(x)；x 的定义域未说明。若 x 为实数，F 的定义域不匹配。
- F 的正性、整数性和下界未说明。若允许 0、负值或小于 1 的实值，分母和开区间计数会产生额外的平凡失败或无定义情形。
- “for almost all n”在数论中通常指自然密度 1，但此处没有明示例外集的密度定义和极限是在何集合上取。
- f 的允许类别没有定义；备注仅说 Er97 限于慢增长函数，未给出完整的函数空间、非负性或零点处理。
- “for which f”要求分类，且不等同于已知对 ω 的一个局部集中定理或对 τ、ω 的报道性结论。

需要固定的量词/约定：

- State f:N→(0,∞) and define the intended class of arithmetic functions, including the precise slow-growth restriction if it is part of the question.
- State F:N→[1,∞), with x∈N, or instead F:[1,∞)→(0,∞), with x∈R; do not mix these alternatives.
- Define “F(n)/f(n)→0 for almost all n” by an explicit density-one subset of N, or specify an alternative density notion.
- Replace the malformed conclusion by one exact alternative, preferably limsup_{x→∞} A_F,f(x)=∞, or explicitly quantify a sequence x_j→∞.
- Specify whether the count is over all n∈N or n≤x, and state interval-endpoint convention. The latter is harmless only after the domain/integrality conventions are fixed.

### 文献与当前边界

已核验的主要结果：

- EPS97（同行评审）直接研究 h(n)=n+ω(n)。其摘要和第 1 节说明：g(t)=#{m:m+ω(m)=t} 无界；Theorem 1 给出 g 的定量下界，Theorem 2 给出 h 的局部重复值上界，Theorem 3 构造长区间使 ω 连续严格递增。证明使用大模数等差数列上加性函数的 Turán–Kubilius 型不等式。
- 数据库从 EPS97 的构造概括出：对充分大尺度存在源区间 I 和像区间 J，|I|≈(log x/loglog x)^(1/2)、|J|≈(loglog x)^(1/2)，且 n∈I 蕴含 n+ω(n)∈J。EPS97 原文的证明段落确实构造许多 h(n+i) 落在短范围内；但这不是对数据库“每个 F”的量词陈述的逐字定理。
- 数据库称 Er97 和 Er97e 报告 f=τ、ω 的“more general claim”可证，并称 φ、σ 情形“probably fails”。由于 Er97/Er97e 正文未获读，此项只能作为有出处的二手报告，不能升格为已核实的完整定理或反例。

最近相关工作：Tao–Teräväinen 的 arXiv:2512.01739（v2，2026-04-25）是本审计检到的最近、确实涉及 ω、τ 与相邻整数相关性的工作；它解决的是 ω(n)=ω(n+1) 计数渐近问题，而非 n+f(n) 在任意短 F(x) 区间内的高重数问题。其存在不能改变本题状态，但提示近期的定量乘法函数相关性方法可能相邻。

剩余核心：首要未决问题是编辑性的：从 Er97/Er97e 取得原文，确定“无穷多个 x”和箭头的正式量词、F 的域与正性、almost all 的密度定义、以及 f 的许可类别。若确认自然修复为 limsup 版本，则剩余数学目标是给出慢增长算术函数的分类；已报道的 τ、ω 正例和对 φ、σ 的猜测不构成完整分类。

已使用方法：

- EPS97：在大模数等差数列上处理加性函数的 Turán–Kubilius 型不等式，并以局部构造制造 h(n)=n+ω(n) 的高纤维。
- Tao–Teräväinen（预印本）：概率方法、Maynard 型高维筛（用于另一问题）及具有对数节省的二点乘法函数相关性估计；它们尚未被证明适用于本题的任意 F 局部聚集目标。

争议或不确定性：

- 数据库状态为 open，但其自身历史显示关键比值曾在 2025 年写反；因此需谨慎对待未由原文支持的转述。
- 当前文字的极限变量歧义是致命的，而非仅排版瑕疵。
- 未找到近三年直接解决分类或给出 φ/σ 反例的论文；这是有限检索证据，不是不存在证明的逻辑证明。
- 论坛线程存在但未能打开，故没有采用其中任何潜在解答声称。

### 证据来源

- [Erdős Problems — LaTeX for Problem 122](https://www.erdosproblems.com/latex/122) — Thomas F. Bloom / Erdős Problems contributors, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 直接给出当前问题文字、慢增长备注、EPS97 的 ω 局部区间说明，以及 Er97/Er97e 的报道性总结；不能单独证明当前开放状态。
- [Erdős Problems — revision history for Problem 122](https://www.erdosproblems.com/history/122) — Thomas F. Bloom / Erdős Problems contributors, 2026-04-01; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 直接记录 2025-10-20 至 2026-04-01 的文字修订，尤其是 F/f 比值方向的更正和备注改写；也显示当前措辞未修复自由极限变量。
- [Erdős Problem #122 — discussion thread](https://www.erdosproblems.com/forum/thread/122?order=newest) — Erdős Problems forum users, date unknown; `forum`, `informal_claim`, directness=`indirect`, reliability=`low`. 搜索结果确认该线程存在并显示 3 条评论，但页面在本审计环境中缓存未命中，故未将任何论坛内容用作数学证据。
- [On Locally Repeated Values of Certain Arithmetic Functions, IV](https://math.dartmouth.edu/~carlp/PDF/paper112.pdf) — Paul Erdős, Carl Pomerance, András Sárközy, 1997; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 原文直接定义 g(t)=#{m:m+ω(m)=t} 和 h(n)=n+ω(n)，证明 g 在无界序列上有下界，并证明 h 的局部重复值结果；摘要明确称主要工具为大模数等差数列上加性函数的 Turán–Kubilius 型不等式。原文第 1 节的 Theorems 1–3 是数据库所述 ω 局部集中现象的可审计来源。
- [Paul Erdős, Problems in number theory, pp. 155–160](https://digitalnz.org/records/37328680) — Paul Erdős; University of Auckland Library record, 1997; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`medium`. 确认 Er97 的书目记录、页码和版权限制；本审计未取得正文，故不能用它直接确认 τ/ω 的全称 F 结论或 φ/σ 的精确措辞。
- [Mathematica Japonica, Volume 45 Issue 3 — contents](https://www.jams.jp/notice/mj/46-3.html) — Mathematica Japonica / Japan Association for Mathematical Sciences, 1997; `secondary_index`, `database_record`, directness=`indirect`, reliability=`medium`. 确认 Er97e 所在期刊期号列出《Some of my favourite unsolved problems》；网页字符编码使正文不可读取，不能作为其数学内容的直接证据。
- [Quantitative correlations and some problems on prime factors of consecutive integers](https://arxiv.org/abs/2512.01739) — Terence Tao, Joni Teräväinen, 2025-12-01; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 2026-04-25 修订的预印本证明几项相邻整数素因子数问题，包括几乎所有 x 上 ω(n)=ω(n+1) 的计数渐近式；这与 Problem 122 的 n+f(n) 局部纤维聚集不同，不能当作该题的解答。
- [On numbers not representable as n+ω(n)](https://www.mathnet.ru/php/archive.phtml?jrnid=mzm&option_lang=rus&paperid=13718&wshow=paper) — P. A. Kucheryavyi, 2023; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`medium`. 搜索结果显示该文研究 n+ω(n) 的表示问题，并引用旧的 Pomerance 结果；本环境未能打开正文，故不据此归纳其具体新定理或 Problem 122 状态。

### 完成标准

- 肯定出口: After a source-approved repair P(f), either prove a necessary-and-sufficient characterization of every f in the stated slow-growth class, or prove P(f) for a specifically named residual f with every admissible F and the exact limsup/sequence conclusion.
- 否定出口: For a source-approved repaired statement and a specified f, exhibit an admissible F and prove that the required limsup is finite (or that every permitted location sequence fails); for a classification, prove the stated f is outside the class or prove a complete exclusion criterion.

不构成完成：

- A local-concentration result for one hand-picked F only.
- A result for omega(n)=omega(n+1), or for repeated values of omega itself, without deriving the n+f(n) and universal-F conclusion.
- Repeating Erdős's reported phrase “probably fails” for phi or sigma without an admissible F and a proof of failure.
- Numerical clustering data without a theorem that preserves all quantifiers and density conditions.

正确性陷阱：

- Do not treat “there are infinitely many x such that A(x)→∞” as formal mathematics without choosing and defending a precise repair.
- Do not exchange density-one control of F(n)/f(n) with pointwise control at specially constructed interval locations.
- Do not infer a universal-F conclusion from an EPS97 interval construction unless the relationship between F(x), the target interval width, and every exceptional-set issue is proved.
- Check F(x)>0, its domain, and integer-versus-real x before dividing by F(x) or counting in (x,x+F(x)).
- Keep tau, omega, phi, and sigma separate: a report of a proof, a published theorem, and an authorial conjecture have different evidentiary status.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `0/100`
- 信心: `high`
- 结论: 当前字面记录没有可执行的数学完成标准，故不应派遣求解代理；评分为 0 表示在完成陈述修复前不存在可评估的“当前开放目标”，并不表示经修复后的某个版本必然不可做。

支持理由：

- EPS97 提供了可读的原始论文和明确的局部重复值技术起点。
- 近期 ω/τ 相关性工作显示相邻算术函数问题仍有活跃的现代方法。

主要障碍：

- 致命的量词/极限歧义阻止任何严格的成功判定。
- “for which f”是可能极宽的分类要求，而非单一命题。
- 关键的 τ/ω 全称 F 结果和 φ/σ 失败说法尚未由 Er97/Er97e 正文直接核验。

Proof-first 路线：

- 先取得并逐字转录 Er97 与 Er97e 的相关段落，建立经编辑批准的形式化目标。
- 只在目标固定后，检查 EPS97 的局部区间构造是否能对任意允许 F 保持量词和密度条件，而不能仅凭尺度比较推断。
- 可选计算至多一次：针对预先写定的有限引理，测试候选 f、F 是否出现局部纤维障碍；停止条件必须是该引理的有限证书或反例候选，不能是经验性“似乎聚集”。

需要验证：

- 取得 Er97 第 155–160 页及 Er97e 第 527–537 页的可读正文，记录页码和原句。
- 读取 Problem 122 论坛三条评论；对任何状态声称追溯至证明/预印本。
- 以修复后的精确符号再次检索 MathSciNet、zbMATH、arXiv、作者主页和引用链，特别查 2023–2026 文献。
- 若选择 limsup 修复，证明或否证 EPS97 结果到全称 F 的推导，而不是把数据库备注当作该推导。

### 审计限制与人工复核理由

- Er97 与 Er97e 的书目记录/目录已确认，但本审计环境未能获得两文相关正文；因此关于 τ、ω 的完整全称 F 结论及 φ、σ 的措辞仅能按数据库转述记录。
- Problem 122 论坛线程的存在已确认，但页面缓存未命中，未检视其三条评论。
- 近年检索覆盖精确短语、作者、n+ω(n) 和 arXiv 等途径；未找到直接解答不是不存在解答的逻辑证明。
- EPS97 可读原文验证了 ω 的局部重复值背景，但没有在本审计中验证它等价于任何未批准的 universal-F 修复版本。

- 需取得并核读 Er97 与 Er97e 原文，才能确定历史问题的精确量词和 Erdos 对 τ、ω、φ、σ 的实际陈述。
- 需要编辑者在 limsup、序列发散或其他解释之间批准一个规范目标；当前字面文字无法直接形式化。
- 取得论坛内容后，任何声称的解答或反例都须由独立原始证明核查。

<!-- DEEP_REVIEW:END -->
