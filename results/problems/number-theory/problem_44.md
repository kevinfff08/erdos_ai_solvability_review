# Problem 44

## 基本信息

- 原始链接: https://www.erdosproblems.com/44
- LaTeX 页面: https://www.erdosproblems.com/latex/44
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `sidon sets`, `additive combinatorics`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $N\geq 1$ and $A\subset \{1,\ldots,N\}$ be a Sidon set. Is it true that, for any $\epsilon>0$, there exist $M$ and $B\subset \{N+1,\ldots,M\}$ (which may depend on $N,A,\epsilon$) such that $A\cup B\subset \{1,\ldots,M\}$ is a Sidon set of size at least $(1-\epsilon)M^{1/2}$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `26/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：additive combinatorics, number theory, sidon sets
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: additive combinatorics, number theory, sidon sets
- 有限/计算线索: 无
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。GPT-5.5 配合计算搜索、形式化验证和定向文献检索，较可能产出有价值的结构化推进、候选构造或排除若干自然反例路线；但直接给出完整正解的概率偏低，因为目标要求在保留任意有限 Sidon 前缀的同时达到几乎最优的平方根规模。**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 信心: `medium`
- 可能路线: 把给定有限前缀 A 视为固定约束，将扩展 B 的条件拆成内部 Sidon 约束、A 与 B 的混合和冲突约束、以及渐近密度约束；用 SAT/ILP/随机搜索检验小规模实例与反例模式，再尝试把成功模式抽象成带有限禁忌配置的近最优 Sidon 构造，并用形式化证明检查关键归约和边界条件。

### 支持理由

- 问题已经形式化，适合把 Sidon 条件和混合和冲突条件转成可机检的谓词与有限验证任务。
- A 是固定有限集合，许多额外约束可被整理为有限前缀诱导的禁忌关系，这给计算实验和构造性归约留下空间。
- 目标是存在某个足够大的 M 和 B，而不是要求对所有 M 构造，因此可以利用放大、稀疏化或选择性构造的自由度。
- 工具增强模型可以系统枚举小 N、小 A 的极端情形，寻找混合碰撞的最小障碍，并验证候选证明中的局部组合命题。

### 主要障碍

- 要求大小至少为 (1-epsilon) M^{1/2}，常数几乎最优，任何删除线性于 M^{1/2} 的坏点都会破坏结论。
- 任意给定 A 会引入混合和碰撞，例如 A+B 与 B+B、A+B 内部不同表示之间的冲突；这些不是单纯保持 B 自身为 Sidon 就能解决。
- 小规模计算很容易被有限效应误导，无法直接证明任意 epsilon 与任意固定前缀下的渐近存在性。
- 完整证明可能需要新的代数或概率构造，并且误差项必须对固定的 N、A、epsilon 有清晰依赖。
- 形式化证明可以降低错误率，但不能替代核心组合构造；若候选证明依赖复杂渐近估计，形式化成本会较高。

### 需要的验证

- 对所有 Sidon 条件进行机检拆分，尤其验证 A+A、A+B、B+B 三类和之间没有重复表示。
- 对小规模 N 和所有 Sidon 前缀 A 做穷举或约束求解，检查是否存在异常障碍模式。
- 若提出构造，需要证明删除或修补的元素数为 o(M^{1/2})，不能只是 O(M^{1/2})。
- 需要形式化或半形式化验证关键归约：固定前缀诱导的禁忌配置是否真的覆盖所有混合冲突。
- 需要独立审查渐近量词顺序：给定 N、A、epsilon 后选择 M、B，而不是反向依赖。

### 公开版思考摘要

这个题的可攻性来自前缀 A 是有限固定对象，模型和工具可以把它转化为一组显式禁忌配置并做大量计算验证；难点在于结论要求近乎最优的平方根规模，几乎没有空间用粗暴删除法处理混合冲突。因此 GPT-5.5 更现实的贡献是发现并验证候选构造、证明局部引理、排除自然反例和完善形式化框架；完整解决需要相当强的新组合构造，成功概率不高但不应视为零。

### 免责声明

以上是对 AI 辅助可推进性的审查，不是该 Erdős 问题的解答，也不声称给出了正例构造或反例。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-07-27`
- 核验模型: `gpt-5.6-terra`
- 当前状态: `likely_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [prompts/problem_44.md](../../prompts/problem_44.md)

### 状态结论

截至 2026-07-27，题目 #44 的精确“任意有限 Sidon 初始段可扩充为渐近最优有限 Sidon 集”命题仍很可能开放。ErdosProblems 页面于 2026-01-09 仍标为 OPEN；针对精确陈述、题号、Sidon-extension/PDS 术语、近三年 arXiv 与形式化仓库的检索未发现该命题的证明或反例。2025 年 Alexeev–Mixon 对更强的 #707（扩充为有限完美差集）给出了反例；这只切断了 #707 ⇒ #44 的历史蕴含，既不证明也不反驳 #44。

### 当前规范陈述

定义：有限整数集 S 为 Sidon 集，若任意 a,b,c,d∈S 满足 a+b=c+d 时，二重集 {a,b} 与 {c,d} 相同；等价地，每个正差至多由一对 S 中不同元素实现。规范目标为：对每个整数 N≥1、每个 Sidon 集 A⊆{1,…,N} 及每个实数 ε>0，存在整数 M>N 和 B⊆{N+1,…,M}，使 A∪B 为 Sidon 集且 |A∪B|≥(1−ε)√M。ε≥1 时不等式平凡；实质情形为 0<ε<1。M、B 可依赖于 N、A、ε。

```text
A finite set S of integers is Sidon if for all a,b,c,d in S, a+b=c+d implies {a,b}={c,d} as multisets (equivalently, every positive difference of two distinct elements of S has at most one ordered realization). The target is: for every integer N>=1, every Sidon set A⊆{1,...,N}, and every real ε>0, there exist an integer M>N and B⊆{N+1,...,M} such that A∪B is Sidon and |A∪B|≥(1−ε)√M. The cases ε≥1 are vacuous; the substantive demand is 0<ε<1. M and B may depend on N, A, and ε. The inclusion A∪B⊆{1,...,M} follows from the displayed range conditions and need not be an extra hypothesis.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现能否定上述精确命题的简单构造。Hall 及 Alexeev–Mixon 的集合只能阻止扩充到有限完美差集（PDS），而 PDS 要求所有非零模差恰好出现一次，远强于本题只要求在某个区间内达到 (1−ε)√M 的 Sidon 超集；不能把这些 PDS 反例当作 #44 的反例。
- 版本变化: 历史备注称 #707 的肯定解蕴含 #44，#44 又蕴含 #329。Alexeev–Mixon（2025 预印本，含 Lean 核验的相关核心）及 Hall 的早期工作否定了 #707 的有限 PDS 扩充猜想，因此该蕴含链的最强端已失效；#44 本身并未被该结果修订、解决或反驳。2026 年 Tong Niu 的 size-4 PDS-extension 预印本也明确仍只是有限范围计算与条件性/经验性证据，不能改变 #44 状态。

