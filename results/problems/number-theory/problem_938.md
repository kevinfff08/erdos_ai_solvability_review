# Problem 938

## 基本信息

- 原始链接: https://www.erdosproblems.com/938
- LaTeX 页面: https://www.erdosproblems.com/latex/938
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `yes`
- OEIS: `A001694`, `possible`
- 原站备注字段: 无

## 原问题

Let $A=\{n_1<n_2<\cdots\}$ be the sequence of powerful numbers (if $p\mid n$ then $p^2\mid n$).

Are there only finitely many three-term progressions of consecutive terms $n_k,n_{k+1},n_{k+2}$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `42/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 所属标签偏证明密集：number theory

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: finite, finitely
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **GPT-5.5 级别模型很可能无法单独完成完整证明，但有中等偏高机会显著推进：可建立大规模计算证据、生成并验证候选参数化族、把问题化约为有限个丢番图/椭圆曲线或筛法子问题，并检查形式化定义与枚举正确性。若要给出最终“只有有限多”的证明，需要新的全局间隙或排除机制，难度较高。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 较现实的路线是先利用 powerful number 的结构表示生成严格枚举器，搜索连续 powerful 数中的三项等差模式；同时把三项 powerful 等差条件写成若干指数受限的丢番图方程族，结合模筛、局部障碍、椭圆曲线/超椭圆曲线计算和形式化验证，尝试证明大范围无例外或把无限族压缩到少量不可解情形。模型可在计算实验、猜想提炼、Lean/Isabelle 形式化枚举器、以及文献检索整理上发挥作用。

### 支持理由

- 问题表述短且结构清楚：只涉及 powerful numbers 的有序序列和连续三项等差条件，适合程序化枚举、形式化规格化和反例搜索。
- powerful number 有标准结构表示，模型配合计算工具可以较可靠地生成候选、验证相邻性条件，并发现小例子或长区间缺例现象。
- 问题已标记 formalized=yes，说明至少形式化陈述层面可被机器检查；这有利于把计算证据、枚举边界和辅助引理逐步纳入可审计流程。
- 三项等差约束比任意模式更代数化，可能被转写为若干曲线上的有理点/整数点问题，适合 CAS、Sage、Magma、SMT/模筛和证明助理协作。
- 即使不能证明有限性，模型也可能给出有价值推进：更高搜索界、候选反例数据库、必要同余条件、等价重述、或把某些指数模式完全排除。

### 主要障碍

- 关键困难不是找到三项 powerful 等差数列，而是证明它们作为 consecutive terms 只出现有限多次；相邻性条件是全局排序条件，通常比单纯丢番图方程更难控制。
- powerful numbers 的平均间隙增长，但局部聚集仍可能复杂；从密度估计推出等差连续三元组有限性需要远强于平均分布的结果。
- 备注中相邻整数形态的相关猜想也显示，短区间内 powerful numbers 的排除问题可能触及很深的丢番图难题。
- 若存在无限参数族的 powerful 三项等差数列，仍需证明其中几乎都被区间内其他 powerful number 打断；这类“无中间项”条件不容易代数化。
- 计算搜索只能给出有限范围证据，若没有可证明的上界或下降机制，无法直接转化为完整证明。

### 需要的验证

- 实现至少两个独立枚举器，交叉验证 powerful number 生成、排序、去重和 consecutive 三项等差检测。
- 对搜索到的每个候选三元组，机器验证三项均 powerful，且两个开区间内没有其他 powerful number。
- 记录搜索上界、复杂度、整数溢出处理和 squarefree/幂次分解假设，最好给出可复现实验脚本。
- 对任何声称的理论化约，需要用 CAS 或证明助理验证局部同余筛、曲线模型、变量范围和例外情形。
- 若提出有限性证明路线，必须明确从密度/间隙/丢番图约束到“只有限多个 consecutive AP”的逻辑桥梁，并检查是否隐含未证明的短区间 powerful number 猜想。

### 公开版思考摘要

这个问题对 AI 工具链是有吸引力的：定义可计算、形式化友好，且三项等差条件提供了代数入口。GPT-5.5 级别模型大概率能产出可靠的实验平台和若干可验证引理，也可能通过文献检索与计算代数把问题拆成更清楚的子问题。但完整证明需要控制 powerful numbers 的局部分布和相邻性，这超出普通枚举与模式识别，除非发现新的强结构或成功化约到可完全求解的有限曲线族。因此评为 medium_candidate，而不是 high_candidate。

### 免责声明

以上不是该 Erdős 问题的解答，也不声称证明有限性或无限性；它只是基于给定 problem JSON 对 GPT-5.5 级别模型辅助研究可行性的审查。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `likely_open`
- 状态信心: `medium`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_938.md](../../prompts/problem_938.md)

### 状态结论

题面明确，当前页仍开放且有研究者登记正在工作；缺少实质已知结果，因此只能 likely_open 并提示碰撞风险。

### 当前规范陈述

把正强大数递增排列为 n_1<n_2<…。满足 n_k,n_{k+1},n_{k+2} 构成非平凡三项等差数列的指标 k 是否只有有限个？

```text
List the powerful positive integers increasingly as n_1<n_2<.... Is the set of indices k for which n_k,n_{k+1},n_{k+2} form a nonconstant three-term arithmetic progression finite?
```

### 陈述、量词与反例审计

- 歧义严重度: `minor`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 相关“连续三个整数都强大”是不同问题；有限计算不能证明本题有限性。
- 版本变化: 题目页仅列相关的 #364 猜想，无直接部分结果。

陈述问题：

- consecutive 指强大数序列中的连续三项，不是三个连续整数。
- 强大数要求每个整除它的素数至少平方整除。

需要固定的量词/约定：

- The arithmetic progression condition is n_k+n_{k+2}=2n_{k+1}.
- Finiteness is over all indices k.

### 文献与当前边界

已核验的主要结果：

- 强大数可参数化为 a^2b^3（b 平方自由），但表示可能不唯一需规范。
- 没有列出的无限排除或构造定理。

最近相关工作：题目页更新至 2025-10-31，并显示 SkyYang 正在研究；未列出解答主张。

剩余核心：证明充分大的连续三强大数不成 AP，或构造无穷多个这样的连续三项。

已使用方法：

- a^2b^3 参数化与椭圆/超椭圆曲线。
- 强大数间隙和区间排除。

争议或不确定性：

- 活跃研究者意味着并行碰撞和状态快速变化风险。
- 缺少直接文献使开放置信度仅为中。

### 证据来源

- [Erdős Problem 938](https://www.erdosproblems.com/938) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 938](https://www.erdosproblems.com/latex/938) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。

### 完成标准

- 肯定出口: Prove there exists K such that no k>=K satisfies n_k+n_{k+2}=2n_{k+1}.
- 否定出口: Construct infinitely many indices k for which three consecutive powerful numbers form an arithmetic progression, including proof that no other powerful number lies in either intervening interval.

不构成完成：

- Finding many triples of powerful numbers that are not consecutive in the powerful-number sequence.
- Finite searches.
- Solving only the consecutive-integers problem.

正确性陷阱：

- Prove consecutiveness by excluding all intervening powerful numbers.
- Handle nonuniqueness in a^2b^3 parametrisations.
- Do not infer finiteness from density zero.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `40/100`
- 信心: `medium`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 把 AP 方程与两个空区间条件联合参数化。
- 推导强大数局部间隙的有效下界以排除大解。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
