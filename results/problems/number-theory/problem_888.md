# Problem 888

## 基本信息

- 原始链接: https://www.erdosproblems.com/888
- LaTeX 页面: https://www.erdosproblems.com/latex/888
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `squares`
- 形式化状态: `yes`
- OEIS: `A387584`
- 原站备注字段: 无

## 原问题

What is the size of the largest $A\subseteq \{1,\ldots,n\}$ such that if $a\leq b\leq c\leq d\in A$ are such that $abcd$ is a square then $ad=bc$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `24/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：\gg, o(, prime, primes
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: \gg, o(, prime, primes
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选：GPT-5.5 级别模型很可能不能可靠地直接给出完整渐近解，但有较好机会在构造、有限计算、形式化验证和上界框架整理上取得可审计推进。**
- 等级: `medium_candidate`
- 分数: `63/100`
- 信心: `medium`
- 可能路线: 可行路线是把每个整数按平方因子剥离后的平方自由核表示为向量，将条件转化为 GF(2) 上的奇偶关系和乘法比例约束；先用 SAT/ILP/最大独立集或超图搜索计算 A387584 的更多项，寻找极值结构；再形式化验证 primes、semiprimes 等构造满足条件，并尝试推广到受控素因子个数的集合；上界方面可把违规四元组建成稀疏超图，结合筛法、加性组合/乘法能量和容器方法尝试把已有 o(n) 推进到更接近 n log log n / log n 的量级。

### 支持理由

- 题目条件具有明确的代数编码：abcd 为平方等价于四个平方自由核的异或和为零，这适合计算搜索、SAT/ILP 建模和形式化证明。
- 已有备注给出非平凡上下界：o(n) 上界与 semiprimes 下界之间仍有明显空隙，模型可以围绕这个空隙提出可检验的中间命题。
- formalized=yes 说明至少存在形式化入口，适合让模型做定义等价变换、有限 case 验证、构造正确性证明和反例检查。
- OEIS 条目存在，说明小 n 数据可能可扩展；模型配合程序可生成更多极值样本来辅助猜测结构。
- 构造侧比完整上界更可控，primes 和 semiprimes 的正确性证明短而结构化，模型有机会推广或排除若干自然候选族。

### 主要障碍

- 完整答案很可能需要精细的乘法组合数论，而不仅是局部搜索或形式化验证。
- 从 o(n) 上界推进到匹配 semiprime 级别下界，需要控制大量由平方自由核关系诱导的四元约束，技术难度较高。
- 有限计算可能强烈受小 n 偏差影响，极值集合结构未必稳定外推。
- 形式化证明可以验证候选论证，但不能自动提供关键筛法或容器论证。
- 备注中的已有证明与评论未在本 JSON 中展开，因此任何复现或改进都必须额外进行文献/评论核验后才能算作可靠进展。

### 需要的验证

- 复现并形式化验证 primes 与 semiprimes 构造确实满足条件。
- 编写独立搜索程序，计算更多 n 的最大值或强上下界，并用第二种方法交叉验证。
- 把条件等价转换为平方自由核向量关系，并在证明助手中验证该转换无遗漏，尤其是 a≤b≤c≤d 与重复元素情形。
- 若提出新构造，需要自动枚举小范围反例并给出一般证明。
- 若提出新上界，需要与已知 o(n) 论证逐行比对，并检查所有筛法误差项和常数依赖。

### 公开版思考摘要

这个问题不是纯定义展开题，而是带有清晰代数结构的开放极值数论问题。AI 的优势在于把平方条件编码成可计算对象、扩大实验数据、验证自然构造、整理已有 o(n) 证明并尝试局部改进；劣势在于完整渐近式大概率依赖深层筛法或乘法组合论。综合看，它适合作为“显著推进或验证”的候选，但不应高估为短期可完全解决。

### 免责声明

以上是对 GPT-5.5 级别模型可推进性的审查，不是该 Erdős 问题的解答，也没有声称给出最优上界、下界或完整渐近公式。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `solved`
- 状态信心: `high`
- 可行动性: `closed_verification_only`
- 人工复核: `required`
- 独立研究 Prompt: `not published (closed/non-research status)`

### 状态结论

2026 年公开证明给出与半素数下界匹配到常数因子的上界，原站于 2026-05-28 改为 SOLVED；按规则 V2 评分固定为 0 且不发布研究 prompt。

### 当前规范陈述

令 M(n) 为满足下述性质的 A⊆[1,n] 的最大大小：若 a≤b≤c≤d∈A 且 abcd 为平方数，则 ad=bc。现已确定 M(n)=Θ(n log log n/log n)。

```text
Let M(n) be the maximum size of A subset [1,n] such that whenever a<=b<=c<=d are elements of A and abcd is a square, then ad=bc. The resolved order of magnitude is M(n)=Theta(n log log n/log n).
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `not_applicable`
- 检查说明: 未发现使新上界失效的简单边界例；正式核验仍应关注重复元素和图分解。
- 版本变化: 从 o(n) 上界与素数/半素数下界推进到匹配的 n log log n/log n 量级。

