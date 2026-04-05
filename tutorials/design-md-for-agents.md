# DESIGN.md：让 AI Coding Agent 读懂设计系统

> 让 AI 在任何项目中构建风格一致的 UI — 通过可执行的设计规范文档

**阅读时间**：25 分钟  
**难度**：⭐⭐⭐  
**标签**：#tutorial #design #ui #coding-agent  

---

## 背景

当 AI Coding Agent（如 Claude Code、Cursor）开始构建 UI 界面时，最大的问题是什么？

**风格不一致。**

同一个项目里，Agent 可能：
- 这次用 `#3B82F6`，下次用 `#2563EB`（差不多的蓝色）
- 这次用 `Inter` 字体，下次用 `system-ui`
- 这次圆角 `8px`，下次 `12px`

根本原因：**Agent 没有「设计系统」的概念**，它只能从对话上下文中模糊地感知风格，而设计系统本质上是一套可枚举、可查阅的规范。

---

## 什么是 DESIGN.md？

`DESIGN.md` 是一种**面向 AI Agent 的设计规范文件**。

它脱胎于 `AGENTS.md`/`CLAUDE.md`/`CURSOR.md` 等 AI 友好文档规范，专注于描述项目的视觉设计系统，供 AI Coding Agent 在生成代码时直接参考。

### 核心思想

```
传统设计系统 → 人类设计师查阅
DESIGN.md    → AI Coding Agent 直接解析执行
```

### 典型结构

```markdown
# DESIGN.md — MyApp Design System

## 色彩（Colors）
| Token | Hex | 用途 |
|-------|-----|------|
| primary | #3B82F6 | 主按钮、重要链接 |
| primary-hover | #2563EB | 主按钮悬停态 |
| secondary | #64748B | 次要文字、图标 |
| background | #FFFFFF | 页面背景 |
| surface | #F8FAFC | 卡片、面板背景 |
| border | #E2E8F0 | 边框、分隔线 |
| text-primary | #0F172A | 主文字 |
| text-secondary | #64748B | 次要文字 |

## 字体（Typography）
- **主字体**：`Inter, -apple-system, BlinkMacSystemFont, sans-serif`
- **等宽字体**：`JetBrains Mono, Menlo, monospace`
- **标题比例**：h1: 32px/700, h2: 24px/600, h3: 18px/600

## 间距（Spacing）
- 基础单位：4px
- 间距刻度：4, 8, 12, 16, 24, 32, 48, 64
- 组件内 padding：16px
- 组件间 gap：12px

## 圆角（Border Radius）
- 小（按钮、输入框）：6px
- 中（卡片、弹窗）：8px
- 大（特殊容器）：12px

## 阴影（Shadows）
- sm: `0 1px 2px rgba(0,0,0,0.05)`
- md: `0 4px 6px -1px rgba(0,0,0,0.1)`
- lg: `0 10px 15px -3px rgba(0,0,0,0.1)`

## 组件规范

### 按钮（Buttons）
- Primary: bg-primary, text-white, rounded-6px, px-16px py-8px
- Secondary: bg-transparent, border-border, text-primary
- 悬停：背景色加深 10%

### 输入框（Inputs）
- border-border, rounded-6px, px-12px py-8px
- Focus: ring-2 ring-primary ring-opacity-50

### 卡片（Cards）
- bg-surface, rounded-8px, shadow-sm, p-16px
```

---

## VoltAgent/awesome-design-md 实践

### 项目地址
```
https://github.com/VoltAgent/awesome-design-md
```

### 收录的设计系统（部分）

| 设计系统 | 描述 |
|---------|------|
| Tailwind CSS 官方 | V4 设计系统 |
| Stripe | Stripe 官方设计规范 |
| Vercel | Vercel/Next.js 风格 |
| Linear | Linear App 极简风格 |
| GitHub | GitHub UI 风格 |

每个设计系统都是一个独立的 `DESIGN.md` 文件，AI Agent 可以直接复制到项目中。

### 使用方法

**Step 1：克隆/下载目标设计系统的 DESIGN.md**

```bash
curl -O https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-systems/vercel/DESIGN.md
```

