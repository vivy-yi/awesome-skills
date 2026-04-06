# Context Engineering & Multi-Agent Architectures
> 让 AI Agent 在有限注意力中保持巅峰表现

> **适合人群**：AI Agent 开发者、平台工程师、LangChain/LangGraph 用户
> **预计阅读时间**：50 分钟
> **前置要求**：熟悉 AI Coding Agent（Claude Code/Cursor/OpenCode）基础用法

---

## 1. 概述

### 什么是 Context Engineering？

**Context Engineering** 是管理语言模型上下文窗口的学科。与"提示工程"（Prompt Engineering）专注于编写有效指令不同，Context Engineering 关注的是**输入模型的所有信息的整体策划**：系统提示词、工具定义、检索文档、对话历史和工具输出。

核心挑战在于：上下文窗口的约束不是由原始 token 容量决定的，而是由**注意力机制**决定的。随着上下文长度增加，模型会表现出可预测的退化模式：

- **Lost-in-the-Middle** 现象：中间位置的信息recall准确率比首尾低10-40%
- **U 形注意力曲线**：首尾注意力强，中间注意力弱
- **注意力稀缺**：上下文项过多时相互竞争

Context Engineering 的目标是找到**最小的高信号 token 集合**，以最大化期望结果的概率。

### 什么是 Multi-Agent Architecture？

Multi-Agent Architecture 将工作分配给多个语言模型实例，每个实例拥有独立的上下文窗口。设计良好时，这种分配能够实现超越单 Agent 限制的能力；设计糟糕时，则会引入抵消收益的协调开销。

**关键洞察**：Sub-Agent 的存在主要是为了**隔离上下文**，而不是将角色分工拟人化。

### 为什么这两个领域必须一起学？

Context Engineering 和 Multi-Agent 是同一枚硬币的两面：

- **Context Engineering** 解决"如何在单一上下文窗口中最大化效果"
- **Multi-Agent** 解决"如何通过分布式架构突破单一窗口限制"

两者结合，才能构建生产级别的 AI Agent 系统。

---

## 2. 核心概念

### 2.1 上下文的解剖学

**系统提示词（System Prompts）**

用 XML 标签或 Markdown 标题将系统提示词组织为不同部分：

```markdown
<BACKGROUND_INFORMATION>
你是一个 Python 专家，帮助开发团队构建数据处理管道。
</BACKGROUND_INFORMATION>

<INSTRUCTIONS>
- 编写简洁、符合 Python 习惯的代码
- 函数签名包含类型提示
- 公共函数添加文档字符串
- 遵循 PEP 8 风格规范
</INSTRUCTIONS>

<TOOL_GUIDANCE>
使用 bash 执行 shell 操作，python 执行代码任务。
文件操作使用 pathlib 以保证跨平台兼容性。
</TOOL_GUIDANCE>

<OUTPUT_DESCRIPTION>
提供带语法高亮的代码块。
非显而易见的决策在注释中说明。
</OUTPUT_DESCRIPTION>
```

**工具定义（Tool Definitions）**

工具描述需要回答三个问题：
1. 工具做什么
2. 何时使用
3. 返回什么

```markdown
## tool: fetch_weather
描述: 获取指定城市的当前天气信息
何时使用: 用户询问天气或需要根据天气做决策时
返回: { temperature: number, condition: string, humidity: number }
```

**注意**：工具 schema 在 JSON 序列化后会膨胀 **2-3 倍**。10 个中等规模的工具 schema 在发送任何消息之前就能消耗 5,000-8,000 个 token。

**检索文档（Retrieved Documents）**

维护轻量级标识符（文件路径、存储查询、网页链接），动态按需加载数据。保持边界清晰：一旦激活技能或文档，就完整加载——部分加载会产生令人困惑的空白，破坏推理质量。

**对话历史（Message History）**

对话历史充当 Agent 的草稿纸。监控其增长：在长对话中，历史可能消耗 70-80% 的窗口，而 Agent 没有任何可见症状，直到推理质量突然崩溃。

**工具输出（Tool Outputs）**

研究显示，观测结果可以占据 Agent 轨迹总 token 的 **83.9%**。应用**观测遮蔽（Observation Masking）**：一旦 Agent 处理了结果，用紧凑引用替换冗长的输出。

### 2.2 注意力预算

对于 n 个 token，注意力机制计算 n² 个两两关系。随着上下文增长，维持这些关系的能力会下降——不是硬性悬崖，而是性能梯度。

