# Problem 9

## 基本信息

- 原始链接: https://www.erdosproblems.com/9
- LaTeX 页面: https://www.erdosproblems.com/latex/9
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive basis`, `primes`
- 形式化状态: `yes`
- OEIS: `A006286`
- 原站备注字段: 无

## 原问题

Let $A$ be the set of all odd integers $\geq 1$ not of the form $p+2^{k}+2^l$ (where $k,l\geq 0$ and $p$ is prime). Is the upper density of $A$ positive?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `31/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory, primes
- 题面含渐近/无限对象线索：\gg, density, infinitely many, prime, primes

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: additive basis
- 证明密集标签命中: number theory, primes
- 有限/计算线索: covering system, finite, finitely
- 渐近/无限线索: \gg, density, infinitely many, prime, primes
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **有可能做出有价值的计算与证明验证推进，但直接完成正上密度证明的概率偏低；更现实的目标是复现并形式化已有下界、扩大反例搜索、检验模结构与筛法路线是否能产生可升级的正密度候选证明。**
- 等级: `low_to_medium_candidate`
- 分数: `35/100`
- 信心: `medium`
- 可能路线: 可行路线是把问题拆成三层：先用程序高效生成到大范围的不可表示奇数并估计局部密度；再系统搜索模数、剩余类和覆盖型/非覆盖型构造，寻找能给出正比例遗漏的结构；最后把候选结构转化为关于素数避开若干剩余类、二进制幂和集的筛法或调和分析命题，并用形式化证明工具验证所有有限组合部分。

### 支持理由

- 问题表述短且形式化状态为 yes，适合机器检查有限范围、模运算断言和候选引理。
- 已有结果从无限多个反例推进到对任意 epsilon 有 N^{1-epsilon} 级别下界，说明问题不是纯构造缺口，存在可继续分析的结构。
- 表示式 p+2^k+2^l 具有可计算性强的稀疏加法结构，模型配合计算能系统搜索异常数列、模周期现象和潜在筛法证据。
- OEIS 序列存在，有利于交叉检查计算数据和发现早期项规律。
- Erdős 关于覆盖系统路线的备注提示了明确的负面约束，能帮助模型避免只依赖简单算术级数覆盖。

### 主要障碍

- 要证明上密度为正，需要从 N^{1-epsilon} 级别跃迁到 cN 级别，这通常要求新的全局结构或强筛法，而不是更大规模计算。
- 素数项会破坏单纯模覆盖思路；若每个无限等差数列都含有可表示数，则正密度证明必须更精细地控制许多模条件的联合效应。
- 二的幂在模奇数时呈周期行为，但两个幂之和的剩余类集合可能很快变大，难以产生稳定的正比例排除。
- 计算实验只能给出有限区间证据，若没有可推广的模数族或解析估计，很难排除后续密度衰减到 0。
- 相关证明可能需要深层解析数论输入，例如素数在大量剩余类中的分布、筛法误差控制或指数和估计，这些仍是 GPT-5.5 级模型的高风险区域。

### 需要的验证

- 独立实现表示数判定，并与 A006286 的初始项核对，避免把计算伪影当作结构。
- 在多个增长区间估计 A 的计数函数，检查是否支持正密度、缓慢衰减或 N^{1-o(1)} 型行为。
- 对任何候选模构造，必须形式化验证所有剩余类计算和周期声明。
- 若提出解析证明，需要逐条验证所用素数分布、筛法和误差项是否在所需参数范围内成立。
- 需要文献检索确认 Crocker、Pan 以及备注中提到的相关结果的精确强度，防止重复已有结论或误用定理。

### 公开版思考摘要

这个问题对 AI 工具友好的一面是表示式简单、可计算、可形式化，且已有接近稠密的下界可作为技术起点。困难在于目标是正上密度，远强于已知 N^{1-epsilon} 下界；朴素覆盖系统路线又被问题备注指出大概率不足。因此 GPT-5.5 更可能提供系统计算、候选结构发现、局部证明验证和已有路线整合，而不是独立给出完整解决方案。

