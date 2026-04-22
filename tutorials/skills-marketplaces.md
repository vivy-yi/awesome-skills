# Skills 市场与资源汇总

> **适合人群**：想了解 Skills 生态系统全貌的学习者
> **预计阅读时间**：20 分钟
> **更新日期**：2026-04-21

---

## 1. Skills 市场全景图

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           Skills 生态系统                                              │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │                         官方市场                                              │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐        │   │
│  │  │ Claude Code │ │ OpenClaw   │ │  Hermes    │ │  OpenCode  │        │   │
│  │  │   Skills   │ │  ClawHub   │ │ Skills Hub │ │   Skills   │        │   │
│  │  │   (17+)   │ │  (13k+)   │ │           │ │  (社区)    │        │   │
│  │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘        │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                     │
│  ┌─────────────────────────────────────────────────────────────────────────────┐   │
│  │                         社区 Awesome Lists                                   │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐        │   │
│  │  │ awesome-    │ │ awesome-    │ │ awesome-   │ │ awesome-   │        │   │
│  │  │ skills      │ │ claude-    │ │ openclaw   │ │  agents    │        │   │
│  │  │ (276 repos) │ │   skills   │ │            │ │  skills    │        │   │
│  │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘        │   │
│  └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. 官方 Skills 市场

### 2.1 Claude Code Skills

