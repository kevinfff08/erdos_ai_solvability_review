# Problem 36

## 基本信息

- 原始链接: https://www.erdosproblems.com/36
- LaTeX 页面: https://www.erdosproblems.com/latex/36
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `additive combinatorics`
- 形式化状态: `yes`
- OEIS: `A393584`, `possible`
- 原站备注字段: minimum overlap problem

## 原问题

Find the optimal constant $c>0$ such that the following holds.

For all sufficiently large $N$, if $A\sqcup B=\{1,\ldots,2N\}$ is a partition into two equal parts, so that $\lvert A\rvert=\lvert B\rvert=N$, then there is some $x$ such that the number of solutions to $a-b=x$ with $a\in A$ and $b\in B$ is at least $cN$.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `32/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：additive combinatorics, number theory
- 题面含渐近/无限对象线索：sufficiently large
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics, number theory
- 有限/计算线索: 无
- 渐近/无限线索: sufficiently large
- 构造/存在性线索: find

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **高候选：GPT-5.5 级别模型很可能显著推进该问题，尤其是在上界构造搜索、下界证明候选生成、形式化验证和数值到证明的闭环方面；但直接确定最优常数仍有明显不确定性。**
- 等级: `high_candidate`
- 分数: `82/100`
- 信心: `medium`
- 可能路线: 可行路线是把最小重叠问题转化为有限或极限形式的差集卷积优化：一方面用计算搜索、整数规划、局部搜索或进化式方法寻找更优分割模板，压低上界；另一方面从卷积、能量不等式、线性/半定规划对偶、稳定性分析等方向生成可验证的下界证书。由于题目已形式化，模型还可以辅助把候选不等式、有限归约和极限论证交给证明助手或独立程序验证。

### 支持理由

- 问题结构离散且目标函数明确，适合反例搜索、有限 N 实验、模板外推和优化证书生成。
- 给定备注显示已有 LLM 系统和 AlphaEvolve 类方法改善过上界，说明工具增强模型在该问题上不是纯猜测，而已有可行作用模式。
- 当前上下界 0.379005 与 0.380876 的差距较小，计算搜索和证明证书都有明确的反馈信号。
- 题目已 formalized，这降低了验证候选证明、检查边界条件和复现实验构造的成本。
- 该问题属于加性组合与数论交界，许多步骤可拆成可审计子任务：构造、极限化、对偶证书、误差界、形式化核查。

### 主要障碍

- 确定最优常数可能需要新的全局下界思想，而不仅是更强的局部搜索或数值拟合。
- 从有限 N 计算构造推广到所有充分大 N，需要严格的渐近模板和误差控制。
- 下界证明可能涉及高维对偶证书或复杂不等式，模型生成的证明草案容易隐藏未证的紧性或极限交换步骤。
- 上下界已很接近，进一步改进可能需要极高精度搜索和严格认证，容易出现数值伪改进。
- 即使找到更好的上界构造，也不等于完成问题；要找到最优 c 还需要匹配下界。

### 需要的验证

- 对任何新上界构造，需要独立程序复算差值重数，并验证可扩展到任意充分大 N。
- 对任何下界改进，需要给出可机检或至少可复现的证书，例如 LP/SDP 对偶证书、精确有理系数证书或形式化证明片段。
- 需要测试小到中等 N 的最优或近似最优分割，确认候选极限结构不是有限规模假象。
- 需要把数值常数转成带严格误差界的区间，而不是只报告浮点结果。
- 若声称解决最优常数，需要同时给出匹配上下界并形式化检查所有渐近和边界条件。

### 公开版思考摘要

该问题不是要求构造一个单一反例，而是寻找所有等分割中最大差值交叉重数的最小渐近常数。它有清晰的优化目标、已知较窄的上下界、形式化状态，并且备注中已经出现工具增强 LLM 改进上界的证据。因此 GPT-5.5 配合计算搜索和证明验证工具，很适合继续推进，尤其是产生更好构造或可验证的下界证书。不过，最终闭合约 0.0019 的间隙仍可能需要新的加性组合洞见，不能仅凭搜索能力保证完成。

### 免责声明

以上是对 AI 工具辅助可解性和推进潜力的审查，不是该 Erdős 问题的数学解答，也未声称给出最优常数。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `confirmed_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_36.md](../../prompts/problem_36.md)

