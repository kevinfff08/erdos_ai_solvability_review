# Problem 307

## 基本信息

- 原始链接: https://www.erdosproblems.com/307
- LaTeX 页面: https://www.erdosproblems.com/latex/307
- 原始状态: `verifiable`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `unit fractions`
- 形式化状态: `yes`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Are there two finite sets of primes $P,Q$ such that\[1=\left(\sum_{p\in P}\frac{1}{p}\right)\left(\sum_{q\in Q}\frac{1}{q}\right)?\]

## AI 完成可能性判断

- 结论: **AI 辅助完成有现实候选路线，但需要外部计算或严格验证**
- 等级: `medium_candidate`
- 分数: `64/100`
- 建议路线: 优先搜索有限证书；若找到证书，再做独立程序验证和形式化复核。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：prime, primes

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: unit fractions
- 证明密集标签命中: number theory
- 有限/计算线索: finite
- 渐近/无限线索: prime, primes
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。