陈述问题：

- 输入未明说 M 的取值域及 M>N；按有限区间 Sidon 问题的标准约定，M 应为整数且必须取 M>N。否则 {N+1,…,M} 在 M≤N 时为空，不能表达“向右扩充”的意图。
- “A∪B⊆{1,…,M}”由 A⊆{1,…,N}、B⊆{N+1,…,M} 与 M>N 自动推出，故并非独立限制。
- “for any ε>0”包含 ε≥1 的平凡情形；这不改变真值，但研究与验证应只处理 0<ε<1。
- 形式化仓库中的 44.lean 提供了带 M>N 的开放命题陈述，但仍含 sorry；它不是证明，也不应单独作为陈述完全正确的保证。

需要固定的量词/约定：

- Quantify N over positive integers, A over all finite subsets of [1,N], and ε over positive real numbers.
- Quantify M over integers with M>N; B may depend on all of N, A, ε.
- The assertion is existential in M for each fixed triple (N,A,ε), not a uniform bound M(ε) independent of N and A.
- The size threshold is weak: |A∪B|≥(1−ε)√M. A negative certificate must therefore exclude every M>N and every admissible B for one fixed N,A,ε.

### 文献与当前边界

已核验的主要结果：

- 经典有限构造表明无预先指定前缀时，区间 [1,M] 中可有规模 (1−o(1))√M 的 Sidon 集；但这不能保证包含任意给定 A。
- Alexeev–Mixon 的 2025 结果（并追溯 Hall 1947）否定了“每个有限 Sidon 集扩充为有限 PDS”的更强 #707。该结果只说明原先的充分路线失败，不构成本题的负例。
- Cilleruelo–Nathanson 的无限 PDS 构造及 Alexeev–Mixon 文中引用的 Hall 贪心扩充表明：有限 Sidon 前缀可嵌入某个无限 PDS；但该无限超集不提供题目所需的任意 ε 下、某有限截断处接近 1 的 √M 常数。
- Eberhard–Manners（2023）将已知高密度有限群 Sidon 集与射影平面联系起来，并提出结构猜想而非定理；这提供了可能的结构障碍背景，但尚未给出任意前缀延拓结论。

