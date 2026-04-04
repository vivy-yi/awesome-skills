# Core Frameworks 深度解析：Anthropic Skills 体系

> **适合人群**：想深入理解 Skills 核心机制的开发者
> **预计阅读时间**：30 分钟
> **来源**：基于 GitHub anthropics/skills (56k⭐) 官方仓库分析

---

## 1. Anthropic Skills 核心架构

### 1.1 设计理念

Anthropic Skills 的设计哲学是**渐进式披露（Progressive Disclosure）**：

```
┌─────────────────────────────────────────────────────────────┐
│                    SKILL.md 加载机制                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  用户查询 ──→ Agent 评估相关性 ──→ 加载 SKILL.md              │
│                              │                              │
│                              ▼                              │
│                    需要更多细节？                             │
│                              │                              │
│              ┌───────────────┼───────────────┐              │
│              ▼               ▼               ▼              │
│         FORMS.md         REFERENCE.md    EXAMPLES.md        │
│         (表单格式)        (参考文档)       (示例)            │
│              │               │               │              │
│              └───────────────┴───────────────┘              │
│                              │                              │
│                              ▼                              │
│                    按需加载，不浪费 Token                     │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 文件结构

```
skill-name/
├── SKILL.md          # 必需：技能入口，描述何时触发
├── FORMS.md          # 可选：表单格式定义
├── reference/        # 可选：参考文档目录
│   ├── setup.md      # 安装配置
│   ├── api.md        # API 参考
│   └── ...
├── examples/         # 可选：示例目录
│   └── example-1.md  # 具体示例
├── scripts/          # 可选：可执行脚本
│   └── run.sh        # 自动化脚本
├── assets/           # 可选：静态资源
│   └── diagram.png   # 图表
└── evals/            # 可选：测试评估
    └── eval.json     # 测试用例
```

### 1.3 SKILL.md 标准格式

```markdown
---
name: skill-name
description: 简短描述（1-2句话），说明这个 Skill 做什么
version: 1.0.0
tags: [tag1, tag2, tag3]
trigger: "当用户说...时触发"
---

# Skill 名称

## 概述
这个 Skill 的高级描述，解释它的目的和使用场景。

## 触发条件
- 当用户要求...
- 当任务涉及...
- 触发概率应达到 90%

## 使用指南

### 前提条件
- 条件 1
- 条件 2

### 步骤

#### 步骤 1: ...
描述...

#### 步骤 2: ...
描述...

### 代码示例

```language
// 示例代码
```

## 参考资料
详细文档链接：
- [详细指南](reference/guide.md)
- [API 参考](reference/api.md)

## 最佳实践

1. 最佳实践 1
2. 最佳实践 2

## 已知限制
- 限制 1
- 限制 2
```

---

## 2. SKILL.md 编写规范

### 2.1 必须字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | string | Skill 名称（英文、kebab-case） |
| `description` | string | 简短描述，1-2 句话 |

### 2.2 可选字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `version` | string | 版本号（语义化） |
| `tags` | array | 标签数组 |
| `trigger` | string | 触发条件描述 |
| `platforms` | array | 支持的平台 |

### 2.3 触发条件设计

**好的触发条件**：
```markdown
trigger: "当用户想要创建、编辑或优化一个 Skill 时触发"
```

**不好的触发条件**：
```markdown
trigger: "读取文件"  # 太宽泛，会频繁误触发
```

### 2.4 Description 优化技巧

**问题描述模式** → **技能编排模式**：

```
❌ "I need to read a file"
   → 太具体，只触发文件读取

✅ "I need to set up a project workspace"
   → 问题导向，触发完整的项目设置流程
```

---

## 3. Superpowers 框架深度解析

> **来源**：GitHub obra/superpowers (52k⭐)
> **定位**：将 AI Agent 训练成有纪律的软件工程师

### 3.1 核心原则

```
Superpowers 三大铁律：
┌─────────────────────────────────────────────────────────────┐
│  1. 设计先行 │ 写代码之前先设计                              │
│  2. 测试先行 │ 功能之前先写测试                              │
│  3. 审查贯穿 │ 每个任务之间都有结构化审查                     │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 工作流模式

