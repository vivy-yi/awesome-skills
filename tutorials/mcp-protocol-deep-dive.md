# MCP & Integrations 深度解析：Model Context Protocol 完全指南

> **适合人群**：想理解 MCP 与 Skills 协同工作的开发者
> **预计阅读时间**：40 分钟
> **来源**：基于 modelcontextprotocol.io 官方文档和实战分析

---

## 1. MCP 核心概念

### 1.1 什么是 MCP？

**Model Context Protocol (MCP)** 是一个开放协议，让 AI 应用能够：
- **发现**外部数据源和工具
- **连接**到各种外部系统
- **执行**标准化操作

```
┌─────────────────────────────────────────────────────────────┐
│                     MCP 架构全景                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────┐         ┌─────────┐         ┌─────────┐      │
│   │  AI     │  ────→  │   MCP   │  ────→  │   MCP   │      │
│   │ Agent   │  ←───   │  Client │  ←───   │  Server │      │
│   └─────────┘         └─────────┘         └─────────┘      │
│       │                                        │            │
│       │              MCP Protocol              │            │
│       │         (JSON-RPC 2.0 over stdio)      │            │
│       │                                        │            │
│       ▼                                        ▼            │
│   ┌─────────┐                          ┌─────────┐        │
│   │ Claude  │                          │ GitHub  │        │
│   │Desktop  │                          │ Server  │        │
│   │  App    │                          └─────────┘        │
│   └─────────┘                          ┌─────────┐        │
│                                        │ Slack   │        │
│                                        │ Server  │        │
│                                        └─────────┘        │
│                                        ┌─────────┐        │
│                                        │  Files  │        │
│                                        │ System  │        │
│                                        └─────────┘        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 MCP vs Skills：职责分工

| 维度 | MCP | Skills |
|------|-----|--------|
| **核心职责** | 外部集成连接 | 认知流程封装 |
| **解决的问题** | "AI 如何访问工具和数据" | "AI 如何正确执行任务" |
| **抽象层次** | 协议层 | 应用层 |
| **典型内容** | 工具定义、资源访问 | 工作流程、最佳实践 |
| **更新频率** | 稳定（协议少变） | 频繁（持续优化） |

**协同关系**：
```
MCP（连接外部世界）+ Skills（正确的做事方式）= 完整的 AI Agent
```

---

## 2. MCP 服务器类型

### 2.1 内置资源服务器

| 服务器 | 功能 | 用途 |
|--------|------|------|
| `filesystem` | 本地文件访问 | 读写本地文件 |
| `github` | GitHub API | PR、Issue、代码库操作 |
| `slack` | Slack 消息 | 发送/读取消息 |
| `postgres` | PostgreSQL | 数据库查询 |

### 2.2 工具服务器

```json
// 工具定义示例
{
  "name": "github_create_issue",
  "description": "在 GitHub 仓库创建 Issue",
  "inputSchema": {
    "type": "object",
    "properties": {
      "owner": { "type": "string" },
      "repo": { "type": "string" },
      "title": { "type": "string" },
      "body": { "type": "string" }
    },
    "required": ["owner", "repo", "title"]
  }
}
```

### 2.3 提示词服务器

```json
{
  "name": "code_review_prompt",
  "description": "标准的代码审查提示词",
  "arguments": [
    { "name": "language", "required": true },
    { "name": "files", "required": true }
  ]
}
```

---

## 3. MCP + Skills 协同模式

### 3.1 模式一：MCP 供电 + Skills 指导

```
用户："帮我审查这个 PR"

┌─────────────────────────────────────────────────────────────┐
│  Skills: PR 审查流程                                         │
│  ├── 步骤 1: 获取 PR 信息（MCP: github）                    │
│  ├── 步骤 2: 获取代码变更（MCP: github）                    │
│  ├── 步骤 3: 执行审查（Skills: 审查标准）                   │
│  └── 步骤 4: 生成报告（Skills: 输出格式）                   │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 模式二：Skills 封装 MCP 调用

```yaml
# SKILL.md 中的 MCP 集成
---
name: github-pr-reviewer
description: GitHub PR 审查技能，使用 MCP 连接 GitHub
mcp_servers:
  - github
---

## 使用方法

### 1. 准备工作
确保已配置 GitHub MCP 服务器：
```
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    }
  }
}
```

### 2. 执行审查
使用 MCP 工具获取 PR 信息：
- `github_get_pr` - 获取 PR 详情
- `github_get_files` - 获取变更文件
- `github_create_review` - 提交审查意见
```

### 3.3 模式三：Skills 辅助 MCP 开发

```yaml
# MCP 服务器开发 Skill
---
name: mcp-server-dev
description: 使用 Skills 辅助开发 MCP 服务器
---

## 开发流程

### 1. 设计阶段
使用 Skill 提问：
- "我需要连接到什么数据源？"
- "需要暴露哪些工具？"
- "认证方案是什么？"

### 2. 实现阶段
Skill 提供：
- 项目脚手架
- 类型定义
- 测试模板

### 3. 部署阶段
Skill 协助：
- Docker 容器化
- MCPB 打包
- 分发配置
```

---

## 4. 实战：构建 MCP 服务器

### 4.1 项目结构

```
my-mcp-server/
├── package.json
├── tsconfig.json
├── src/
│   ├── index.ts          # 入口
│   ├── server.ts         # MCP 服务器
│   └── tools/
│       ├── example.ts    # 工具定义
└── README.md
```

### 4.2 服务器实现