### 免责声明

以上是对 GPT-5.5 级别模型辅助研究可行性的审查，不是该 Erdős 问题的解答或证明。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_9.md](../../prompts/problem_9.md)

### 状态结论

该精确定义的密度问题仍为公开问题。Erdős Problems 当前记录仍标为 OPEN，且 2026 年 7 月 Ding、Sun、Zhao 的预印本明确把“是否存在 c0>0 使 N(x)>c0 x”作为尚未解决的动机问题，并仅改进了已知下界，未证明正上密度。未发现可检验的解答或反例。

### 当前规范陈述

令 P 为正素数集合，令 A={n∈N：n 为奇数，且不存在 p∈P、k,l∈Z_{e0} 使 n=p+2^k+2^l}。记 A(X)=|A∩[1,X]|。问题是是否 \bar d(A):=limsup_{X→∞}A(X)/X>0；等价地，是否存在 c>0 及无界序列 X_j，使 A(X_j)≥cX_j。若把密度改为相对于奇整数计，数值仅相差因子 2，故是同一是/否问题。

```text
Let P be the set of positive primes and let A={n in N: n is odd and there do not exist p in P and k,l in Z_{e0} with n=p+2^k+2^l}. Put A(X)=|A cap [1,X]|. Determine whether the upper asymptotic density \bar d(A):=limsup_{X->infinity} A(X)/X is positive; equivalently, whether there are c>0 and an unbounded sequence X_j such that A(X_j)>=cX_j. Using density relative only to odd integers changes this quantity by a factor of two and hence gives the same yes/no question.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定该密度命题的简单构造。小数值、覆盖同余类或有限计算都不能决定 limsup 密度；已知覆盖系统只给出稀疏的例外数构造，不能推出正密度。
- 版本变化: Crocker（1971）历史上先证明正指数版本存在无穷多个例外。后续文献说明可把相关构造延至非负指数；Pan（2011）直接以 a,b≥0 的表示式工作。当前题目不是被替换的旧命题，而是这一精确定义下仍未解决的正上密度问题。

陈述问题：

- 原文未说明“upper density”的分母是所有正整数还是仅奇整数；两种约定的正性等价，因此不改变问题真值。
- “prime”须按通常约定解释为正素数；k,l≥0 已排除了指数约定的实质歧义。
- 早期 Crocker 论文的定理陈述使用正指数；这不能单独覆盖当前 k,l≥0 的版本。Pan 2011 的证明中明确处理 a,b≥0，故该历史差异不会使当前题目失定义。
- 数据库写有“formalized: yes”，但本次未找到可直接审计的正式化工件；不能将该标签视为已形式化了密度结论。

需要固定的量词/约定：

- The question is existential: prove or refute the existence of a fixed c>0 witnessing positive limsup density; c must not depend on X.
- The representation quantifiers are existential for each n, while membership in A requires failure for every p,k,l with p prime and k,l>=0.
- The two exponents may be equal and their order is irrelevant.
- A lower bound along a subsequence suffices for positive upper density; an eventual lower bound is stronger but also sufficient.

### 文献与当前边界

已核验的主要结果：

- Crocker（1971，同行评审）证明有无穷多个正奇整数不能表示为素数加两个正的 2 的幂；后来的文献将其工作概括为 N(x)≫loglog x 级别的下界。
- Chen、Feng、Templier（2008，同行评审）研究更一般的素数幂加两个幂问题，并给出与费马数有关的条件性结论；这些不等同于本题的无条件正密度结论。
- Pan（2011，同行评审）以 Selberg 筛和同余覆盖技术证明 N(x)≫x exp(-C log x·loglogloglog x/logloglog x)，特别地 N(x)≫_ε x^(1-ε)（任意 ε>0）。
- Ding、Sun、Zhao（2026-07-06，预印本）将 Pan 的指数损失改进为：任意 η>0 时 N(x)≫_η x exp(-(4+η)(logloglog x/loglog x)log x)。该下界仍为 x 的 x^{-o(1)} 倍，不能给出固定正比例。

最近相关工作：Ding、Sun、Zhao 的 arXiv:2607.05357（2026-07-06，9 页预印本）是本次检索到的最新且直接的进展。它审计了同一个 N(x)，给出更强的近线性下界，但没有声称或证明 N(x)≫x。由于预印本发布仅约三周，需在后续研究前复核其版本、同行评审状态和全部证明。

剩余核心：证明或否证存在绝对常数 c>0，使例外奇整数的计数函数 N(x) 在无界尺度上满足 N(x)≥cx；等价地判定 \bar d(A)>0。现有 x^{1-o(1)} 型下界与该结论之间仍有本质鸿沟。

已使用方法：

- 覆盖同余与中国剩余定理：为指数差分类制造强制合数的候选素数。
- Brun–Titchmarsh、Selberg 筛等筛法：控制某一同余类中仍可能为素数的剩余表示。
- 费马数/广义费马数及 2 的模素数阶的因子性质：构造适合的模数和覆盖。
- 最新预印本中的部分覆盖、概率法选取剩余类和筛估计。

争议或不确定性：

- 未发现可信的完整解答或反例声明；但“未找到”并非对全世界文献穷尽性的证明。
- Erdős Problems 的 formalized 标记未附本次可访问的正式化链接或工件；正式化范围不明。
- Ding、Sun、Zhao 的结果为新预印本，尚未在本次审计中逐行复核证明或确认同行评审状态。

### 证据来源

- [Erdős Problem #9](https://www.erdosproblems.com/9) — Thomas F. Bloom / Erdős Problems contributors, date unknown; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 当前数据库记录将该题标为 OPEN，显示一个论坛评论且无解答或部分解答声明，并标注其不能由有限计算解决。
- [On the sum of a prime and of two powers of two](https://msp.org/pjm/1971/36-1/pjm-v36-n1-p09-p.pdf) — Roger C. Crocker, 1971-11; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 证明存在无穷多个不能写成“素数加两个正的 2 的幂”的正奇整数；这是例外集合非空且无穷的历史基础，但原始定理的指数为正。
- [On the integers not of the form p+2^a+2^b](https://www.impan.pl/shop/publication/transaction/download/product/83300) — Hao Pan, 2011; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 定义当前型例外集合，明确将 Erdős 问题表为是否 |N∩[1,x]|≫x；证明 |N∩[1,x]|≫x exp(-C log x·loglogloglog x/logloglog x)，从而得到对任意 ε>0 的 ≫_ε x^(1-ε) 下界。证明中使用 a,b≥0。
- [Fermat numbers and integers of the form a^k+a^l+p^α](https://doi.org/10.4064/aa135-1-4) — Yong-Gao Chen, Rui Feng, Nicolas Templier, 2008; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 提供与费马数及“素数幂加两个幂”有关的条件性结果；不能直接解决本题的素数版本，但解释了该方向与费马数性质的联系，并说明早期正指数构造可延至非负指数。
- [An improved lower bound for odd integers not of the form p+2^a+2^b](https://arxiv.org/abs/2607.05357) — Yuchen Ding, Yu-Chen Sun, Lilu Zhao, 2026-07-06; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 最新直接相关工作。其摘要将问题表为是否 N(x)>c0x，并证明对任意 η>0，N(x)≫_η x exp(-(4+η)(logloglog x/loglog x)log x)；这是强于 Pan 的下界但仍不足以推出正上密度。
- [A006286: Numbers not of form p + 2^x + 2^y](https://oeis.org/A006286) — OEIS Foundation and contributors, date unknown; `oeis`, `database_record`, directness=`indirect`, reliability=`medium`. 核对了序列对象、前若干项及其与 Crocker、Pan 和 Erdős Problems 的链接；它不是关于密度的证明来源。

### 完成标准

- 肯定出口: Prove that there exists c>0 such that limsup_{X->infinity} A(X)/X >= c; equivalently, exhibit c>0 and arbitrarily large X with A(X)>=cX, with every excluded representation checked for all primes p and k,l>=0.
- 否定出口: Prove limsup_{X->infinity} A(X)/X=0, equivalently A(X)=o(X), by showing that for every epsilon>0 all sufficiently large X satisfy A(X)<=epsilon X.

不构成完成：

- Proving only that A is infinite, or only A(X)>>(log log X), X^(1-epsilon), or X^(1-o(1)).
- A positive lower bound for a different set, such as exponents k,l>0, prime powers in place of primes, or a fixed coefficient multiplying one power.
- A conditional proof without explicitly identifying and retaining the hypothesis.
- Finite verification, numerical density plots, or a long finite progression without an asymptotic argument.
- Proving a positive density for representable integers; that does not imply a positive density for the complement.

正确性陷阱：

- Keep the p=2 case and the k=0 or l=0 cases; parity shortcuts can silently discard them.
- Do not replace upper density by lower density, natural density, logarithmic density, or density relative to an arithmetic progression without proving the needed implication.
- A covering construction must rule out the possibility that the forced divisor equals the candidate prime itself; exceptional equality cases require separate control.
- Bounds whose constants or moduli vary with X must be checked carefully: they do not automatically yield one fixed positive density constant.
- When importing results about prime powers, verify that the deduction returns to p prime rather than p^alpha.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `8/100`
- 信心: `high`
- 结论: 目标清晰且可严格核查，但它是长期未解的解析加法数论密度问题；以当前记录看，AI 独立完成解决的机会很低。

支持理由：

- 命题具有精确的二值完成条件，且已有可直接比较的定量下界。
- 已有文献公开了具体的覆盖和筛法结构，局部引理可以逐项审计。
- 最新进展表明该方向仍活跃，可能存在可识别的技术瓶颈。

主要障碍：

- 从 x^{1-o(1)} 到固定正比例不是常数优化，而是质变的密度缺口。
- 现有方法依赖精细的覆盖、素因子分布和筛上界；简单扩展很容易因模数增长而损失全部密度。
- 费马数相关条件性路径涉及深且未解决的素数性/因子问题。

Proof-first 路线：

- 先精确重建 Pan 与 Ding–Sun–Zhao 中损失密度的单一位置，尝试证明一个固定密度的覆盖/剩余控制引理；只有该引理有明确停止条件时才计算。
- 尝试反向路线：证明任何可用覆盖机制的密度必趋于零，并明确说明这只能排除一类方法、不能否定原命题。
- 审计能否将最新的部分覆盖随机化升级为常数比例覆盖，同时独立验证候选素数等于模素数的例外处理。

需要验证：

- 逐页复核 arXiv:2607.05357 的定理假设、常数依赖和与 Pan 下界的严格比较。
- 定位或向 Erdős Problems 维护者索取“formalized: yes”所指工件，并核对其精确陈述。
- 在任何声称改进前，逐项核验 k,l=0、k=l、p=2 与所有有限异常。

### 审计限制与人工复核理由

- Erdős Problems 主页面及 LaTeX 页面在本次工具中出现 403/抓取错误；其状态、论坛计数和无解答声明通过该站点的可检索缓存记录交叉取得。
- 本次检索覆盖了精确题述、主要作者、最新 arXiv 和相关费马数文献，但无法逻辑上穷尽所有未索引论文、私人手稿或未来更新。
- 最新 Ding–Sun–Zhao 预印本已读摘要和可访问的 HTML/文本片段，但未进行逐行的完整证明复核。
- “formalized: yes”的具体正式化工件未能定位，因此不对其内容、系统或可信核作任何结论。

- 应由数论专家逐页检查 2026 新预印本的定理、常数和是否存在后续勘误或正式发表；这对“最强已知结果”判断重要。
- 应联系数据库维护者或查找提交历史，以定位 formalized 标签对应的工件并确定其只形式化陈述还是形式化实质结果。
- 任何将新下界解释为正密度、或忽略 k,l=0 与候选素数等于模素数的论证，均需人工严格审稿。

<!-- DEEP_REVIEW:END -->
