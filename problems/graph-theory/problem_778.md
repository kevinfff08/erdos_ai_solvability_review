# Problem 778

## 基本信息

- 原始链接: https://www.erdosproblems.com/778
- LaTeX 页面: https://www.erdosproblems.com/latex/778
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Alice and Bob play a game on the edges of $K_n$, alternating colouring edges by red (Alice) and blue (Bob). Alice goes first, and wins if at the end the largest red clique is larger than any of the blue cliques.

Does Bob have a winning strategy for $n\geq 3$? (Erd\H{o}s believed the answer is yes.)

If we change the game so that Bob colours two edges after each edge that Alice colours, but now require Bob's largest clique to be strictly larger than Alice's, then does Bob have a winning strategy for $n>3$?

Finally, consider the game when Alice wins if the maximum degree of the red subgraph is larger than the maximum degree of the blue subgraph. Who wins?

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `37/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：density

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory
- 证明密集标签命中: 无
- 有限/计算线索: colouring, graph
- 渐近/无限线索: density
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。
