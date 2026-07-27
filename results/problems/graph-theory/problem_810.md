# Problem 810

## 基本信息

- 原始链接: https://www.erdosproblems.com/810
- LaTeX 页面: https://www.erdosproblems.com/latex/810
- 原始状态: `open`
- 奖金: `no`
- 主类别: `graph theory`
- 原始标签: `graph theory`, `ramsey theory`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Does there exist some $\epsilon>0$ such that, for all sufficiently large $n$, there exists a graph $G$ on $n$ vertices with at least $\epsilon n^2$ many edges such that the edges can be coloured with $n$ colours so that every $C_4$ receives $4$ distinct colours?

## AI 完成可能性判断

- 结论: **AI 可能做出局部推进或搜索反例，但完整解决把握不足**
- 等级: `low_to_medium_candidate`
- 分数: `43/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 题面含渐近/无限对象线索：for all large, sufficiently large

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: graph theory, ramsey theory
- 证明密集标签命中: 无
- 有限/计算线索: colouring, graph, ramsey
- 渐近/无限线索: for all large, sufficiently large
- 构造/存在性线索: does there exist

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **不太可能由 GPT-5.5 级别模型直接完成，但有中等概率显著推进：尤其是把“同色边对不能处在同一个 C4 中”的约束转化为可验证的极值不等式、生成有限模型反例搜索、或形式化检查已有条件性归约。若目标是给出完整否定解答，难度仍接近开放极值图论核心问题。**
- 等级: `low_to_medium_candidate`
- 分数: `38/100`
- 信心: `medium`
- 可能路线: 较可行的路线是先完全避免求解式蛮力，改做结构化归约：把每个颜色类视为一组边，要求任意同色两边不共同落入任何 C4；再用 codegree、C4 计数、能量法、dependent random choice 或双计数证明若 e(G) >= epsilon n^2 且颜色数 <= n，则必然存在一个非彩虹 C4。工具可用于小规模 SAT/ILP 搜索、猜测极值构型、验证双计数不等式、以及把局部引理形式化。若走构造方向，则可搜索有限几何、群标号或设计理论型着色，但 remarks 暗示主流猜测是否定，因此构造路线风险更高。

### 支持理由

- 问题表述清晰，约束可以直接转成“同色边对不得属于任何 C4”的组合条件，适合计算搜索和形式化验证局部引理。
- 它不是纯元数学问题；可以通过极值图论、反 Ramsey 数、超图 Zarankiewicz 型对象等已有工具链进行系统攻击。
- remarks 已给出重要结构线索：P4 版本已有否定结果，更一般的连通二部非星图除完全二部图外已有进展，说明 C4 是边界难点但并非完全无抓手。
- 与 3-均匀超图函数 g(n;7,4) 的联系给出一条条件性路线：若能证明相关 o(n^2) 型上界，可能推出本问题方向上的结果。
- GPT-5.5 配合 SAT/ILP、随机搜索和符号双计数，可能发现新的局部禁形、改进常数、或验证某些强假设下的否定结论。

### 主要障碍

- 完整否定解答似乎需要解决 C4 作为完全二部图时的特殊困难；remarks 明确说一般定理目前仍剩 complete bipartite 情形。
- 若证明依赖 g(n;7,4)=o(n^2) 一类超图极值猜想，则会触及另一个未解决核心难题，AI 很难直接跨越。
- 颜色数为 n 而边数为 epsilon n^2，平均每色线性多条边；但将这个平均信息转化为必然产生非彩虹 C4 的全局论证并不直接。
- 计算搜索只能覆盖很小 n，容易产生误导性模式；从有限模式外推到渐近 epsilon n^2 需要强理论桥接。
- 构造方向也困难：高 girth 图边数不足二次量级，而稠密图通常含大量 C4，着色必须同时避免所有 C4 的重复颜色。

### 需要的验证

- 建立精确定义检查：确认“每个 C4 receives 4 distinct colours”是否等价于任意同色边对不共同处于某个 C4，并把该条件用于所有后续推导。
- 用 SAT/ILP 或 CP-SAT 枚举小 n 的最大边数与最少颜色数，寻找可重复的极值模式，而不是只看随机例子。
- 对任何候选上界证明进行形式化或半形式化验证，特别是双计数中关于 codegree、颜色类大小、相交边对和对边对的分类。
- 检索并核查 BEGS89 与 Sarkozy-Selkow 相关结果，确认可用定理的精确假设、是否覆盖 C4 的任何子情形、以及 P4 证明是否可迁移。
- 若提出条件性结果，需要明确依赖的超图极值命题强度，不能把 g(n;7,4)=o(n^2) 当作已知事实。

### 公开版思考摘要

这个问题对 AI 的主要吸引力在于形式短、约束可计算、且已有 remarks 提供了几条明确攻击线；因此 GPT-5.5 级别模型有机会做出严肃的局部推进或验证工作。可是完整解决大概率需要新的极值图论思想，尤其要处理 C4/complete bipartite 的剩余难点，可能还牵连到独立的超图极值问题。因此我把它评为 low_to_medium_candidate：适合 AI 辅助研究推进，不适合期待一次性自动解决。

### 免责声明

以上不是该 Erdős 问题的解答，也没有声称证明存在或不存在这样的 epsilon；它只是基于给定 Problem JSON 对 GPT-5.5 级别工具增强模型可推进性的审查。

<!-- MODEL_REVIEW:END -->
