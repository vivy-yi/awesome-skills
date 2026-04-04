# AI Agent Skills 的供应链安全风险

> **来源**：PRPL Security Research
> **原文**：https://www.prplbx.com/blog/agent-skills-supply-chain

---

## 核心发现

安全研究人员在 2026 年初发现：

- **Anthropic Agent Skills 标准**：2025 年 12 月 18 日开放
- **恶意 Skills 增长**：到 2026 年 2 月 3 日，仅 ClawHub 上就发现 **341 个恶意 Skills**

## 风险类型

### 1. 恶意代码注入
攻击者通过 Skills 植入：
- 🔑 **API Key 窃取**：读取环境变量中的密钥
- 📁 **文件窃取**：上传敏感文件到外部服务器
- 🎯 **后门植入**：在代码中植入后门

### 2. 依赖供应链污染
恶意 Skills 依赖：
- 恶意 npm 包
- 被污染的 Python 库
- 伪造的工具包

### 3. 社会工程学
- 伪装成热门项目的 Skills
- 虚假评分和评论
- 钓鱼式安装引导

## 攻击案例

```markdown
# 恶意 Twitter Bot Skill

这个 Skill 声称可以帮助你自动化 Twitter 操作。
实际上，它在后台悄悄执行：

1. 读取 ~/.twitter-api-keys 文件
2. 将 API keys 发送到攻击者服务器
3. 发送垃圾推文
```

## 安全防护措施

### 1. 代码审查（必须）
在安装任何第三方 Skill 前：

```bash
# 检查可疑的网络请求
grep -r "requests\.\|http\.\|fetch" .

# 检查环境变量访问
grep -r "environ\|getenv" .

# 检查文件操作
grep -r "open\|read\|Path" .

# 检查 base64 编码（常用于隐蔽传输）
grep -r "base64\|atob\|btoa" .
```

### 2. 沙盒隔离
- 在隔离环境中测试 Skills
- 使用容器/VM
- 限制网络访问

### 3. 权限控制
```json
{
  "skill": {
    "name": "trusted-skill",
    "permissions": {
      "network": ["api.example.com"],
      "filesystem": false,
      "env_vars": ["PATH"],
      "subprocess": false
    }
  }
}
```

### 4. 来源验证
| 来源 | 信任度 | 审查要求 |
|------|--------|----------|
| 官方发布 | ✅ 高 | 快速审查 |
| 知名社区 | ⚠️ 中 | 完整审查 |
| 未知来源 | ❌ 低 | 禁止安装 |

## 安全使用规范

1. **最小权限原则**：只授予必要的权限
2. **来源验证**：确认 Skill 发布者的身份
3. **定期审计**：检查已安装 Skills 的安全性
4. **隔离环境**：生产环境使用经过验证的 Skills
5. **监控日志**：关注异常的网络请求和文件访问

## 相关资源

- [原文：AI Agent Skills Supply Chain Risk](https://www.prplbx.com/blog/agent-skills-supply-chain)
- [Anthropic Agent Skills 官方文档](https://docs.anthropic.com/en/docs/claude-code/skills)
- [ClawHub Security](https://clawhub.ai)

---

*整理：墨鉴 | 2026-04-05*
*备注：本报告已同步到 openclaw-master-tutorial 第 22 章安全部分*
