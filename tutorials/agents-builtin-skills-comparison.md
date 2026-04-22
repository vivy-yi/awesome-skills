# Agentic Tools 内置 Skills 三层架构对比

> **适合人群**：想了解不同 AI Agent 内置 Skills 系统的开发者
> **预计阅读时间**：40 分钟
> **更新日期**：2026-04-21

---

## 1. 三层架构概述

### 1.1 什么是三层架构

三层架构是一种**分层解耦**的 Skills 组织方式，让不同层次的技能各司其职：

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         Skills 三层架构                                              │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  Layer 3: 垂直领域技能 (Vertical)                                                    │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐                                │
│  │ Apple 🍎│ │ GitHub 🐙│ │ Gaming 🎮│ │ 金融 💰 │                                │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘                                │
│                              │                                                      │
│  Layer 2: 能力平台技能 (Platform)                                                   │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐                                │
│  │ Creative │ │ Research │ │ DevOps  │ │ 编程 💻 │                                │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘                                │
│                              │                                                      │
│  Layer 1: 基础设施技能 (Foundation)                                                │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐                                              │
│  │ AI代理 🤖│ │ 推理服务 │ │ MCP 🔌 │                                              │
│  └─────────┘ └─────────┘ └─────────┘                                              │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

| 层级 | 定位 | 特点 | 示例 |
|------|------|------|------|
| **Layer 1** | 基础设施 | 跨平台通用，不依赖具体领域 | AI Agents、推理服务、MCP |
| **Layer 2** | 能力平台 | 通用能力封装，可组合使用 | 创意、研究、编程，开发 |
| **Layer 3** | 垂直领域 | 深度集成特定平台/场景 | Apple、GitHub，游戏、金融 |

---

## 2. Claude Code Skills 系统

### 2.1 定位

| 属性 | 值 |
|------|-----|
| **Skills 数量** | 17+ 官方 |
| **Star** | ⭐ 56,124 (GitHub) |
| **设计理念** | 少而精，渐进式披露 |
| **生态** | Anthropic 官方 + 社区 |

### 2.2 三层架构

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                    Claude Code Skills 三层架构                                         │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  Layer 3: 垂直领域 — Claude Code 官方不内置，按需安装                                  │
│                                                                                     │
│  Layer 2: 能力平台 — 官方提供少量核心 Skills                                         │
│  ├── code-review                                                                 │
│  ├── docs                                                                         │
│  ├── test                                                                         │
│  └── debug                                                                        │
│                                                                                     │
│  Layer 1: 基础设施 — 核心内置工具 (非 Skills)                                         │
│  ├── Read, Write, Bash, Grep                                                       │
│  ├── WebFetch, WebSearch                                                           │
│  ├── Agent, Task                                                                 │
│  └── MCP (外部扩展)                                                                │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.3 官方 Skills 列表

| Skill | 分类 | 描述 |
|-------|------|------|
| `code-review` | Layer 2 | 代码审查与质量检查 |
| `docs` | Layer 2 | 文档生成 |
| `test` | Layer 2 | 测试生成 |
| `debug` | Layer 2 | 调试辅助 |
| `refactor` | Layer 2 | 重构建议 |
| `git-commit` | Layer 2 | Git 提交生成 |

### 2.4 设计特点

**优势**：
- 官方 Skills 经过严格测试，质量有保障
- 渐进式披露机制节省 Token
- 社区生态丰富，1,000+ Skills 可选

**局限**：
- 官方 Skills 数量较少
- Layer 1 能力依赖 MCP 扩展
- 无内置的三层架构组织

---

## 3. OpenClaw Skills 系统

### 3.1 定位

| 属性 | 值 |
|------|-----|
| **Skills 数量** | 120+ 内置 + 13,729+ 市场 |
| **市场** | ClawHub (clawhub.ai) |
| **设计理念** | 大而全，开箱即用 |
| **特点** | 内置丰富，分类清晰 |

