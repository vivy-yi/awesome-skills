# Skills 教程索引

> 本目录包含 Skills 的深度教程，覆盖核心框架、MCP 集成、领域特定技能等。

---

## 📚 教程列表

### 0. Skills 市场与资源

| 教程 | 描述 | 阅读时间 |
|------|------|----------|
| [skills-marketplaces.md](skills-marketplaces.md) | Skills 市场全景图、官方/社区资源汇总 | 20 分钟 |

**核心内容**：
- 官方 Skills 市场（Claude Code、OpenClaw、Hermes、OpenCode）
- 社区 Awesome Lists 精选
- Skills 创建工具链
- 快速入门指南

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

### 6. Self-Evolution Skills（自进化技能）

| 教程 | 描述 | 阅读时间 |
|------|------|----------|
| [self-evolution-skills.md](self-evolution-skills.md) | Agent Self-Evolution 深度解析 — GEP 协议 / 群体进化 / 自动生成 Skills | 50 分钟 |

**核心内容**：
- Evolver：GEP 基因组进化协议、Gene/Capsule 资产体系、验证者角色
- SkillClaw：群体技能进化、跨 Agent 共享、多设备同步
- SkillAnything：7 相自动工厂、从任意目标生成多平台 Skills
- Hermes Agent 生态集成
- 三大框架横向对比与选型决策树
- 团队 AI Agent 进化体系组合实战

### 7. Portable Agent Skills（跨平台可移植架构）

| 教程 | 描述 | 阅读时间 |
|------|------|----------|
| [portable-agent-skills-architecture.md](portable-agent-skills-architecture.md) | .agent/ 跨平台 + Skills 工程化实践 | 45 分钟 |

**核心内容**：
- agentic-stack：8 平台通用的 .agent/ 便携记忆容器
- SkillAnything：7 相自动工厂，从任何目标生成跨平台 Skills
- harness：4 层增强元技能（知识管理、架构约束、反馈回路、熵管理）
- SkVM：Skills 语言虚拟机，编译 Skills 以匹配异构模型
- 渐进式披露、Lesson 毕业协议、B-tree 记忆索引

### 8. Skills 场景配置（场景化技能组合）

| 教程 | 描述 | 阅读时间 |
|------|------|----------|
| [skills-scene-configuration.md](skills-scene-configuration.md) | 四大 Agentic Tools 场景化技能组合配置指南 | 35 分钟 |

**核心内容**：
- 场景配置概述：基础层、任务层、场景层三层组合关系
- Claude Code 场景配置：Superpowers 组合、快速修复、文档驱动开发
- OpenClaw 场景配置：企业开发、金融投资、智能家居
- Hermes Agent 场景配置：MLOps 研究、创意开发、Apple 生态
- OpenCode 场景配置：Web 开发、多模型研究
- 场景化技能矩阵：通用开发/企业场景/专业场景横向对比
- 配置决策树：根据身份和需求选择最佳 Skill 组合

### 9. Best Skills 推荐榜单

| 教程 | 描述 | 阅读时间 |
|------|------|----------|
| [best-skills-recommendations.md](best-skills-recommendations.md) | 四大 Agentic Tools Best Skills 排行榜 | 30 分钟 |

**核心内容**：
- Claude Code Best Skills：TDD/Security/Git/Architecture 分类排行
- OpenClaw Best Skills：Medical/Enterprise 特色推荐
- Hermes Agent Best Skills：Autonomous/Production 推荐
- OpenCode Best Skills：SOP/Productivity 推荐
- 跨平台 Best Skills：ai-dev-kit、hatch3r 全平台通用
- Stars 排行榜：全平台 Top 10 和分类排行
- 场景化组合：TDD 开发、安全项目、企业/团队等最佳组合

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
  ├─→ context-engineering-multi-agent.md (上下文工程)
  │
  └─→ skills-scene-configuration.md (场景配置)
  │
高级
  │
  ├─→ self-evolution-skills.md (自进化技能)
  │
  ├─→ portable-agent-skills-architecture.md (跨平台可移植)
  │
  └─→ domain-specific-skills.md (领域专精)
```

---

## 🔄 教程更新日志

| 日期 | 更新内容 |
|------|----------|
| 2026-04-21 | 新增 Best Skills 推荐榜单（30分钟）— Stars 排行榜 / 场景化组合 / 跨平台推荐 |
| 2026-04-21 | 新增 Skills 场景配置指南（35分钟）— 四大 Agentic Tools 场景化技能组合配置 / 决策树 / 快速启动模板 |
| 2026-04-21 | 新增 Agentic Tools 内置 Skills 三层架构对比 — Claude Code / OpenClaw / Hermes / OpenCode 全方位对比 |
| 2026-04-21 | 新增 Skills 市场与资源汇总（20分钟）— 官方市场 / 社区 Awesome Lists / 创建工具链 |
| 2026-04-20 | 新增 Self-Evolution Skills 深度教程（50分钟）— Evolver GEP / SkillClaw 群体进化 / SkillAnything 自动工厂 / Hermes 生态 |
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

*整理：墨鉴 | 2026-04-20*