最近相关工作：直接相关的最新状态信息仍是 ErdosProblems 于 2026-01-09 的 OPEN 记录。2026 年 Niu 的 PDS-extension 预印本与 O'Bryant 的无限 Sidon 厚度预印本都相关但不处理本题精确量词；检索未找到 2023–2026 年针对 #44 的证明或反例。

剩余核心：是否每个有限 Sidon 集 A 都可在其右侧补点，并在某个足够远的有限终点 M 达到任意接近最优的比例 |A∪B|/√M≥1−ε。关键困难是既要保存 A 的全部已占差，又要把新增点之间及新增点与 A 的差控制为唯一，同时避免在密度常数上损失固定比例。

已使用方法：

- 有限域/循环群中的 Singer、Bose–Chowla 与完美差集构造。
- 贪心及稀疏补点构造；它们通常保证无穷延拓或较低密度，而非固定前缀后的近最优有限端点。
- 高密度 Sidon 集的傅里叶均匀性、射影平面/极性与结构研究。
- 将 PDS extension 视为更强路线；其已知反例表明不能把该路线当作普遍证明。

争议或不确定性：

- OPEN 标签是维护者信念而非文献完备性的逻辑证明，但本次检索没有发现相反的可核验声明。
- #44 的 Lean 文件有 sorry，且其具体编码应由 Lean 审核者复核；它不能被解释为完全形式化证明。
- Niu（2026）关于 size-4 PDS-extension 的“apparent”无限族与部分条件性结论不得升级为已证事实。

### 证据来源

