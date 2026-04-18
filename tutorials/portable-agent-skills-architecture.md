# 可移植 Agent Skills：跨平台 .agent/ 架构与 Skills 工程化实践

> **适合人群**：Agent 开发者、平台架构师、Skills 维护者
> **预计阅读时间**：45 分钟
> **前置要求**：熟悉 SKILL.md 基础格式，了解至少一种 Agent 平台（Claude Code / OpenClaw / Cursor）

---

## 1. 概述

### 1.1 背景：Skills 生态的四重碎片化

当前 Agent Skills 生态面临严峻的可移植性挑战：

| 碎片化维度 | 具体表现 |
|-----------|---------|
| **平台碎片化** | Claude Code / Cursor / Windsurf / OpenCode / OpenClaw / Hermes 各有独立的 skills 存储机制 |
| **模型碎片化** | 同一 Skill 在不同模型（GPT-4o / Claude 3.5 / Gemini 2.0）上的表现差异巨大 |
| **版本碎片化** | Skill 更新后没有跨平台同步机制 |
| **记忆碎片化** | 每次会话从零开始，跨会话上下文丢失 |

截至 2026-04-18，awesome-skills 收录了 **260 个 Skills 仓库**，覆盖 **4100+ 个独立 Skills**，但这些 Skills 大多只能在单一平台内使用。

### 1.2 本教程的目标项目

本教程深度分析 4 个代表性项目，它们共同构成"可移植 Skills 栈"的核心组件：

