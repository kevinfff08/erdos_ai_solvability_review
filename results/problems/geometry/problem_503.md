# Problem 503

## 基本信息

- 原始链接: https://www.erdosproblems.com/503
- LaTeX 页面: https://www.erdosproblems.com/latex/503
- 原始状态: `open`
- 奖金: `no`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`
- 形式化状态: `yes`
- OEIS: `A175769`
- 原站备注字段: 无

## 原问题

What is the size of the largest $A\subseteq \mathbb{R}^d$ such that every three points from $A$ determine an isosceles triangle? That is, for any three points $x,y,z$ from $A$, at least two of the distances $\lvert x-y\rvert,\lvert y-z\rvert,\lvert x-z\rvert$ are equal.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `35/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：distances, geometry
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: distances, geometry
- 有限/计算线索: 无
- 渐近/无限线索: 无
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。该题有清晰的有限点集几何表述、已形式化、上下界相差只有线性量级，适合 GPT-5.5 级别模型结合代数几何建模、Gram 矩阵、SAT/SMT/SDP 搜索和形式化验证来推进；但要给出所有维数 d 的精确极值，很可能仍需要新的结构性几何论证，因此不应评为高可解。**
- 等级: `medium_candidate`
- 分数: `64/100`
- 信心: `medium`
- 可能路线: 可行路线是把点集转化为带距离颜色的完全图与半正定 Gram 矩阵约束：每个三角形至多出现两种边长。模型可先复现并形式化已有的二维、三维结论和 Blokhuis 上界框架，再系统枚举小维数、小规模候选距离图，用 SDP/符号秩约束筛掉不可嵌入图，寻找超过已知下界的构造或证明特定规模不可能。若发现稳定模式，再尝试把距离图结构归纳为一般 d 的线性改进上界或新下界。

### 支持理由

- 问题陈述短且精确，核心条件可直接编码为三点距离相等约束，适合自动搜索和形式化证明辅助。
- 已知上下界为 binom(d+1,2)+1 与 binom(d+2,2)，差距约为 d，不是数量级未知的问题；这提高了局部推进的可行性。
- 已形式化这一点很有利：模型可以把实验性证明片段、有限维小案例或代数不等式交给证明助手验证，降低伪证明风险。
- 低维答案 d=2,3 已知，可作为回归测试，帮助检查搜索器、Gram 矩阵约束和证明策略是否正确。
- Alweiss/Weisenberg 构造基于坐标向量和简单距离结构，模型较可能自动分析其可推广性或寻找小幅增强。

### 主要障碍

- 全维数精确答案可能依赖深层结构定理，而不只是有限枚举；GPT-5.5 即使有工具也未必能发明关键几何分类。
- 欧氏可嵌入性不是单纯图论性质，需要同时控制距离取值、Gram 矩阵半正定性和嵌入维数，自动搜索容易产生假候选。
- 已知 d=3 的答案为 8 暗示简单上下界都不是真相，可能存在维数相关的例外结构或复杂最优族。
- 若要证明上界，必须排除连续参数族，而非只排除有限距离图；这对自动代数消元和形式化验证都较重。
- 问题虽然形式化，但现有备注只给出边界和少量构造信息；模型需要额外文献检索才能可靠复现已有证明脉络。

### 需要的验证

- 验证形式化版本是否完全对应题目中的欧氏距离条件，尤其是点是否要求互异、A 是否有限、维数嵌入约束如何表达。
- 复现 d=2 最大值 6 与 d=3 最大值 8，作为计算与证明管线的基准测试。
- 对候选距离图进行双重验证：组合枚举检查三点条件，Gram/SDP 或符号计算检查是否可嵌入 R^d。
- 若提出新构造，需要给出显式坐标、距离计算和维数降维证明。
- 若提出新上界，需要形式化或至少机器可检查地覆盖连续参数情形，而不是只报告随机或有限搜索失败。

### 公开版思考摘要

