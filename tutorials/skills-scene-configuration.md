# Skills 场景配置指南

> **适合人群**：想为不同 Agentic Tool 配置最佳 Skills 组合的开发者
> **预计阅读时间**：35 分钟
> **更新日期**：2026-04-21

---

## 1. 场景配置概述

### 1.1 什么是场景配置

场景配置是将 Skills 按照**三层架构**组织成可复用组合的方式，让 AI Agent 在特定场景下发挥最佳效果：

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                          Skills 场景配置体系                                         │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  场景 Skill 组合                                                                    │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  场景层 (Scene) — 垂直领域组合                                                │   │
│  │  如：金融分析、游戏开发、数据科学                                              │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                    │                                                │
│  任务 Skill 组合                                                                    │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  任务层 (Task) — 能力平台组合                                                │   │
│  │  如：代码审查、测试生成、文档编写                                              │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                    │                                                │
│  基础 Skill 组合                                                                    │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │  基础层 (Base) — 基础设施技能                                                │   │
│  │  如：AI 代理、推理服务、MCP                                                  │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 三层组合关系

| 层级 | 定位 | 作用 | 示例 |
|------|------|------|------|
| **基础层** | 驱动引擎 | 提供核心 AI 能力 | AI 代理、推理服务、MCP |
| **任务层** | 能力平台 | 封装通用能力 | 代码审查、测试生成、文档 |
| **场景层** | 垂直领域 | 深度集成特定场景 | 金融分析、游戏开发、数据科学 |

---

## 2. Claude Code 场景配置

### 2.1 基础配置

**Layer 1: 基础设施**

```bash
# 基础 Skills（内置）
- Read, Write, Bash, Grep
- WebFetch, WebSearch
- Agent, Task
- MCP (外部扩展)
```

**推荐 Layer 1 扩展**

| Skill | 来源 | 用途 |
|-------|------|------|
| `coding-agent` | 第三方 | 驱动 Codex 外部 AI |
| `claude-code` | Anthropic | 深度推理 + MCP |

### 2.2 任务配置

**通用开发任务**

```yaml
任务组合: 通用软件开发
├── Layer 2 (任务层)
│   ├── code-review      # 代码审查
│   ├── test            # 测试生成
│   ├── docs            # 文档编写
│   └── debug           # 调试辅助
└── Layer 3 (场景层)
    └── (按需添加)
```

**安装命令**

```bash
claude skills install anthropics/skills/code-review
claude skills install anthropics/skills/test
claude skills install anthropics/skills/docs
claude skills install anthropics/skills/debug
```

### 2.3 场景配置

**场景 1: 严肃软件开发**

推荐组合：**Claude Code + Superpowers**

| 层级 | Skill | 用途 |
|------|-------|------|
| **Layer 2** | `brainstorming` | 头脑风暴 |
| | `writing-plans` | 项目规划 |
| | `test-driven-development` | TDD 开发 |
| | `systematic-debugging` | 系统调试 |
| **Layer 1** | `subagent-driven-development` | 子 Agent 开发 |
| | `requesting-code-review` | 请求审查 |
| | `receiving-code-review` | 接收审查 |

```bash
# 安装 Superpowers
git clone https://github.com/obra/superpowers ~/.claude/skills/superpowers
```

**场景 2: 快速修复**

| 层级 | Skill | 用途 |
|------|-------|------|
| **Layer 2** | `debug` | 调试定位 |
| | `refactor` | 重构建议 |
| **Layer 1** | 内置工具 | 文件操作 |

**场景 3: 文档驱动开发**

| 层级 | Skill | 用途 |
|------|-------|------|
| **Layer 2** | `docs` | 文档生成 |
| | `writing-plans` | 规划编写 |
| **Layer 3** | `design-md` | DESIGN.md 设计系统 |

---

## 3. OpenClaw 场景配置

### 3.1 基础配置

**Layer 1: 基础设施**

| Skill | 描述 | 用途 |
|-------|------|------|
| `coding-agent` | 驱动外部 AI 编程引擎 | Codex/Claude Code |
| `skill-creator` | 创建/编辑/改进 Skills | 技能开发 |
| `self-improvement` | 自进化记忆 | 持续改进 |
| `clawhub` | 技能市场集成 | 搜索/安装/发布 |

