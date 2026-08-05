# Problem 848

## 基本信息

- 原始链接: https://www.erdosproblems.com/848
- LaTeX 页面: https://www.erdosproblems.com/latex/848
- 原始状态: `decidable`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Is the maximum size of a set $A\subseteq \{1,\ldots,N\}$ such that $ab+1$ is never squarefree (for all $a,b\in A$) achieved by taking those $n\equiv 7\pmod{25}$?

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `59/100`
- 建议路线: 优先将已有有限化归约转成可复现实验、SAT/ILP/穷举或证明助理验证。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：o(, prime, sufficiently large

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: number theory
- 有限/计算线索: 无
- 渐近/无限线索: o(, prime, sufficiently large
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **高可行候选。根据给定 JSON，本题已有 Sawhney 对充分大 N 的解决性说明，且标记为 decidable、formalized=yes；因此 GPT-5.5 级别模型在工具辅助下更可能完成的是复现证明、检查边界条件、形式化验证或计算检验，而不是从零发现全新突破。**
- 等级: `high_candidate`
- 分数: `88/100`
- 信心: `high`
- 可能路线: 可行路线是从模 25 构造出发，证明 n≡7 或 18 mod 25 的单剩余类给出密度 1/25 的可行集；再利用给定备注中的近极值结构定理：若 |A|≥(1/25-c)N 且 N 足够大，则 A 必须包含于两个极值剩余类之一。模型可结合计算搜索检验小 N、形式化证明系统核验同余与平方因子条件，并用文献检索/证明重构工具复核 Sawhney 注记中的稳定性论证。

### 支持理由

- 题目 JSON 明确给出 status=decidable，说明它不是当前信息下完全开放的不可判定研究问题。
- formalized=yes 显著提高了模型辅助验证的可行性，可将自然语言证明与形式化断言互相校验。
- 备注已经给出关键上界思路：由 a^2+1 必有某个 p^2 因子，得到约 0.108 或 0.105 的粗上界，这为证明结构提供了可审计入口。
- 备注还说明 Sawhney 已对充分大 N 证明更强命题：近 1/25 密度的集合必须落在 n≡7 或 n≡18 mod 25 之一，这几乎直接对应极值结构。
- 候选构造本身很容易验证：若 a,b 同属 7 mod 25，则 ab+1 被 25 整除，因此必非 squarefree；18 mod 25 同理。
- 模型可用穷举和 SAT/SMT/整数规划搜索检验有限 N 或寻找反例模式，用于支持或定位小 N 例外。

### 主要障碍

- 核心难点不是同余构造，而是排除所有其他大集合；这通常需要精细筛法、稳定性或加性组合数论论证，不能只靠局部模运算。
- 题目问的是最大值是否由 7 mod 25 达成；备注同时出现 18 mod 25，因此必须仔细处理 N 的余数导致两个剩余类大小可能不同或并列的问题。
- Sawhney 的结果只在备注中概述为“充分大 N”，若要给出完整验证，需要拿到并逐行核验原注记的常数、阈值和例外范围。
- 形式化证明虽然已有标记，但模型仍需确认形式化对象是否精确覆盖本题原命题，尤其是 squarefree、最大值、充分大 N 与有限 N 的量词。
- 若目标扩展到所有 N 而非充分大 N，可能还需要大量有限计算或额外论证。

### 需要的验证

- 核验 Sawhney 注记的完整证明，确认其确实推出题目所问的极值结论，而不仅是近极值分类。
- 检查 n≡7 mod 25 与 n≡18 mod 25 在区间 {1,...,N} 中的计数差异，明确“achieved by 7 mod 25”的确切含义。
- 用程序穷举小 N，寻找是否存在比单个模 25 剩余类更大的例外集合，或验证充分大阈值之外的行为。
- 审计 formalized=yes 对应的形式化文件，确认定理陈述、依赖库和证明状态。
- 对上界论证中的素数平方覆盖、重叠计数和 o(1) 项做独立复核，避免把粗上界误当成最终 1/25 上界。

### 公开版思考摘要

给定材料显示本题已有解决性进展且形式化过，极值构造也非常透明：同一模 25 的 7 类或 18 类会使所有 ab+1 被 25 整除。真正困难在于证明不存在其他同等或更大的集合。备注中 Sawhney 的强稳定性结果正好提供了这一步的核心结构，因此 GPT-5.5 在检索、计算和形式化工具配合下很有希望重构、验证并整理完整解答，尤其适合做证明审计和有限例外检查。

### 免责声明

以上不是该题的数学解答，也不声称已重新证明 Sawhney 的结果；这是基于给定 Problem JSON 对 GPT-5.5 工具辅助可解性与验证可行性的审查。

<!-- MODEL_REVIEW:END -->

<!-- DEEP_REVIEW:START -->

## 证据化深度核验（V2）

- 核验日期: `2026-08-05`
- 核验模型: `gpt-5.6-sol`
- 当前状态: `solved`
- 状态信心: `high`
- 可行动性: `closed_verification_only`
- 人工复核: `required`
- 独立研究 Prompt: `not published (status is not open/revised-open)`

### 状态结论

Sawhney 已证明对充分大 N，最大值由模 25 的 7 类取得，并给出近极值稳定性；这正是题目页面所问的充分大 N 版本，因此状态为 solved，V2 分数固定为 0，不生成 Prompt。

### 当前规范陈述

对充分大的 N，在所有满足任意 a,b∈A 时 ab+1 都非平方自由的 A⊆[N] 中，确定 |A| 的最大值及极值集合。

```text
For sufficiently large N, among A subset [N] such that ab+1 is not squarefree for every a,b in A, determine the maximum |A| and its extremizers.
```

### 陈述、量词与反例审计

- 歧义严重度: `none`
- 简单反例检查: `none_found_after_targeted_check`
- 检查说明: 模 25 的 7 类满足 ab+1≡0 mod25；18 类在某些 N 也可取等号。
- 版本变化: van Doorn、Weisenberg、Cambie 给出密度上界和结构观察；Sawhney 在 OpenAI 科学加速实验中完成稳定性与精确充分大 N 证明。

陈述问题：

- 题目包含 a=b 的情形。
- 结论只声称充分大 N；小 N 的精确分类不是原题关闭所必需。

需要固定的量词/约定：

- The property is required for all ordered or unordered pairs, including a=b.
- The theorem is asymptotic in the sense of all N>=N_0, but the maximum is exact there.

### 文献与当前边界

已核验的主要结果：

- Elementary arguments first bounded the density near 0.105.
- Sawhney proved |A|<=|{n<=N:n≡7 mod25}| for all sufficiently large N.
- Equality/stability forces the 7 or possibly 18 residue class modulo 25.

最近相关工作：Sawhney 的四页证明原文给出 Proposition 1.1 和稳定性说明；OpenAI 报告也明确把 #848 列为 settled。

剩余核心：无剩余开放核心；若研究小 N，应作为新的有限分类问题另行陈述。

已使用方法：

- stability for near-extremal residue classes
- square-divisor sieve

争议或不确定性：

- 证明为研究笔记而非传统期刊论文，但原文完整可核验，且结论与充分大 N 题面完全匹配。

### 证据来源

- [Erdős Problem 848](https://www.erdosproblems.com/848) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对当前题面、状态标签、备注、历史修订和评论声明。
- [LaTeX source for Erdős Problem 848](https://www.erdosproblems.com/latex/848) — Thomas F. Bloom (database editor); `problem_page`, `database_record`, reliability=`medium`. 核对公式、量词和原始引用键。
- [On A subset [N] such that ab+1 is never squarefree](https://www.math.columbia.edu/~msawhney/Problem_848.pdf) — Mehtaab Sawhney; `primary_paper`, `preprint`, reliability=`high`. Proposition 1.1 对充分大 N 给出精确极值上界和近极值结构。
- [Early science acceleration experiments with GPT-5](https://cdn.openai.com/pdf/4a25f921-e4e0-479a-9b38-5367b47e8fd0/early-science-acceleration-experiments-with-gpt-5.pdf) — OpenAI researchers and collaborators; `other`, `preprint`, reliability=`high`. 明确说明 #848 被 Sawhney 的证明解决，并交代 AI 提供初始思路。

### 完成标准

- 肯定出口: Verify Sawhney's proposition and its equality statement against the canonical target.
- 否定出口: Find an error in the proof or a sufficiently large counterexample, with exact certification.

不构成完成：

- Reproving the old 0.105 density bound.
- Classifying small N only.
- Treating the 18 mod 25 class as always equal-sized without checking N.

正确性陷阱：

- Check that a=b is included in every reduction.
- Track floor effects between the 7 and 18 residue classes.
- Do not weaken exact maximum to asymptotic density.

### 更新后的 AI 可解答性

- 等级: `not_applicable_closed_or_invalid`
- 分数: `0/100`
- 信心: `high`
- 结论: 该题已关闭，V2 分数按规则固定为 0。

支持理由：

- 该记录当前不发布求解 Prompt。
- V2 评分按状态规则固定为 0。

主要障碍：

- 证明为研究笔记而非传统期刊论文，但原文完整可核验，且结论与充分大 N 题面完全匹配。
- 完整结论仍要求逐项核验全部量词、边界条件和外部定理假设。

Proof-first 路线：

- 逐行审计稳定性引理与有限例外。
- 当前状态不适用新的求解路线；仅保留独立证明核验义务。

需要验证：

- 逐条核验最终论证的量词、边界和等号情形。
- 复核外部定理的精确假设与引用版本。

### 审计限制与人工复核理由

- 联网检索覆盖题目页、历史、讨论及可定位论文，但不能证明不存在未索引、未公开或不同术语下的结果。
- 未对所有引用论文逐行形式化重证；论坛、AI 生成材料和未同行评议预印本按较低证据等级记录。

- 本批次尚未经过第二个独立强模型复审。
- 状态涉及题面修订、解答声明、低覆盖文献或较新预印本，建议专家重点抽查。

<!-- DEEP_REVIEW:END -->
