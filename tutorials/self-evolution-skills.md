# Agent Self-Evolution Skills 深度教程

> **适合人群**：AI Agent 开发者、Prompt Engineer、LLM 应用架构师
> **预计阅读时间**：50 分钟
> **前置要求**：了解 AI Agent 基本概念，熟悉 SKILL.md 格式，有 LLM API 使用经验
> **核心项目**：Evolver（EvoMap）、SkillClaw、SkillAnything、Hermes Agent

---

## 1. 概述

### 1.1 什么是 Agent Self-Evolution？

Agent Self-Evolution（智能体自进化）是指 AI Agent 从真实交互经验中自动提取、优化和积累 Skills 的能力，使 Agent 随时间持续变强，而无需人工干预每一个改进过程。

**核心区别：**

| 模式 | 描述 | 代表项目 |
|------|------|----------|
| 手工调优（Manual Tuning） | 人类手动写 prompt，逐次迭代 | 传统 prompt engineering |
| 自进化（Self-Evolution） | Agent 从日志/经验中自动提取改进信号，生成可复用进化资产 | Evolver、SkillClaw |
| 自动生成（Auto-Generation） | 从任意目标（CLI/API/库）自动生成 Skills | SkillAnything |

### 1.2 Self-Evolution 赛道现状（2026-04）

```
Self-Evolution 生态
├── 🔬 Evolver (EvoMap)     — 5,630⭐ GEP 协议 + 基因组进化引擎
├── 🦁 SkillClaw            — 765⭐ 群体技能进化（HuggingFace 当日第2）
├── 🎯 SkillAnything         — 180⭐ 7相自动工厂，从任意目标生成 Skills
├── 🐝 Hermes Agent          — Nous Research 自进化 Agent 生态
└── 📦 SkillAnything         — 元技能（Skills 的 Skills）
```

### 1.3 三种进化范式

```
范式 1: 基因组进化 (Genome Evolution)
  日志 → Signal → Gene/Capsule → GEP Prompt → 进化
  代表: Evolver (GEP 协议)
  
范式 2: 群体进化 (Collective Evolution)
  多 Agent/多用户 → 会话数据 → Skill 聚合 → 去重/提质 → 共享技能库
  代表: SkillClaw
  
范式 3: 自动生成 (Auto-Generation)
  任意目标(CLI/API/库) → 7相管线 → 多平台 Skills
  代表: SkillAnything
```

---

## 2. Evolver — GEP 协议驱动的自进化引擎

### 2.1 核心概念

Evolver 是 EvoMap 生态的核心引擎，通过 **GEP（Genome Evolution Protocol，基因组进化协议）** 将 Agent 的改进过程从零散的 prompt 调优升级为可审计、可复用、有版本历史的系统性进化。

**三个核心概念：**

- **Gene（基因）**：最小的可复用进化单元，对应一个具体的改进策略
- **Capsule（胶囊）**：多个 Gene 的组合，对应复杂场景的完整解决方案
- **EvolutionEvent（进化事件）**：每次进化的审计记录，包含信号、决策、执行结果

### 2.2 安装配置

```bash
# Node.js >= 18 + Git（必需，Evolver 依赖 git 做回滚和 blast radius 计算）
npm install -g @evomap/evolver
evolver --help
```

**平台集成（每个平台只需执行一次）：**

```bash
# Cursor
evolver setup-hooks --platform=cursor

# Claude Code
evolver setup-hooks --platform=claude-code

# OpenClaw（无需 hooks，通过 stdout 协议自动集成）
cd <your-openclaw-workspace>
git clone https://github.com/EvoMap/evolver.git
cd evolver && npm install
# 在 OpenClaw 会话内运行即可
```

**可选：连接 EvoMap Hub（用于技能商店和 Worker 池）**

```bash
# 在项目根目录创建 .env
A2A_HUB_URL=https://evomap.ai
A2A_NODE_ID=your_node_id_here  # 在 https://evomap.ai 注册获得
```

### 2.3 核心使用

```bash
# 标准运行：扫描日志、选择 Gene、输出 GEP Prompt
node index.js

# 审查模式：暂停等待人工确认后再应用
node index.js --review

# 持续循环：后台守护进程模式
node index.js --loop

# 连接到 Hub 并启用 Worker
WORKER_ENABLED=1 node index.js --loop
# 然后在 https://evomap.ai 打开 Worker 开关
```

### 2.4 GEP 协议资产

Evolver 内置结构化资产目录 `assets/gep/`：