### 状态结论

问题仍是开放的尖锐常数问题。原始网页在2026年1月仍标为 open，但其记录已过时：近期预印本报告了更好的两侧界。可直接审计的当前文献记录给出 0.37912 ≤ C ≤ 0.380856（上界为 SimpleTES 论文报告的消融运行结果）；下界来自 Kim–Pilanci 的严格有理数对偶证书预印本。两篇均未见同行评审，故最新数值界须复核其代码、构造和证书，但不影响“尚未求出精确常数、因此开放”的结论。

### 当前规范陈述

对 N≥1，定义 M(N)=min_{A⊔B={1,…,2N}, |A|=|B|=N} max_{x∈Z} r_{A,B}(x)，其中 r_{A,B}(x)=|{(a,b)∈A×B:a-b=x}|。最小重叠常数为 C=lim_{N→∞}M(N)/N（该极限的存在是已知结果）。原题中“对充分大的 N”应明确为：存在 N0，使得任意 N≥N0 及任意平衡分割 (A,B)，存在整数 x 满足 r_{A,B}(x)≥cN。“最优 c”应解释为所有满足该最终性质的 c 的上确界，即 C；题面本身并不保证端点 c=C 也满足该最终不等式。研究目标是精确确定 C，亦即对某个明确 α 同时严格证明 C≥α 与 C≤α。

