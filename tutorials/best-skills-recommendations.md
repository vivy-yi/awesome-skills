# Best Skills 推荐榜单

> **适合人群**：想为 Agentic Tool 配置最佳 Skills 的开发者
> **预计阅读时间**：30 分钟
> **更新日期**：2026-04-21

---

## 1. Best Skills 概览

### 1.1 推荐榜单体系

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                          Best Skills 推荐体系                                        │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  ⭐ Claude Code Best Skills                                                        │
│  ├── TDD/Testing: upstack, testing-best-practices, specmint-tdd                   │
│  ├── Security: trailofbits/skills, claude-code-owasp                             │
│  ├── Git/Workflow: git-workflow-skill, claude-git-expert                         │
│  └── Architecture: claude-architecture-skills, arkhe-claude-plugins              │
│                                                                                     │
│  🟠 OpenClaw Best Skills                                                          │
│  ├── Medical: OpenClaw-Medical-Skills (最大开源医疗 AI)                             │
│  ├── Enterprise: awesome-openclaw-agent-packs (30+ Agent Packs)                   │
│  └── Security: openclaw-skills-security                                          │
│                                                                                     │
│  🔵 Hermes Agent Best Skills                                                      │
│  ├── Autonomous: hermes-incident-commander (SRE 自动化)                            │
│  ├── Production: hermes-patterns (6 种生产级模式)                                  │
│  └── Enterprise: awesome-OPC-lark-cli-skills (飞书集成)                            │
│                                                                                     │
│  🟢 OpenCode Best Skills                                                          │
│  ├── SOP: opencode-sop-engine (生产级 SOP 执行)                                   │
│  ├── Productivity: easy_opencode (13 专业 Agent)                                   │
│  └── Cross-Platform: ai-dev-kit, hatch3r (全平台通用)                            │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Claude Code Best Skills

### 2.1 必备 Awesome Lists