### 3.2 任务配置

**企业协作任务**

```yaml
任务组合: 企业协作
├── Layer 2 (任务层)
│   ├── github           # GitHub Issues/PR/CI
│   ├── notion           # Notion 数据库和页面
│   ├── obsidian         # Obsidian 笔记库
│   └── cron             # 定时任务
└── Layer 3 (场景层)
    ├── feishu-doc       # 飞书文档
    ├── feishu-wiki      # 飞书 Wiki
    └── feishu-bitable   # 飞书多维表格
```

**安装命令**

```bash
clawhub install openclaw/github
clawhub install openclaw/notion
clawhub install openclaw/obsidian
clawhub install openclaw/feishu-doc
clawhub install openclaw/feishu-wiki
```

### 3.3 场景配置

**场景 1: 企业应用开发**

| 层级 | Skill | 用途 |
|------|-------|------|
| **Layer 1** | `coding-agent` | AI 编程引擎 |
| **Layer 2** | `github`, `coding-agent` | 开发流程 |
| **Layer 3** | `feishu-doc`, `notion`, `law-*` | 企业集成 |

**完整组合命令**

```bash
# 基础层
clawhub install openclaw/coding-agent
clawhub install openclaw/skill-creator

# 任务层
clawhub install openclaw/github
clawhub install openclaw/obsidian
clawhub install openclaw/notion

# 场景层 - 飞书集成
clawhub install openclaw/feishu-doc
clawhub install openclaw/feishu-wiki
clawhub install openclaw/feishu-bitable
clawhub install openclaw/feishu-chat

# 场景层 - 法律合规（OpenClaw 特色）
clawhub install openclaw/law-expert
clawhub install openclaw/contract-review
```

**场景 2: 金融投资分析**

| 层级 | Skill | 用途 |
|------|-------|------|
| **Layer 2** | `tavily-search` | 实时搜索 |
| **Layer 3** | `stock-analysis` | 股票分析 |
| | `portfolio-optimizer` | 组合优化 |
| | `seven-dimension-analysis` | 七维度分析 |

**完整组合命令**

```bash
# 任务层
clawhub install openclaw/tavily-search
clawhub install openclaw/agent-reach

# 场景层 - 金融
clawhub install openclaw/stock-analysis
clawhub install openclaw/portfolio-optimizer
clawhub install openclaw/seven-dimension-analysis
```

**场景 3: 智能家居控制**

| 层级 | Skill | 用途 |
|------|-------|------|
| **Layer 2** | `spotify-player` | 音乐控制 |
| **Layer 3** | `openhue` | Philips Hue |
| | `sonoscli` | Sonos 音箱 |

---

## 4. Hermes Agent 场景配置

### 4.1 基础配置

**Layer 1: 基础设施**

| Skill | 来源 | 特点 |
|-------|------|------|
| `claude-code` | Anthropic | 深度推理 + MCP |
| `codex` | OpenAI | 轻量快速 + PR 专精 |
| `opencode` | 开源 | provider-agnostic |
| `hermes-agent` | Hermes 原生 | 递归委托 + 任务分解 |

**推理服务**

| Skill | 用途 |
|-------|------|
| `vllm` | 生产级高吞吐推理 |
| `llama-cpp` | CPU/边缘推理 |
| `outlines` | 结构化输出 (JSON) |
| `guidance` | Grammar 精确控制 |
| `inference-sh` | 云平台 150+ 应用 |

### 4.2 任务配置

**MLOps 任务**

```yaml
任务组合: MLOps
├── Layer 2 (任务层)
│   ├── vllm                    # 推理服务
│   ├── llama-cpp               # 模型推理
│   ├── transformers            # 模型加载
│   ├── peft                    # 微调训练
│   └── lm-evaluation-harness   # 评估
└── Layer 1 (基础层)
    └── inference-sh            # 推理平台
```

**完整组合命令**