```text
For N≥1, let M(N)=min_{A⊔B={1,...,2N}, |A|=|B|=N} max_{x∈Z} r_{A,B}(x), where r_{A,B}(x)=|{(a,b)∈A×B:a-b=x}|. The minimum-overlap constant is C=lim_{N→∞}M(N)/N (the existence of the limit is a known result). The literal eventual assertion for a real c is: ∃N0 ∀N≥N0 ∀ balanced partitions (A,B), ∃x∈Z with r_{A,B}(x)≥cN. Its optimal value must be read as the supremum of admissible c, namely C; the wording does not itself establish that the endpoint c=C satisfies the eventual inequality. The mathematical target is to determine C exactly, equivalently to prove matching rigorous lower and upper bounds C≥α and C≤α for an explicitly identified α.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 对字面量词作了检查，未发现会推翻命题的简单分割。连续中段分割 A={N/2+1,…,3N/2}（N 为偶数）只给出 C≤1/2，而非反例。
- 版本变化: Erdős最初猜测 C=1/2；后续工作持续收紧而未确定 C。Haugland（2016）给出约 0.38092685 的上界，White（2022）给出 0.379005 的下界；2026 年的搜索型工作依次报告更小上界，SimpleTES 论文报告 0.380856。Kim–Pilanci（2026-06）报告经精确有理数对偶证书验证的下界 0.37912。原数据库页未纳入这些后续更新。

陈述问题：

- “optimal constant such that the following holds”把上确界与端点是否实际满足“充分大 N”的性质混在一起；规范目标应为确定 C=lim M(N)/N，而不是未经证明地要求端点性质。
- 题面未定义 x 的域；由 a-b=x 可自然且必须取 x∈Z。
- 输入记录的 2026 年上界 0.380876 已被随后报告的构造改进；这属于文献更新，不是题面逻辑缺陷。

需要固定的量词/约定：

- N ranges over positive integers; “for all sufficiently large N” means ∃N0∈N such that ∀N≥N0.
- The partition quantifier is universal: ∀(A,B) with A⊔B=[2N] and |A|=|B|=N, followed by ∃x∈Z.
- r_{A,B}(x) counts ordered pairs (a,b)∈A×B. The maximum is finite because r_{A,B}(x)=0 outside [-(2N-1),2N-1].
- The exact constant is the supremum of eventual lower-bound constants. Equality at that supremum requires an additional argument and should not be silently assumed.

### 文献与当前边界

已核验的主要结果：

- 设 C=lim M(N)/N。Erdős的平均论证给出 C≥1/4；Scherk 提升至 1-1/√2；Moser/Świerczkowski/Haugland 等继续改进历史界。
- Haugland（Journal of Number Theory, 1996；以及2016预印本）使用连续密度函数/阶梯函数给出上界；2016 版本约为 C≤0.3809268534。
- White（2022预印本，后见 Acta Arithmetica 同名论文）以傅里叶分析和凸优化证明 C>0.379005。
- Yuksekgonul 等（2026预印本）报告可复现的阶梯函数搜索构造 C≤0.380876；其后 TogetherAI 报告0.380871，SimpleTES 报告0.380868及一项0.380856消融构造。
- Kim–Pilanci（2026-06预印本）以外松弛、附加 Toeplitz 半正定约束、分支定界和精确有理对偶可行证书报告 C≥0.37912。

最近相关工作：截至审计日，最新直接相关的下界工作是 Kim–Pilanci, arXiv:2606.31182（2026-06-30）；最新的上界报告来自 Ye 等, arXiv:2604.19341（2026-04-21），其作者页面说明其消融运行找到0.380856。两者均为未同行评审预印本，且本审计未逐项执行其证书或构造验证。

剩余核心：精确确定 C。以目前可检索的报告性记录，缺口至多约0.001736：0.37912≤C≤0.380856。任何仅优化离散样本、却未证明连续/渐近转移有效的数值结果，都不能关闭该缺口。

已使用方法：

- 组合平均与重排不等式。
- Swinnerton-Dyer 型离散—连续转移：用 [0,2] 上取值于[0,1]且积分为1的阶梯/密度函数产生渐近上界。
- 显式阶梯函数、线性规划及搜索型构造，用于上界。
- 傅里叶系数约束、凸优化外松弛、半正定 Toeplitz 约束、分支定界和精确有理对偶证书，用于下界。

争议或不确定性：

- 0.37912 下界是近期预印本的作者主张，虽其文中称有精确证书，但未见独立的同行评审或本审计中的逐项复核。
- 0.380856 是 SimpleTES 论文所述消融中找到的构造；维护常数索引仍列主结果0.380868。因此应在将其作为正式纪录前核验完整构造、归一化、卷积计算和离散—连续转移。
- 原问题页的0.380876记录已滞后，不能当作2026-07的完整文献综述。

### 证据来源

- [Erdős Problem 36](https://www.erdosproblems.com/36) — Thomas F. Bloom / Erdős Problems, 2026-01-23; `problem_page`, `database_record`, directness=`direct`, reliability=`medium`. 给出原始题面、旧记录 0.379005<c<0.380876、页面仍标为 open，并显示没有评论区的完整或部分解答主张；该页最后编辑于2026-01，故其数值记录不是当前上限。
- [Erdős' minimum overlap problem](https://arxiv.org/abs/2201.05704) — Ethan Patrick White, 2022-01-14; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 以初等傅里叶分析将问题转化为凸优化，建立显著改进的下界；其后正式发表页明确陈述 lim M(n)/n>0.379005。
- [A new bound for Erdős’ minimum overlap problem](https://www.impan.pl/en/publishing-house/journals-and-series/acta-arithmetica/online/115217/a-new-bound-for-erdos-minimum-overlap-problem) — Ethan Patrick White, 2023; `primary_paper`, `peer_reviewed`, directness=`direct`, reliability=`high`. 同行评审版本摘要明确给出 lim_{n→∞}M(n)/n>0.379005。
- [The minimum overlap problem revisited](https://arxiv.org/abs/1609.08000) — Jan Kristian Haugland, 2016-09-23; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 定义 M(n)，说明 Swinnerton-Dyer 的结果可将上界转为区间 [0,2] 上密度函数/阶梯函数的优化，并给出约0.380926的上界。
- [Learning to Discover at Test Time](https://arxiv.org/abs/2601.16175) — Mert Yuksekgonul, Daniel Koceja, Xinhao Li, Federico Bianchi, Jed McCaleb, Xiaolong Wang, Jan Kautz, Yejin Choi, James Zou, Carlos Guestrin, Yu Sun, 2026-02-05; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 报告并提供代码链接的 TTT-Discover 上界记录 0.380876；是输入记录采用的最新上界来源，但已被后来报告超越。
- [Evaluation-driven Scaling for Scientific Discovery](https://arxiv.org/abs/2604.19341) — Haotian Ye, Haowei Lin, Jingyi Tang, Yizhen Luo, Caiyin Yang, Chang Su, Rahul Thapa, Rui Yang, Ruihua Liu, Zeyu Li, Chong Gao, Dachao Ding, Guangrong He, Miaolei Zhang, Lina Sun, Wenyang Wang, Yuchen Zhong, Zhuohao Shen, Di He, Jianzhu Ma, Stefano Ermon, Tongyang Li, Xiaowen Chu, James Zou, Yuzhi Xu, 2026-04-21; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 论文摘要称发现了超越此前最优的最小重叠构造；作者项目页及论文检索结果报告 SimpleTES 的0.380868及消融中的0.380856构造。该构造尚未在本审计中逐项复算。
- [AI-Assisted Discovery of Convex Relaxations via Dual Agents](https://arxiv.org/abs/2606.31182) — Sungyoon Kim, Mert Pilanci, 2026-06-30; `preprint`, `preprint`, directness=`direct`, reliability=`medium`. 报告把最小重叠常数的认证下界从0.379005提升至0.37912，并称最终界由精确有理算术检查的显式对偶可行点认证。
- [Erdős minimum overlap constant](https://teorth.github.io/optimizationproblems/constants/1b.html) — Damek Davis, Paata Ivanisvili, Terence Tao, and contributors, 2026; `secondary_index`, `database_record`, directness=`indirect`, reliability=`high`. 维护者列出历史上界至 TTT-Discover、TogetherAI 与 SimpleTES 0.380868；用于交叉核验近期上界演变，不替代构造证明。
- [FormalConjectures.ErdosProblems.«36»](https://firsching.ch/formal-conjectures/src/FormalConjectures/ErdosProblems/%C2%AB36%C2%BB/) — Formal Conjectures authors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`medium`. 形式化了 M(N)、重叠计数和若干历史变体的陈述，但关键定理仍含 sorry；它不是对精确常数或最新界的已核验形式证明。
- [EinsteinArena thread 243](https://einsteinarena.com/problems/erdos-min-overlap/threads/243) — EinsteinArena community, 2026; `forum`, `informal_claim`, directness=`indirect`, reliability=`medium`. 论坛明确把 Kim–Pilanci 的0.37912称为尚未由该平台独立验证的预印本主张；用于记录独立复核尚缺。

### 完成标准

- 肯定出口: Produce an explicit real number α and a complete proof that C=α: (i) for every ε>0, all sufficiently large balanced partitions have max_x r_{A,B}(x)≥(α-ε)N (or an equivalent rigorous lower-bound/limit argument), and (ii) give balanced partitions for arbitrarily large N, or a valid continuous construction with a proved transference theorem, giving M(N)/N≤α+o(1).
- 否定出口: For any claimed exact value α, a decisive rejection is a rigorous proof of C<α or C>α; for a claimed bound, a decisive rejection is a verified partition/function violating the asserted universal lower bound or a proof that the asserted upper construction/transference estimate is invalid.

不构成完成：

- A finite search over N, even with many exact values of M(N), without a theorem controlling the N→∞ limit.
- A numerically optimized sampled function without an exact interval/analytic bound on the true overlap integral and without verified normalization and range constraints.
- An improved upper construction alone, or an improved lower relaxation alone, when no matching bound identifies C.
- A floating-point dual solution unless it is converted into a valid exact or rigorously interval-certified dual feasible point for a proved outer relaxation.

正确性陷阱：

- Keep the orientation and normalization straight: r_{A,B}(x) is cross-difference overlap, not an autocorrelation of A alone.
- Check whether max_x ranges over all integers and whether zero-padded extensions are used in the continuous convolution formulation.
- Do not infer endpoint attainment of the original ‘eventually ≥cN’ statement merely from convergence to C.
- For upper bounds, prove the discrete-to-continuous/step-function transference and account for boundary and o(N) errors.
- For lower bounds, every relaxation constraint must be necessary for every admissible function; a restrictive but unproved constraint invalidates the bound.
- Separate machine-discovered candidates from a complete certificate that can be independently replayed.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `22/100`
- 信心: `medium`
- 结论: 这是定义清楚、可验证但高度尖锐的开放常数问题；AI 可有价值地生成并核验局部引理或严格证书，却不应把可优化的连续评分器误认为精确求解路线。

支持理由：

- 目标可规范为单一极限常数，且上下界验证具有清晰的数学证书形式。
- 近期已有多种不同方法和极窄数值缺口，提供了可比较的中间目标。
- 下界的凸松弛/对偶证书、上界的显式函数构造，原则上可被独立检查。

主要障碍：

- 精确值没有可信的结构性猜想或匹配两侧机制；0.0017 左右的数值缺口未自动转化为有限问题。
- 上界搜索容易受离散化、浮点误差和错误的连续—离散转移误导。
- 下界改进要求对所有可容许函数成立；外松弛中任一未经证明的约束都足以使“证明”失效。

Proof-first 路线：

- 先独立复核 Kim–Pilanci 的每个新增必要约束和精确对偶证书；若成立，寻找可普遍化的分析不等式，而非只增加网格精度。
- 对任何新上界候选，先给出有限阶梯函数的精确分段积分证书及转移引理，再讨论搜索。
- 研究极小化函数的对称化、紧性或欧拉—拉格朗日/对偶互补条件，力求把数值候选转为可证明的结构定理。

需要验证：

- 下载并重跑/审计 0.37912 的有理数对偶证书、分支盒覆盖和每个Toeplitz约束的必要性证明。
- 取得并精确验证 SimpleTES 0.380856 构造的完整数据、[0,1]范围、积分归一化、所有位移上的最大重叠及渐近转移。
- 确认后续版本、期刊论文或正式勘误是否已更新这些2026预印本结果。

### 审计限制与人工复核理由

- 直接打开 Erdős Problems 的网页与 LaTeX 页时遭遇403；已通过搜索索引读取其当前可见内容，故页面的状态和评论记录仅为数据库证据。
- 未在本审计中下载、执行或逐行验证 Kim–Pilanci 的有理数对偶证书，也未获得并复算 Ye 等报告的0.380856阶梯函数；最新界应视为强的未同行评审主张。
- 没有发现该问题页所链接的独立论坛解答；检索到的 EinsteinArena 讨论明确保留了对最新下界的独立核验意见。
- “0.380856”来自论文/作者报告的消融运行，而维护索引列主结果0.380868；最终数据库更新前应要求作者提供固定、可复现的构造和验证脚本。

- 应由数学审稿人复核2026年预印本下界的外松弛有效性、精确对偶证书与分支覆盖。
- 应由独立脚本复算所有近期上界候选，尤其是0.380856消融构造，并验证其离散—连续转移。
- 数据库页的旧数值记录与2026年后续预印本不一致，维护者需要决定哪些可作为正式“当前纪录”写入。

<!-- DEEP_REVIEW:END -->