#### 模式 A：TDD 开发流

```
┌──────────────────────────────────────────────────────────────┐
│                    TDD RED-GREEN-REFACTOR                     │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│   ┌─────┐    ┌─────┐    ┌────────────┐                       │
│   │ RED │ →  │GREEN│ →  │ REFACTOR  │ → 下一轮              │
│   │写测试│    │实现代码│    │优化代码    │                       │
│   │失败  │    │通过   │    │保持测试通过│                       │
│   └─────┘    └─────┘    └────────────┘                       │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

#### 模式 B：设计优先流程

```
用户需求 → 头脑风暴 → 规格说明 → 实现计划 → 执行
              ↓
         Socratic 提问确保设计质量
```

#### 模式 C：Subagent 审查流

```
┌─────────────────────────────────────────────────────────────┐
│                  两阶段 Subagent 审查                         │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│   代码完成 ──→ Subagent A 审查 ──→ 反馈 ──→ Subagent B 审查   │
│                            ↓                                  │
│                       人工确认                                 │
│                            ↓                                  │
│                       合并/丢弃                               │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

### 3.3 Skill 激活机制

```yaml
# Skill 激活配置示例
superpowers:
  skills:
    - name: planning
      trigger: "auto"  # 自动触发于每个任务开始
      
    - name: implementing
      trigger: "context"  # 根据上下文触发
      
    - name: debugging
      trigger: "error"  # 遇到错误时触发
      
    - name: reviewing
      trigger: "manual"  # 手动触发
```

### 3.4 Git Worktree 隔离

Superpowers 使用 Git Worktree 实现并行分支隔离：

```bash
# 自动创建隔离的 worktree
superpowers worktree create feature-x

# 在 worktree 中工作
cd ../feature-x-worktree

# 完成后合并或丢弃
superpowers worktree merge feature-x
```

---

## 4. AgentSkills 规范

> **来源**：GitHub agentskills/agentskills (7.6k⭐)
> **定位**：Agent Skills 的开放规范和文档

### 4.1 规范核心要素

```json
{
  "name": "skill-name",
  "version": "1.0.0",
  "description": "What this skill does",
  "triggers": [
    "When user wants to...",
    "When task involves..."
  ],
  "inputs": {
    "required": ["input1"],
    "optional": ["input2"]
  },
  "outputs": {
    "type": "result",
    "format": "markdown"
  },
  "dependencies": [],
  "constraints": []
}
```

### 4.2 跨平台兼容性

Skills 规范设计为跨平台兼容：

| 平台 | 支持度 | 说明 |
|------|--------|------|
| Claude Code | ✅ 完整 | 官方支持 |
| Codex | ✅ 完整 | 兼容 |
| OpenClaw | ✅ 完整 | 兼容 |
| Cursor | ⚠️ 部分 | 需适配 |
| Vercel v0 | ⚠️ 部分 | 有限支持 |

---

## 5. 实践：编写一个完整的 Skill

### 5.1 需求分析

假设我们要创建一个 **"React 性能优化"** Skill

### 5.2 目录结构

```
react-performance/
├── SKILL.md
├── FORMS.md
├── reference/
│   ├── setup.md
│   ├── common-issues.md
│   └── optimization-techniques.md
└── examples/
    ├── before-after.md
    └── case-study.md
```

### 5.3 SKILL.md 编写