| 列表 | Stars | 描述 |
|------|-------|------|
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | ⭐ 2,200+ | Skills、Hooks、Commands 全方位精选 |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | ⭐ 1,000+ | 跨平台 Skills（Claude Code、Codex、Gemini） |
| [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | ⭐ 4,554 | 1,400+ 可安装 Skills |

### 2.2 TDD/Testing Skills

| Skill | Stars | 描述 | 链接 |
|-------|-------|------|------|
| **upstack** | ⭐ 1,600+ | Red/Green TDD 工作流，轻量级 | [GitHub](https://github.com/Upsolve-Labs/upstack) |
| **testing-best-practices** | ⭐ 800+ | TDD、属性测试、反模式检测 | [GitHub](https://github.com/adewale/testing-best-practices) |
| **specmint-tdd** | ⭐ 200+ | 严格的 Red-Green-Refactor 执行 | [GitHub](https://github.com/ngvoicu/specmint-tdd) |
| **claude-tdd-skill** | ⭐ 150+ | 交互式 TDD 带检查点 | [GitHub](https://github.com/or-ituran/claude-tdd-skill) |
| **muki-ai-plugins** | ⭐ 500+ | TDD、代码审查、规划、E2E | [GitHub](https://github.com/mukiwu/muki-ai-plugins) |

**推荐组合**：`upstack` + `testing-best-practices` + `specmint-tdd`

### 2.3 Security Skills

| Skill | Stars | 描述 | 链接 |
|-------|-------|------|------|
| **trailofbits/skills** | ⭐ 3,000+ | 安全研究、漏洞检测 | [GitHub](https://github.com/trailofbits/skills) |
| **claude-code-owasp** | ⭐ 1,500+ | OWASP 最佳实践 (2025-2026) | [GitHub](https://github.com/agamm/claude-code-owasp) |
| **Anthropic-Cybersecurity-Skills** | ⭐ 2,000+ | 754 网络安全 Skills | [GitHub](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) |
| **raptor** | ⭐ 800+ | 进攻/防御安全 Agent | [GitHub](https://github.com/gadievron/raptor) |

**推荐组合**：`trailofbits/skills` + `claude-code-owasp`

### 2.4 Git/Workflow Skills

| Skill | Stars | 描述 | 链接 |
|-------|-------|------|------|
| **git-workflow-skill** | ⭐ 900+ | 分支、提交、PR 工作流 | [GitHub](https://github.com/netresearch/git-workflow-skill) |
| **claude-git-expert** | ⭐ 600+ | 高级 Git 工作流自动化 | [GitHub](https://github.com/IncomeStreamSurfer/claude-git-expert) |
| **claude-ship-command** | ⭐ 400+ | 自动 git commit、push、build、deploy | [GitHub](https://github.com/sterlingsky/claude-ship-command) |
| **claude-git-pr-skill** | ⭐ 300+ | GitHub PR 审查 | [GitHub](https://github.com/aidankinzett/claude-git-pr-skill) |

### 2.5 Architecture Skills

| Skill | Stars | 描述 | 链接 |
|-------|-------|------|------|
| **claude-architecture-skills** | ⭐ 1,200+ | 架构审查、设计、改进（7 Skills） | [GitHub](https://github.com/keez97/claude-architecture-skills) |
| **arkhe-claude-plugins** | ⭐ 2,500+ | 109 组件、22 Agents、55 Skills | [GitHub](https://github.com/joaquimscosta/arkhe-claude-plugins) |
| **c3-skill** | ⭐ 300+ | C3 架构设计方法论 | [GitHub](https://github.com/lagz0ne/c3-skill) |
| **code-architect** | ⭐ 500+ | 软件架构设计和规划 | [GitHub](https://github.com/rgvai/code-architect) |

### 2.6 Code Review Skills

| Skill | Stars | 描述 | 链接 |
|-------|-------|------|------|
| **code-review-skill** | ⭐ 1,800+ | React 19、Vue 3、Rust、TypeScript 审查 | [GitHub](https://github.com/awesome-skills/code-review-skill) |
| **pragmatic-clean-code-reviewer** | ⭐ 400+ | Clean Code、Clean Architecture 原则 | [GitHub](https://github.com/Zhen-Bo/pragmatic-clean-code-reviewer) |
| **claude-wizard** | ⭐ 600+ | 高级软件架构师 - 8 阶段开发 | [GitHub](https://github.com/vlad-ko/claude-wizard) |

### 2.7 Best Skill Collections

| Collection | Stars | 描述 |
|------------|-------|------|
| **everything-claude-code** | ⭐ 32,880 | Agent Harness 性能优化 - Skills、Instincts、Memory、Security |
| **claude-superpowers** | ⭐ 3,000+ | TDD、头脑风暴、调试实战 Skills |
| **omega-skills** | ⭐ 1,500+ | 会话专注、重构、安全审计、测试设计 |
| **specops** | ⭐ 2,000+ | 自主 TDD Agent 团队 |

---

## 3. OpenClaw Best Skills

### 3.1 必备 Awesome Lists

| 列表 | Stars | 描述 |
|------|-------|------|
| [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | ⭐ 1,500+ | 5,400+ Skills 筛选分类 |
| [SamurAIGPT/awesome-openclaw](https://github.com/SamurAIGPT/awesome-openclaw) | ⭐ 1,000+ | 资源、工具、Skills、教程精选 |

### 3.2 Medical Skills（OpenClaw 特色）

| Skill | Stars | 描述 | 链接 |
|-------|-------|------|------|
| **OpenClaw-Medical-Skills** | ⭐ 5,000+ | **最大开源医疗 AI Skills 库** | [GitHub](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) |

### 3.3 Enterprise Skills

| Skill | Stars | 描述 | 链接 |
|-------|-------|------|------|
| **awesome-openclaw-agent-packs** | ⭐ 800+ | 30+ 可部署 Agent Packs（销售、工程、营销） | [GitHub](https://github.com/clawpod-app/awesome-openclaw-agent-packs) |
| **awesome-OPC-lark-cli-skills** | ⭐ 500+ | 飞书/Lark CLI 企业集成 | [GitHub](https://github.com/cnzhihao/awesome-OPC-lark-cli-skills) |

### 3.4 Popular Skills

| Skill | Stars | 描述 | 链接 |
|-------|-------|------|------|
| **openclaw-code-formatter** | ⭐ 300+ | 自动格式化（Prettier、Black、gofmt） | [GitHub](https://github.com/0xtodor-cyber/openclaw-code-formatter) |
| **open-claw_hot_topics** | ⭐ 200+ | 汇总 V2EX、Hacker News、GitHub Trending | [GitHub](https://github.com/kongzhixx11/open-claw_hot_topics) |
| **openclaw-magic-achievement-system-skill** | ⭐ 150+ | 游戏化成就系统 | [GitHub](https://github.com/J JarvisZhu97/openclaw-magic-achievement-system-skill) |

### 3.5 Security Skills

| Skill | Stars | 描述 | 链接 |
|-------|-------|------|------|
| **openclaw-skills-security** | ⭐ 400+ | 提示注入、供应链攻击、凭证泄露 | [GitHub](https://github.com/UseAI-pro/openclaw-skills-security) |

---

## 4. Hermes Agent Best Skills

### 4.1 必备 Awesome Lists

| 列表 | Stars | 描述 |
|------|-------|------|
| [0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) | ⭐ 826 | Skills、工具、集成 |
| [ChuckSRQ/awesome-hermes-skills](https://github.com/ChuckSRQ/awesome-hermes-skills) | ⭐ 300+ | 生产级 Skills 集合 |

### 4.2 Autonomous Operations

| Skill | Stars | 描述 | 链接 |
|-------|-------|------|------|
| **hermes-incident-commander** | ⭐ 1,200+ | 自主 SRE Agent - 检测、恢复、学习 | [GitHub](https://github.com/Lethe044/hermes-incident-commander) |
| **hermes-patterns** | ⭐ 600+ | 6 种生产级 Agent 模式（记忆、验证） | [GitHub](https://github.com/DevvGwardo/hermes-patterns) |
| **WZRD-Skill** | ⭐ 300+ | 生产级自动化 Skills | [GitHub](https://github.com/gratitude5dee/WZRD-Skill) |
| **sebastian-skills** | ⭐ 200+ | Hermes 生产级自动化 | [GitHub](https://github.com/sportkkclaw-gif/sebastian-skills) |

### 4.3 Enterprise Integration

| Skill | Stars | 描述 | 链接 |
|-------|-------|------|------|
| **awesome-OPC-lark-cli-skills** | ⭐ 500+ | 飞书/Lark CLI 企业集成 | [GitHub](https://github.com/cnzhihao/awesome-OPC-lark-cli-skills) |

---

## 5. OpenCode Best Skills

### 5.1 必备 Awesome Lists

| 列表 | Stars | 描述 |
|------|-------|------|
| [jshsakura/awesome-opencode-skills](https://github.com/jshsakura/awesome-opencode-skills) | ⭐ 400+ | 136+ OpenCode Skills 自动同步 |
| [weisser-dev/awesome-opencode](https://github.com/weisser-dev/awesome-opencode) | ⭐ 300+ | 108 Agents、15 Skills |

### 5.2 Productivity Skills

| Skill | Stars | 描述 | 链接 |
|-------|-------|------|------|
| **opencode-sop-engine** | ⭐ 800+ | 生产级 SOP 执行、长上下文控制 | [GitHub](https://github.com/wyf111/opencode-sop-engine) |
| **easy_opencode** | ⭐ 500+ | 13 专业 Agents、50+ Skills、33 Commands | [GitHub](https://github.com/jabing/easy_opencode) |
| **opencode-harness** | ⭐ 300+ | 生产级 Agents 引导 | [GitHub](https://github.com/tankdonut/opencode-harness) |

---

## 6. 跨平台 Best Skills

### 6.1 全平台通用 Skills

| Skill | Stars | 支持平台 | 描述 | 链接 |
|-------|-------|----------|------|------|
| **ai-dev-kit** | ⭐ 2,000+ | Claude Code, Codex, Gemini, Copilot, Qwen, OpenCode | 59 Skills、33 Agents、Hooks、Rules | [GitHub](https://github.com/noah-sheldon/ai-dev-kit) |
| **hatch3r** | ⭐ 1,500+ | 所有主流平台 | 11 Agents、22 Skills、18 Rules、25 Commands、MCP | [GitHub](https://github.com/hatch3r/hatch3r) |
| **specialist-agent** | ⭐ 1,200+ | Claude Code, Cursor, VS Code, Windsurf, Codex, OpenCode | 27+ Agents、21 Skills | [GitHub](https://github.com/HerbertJulio/specialist-agent) |
| **ai-foundry** | ⭐ 800+ | Claude 和所有主流 Harness | 生产级 Skills/Agents/Hooks 注册表 | [GitHub](https://github.com/msdakot/ai-foundry) |

### 6.2 Awesome Lists 跨平台

| 列表 | Stars | 描述 |
|------|-------|------|
| [awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | ⭐ 1,000+ | Claude Code、Codex、Gemini CLI、Cursor |
| [awesome-qa-skills](https://github.com/naodeng/awesome-qa-skills) | ⭐ 500+ | Cursor、Claude Code、Codex、OpenCode |
| [Antigravity](https://github.com/sickn33/antigravity-awesome-skills) | ⭐ 4,554 | Claude Code、Cursor、Codex CLI、Gemini CLI、Antigravity |

---

## 7. 场景化 Best Skills 组合

### 7.1 TDD 驱动开发

```
推荐组合：upstack + testing-best-practices + specmint-tdd

安装命令：
git clone https://github.com/Upsolve-Labs/upstack ~/.claude/skills/upstack
git clone https://github.com/adewale/testing-best-practices ~/.claude/skills/testing-best-practices
git clone https://github.com/ngvoicu/specmint-tdd ~/.claude/skills/specmint-tdd
```

### 7.2 安全关键项目

```
推荐组合：trailofbits/skills + claude-code-owasp + Anthropic-Cybersecurity-Skills

安装命令：
git clone https://github.com/trailofbits/skills ~/.claude/skills/trailofbits
git clone https://github.com/agamm/claude-code-owasp ~/.claude/skills/owasp
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills ~/.claude/skills/cybersecurity
```

### 7.3 企业/团队开发

```
推荐组合：everything-claude-code + git-workflow-skill + claude-architecture-skills

安装命令：
git clone https://github.com/affaan-m/everything-claude-code ~/.claude/skills/everything
git clone https://github.com/netresearch/git-workflow-skill ~/.claude/skills/git-workflow
git clone https://github.com/keez97/claude-architecture-skills ~/.claude/skills/architecture
```

### 7.4 多平台开发

```
推荐组合：ai-dev-kit + hatch3r + ai-foundry

安装命令：
git clone https://github.com/noah-sheldon/ai-dev-kit ~/.claude/skills/ai-dev-kit
git clone https://github.com/hatch3r/hatch3r ~/.claude/skills/hatch3r
git clone https://github.com/msdakot/ai-foundry ~/.claude/skills/ai-foundry
```

### 7.5 医疗健康（OpenClaw 特色）

```
推荐组合：OpenClaw-Medical-Skills + law-* + feishu-*

安装命令：
clawhub install FreedomIntelligence/OpenClaw-Medical-Skills
clawhub install openclaw/law-expert
clawhub install openclaw/feishu-doc
```

### 7.6 MLOps/AI 研究

```
推荐组合（Hermes）：hermes-incident-commander + hermes-patterns + mlops/*

安装命令：
hermes skills install autonomous-ai-agents/hermes-incident-commander
hermes skills install autonomous-ai-agents/hermes-patterns
hermes skills install mlops/vllm
hermes skills install mlops/transformers
```

---

## 8. Stars 排行榜

### 8.1 全平台 Top 10

| 排名 | Skill | Stars | 平台 | 描述 |
|------|-------|-------|------|------|
| 🥇 | **everything-claude-code** | ⭐ 32,880 | Claude Code | Agent Harness 性能优化 |
| 🥈 | **antigravity-awesome-skills** | ⭐ 4,554 | 跨平台 | 1,400+ 可安装 Skills |
| 🥉 | **awesome-claude-skills** | ⭐ 27,053 | Claude Code | Claude Skills 精选 |
| 4 | **Anthropic-Cybersecurity-Skills** | ⭐ 2,000+ | Claude Code | 754 网络安全 Skills |
| 5 | **arkhe-claude-plugins** | ⭐ 2,500+ | Claude Code | 109 组件、22 Agents |
| 6 | **ai-dev-kit** | ⭐ 2,000+ | 跨平台 | 59 Skills、33 Agents |
| 7 | **trailofbits/skills** | ⭐ 3,000+ | Claude Code | 安全研究、漏洞检测 |
| 8 | **specops** | ⭐ 2,000+ | Claude Code | 自主 TDD Agent 团队 |
| 9 | **awesome-agent-skills** | ⭐ 1,000+ | 跨平台 | 1,000+ Agent Skills |
| 10 | **upstack** | ⭐ 1,600+ | Claude Code | Red/Green TDD |

### 8.2 分类排行榜

**TDD/Testing**

| Skill | Stars | 链接 |
|-------|-------|------|
| **upstack** | ⭐ 1,600+ | [GitHub](https://github.com/Upsolve-Labs/upstack) |
| **testing-best-practices** | ⭐ 800+ | [GitHub](https://github.com/adewale/testing-best-practices) |
| **specops** | ⭐ 2,000+ | [GitHub](https://github.com/meganide/specops) |

**Security**

| Skill | Stars | 链接 |
|-------|-------|------|
| **trailofbits/skills** | ⭐ 3,000+ | [GitHub](https://github.com/trailofbits/skills) |
| **claude-code-owasp** | ⭐ 1,500+ | [GitHub](https://github.com/agamm/claude-code-owasp) |
| **Anthropic-Cybersecurity-Skills** | ⭐ 2,000+ | [GitHub](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) |

**Git/Workflow**

| Skill | Stars | 链接 |
|-------|-------|------|
| **git-workflow-skill** | ⭐ 900+ | [GitHub](https://github.com/netresearch/git-workflow-skill) |
| **claude-git-expert** | ⭐ 600+ | [GitHub](https://github.com/IncomeStreamSurfer/claude-git-expert) |

---

## 9. 快速参考表

### 9.1 按需求选择

| 需求 | 首选 | 备选 |
|------|------|------|
| **TDD 开发** | upstack | testing-best-practices |
| **安全审计** | trailofbits/skills | claude-code-owasp |
| **代码审查** | code-review-skill | pragmatic-clean-code-reviewer |
| **架构设计** | claude-architecture-skills | arkhe-claude-plugins |
| **Git 工作流** | git-workflow-skill | claude-git-expert |
| **医疗健康** | OpenClaw-Medical-Skills | - |
| **企业集成** | awesome-openclaw-agent-packs | awesome-OPC-lark-cli-skills |
| **SRE 自动化** | hermes-incident-commander | hermes-patterns |

### 9.2 安装命令速查

```bash
# Claude Code - TDD
git clone https://github.com/Upsolve-Labs/upstack ~/.claude/skills/upstack

# Claude Code - Security
git clone https://github.com/trailofbits/skills ~/.claude/skills/trailofbits

# Claude Code - Workflow
git clone https://github.com/netresearch/git-workflow-skill ~/.claude/skills/git-workflow

# OpenClaw - Medical
clawhub install FreedomIntelligence/OpenClaw-Medical-Skills

# Hermes - Autonomous
hermes skills install autonomous-ai-agents/hermes-incident-commander

# Cross-platform
git clone https://github.com/noah-sheldon/ai-dev-kit ~/.claude/skills/ai-dev-kit
```

---

## 10. 相关资源

| 资源 | 链接 |
|------|------|
| awesome-claude-code | [GitHub](https://github.com/hesreallyhim/awesome-claude-code) |
| VoltAgent/awesome-agent-skills | [GitHub](https://github.com/VoltAgent/awesome-agent-skills) |
| Antigravity | [GitHub](https://github.com/sickn33/antigravity-awesome-skills) |
| everything-claude-code | [GitHub](https://github.com/affaan-m/everything-claude-code) |
| ai-dev-kit | [GitHub](https://github.com/noah-sheldon/ai-dev-kit) |
| OpenClaw-Medical-Skills | [GitHub](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) |
| hermes-incident-commander | [GitHub](https://github.com/Lethe044/hermes-incident-commander) |

---

## 11. 更新日志

| 日期 | 更新内容 |
|------|----------|
| 2026-04-21 | 新增 Best Skills 推荐榜单，含 Stars 排行榜和场景化组合 |

---

*整理：墨鉴 | 2026-04-21*