```bash
# 基础层
hermes skills install autonomous-ai-agents/claude-code
hermes skills install inference-sh/vllm
hermes skills install inference-sh/llama-cpp

# 任务层
hermes skills install mlops/transformers
hermes skills install mlops/peft
hermes skills install mlops/axolotl
hermes skills install mlops/trl-fine-tuning
```

### 4.3 场景配置

**场景 1: AI/ML 研究**

| 层级 | Skill | 用途 |
|------|-------|------|
| **Layer 1** | `inference-sh` | 推理平台 |
| **Layer 2** | `arxiv`, `llm-wiki`, `research-paper-writing` | 研究工具 |
| **Layer 3** | `mlops/*` | MLOps 集成 |

**完整组合命令**

```bash
# 基础层
hermes skills install autonomous-ai-agents/hermes-agent
hermes skills install inference-sh/inference-sh

# 任务层 - Research
hermes skills install research/arxiv
hermes skills install research/blogwatcher
hermes skills install research/llm-wiki
hermes skills install research/research-paper-writing

# 任务层 - MLOps
hermes skills install mlops/vllm
hermes skills install mlops/llama-cpp
hermes skills install mlops/transformers
hermes skills install mlops/peft
```

**场景 2: 创意开发**

| 层级 | Skill | 用途 |
|------|-------|------|
| **Layer 2** | `excalidraw` | 手绘图表 |
| | `manim-video` | 数学动画 |
| | `p5js` | 创意编程 |
| **Layer 3** | `ascii-art/video` | ASCII 艺术 |
| | `songwriting-and-ai-music` | AI 音乐 |

**完整组合命令**

```bash
# 任务层 - Creative
hermes skills install creative/excalidraw
hermes skills install creative/manim-video
hermes skills install creative/p5js
hermes skills install creative/ascii-art

# 场景层
hermes skills install creative/songwriting-and-ai-music
```

**场景 3: Apple 生态集成**

| 层级 | Skill | 用途 |
|------|-------|------|
| **Layer 2** | `apple-notes` | 笔记同步 |
| **Layer 3** | `apple-reminders` | 提醒事项 |
| | `findmy` | 查找设备 |
| | `imessage` | 即时消息 |

---

## 5. OpenCode 场景配置

### 5.1 基础配置

**Layer 1: 基础设施**

| 组件 | 描述 |
|------|------|
| OpenSkills | 通用 Skills 加载器 |
| 多模型支持 | OpenRouter, Anthropic, OpenAI, 本地模型 |
| MCP 集成 | 外部工具扩展 |

**内置 Agents**

| Agent | Type | Purpose |
|-------|------|---------|
| `build` | primary | 默认开发 agent |
| `plan` | primary | 规划分析 |
| `general` | subagent | 通用研究 |
| `explore` | subagent | 代码探索 |

### 5.2 任务配置

**内置 Skills**

| Skill | 用途 |
|-------|------|
| `git-master` | Git 专家 |
| `playwright` | E2E 测试 |
| `agent-browser` | 浏览器自动化 |

### 5.3 场景配置

**场景 1: Web 开发**

```bash
# 安装 Web 开发 Skills
openskills install playwright
openskills install agent-browser

# 配置 build agent
opencode config set agent.build.tools playwright,agent-browser
```

**场景 2: 多模型研究**

```bash
# 安装 OpenSkills
npm install -g openskills

# 搜索并安装 Skills
openskills search context-engineering
openskills install context-engineering-kit
```

---

## 6. 场景化技能矩阵

### 6.1 通用开发场景

| 场景 | Claude Code | OpenClaw | Hermes | OpenCode |
|------|-------------|----------|--------|----------|
| **基础开发** | code-review + test + docs | github + coding-agent | plan + tdd + code-review | git-master + playwright |
| **快速修复** | debug + refactor | github + debug | systematic-debugging | 内置 |
| **代码审查** | code-review | github + code-review | code-review + requesting | git-master |
| **文档驱动** | docs + writing-plans | obsidian + notion | docs + research | 内置 |

### 6.2 企业场景