### 3.2 三层架构

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                    OpenClaw Skills 三层架构                                           │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  Layer 3: 垂直领域 (30+ 分类)                                                        │
│  ├── 飞书集成 (feishu-doc/wiki/bitable/chat)                                        │
│  ├── Apple 生态 (apple-notes/reminders/findmy/imessage)                             │
│  ├── 金融投资 (stock-analysis/portfolio-optimizer)                                   │
│  ├── 法律合规 (law-expert/contract/document, 18个)                                    │
│  └── 物联网 (spotify-player/openhue/sonoscli)                                      │
│                                                                                     │
│  Layer 2: 能力平台                                                                    │
│  ├── 开发类: github/gh-issues/coding-agent/skill-creator                           │
│  ├── 笔记类: obsidian/notion/apple-notes/bear-notes                                  │
│  ├── 任务类: things-mac/trello/cron                                                 │
│  ├── 通讯类: discord/slack/imsg/voice-call                                          │
│  └── 媒体类: excalidraw/stable-diffusion/image-generate                              │
│                                                                                     │
│  Layer 1: 基础设施                                                                    │
│  ├── coding-agent — 驱动 Codex/Claude Code 外部 AI 编程引擎                         │
│  ├── skill-creator — 创建/编辑/改进/审计 AgentSkills                                │
│  ├── self-improvement — 自进化记忆，持续改进                                          │
│  └── clawhub — 技能市场集成                                                          │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 3.3 核心 Skills 清单

**Layer 1: 基础设施**

| Skill | 描述 | 依赖 |
|-------|------|------|
| `coding-agent` | 委托 Codex/Claude Code 执行编码 | 外部 Agent |
| `skill-creator` | 创建新的 AgentSkills | - |
| `self-improvement` | 捕获错误、用户纠正到记忆 | - |
| `clawhub` | 技能市场搜索/安装/发布 | 网络 |

**Layer 2: 能力平台**

| Skill | 描述 | 分类 |
|-------|------|------|
| `github` | GitHub Issues/PR/CI 操作 | 开发 |
| `obsidian` | Obsidian 笔记库操作 | 笔记 |
| `notion` | Notion 数据库和页面 | 笔记 |
| `tavily-search` | 实时网络搜索 | 搜索 |
| `agent-reach` | 16+ 平台内容采集 | 搜索 |
| `excalidraw` | 手绘风格图表生成 | 创意 |
| `weather` | 天气预报 | 效率 |

**Layer 3: 垂直领域**

| Skill | 描述 | 分类 |
|-------|------|------|
| `feishu-doc/wiki/bitable` | 飞书全家桶 | 企业协作 |
| `stock-analysis` | 股票分析 | 金融 |
| `seven-dimension-analysis` | 七维度分析 | 金融 |
| `law-*` (18个) | 法律全场景 | 法律 |
| `openhue` | Philips Hue 控制 | 物联网 |

### 3.4 设计特点

**优势**：
- 内置 120+ Skills，开箱即用
- 墨家定制 Skills（金融、法律等）
- 完善的 CLI 工具链
- 技能市场丰富

**局限**：
- 部分 Skills 需要额外 API Key
- Layer 1 依赖外部 Agent（coding-agent）

---

## 4. Hermes Agent Skills 系统

### 4.1 定位

| 属性 | 值 |
|------|-----|
| **Skills 数量** | 80+ 内置 + 50+ 可选 |
| **市场** | Skills Hub (skills.hermesagent.io) |
| **设计理念** | 三层架构，递归委托 |
| **特点** | 原生支持 Agent 嵌套 |

### 4.2 三层架构（完整）

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                    Hermes Agent Skills 三层架构                                       │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  Layer 3: 垂直领域 (15+ 目录)                                                        │
│  ├── 🍎 Apple: apple-notes, apple-reminders, findmy, imessage                      │
│  ├── 🐙 GitHub: code-review, issues, pr-workflow, repo-management                  │
│  ├── 🎮 游戏: minecraft-modpack-server, pokemon-player                              │
│  ├── 🎭 媒体: gif-search, youtube-content, songsee                                 │
│  ├── 🏠 智能家居: openhue                                                          │
│  ├── 📱 社交媒体: xitter                                                            │
│  ├── 📝 笔记: obsidian                                                             │
│  └── 🛡️ 红队: godmode                                                             │
│                                                                                     │
│  Layer 2: 能力平台 (8 大类)                                                          │
│  ├── 🎨 Creative: excalidraw, manim-video, p5js, ascii-art, songwriting           │
│  ├── 💻 Software Dev: plan, tdd, code-review, requesting-code-review                │
│  ├── 🔍 Research: arxiv, blogwatcher, llm-wiki, research-paper-writing             │
│  ├── 📦 Productivity: notion, google-workspace, linear, powerpoint, ocr            │
│  ├── 🚀 MLOps: vllm, llama-cpp, transformers, peft, axolotl                       │
│  ├── 🛠️ DevOps: webhook-subscriptions                                              │
│  ├── 📧 Email: himalaya                                                             │
│  └── 🔬 Data Science: jupyter-live-kernel                                           │
│                                                                                     │
│  Layer 1: 基础设施 (3 大类)                                                          │
│  ├── 🤖 AI Agents: claude-code, codex, opencode, hermes-agent                       │
│  ├── 🔥 推理服务: inference-sh (150+ AI 应用)                                        │
│  └── 🔌 MCP: mcporter, native-mcp                                                 │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 4.3 Layer 1 详解