陈述问题：

- a,b,c,d 可相等，因为题面使用非严格不等号。
- 解决的是增长阶，不是精确常数。

需要固定的量词/约定：

- The extremal property ranges over all nondecreasing quadruples from A.
- Theta means two absolute positive constants for all sufficiently large n.

### 文献与当前边界

已核验的主要结果：

- Sárközy/Tao 给 M(n)=o(n)。
- 半素数给 M(n)≫n log log n/log n。
- Chojecki 提示的 GPT-5.5 Pro 证明给匹配上界。

最近相关工作：公开 12 页笔记给出主定理证明，原站在 2026-05-28 标记解决并有标准检查无问题的论坛记录。

剩余核心：题目已关闭；剩余工作仅是独立验证、同行评议或常数优化，不属于开放问题求解。

已使用方法：

- 平方自由核着色的二部图。
- Kővári–Sós–Turán 型矩形计数。

争议或不确定性：

- 当前证明为公开研究笔记而非同行评议期刊论文。
- 本审计未形式化重证全部引理。

### 证据来源

- [Erdős Problem 888](https://www.erdosproblems.com/888) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 888](https://www.erdosproblems.com/latex/888) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。
- [A square-product rigidity problem of Erdős, Sárközy and Sós](https://www.ulam.ai/research/erdos888.pdf) — P. Chojecki with GPT-5.5 Pro; `preprint`, `preprint`, reliability=`high`. 证明 M(n)≪n log log n/log n，与半素数下界匹配。
- [Problem 888 discussion thread](https://www.erdosproblems.com/forum/thread/888) — multiple contributors; `forum`, `informal_claim`, reliability=`medium`. 记录证明发布、检查和题目关闭过程。

### 完成标准

- 肯定出口: Verify the published upper bound and semiprime lower bound to conclude M(n)=Theta(n log log n/log n).
- 否定出口: A valid challenge would identify a concrete fatal flaw in the upper bound and show the claimed order is unsupported; absent that, the problem remains classified solved.

不构成完成：

- Claiming an exact leading constant not proved by the source.
- Citing only the database status without the proof note.
- Treating the earlier o(n) theorem as the final estimate.

正确性陷阱：

- Audit repeated entries a<=b<=c<=d.
- Check the squarefree-core graph decomposition and rectangle count.
- Separate order of magnitude from asymptotic equivalence.

### 更新后的 AI 可解答性

- 等级: `not_applicable_closed_or_invalid`
- 分数: `0/100`
- 信心: `high`
- 结论: 题目已关闭，V2 可解答性按规则固定为 0。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 逐引理验证公开笔记。
- 独立重证图论计数及解析数论估计。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