| 场景 | Claude Code | OpenClaw | Hermes | OpenCode |
|------|-------------|----------|--------|----------|
| **飞书集成** | (需 MCP) | feishu-* 全家桶 | (需 MCP) | (需 MCP) |
| **Notion** | (需第三方) | notion + obsidian | notion | (需第三方) |
| **法律合规** | (需第三方) | law-* 18个 | (需第三方) | (需第三方) |

### 6.3 专业场景

| 场景 | Claude Code | OpenClaw | Hermes | OpenCode |
|------|-------------|----------|--------|----------|
| **ML/AI 研究** | (有限) | (有限) | **mlops/* 25+** | (需社区) |
| **金融分析** | (需第三方) | **stock-analysis** | (有限) | (需社区) |
| **游戏开发** | (需第三方) | (有限) | gaming/* | (需社区) |
| **Apple 生态** | (需 MCP) | apple-* | **apple-* 全家桶** | (需社区) |

---

## 7. 快速启动模板

### 7.1 通用软件开发模板

```bash
# Claude Code
claude skills install anthropics/skills/code-review
claude skills install anthropics/skills/test
claude skills install anthropics/skills/docs

# Superpowers (高级)
git clone https://github.com/obra/superpowers ~/.claude/skills/superpowers
```

### 7.2 企业开发模板

```bash
# OpenClaw
clawhub install openclaw/coding-agent
clawhub install openclaw/github
clawhub install openclaw/feishu-doc
clawhub install openclaw/feishu-wiki
clawhub install openclaw/law-expert
```

### 7.3 MLOps 研究模板

```bash
# Hermes Agent
hermes skills install autonomous-ai-agents/hermes-agent
hermes skills install inference-sh/vllm
hermes skills install mlops/transformers
hermes skills install mlops/peft
hermes skills install mlops/axolotl
hermes skills install research/arxiv
```

### 7.4 创意开发模板

```bash
# Hermes Agent
hermes skills install creative/excalidraw
hermes skills install creative/manim-video
hermes skills install creative/p5js
hermes skills install software-development/plan
```

---

## 8. 配置决策树

### 8.1 选择流程

```
你是谁？
│
├─→ 独立开发者
│   └─→ 主要语言？
│       ├─→ Python/数据科学 → Hermes + mlops/*
│       └─→ 通用编程 → Claude Code + Superpowers
│
├─→ 企业团队
│   └─→ 主要平台？
│       ├─→ 飞书 → OpenClaw + feishu-*
│       ├─→ Notion → OpenClaw + notion
│       └─→ GitHub → 各平台都支持
│
├─→ 研究人员
│   └─→ 研究方向？
│       ├─→ ML/AI → Hermes + mlops/* + research/*
│       ├─→ 学术写作 → Hermes + research/*
│       └─→ 数据分析 → Hermes + data-science/*
│
└─→ 创作者
    └─→ 创作类型？
        ├─→ 视频/动画 → Hermes + creative/*
        ├─→ 音乐 → Hermes + songwriting
        └─→ 游戏 → Hermes + gaming/*
```

### 8.2 Skill 数量与质量平衡

| 平台 | 理念 | 推荐策略 |
|------|------|----------|
| **Claude Code** | 少而精 | 安装 3-5 个核心 Skills，避免堆砌 |
| **OpenClaw** | 大而全 | 按需安装，企业场景全套 |
| **Hermes** | 三层架构 | 基础层固定 + 按场景叠加 |
| **OpenCode** | 开放生态 | 从社区精选，避免污染 |

---

## 9. 相关资源

| 资源 | 链接 |
|------|------|
| Superpowers | [GitHub](https://github.com/obra/superpowers) |
| ClawHub | [clawhub.ai](https://clawhub.ai/skills) |
| Hermes Skills Hub | [skills.hermesagent.io](https://skills.hermesagent.io) |
| OpenSkills | [GitHub](https://github.com/numman-ali/openskills) |

---

## 10. 更新日志

| 日期 | 更新内容 |
|------|----------|
| 2026-04-21 | 新增 Skills 场景配置指南，含决策树和快速启动模板 |

---

*整理：墨鉴 | 2026-04-21*