| 项目 | ⭐ | 核心角色 | 解决的问题 |
|------|-----|---------|-----------|
| [codejunkie99/agentic-stack](https://github.com/codejunkie99/agentic-stack) | 400 | **跨平台记忆与 Skills 容器** | 统一的 `.agent/` 文件夹，8 大平台即插即用 |
| [AgentSkillOS/SkillAnything](https://github.com/AgentSkillOS/SkillAnything) | 180 | **Skills 自动工厂** | 一个目标 → 多平台可部署的 Skills |
| [xwtro0tk1t-cloud/harness](https://github.com/xwtro0tk1t-cloud/harness) | 134 | **元技能（Meta-Skill）** | 4 层增强框架，一次安装，全项目生效 |
| [SJTU-IPADS/SkVM](https://github.com/SJTU-IPADS/SkVM) | 68 | **Skills 语言虚拟机** | 编译 Skills 以匹配不同模型能力 |

### 1.3 核心设计理念

```
Skills 可移植栈 = 可移植容器 × 自动工厂 × 质量增强 × 模型适配

"一次编写，随处运行"  → agentic-stack（.agent/ 容器）
"任何目标，生成 Skill" → SkillAnything（7 相自动工厂）
"一次安装，全面增强" → harness（4 层元技能）
"模型定制，性能最优" → SkVM（编译型 Skills 运行时）
```

---

## 2. agentic-stack：跨平台 .agent/ 文件夹

> **仓库**：codejunkie99/agentic-stack | ⭐ 400 | MIT License
> **支持平台**：Claude Code, Cursor, Windsurf, OpenCode, OpenClaw, Hermes, Pi Coding Agent, Standalone Python

### 2.1 核心架构

agentic-stack 的核心洞察是：**Skills 和记忆本身就是数据，应该与平台无关**。

它将所有 Agent 运行时依赖打包到一个 portable `.agent/` 文件夹：

```
.agent/                              # 便携式智能体大脑（跨平台通用）
├── AGENTS.md                        # 全局地图（LLM 启动时读取）
├── memory/                          # 四层记忆系统
│   ├── working/                     # 当前会话工作记忆
│   ├── episodic/                    # 历史会话事件记忆
│   ├── semantic/                    # 抽象知识（毕业 Lessons）
│   │   └── LESSONS.md               # 从 lessons.jsonl 渲染
│   └── personal/                    # 用户偏好
│       └── PREFERENCES.md           # 个性化配置（会话启动必读）
├── skills/                          # Skills 库
│   ├── _index.md                    # 轻量索引（始终加载）
│   ├── _manifest.jsonl              # Skills 清单（按需加载）
│   └── *.SKILL.md                   # 各 Skill 完整定义
├── protocols/                       # 协议层
│   ├── permissions.md               # 权限约束（PreToolUse Hook 执行）
│   ├── tool_schemas/                # 类型化工具模式
│   └── delegation.md                # 子 Agent 委托契约
├── harness/                         # conductor + hooks（独立路径）
└── tools/                           # 主人 Agent CLI 工具
    ├── list_candidates.py           # 候选 Lesson 列表
    ├── graduate.py                  # 接收 Lesson（需提供理由）
    ├── reject.py                    # 拒绝 Lesson（需提供原因）
    └── reopen.py                    # 重新开启已拒绝的 Lesson
```

### 2.2 平台适配器系统

agentic-stack 的精髓在于 **adapters/** 目录——每个平台只需一个小 shim：

```
adapters/
├── claude-code/    CLAUDE.md + .claude/settings.json (hooks)
├── cursor/         .cursor/rules/*.mdc
├── windsurf/       .windsurfrules
├── opencode/       AGENTS.md + opencode.json
├── openclaw/       system-prompt include
├── hermes/         AGENTS.md (agentskills.io 兼容)
├── pi/             AGENTS.md + .pi/skills symlink
└── standalone-python/  run.py（任意 LLM 的 DIY conductor）
```

安装时选择一个 adapter，即可在对应平台使用完整的 `.agent/` 大脑：

```bash
brew tap codejunkie99/agentic-stack https://github.com/codejunkie99/agentic-stack
brew install agentic-stack

cd your-project
agentic-stack claude-code    # 安装 Claude Code 适配器
# 或: agentic-stack openclaw  # 安装 OpenClaw 适配器
```

### 2.3 四层记忆系统

agentic-stack 的记忆系统是其最有深度的设计之一：

| 层级 | 名称 | 内容 | 保留策略 |
|------|------|------|---------|
| **L1** | Working | 当前会话的临时上下文 | 会话结束清除 |
| **L2** | Episodic | 历史会话事件（.agent/ memory/dream.log） | 按需压缩 |
| **L3** | Semantic | 抽象知识：从候选 Lesson 毕业而来 | 永久保留 |
| **L4** | Personal | 用户偏好 PREFERENCES.md | 永久保留 |

**关键创新：Lesson 毕业协议**

```
会话发生
    ↓
auto_dream.py 聚类 → 候选 Lesson（仅暂存，不生效）
    ↓
主人 Agent 审查（via graduate.py / reject.py）
    ↓
graduated → lessons.jsonl + LESSONS.md 渲染
rejected → 保留决策历史（防重复 churn）
    ↓
未来会话自动加载相关 Lessons
```

这个设计的核心原则是：**机械 staging + 人工 reasoning 分离**。auto_dream.py 只做聚类/文件操作，不做推理；主人 Agent 通过 CLI 工具进行有据可查的审查（必须提供 rationale）。

### 2.4 Seed Skills（5 个预置 Skills）

| Skill | 功能 |
|-------|------|
| `skillforge` | 从重复模式中创建新 Skills |
| `memory-manager` | 运行反思周期，表面候选 Lessons |
| `git-proxy` | 所有 Git 操作 + 安全约束 |
| `debug-investigator` | 重现 → 隔离 → 假设 → 验证 |
| `deploy-checklist` | Staging 与 Production 之间的护栏 |

### 2.5 PREFERENCES.md 引导流程

安装后首次运行引导向导，6 个偏好问题：

```markdown
# PREFERENCES.md — AI Onboarding

## 基本信息
Name: [用户回答]
Languages: [用户回答]

## 工作风格
Explanation style: concise | detailed | technical
Test strategy: test-first | test-after | no-test
Commit style: conventional-commits | freeform
Code review depth: critical-only | balanced | thorough
```

这些偏好直接影响 AI 的行为——例如 `concise` 风格会让 AI 生成更短的解释，`conventional-commits` 会强制使用规范提交格式。

### 2.6 使用场景

**场景 1：在团队项目中跨成员共享 Agent 上下文**

```bash
# 团队成员 A 配置好 .agent/ 后推送到 Git
git add .agent/
git commit -m "feat: add agentic-stack brain for backend team"

# 团队成员 B clone 后自动继承相同的记忆和 Skills
agentic-stack claude-code
# AI 启动时自动读取 .agent/memory/semantic/LESSONS.md
# AI 启动时自动读取 .agent/memory/personal/PREFERENCES.md
```

**场景 2：在不同平台间切换项目**

```bash
# 在 Claude Code 中工作了一段时间后切换到 Cursor
agentic-stack cursor
# .cursor/rules/ 目录下生成 shim，自动指向 .agent/ 目录
# Cursor AI 立即获得相同记忆和 Skills
```

---

## 3. SkillAnything：Skills 自动工厂

> **仓库**：AgentSkillOS/SkillAnything | ⭐ 180 | MIT License
> **支持平台**：Claude Code, OpenClaw, OpenAI Codex, Generic

### 3.1 核心价值

SkillAnything 是一个"**生成 Skills 的 Skill**"。它的核心洞察是：Skills 的手工编写是重复劳动，应该被自动化。

给一个目标（CLI 工具 / REST API / Python 库 / 工作流），SkillAnything 自动运行 7 相管线，输出多平台可部署的 Skills 包。

### 3.2 七相管线详解

```
Target: "Stripe API"
    │
    ▼
[Phase 1: Analyze]  →  Auto-detect 目标类型、提取能力
    │
    ▼
[Phase 2: Design]   →  能力映射到 Skill 架构
    │
    ▼
[Phase 3: Implement] →  生成 SKILL.md + 脚本 + 参考文档
    │
    ▼
[Phase 4: Test]     →  自动生成评测用例 + 触发查询
    │
    ▼
[Phase 5: Evaluate]  →  有/无 Skill 基准测试，输出通过率
    │
    ▼
[Phase 6: Optimize]  →  训练/测试循环优化描述词
    │
    ▼
[Phase 7: Package]   →  多平台分发包
    │
    ▼
dist/
├── claude-code/    # Claude Code 格式
├── openclaw/      # OpenClaw 格式
├── codex/         # OpenAI Codex 格式
└── generic/       # 平台无关 zip
```

### 3.3 目标自动检测

| 目标类型 | 检测方法 | 示例 |
|---------|---------|------|
| CLI 工具 | `which <name>` + `--help` 解析 | `jq`, `httpie`, `ffmpeg` |
| REST API | URL + OpenAPI/Swagger spec | Stripe API, GitHub API |
| Python 库 | pip/npm 包名 | `pandas`, `lodash` |
| 工作流 | 分步描述 | ETL pipeline, CI/CD |
| Web 服务 | URL + Web 文档 | Slack, Notion |

### 3.4 使用方法

**在 Claude Code 中（自然语言触发）**：

```
> Create a skill for the httpie CLI tool
> Generate a multi-platform skill for the Stripe API
> Turn this data pipeline workflow into a skill
```

**分步执行**：

```bash
# Phase 1-2: 分析 + 设计
python -m scripts.analyze_target --target "jq" --output analysis.json
python -m scripts.design_skill --analysis analysis.json --output architecture.json

# Phase 3: 脚手架
python -m scripts.init_skill my-skill --template cli --output ./out

# Phase 7: 多平台打包
python -m scripts.package_multiplatform ./out/my-skill \
  --platforms claude-code,openclaw,codex
```

### 3.5 Phase 6 优化循环

最值得关注的 Phase 6 —— 它用 train/test 循环自动优化 Skill 描述词：

```bash
# 基于触发查询评测集，反复优化 SKILL.md 描述
skvm run_loop \
  --eval-set trigger-evals.json \
  --skill-path ./out/my-skill \
  --model claude-sonnet-4-20250514
```

这本质上是一个**可运行的超参数搜索**：给定评测集和目标模型，自动寻找使触发准确率最大化的 Skill 描述措辞。

---

## 4. harness：元技能与四层增强框架

> **仓库**：xwtro0tk1t-cloud/harness | ⭐ 134 | MIT License
> **设计者**：@AV1DLIVE（与 agentic-stack 同一作者）
> **兼容平台**：Claude Code（最佳）、Cursor、Windsurf、Cline、GitHub Copilot、Aider、Continue、Devin

### 4.1 核心问题诊断

harness 的创始动机非常务实：AI Agent 写代码快，但"快"带来了 4 大核心问题：

| 问题 | 表现 | 后果 |
|------|------|------|
| **知识断层** | 每次新会话从零开始 | 重复犯错、违反规范 |
| **无约束** | 坏代码存在于代码库，AI 复制并产生更多坏代码 | 安全漏洞、架构腐坏 |
| **无反馈** | AI 自信宣告完成，实际是一团糟 | 生产事故、返工 |
| **熵增** | 写得快 = 垃圾堆积更快 | 技术债务爆炸、文档过时 |

### 4.2 四层增强系统

```
┌──────────────────────────────────────────────────────────────┐
│                    Harness Enhancement System                 │
├─────────────┬──────────────┬───────────────┬────────────────┤
│  Layer 1    │   Layer 2    │   Layer 3     │   Layer 4      │
│  Knowledge  │  Architecture │  Feedback    │   Entropy      │
│  Mgmt 📋   │  Constraints🚧│  Loops 🔄    │   Mgmt 🧹      │
├─────────────┼──────────────┼───────────────┼────────────────┤
│  CLAUDE.md  │  Hook-based  │  TDD          │  Code hygiene  │
│  docs/ tree │  enhancement │  Code Review  │  Doc sync      │
│  Agent Team │  Security    │  Verification │  Pitfall       │
│  Skill      │  standards   │  gates        │  records       │
│  ecosystem  │  CWE defense │  Security     │  Knowledge     │
│             │  Behavior    │  review       │  extraction    │
│             │  red lines   │               │                │
└─────────────┴──────────────┴───────────────┴────────────────┘
```

### 4.3 Layer 1：知识管理

**CLAUDE.md ≤ 150 行原则**：

harness 的一条关键规则是：CLAUDE.md 必须 ≤ 150 行。因为 CLAUDE.md 在每次会话启动时完整读取，500 行的 CLAUDE.md = token 浪费 + 关键信息被淹没。

详细内容拆分到 `docs/` 子文档，按需加载。

**docs/ B-tree 索引结构**：

```
L0: CLAUDE.md (≤150 lines)          — AI 每次必读，零详细内容
     → 5 个分类指针，无实际内容

L1: docs/xxx/INDEX.md (≤50 lines)   — 模块列表 + 一句话总结 + 更新日期
     → 指向 L2 子索引

L2: docs/xxx/module/INDEX.md (≤30 lines)  — 叶子文档列表 + 时间线
     → 指向 L3 实际内容

L3: docs/xxx/module/topic.md (≤150 lines)  — 实际内容（唯一有内容的层级）
```

**AI 记忆恢复路径**：读取 L0 → 确定方向 → 读取 L1 → 定位模块 → 读取 L2 → 找到文档 → 读取 L3。每次只读一个索引层级，将 token 消耗降到最低。

### 4.4 Layer 2：架构约束

**PreToolUse Hook 执行权限控制**：

```python
# .claude/settings.json 中的权限约束示例
{
  "permissions": {
    "allow": ["Read", "Edit", "Bash:git*"],
    "deny": ["Bash:rm -rf", "Bash:sudo", "Write:prod/**"],
    "requireConfirmation": ["Bash:*", "Write:src/**"]
  }
}
```

### 4.5 Layer 3：反馈回路

**TDD 铁律**：superpowers TDD 强制要求"无失败测试，不写代码"（NO CODE WITHOUT FAILING TEST FIRST）。

**验证铁律**：superpowers verification 强制要求阶段完成必须有证据。

### 4.6 Agent Team 角色分离

harness 实现了基于角色的 Agent 分工：

| 角色 | 职责 | 约束 |
|------|------|------|
| **Architect (A)** | 规划、设计、交互动、提交、文档 | 必须先头脑风暴 → 用户批准 → 写设计文档 |
| **Challenger (C)** | 对计划/设计/声明进行对抗性审查 | 不接受无证据声明；验证 API 使用、线程安全、边界情况 |
| **Engineer (E)** | 编码、修复、重构 | 必须 TDD，不得触碰架构级配置 |
| **Tester (T)** | 编写测试、验证 | **不得修改业务代码**，只报告 bug |

**触发方式**：自然语言（"Have Agent B implement this feature"）或 Agent 工具（带 `isolation: "worktree"` 的隔离模式）。

### 4.7 24 个痛点覆盖

harness 的 README 详细列出了 AI 辅助开发中的 24 个常见痛点及其解决强度评级：

- ★★★★★ 完全解决（4 个）：先思考再编码、TDD、验证铁律、新会话冷启动
- ★★★★☆ 强力解决（13 个）：计划崩溃中途、跨会话重复犯错、安全漏洞检查等
- ★★★☆☆ 部分解决（7 个）：上下文质量退化、文档过期、secret 泄露等

### 4.8 与 agentic-stack 的关系

harness 和 agentic-stack 来自同一作者（@AV1DLIVE），设计理念高度一致：

| 共享模式 | agentic-stack | harness |
|---------|--------------|---------|
| 知识分层 | `.agent/memory/semantic/LESSONS.md` | `docs/` B-tree |
| 约束执行 | `protocols/permissions.md` (Hook) | Layer 2 Hook 增强 |
| 角色分离 | Agent Team 架构 | 4 角色 + Agent Teams |
| 学习循环 | `auto_dream.py` + 毕业协议 | `claudeception` 持续学习 |

两者可以协同使用：harness 提供项目级别的增强框架，agentic-stack 提供跨项目/跨平台的记忆持久化。

---

## 5. SkVM：Skills 语言虚拟机

> **仓库**：SJTU-IPADS/SkVM | ⭐ 68 | 上海交大 IPADS 实验室
> **论文**：arXiv:2604.03088 | [官网](https://skillvm.ai)

### 5.1 核心问题

SkVM 要解决的问题是：**同一 Skill 在不同模型上的效果差异巨大**。

例如，一个为 Claude 3.5 设计的 Skill，在 Qwen 3.5 上可能因为以下原因失效：
- 模型对特定格式的指令理解能力不同
- 模型的工具调用能力有差异
- 模型的上下文窗口大小不同

### 5.2 架构概览

SkVM 是一个 **Skills 编译和运行时系统**，包含 4 个主要组件：

```
SkVM
├── Profile     — 测量模型 + harness 的原始能力
├── AOT-Compile — AOT 编译器多遍优化 Skills
├── JIT-Optimize — JIT 即时优化（运行时加速 + 内容优化）
└── Benchmark   — 评估 Skills 在不同任务/条件/模型下的表现
```

### 5.3 Profile：模型能力分析

```bash
skvm profile \
  --model=qwen/qwen3.5-35b-a3b \
  --adapter=bare-agent
```

Profile 输出模型在预定义原始能力上的评分，作为后续编译的依据。

预置 profile 数据覆盖：`qwen3.5-35b-a3b`, `deepseek-v3.2`, `anthropic/claude-opus-4.6` 等。

### 5.4 AOT-Compile：编译型 Skills

```bash
skvm aot-compile \
  --skill=path/to/skill-dir \
  --model=qwen/qwen3.5-35b-a3b \
  --adapter=bare-agent \
  --pass=1 \
  --compiler-model=anthropic/claude-sonnet-4.6
```

AOT 编译器根据模型能力 Profile 重写 Skill，将 Skill 适配到目标模型的指令理解能力和工具调用模式。编译结果缓存于 `~/.skvm/proposals/aot-compile/`。

### 5.5 JIT-Optimize：即时优化

**Synthetic 模式**（基于合成任务）：

```bash
skvm jit-optimize \
  --skill=path/to/skill-dir \
  --task-source=synthetic \
  --task-concurrency=3 \
  --target-adapter=bare-agent \
  --optimizer-model=anthropic/claude-sonnet-4.6 \
  --rounds=1 \
  --target-model=qwen/qwen3.5-35b-a3b
```

**Log 模式**（基于会话日志，无重跑）：

```bash
skvm jit-optimize \
  --skill=path/to/skill-dir \
  --task-source=log \
  --logs=path/to/session.jsonl \
  --optimizer-model=anthropic/claude-sonnet-4.6 \
  --target-model=qwen/qwen3.5-35b-a3b
```

### 5.6 与前三者的互补关系

```
agentic-stack    →  Skills 的存储和记忆层
SkillAnything    →  Skills 的生成层
harness          →  Skills 的质量增强层
SkVM             →  Skills 的运行时适配层

四者不是竞争关系，而是分工：
生产(生成) → 质量(增强) → 存储(记忆) → 运行时(适配)
```

---

## 6. 综合应用：从零构建一个跨平台可移植 Skill 栈

### 6.1 完整工作流

假设你正在维护一个包含 10+ 开发者的前端项目，需要让所有开发者共享同一个 Agent 技能栈。

**Step 1：用 SkillAnything 生成项目专属 Skill**

```bash
# 分析项目技术栈，生成专属 Skills
git clone https://github.com/AgentSkillOS/SkillAnything.git \
  ~/.claude/skills/skill-anything

# 在 Claude Code 中执行
> Generate a multi-platform skill for our React + TypeScript + Tailwind project
```

**Step 2：用 harness 增强项目质量约束**

```bash
git clone https://github.com/xwtro0tk1t-cloud/harness.git .harness

# 在项目中初始化 harness
cd your-project
./install-harness.sh claude-code

# 这会：
# 1. 生成 ≤150 行的 CLAUDE.md
# 2. 创建 docs/ B-tree 索引结构
# 3. 配置 Hooks（PreToolUse / PostToolUse / Stop）
# 4. 设置 Agent Teams 配置
```

**Step 3：用 agentic-stack 建立跨平台记忆**

```bash
brew install agentic-stack
cd your-project
agentic-stack claude-code  # 生成 .agent/ 便携大脑
# 回答 onboarding 向导（6 个偏好问题）

# 推送 .agent/ 到 Git，团队成员 clone 后即可使用相同上下文
git add .agent/
git commit -m "feat: add shared agentic-stack brain"
```

**Step 4：用 SkVM 优化 Skill 性能**

```bash
# 在 CI/CD 中集成 SkVM 优化
skvm profile --model=claude-3.5-sonnet-20241022 --adapter=claude-code

skvm aot-compile \
  --skill=~/.claude/skills/skill-anything \
  --model=claude-3.5-sonnet-20241022 \
  --adapter=claude-code \
  --pass=3
```

### 6.2 项目目录结构示例

```
your-project/
├── .agent/                     # agentic-stack 便携记忆（Git 跟踪）
│   ├── AGENTS.md
│   ├── memory/
│   │   ├── semantic/LESSONS.md
│   │   └── personal/PREFERENCES.md
│   ├── skills/
│   │   └── your-project-skill.SKILL.md
│   └── protocols/permissions.md
│
├── .harness/                  # harness 元技能
│   ├── agents/                # Agent Team 定义
│   ├── hooks/                 # Claude Code Hooks
│   └── docs/                  # B-tree 文档树
│
├── CLAUDE.md                   # harness 生成（≤150 行）
│
└── docs/                      # B-tree 文档结构
    ├── architecture/INDEX.md
    ├── conventions/INDEX.md
    └── pitfalls/INDEX.md
```

---

## 7. 最佳实践

### 7.1 可移植性原则

**原则 1：SKILL.md 内容优先于平台特定配置**

```markdown
# ✅ 好：内容与格式分离
# SKILL.md 中只放跨平台一致的内容
# 平台特定配置放在 adapter/ 目录下

# ❌ 差：平台特定指令混入 Skill 内容
When using Claude Code, run `npx skills add xxx`
```

**原则 2：渐进式披露避免全量加载**

agentic-stack 的 `_index.md` + `_manifest.jsonl` 模式是最佳实践：

```markdown
# _index.md（始终加载，<50 行）
## Available Skills
- git-proxy: Git operations with safety constraints → `git-proxy.SKILL.md`
- debug-investigator: Reproduce → isolate → hypothesize → verify → `debug-investigator.SKILL.md`

# git-proxy.SKILL.md（按需加载，仅在任务匹配触发词时加载）
## Triggers
- "run git"
- "commit changes"
- "check git status"
## Content
[完整 Skill 内容...]
```

**原则 3：偏好设置与 Skill 分离**

PREFERENCES.md 应该只包含行为偏好，不应包含 Skill 指令：

```markdown
# ✅ PREFERENCES.md 内容
Explanation style: concise
Test strategy: test-after
Commit style: conventional-commits

# ❌ 不应该放在 PREFERENCES.md
Skill instructions, tool usage patterns
```

### 7.2 安全原则

**harness 的 4 层安全增强值得借鉴**：

1. **权限分层**：明确 allow/deny/requireConfirmation 边界
2. **行为红线**：CLAUDE.md 中的 MUST NOT 规则
3. **提交前扫描**：Enterprise Hook 的 pre-commit secret scan
4. **供应链审计**：supply-chain-audit Skill（8 种语言）

**agentic-stack 的权限执行**：

`protocols/permissions.md` 在 PreToolUse Hook 阶段强制执行，防止恶意工具调用。

### 7.3 记忆管理原则

**Lesson 毕业协议的核心价值**：

```
设计原则：机械 staging + 人工 reasoning 分离

auto_dream.py：
  ✅ 可以做：聚类、阶段、去重、衰减
  ❌ 不能做：推理、接受/拒绝、修改语义记忆

graduated.py（主人 Agent 执行）：
  ✅ 必须提供：--rationale（理由）
  ❌ 拒绝无理由通过
```

### 7.4 SkVM 性能优化原则

1. **优先 Profile**：不同模型 + adapter 组合能力差异大，先 Profile 再编译
2. **AOT + JIT 组合**：AOT 解决基础适配，JIT 解决运行时细节
3. **Synthetic + Log 组合**：Synthetic 快速迭代，Log 用于真实会话复盘
4. **Proposal 审查**：JIT 优化建议必须人工审查再接受（与 Lesson 毕业协议同理）

---

## 8. 重要注意事项

### 8.1 agentic-stack 的限制

| 限制 | 说明 |
|------|------|
| **Cursor/Windsurf 无 Hook** | 这些平台的 Hook 需要手动调用 `memory_reflect`，无法自动化 |
| **Lessons 需要主人 Agent 审查** | 无法完全自动化，依赖主人 Agent 在会话中执行审查 |
| **FTS5 搜索默认关闭** | BETA 功能，启用后增加 `.agent/memory/.index/` 存储 |
| **OpenClaw 适配器** | 名称从 OpenClient 变更，部分 Breaking Change |

### 8.2 SkillAnything 的限制

| 限制 | 说明 |
|------|------|
| **Phase 6 依赖大模型** | 优化循环需要调用大模型 API，有成本 |
| **API / 库类型检测依赖规格** | 无 OpenAPI spec 的私有 API 可能检测失败 |
| **Benchmark 需要 ground truth** | 评测集质量直接影响优化结果 |

### 8.3 harness 的局限性

| 局限 | 说明 |
|------|------|
| **最优体验在 Claude Code** | Hook 系统是其核心，其他平台只能部分兼容 |
| **Agent Team 需要人工协调** | 角色切换和约束目前靠约定，缺乏强制执行机制 |
| **CLAUDE.md 150 行限制** | 复杂项目的约束可能超出此限制 |
| **Pitfall 记录需要主动维护** | 不维护 = 不生效 |

### 8.4 SkVM 的技术约束

| 约束 | 说明 |
|------|------|
| **Node ≥ 18** | npm 安装需要 Node 18+ |
| **需要 API Key** | Profile、JIT-Optimize 等功能需要 OpenRouter / OpenAI 等 API Key |
| **预置 Profile 有限** | 只有部分热门模型有预置 Profile，冷门模型需要自行 Profile |
| **编译结果非跨模型复用** | 为 Qwen 编译的 Skill 不能直接给 Claude 使用 |

---

## 9. 总结：可移植 Skills 生态全景图

### 9.1 四层架构总结

```
┌─────────────────────────────────────────────────────────┐
│                    可移植 Skills 生态                    │
├──────────────────┬──────────────────┬──────────────────┤
│   生成层          │   质量层          │   存储层          │
│   SkillAnything   │   harness         │   agentic-stack   │
│   (任何→Skill)    │   (4层增强)       │   (跨平台记忆)    │
├──────────────────┴──────────────────┴──────────────────┤
│                   运行时适配层                           │
│                     SkVM                                │
│              (模型定制化编译)                            │
└─────────────────────────────────────────────────────────┘
```

### 9.2 关键设计模式

| 模式 | 来源 | 核心价值 |
|------|------|---------|
| **Portable .agent/ Container** | agentic-stack | "一次编写，随处运行" |
| **7-Phase Auto-Factory** | SkillAnything | 消除 Skills 手工编写瓶颈 |
| **4-Layer Enhancement** | harness | 全面质量保障 |
| **AOT + JIT Compilation** | SkVM | 模型无关 Skills 性能优化 |
| **Graduation Protocol** | agentic-stack | 机械 staging + 人工 reasoning 分离 |
| **B-tree Memory Index** | harness | 渐进式披露，最小化 token 消耗 |
| **Role-Based Agent Team** | harness | 对抗性审查，防止 AI 自说自话 |

### 9.3 适用场景决策树

```
你的主要需求是？
    │
    ├─→ "我要让团队成员共享同一 Agent 上下文"
    │       → agentic-stack（.agent/ 便携文件夹）
    │
    ├─→ "我要为某个工具/API 自动生成跨平台 Skill"
    │       → SkillAnything（7 相自动工厂）
    │
    ├─→ "我要在项目中建立全面的质量护栏"
    │       → harness（4 层增强）
    │
    ├─→ "我要优化 Skill 在特定模型上的表现"
    │       → SkVM（AOT + JIT 编译）
    │
    └─→ "我要完整解决方案"
            → agentic-stack + harness + SkVM 组合使用
```

---

## 10. 相关资源

| 资源 | 链接 |
|------|------|
| agentic-stack GitHub | https://github.com/codejunkie99/agentic-stack |
| SkillAnything GitHub | https://github.com/AgentSkillOS/SkillAnything |
| harness GitHub | https://github.com/xwtro0tk1t-cloud/harness |
| SkVM 官网 | https://skillvm.ai |
| SkVM 论文 | https://arxiv.org/abs/2604.03088 |
| @AV1DLIVE Twitter | https://x.com/Av1dlive |
| "The Agentic Stack" 文章 | https://x.com/Av1dlive/status/2044453102703841645 |

---

## 下一步

1. **立即尝试**：在本地项目运行 `agentic-stack claude-code`，体验跨平台记忆
2. **深入学习**：阅读各项目的 architecture 文档（`docs/architecture.md`）
3. **贡献社区**：如果你的工具/平台还没有适配器，为 agentic-stack 编写 adapter
4. **集成 SkVM**：在 CI/CD 中集成 SkVM benchmark，持续监控 Skills 质量

---

*整理：墨鉴 | 2026-04-18*
*相关教程：[Context Engineering & Multi-Agent](/Volumes/waku/github-维护/awesome/awesome-skills-repos/tutorials/context-engineering-multi-agent.md) | [Core Frameworks Deep Dive](/Volumes/waku/github-维护/awesome/awesome-skills-repos/tutorials/core-frameworks-deep-dive.md)*