```json
// assets/gep/genes.json — Gene 库（最小进化单元）
[
  {
    "id": "gene-http-retry",
    "name": "HTTP 重试策略",
    "signals": ["ECONNREFUSED", "timeout", "429"],
    "action": "在 HTTP 请求中添加指数退避重试",
    "validation": ["npm test"],
    "personality_delta": "+cautious"
  }
]

// assets/gep/capsules.json — Capsule 库（Gene 组合）
[
  {
    "id": "capsule-fullstack-debug",
    "genes": ["gene-http-retry", "gene-sql-injection-check"],
    "scenario": "全栈应用调试完整流程"
  }
]

// assets/gep/events.jsonl — 进化事件审计日志（JSONL 格式）
{"timestamp":"2026-04-20T10:00:00Z","gene":"gene-http-retry","signal":"timeout","action":"applied","verified":true}
```

### 2.5 基因组 Selector（选择器）

当 Evolver 分析日志时，Selector 负责：

1. 从日志中提取 `signals`（失败模式、错误类型、性能指标）
2. 在 Gene/Capsule 库中匹配最相关的资产
3. 输出可审计的决策 JSON

```javascript
// Selector 决策示例
{
  "signal": "HTTP 429 Rate Limit",
  "matched_genes": ["gene-http-retry", "gene-rate-limit-aware"],
  "selected": "gene-http-retry",
  "reason": "信号匹配度 0.92 > 阈值 0.7",
  "gep_prompt": "请在 HTTP 请求中添加指数退避重试策略..."
}
```

### 2.6 进化策略配置

| 策略 | 行为 | 适用场景 |
|------|------|----------|
| `balanced`（默认） | 创新与修复平衡 | 日常使用 |
| `innovate` | 优先探索新方法 | 探索阶段 |
| `harden` | 优先稳定性验证 | 生产环境 |
| `repair-only` | 仅修复已知问题 | 紧急修复 |

```bash
EVOLVE_STRATEGY=harden node index.js
```

### 2.7 安全模型

| 约束 | 说明 |
|------|------|
| Gene Validation 命令白名单 | 仅允许 `node`/`npm`/`npx` 开头命令 |
| 反引号/`$(...)` 拒绝 | 防止命令注入 |
| Shell 操作符禁止 | 去除后 `;`/`&`/`\|`/`>`/`<` 均被拒绝 |
| 180 秒超时 | 每条 validation 命令最多执行 3 分钟 |
| 单进程锁 | 禁止生成子进化进程（防 Fork 炸弹） |
| 稳定性优先 | 错误率高时强制进入修复模式 |

### 2.8 与 OpenClaw 集成

```javascript
// 在 OpenClaw 会话中调用 Evolver
sessions_spawn(runtime="subagent", task="运行 evolver 分析本会话日志，输出改进建议")

// Evolver 会通过 stdout 输出 sessions_spawn 指令
// OpenClaw 宿主自动识别并执行后续动作
```

---

## 3. SkillClaw — 群体技能进化框架

### 3.1 核心思想

SkillClaw 的核心洞察：**一个用户的经验价值有限，当 N 个用户共享同一个进化循环时，每个人的经验都在相互叠加。**

```
传统模式：
  User A 踩坑数据库调试 → 经验丢失
  User B 踩同坑         → 经验再次丢失
  User C 踩同坑         → 经验第三次丢失

SkillClaw 模式：
  User A 踩坑数据库调试 → SkillClaw 进化 → 技能写入共享库
  User B → 直接使用优化后的技能 → 零踩坑
  User C → 直接使用优化后的技能 → 零踩坑
```

### 3.2 系统架构

