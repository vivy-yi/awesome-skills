# The SKILL.md Pattern: 如何编写真正有效的 AI Agent Skills

> **来源**：Medium - bibek-poudel
> **原文**：https://bibek-poudel.medium.com/the-skill-md-pattern-how-to-write-ai-agent-skills-that-actually-work-72a3169dd7ee

---

## 核心观点

SKILL.md 是一种让 AI Agent 掌握特定技能的文本模式。当 AI 需要执行特定任务时，它会自动找到对应的 Skill 并按照其指令执行。

## 为什么 Skills 有效

1. **上下文注入**：Skills 作为提示注入到 Agent 的上下文中
2. **模式识别**：Agent 识别任务类型，自动选择合适的 Skill
3. **可复用性**：一次编写，多次使用
4. **跨平台兼容**：Claude Code、Codex、OpenClaw、OpenAI Skills 都使用兼容格式

## SKILL.md 标准格式

```markdown
---
name: skill-name
description: 简短描述这个 Skill 做什么
version: 1.0.0
tags: [tag1, tag2]
---

# Skill 名称

## 概述
这个 Skill 解决什么问题。

## 触发条件
- 当用户要求...
- 当任务涉及...

## 操作指南

### 步骤 1: ...
### 步骤 2: ...

### 代码示例
```javascript
// 示例代码
```
```

## 最佳实践

1. 保持简洁（建议 <200 行）
2. 使用清晰的标题层级
3. 包含具体的代码示例
4. 明确标注触发条件

## 常见错误

❌ 写得过于宽泛
❌ 缺少具体示例
❌ 触发条件不明确
❌ 过度复杂化

---

## 相关资源

- [The SKILL.md Pattern 原文章](https://bibek-poudel.medium.com/the-skill-md-pattern-how-to-write-ai-agent-skills-that-actually-work-72a3169dd7ee)
- [10 Must-Have Skills for Claude in 2026](https://medium.com/@unicodeveloper/10-must-have-skills-for-claude-and-any-coding-agent-in-2026-b5451b013051)
- [Claude Code SKILL.md 官方规范](https://docs.anthropic.com/en/docs/claude-code/skills)

---

*整理：墨鉴 | 2026-04-05*