**设计原则**：

| 参数 | 建议值 |
|------|--------|
| 有效容量上限 | 广告窗口的 **60-70%** |
| 200K token 模型开始退化 | 约 120-140K token |
| 复杂检索准确率下降 | 极端长度下可低至 **15%** |

**Token 估算的陷阱**：英文 prose 约 4 字符/token，但代码是 **2-3 字符/token**，URL 和文件路径每个斜杠/点/冒号都是一个独立 token。使用 provider 的实际 tokenizer 进行任何预算关键计算。

### 2.3 渐进式披露（Progressive Disclosure）

渐进式披露在三个层级实现：

```
Level 1: 技能选择 — 启动时只加载名称和描述
                  ↓ 按需激活
Level 2: 文档加载 — 先加载摘要；任务需要时再获取详细章节
                  ↓ 按需触发
Level 3: 工具结果保留 — 最近结果保留完整；较旧的结果压缩或驱逐
```

**关键原则**：如果一个技能被激活，就完整加载它——部分加载会破坏推理质量。

### 2.4 多 Agent 架构的三种主要模式

**模式 1：Supervisor/Orchestrator（主管/编排器）**

```
用户查询 → 主管 → [专家A, 专家B, 专家C] → 聚合 → 最终输出
```

适用于：任务有清晰分解、需要跨域协调或人类监督。

**模式 2：Peer-to-Peer/Swarm（点对点/蜂群）**

移除中央控制，允许 Agent 通过预定义协议直接通信。

```python
def transfer_to_agent_b():
    return agent_b  # 通过函数返回进行交接

agent_a = Agent(
    name="Agent A",
    functions=[transfer_to_agent_b]
)
```

适用于：任务需要灵活探索、刚性计划适得其反或需求动态涌现。

**模式 3：Hierarchical（层级式）**

```
策略层（目标定义）→ 规划层（任务分解）→ 执行层（原子任务）
```

适用于：项目有清晰的层级结构、工作流涉及管理层或任务同时需要高层规划和详细执行。

### 2.5 Token 经济学的现实

生产数据显示，多 Agent 系统运行成本约为单 Agent 聊天的 **15 倍**：

| 架构 | Token 倍数 | 适用场景 |
|------|-----------|---------|
| 单 Agent 聊天 | 1x 基线 | 简单查询 |
| 单 Agent + 工具 | ~4x 基线 | 工具调用任务 |
| 多 Agent 系统 | ~15x 基线 | 复杂研究/协调 |

BrowseComp 评估研究发现，三个因素解释了 **95% 的性能方差**：token 使用量（占方差的 80%）、工具调用次数、模型选择。在更好的模型和更多 token 预算之间，模型质量提升往往提供更大的性能增益。

---

## 3. 主流 Skills 工具深度解析

### 3.1 Agent-Skills-for-Context-Engineering

**GitHub**: `muratcankoylan/Agent-Skills-for-Context-Engineering` ⭐ 7,879

这是 Context Engineering 领域最系统的 Skills 集合，涵盖了构建生产级 AI Agent 系统所需的核心原则。

**核心技能概览**：

| 技能 | 主题 |
|------|------|
| `context-fundamentals` | 上下文基础：上下文窗口、注意力机制、渐进式披露 |
| `context-degradation` | 上下文退化：lost-in-middle、中毒、分心、冲突 |
| `context-compression` | 上下文压缩：为长运行会话设计压缩策略 |
| `multi-agent-patterns` | 多 Agent 架构：编排器、点对点、层级式 |
| `memory-systems` | 记忆系统：短期、长期、图基记忆架构 |
| `tool-design` | 工具设计：构建 Agent 可有效使用的工具 |
| `filesystem-context` | 文件系统上下文：动态上下文发现、工具输出卸载、计划持久化 |
| `context-optimization` | 上下文优化：压缩、遮蔽、缓存策略 |
| `evaluation` | 评估框架：构建 Agent 系统评估 |
| `advanced-evaluation` | 高级评估：LLM-as-Judge 技术 |

**设计哲学**：

- **渐进式披露**：启动时只加载技能名称和描述，完整内容在任务激活时加载
- **平台无关**：专注于跨 Claude Code、Cursor 和任何支持技能的平台的可迁移原则
- **概念基础 + 实践示例**：使用 Python 伪代码演示概念，适用于任何环境