**AI Agents（4 个）**

| Skill | 来源 | 特点 |
|-------|------|------|
| `claude-code` | Anthropic | 深度推理 + MCP 支持 |
| `codex` | OpenAI | 轻量快速 + PR 专精 |
| `opencode` | 开源 | provider-agnostic + TUI |
| `hermes-agent` | Hermes 原生 | 递归委托 + 任务分解 |

**推理服务（10+ 个）**

| Skill | 描述 |
|-------|------|
| `vllm` | 生产级高吞吐推理 |
| `llama-cpp` | CPU/边缘推理 |
| `outlines` | 结构化输出 (JSON) |
| `guidance` | Grammar 精确控制 |
| `inference-sh` | 云平台 150+ 应用 |

**MCP（2 个）**

| Skill | 描述 |
|-------|------|
| `mcporter` | CLI 工具，ad-hoc 连接 |
| `native-mcp` | 配置驱动，持久集成 |

### 4.4 Layer 2 详解

**Creative (8 个)**

| Skill | 描述 |
|-------|------|
| `excalidraw` | 手绘图表 |
| `manim-video` | 数学动画 |
| `p5js` | 创意编程 |
| `ascii-art/video` | ASCII 艺术 |
| `songwriting-and-ai-music` | AI 音乐 |

**Software Development (6 个)**

| Skill | 描述 |
|-------|------|
| `plan` | 项目规划 |
| `test-driven-development` | TDD 开发 |
| `code-review` | 代码审查 |
| `requesting-code-review` | 请求审查 |
| `subagent-driven-development` | 子 Agent 开发 |
| `systematic-debugging` | 系统调试 |

**MLOps (25+ 个)**

| 分类 | Skills |
|------|--------|
| 推理 | vllm, llama-cpp, guidance, outlines, gguf |
| 模型 | audiocraft, clip, segment-anything, stable-diffusion, whisper |
| 训练 | axolotl, grpo-rl-training, peft, pytorch-fsdp, trl-fine-tuning, unsloth |
| 评估 | lm-evaluation-harness, weights-and-biases |
| 云 | modal, huggingface-hub |

### 4.5 设计特点

**优势**：
- 完整的三层架构设计
- 原生支持 Agent 递归委托
- MLOps 领域深度集成
- 自我进化能力

**局限**：
- 学习曲线较陡
- 部分 Skills 需要专业知识

---

## 5. OpenCode Skills 系统

### 5.1 定位

| 属性 | 值 |
|------|-----|
| **Skills 来源** | 社区生态 + OpenSkills |
| **兼容性** | provider-agnostic |
| **设计理念** | 开放生态，按需加载 |
| **特点** | 多模型支持，TUI 交互 |

### 5.2 三层架构

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                    OpenCode Skills 三层架构                                         │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  Layer 3: 垂直领域 — 依赖社区 Skills                                                  │
│  ├── GitHub 集成                                                                   │
│  ├── 数据库操作                                                                   │
│  └── 其他垂直场景                                                                  │
│                                                                                     │
│  Layer 2: 能力平台 — 依赖社区 Skills                                                  │
│  ├── 代码生成/审查                                                                 │
│  ├── 文档处理                                                                     │
│  └── 测试生成                                                                      │
│                                                                                     │
│  Layer 1: 基础设施                                                                   │
│  ├── OpenSkills — 通用 Skills 加载器                                                │
│  ├── 多模型支持 — OpenRouter, Anthropic, OpenAI, 本地模型                           │
│  └── MCP 集成 — 外部工具扩展                                                        │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 5.3 OpenSkills 加载器

