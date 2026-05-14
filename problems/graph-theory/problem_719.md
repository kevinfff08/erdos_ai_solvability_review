# Problem 719

## 基本信息

- 原始链接: https://www.erdosproblems.com/719
- LaTeX 页面: https://www.erdosproblems.com/latex/719
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `hypergraphs`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Let $\mathrm{ex}_r(n;K_{r+1}^r)$ be the maximum number of $r$-edges that can be placed on $n$ vertices without forming a $K_{r+1}^r$ (the $r$-uniform complete graph on $r+1$ vertices).

Is every $r$-hypergraph $G$ on $n$ vertices the union of at most $\mathrm{ex}_{r}(n;K_{r+1}^r)$ many copies of $K_r^r$ and $K_{r+1}^r$, no two of which share a $K_r^r$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `44/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

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
