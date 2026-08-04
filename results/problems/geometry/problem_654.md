# Problem 654

## 基本信息

- 原始链接: https://www.erdosproblems.com/654
- LaTeX 页面: https://www.erdosproblems.com/latex/654
- 原始状态: `open`
- 奖金: `no`
- 主类别: `geometry`
- 原始标签: `geometry`, `distances`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $f(n)$ be such that, given any $x_1,\ldots,x_n\in \mathbb{R}^2$ with no four points on a circle, there exists some $x_i$ with at least $f(n)$ many distinct distances to other $x_j$. Estimate $f(n)$ - in particular, is it true that\[f(n)>(1-o(1))n?\]Or at least\[f(n) > (1/3+c)n\]for some $c>0$, for all large $n$?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `20/100`
- 建议路线: 优先提取等价表述、尝试特殊情形、寻找可计算子问题，再决定是否进入证明搜索。

## 判断依据

### 有利因素

- 目前只能依靠通用数学推理、文献归纳和特殊情形探索

### 主要障碍

- 所属标签偏证明密集：distances, geometry
- 题面含渐近/无限对象线索：for all large, o(
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: distances, geometry
- 有限/计算线索: 无
- 渐近/无限线索: for all large, o(
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **适合作为中等候选问题：GPT-5.5 级别模型较可能在“验证已有反例、形式化命题边界、搜索改进构造、整理可计算证据”方面显著推进，但不宜预期直接证明正的线性改进下界。**
- 等级: `medium_candidate`
- 分数: `62/100`
- 信心: `medium`
- 可能路线: 最现实路线是先把给定备注中的 Fe26 型反例转化为可复核的构造与验证任务：证明无四点共圆、逐点统计不同距离数，并形式化排除退化情形；随后用计算搜索两线或少数曲线上的参数化点集，寻找把上界从 3/4 n 继续压低的族。对于下界方向，模型可尝试把“同一点多重等距圈”转化为圆-点关联或能量不等式问题，检验是否能超过平凡的 (n-1)/3，但这一步更依赖新的组合几何想法。

### 支持理由

- 问题表述清晰，核心对象是有限点集、圆上点数限制和单点 distinct distances，适合程序枚举、符号代数验证和形式化证明辅助。
- 给定备注已经显示最强猜想 f(n)>(1-o(1))n 被反例击破，因此模型不必从零解决全部问题，也可以围绕反例验证和上界改进做可审计推进。
- “无四点共圆”和“从每个点看到的不同距离数”都是可计算性质；对参数化构造可用代数消元、随机特化和精确有理数检查形成较强证据。
- 若目标是证明或反驳较弱的 f(n)>(1/3+c)n，模型可生成大量候选极端构型，帮助判断 1/3 附近是否有真实障碍。

### 主要障碍

- 正向下界需要全局控制所有点的距离重数，通常会牵涉深层离散几何和关联界；工具化搜索本身很难自动产生新的常数提升证明。
- 无四点共圆约束既排除许多规则格点例子，也让极端构造更脆弱，参数选择中的退化情况必须逐一排除。
- 已有 3/4 n 上界反例说明原来的强猜想已失败，但离判定是否存在 (1/3+c)n 的普适下界仍有很大间隙。
- 计算搜索容易发现小 n 或特殊族现象，但把它推广成任意大 n 的严格构造或定理是主要难点。

### 需要的验证

- 对 Fe26 反例或任何新构造给出精确坐标族，并机器验证任意 n 或无限子序列下无四点共圆。
- 对每个点的 distinct distances 上界给出可形式化证明，而不是只依赖数值统计。
- 若声称改进下界，需要明确依赖的几何引理、常数损失和所有退化配置处理，并最好用 Lean/Isabelle 或可检查证明脚本验证关键组合计数。
- 若提出计算搜索证据，需要保存代码、随机种子、精确算术输出和失败案例，避免浮点距离相等造成误判。

### 公开版思考摘要

这个问题对 AI 的可操作部分较强：性质可判定、反例可验证、候选构造可搜索，且给定备注已经把最强版本转化为可审计的反例验证与上界优化问题。困难在于剩余的核心开放部分是普适线性下界，可能需要新的离散几何不等式，而不只是更大规模计算。因此我判断 GPT-5.5 配合工具有较好机会做出有价值推进或验证，但直接完成完整估计 f(n) 的概率中等偏低。

### 免责声明

以上不是该 Erdős 问题的解答，也不声称证明或反驳剩余开放断言；它只是基于给定 problem JSON 对 GPT-5.5 级别模型可推进性的审查。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-04`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `revised_open`
- 状态信心: `high`
- 可行动性: `research_ready`
- 人工复核: `required`
- 独立研究 Prompt: [results/prompts/problem_654.md](../../prompts/problem_654.md)

### 状态结论

Aletheia 的两直线构造否定无一般位置条件的强猜想，但未触及较弱线性改进，也未否定附加无三点共线的强版本；规范目标取较弱开放核心。

### 当前规范陈述

令 f(n) 为如下保证的最大整数：任意无四点共圆的 n 点平面集都有一点向其余点确定至少 f(n) 种距离。证明或否定存在绝对常数 c>0，使充分大 n 有 f(n)>(1/3+c)n。无一般位置假设的 (1-o(1))n 强猜想已被否定。

```text
Let f(n) be the largest integer such that every n-point set in R^2 with no four concyclic contains a point determining at least f(n) distinct distances to the other points. Prove or disprove that f(n)>(1/3+c)n for some absolute c>0 and all sufficiently large n. The stronger claim f(n)>(1-o(1))n without a general-position assumption is false and is not the target.
```

### 陈述、量词与反例审计

- 歧义严重度: `material`
- 简单反例检查: `counterexample_found`
- 检查说明: 两条直线上的构造使每点至多约 3n/4 种距离，否定无条件 (1-o(1))n；不否定 (1/3+c)n。
- 版本变化: 平凡下界 (n-1)/3；2026 构造否定最强版本后，弱线性改进仍开放。

陈述问题：

- f(n) 是对所有配置的最坏情形保证。
- 无四点共圆允许大量共线点。
- 强版本、弱版本和一般位置版本必须分开。

需要固定的量词/约定：

- c is one absolute positive constant independent of n.
- The assertion is for every sufficiently large n and every admissible configuration.

### 文献与当前边界

已核验的主要结果：

- f(n)≥(n-1)/3。
- 无条件 (1-o(1))n 被至多 3n/4 的构造否定。
- 带无三点共线的一般位置强版本未被该构造处理。

最近相关工作：Feng 等 2026 的 Gemini/Aletheia 案例给出反例构造并被题目页吸收。

剩余核心：证明某个固定 c>0 的普适线性改进，或构造使 f(n)≤(1/3+o(1))n 的反例族。

已使用方法：

- 等距图和圆周容量双计数。
- 两线/多线构造与代数避免共圆。

争议或不确定性：

- 最新反例来自预印本。
- 一般位置变体是不同目标，不应静默替代。

### 证据来源

- [Erdős Problem 654](https://www.erdosproblems.com/654) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态、已知结果、评论主张和页面更新时间。
- [LaTeX source for Erdős Problem 654](https://www.erdosproblems.com/latex/654) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对题面公式、原始引用键和备注。
- [Semi-Autonomous Mathematics Discovery with Gemini: A Case Study on the Erdős Problems](https://arxiv.org/abs/2601.22401) — T. Feng et al.; `preprint`, `preprint`, reliability=`high`. 给出两直线反例，否定无条件 (1-o(1))n 强版本。

### 完成标准

- 肯定出口: Prove an explicit absolute c>0 and N_0 such that every admissible n-point configuration with n>=N_0 has a point with more than (1/3+c)n distinct distances.
- 否定出口: Construct admissible configurations for infinitely many n in which every point determines at most (1/3+o(1))n distinct distances.

不构成完成：

- Refuting only the already false (1-o(1))n claim.
- Proving the statement under no-three-collinear unless explicitly presented as partial progress.
- A finite configuration family without asymptotic control.

正确性陷阱：

- Verify no four points are concyclic.
- Count distinct distances from a single point, not globally.
- Keep constants uniform in n.

### 更新后的 AI 可解答性

- 等级: `low_to_medium_candidate`
- 分数: `36/100`
- 信心: `medium`
- 结论: 该评分只针对核验后的开放核心；它反映定义清晰度、已有结构、可验证性与剩余理论跨度，不把有限计算或文献整理当作解答。

支持理由：

- 规范目标及完成标准可明确写出。
- 已有结果提供可复核的技术入口或边界。

主要障碍：

- 完整结论仍含无限量词或一般维数/一般参数。
- 现有结果与完整解决之间仍需新的数学论证。

Proof-first 路线：

- 加强圆周入射双计数以超过 1/3。
- 系统分析少数直线支撑的极端构造及其界限。

需要验证：

- 逐条核验最终论证的量词和边界情形。
- 复核所有外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、LaTeX、讨论与可定位的直接论文，但无法证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛和预印本主张按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态或规范目标涉及近期预印本、历史歧义、有限残余或低文献覆盖，需要专家抽查。

<!-- DEEP_REVIEW:END -->
