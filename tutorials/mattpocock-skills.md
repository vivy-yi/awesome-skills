# Matt Pocock's Agent Skills — 生产级工程技能集

> **深度调研教程** | 时长：约 40 分钟 | 更新：2026-04-27

## 目录

1. [概述](#1-概述)
2. [安装与配置](#2-安装与配置)
3. [核心设计理念](#3-核心设计理念)
4. [技能全解](#4-技能全解)
   - [规划与设计技能](#规划与设计技能)
   - [开发技能](#开发技能)
   - [工具与配置技能](#工具与配置技能)
   - [写作与知识技能](#写作与知识技能)
5. [关键技能深度剖析](#5-关键技能深度剖析)
   - [TDD 技能详解](#tdd-技能详解)
   - [to-prd 技能详解](#to-prd-技能详解)
   - [ubiquitous-language 技能详解](#ubiquitous-language-技能详解)
   - [write-a-skill 技能详解](#write-a-skill-技能详解)
   - [triage-issue 技能详解](#triage-issue-技能详解)
6. [与 addyosmani/agent-skills 对比](#6-与-addyosmaniagent-skills-对比)
7. [最佳实践](#7-最佳实践)
8. [常见陷阱](#8-常见陷阱)
9. [集成与扩展](#9-集成与扩展)
10. [总结与选型建议](#10-总结与选型建议)

---

## 1. 概述

### 1.1 什么是 mattpocock/skills

**mattpocock/skills** 是 TypeScript 布道者 Matt Pocock（@mattpocockuk）维护的个人 AI Agent 技能目录，收录了他在真实工程实践中每日使用的 21 个生产级技能。

- **GitHub**: https://github.com/mattpocock/skills
- **Stars**: 24,504（2026-04-27），其中 2,519 今日新增
- **安装方式**: `npx skills@latest add mattpocock/skills/<skill-name>`
- **定位**: "Agent Skills for real engineers. Straight from my .claude directory."

### 1.2 核心理念：反"Vibe Coding"

Matt Pocock 在多个公开场合强调，他的技能集是**反 vibe coding（氛围编码）**的——不是给 AI 丢一句模糊需求然后等它"感觉对"，而是用结构化的工程方法引导 AI Agent。

**核心区别**：

| 维度 | Vibe Coding | mattpocock/skills |
|------|-------------|-------------------|
| 需求处理 | 一次性描述所有需求 | 渐进式 PRD + 用户访谈 |
| 测试策略 | 边写边测或最后补测 | TDD 垂直切片优先 |
| 架构决策 | AI 自主决定 | 明确接口 + DDD 语言 |
| 进度控制 | 全量实现后 review | 垂直切片可独立交付 |
| 安全防护 | 信任 AI 的 git 操作 | git-guardrails 主动拦截 |

### 1.3 与其他 Skills 集合的差异

| 特性 | mattpocock/skills | addyosmani/agent-skills | antigravity-awesome-skills |
|------|-------------------|------------------------|---------------------------|
| **规模** | 21 个精选 | 7 大斜杠命令 | 1,370+ 可安装 |
| **定位** | 个人工程实践 | Google 工程标准 | 社区大杂烩 |
| **粒度** | 小而锐利（单一职责） | 中等（命令式） | 粗细不一 |
| **安装方式** | npx skills@latest | 手动复制 | 各仓库独立 |
| **文档深度** | 每个技能都有深度文档 | 简短描述 | 参差不齐 |
| **控制词汇** | ✅ LANGUAGE.md 体系 | ❌ | ❌ |

### 1.4 技能分类总览

```
mattpocock/skills
├── Planning & Design (5个)
│   ├── to-prd              # 对话 → PRD GitHub Issue
│   ├── to-issues          # PRD → 垂直切片 Issues
│   ├── grill-me           # Socratic 追问直到决策树清晰
│   ├── design-an-interface # 并行子 Agent 多方案设计
│   └── request-refactor-plan # 重构计划 via 用户访谈
├── Development (5个)
│   ├── tdd                # 红-绿-重构循环
│   ├── triage-issue       # Bug 调查 → TDD 修复计划
│   ├── improve-codebase-architecture # 架构改进机会发现
│   ├── migrate-to-shoehorn # TypeScript 类型迁移
│   └── scaffold-exercises # 练习目录结构搭建
├── Tooling & Setup (2个)
│   ├── setup-pre-commit   # Husky + lint-staged 配置
│   └── git-guardrails-claude-code # Git 危险操作拦截
├── Writing & Knowledge (4个)
│   ├── write-a-skill      # 技能编写方法论
│   ├── edit-article       # 文章重构与润色
│   ├── ubiquitous-language # DDD 通用语言提取
│   └── obsidian-vault     # Obsidian 笔记管理
└── Additional (5个+)
    ├── caveman            # 洞穴人法则（简单性优先）
    ├── domain-model        # 领域模型检查
    ├── github-triage       # GitHub Issue 分类
    ├── qa                 # QA 工作流
    └── zoom-out           # 拉远视角看全局
```

---

## 2. 安装与配置

### 2.1 前置要求

- Node.js 18+
- npm 或 pnpm
- 支持 skills 协议的 Agent（Claude Code、OpenClaw 等）

### 2.2 安装单个技能

```bash
# 安装 TDD 技能
npx skills@latest add mattpocock/skills/tdd

# 安装 to-prd 技能
npx skills@latest add mattpocock/skills/to-prd

# 安装全部技能
npx skills@latest add mattpocock/skills/<each-skill>
```

### 2.3 验证安装

技能安装后会出现在项目的 `.claude/skills/` 或对应 Agent 的技能目录中：

```bash
# 查看已安装的 mattpocock 技能
ls -la .claude/skills/mattpocock/

# 或查看技能描述
cat .claude/skills/mattpocock/tdd/SKILL.md | head -20
```

### 2.4 与 OpenClaw 集成

在 OpenClaw 中，技能会自动注册到可用技能列表。触发方式：

- **自动触发**: 当 Agent 检测到技能描述中的关键词时自动加载
- **手动触发**: 用户明确调用 `/skill tdd` 或类似命令

---

## 3. 核心设计理念

### 3.1 单一职责原则

每个技能只做**一件事**，但做到极致。例如：

- `tdd`: 只关注红-绿-重构循环，不包含测试工具配置
- `to-prd`: 只做对话 → PRD 转换，不做项目管理

### 3.2 垂直切片优先

这是 mattpocock/skills 最核心的方法论。**垂直切片**指的是：

> 一个端到端可工作的功能片段，覆盖从 UI 到数据库的完整层次。

**水平切片（错误）**：
```
RED: 写所有测试（test_auth.py, test_products.py, test_orders.py...）
GREEN: 写所有实现
```
→ 测试基于想象的行为，而非实际需求；最后发现架构不匹配。

**垂直切片（正确）**：
```
RED→GREEN: test_checkout → 实现 checkout 完整链路
RED→GREEN: test_refund → 实现 refund 完整链路
...
```
→ 每个切片都可独立交付和验证。

### 3.3 控制词汇（LANGUAGE.md 体系）

mattpocock 强调在项目中建立**一致的领域术语表**。技能中大量使用：

- **Deep Module**: 小接口、大实现的模块（如 `JSON.parse`）
- **Shallow Module**: 大接口、浅实现的模块（需要避免）
- **Ubiquitous Language**: 团队共享的领域术语
- **Vertical Slice**: 端到端功能片段

### 3.4 行为验证而非实现验证

测试应该验证**公开行为**（API 响应、UI 状态），而非**内部实现**（私有方法、数据库结构）。

**好测试**：
```typescript
test('user can checkout with valid cart', async () => {
  const cart = createCartWithItems();
  const order = await checkout(cart);
  expect(order.status).toBe('confirmed');
});
```

**坏测试**：
```typescript
test('checkout calls createOrder and saveToDatabase', () => {
  const mockDb = jest.fn();
  await checkout(cart, mockDb);
  expect(mockDb).toHaveBeenCalledWith('orders', expect.anything());
});
```

---

## 4. 技能全解

### 规划与设计技能

#### 4.1.1 to-prd

**描述**: 将当前对话上下文转化为 PRD（产品需求文档），并提交为 GitHub Issue。

**使用场景**：
- 用户想要创建新功能但只有模糊想法
- 需要将讨论结果正式化为文档
- 想要一个可追踪的需求记录

**工作流**：
1. 探索代码库了解当前状态
2. 草拟需要构建/修改的主要模块
3. 主动寻找可提取为深模块的机会
4. 用 PRD 模板撰写并通过 `gh issue create` 提交

**PRD 模板结构**：
- Problem Statement（用户视角的问题）
- Solution（用户视角的解决方案）
- User Stories（详细用户故事）
- Implementation Decisions（实现决策，不含具体代码）
- Testing Decisions（测试决策）
- Out of Scope
- Further Notes

**触发词**: "create a PRD", "turn this into a spec", "write a product requirement"

---

#### 4.1.2 to-issues

**描述**: 将 PRD 或计划拆解为独立的、可领取的 GitHub Issues，使用垂直切片策略。

**使用场景**：
- PRD 完成后需要分解为可执行任务
- 需要确保每个 Issue 独立可工作

**核心原则**：
- 每个 Issue 是一个垂直切片（端到端功能）
- Issue 之间无隐式依赖
- 每个 Issue 有清晰的验收标准

**触发词**: "break this into issues", "create tickets", "slice this vertically"

---

#### 4.1.3 grill-me

**描述**: Socratic 追问技能——对计划或设计进行无情追问，直到决策树的每个分支都被解决。

**使用场景**：
- 设计方案有未考虑到的边界情况
- 需要挑战假设
- 避免过早承诺

**工作方式**：
- Agent 提出尖锐问题
- 用户回答后，Agent 继续追问基于该答案的隐含假设
- 循环直到"我不知道"变成"已考虑"

**触发词**: "grill me", "challenge this", "what am I missing"

---

#### 4.1.4 design-an-interface

**描述**: 使用并行子 Agent 生成模块的多个完全不同设计选项。

**使用场景**：
- 接口设计初期需要探索多种可能
- 想要对比不同方案的权衡

**工作方式**：
- 主 Agent 协调多个子 Agent
- 每个子 Agent 提出一个完全不同的设计方案
- 用户选择或混合

**触发词**: "design alternatives", "multiple interface designs", "compare approaches"

---

#### 4.1.5 request-refactor-plan

**描述**: 通过用户访谈创建详细的重构计划，包含小提交粒度，然后提交为 GitHub Issue。

**使用场景**：
- 需要重构但不确定范围
- 想要渐进式重构而非大规模重写

**工作方式**：
- Agent 询问一系列问题了解现状
- 生成小步提交的重构计划
- 提交为 Issue 供后续执行

**触发词**: "refactor plan", "we need to clean this up", "restructure"

---

### 开发技能

#### 4.2.1 tdd（核心技能）

**描述**: 测试驱动开发，使用红-绿-重构循环，每次构建一个垂直切片功能或修复一个 Bug。

**核心原则**：
- 测试验证行为，不验证实现
- 一次只写一个测试
- 垂直切片优先（不是水平切片——不是先写完所有测试再写代码）

**工作流**：
```
1. 规划阶段
   - 确认接口变更
   - 确认要测试的行为（按优先级）
   - 识别深模块机会
   - 设计可测试的接口
   - 获取用户对计划的批准

2. tracer bullet
   - RED: 写第一个行为的测试 → 测试失败
   - GREEN: 写最小代码通过测试 → 测试通过

3. 增量循环
   - RED: 写下个测试 → 失败
   - GREEN: 最小代码通过 → 通过

4. 重构
   - 提取重复
   - 加深模块
   - 应用 SOLID 原则
   - 每步重构后运行测试
```

**禁止行为**：
- ❌ 先写所有测试，再写所有实现（水平切片）
- ❌ 测试私有方法
- ❌ 用 mock 替代真实协作对象（过度使用）
- ❌ 在 RED 状态下重构

**触发词**: "TDD", "red-green-refactor", "test-first", "write tests first"

---

#### 4.2.2 triage-issue

**描述**: 调查 Bug，探索代码库找到根因，然后创建带 TDD 修复计划的 GitHub Issue。

**使用场景**：
- 用户报告了 Bug
- 需要系统化调查和规划修复

**工作流**：
1. 从用户获取问题描述
2. 使用 Explore 子 Agent 深入调查代码库
3. 找到 bug 位置、涉及代码路径、失败原因
4. 设计 TDD 修复计划（有序的 RED-GREEN 循环）
5. 用 `gh issue create` 创建 Issue

**关键要求**：
- 最小化向用户提问（mostly hands-off）
- Issue 中描述行为和契约，不描述内部结构
- 测试通过公开接口验证

**触发词**: "triage", "investigate this bug", "find the root cause"

---

#### 4.2.3 improve-codebase-architecture

**描述**: 在代码库中寻找架构深化机会，受 `CONTEXT.md` 中的领域语言和 `docs/adr/` 中的决策指导。

**使用场景**：
- 想要改进现有代码架构
- 需要识别可以加深的核心模块

**参考文件**：
- `CONTEXT.md`: 项目领域语言
- `docs/adr/`: 架构决策记录

**触发词**: "improve architecture", "deepen this module", "refactor for better design"

---

#### 4.2.4 migrate-to-shoehorn

**描述**: 将测试文件从 `as` 类型断言迁移到 `@total-typescript/shoehorn`。

**使用场景**：
- 需要更严格的类型测试
- 从宽松类型升级到严格类型

**触发词**: "migrate to shoehorn", "use @total-typescript/shoehorn"

---

#### 4.2.5 scaffold-exercises

**描述**: 创建练习目录结构，包含章节、问题、解决方案和解释器。

**使用场景**：
- 制作编程练习
- 搭建学习材料结构

**触发词**: "scaffold exercises", "create practice problems", "setup exercise structure"

---

### 工具与配置技能

#### 4.3.1 setup-pre-commit

**描述**: 配置 Husky 预提交钩子，包含 lint-staged、Prettier、类型检查和测试。

**工作流**：
- 安装 Husky
- 配置 lint-staged
- 设置 Prettier
- 添加类型检查命令
- 添加测试命令

**触发词**: "setup pre-commit", "configure husky", "add pre-commit hooks"

---

#### 4.3.2 git-guardrails-claude-code

**描述**: 设置 Claude Code 钩子，在危险 git 命令执行前进行拦截。

**拦截的命令**：
- `git push --force`
- `git reset --hard`
- `git clean -f`
- 其他可能破坏性操作

**工作方式**：
- 添加 git 钩子脚本
- 在执行危险命令前提示确认
- 可选择跳过（skip）但需要明确意图

**触发词**: "git guardrails", "protect git commands", "block dangerous git operations"

---

### 写作与知识技能

#### 4.4.1 write-a-skill（技能编写方法论）

**描述**: 创建具有正确结构、渐进式披露和捆绑资源的新 Agent 技能。

**技能结构**：
```
skill-name/
├── SKILL.md           # 主指令（必需）
├── REFERENCE.md       # 详细文档（如需要）
├── EXAMPLES.md        # 使用示例（如需要）
└── scripts/           # 工具脚本（如需要）
    └── helper.js
```

**SKILL.md 模板**：
```yaml
---
name: skill-name
description: 能力简述。使用时机：[具体触发词]。
---

# Skill Name

## Quick start

[最小可工作示例]

## Workflows

[分步流程，包含复杂任务的检查清单]

## Advanced features

[链接到其他文件：参见 REFERENCE.md]
```

**描述写作规范**：
- 最多 1024 字符
- 第三人称
- 第一句：做什么
- 第二句：何时触发

**好描述**：
```
从 PDF 文件提取文本和表格，填写表单，合并文档。
使用时机：处理 PDF 文件、提到 PDF/表单/文档提取。
```

**触发词**: "write a skill", "create a new skill", "build a skill"

---

#### 4.4.2 edit-article

**描述**: 通过重构章节、提高清晰度、收紧散文来编辑和改进文章。

**使用场景**：
- 改进文档
- 润色技术文章

**工作方式**：
- 重构章节结构
- 提高语言清晰度
- 收紧冗余内容

**触发词**: "edit this article", "improve the writing", "tighten this prose"

---

#### 4.4.3 ubiquitous-language（DDD 通用语言）

**描述**: 从当前对话中提取 DDD 风格的通用语言词汇表，标记歧义并提出规范术语。保存到 `UBIQUITOUS_LANGUAGE.md`。

**核心概念**：
- **歧义**: 同一词用于不同概念
- **同义词**: 不同词用于同一概念
- **模糊术语**: 需要明确的术语

**输出格式**：
- 按领域分组的多张表（术语、定义、避免的别名）
- 关系描述（用粗体术语名）
- 示例对话（展示术语如何在实践中使用）
- 标记的歧义

**关键规则**：
- 有主见——选择最佳术语并列出别名
- 明确标记冲突
- 只包含领域专家相关的术语
- 定义保持简洁（一句话）
- 显示关系（用粗体）
- 写示例对话（3-5 轮）

**触发词**: "define domain terms", "build a glossary", "create ubiquitous language", "DDD"

---

#### 4.4.4 obsidian-vault

**描述**: 在 Obsidian 保险库中搜索、创建和管理笔记，使用 wikilinks 和索引笔记。

**使用场景**：
- 管理项目知识库
- 维护决策记录

**触发词**: "search obsidian", "manage notes", "update vault"

---

## 5. 关键技能深度剖析

### 5.1 TDD 技能详解

#### 哲学基础

**核心原则**: 测试应该通过公开接口验证行为，而非验证实现细节。代码可以完全改变，测试不应该随之失效。

**好测试是集成风格的**: 它们通过公开 API 真实地运行代码路径。它们描述系统**做什么**，而不是**怎么做**。

**坏测试耦合到实现**: 它们 mock 内部协作对象，测试私有方法，或通过外部手段验证。警告信号：重构后测试失败，但行为没变。

#### 垂直切片 vs 水平切片

**水平切片（错误）**：
```
WRONG:
  RED:   test1, test2, test3, test4, test5
  GREEN: impl1, impl2, impl3, impl4, impl5
```

**垂直切片（正确）**：
```
RIGHT:
  RED→GREEN: test1→impl1
  RED→GREEN: test2→impl2
  RED→GREEN: test3→impl3
  ...
```

#### 工作流详解

**1. 规划阶段（必须）**：
- [ ] 与用户确认接口变更
- [ ] 确认要测试的行为（按优先级）
- [ ] 识别深模块机会
- [ ] 设计可测试接口
- [ ] 列出要测试的行为（不是实现步骤）
- [ ] 获得用户对计划的批准

**关键问题**: "公开接口应该是什么样？哪些行为最重要？"

**2. Tracer Bullet**:
```
RED:   写第一个行为的测试 → 测试失败
GREEN: 写最小代码通过 → 测试通过
```

**3. 增量循环**:
- 一次一个测试
- 只写刚好够通过当前测试的代码
- 不预测未来测试
- 保持测试专注于可观察行为

**4. 重构（只在 GREEN 状态）**:
- [ ] 提取重复
- [ ] 加深模块（将复杂性隐藏在简单接口后）
- [ ] 应用 SOLID 原则
- [ ] 考虑新代码对现有代码的揭示
- [ ] 每次重构后运行测试

#### 每个循环的检查清单

```
[ ] 测试描述行为，不描述实现
[ ] 测试只使用公开接口
[ ] 测试在内部重构后仍能存活
[ ] 代码对于这个测试是最小的
[ ] 没有添加投机性功能
```

---

### 5.2 to-prd 技能详解

#### 与传统 PRD 的区别

传统 PRD 通常是：
- 冗长的文档
- 包含大量实现细节
- 容易过时

**to-prd 产出的 PRD**：
- 以用户视角为核心
- 强调行为和契约
- 包含测试决策（验证行为的方式）
- 不包含具体代码路径（保持文档稳定）

#### PRD 模板核心部分

**User Stories 格式**：
```markdown
1. As an <actor>, I want <feature>, so that <benefit>
```

**Implementation Decisions**：
- 要构建/修改的模块
- 要修改的模块接口
- 技术澄清
- 架构决策
- Schema 变更
- API 契约
- 特定交互

**不包含**：具体文件路径、代码片段（会很快过时）

**Testing Decisions**：
- 什么样的测试是好测试（只测外部行为，不测实现细节）
- 哪些模块需要测试
- 测试的先例（代码库中类似测试的参考）

#### 使用示例

```
用户：我想给电商网站加一个积分系统
Agent：好的，让我先探索一下代码库...
[探索完成后]
Agent：我已经草拟了模块划分，包括：
- LoyaltyAccount（积分账户）
- PointTransaction（积分交易）
- RedemptionEngine（兑换引擎）

这些模块可以独立测试。让我确认：
1. 你希望哪些模块有测试？
2. 积分计算规则是什么（比如 1 元 = 1 分，还是有分层？）


```

---

### 5.3 ubiquitous-language 技能详解

#### 核心价值

在团队中建立**一致的领域术语**，避免沟通中的歧义和误解。

#### 输出文件格式

`UBIQUITOUS_LANGUAGE.md` 结构：

```markdown
# Ubiquitous Language

## [领域分组名称]

| 术语 | 定义 | 要避免的别名 |
|------|------|-------------|
| **Order** | 客户购买请求 | Purchase, transaction |

## 关系

- 一个 **Invoice** 属于一个 **Customer**
- 一个 **Order** 产生一个或多个 **Invoice**

## 示例对话

> **Dev:** "当 **Customer** 下 **Order** 时，我们立即创建 **Invoice** 吗？"
> **Domain expert:** "不——**Invoice** 只在 **Fulfillment** 确认后才生成。单个 **Order** 如果物品分批发货，可以产生多个 **Invoice**。"

## 标记的歧义

- "account" 被用来同时表示 **Customer** 和 **User**——这是两个不同的概念
```

#### 关键规则

1. **有主见**: 当多个词表达同一概念时，选择最好的，列出其他为别名
2. **明确标记冲突**: 如果术语在对话中有歧义，在"Flagged ambiguities"中明确指出
3. **只包含领域专家相关的术语**: 跳过模块名/类名（除非在领域语言中有意义）
4. **保持定义紧凑**: 最多一句话
5. **显示关系**: 用粗体术语名，必要时显示基数
6. **只包含领域术语**: 跳过通用编程概念（array、function、endpoint）除非有特定领域含义
7. **写示例对话**: 展示术语如何在实践中自然使用

#### 使用示例

```markdown
## Order lifecycle

| Term | Definition | Aliases to avoid |
|------|-----------|-----------------|
| **Order** | 客户购买请求 | Purchase, transaction |
| **Invoice** | 交付后发送给客户的付款请求 | Bill, payment request |

## Flagged ambiguities

- "shipment" 和 "fulfillment" 在对话中被混用。
  推荐使用 **Fulfillment** 表示确认发货的事件，**Shipment** 表示实际的物理运输。
```

---

### 5.4 write-a-skill 技能详解

#### 技能结构规范

```
skill-name/
├── SKILL.md           # 主指令（必需）
├── REFERENCE.md       # 详细文档（如果内容超过 500 行）
├── EXAMPLES.md        # 使用示例（如果需要）
└── scripts/           # 工具脚本（如果需要确定性操作）
    └── helper.js
```

#### SKILL.md 格式

```yaml
---
name: skill-name
description: 简短描述能力。使用时机：[具体触发词]。
---

# Skill Name

## Quick start

[最小可工作示例]

## Workflows

[分步流程，包含复杂任务的检查清单]

## Advanced features

[链接到单独文件：参见 REFERENCE.md]
```

#### 描述（Description）规范

描述是** Agent 决定加载哪个技能时唯一看到的东西**。它被放在系统提示中与其他已安装技能一起展示。

**目标**：给 Agent 足够信息知道：
1. 这个技能提供什么能力
2. 何时/为什么触发它（具体关键词、上下文、文件类型）

**格式要求**：
- 最多 1024 字符
- 第三人称
- 第一句：做什么
- 第二句："使用时机：[具体触发词]"

**好例子**：
```
从 PDF 文件提取文本和表格，填写表单，合并文档。
使用时机：处理 PDF 文件或提到 PDF、表单、文档提取。
```

**坏例子**：
```
帮助处理文档。
```

坏例子无法帮助 Agent 将其与其他文档技能区分开来。

#### 何时添加脚本

添加工具脚本当：
- 操作是确定性的（验证、格式化）
- 相同代码会被重复生成
- 错误需要明确处理

脚本节省 token 并提高可靠性。

#### 何时拆分文件

拆分为单独文件当：
- SKILL.md 超过 100 行
- 内容有不同领域（finance vs. sales schemas）
- 高级功能很少需要

#### 审查清单

完成后验证：
- [ ] 描述包含触发词（"使用时机..."）
- [ ] SKILL.md 在 100 行以内
- [ ] 无时间敏感信息
- [ ] 术语一致
- [ ] 包含具体示例
- [ ] 引用只深入一层

---

### 5.5 triage-issue 技能详解

#### 核心特点：Mostly Hands-off

大多数 Bug 分诊工作应该是**自动的**——尽量减少向用户提问。立即开始调查。

#### 工作流详解

**1. 捕获问题（最少提问）**：
- 获取用户的问题简述
- 如果用户没提供，问一个问题："你看到的问题是什么？"
- **不要追问**——立即开始调查

**2. 探索和诊断**：
使用 `Explore` 子 Agent 深入调查代码库，目标是找到：
- **哪里** bug 表现出来（入口点、UI、API 响应）
- **什么**代码路径涉及（追踪流程）
- **为什么**失败（根因，不是症状）
- **什么**相关代码存在（类似模式、测试、邻近模块）

**调查内容**：
- 相关源文件及其依赖
- 现有测试（测了什么，缺什么）
- 受影响文件的最近变更（`git log`）
- 代码路径中的错误处理
- 代码库中其他正常工作的类似模式

**3. 识别修复方法**：
- 修复根因所需的最小变更
- 受影响的模块/接口
- 需要通过测试验证的行为
- 这是回归、缺失功能还是设计缺陷

**4. 设计 TDD 修复计划**：
创建具体的、有序的 RED-GREEN 循环列表。每个循环是一个垂直切片：

- **RED**: 描述捕获 broken/missing 行为的特定测试
- **GREEN**: 描述使测试通过的最小代码变更

**规则**：
- 测试通过公开接口验证行为，不验证实现细节
- 一次一个测试，垂直切片
- 每个测试应该在内部重构后存活
- 包括最终重构步骤（如需要）
- **持久性**：只建议在重大代码库变更后仍能存活的修复。描述行为和契约，不描述内部结构。

**5. 创建 GitHub Issue**：
使用 `gh issue create` 创建 Issue，用模板格式。不要问用户审核——直接创建并分享 URL。

---

## 6. 与 addyosmani/agent-skills 对比

| 维度 | mattpocock/skills | addyosmani/agent-skills |
|------|-------------------|------------------------|
| **维护者** | Matt Pocock（TypeScript 布道者） | Addy Osmani（Google Chrome 工程师） |
| **技能数量** | 21 个精选 | 7 大斜杠命令 |
| **粒度** | 小而单一职责 | 中等粒度（命令式） |
| **哲学** | 反 vibe coding，工程实践优先 | 工程标准优先 |
| **测试方法** | 强推 TDD + 垂直切片 | 提到测试但非核心 |
| **文档深度** | 每个技能都有完整文档 | 简短描述 |
| **安装方式** | npx skills@latest | 手动复制 |
| **控制词汇** | ✅ 强推 LANGUAGE.md | ❌ |
| **Git 安全** | ✅ git-guardrails | ❌ |
| **学习曲线** | 中等（需要理解工程概念） | 较低（命令直接使用） |

### 互补使用建议

**可以同时使用两个集合**：
- 用 `addyosmani/agent-skills` 作为快速启动命令（`/spec`、`/review`、`/test`）
- 用 `mattpocock/skills` 作为深度工程实践指导（TDD、PRD 生成、架构改进）

---

## 7. 最佳实践

### 7.1 使用时机

| 技能 | 最佳使用时机 |
|------|-------------|
| `to-prd` | 功能讨论初期，从模糊想法开始 |
| `to-issues` | PRD 完成后，需要分解任务 |
| `grill-me` | 设计决策前，需要挑战假设 |
| `tdd` | 任何新功能开发或 Bug 修复 |
| `triage-issue` | 用户报告 Bug，需要系统调查 |
| `ubiquitous-language` | DDD 项目启动，或沟通出现歧义 |
| `git-guardrails` | 任何涉及危险 git 操作的项目 |
| `write-a-skill` | 需要创建新的自定义技能 |

### 7.2 技能组合使用

**新功能开发完整工作流**：
```
1. grill-me          # 挑战设计假设
   ↓
2. to-prd           # 生成 PRD
   ↓
3. to-issues        # 拆解为垂直切片 Issues
   ↓
4. tdd (每个 Issue)  # 垂直切片开发
   ↓
5. git-guardrails   # 安全 git 操作
```

**Bug 修复工作流**：
```
1. triage-issue     # 调查 + 生成 TDD 修复计划
   ↓
2. tdd              # 按计划执行修复
   ↓
3. improve-codebase-architecture  # 可选的架构改进
```

### 7.3 技能触发建议

- 当不确定用哪个技能时，优先选择**更具体**的那个
- `grill-me` 在设计早期使用，避免后期返工
- `ubiquitous-language` 在项目启动时建立，后续所有技能都受益
- `write-a-skill` 用于沉淀团队特定工作流为可复用技能

---

## 8. 常见陷阱

### 8.1 TDD 常见错误

**陷阱 1：水平切片**
```
❌ 先写所有测试，再写所有代码
```
→ 测试基于想象的行为，与实际需求脱节。

**陷阱 2：测试实现细节**
```
❌ mock 内部方法，测试私有逻辑
```
→ 重构后测试失败，但行为未变。

**陷阱 3：RED 状态下重构**
```
❌ 测试失败时开始"优化"代码
```
→ 破坏已验证的代码，引入新问题。

**陷阱 4：过多预规划**
```
❌ 在 RED 前详细设计每个测试
```
→ 浪费精力在不相关或不存在的行为上。

### 8.2 to-prd 常见错误

**陷阱：包含实现细节**
```markdown
❌ BAD:
- 在 `src/services/loyalty.ts` 添加 `calculatePoints` 方法

✅ GOOD:
- 添加积分计算模块，支持分层比率
```

### 8.3 ubiquitous-language 常见错误

**陷阱：包含技术术语**
```markdown
❌ BAD:
- `useState` - React 状态钩子
- `array.map()` - 数组转换方法

✅ GOOD:
- 只包含领域专家相关的术语
- 技术实现不属于领域语言
```

---

## 9. 集成与扩展

### 9.1 与 GitHub Actions 集成

可以将 triage-issue 的输出自动创建 Issue：

```yaml
# .github/workflows/bug-triage.yml
name: Bug Triage
on:
  issue_comment:
    types: [created]
jobs:
  triage:
    if: contains(github.event.comment.body, '/triage')
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Triage
        run: |
          # Agent 执行 triage-issue 技能
          claude --print --no-input "Run triage-issue for: ${{ github.event.issue.body }}"
```

### 9.2 与 CI/CD 集成

git-guardrails 可以集成到 CI 中作为额外安全层：

```yaml
# .github/workflows/ci.yml
- name: Git Guardrails Check
  run: |
    npx @mattpocock/git-guardrails check --dry-run
```

### 9.3 创建团队自定义技能

基于 mattpocock 方法论创建团队特定技能：

```markdown
# write-a-skill 示例：团队代码审查技能

---
name: team-code-review
description: 执行团队标准代码审查，检查安全性、性能和可维护性。
使用时机：需要进行代码审查、提到 review、PR 审查。
---

# Team Code Review

## 团队审查标准

### 安全性检查
- [ ] 无硬编码凭证
- [ ] 输入验证完整
- [ ] 权限检查正确

### 性能检查
- [ ] 无 N+1 查询
- [ ] 缓存使用恰当
- [ ] 大数据集处理合理

### 可维护性检查
- [ ] 命名清晰一致
- [ ] 文档完整
- [ ] 测试覆盖充分
```

---

## 10. 总结与选型建议

### 10.1 何时选择 mattpocock/skills

**适合场景**：
- ✅ 团队有扎实工程基础，追求高质量代码
- ✅ 采用 TDD/领域驱动设计
- ✅ 需要在 AI Agent 中保持工程纪律
- ✅ 项目复杂度高，需要结构化方法论

**不适合场景**：
- ❌ 快速原型/POC 阶段（技能开销过高）
- ❌ 团队工程经验不足（需要先建立基础）
- ❌ 简单脚本任务（用不上这些方法论）

### 10.2 与其他 Skills 集合的关系

```
addyosmani/agent-skills     ← 快速命令，标准工程实践
mattpocock/skills           ← 深度方法论，工程纪律
antigravity-awesome-skills  ← 工具箱，按需选用
```

### 10.3 入门建议

1. **第一天**：安装 `tdd`、`to-prd`、`git-guardrails`，开始在实际项目中使用
2. **第一周**：加入 `grill-me`、`ubiquitous-language`，建立团队术语
3. **第一个月**：深入 `write-a-skill`，将团队最佳实践沉淀为可复用技能

### 10.4 关键资源

- **GitHub**: https://github.com/mattpocock/skills
- **Newsletter**: https://www.aihero.dev/s/skills-newsletter（~60,000 开发者订阅）
- **配套视频**: Matt Pocock 的 YouTube 频道有大量技能使用演示

---

## 更新日志

| 日期 | 更新内容 |
|------|---------|
| 2026-04-27 | 初始版本，基于 mattpocock/skills 全面分析 |

---

> **相关调研**：本教程是墨鉴 awesome-skills 每周深度调研的一部分。相关主题：Addy Osmani Agent Skills、Self-Evolution Skills、Portable Agent Skills Architecture。