```markdown
---
name: react-performance
description: React 组件性能优化技能，包括重渲染检测、bundle 优化、网络瀑布分析
version: 1.0.0
tags: [react, performance, frontend, optimization]
trigger: "当用户想要优化 React 性能、减少重渲染、或分析 bundle 大小时触发"
---

# React Performance Skill

## 概述
这个 Skill 帮助识别和修复 React 应用中的性能问题。

## 触发条件
- 用户要求"优化 React 性能"
- 用户抱怨"组件频繁重渲染"
- 用户想要"分析 bundle 大小"
- 用户要求"减少网络请求瀑布"

## 性能检查清单

### 1. React DevTools Profiler
使用 React DevTools Profiler 检查：
- 哪些组件频繁重渲染
- 渲染耗时多少
- 触发渲染的原因

### 2. Bundle 分析
```bash
npx source-map-explorer dist/*.js
# 或
npx webpack-bundle-analyzer
```

### 3. 常见问题检测

| 问题 | 症状 | 解决方案 |
|------|------|----------|
| 未优化的回调 | 每次渲染创建新函数 | useCallback |
| 未优化的值 | 每次渲染创建新对象 | useMemo |
| 不必要的重渲染 | 父组件更新导致子组件更新 | React.memo |
| 大列表 | 渲染大量项 | 虚拟化 |

### 4. 优化技术

#### useCallback 最佳实践
```jsx
// ❌ 错误：每次渲染创建新函数
<Button onClick={() => handleClick()} />

// ✅ 正确：缓存函数引用
const handleClick = useCallback(() => {
  // 处理逻辑
}, [dependency]);

<Button onClick={handleClick} />
```

#### React.memo 最佳实践
```jsx
// ❌ 错误：所有 props 变化都重渲染
const MyComponent = ({ title, onClick }) => (
  <div onClick={onClick}>{title}</div>
);

// ✅ 正确：只比较需要的 props
const MyComponent = React.memo(({ title, onClick }) => (
  <div onClick={onClick}>{title}</div>
), (prevProps, nextProps) => {
  // 自定义比较逻辑
  return prevProps.title === nextProps.title;
});
```

## 参考资料
- [React Profiler](reference/profiler-guide.md)
- [常见问题](reference/common-issues.md)
- [优化技术](reference/optimization-techniques.md)

## 示例
- [优化前后对比](examples/before-after.md)
- [真实案例](examples/case-study.md)
```

### 5.4 FORMS.md 编写

```markdown
# React Performance Audit Form

## 组件信息
- 组件名称：___________
- 组件路径：___________
- 问题描述：___________

## 性能指标
- 当前渲染时间：___________
- 重渲染频率：___________
- Bundle 大小：___________

## 检查项目
- [ ] 使用了 React DevTools Profiler？
- [ ] 运行了 bundle 分析？
- [ ] 识别了不必要的重渲染？
- [ ] 应用了 useCallback/useMemo？
- [ ] 考虑了虚拟化方案？
```

---

## 6. 最佳实践总结

### 6.1 Skill 设计原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **单一职责** | 每个 Skill 只做一件事 | "React 优化" 而不是 "前端全包" |
| **清晰触发** | 明确说明何时触发 | "当用户要求优化性能时" |
| **渐进披露** | 按需加载详细内容 | SKILL.md → REFERENCE.md |
| **可测试** | 提供测试用例 | eval.json 测试用例 |
| **版本管理** | 跟踪变更 | 语义化版本号 |

### 6.2 常见错误

❌ **描述太宽泛**
```markdown
description: "文件操作"
```
→ 几乎所有任务都会触发

❌ **缺少代码示例**
```markdown
## 使用方法
请按照最佳实践使用
```
→ Agent 无法理解具体操作

❌ **触发条件缺失**
```markdown
---
name: my-skill
---
# My Skill
...
```
→ Agent 不知道何时使用

✅ **正确的触发条件**
```markdown
trigger: "当用户想要创建一个新的 Skill 时触发"
```

---

## 7. 相关资源

- [Anthropic Skills 官方仓库](https://github.com/anthropics/skills)
- [Superpowers 框架](https://github.com/obra/superpowers)
- [AgentSkills 规范](https://github.com/agentskills/agentskills)
- [SKILL.md 规范文档](https://docs.anthropic.com/en/docs/claude-code/skills)

---

## 下一步

- [ ] 尝试编写自己的第一个 Skill
- [ ] 使用 Superpowers 框架规范开发流程
- [ ] 为现有项目创建优化类 Skill

---

*整理：墨鉴 | 2026-04-05*