| 属性 | 值 |
|------|-----|
| **官方仓库** | [anthropics/skills](https://github.com/anthropics/skills) |
| **Star** | ⭐ 56,124 |
| **Skills 数量** | 17+ 官方 Skills |
| **市场地址** | [docs.anthropic.com](https://docs.anthropic.com/en/docs/claude-code/skills) |

**官方 Skills 列表**：

| Skill | 描述 |
|-------|------|
| `code-review` | 代码审查 |
| `git-commit` | Git 提交生成 |
| `docs` | 文档生成 |
| `test` | 测试生成 |
| `debug` | 调试辅助 |
| `refactor` | 重构建议 |

**安装方式**：
```bash
# 通过 GitHub 安装
claude skills install anthropics/skills/<skill-name>

# 或复制 SKILL.md 到 ~/.claude/skills/
```

---

### 2.2 OpenClaw ClawHub

| 属性 | 值 |
|------|-----|
| **市场地址** | [clawhub.ai](https://clawhub.ai/skills) |
| **Skills 数量** | 13,729+ |
| **CLI 工具** | `clawhub` |
| **官方文档** | [docs.openclaw.ai](https://docs.openclaw.ai) |

**热门 Skills 分类**：

| 分类 | 代表 Skills | 安装命令 |
|------|-----------|---------|
| **开发效率** | agent-commons, agentdo, active-maintenance | `clawhub install zanblayde-agent-commons` |
| **多 Agent 协作** | agent-team-orchestration, arc-agent-lifecycle | `clawhub install arminnaimi-agent-team-orchestration` |
| **搜索研究** | academic-research, arxiv-search-collector | `clawhub install rogersuperbuilderalpha-academic-research` |
| **创意工具** | movie-producer-scene, 3d-model-generation | `clawhub install eftalyurtseven-3d-model-generation` |
| **运维部署** | azure-devops, auto-pr-merger | `clawhub install pals-software-azure-devops` |

**批量安装脚本**：
```bash
# 开发效率
clawhub install zanblayde-agent-commons
clawhub install wrannaman-agentdo
clawhub install xiaowenzhou-active-maintenance

# 多 Agent 协作
clawhub install arminnaimi-agent-team-orchestration
clawhub install trypto1019-arc-agent-lifecycle
clawhub install sharbelayy-agent-audit
```

---

### 2.3 Hermes Agent Skills Hub

| 属性 | 值 |
|------|-----|
| **市场地址** | [skills.hermesagent.io](https://skills.hermesagent.io) |
| **Skills 数量** | 80+ 内置 + 50+ 可选 |
| **内置路径** | `skills/` |
| **可选路径** | `optional-skills/` |

**Skills 分类（三层架构）**：

```
Layer 1: 基础设施技能
├── autonomous-ai-agents (4) — claude-code, codex, opencode, hermes-agent
├── inference-sh (1) — 推理服务
└── mcp (2) — mcporter, native-mcp

Layer 2: 能力平台技能
├── creative (8) — excalidraw, manim-video, p5js
├── software-development (6) — plan, tdd, code-review
├── research (5) — arxiv, blogwatcher, llm-wiki
├── productivity (6) — notion, google-workspace, linear
├── devops (1) — webhook-subscriptions
├── mlops (25+) — vllm, llama-cpp, transformers
└── data-science (1) — jupyter-live-kernel

Layer 3: 垂直领域技能
├── github (5) — code-review, issues, pr-workflow
├── apple (4) — notes, reminders, findmy, imessage
├── gaming (2) — minecraft, pokemon
├── media (4) — gif-search, youtube-content
└── security (3) — 1password, oss-forensics, sherlock
```

---

### 2.4 OpenCode Skills

| 属性 | 值 |
|------|-----|
| **官方仓库** | [opencode](https://github.com/opencode) |
| **Skills 来源** | 社区生态 + OpenSkills |
| **兼容性** | provider-agnostic |

**获取 Skills 方式**：
```bash
# OpenSkills 通用加载器
npm install -g openskills

# 搜索社区 Skills
openskills search <keyword>

# 安装 Skills
openskills install <skill-name>
```

---

## 3. 社区 Awesome Lists

### 3.1 按平台分类

| 列表 | Star | 特点 |
|------|------|------|
| [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | ⭐ 4,554 | 200+ Skills for Claude Code/Antigravity/Cursor |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | ⭐ 27,053 | Claude Skills 精选 |
| [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | ⭐ 32,880 | 完整配置集合 |
| [ZeroLu/awesome-openclaw](https://github.com/ZeroLu/awesome-openclaw) | ⭐ 53 | OpenClaw 教程和 Skills |
| [0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) | ⭐ 826 | Hermes Agent 资源和 Skills |

### 3.2 按用途分类

| 用途 | 推荐列表 |
|------|---------|
| **系统学习** | [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills) ⭐ 1,750 |
| **中文资料** | [libukai/awesome-agent-skills](https://github.com/libukai/awesome-agent-skills) ⭐ 1,309 |
| **学术研究** | [baibizhe/Awesome-Skills-Paper](https://github.com/baibizhe/Awesome-Skills-Paper) ⭐ 213 |
| **Workflow** | [ithiria894/awesome-claude-code-workflows](https://github.com/ithiria894/awesome-claude-code-workflows) ⭐ 68 |

---

## 4. Skills 创建工具

### 4.1 官方工具

| 工具 | 用途 | 位置 |
|------|------|------|
| `init_skill.py` | 创建 Skill 框架 | OpenClaw 内置 |
| `package_skill.py` | 打包验证 | OpenClaw 内置 |
| `skill-creator` | Skill 创建框架 | ClawHub |

### 4.2 社区工具

| 工具 | Star | 特点 | 安全 |
|------|------|------|------|
| [skill-builder](https://clawhub.ai/skills/skill-builder) | ⭐ 13 | 渐进式披露最佳实践 | ✅ |
| [skill-test](https://clawhub.ai/skills/skill-test) | ⭐ 2 | 沙箱测试 | ✅ |
| [Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | ⭐ 8,243 | 文档→Skill 转换 | ✅ |
| [skill-forge](https://clawhub.ai/skills/skill-forge) | ⭐ 0 | 全自动流水线 | ⚠️ |
| [mcp-to-skill-converter](https://github.com/GBSOSS/-mcp-to-skill-converter) | ⭐ 112 | MCP→Skill 转换 | ✅ |

### 4.3 推荐工具链

```bash
# 场景 1: 从零创建新 Skill
python3 init_skill.py --name my-skill          # 初始化
clawhub install skill-builder                   # 获取方法论
clawhub install skill-test                      # 测试

# 场景 2: 从文档转换 Skill
clawhub install Skill_Seekers                  # 文档扫描
openskills convert <doc-url>                   # 转换为 Skill

# 场景 3: MCP 服务器转 Skill
mcp-to-skill-converter <server-name>           # 转换
```

---

## 5. Skills 生态统计

### 5.1 规模统计

| 指标 | 数值 |
|------|------|
| **Awesome Lists** | 276+ repositories |
| **Skills 总量** | 14,437+ skills |
| **覆盖平台** | Claude Code, OpenClaw, Hermes, OpenCode, Cursor |
| **最大集合** | jeremylongshore (3,143 skills) |

### 5.2 Skills 分布

```
Skills 规模分布：
├── 🏆 Mega (>1000): 5 repos, 10,668 skills (73.9%)
├── 📦 Large (100-999): 7 repos, 1,867 skills (12.9%)
├── 📝 Medium (50-99): 8 repos, 574 skills (4.0%)
└── 🔹 Small (<50): 154 repos, 1,328 skills (9.2%)
```

---

## 6. 快速入门

### 6.1 Claude Code 用户

```bash
# 1. 查看官方 Skills
claude skills list

# 2. 安装社区热门 Skills
claude skills install anthropics/skills/code-review
claude skills install anthropics/skills/test

# 3. 创建自定义 Skill
# 复制 SKILL.md 到 ~/.claude/skills/
```

### 6.2 OpenClaw 用户

```bash
# 1. 搜索 Skills
clawhub search <keyword>

# 2. 安装 Skills
clawhub install <skill-name>

# 3. 查看已安装
openclaw skills list

# 4. 创建自定义 Skill
python3 init_skill.py --name my-skill
```

### 6.3 Hermes Agent 用户

```bash
# 1. 浏览内置 Skills
hermes skills browse

# 2. 搜索可选 Skills
hermes skills search <query>

# 3. 安装可选 Skill
hermes skills install <identifier>

# 4. 创建自定义 Skill
# 在 skills/ 目录创建 SKILL.md
```

---

## 7. 相关资源

### 7.1 核心框架

| 资源 | 链接 |
|------|------|
| Anthropic Skills | [GitHub](https://github.com/anthropics/skills) |
| Superpowers | [GitHub](https://github.com/obra/superpowers) |
| AgentSkills 规范 | [GitHub](https://github.com/agentskills/agentskills) |

### 7.2 市场平台

| 平台 | 特点 | 适合谁 | 链接 |
|------|------|--------|------|
| **SkillsMP** | 模板商店，已有 36 万+ Skills | 想挑成品技能包的 | [skillsmp.com](https://skillsmp.com/) |
| **agent-skills.md** | 收录 6000+ 常用技能，强调直接可用 | 想快速上手，不想自己写的 | [agent-skills.md](https://www.agent-skills.md) |
| **Agent Skills Me** | 人工精选，"精而少" | 不想花时间筛选的 | [agentskills.me](https://agentskills.me) |
| **Skills Directory** | Reddit 社区推荐，偏口碑榜单 | 想看真实评价再决定的 | [skills.directory](https://skills.directory) |
| **SkillStore** | 中文友好，经过安全审查 | 团队使用或合规敏感场景 | [skillstore.ai](https://skillstore.ai) |
| **Skills.sh** | 热门趋势技能，支持一键安装 | 想快速尝鲜新技能的 | [skills.sh](https://skills.sh) |
| **aitmpl.com/skills** | Claude Code 模板集合 | Claude Code 用户 | [aitmpl.com/skills](https://aitmpl.com/skills) |
| **ClawHub** | OpenClaw 官方，13k+ Skills | 企业用户/飞书集成 | [clawhub.ai](https://clawhub.ai/skills) |
| **Hermes Skills Hub** | Hermes 官方，80+ 内置 + 50+ 可选 | MLOps/AI 研究 | [skills.hermesagent.io](https://skills.hermesagent.io) |
| **AgentSkills.io** | 通用 Skills 市场 | 跨平台用户 | [agentskills.io](https://agentskills.io/) |

### 7.3 教程

| 教程 | 位置 |
|------|------|
| Core Frameworks Deep Dive | [tutorials/core-frameworks-deep-dive.md](./core-frameworks-deep-dive.md) |
| MCP Protocol Deep Dive | [tutorials/mcp-protocol-deep-dive.md](./mcp-protocol-deep-dive.md) |
| SKILL.md Pattern | [tutorials/the-skill-md-pattern.md](./the-skill-md-pattern.md) |

---

## 8. 更新日志

| 日期 | 更新内容 |
|------|---------|
| 2026-04-21 | 新增 7 个 Skills 市场平台（SkillsMP、agent-skills.md、Agent Skills Me、Skills Directory、SkillStore、Skills.sh、aitmpl.com/skills）及详细特点描述 |
| 2026-04-21 | 整合 OpenClaw/Hermes 官方文档，添加三层架构分析 |
| 2026-04-19 | 新增 Skills 市场资源汇总 |

---

*整理：墨鉴 | 2026-04-21*
