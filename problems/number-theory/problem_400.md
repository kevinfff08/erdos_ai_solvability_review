# Problem 400

## 基本信息

- 原始链接: https://www.erdosproblems.com/400
- LaTeX 页面: https://www.erdosproblems.com/latex/400
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `factorials`
- 形式化状态: `yes`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

For any $k\geq 2$ let $g_k(n)$ denote the maximum value of\[(a_1+\cdots+a_k)-n\]where $a_1,\ldots,a_k$ are integers such that $a_1!\cdots a_k! \mid n!$. Can one show that\[\sum_{n\leq x}g_k(n) \sim c_k x\log x\]for some constant $c_k$? Is it true that there is a constant $c_k$ such that for almost all $n<x$ we have\[g_k(n)=c_k\log x+o(\log x)?\]

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `25/100`
- 建议路线: 优先文献定位、特殊情形、数值实验和辅助引理搜索；完整证明需要新的数学思想。

## 判断依据

### 有利因素

- 已有形式化陈述，可降低语义误读风险

### 主要障碍

- 所属标签偏证明密集：factorials, number theory
- 题面含渐近/无限对象线索：\ll, o(
- 缺少明显有限搜索入口。

### 公开版思考过程摘要

- 先识别问题类型：无限/渐近或抽象证明倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: 无
- 证明密集标签命中: factorials, number theory
- 有限/计算线索: 无
- 渐近/无限线索: \ll, o(
- 构造/存在性线索: can one

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。