```typescript
// src/server.ts
import { McpServer } from "@modelcontextprotocol/sdk/server";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server-stdio";
import { z } from "zod";

const server = new McpServer({
  name: "my-mcp-server",
  version: "1.0.0"
});

// 定义工具
server.tool(
  "get_weather",
  "获取指定城市的天气",
  {
    city: z.string().describe("城市名称")
  },
  async ({ city }) => {
    // 实现逻辑
    const weather = await fetchWeather(city);
    return {
      content: [
        { type: "text", text: JSON.stringify(weather) }
      ]
    };
  }
);

// 启动服务器
const transport = new StdioServerTransport();
server.run(transport);
```

### 4.3 工具注册

```typescript
// 工具定义规范
{
  name: "tool_name",           // 工具名称（英文、snake_case）
  description: "工具描述",       // 人类可读的描述
  inputSchema: {               // 输入参数 schema
    type: "object",
    properties: {
      param1: { type: "string" }
    },
    required: ["param1"]
  }
}
```

### 4.4 配置到 OpenClaw

```json
// openclaw.json
{
  "mcpServers": {
    "my-server": {
      "command": "node",
      "args": ["/path/to/my-mcp-server/dist/index.js"],
      "env": {
        "API_KEY": "xxx"
      }
    }
  }
}
```

---

## 5. MCP 安全最佳实践

### 5.1 敏感信息处理

```typescript
// ❌ 错误：硬编码密钥
const apiKey = "sk-xxxxx";

// ✅ 正确：从环境变量读取
const apiKey = process.env.API_KEY;

// ✅ 最佳：使用 MCP 的密钥管理
server.tool(
  "sensitive_operation",
  "敏感操作",
  {},
  async () => {
    const credentials = server.getCredentials("my-service");
    // 使用凭证
  }
);
```

### 5.2 工具权限控制

```json
// MCP 服务器配置
{
  "tools": {
    "dangerous_action": {
      "description": "危险操作",
      "requires_approval": true,
      "allowed_users": ["admin@example.com"]
    }
  }
}
```

### 5.3 审计日志

```typescript
// 所有 MCP 调用都应记录审计日志
server.tool(
  "data_operation",
  "数据操作",
  {},
  async ({ operation, data }) => {
    // 审计日志
    console.log(JSON.stringify({
      timestamp: new Date().toISOString(),
      operation,
      dataHash: hash(data),  // 不记录敏感数据
      user: getCurrentUser()
    }));
    
    return { /* result */ };
  }
);
```

---

## 6. MCP 与 Skills 的协同案例

### 案例：自动化代码审查流程

```yaml
# skill: automated-code-review
---
name: automated-code-review
description: 使用 MCP + Skills 实现自动化代码审查
mcp_servers:
  - github
  - filesystem

triggers:
  - "审查这个 PR"
  - "帮我看看代码有什么问题"
  - "执行代码质量检查"
---

## 工作流程

### Step 1: 获取 PR 信息
```bash
# 使用 GitHub MCP
github_get_pr(owner: "org", repo: "repo", pr_number: 123)
```

### Step 2: 获取代码变更
```bash
# 获取变更文件列表
github_get_pr_files(owner: "org", repo: "repo", pr_number: 123)
```

### Step 3: 质量分析
对每个文件执行检查：
- 复杂度分析
- 安全扫描
- 最佳实践检查

### Step 4: 生成报告
输出格式化的审查报告：
- 总体评分
- 问题列表（按严重程度）
- 改进建议

## 输出模板

```markdown
# 代码审查报告

## 基本信息
- PR: #123
- 作者: @username
- 变更: +100 -20

## 总体评分
⭐⭐⭐⭐☆ (4/5)

## 问题汇总
| 严重程度 | 文件 | 问题 | 建议 |
|----------|------|------|------|
| 🔴 高 | src/a.ts | 函数过长 | 拆分为小函数 |
| 🟡 中 | src/b.ts | 缺少错误处理 | 添加 try-catch |
| 🟢 低 | src/c.ts | 命名不规范 | 考虑更清晰的命名 |

## 最佳实践
- ✅ 使用了 TypeScript 类型
- ✅ 有单元测试
- ⚠️ 缺少集成测试
```

---

## 7. MCPB 打包格式

MCPB (MCP Bundle) 是 MCP 服务器的打包分发格式：

```bash
# 安装 MCPB CLI
npm install -g @modelcontextprotocol/mcpb

# 打包服务器
mcpb bundle ./my-mcp-server --output my-server.mcpb

# 分发和安装
# 用户只需：
openclaw mcp install my-server.mcpb
```

---

## 8. 常见问题排查

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| MCP 服务器连接失败 | 路径错误 | 检查 `command` 和 `args` |
| 工具调用超时 | 工具执行慢 | 增加 `timeout` 配置 |
| 权限不足 | 未授权操作 | 配置 `allowed_tools` |
| 数据格式错误 | Schema 不匹配 | 验证 `inputSchema` |

---

## 9. 相关资源

- [MCP 官方文档](https://modelcontextprotocol.io)
- [MCP 规范](https://spec.modelcontextprotocol.io)
- [MCP 服务器列表](https://github.com/modelcontextprotocol/servers)
- [OpenClaw MCP 集成](../16_system_layer/README.md#mcp)

---

## 下一步

- [ ] 尝试连接一个 MCP 服务器
- [ ] 开发自己的第一个 MCP 服务器
- [ ] 使用 Skills 封装 MCP 调用

---

*整理：墨鉴 | 2026-04-05*