```bash
# 安装 OpenSkills
npm install -g openskills

# 搜索 Skills
openskills search <keyword>

# 安装 Skills
openskills install <skill-name>

# 列出已安装
openskills list
```

### 5.4 设计特点

**优势**：
- provider-agnostic，不绑定厂商
- 丰富的社区生态
- 轻量级设计

**局限**：
- 无内置丰富 Skills
- 依赖社区贡献

---

## 6. 横向对比

### 6.1 三层架构完整度对比

| 层级 | Claude Code | OpenClaw | Hermes | OpenCode |
|------|-------------|----------|--------|----------|
| **Layer 1** | ❌ 无内置 | ✅ 3 个核心 | ✅ 3 大类完整 | ⚠️ OpenSkills |
| **Layer 2** | ⚠️ 少量 | ✅ 完整 | ✅ 完整 | ⚠️ 依赖社区 |
| **Layer 3** | ❌ 无内置 | ✅ 30+ 分类 | ✅ 15+ 目录 | ❌ 无 |
| **总数量** | 17+ | 120+ | 80+ 内置 | 依赖社区 |

### 6.2 核心能力对比

| 能力 | Claude Code | OpenClaw | Hermes | OpenCode |
|------|-------------|----------|--------|----------|
| **AI 代理委托** | ⚠️ 有限 | ✅ coding-agent | ✅ 原生嵌套 | ✅ 完整 |
| **自进化** | ❌ | ⚠️ self-improvement | ✅ SkillClaw | ❌ |
| **MCP 集成** | ✅ | ⚠️ mcporter | ✅ mcporter/native | ✅ |
| **技能市场** | 社区 | ClawHub (13k+) | Skills Hub | OpenSkills |
| **MLOps 集成** | ❌ | ⚠️ 少量 | ✅ 25+ | ❌ |

### 6.3 设计理念对比

| 维度 | Claude Code | OpenClaw | Hermes | OpenCode |
|------|-------------|----------|--------|----------|
| **核心理念** | 少而精 | 大而全 | 三层架构 | 开放生态 |
| **内置数量** | 少 | 多 | 中等 | 极少 |
| **扩展方式** | 社区 | 官方市场 | 官方+可选 | 社区 |
| **学习曲线** | 低 | 中 | 高 | 低 |
| **适用场景** | 通用编程 | 企业/专业 | MLOps/研究 | 通用 |

---

## 7. 选择指南

### 7.1 按场景选择

| 场景 | 推荐 | 理由 |
|------|------|------|
| **通用软件开发** | Claude Code | 官方支持，质量有保障 |
| **企业应用/飞书集成** | OpenClaw | 丰富的企业集成 |
| **ML/AI 研究** | Hermes Agent | 深度 MLOps 集成 |
| **多模型切换** | OpenCode | provider-agnostic |
| **金融/法律专业** | OpenClaw | 墨家定制 Skills |
| **快速上手** | Claude Code | 少而精，简单 |

### 7.2 Skills 组合建议

```
通用开发 → Claude Code + code-review + test
       → 或 OpenClaw + github + coding-agent

企业场景 → OpenClaw + feishu-* + notion + law-*

ML/AI 研究 → Hermes Agent + mlops/* + inference-sh

多模型 → OpenCode + OpenSkills
```

---

## 8. 相关资源

| 资源 | 链接 |
|------|------|
| Anthropic Skills | [GitHub](https://github.com/anthropics/skills) |
| OpenClaw 文档 | [docs.openclaw.ai](https://docs.openclaw.ai) |
| Hermes Skills Hub | [skills.hermesagent.io](https://skills.hermesagent.io) |
| OpenSkills | [GitHub](https://github.com/numman-ali/openskills) |

---

## 9. 更新日志

| 日期 | 更新内容 |
|------|---------|
| 2026-04-21 | 新增四大 Agentic Tools 三层架构对比 |

---

*整理：墨鉴 | 2026-04-21*