我把该题视为一个结构清晰但仍有核心创新门槛的极值欧氏几何问题。它对 AI 友好的部分是条件局部、代数化自然、已有形式化、低维可校验、上下界差距不大；不友好的部分是一般 d 的精确极值很可能需要分类定理或新的几何不变量。因此 GPT-5.5 级别模型较可能显著推进小维数验证、候选构造搜索、线性幅度的界改进或形式化复核，但直接完整解决全问题的概率只属中等。

### 免责声明

以上是对 AI 辅助可推进性的评估，不是该 Erdős 问题的解答，也不声称给出了新的上下界或最优构造。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_503.md](../../prompts/problem_503.md)

### 状态结论

一般维数仍开放；2026 论坛笔记给出精确约化且修补过重大缺口，但未同行评议、形式化不完整，故为 likely_open 并进入人工复核。

### 当前规范陈述

对每个 d≥1，求有限集合 S⊂R^d 的最大大小 f(d)，其中任意三个互异点至多产生两种非零距离。近期未审稿笔记声称把 f(d) 约化为二距离极值函数；只有独立核验后才能使用。

```text
For each d>=1, determine f(d), the maximum cardinality of a finite set S subset R^d such that every three distinct points of S determine at most two nonzero distances. A current unrefereed reduction claims f(d)=max{g(d),s(d)+1,s(d-1)+3}; it may be used only after its proof is independently audited.
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 未发现字面反例；近期约化早期版本曾因完整分解中二点块条件错误而出现重大缺口，修订版声称已修复。
- 版本变化: 已知 f(2)=6、f(3)=8、f(4)=11、f(22)=276；Blokhuis 给一般二次上界。

陈述问题：

- 三点必须互异，二距离按非零欧氏距离。
- “求大小”是对每个维数的精确极值问题。

需要固定的量词/约定：

- The property is required for every three-element subset of S.
- A complete answer must determine f(d) for all dimensions or reduce it rigorously to explicitly defined standard extremal functions in a way accepted as resolving the target.

### 文献与当前边界

已核验的主要结果：

- 二维与三维精确值分别为 6、8。
- 一般上界 f(d)≤C(d+2,2)，下界至少 C(d+1,2)+1。
- 2026 修订笔记声称精确约化到欧氏/球面二距离极值函数。

最近相关工作：Chojecki 2026 修订笔记修补了二点首块的极端情形；论坛有独立正面检查，但尚非正式同行评议。

剩余核心：独立核验或修正该约化，并进一步决定仍未知的 g(d)、s(d) 组合所给出的 f(d)。

已使用方法：

- Ionin 完整分解。
- 球面与欧氏二距离集的多项式界。

争议或不确定性：

- 关键最新来源为非审稿笔记。
- 早期版本有已确认重大漏洞，修订证明必须逐行审计。

### 证据来源

- [Erdős Problem 503](https://www.erdosproblems.com/503) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 503](https://www.erdosproblems.com/latex/503) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。
- [Problem 503 discussion thread](https://www.erdosproblems.com/forum/thread/503) — multiple contributors; `forum`, `informal_claim`, reliability=`medium`. 记录约化、原重大缺口、修订与后续检查。
- [Euclidean isosceles sets and two-distance extremal functions](https://www.ulam.ai/research/erdos503-final.pdf) — P. Chojecki with AI assistance; `preprint`, `preprint`, reliability=`medium`. 修订笔记声称 f(d)=max{g(d),s(d)+1,s(d-1)+3}。

### 完成标准

- 肯定出口: Give a complete proof determining f(d) for every d, or rigorously establish the stated reduction and close every remaining extremal term needed to make f(d) explicit.
- 否定出口: Refute the current reduction by an explicit configuration or a proved logical gap that survives the revised note, then provide the correct extremal statement if claiming resolution.

不构成完成：

- Quoting the revised note without auditing it.
- Determining only finitely many dimensions.
- Repeating Blokhuis's upper bound.

正确性陷阱：

- Use Ionin's correct condition |S_i|>=2, not >=3.
- Separate at-most-two from exactly-two distance conventions.
- Check affine dimension and spherical-center assumptions in the two-point block case.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 对修订约化的二点块与 two-shell 引理做独立重证。
- 分析 g(d)、s(d) 的已知相对界能否使最大项唯一。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