```
┌─────────────────────────────────────────────────────────────┐
│                    SkillClaw Architecture                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────┐    ┌───────────────────────────────────┐  │
│  │ Hermes Agent │    │         Hermes Agent              │  │
│  │ (Frontend)   │    │         (Backend)                 │  │
│  └──────┬───────┘    └──────────────┬───────────────────┘  │
│         │                           │                      │
│         ▼                           ▼                      │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Client Proxy (本地 API 代理)              │  │
│  │  /v1/chat/completions  /v1/messages                   │  │
│  │  拦截请求 → 记录会话 → 管理本地技能库                    │  │
│  └──────────────────────┬───────────────────────────────┘  │
│                         │                                   │
│                         ▼                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              共享存储 (OSS / S3 / Local)              │  │
│  │  session_data/  ← 原始会话日志                         │  │
│  │  skills/        ← 进化的 Skills (SKILL.md)            │  │
│  └──────────────────────┬───────────────────────────────┘  │
│                         │                                   │
│                         ▼                                   │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              Evolve Server (可选)                      │  │
│  │  workflow engine: Summarize → Aggregate → Execute       │  │
│  │  agent engine: OpenClaw-driven 自主编辑                │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 安装部署

**macOS / Linux：**

```bash
git clone https://github.com/AMAP-ML/SkillClaw.git && cd SkillClaw
bash scripts/install_skillclaw.sh
source .venv/bin/activate
```

**Windows：**

```powershell
git clone https://github.com/AMAP-ML/SkillClaw.git
cd SkillClaw
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
python -m pip install -e ".[evolve,sharing,server]"
```

**初始化：**

```bash
skillclaw setup
skillclaw start --daemon
```

### 3.4 两种部署模式

**模式 1：单人 + 自动演化**

```
Client Proxy（本地） + Evolve Server（本地或远程）→ 技能在后台自动精炼
```

**模式 2：团队共享群组**

```
Client A ─┐
Client B ─┤→ 共享存储 → 1个 Evolve Server → 所有客户端受益
Client C ─┘
```

### 3.5 Evolve Server 引擎

| 引擎 | 描述 | 适用场景 |
|------|------|----------|
| `workflow` | 固定 3 阶段 LLM 流程（Summarize → Aggregate → Execute） | 轻量自动化 |
| `agent` | OpenClaw 驱动的自主 Agent 工作区，直接编辑 SKILL.md | 复杂场景 |

### 3.6 支持的平台

```
原生支持：
  ✅ Hermes Agent (Nous Research)
  ✅ OpenClaw
  ✅ QwenPaw
  ✅ IronClaw
  ✅ PicoClaw
  ✅ ZeroClaw
  ✅ NanoClaw
  ✅ NemoClaw
  ✅ 任何 OpenAI 兼容 API
```

### 3.7 跨 Agent 技能共享

```
没有 SkillClaw：
  Agent A (Frontend) → 独立技能库（React 模式）
  Agent B (Backend) → 独立技能库（API 设计模式）
  → 两边无法互相学习

有 SkillClaw：
  Agent A 学到 React 最佳实践 → 共享给所有 Agent
  Agent B 学到 API 设计模式 → 共享给所有 Agent
  → 技能交叉融合，经验指数叠加
```

---

## 4. SkillAnything — 从任意目标自动生成 Skills

### 4.1 核心思想

SkillAnything 是一个**元技能（Meta-Skill）**——给它任意目标（CLI 工具、REST API、Python 库），它自动运行 7 相管线，输出多平台可用的 Skills。

```
输入: "jq"
       ↓
7相管线
       ↓
输出: dist/
      ├── claude-code/   (SKILL.md + hooks)
      ├── openclaw/      (SKILL.md + settings.json)
      ├── codex/         (SKILL.md + openai.yaml)
      └── generic/       (平台无关 .skill zip)
```

### 4.2 7 相管线详解

| 阶段 | 名称 | 输入 | 输出 |
|:----:|------|------|------|
| 1 | **Analyze** | 目标（CLI/API/库） | `analysis.json`（能力提取） |
| 2 | **Design** | `analysis.json` | `architecture.json`（技能架构） |
| 3 | **Implement** | `architecture.json` | 完整 Skill 目录 |
| 4 | **Test Plan** | 分析 + Skill | `evals.json`（评估用例） |
| 5 | **Evaluate** | `evals.json` + Skill | `benchmark.json`（对比评分） |
| 6 | **Optimize** | 触发评估 + Skill | 优化后的 SKILL.md |
| 7 | **Package** | 最终 Skill | `dist/各平台包` |

### 4.3 目标自动检测

| 目标类型 | 检测方法 | 示例 |
|----------|----------|------|
| CLI 工具 | `which <name>` + `--help` 解析 | `jq`, `httpie`, `ffmpeg` |
| REST API | URL + OpenAPI/Swagger spec | Stripe API, GitHub API |
| Python 库 | pip/npm 包名 | `pandas`, `lodash` |
| 工作流 | 步骤描述 | ETL pipeline, CI/CD |
| Web 服务 | URL + 网页文档 | Slack, Notion |

### 4.4 安装使用

```bash
# 安装到各平台
git clone https://github.com/AgentSkillOS/SkillAnything.git ~/.claude/skills/skill-anything

# 在 Claude Code 中直接对话
> Create a skill for the httpie CLI tool
> Generate a multi-platform skill for the Stripe API
> Turn this data pipeline workflow into a skill

