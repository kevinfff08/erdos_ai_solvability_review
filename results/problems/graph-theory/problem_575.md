# Problem 575

## 基本信息

- 原始链接: https://www.erdosproblems.com/575
- LaTeX 页面: https://www.erdosproblems.com/latex/575
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `turan number`
- 形式化状态: `no`
- OEIS: `N/A`
- 原站备注字段: 无

## 原问题

If $\mathcal{F}$ is a finite set of finite graphs then $\mathrm{ex}(n;\mathcal{F})$ is the maximum number of edges a graph on $n$ vertices can have without containing any subgraphs from $\mathcal{F}$. Note that it is trivial that $\mathrm{ex}(n;\mathcal{F})\leq \mathrm{ex}(n;G)$ for every $G\in\mathcal{F}$.

Is it true that, for every $\mathcal{F}$, if there is a bipartite graph in $\mathcal{F}$ then there exists some bipartite $G\in\mathcal{F}$ such that\[\mathrm{ex}(n;G)\ll_{\mathcal{F}}\mathrm{ex}(n;\mathcal{F})?\]

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `41/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：\ll

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, turan number
- 证明密集标签命中: 无
- 有限/计算线索: finite, graph
- 渐近/无限线索: \ll
- 构造/存在性线索: 无

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等偏低候选：GPT-5.5 级别系统不太可能直接解决该公开 Erdős-Simonovits 极值图论问题，但有现实机会在受限图族、候选反例搜索、已知 Turan 上下界整理、以及形式化验证局部归约方面取得显著推进。**
- 等级: `low_to_medium_candidate`
- 分数: `43/100`
- 信心: `medium`
- 可能路线: 可行路线不是直接给出全局证明，而是把命题重写为“有限禁止族中某个二部成员是否在常数因子内决定 family Turan 数”。模型可先按二部成员的已知 ex(n;G) 阶、2-density、退化度、含环结构、树/森林/偶圈/完全二部图等类别拆分；再用计算搜索生成小图族 F，结合 extremal graph SAT/ILP 或 flag algebra 式证书寻找 ex(n;F) 比所有二部单图 ex(n;G) 小超常数因子的模式；对发现的模式尝试抽象为一般构造或证明其不可能。形式化证明更适合验证有限图族、有限 n 的 extremal certificates，以及某些标准归约，而不是一次性形式化完整开放问题。

### 支持理由

- 问题陈述短且结构清晰，核心是一个可形式化的不等式和有限禁止族量词，适合由模型转成可计算搜索与证明子目标。
- 该问题属于极值图论中有大量已知技术和特例的区域；工具辅助模型可以系统整理单个二部图和禁止族的已知 Turan 阶，并寻找可复用的充分条件。
- 反例搜索有明确计算入口：枚举小型二部图集合与混合禁止族，用 SAT/ILP/MaxSAT 求有限 n 的 extremal numbers，观察比例是否呈增长趋势。
- 即使不能解决全局命题，模型可产出有价值的中间成果，例如覆盖树、森林、偶圈、部分 complete bipartite graphs、或 bounded-degree 小图的特例证明草案。
- 命题要求常数因子比较而非精确常数，理论上比精确 Turan 数更适合自动化推理和渐近归约。

### 主要障碍

- 这是开放的 Erdős-Simonovits 问题，可能触及二部 Turan 数中许多未解决的指数和上界问题；现有工具难以自动发现全新全局方法。
- 关键困难在于 family 禁止条件可能通过多个图的交互显著降低 extremal number，判断这种交互是否总能由某个单一二部成员代表并不局部。
- 很多二部图的 ex(n;G) 本身只知道粗略界或 conjectural exponent，模型若依赖未证事实容易生成看似合理但不可用的证明。
- 有限 n 计算只能提供模式或排除小反例，不能直接证明渐近常数因子结论；外推风险很高。
- 形式化证明库中对现代 extremal graph theory 的覆盖通常不足，许多标准渐近工具需要先做大量基础形式化。

### 需要的验证

- 核对所有使用的 Turan 数特例和引理是否为已发表定理，避免把猜想或经验上界当作事实。
- 对任何候选反例族，需要计算多组递增 n，并给出可复验的 SAT/ILP 证书或构造性上下界。
- 若提出正向特例证明，需要明确常数依赖只允许依赖 F，并逐步检查渐近符号方向是否与命题一致。
- 需要独立专家审读，特别检查 family 禁止条件与单图禁止条件之间的包含关系、量词顺序和二部成员选择是否被误用。
- 若使用形式化证明，应优先形式化定义、单调性、有限证书验证器和具体小图案例，而不是声称已形式化完整定理。

### 公开版思考摘要

该问题很适合工具化研究推进：定义明确、可计算搜索空间存在、并且许多特例可由已知 extremal graph theory 技术处理。但它的全局形式仍可能需要新的二部 Turan 理论，尤其要控制多个禁止图之间的交互是否能被一个二部成员常数因子代表。因此对 GPT-5.5 级别模型的合理预期是发现特例、整理证据、提出候选归约或反例方向，而不是高置信度地完成最终证明。

### 免责声明

以上是 AI 可解性与研究推进潜力评估，不是该 Erdős 问题的解答，也不声称证明或反驳了命题。

<!-- MODEL_REVIEW:END -->
