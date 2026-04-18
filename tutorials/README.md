# Skills 教程索引

> 本目录包含 Skills 的深度教程，覆盖核心框架、MCP 集成、领域特定技能等。

---

## 📚 教程列表

### 1. Core Frameworks（核心框架）

| 教程 | 描述 | 阅读时间 |
|------|------|----------|
| [core-frameworks-deep-dive.md](core-frameworks-deep-dive.md) | Anthropic Skills 体系、Superpowers 框架深度解析 | 30 分钟 |

**核心内容**：
- SKILL.md 标准格式与规范
- Progressive Disclosure 加载机制
- Superpowers TDD 工作流
- AgentSkills 开放规范
- 完整 Skill 编写实战

### 2. MCP & Integrations（MCP 协议集成）

| 教程 | 描述 | 阅读时间 |
|------|------|----------|
| [mcp-protocol-deep-dive.md](mcp-protocol-deep-dive.md) | Model Context Protocol 完全指南 | 40 分钟 |

**核心内容**：
- MCP 与 Skills 的职责分工
- MCP 服务器类型与实现
- MCP + Skills 协同模式
- MCP 服务器开发实战
- 安全最佳实践

### 3. Domain-Specific Skills（领域特定技能）

| 教程 | 描述 | 阅读时间 |
|------|------|----------|
| [domain-specific-skills.md](domain-specific-skills.md) | 安全技能专题 | 35 分钟 |

**核心内容**：
- OWASP Top 10 安全检查
- 密钥检测与防护
- 自动化安全审查
- CI/CD 安全集成
- GDPR/PCI-DSS 合规

### 4. Best Practices（最佳实践）

| 教程 | 描述 | 阅读时间 |
|------|------|----------|
| [design-md-for-agents.md](design-md-for-agents.md) | DESIGN.md 设计系统规范 — 让 AI Coding Agent 构建风格一致的 UI | 25 分钟 |
| [the-skill-md-pattern.md](the-skill-md-pattern.md) | SKILL.md 编写规范 | 15 分钟 |

**核心内容**：
- SKILL.md 标准格式
- 触发条件设计
- 代码示例规范
- 常见错误避免

### 5. Context Engineering & Multi-Agent（上下文工程与多智能体）

| 教程 | 描述 | 阅读时间 |
|------|------|----------|
| [context-engineering-multi-agent.md](context-engineering-multi-agent.md) | Context Engineering 基础 + Multi-Agent 架构模式深度解析 | 50 分钟 |

**核心内容**：
- Context Engineering 核心概念：注意力预算、渐进式披露、Lost-in-Middle
- Multi-Agent 三种架构模式：Supervisor、Swarm、Hierarchical
- Context Degradation 的识别与应对
- Planning with Files（Manus 风格持久化规划）
- OpenSkills 通用技能加载器

### 6. Portable Agent Skills（跨平台可移植架构）

| 教程 | 描述 | 阅读时间 |
|------|------|----------|
| [portable-agent-skills-architecture.md](portable-agent-skills-architecture.md) | .agent/ 跨平台 + Skills 工程化实践 | 45 分钟 |

**核心内容**：
- agentic-stack：8 平台通用的 .agent/ 便携记忆容器
- SkillAnything：7 相自动工厂，从任何目标生成跨平台 Skills
- harness：4 层增强元技能（知识管理、架构约束、反馈回路、熵管理）
- SkVM：Skills 语言虚拟机，编译 Skills 以匹配异构模型
- 渐进式披露、Lesson 毕业协议、B-tree 记忆索引

---

## 📖 学习路径

```
入门
  │
  ├─→ the-skill-md-pattern.md (SKILL.md 基础)
  │
中级
  │
  ├─→ core-frameworks-deep-dive.md (核心框架)
  │
  ├─→ mcp-protocol-deep-dive.md (MCP 集成)
  │
  └─→ context-engineering-multi-agent.md (上下文工程)
  │
高级
  │
  ├─→ portable-agent-skills-architecture.md (跨平台可移植)
  │
  └─→ domain-specific-skills.md (领域专精)
```

---

## 🔄 教程更新日志

| 日期 | 更新内容 |
|------|----------|
| 2026-04-18 | 新增 Portable Agent Skills 跨平台可移植架构教程（45分钟）— agentic-stack / SkillAnything / harness / SkVM |
| 2026-04-06 | 新增 Context Engineering & Multi-Agent 深度教程（50分钟） |
| 2026-04-05 | 初始化教程体系：Core Frameworks、MCP、Security Skills |

---

## 📝 投稿指南

如果你想为 awesome-skills 贡献教程：

1. **Fork** awesome-skills-repos 仓库
2. **创建** `tutorials/your-topic.md`
3. **遵循** 教程格式规范（见下文）
4. **提交** Pull Request

### 教程格式规范

```markdown
# 教程标题

> **适合人群**：...
> **预计阅读时间**：XX 分钟
> **前置要求**：...

## 1. 概述
介绍主题和核心概念

## 2. 核心内容
详细讲解

## 3. 实战案例
提供可运行的示例

## 4. 最佳实践
总结经验

## 5. 相关资源
延伸阅读

## 下一步
实践建议
```

---

## 🏷️ 教程标签

| 标签 | 含义 |
|------|------|
| `core` | 核心概念 |
| `practical` | 实战案例 |
| `security` | 安全相关 |
| `framework` | 框架集成 |
| `mcp` | MCP 协议 |
| `workflow` | 工作流 |

---

*整理：墨鉴 | 2026-04-18*