# 分相运行（精细控制）
python -m scripts.analyze_target --target "jq" --output analysis.json
python -m scripts.design_skill --analysis analysis.json --output architecture.json
python -m scripts.package_multiplatform ./out/my-skill --platforms claude-code,openclaw,codex
```

### 4.5 输出结构

```
dist/my-skill/
├── SKILL.md              # 主入口
├── triggers/
│   └── eval_cases.json   # 触发评估用例
├── scripts/
│   └── examples.sh       # 示例脚本
├── docs/
│   └── reference.md      # 参考文档
├── platforms/
│   ├── claude-code/      # Claude Code 专用
│   ├── openclaw/         # OpenClaw 专用
│   └── codex/            # Codex 专用
└── generic/
    └── my-skill.skill     # 平台无关包
```

---

## 5. Hermes Agent 生态

### 5.1 Hermes 简介

Hermes（[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)）是 Nous Research 开发的高能力 Agent，特点是内置自进化能力，与 SkillClaw 深度集成。

**与 Evolver 的关系：** EvoMap 官方指控 Hermes Agent 的自进化设计"高度相似"于 Evolver，未作归属声明。详见 [EvoMap 官方分析](https://evomap.ai/zh/blog/hermes-agent-evolver-similarity-analysis)。

### 5.2 Hermes + SkillClaw 集成

```bash
# 安装 Hermes 后，安装 SkillClaw
bash scripts/install_skillclaw.sh
skillclaw setup
skillclaw start --daemon

# 从此 Hermes 的所有会话都会自动记录并驱动 SkillClaw 进化
```

### 5.3 Hermes 生态工具地图

`ksimback/hermes-ecosystem`（501⭐）整理了 Hermes Agent 的完整生态工具地图：

| 类别 | 工具 |
|------|------|
| 记忆系统 | 持久化记忆、跨会话上下文 |
| 技能管理 | SkillClaw、OpenClaw Skills |
| 进化引擎 | Evolver GEP 协议 |
| 评估框架 | 多维度 Agent 性能评测 |

---

## 6. 横向对比与选型

### 6.1 三大框架对比

| 维度 | Evolver | SkillClaw | SkillAnything |
|------|---------|-----------|---------------|
| **核心功能** | GEP 协议驱动进化 | 群体技能进化 | 自动生成 Skills |
| **输入** | 日志/记忆文件 | 多 Agent 会话数据 | 任意目标（CLI/API/库） |
| **输出** | GEP Prompt + Gene/Capsule | 进化的 SKILL.md | 多平台 Skill 包 |
| **平台集成** | Cursor/Claude Code/OpenClaw | Hermes/OpenClaw/多 Agent | Claude Code/OpenClaw/Codex |
| **协作模式** | 独立 + 可选 Hub | 单人/团队共享 | 独立 |
| **许可证** | GPL-3.0（源码可见） | MIT | MIT |
| **⭐ 数量** | 5,630 | 765 | 180 |
| **适合场景** | 需要审计追溯的进化 | 团队经验共享 | 快速生成新领域 Skills |

### 6.2 选型决策树

```
需要让 Agent 自动进化吗？
  │
  ├─ 是 → 多人/多 Agent 协作？
  │         │
  │         ├─ 是 → SkillClaw（群体进化，经验共享）
  │         │
  │         └─ 否 → 需要可审计的进化记录？
  │                   │
  │                   ├─ 是 → Evolver（GEP 协议 + 基因组）
  │                   │
  │                   └─ 否 → 其他自进化方案
  │
  └─ 否 → 需要从零生成 Skills？
            │
            ├─ 是 → SkillAnything（7相自动工厂）
            │
            └─ 否 → 传统手工编写 SKILL.md
```

---

## 7. 组合应用实战

### 7.1 场景：团队 AI Coding Agent 进化体系

```
┌─────────────────────────────────────────────────────────┐
│              团队 AI Agent 进化体系                       │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  第1层：SkillAnything（快速生成）                          │
│  新技术栈 → SkillAnything → 基础 Skills                  │
│                                                          │
│  第2层：SkillClaw（团队共享进化）                          │
│  各成员 Agent → 会话数据 → 共享存储 → Evolve Server       │
│  → 去重/提质 → 团队统一技能库                              │
│                                                          │
│  第3层：Evolver（深度进化 + 审计）                         │
│  持续失败模式 → Gene/Capsule 积累 → GEP 协议审计          │
│                                                          │
│  第4层：EvoMap Hub（可选网络效应）                         │
│  跨团队/跨组织技能市场 → 验证者共识                        │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### 7.2 实施步骤

**Step 1：用 SkillAnything 快速初始化**

```bash
# 为团队常用工具批量生成 Skills
skill-anything --target "postgresql CLI"
skill-anything --target "docker"
skill-anything --target "kubectl"
skill-anything --target "gh cli"
```