**Step 2：在 AGENTS.md 或 CLAUDE.md 中引入**

```markdown
## 设计规范
在开始 UI 开发前，请阅读项目根目录的 DESIGN.md 文件，
严格按照其中的色彩、字体、间距规范执行。
```

**Step 3：让 Agent 生成风格一致的 UI**

```
> 用卡片展示用户信息，包含头像、姓名和邮箱
（Agent 会自动查阅 DESIGN.md 中的卡片规范）
```

---

## 与现有 SKILL.md 体系的关系

| 规范 | 目标 | 格式 |
|------|------|------|
| SKILL.md | 教 Agent 工具/技能 | Markdown + 指令 |
| AGENTS.md | 指导 Agent 全局行为 | Markdown 指令 |
| DESIGN.md | 约束 Agent UI 输出 | 设计 Token + 组件规范 |

三者可以共存，互补协同：

```
CLAUDE.md
├── SKILL.md        # 如何使用工具
├── DESIGN.md       # 如何构建 UI
└── CONTEXT.md     # 业务背景
```

---

## 扩展：Design Token 标准

DESIGN.md 本质上是 **Design Token** 的 Markdown 表达。

### 推荐的 Design Token 分类

```
1. Primitives（原始值）
   color: #3B82F6

2. Semantic Tokens（语义值）
   color.primary: {primitives.blue.500}
   color.primary-hover: {primitives.blue.600}

3. Component Tokens（组件值）
   button.bg: {semantic.color.primary}
   button.radius: {semantic.radius.sm}
```

### 为什么 Markdown 优于 JSON/YAML？

**AI 可读性第一。** Markdown 格式：
- 人类和 AI 都能直接理解
- 无需解析器，直接嵌入 AGENTS.md
- 可以包含注释说明设计意图

---

## 实践练习

### 练习：为你的项目创建 DESIGN.md

**目标**：为你的 Web 项目创建一份可执行的 Design 规范。

**步骤**：

1. **提取设计 Token**
   从 Figma/设计稿中导出颜色、字体、间距值

2. **写入 DESIGN.md**
   按上文章节结构组织（Colors、Typography、Spacing...）

3. **在 CLAUDE.md 中引入**
   ```markdown
   > 开始任何 UI 开发前，先阅读 DESIGN.md 并严格遵守。
   ```

4. **测试：让 Agent 构建一个组件**
   ```
   用卡片形式展示这个用户数据：
   { name: "张三", email: "zhang@example.com" }
   ```

5. **对比检验**
   检查生成代码是否符合 DESIGN.md 规范，如有偏差则更新文档。

---

## 相关资源

### 开源项目
- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — 收录 50+ 主流网站设计系统
- [design-tokens](https://github.com/amzn/design-tokens) — Amazon 设计 Token 规范
- [Style Dictionary](https://github.com/amzn/style-dictionary) — Design Token 转换工具

### 相关 SKILL
- [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills) — Obsidian 的 SKILL.md 实践
- [anthropics/skills](https://github.com/anthropics/skills) — Anthropic 官方 Skills 规范

### 延伸阅读
- [Designing for AI](https://anthropic.com/blog/designing-for-ai) — Anthropic 关于 AI UI 的思考
- [The Rise of AI Coding Agents](https://a16z.com/ai-coding-agents/) — a16z 关于 AI Coding Agent 的分析

---

## 总结

| 维度 | 评价 |
|------|------|
| 创新性 | ⭐⭐⭐⭐⭐ — 新兴模式，直接解决 Agent UI 一致性问题 |
| 实用性 | ⭐⭐⭐⭐ — 可直接落地，适合各类 Web 项目 |
| 生态成熟度 | ⭐⭐⭐ — VoltAgent/awesome-design-md 已收录大量资源 |
| 与 Skills 集成 | ⭐⭐⭐⭐ — 与 SKILL.md 体系天然互补 |

**核心洞见**：`DESIGN.md` 是 AI Coding Agent 时代的设计系统新形态 — 它不是为了人类阅读优化，而是为了让 AI 精确执行。设计系统正在从「人类的参考文档」演变为「Agent 的可执行规范」。
