# Problem 1188

## 基本信息

- 原始链接: https://www.erdosproblems.com/1188
- LaTeX 页面: https://www.erdosproblems.com/latex/1188
- 原始状态: `open`
- 奖金: `no`
- 主类别: `number theory`
- 原始标签: `number theory`, `covering systems`
- 形式化状态: `no`
- OEIS: `possible`
- 原站备注字段: 无

## 原问题

Call a set of distinct integers $1<n_1<\cdots<n_k$ with associated congruence classes $a_i\pmod{n_i}$ a distinct covering system if every integer satisfies at least one of these congruences. A minimal distinct covering system is one such that no proper subset forms a covering system.

Let $F(x)$ count the number of minimal distinct covering systems with all moduli in $[1,x]$. Estimate $F(x)$.

## AI 完成可能性判断

- 结论: **当前通用 AI 单独完整解决的可能性低**
- 等级: `low_candidate`
- 分数: `33/100`
- 建议路线: 优先小规模实验、自动猜想、SAT/SMT/ILP 编码、Lean/Isabelle 形式化局部引理。

## 判断依据

### 有利因素

- AI 擅长把有限组合结构转成搜索/优化/验证程序
- 题面或备注出现有限对象/计算线索

### 主要障碍

- 所属标签偏证明密集：number theory
- 题面含渐近/无限对象线索：\gg

### 公开版思考过程摘要

- 先识别问题类型：有限/可计算倾向
- 再比较 AI 强项：符号化、程序化搜索、形式化检查、文献归纳与反例生成。
- 最后按主要障碍扣分：无限量词、渐近估计、素数/分析工具、长期高奖金和缺少有限证书都会降低完整解决概率。

## 特征记录

- 计算/组合标签命中: covering systems
- 证明密集标签命中: number theory
- 有限/计算线索: covering system
- 渐近/无限线索: \gg
- 构造/存在性线索: construct

## 备注

这是一份 AI 可完成性评估，不是该问题的数学解答。评估不使用“人类尚未解决所以 AI 不能解决”的规则；它按问题结构、可计算入口、形式化状态、验证难度和工具需求作判断。

<!-- MODEL_REVIEW:START -->

## GPT-5.5 单题模型复审

- 复审类型: `one_problem_model_review`
- 模型: `GPT-5.5`
- 结论: **中等候选。GPT-5.5 级别模型不太可能一次性给出可信的完整估计，但有现实机会在计算枚举、SAT/整数规划建模、形式化验证已有构造、以及寻找新的下界族或小范围精确值方面显著推进。**
- 等级: `medium_candidate`
- 分数: `58/100`
- 信心: `medium`
- 可能路线: 可行路线是先把“最小 distinct covering system”转化为有限约束问题：对给定模数集合枚举或求解可覆盖所有剩余类的同余类选择，并检查每个同余类的必要性；用 SAT/精确覆盖/CRT 分解枚举小 x 的 F(x)，识别可扩展模板；同时形式化验证已知下界构造的 minimal 性和计数，并尝试从构造自由度中抽取更强的参数族。上界方向可尝试用最小性给每个模数分配 witness residue，再结合 lcm 周期、素因子结构和覆盖密度约束压缩搜索空间。

### 支持理由

- 问题定义离散且有限，对固定 x 可完全转化为周期为 lcm(1,...,x) 上的覆盖判定，适合 SAT、SMT、整数规划和证书验证。
- 已有备注给出明确基线：下界至少 exp((log x)^{3-o(1)})，上界 exp(O(x log x))，中间差距巨大，存在可被模型攻击的改进空间。
- minimal 条件提供额外结构：每个同余类必须有至少一个只被它覆盖的整数，这能生成可验证证书，也可能导出非平凡计数约束。
- 模型可结合计算实验发现小模数模式、自动生成候选构造，并用形式化证明工具验证覆盖性、互异模数和最小性。
- 即便不能完成全 asymptotic，给出可复现枚举表、证书格式、构造族验证和改进的局部上下界，也属于对该问题的实质推进。

### 主要障碍

- 完整估计 F(x) 需要同时控制构造数量和排除大量潜在系统，当前上下界差距从 polylog 指数级到线性指数级，结构信息明显不足。
- lcm(1,...,x) 随 x 指数增长，直接周期枚举很快不可行，必须依赖 CRT 分解、剪枝和证书压缩。
- minimal distinct covering systems 的计数对同余类选择和模数集合都敏感，可能存在大量非模板化例外，机器搜索难以外推成定理。
- 上界尤其困难：需要证明所有最小系统都满足强结构约束，而不是只验证已知或搜索到的族。
- 已有备注暗示 Erdős 的直觉可能被新构造改变，说明问题的真实增长阶可能远比朴素预期复杂。

### 需要的验证

- 实现独立的覆盖与 minimal 性证书检查器，避免搜索程序自身错误影响结论。
- 对小 x 枚举结果进行交叉验证：至少使用两种不同编码，例如 SAT 与整数规划或回溯搜索。
- 若提出新下界族，需要给出参数化构造、覆盖证明、minimal 证明和不同系统数目的无重复计数证明。
- 若提出上界，需要明确说明所有 minimal 系统如何被编码，并证明编码数量确实覆盖全部可能情况。
- 所有渐近声明都应拆成可形式化的引理，优先在 Lean/Isabelle 或可检查的组合证明脚本中验证核心有限覆盖论证。

### 公开版思考摘要

这个问题很适合工具辅助，因为固定范围内的对象可以被精确编码并验证，而且 minimal 性天然给出 witness 证书。GPT-5.5 级别模型有较好机会产出可靠计算数据、验证已有构造、发现新模板或提出局部改进。但完整估计 F(x) 仍需要新的全局结构定理，尤其是非平凡上界，因此更应评为“可显著推进”而非“很可能解决”。

### 免责声明

以上不是该问题的解答，也没有声称给出 F(x) 的新估计；它只是评估 GPT-5.5 级别模型在工具辅助下对该单一问题的潜在可解性与推进路径。

<!-- MODEL_REVIEW:END -->