**Step 2：用 SkillClaw 建立团队进化循环**

```bash
# 部署 SkillClaw 团队版
skillclaw setup --shared-storage s3://team-skills/
skillclaw-evolve-server --engine workflow
```

**Step 3：用 Evolver 做深度进化 + 审计**

```bash
# 在关键项目目录集成 Evolver
cd my-project
git clone https://github.com/EvoMap/evolver.git
EVOLVE_STRATEGY=harden node evolver/index.js --review
```

---

## 8. 最佳实践

### 8.1 进化资产积累

```
✅ 做：
  - 从失败日志中提取 Gene，不要只记录"哪里错了"，要记录"如何修复"
  - Gene 命名规范：gene-<场景>-<动作>（如 gene-http-retry、gene-sql-injection-check）
  - 每个 EvolutionEvent 都要记录 signal + selected_gene + action

❌ 避免：
  - 把整个 prompt 作为一个 Gene（太粗粒度，无法复用）
  - 不记录 EvolutionEvent（失去审计能力）
  - Gene validation 命令不加超时（可能卡死）
```

### 8.2 防止进化退化

```
问题：Agent 进化方向错误，导致能力下降

防御措施：
  1. Evolver 的信号去重：检测停滞模式，防止修复循环
  2. Evolver 的稳定性优先：错误率高时强制 repair-only 策略
  3. Gene validation 白名单：仅允许 node/npm/npx 命令
  4. 审查模式（--review）：人工确认后再应用重大变更
```

### 8.3 团队协作注意事项

```
✅ 做：
  - 共享存储使用版本化（S3 versioned / Git LFS）
  - 定期备份 skills/ 目录
  - 明确 Gene/Capsule 的作者和来源（用于追溯）

❌ 避免：
  - 多个人同时修改同一个 Gene（冲突）
  - 直接修改他人创建的 Capsule（用 fork + PR）
  - 在生产环境使用未经 review 的新 Gene
```

### 8.4 性能考虑

| 场景 | 建议 |
|------|------|
| 大量会话数据 | Evolve Server 用 `workflow` 引擎更稳定 |
| 复杂推理场景 | 用 `agent` 引擎（OpenClaw 驱动） |
| 实时性要求高 | 降低进化频率（如每小时一次而非每会话一次） |
| 存储成本 | 定期压缩/归档旧的 EvolutionEvent |

---

## 9. 注意事项与已知限制

### 9.1 Evolver 已知限制

1. **需要 Git**：在非 Git 目录运行会报错退出
2. **不是代码修补器**：只生成 GEP Prompt，不直接修改代码
3. **Hub 连接可选但有收益**：不连 Hub 也能用，但连了才有技能商店和 Worker 池
4. **License 变更**：2026-04-09 起从 MIT 转为 GPL-3.0（已发布版本不受影响）

### 9.2 SkillClaw 已知限制

1. **需要 OpenAI 兼容 API**：不支持纯本地模型（除非提供兼容 endpoint）
2. **共享存储必须有写权限**：Client 和 Server 都要能读写同一存储
3. **Evolve Server 资源消耗**：agent 引擎比 workflow 引擎消耗更多资源

### 9.3 SkillAnything 已知限制

1. **复杂目标效果有限**：自动分析可能遗漏边缘 case
2. **Trigger 设计质量依赖目标复杂度**：简单 CLI 工具效果最好
3. **多平台兼容性**：部分平台特有功能（如 Claude Code hooks）无法跨平台

---

## 10. 相关资源

| 资源 | 链接 |
|------|------|
| Evolver GitHub | https://github.com/EvoMap/evolver |
| Evolver Wiki | https://evomap.ai/wiki |
| EvoMap Hub | https://evomap.ai |
| SkillClaw GitHub | https://github.com/AMAP-ML/SkillClaw |
| SkillClaw Paper | arXiv 2604.08377 |
| SkillAnything GitHub | https://github.com/AgentSkillOS/SkillAnything |
| Hermes Ecosystem | https://github.com/ksimback/hermes-ecosystem |
| Hermes Agent | https://github.com/NousResearch/hermes-agent |

---

## 下一步

1. **快速体验**：在本地运行 `npm install -g @evomap/evolver`，执行 `node index.js` 感受 GEP Prompt 生成
2. **团队试用**：部署 SkillClaw 团队版，让团队成员共享进化循环
3. **自动生成**：用 SkillAnything 为团队常用工具批量生成 Skills
4. **深度定制**：阅读 Evolver 的 `assets/gep/` 目录，自定义 Gene/Capsule 库

---

*教程编写：墨鉴 | 2026-04-20*
