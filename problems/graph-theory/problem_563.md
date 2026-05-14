# Problem 563

## 基本信息

- 原始链接: https://www.erdosproblems.com/563
- LaTeX 页面: https://www.erdosproblems.com/latex/563
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`, `hypergraphs`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

Let $F(n,\alpha)$ denote the smallest $m$ such that there exists a $2$-colouring of the edges of $K_n$ so that every $X\subseteq [n]$ with $\lvert X\rvert\geq m$ contains more than $\alpha \binom{\lvert X\rvert}{2}$ many edges of each colour.

Prove that, for every $0\leq \alpha< 1/2$,\[F(n,\alpha)\sim c_\alpha\log n\]for some constant $c_\alpha$ depending only on $\alpha$.

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `54/100`
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

- 计算/组合标签命中: graph theory, hypergraphs, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: chromatic, colouring, graph, hypergraph, ramsey
- 渐近/无限线索: 无
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5+tools`
- 结论: **低可行。该问题的完整证明很可能超出 GPT-5.5 级别模型当前可可靠完成的范围；但模型可对已知概率上下界、有限反例搜索、形式化等价关系和候选常数区间做有价值的验证与整理。**
- 等级: `low_candidate`
- 分数: `18/100`
- 信心: `high`
- 可能路线: 可行路线不是直接求解，而是先形式化定义并证明 alpha=0 时与对角 Ramsey 数的逆问题等价；再用随机二染色、Chernoff/大偏差和并集界重建 F(n,alpha)=Theta_alpha(log n)；随后尝试寻找能推出极限常数的近似乘法性或子可加结构，并用 SAT/ILP/旗代数或有限搜索检验小规模行为。若只针对固定 alpha>0，可能还能探索更强的大偏差稳定性猜想；但原命题包含 alpha=0，因此完整解决必须处理经典 Ramsey 常数存在性障碍。

### 支持理由

- 问题有清晰的概率方法基线，GPT-5.5 配合计算和形式化工具应能重建 F(n,alpha) 上下界为常数倍 log n 的证明框架。
- alpha=0 子情形等价于要求存在无单色 K_m 的 K_n 二染色，即对角 Ramsey 数 R(m,m) 的反函数；证明 F(n,0) 渐近于 c log n 本质上要求对角 Ramsey 数具有指数级渐近常数。
- 模型可显著推进的部分包括：整理等价命题、验证有限 n 的极值构造、搜索候选近似递推、把随机构造中的大偏差常数显式化，并将部分引理形式化。
- 该问题结构明确、参数单一、已有 Theta(log n) 基线，因此比完全无结构的开放问题更适合工具辅助审计和局部推进。

### 主要障碍

- 完整命题包含 alpha=0，触及经典对角 Ramsey 数指数增长率是否存在的核心困难，现有简单概率方法不足以给出渐近常数。
- 需要控制所有大诱导子集中的两色边密度，这比单个集合的大偏差估计更强，随机模型中的相关性和极值构造都很难精确处理。
- 缺少明显的子加性、超加性或近似乘法性结构来直接推出 F(n,alpha)/log n 的极限。
- 有限计算只能覆盖很小规模，难以区分真实渐近常数、缓慢波动项和构造族之间的差异。

### 需要的验证

- 严格证明 alpha=0 与对角 Ramsey 数反函数的等价，并明确该子问题所需的 Ramsey 渐近常数命题。
- 检查随机染色给出的上界常数和下界常数，确保大偏差估计、并集界和依赖参数没有隐藏的量级损失。
- 用 SAT/ILP 或约束规划验证小 m,n 的 F(n,alpha) 值或界，寻找是否存在支持极限常数的稳定模式。
- 检索并核对相关 Ramsey、quasi-Ramsey、hereditary discrepancy、hypergraph generalization 文献，确认是否已有对固定 alpha>0 的部分结果或反例性波动现象。
- 若提出候选证明，需由形式化证明系统或独立专家审查关键递推/压缩/张量化步骤，因为这类步骤最可能暗中假设了未证明的 Ramsey 乘法性。

### 公开版思考摘要

我将该问题视为一个关于二染色图的 hereditary density 阈值问题。随机染色能解释为什么阈值是 log n 量级，但题目要求存在精确渐近常数。关键判断来自 alpha=0：此时条件退化为避免大小 m 的单色团，正是经典对角 Ramsey 数的逆形式。因此，一份完整证明不能只处理一般密度偏差，还必须解决 Ramsey 数指数常数存在性这一深层障碍。GPT-5.5 可做严谨整理、计算实验和局部引理验证，但不应被评为高概率完成完整开放问题。

### 免责声明

以上是对 AI 工具辅助可解性与推进潜力的审查，不是该 Erdős 问题的证明或反例。

<!-- MODEL_REVIEW:END -->