**学术认可**：被北京大学通用人工智能国家重点实验室引用为静态技能架构的开创性工作（[Meta Context Engineering via Agentic Skill Evolution](https://arxiv.org/pdf/2601.21557), 2026）。

**安装方式**（Claude Code）：
```bash
/plugin marketplace add muratcankoylan/Agent-Skills-for-Context-Engineering
```

### 3.2 planning-with-files

**GitHub**: `OthmanAdi/planning-with-files` ⭐ 11,616

实现 Manus 风格的持久化 Markdown 规划——价值 **$2B 收购**的 AI Agent 公司的工作流模式。

**核心价值**：解决 AI Agent 在长程任务中的"失忆"问题。通过文件持久化维护任务状态，使 Agent 在上下文重置后能恢复工作进度。

**关键特性**：

- **会话恢复**：上下文填满后执行 `/clear` 时，自动恢复之前的会话状态
- **多 IDE 支持**：Claude Code、Cursor、Windsurf、GitHub Copilot、Kiro Agent、Gemini CLI 等 16+ 平台
- **活跃的社区 fork**：devis、multi-manus-planning、plan-cascade 等多个社区衍生项目

**版本历史亮点**：
- v2.30.0: 迁移到 `${CLAUDE_SKILL_DIR}` 环境变量
- v2.29.0: 分析工作流模板 `--template analytics`
- v2.26.0: IDE 审计，Factory hooks、Copilot/Gemini hooks
- v2.18.0: BoxLite 沙箱运行时集成

**会话恢复工作原理**：
1. 检查 `~/.claude/projects/` 中的先前会话数据
2. 找到规划文件最后更新时间
3. 提取可能丢失的上下文之后发生的对话
4. 显示同步报告

### 3.3 openskills

**GitHub**: `numman-ali/openskills` ⭐ 7,276

通用 Skills 加载器——"Anthropic Skills 系统的通用安装程序"。

**核心理念**：生成完全兼容 Claude Code 的 `<available_skills>` XML，兼容 Claude Code、Cursor、Windsurf、Aider、Codex 等所有能读取 `AGENTS.md` 的 Agent。

**快速开始**：
```bash
npx openskills install anthropics/skills
npx openskills sync
```

**OpenSkills vs Claude Code 对比**：

| 方面 | Claude Code | OpenSkills |
|------|-------------|------------|
| 技能格式 | SKILL.md | SKILL.md |
| 技能存储 | `~/.claude/skills` | `~/.claude/skills`（默认）或 `./.claude/skills` |
| 技能发现 | 内置 | `AGENTS.md` 中的 `<available_skills>` 块 |
| 跨 Agent | ❌ 仅限 Claude Code | ✅ 所有支持 AGENTS.md 的 Agent |

### 3.4 agentskills/agentskills

**GitHub**: `agentskills/agentskills` ⭐ 7,599

Agent Skills 的官方开放规范——由 Anthropic 维护的开放格式。

**规范核心**：
- Skills 是包含指令、脚本和资源的文件夹
- Agent 可以发现并使用它们来更好地执行特定任务
- 编写一次，随处使用

**许可**：代码 Apache 2.0，文档 CC-BY-4.0。

---

## 4. Context Degradation 的识别与应对

### 4.1 四种上下文失败模式

**1. Lost-in-the-Middle（中间丢失）**

信息被放在上下文中间时，recall 准确率比放在首尾时低 10-40%。

**应对策略**：
- 关键约束放在开头和结尾
- 中间只放参考性信息

**2. Context Poisoning（上下文中毒）**

无关内容取代有用内容。Agent 注意力被低质量内容稀释。

**应对策略**：
- 应用信号密度测试：移除任何内容，判断模型输出是否改变
- 如果不变，移除它

**3. Attention Scarcity（注意力稀缺）**

上下文项过多，相互竞争注意力预算。

**应对策略**：
- 保持工具集最小化
- 合并重叠工具
- 使用渐进式披露

**4. Instruction Clash（指令冲突）**

不同指令高度或风格不一致，导致行为不一致。

**应对策略**：
- 将指令按高度级别分组
- 保持每个部分内部一致——要么是启发式驱动，要么是规定式，不能混合交错

### 4.2 历史记录膨胀的隐形杀手

在 Agent 循环中，每个工具调用都会将请求和完整响应都添加到历史中。经过 20-30 次迭代，历史可以消耗 70-80% 的窗口，而 Agent 没有任何可见症状，直到推理质量崩溃。

**解决方案**：设置硬性 token 上限，达到 70-80% 利用率时主动触发压缩，而不是等待窗口填满。

---

## 5. Multi-Agent 架构实战

### 5.1 Supervisor Pattern 实现

```python
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class SubAgentResult:
    agent_name: str
    output: str
    confidence: float
    status: str  # "success" | "failed" | "partial"

class Supervisor:
    def __init__(self, task: str):
        self.task = task
        self.agents: List[Agent] = []
        self.global_state = {}
    
    def decompose(self) -> List[SubTask]:
        """将任务分解为可并行的子任务"""
        # Supervisor 维护全局状态和轨迹
        # 将用户目标分解为子任务
        # 路由到适当的 worker
        pass
    
    def aggregate(self, results: List[SubAgentResult]) -> str:
        """综合子 Agent 结果"""
        # 验证结果一致性
        # 处理冲突
        # 生成最终输出
        pass

# 关键问题：电话游戏效应
# Supervisor 架构最初比优化版本差约 50%
# 因为 Supervisor 误解 sub-agent 响应
# 解决方案：直接消息传递机制
def forward_message(message: str, to_user: bool = True):
    """
    直接将 sub-agent 响应转发给用户，
    不经过 Supervisor 综合
    """
    if to_user:
        return {"type": "direct_response", "content": message}
    return {"type": "supervisor_input", "content": message}
```

### 5.2 Peer-to-Peer Swarm Pattern

```python
# 无中央控制，Agent 通过显式交接协议通信
class SwarmAgent:
    def __init__(self, name: str, capabilities: List[str]):
        self.name = name
        self.capabilities = capabilities
        self.peers: List['SwarmAgent'] = []
    
    def can_handle(self, task: str) -> bool:
        return any(cap in task for cap in self.capabilities)
    
    def transfer_to(self, peer: 'SwarmAgent', task: str, context: dict):
        """通过函数返回进行交接"""
        if peer.can_handle(task):
            return peer.process(task, context)
        # 否则尝试其他 peer
        for next_peer in self.peers:
            if next_peer != self and next_peer.can_handle(task):
                return next_peer.process(task, context)
        raise ValueError(f"No peer capable of handling: {task}")
```

### 5.3 上下文隔离机制选择

| 机制 | 适用场景 | Token 效率 | 协调复杂度 |
|------|---------|-----------|-----------|
| **全上下文委托** | 复杂任务，sub-agent 需要完整理解 | 低（共享全部上下文） | 低 |
| **指令传递** | 简单、定义明确的任务 | 高 | 中 |
| **文件系统记忆** | 复杂任务需要共享状态 | 中 | 中 |
| **混合策略** | 稳定内容预加载，动态内容按需获取 | 最高 | 高 |

**默认策略**：优先使用指令传递，需要共享状态时升级到文件系统记忆。避免全上下文委托，除非子任务确实需要。

### 5.4 共识与协调机制

**投票问题**：简单多数投票不可取——弱模型的幻觉与强模型的推理等权重。

**更好的方法**：

```python
# 加权投票
def weighted_vote(agent_outputs: List[AgentOutput], weights: List[float]) -> str:
    scores = defaultdict(float)
    for output, weight in zip(agent_outputs, weights):
        scores[output.value] += weight * output.confidence
    return max(scores, key=scores.get)

# 对抗性批评协议
def adversarial_debate(agents: List[Agent], rounds: int = 3) -> str:
    """多轮结构化批评通常比协作共识产生更高的复杂推理准确率"""
    current_output = agents[0].generate()
    for _ in range(rounds):
        critiques = [a.critique(current_output) for a in agents]
        current_output = synthesize_critiques(current_output, critiques)
    return current_output
```

---

## 6. Planning with Files 实战

### 6.1 核心工作流

```
用户输入
    ↓
创建 PLAN.md（任务分解）
    ↓
按计划执行（保留进度到文件）
    ↓
定期更新 PLAN.md
    ↓
任务完成 → 清理临时文件
```

### 6.2 典型 SKILL.md 触发条件

```markdown
---
name: planning-with-files
description: >
  当用户要求"制定计划"、"规划任务"、"分解目标"、"分步骤执行"、
  "持久化规划"、"保存进度"、"恢复会话"、"管理复杂任务"时激活此技能。
  实现了 Manus 风格的持久化 Markdown 规划模式。
---

# Planning with Files

## 激活条件
当用户需要处理复杂、多步骤任务，且需要跨上下文保持连贯性时使用。

## 核心原则

1. **文件优先**：所有计划和进度必须写入文件，而非留在记忆中
2. **原子性更新**：每次计划变更都是独立的、完整的版本
3. **会话恢复**：上下文重置后，从文件中重建状态

## 使用方法

### `/plan:new <任务描述>`
创建新的 PLAN.md，包含任务分解

### `/plan:status`
查看当前计划状态和进度

### `/plan:checkpoint`
在 PLAN.md 中创建检查点
```

### 6.3 规划文件模板

```markdown
# 任务规划: [任务名称]

## 目标
[高层次目标描述]

## 分解

- [ ] 子任务 1
- [ ] 子任务 2
- [ ] 子任务 3

## 进度

### 2026-04-06 11:30
- [x] 子任务 1 完成
- [ ] 子任务 2 进行中
- 障碍: [如有]

### 2026-04-06 12:00  
- [x] 子任务 2 完成
- [ ] 子任务 3 开始

## 检查点
- [Checkpoint 1] 基础结构完成 @2026-04-06 11:00
- [Checkpoint 2] 核心逻辑完成 @2026-04-06 12:00
```

---

## 7. Skills 加载与管理

### 7.1 Agent Skills 规范核心

Agent Skills 格式是一个开放的文件夹格式：

```
skill-name/
├── SKILL.md          # 核心技能定义（必需）
├── README.md         # 详细文档（可选）
├── scripts/          # 可执行脚本（可选）
│   └── do_something.sh
├── resources/        # 资源文件（可选）
│   └── template.md
└── references/       # 参考资料（可选）
    └── detailed_guide.md
```

### 7.2 SKILL.md 标准格式

```markdown
---
name: skill-name
description: >
  当用户说"..."、"..."、"..."或讨论"..."时激活此技能。
  [一句简短描述技能用途]
---

# 技能标题

## 概述
[技能解决的什么是和为什么]

## 激活条件
[明确描述何时应激活此技能]

## 核心内容
[详细的技能指导]

## 代码示例
[可运行的示例]

## 最佳实践
[总结经验]

## 常见错误
[避免的错误]
```

### 7.3 openskills 使用指南

```bash
# 安装官方技能集合
npx openskills install anthropics/skills

# 安装特定技能
npx openskills install muratcankoylan/Agent-Skills-for-Context-Engineering

# 全局安装（所有项目共享）
npx openskills install <repo> --global

# 项目本地安装
npx openskills install <repo>  # 默认安装到 ./.claude/skills

# 同步技能索引
npx openskills sync

# 读取技能内容
npx openskills read context-fundamentals
```

### 7.4 技能发现机制

Claude Code 通过 `<available_skills>` XML 块暴露技能：

```xml
<available_skills>
<skill>
<name>context-fundamentals</name>
<description>理解上下文、为何重要以及 Agent 系统中上下文的解剖</description>
<location>plugin</location>
</skill>
<skill>
<name>multi-agent-patterns</name>  
<description>掌握编排器、点对点和层级式多 Agent 架构</description>
<location>plugin</location>
</skill>
</available_skills>
```

OpenSkills 生成完全兼容的 `<available_skills>` XML 并写入 `AGENTS.md`，使任何能读取 `AGENTS.md` 的 Agent 都能使用 Claude Code 技能。

---

## 8. 最佳实践总结

### Context Engineering 最佳实践

1. **将上下文视为有限注意力预算，而非存储桶**
   - 每个添加的 token 都与模型的注意力竞争
   - 设计系统以最小高信号 token 集最大化结果

2. **关键信息放在注意力偏好位置（开头和结尾）**
   - recall 准确率：开头/结尾 85-95%，中间 76-82%
   - 安全约束、输出格式要求、行为护栏永不放在中间

3. **使用渐进式披露推迟加载直到需要时**
   - 启动时只加载名称和描述
   - 设置严格的激活阈值——技能只在任务明确匹配其触发条件时加载

4. **上下文填充 70-80% 时主动触发压缩**
   - 不要等待窗口填满
   - 保留架构决策、未解决 bug 和实现细节，丢弃冗余输出

5. **子 Agent 架构执行压缩比**
   - Sub-agent 可以使用数万 token 探索
   - 但必须返回 1,000-2,000 token 的压缩摘要

### Multi-Agent 最佳实践

1. **选择模式基于协调需求，而非组织隐喻**
   - 清晰分解 + 需要监督 → Supervisor
   - 灵活探索 + 动态需求 → Peer-to-Peer Swarm
   - 层级结构 + 管理层 → Hierarchical

2. **设计显式协调协议**
   - 共识机制抵抗谄媚（sycophancy）
   - 失败处理防止错误传播级联

3. **优先选择 Swarm 优于 Supervisor**
   - 当 sub-agent 可以直接响应用户时
   - 这完全消除了翻译错误

4. **对 Token 经济有清醒认识**
   - 多 Agent 系统约 15x 单 Agent 成本
   - 将模型选择和多 Agent 架构视为互补策略

### Planning with Files 最佳实践

1. **文件优先于记忆**：所有计划和进度必须写入文件
2. **原子性更新**：每次变更都是完整版本
3. **定期检查点**：每完成一个阶段就保存快照
4. **会话恢复测试**：定期验证上下文重置后的恢复流程

---

## 9. 常见错误（Gotchas）

### Context Engineering 中的陷阱

| 陷阱 | 影响 | 解决方案 |
|------|------|--------|
| 名义窗口 ≠ 有效容量 | 200K 模型在 120-140K 时就开始退化 | 按 60-70% 广告窗口设计 |
| 字符 token 估算静默漂移 | 代码 2-3 字符/token，URL 每字符独立 | 使用实际 tokenizer |
| 工具 schema 膨胀 2-3 倍 | 10 个工具可消耗 5,000-8,000 token | 审计序列化后的 token 数量 |
| 消息历史静默膨胀 | 20-30 次迭代后消耗 70-80% 窗口 | 设置硬性 token 上限 |
| 中间关键指令丢失 | U 形注意力曲线 | 首尾锚定关键约束 |

### Multi-Agent 中的陷阱

| 陷阱 | 影响 | 解决方案 |
|------|------|--------|
| 电话游戏效应 | Supervisor 误解 sub-agent 响应，性能损失 ~50% | 直接消息传递绕过 Supervisor |
| 多数投票赋予幻觉等权重 | 弱模型幻觉 = 强模型推理 | 加权投票或对抗性批评 |
| 收敛性谄媚 | Agent 为求一致而同意，而非正确 | 结构化多轮对抗批评 |
| 错误传播级联 | 一个 Agent 失败级联到所有 | 每层独立验证机制 |

---

## 10. 相关资源

### 核心仓库

| 仓库 | ⭐ | 主题 |
|------|-----|------|
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 7,879 | Context Engineering + Multi-Agent 系统化技能 |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 11,616 | Manus 风格持久化规划 |
| [numman-ali/openskills](https://github.com/numman-ali/openskills) | 7,276 | 通用 Skills 加载器 |
| [agentskills/agentskills](https://github.com/agentskills/agentskills) | 7,599 | Agent Skills 开放规范 |
| [anthropics/skills](https://github.com/anthropics/skills) | 56,124 | Anthropic 官方技能仓库 |
| [obra/superpowers](https://github.com/obra/superpowers) | 38,315 | Agentic Skills 框架 + TDD 开发方法论 |
| [sanbuphy/learn-coding-agent](https://github.com/sanbuphy/learn-coding-agent) | 11,265 | Coding Agent 研究系统性综述 |

### 学术论文

- [Meta Context Engineering via Agentic Skill Evolution](https://arxiv.org/pdf/2601.21557) — 北京大学 GAIC (2026)
- [Lost-in-the-Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.10290) — 研究中间位置信息 recall 退化
- [BrowseComp: A Multi-Turn Reasoning Benchmark for Large Context Models](https://arxiv.org/abs/2409.13386) — 多轮推理评估

### 延伸阅读

- [Agent Skills 官方文档](https://agentskills.io)
- [Agent Skills 规范](https://agentskills.io/specification)
- [Claude Code 技能系统文档](https://docs.anthropic.com/en/docs/claude-code)

---

## 下一步

1. **入门**：安装 `Agent-Skills-for-Context-Engineering` 并尝试 `context-fundamentals` 技能
2. **实践**：在 Claude Code 中使用 `planning-with-files` 规划一个多日复杂项目
3. **深化**：研究 `multi-agent-patterns` 技能并尝试设计一个 Supervisor 系统
4. **扩展**：使用 `openskills` 将 Claude Code 技能导入其他 Agent 平台
5. **贡献**：为 awesome-skills-repos 提交新发现的 Context Engineering 相关项目

---

*整理：墨鉴 | 2026-04-06 | 来源：muratcankoylan/Agent-Skills-for-Context-Engineering, OthmanAdi/planning-with-files, numman-ali/openskills, agentskills/agentskills*
