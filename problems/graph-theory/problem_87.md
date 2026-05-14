# Problem 87

## 基本信息

- 原始链接: https://www.erdosproblems.com/87
- LaTeX 页面: https://www.erdosproblems.com/latex/87
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`
- 形式化状态: `no`
- OEIS: `A059442`, `possible`
- 原站备注字段: 无

## 原问题

Let $\epsilon >0$. Is it true that, if $k$ is sufficiently large, then\[R(G)>(1-\epsilon)^kR(k)\]for every graph $G$ with chromatic number $\chi(G)=k$?

Even stronger, is there some $c>0$ such that, for all large $k$, $R(G)>cR(k)$ for every graph $G$ with chromatic number $\chi(G)=k$?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `44/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索
- 存在 OEIS 数据入口，利于实验与反例搜索

### 主要障碍

- 题面含渐近/无限对象线索：\gg, asymptotic, for all large, sufficiently large

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: chromatic, colouring, graph, ramsey
- 渐近/无限线索: \gg, asymptotic, for all large, sufficiently large
- 构造/存在性线索: is there

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **低到中等候选。GPT-5.5 级模型较可能形式化并复核已知的随机着色下界、建立小规模反例搜索流程，并把问题推进到更清晰的极值函数表述；但直接解决任一渐近断言，尤其强形式“存在常数 c 使 R(G)>cR(k)”，很可能需要新的 Ramsey 理论思想，不能主要依赖计算或形式化验证完成。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 将问题重述为 f(k)=min_{χ(G)=k} R(G) 与 R(k) 的比较；先形式化 k-critical 子图给出的边数下界，并验证随机着色证明 R(G) 至少为约 2^{k/2} 量级；再用 SAT/ILP、canonical graph generation 和 Ramsey witness 搜索小 k 的低 Ramsey 数 k-色图，寻找可能的结构模式；最后尝试把模式转化为一般构造或把随机/容器/熵方法强化为相对 R(k) 的下界。

### 支持理由

- 问题陈述短、目标清晰，适合被拆成极值函数、随机下界、有限搜索和形式化验证几个子任务。
- 备注中已经给出可机器复核的基线：任意 k-色图有 R(G) 约大于 2^{k/2}，这为形式化证明和常数优化提供入口。
- 小 k 的反例或近反例可以通过 Ramsey SAT 编码、图生成和证书验证推进，模型可辅助设计搜索空间和解释结构。
- 该问题不要求精确求出 R(k)，因此存在通过相对不等式或条件化框架取得部分推进的可能。

### 主要障碍

- 核心困难是要与未知的对角 Ramsey 数 R(k) 比较；目前备注给出的通用下界只匹配 R(k) 的已知下界量级，而不是实际 R(k) 或最佳上界。
- 命题对所有 χ(G)=k 的图成立，最坏图可能是稀疏、临界、非规则或由特殊构造产生，搜索得到的小规模模式未必能外推。
- 强形式 R(G)>cR(k) 比第一问更刚性；即使证明第一问，也未必能给出固定比例。
- 有限计算很快遇到 Ramsey 数和 k-临界图枚举爆炸，最多提供证据、候选构造或可验证证书，难以单独证明渐近结论。

### 需要的验证

- 明确采用的 R(G) 与 R(k) 定义，并核对是否为二色无向 Ramsey 数。
- 对随机着色下界给出可审计证明，最好形式化到 Lean/Isabelle 或至少生成独立可检查的概率论推导。
- 若做计算搜索，需要保存完整 witness coloring、不可嵌入证书、SAT UNSAT 证书和图同构去重记录。
- 若提出新构造或新下界，需要验证其对所有足够大 k 成立，而不是只覆盖特殊图族。
- 若允许文献检索，需要确认已有关于最小 k-色图 Ramsey 数的结果，避免重复已知定理。

### 公开版思考摘要

这个问题适合 AI 工具链做“结构化推进”：整理等价极值函数、验证基线下界、生成小规模证据、搜索候选最坏图族。但它要求把任意 k-色图的 Ramsey 数同 R(k) 的真实增长联系起来，而 R(k) 本身高度未知，所以完整解决概率偏低。最现实的产出是可信的部分定理、反例搜索报告、形式化的已知下界，以及可能的新猜想或受限图族结果。

### 免责声明

以上只是对 GPT-5.5 级模型可推进性的审查，不是该 Erdős 问题的证明、反例或最终数学结论。

<!-- MODEL_REVIEW:END -->