- [Erdős Problem #44: Extending Sidon sets to near optimal](https://www.erdosproblems.com/44) — Thomas F. Bloom / ErdosProblems.com, 2026-01-09; `problem_page`, `database_record`, directness=`direct`, reliability=`high`. 给出本题文字、OPEN 标签、#707⇒#44⇒#329 的关系，并明确提示其开放标签仅反映站点维护者的当前信念，须另行检索。
- [FormalConjectures: Erdős Problem 44](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/44.lean) — Formal Conjectures Authors, 2025; `formalization`, `formalized_artifact`, directness=`direct`, reliability=`high`. 给出 Lean 中带 M>N 的 #44 命题形式；主定理以 sorry 留空，故只支持“已形式化陈述”，不支持真值或解答。
- [Forbidden Sidon subsets of perfect difference sets, featuring a human-assisted proof](https://arxiv.org/abs/2510.19804) — Boris Alexeev and Dustin G. Mixon, 2025-10-23; `preprint`, `preprint`, directness=`direct`, reliability=`high`. 证明 {1,2,4,8,13} 不能扩充为任何有限 PDS，并说明 #44 是介于 PDS-extension 与另一相关猜想之间的问题；该结论不蕴含 #44 的否定。
- [Forbidden Sidon subsets of perfect difference sets, featuring a human-assisted proof](https://borisalexeev.com/pdf/erdos707.pdf) — Boris Alexeev and Dustin G. Mixon, 2026-01-01; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 可检阅全文：区分有限/无限 PDS 扩充，陈述每个有限 Sidon 集可扩充到无限 PDS，并将讨论限制于与 #44 不同的有限 PDS 目标。
- [Size-4 Counterexamples to the Sidon-Extension Conjecture](https://arxiv.org/abs/2604.25214) — Tong Niu, 2026-04-28; `preprint`, `preprint`, directness=`indirect`, reliability=`medium`. 仅报告 size-4 集合对有限 PDS 扩充的有限范围/部分条件性证据，并明确完整证明仍开放；不是 #44 的解答或反例。
- [The apparent structure of dense Sidon sets](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v30i1p33/pdf/) — Sean Eberhard and Freddie Manners, 2023; `primary_paper`, `peer_reviewed`, directness=`indirect`, reliability=`high`. 研究有限阿贝尔群中接近平方根规模 Sidon 集的已知结构，并提出尚未证明的结构猜想；显示高密度端的结构理论仍不完备，未解决区间扩充问题。
- [Perfect difference sets constructed from Sidon sets](https://arxiv.org/abs/math/0609244) — Javier Cilleruelo and Melvyn B. Nathanson, 2006-09-25; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 构造由稠密 Sidon 集得到的无限完美差集，并给出无限对象的密度结果；它不是保留任意给定有限前缀的近最优有限扩充定理。
- [On the Thickness of Infinite Sidon Sets](https://arxiv.org/abs/2606.28651) — Kevin O'Bryant, 2026-07-09; `preprint`, `preprint`, directness=`indirect`, reliability=`high`. 给出无限 Sidon/Golomb ruler 的 liminf 上界及 limsup 构造，强调无限全局密度和本题“任意有限前缀的单次近最优延拓”是不同量词问题。

### 完成标准

- 肯定出口: Prove that for every N∈Z_{≥1}, every Sidon A⊆[1,N], and every ε∈(0,1), there are integers M>N and B⊆[N+1,M] such that A∪B is Sidon and |A∪B|≥(1−ε)√M. The proof must cover arbitrary finite A, not merely selected or maximal A.
- 否定出口: Exhibit explicit N, a Sidon A⊆[1,N], and ε0∈(0,1) and prove that for every integer M>N and every B⊆[N+1,M], either A∪B is not Sidon or |A∪B|<(1−ε0)√M.

不构成完成：

- Showing that A does not lie in a finite perfect difference set, since this is a stronger and different target.
- Producing near-optimal Sidon sets without requiring that they contain the prescribed A.
- Checking all M up to a finite bound without a theorem that excludes all larger M.
- Obtaining density along an infinite Sidon set that does not contain A, or proving only an infinite extension with no near-optimal finite endpoint.
- Treating the trivial ε≥1 cases as evidence for the substantive assertion.

正确性陷阱：

- Use the Sidon convention with repeated summands included; equivalently audit all nontrivial a+b=c+d relations, not merely sums of distinct elements.
- For a claimed extension, check collisions in A−A, A−B, and B−B, including sign/order conventions.
- Do not replace the required coefficient 1−ε by an unspecified positive constant or allow a fixed loss independent of ε.
- Keep quantifiers in order: M and B may depend on N,A,ε; a universal M(ε) is not required, whereas a construction for only some A is insufficient.
- If using modular constructions, prove that the chosen integer representatives have no wraparound-induced sum/difference collision.
- Do not infer a #44 counterexample from a PDS-extension counterexample.

### 更新后的 AI 可解答性

- 等级: `low_candidate`
- 分数: `18/100`
- 信心: `medium`
- 结论: 这是定义清楚、可直接攻关但难度高的开放目标；适合长期、证明优先的探索，不适合以枚举或已被否定的 PDS 路线为主。

支持理由：

- 量词、阈值和反例证书均可精确定义，任何进展可通过有限 Sidon 碰撞检查与明确引理审计。
- 存在丰富的有限最优构造、无限扩充和高密度结构理论，因而有可复用背景。
- #707 的反例排除了最直接的“先嵌入有限 PDS”统一证明方案，反而清楚界定了不能依赖的路线。

主要障碍：

- 问题要求对任意固定前缀保持包含关系；现有近最优构造通常无法吸收任意 A。
- 无限 PDS 延拓并不控制足够密的有限截断，limsup/liminf 结果也不交换本题量词。
- 高密度 Sidon 集的完整结构本身仍含未解猜想；纯计算不能覆盖所有 M。

Proof-first 路线：

- 尝试给出一个“有限禁差前缀可吸收”的定量补全引理，并明确其常数是否可任意逼近 1。
- 研究极大不可扩张 Sidon 前缀的差集缺口是否强迫固定密度损失，从而导向反例证书。
- 把高密度结构定理或其可证弱形式转化为对包含给定 A 的必要条件；先核实该转化不偷偷要求 PDS。

需要验证：

- 任何正解须逐类验证旧–旧、旧–新、新–新加法碰撞，并给出对所有 N,A,ε 的量词闭合。
- 任何负解须证明对全部未来 M 与 B 的排除，而非仅排除 PDS、Singer 模数或有限搜索范围。
- 若用形式化，先审计 44.lean 的量词编码并消除 sorry；现有文件只是陈述工件。

### 审计限制与人工复核理由

- 该结论基于截至指定日期可公开检索和可打开的材料；未找到解答并非逻辑上证明不存在未索引论文。
- ErdosProblems 页面明确将 OPEN 说明为维护者信念，故状态使用 likely_open 而非把数据库标签当作定理。
- 原始 Erdős 文献的完整页码与 #44 最早措辞未能从可访问页面独立逐页核对；输入陈述、当前题页和 Lean 工件在核心目标上相符。
- 论坛页面本身未能稳定打开；已通过当前题页、精确搜索、arXiv、作者 PDF 与正式仓库交叉检查。
- 未运行大规模枚举，因为它不能为本题的全 M 量词提供停止证明；只审计了已公开的有限范围 PDS 计算声明。

- 在启动高成本研究前，建议加法组合数学专家复核“标准 Sidon”定义与 M>N 的规范化是否完全匹配最初 Erdős 来源。
- 若有人声称将 #707 的 PDS 反例推广为 #44 反例，必须人工审查其是否真正排除了所有近最优 Sidon 超集。
- Lean 文件存在 sorry，且量词记号由项目自定义；形式化专家应在将其用作基准前核对其精确语义。

<!-- DEEP_REVIEW:END -->
