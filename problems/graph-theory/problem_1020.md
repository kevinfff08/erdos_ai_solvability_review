# Problem 1020

## 基本信息

- 原始链接: https://www.erdosproblems.com/1020
- LaTeX 页面: https://www.erdosproblems.com/latex/1020
- 原始状态: `falsifiable`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `hypergraphs`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: Erdős matching conjecture

## 原问题

Let $f(n;r,k)$ be the maximal number of edges in an $r$-uniform hypergraph which contains no set of $k$ many independent edges.

For all $r\geq 3$,\[f(n;r,k)=\max\left(\binom{rk-1}{r}, \binom{n}{r}-\binom{n-k+1}{r}\right).\]

## AI 完成可能性判断

- 结论: **AI+计算/形式化工具有较高机会完成或显著推进**
- 等级: `high_candidate`
- 分数: `72/100`
- 建议路线: 优先做反例搜索和小规模枚举；若没有反例，不能据此断言问题为真。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 主要风险是候选证明或计算证书容易存在隐藏漏洞，需要独立复核。

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, hypergraphs
- 证明密集标签命中: 无
- 有限/计算线索: graph, hypergraph
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。
