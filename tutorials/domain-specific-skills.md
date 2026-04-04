# Domain-Specific Skills 深度解析：安全技能专题

> **适合人群**：需要为特定领域构建 Skills 的开发者
> **预计阅读时间**：35 分钟
> **来源**：基于 awesome-skills 仓库 Security 分类分析

---

## 1. 安全 Skills 概述

### 1.1 为什么安全 Skills 重要

```
安全 Skills 的独特价值：
┌─────────────────────────────────────────────────────────────┐
│  1. 自动化安全检查 │ 每次代码提交都自动运行安全扫描            │
│  2. 标准化流程    │ 团队统一的安全最佳实践                    │
│  3. 早发现早修复  │ 在开发阶段发现安全问题                   │
│  4. 持续监控      │ 实时跟踪依赖漏洞                         │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 安全 Skills 分类

| 类别 | 示例 Skills | 用途 |
|------|------------|------|
| **依赖扫描** | npm-audit, safety, pip-audit | 检测依赖漏洞 |
| **代码扫描** | bandit, semgrep, eslint-security | 静态代码分析 |
| **密钥检测** | detect-secrets, gitleaks | 防止密钥泄露 |
| **渗透测试** | sqlmap, nmap, metasploit | 自动化渗透测试 |
| **合规检查** | owasp-check, pci-dss | 法规合规 |

---

## 2. OWASP Security Skill 实战

### 2.1 SKILL.md 结构

```markdown
---
name: owasp-security-check
description: OWASP Top 10 安全检查技能，帮助识别和修复常见安全漏洞
version: 1.0.0
tags: [security, owasp, vulnerability, web]
trigger: "当用户要求安全检查、漏洞扫描、或提到 OWASP 时触发"
platforms: [claude-code, openclaw, codex]
---

# OWASP Security Check Skill

## 概述
这个 Skill 帮助识别 Web 应用中的 OWASP Top 10 安全漏洞。

## OWASP Top 10 (2023)

| # | 漏洞类型 | 描述 |
|---|----------|------|
| A01 | 访问控制失效 | 未授权访问 |
| A02 | 加密失败 | 敏感数据泄露 |
| A03 | 注入 | SQL/NoSQL/命令注入 |
| A04 | 不安全设计 | 设计缺陷 |
| A05 | 安全配置错误 | 错误配置 |
| A06 | 脆弱组件 | 使用有漏洞的库 |
| A07 | 认证失败 | 身份验证缺陷 |
| A08 | 数据完整性失败 | 验证缺失 |
| A09 | 日志失败 | 安全事件未记录 |
| A10 | SSRF | 服务端请求伪造 |

## 检查清单

### A01: 访问控制

```bash
# 检查未受保护的端点
curl -X POST https://api.example.com/admin/delete
# 应该返回 403 Forbidden，而不是 200 OK

# 检查 IDOR
curl https://api.example.com/users/123/profile
# 尝试访问其他用户 ID，看是否越权
```

### A02: 敏感数据暴露

```javascript
// ❌ 错误：响应包含敏感信息
{
  "user": {
    "id": 123,
    "password_hash": "sha256:xxx",  // 不应该暴露
    "ssn": "123-45-6789",          // 敏感数据
    "credit_card": "xxxx-xxxx-xxxx-1234"  // PCI 数据
  }
}

// ✅ 正确：只返回必要信息
{
  "user": {
    "id": 123,
    "name": "John"
  }
}
```

### A03: 注入防护检查

```sql
-- ❌ 危险：直接拼接 SQL
SELECT * FROM users WHERE id = ' + userId + '

-- ✅ 安全：使用参数化查询
SELECT * FROM users WHERE id = $1  -- parameterized
```

```javascript
// ❌ 危险：命令注入
const cmd = `ls ${userInput}`;
// 用户输入: "; rm -rf /"

exec(cmd);

// ✅ 安全：不使用用户输入执行命令
execFile('ls', [validatedPath]);
```

### A06: 依赖漏洞检查

```bash
# Node.js
npm audit
npm outdated

# Python
pip-audit
safety check

# Go
go mod verify
govulncheck
```

## 安全测试命令

### 快速扫描

```bash
# 1. 检查开放端口
nmap -sV localhost

# 2. 检查 HTTP 头部
curl -I https://example.com

# 3. 检查 SSL/TLS
openssl s_client -connect example.com:443

# 4. 检查 SQL 注入
sqlmap -u "https://example.com/?id=1"
```

### 详细渗透测试

```bash
# 使用 Burp Suite 拦截请求
# 检查以下参数：
# - URL 参数
# - POST 数据
# - Cookies
# - Headers
```

## 报告模板

```markdown
# 安全扫描报告

## 基本信息
- 目标：example.com
- 时间：2026-04-05
- 扫描者：Security Skill

## 发现问题

| 严重性 | 类别 | 位置 | 描述 | 修复建议 |
|--------|------|------|------|----------|
| 🔴 高危 | A03 | /login | SQL 注入漏洞 | 使用参数化查询 |
| 🟡 中危 | A05 | config | 调试模式开启 | 生产环境关闭 |
| 🟢 低危 | A09 | /api | 缺少安全日志 | 添加审计日志 |

## 修复优先级
1. 🔴 立即修复：SQL 注入
2. 🟡 本周修复：关闭调试模式
3. 🟢 下月计划：完善日志
```

## 参考资源

- [OWASP Top 10](https://owasp.org/Top10/)
- [OWASP Cheat Sheets](https://cheatsheetseries.owasp.org/)
- [CVE 数据库](https://cve.mitre.org/)
```

---

## 3. 密钥检测 Skill

### 3.1 detect-secrets 集成

```yaml
# skill: secret-detection
---
name: secret-detection
description: 密钥和敏感信息检测技能，防止 secrets 泄露到代码库
trigger: "当用户提交代码、创建新文件、或要求检查 secrets 时触发"
---

## 使用方法

### 1. 安装 detect-secrets

```bash
pip install detect-secrets
```

### 2. 初始化（首次使用）

```bash
detect-secrets init
# 生成 .secrets.yaml 基线文件
```

### 3. 扫描代码

```bash
# 扫描所有文件
detect-secrets scan .

# 扫描并生成报告
detect-secrets scan . --report
```

### 4. 常见密钥模式

```yaml
# .secrets.baseline 配置
{
  "version": "1.0.0",
  "plugins": [
    {
      "name": "AWSKeyDetector"
    },
    {
      "name": "GitHubTokenDetector"
    },
    {
      "name": "StripeDetector"
    },
    {
      "name": "NpmDetector"
    }
  ]
}
```

### 5. 预提交钩子

```bash
# 安装 pre-commit 钩子
detect-secrets install-hook

# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: detect-secrets
        name: detect-secrets
        entry: detect-secrets scan --fail-on-unaudited
        language: system
        stages: [pre-commit]
```

## 检测规则

| 密钥类型 | 模式 | 风险 |
|----------|------|------|
| AWS Access Key | `AKIA[0-9A-Z]{16}` | 🔴 极高 |
| AWS Secret Key | 40 字符 base64 | 🔴 极高 |
| GitHub Token | `gh[pousr]_[A-Za-z0-9_]{36,255}` | 🔴 极高 |
| Stripe Key | `sk_live_[0-9a-zA-Z]{24}` | 🔴 极高 |
| Private Key | `-----BEGIN.*PRIVATE KEY-----` | 🔴 极高 |
| API Key Generic | `[a-zA-Z0-9]{32,64}` | 🟡 中 |
| JWT Token | `eyJ[A-Za-z0-9-_]+\.eyJ[A-Za-z0-9-_]+` | 🟡 中 |

---

## 4. 自动化安全检查 Workflow

### 4.1 CI/CD 集成

```yaml
# .github/workflows/security.yml
name: Security Checks

on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run detect-secrets
        run: |
          pip install detect-secrets
          detect-secrets scan . --fail-on-unaudited
      
      - name: Check dependencies
        run: |
          npm audit --audit-level=high
          # 或
          pip-audit
      
      - name: Run SAST
        run: |
          # Semgrep
          docker run -rm \
            -v "$(pwd):/src" \
            returntocorp/semgrep \
            semgrep --config=auto
      
      - name: Check secrets in commits
        run: |
          git log --format="%H" -n 20 | \
          xargs -I {} git show {} | \
          detect-secrets scan --string
```

### 4.2 完整的安全审查 Skill

```yaml
# skill: comprehensive-security-review
---
name: comprehensive-security-review
description: 综合安全审查技能，涵盖代码、依赖、配置和渗透测试
trigger: "当用户要求完整的安全审查、或启动安全评估时触发"
---

## 审查范围

### 1. 静态代码分析
- 代码注入漏洞
- XSS 漏洞
- CSRF 漏洞
- 认证问题
- 会话管理

### 2. 依赖检查
- 已知漏洞（CVE）
- 过期依赖
- 许可合规

### 3. 配置审计
- 环境变量检查
- 配置文件审查
- 容器安全

### 4. 基础设施
- 网络暴露
- API 安全
- 加密配置

## 执行命令

```bash
# 一键执行所有检查
security-review --target ./src --output report.md

# 分步执行
security-review --step static
security-review --step dependencies
security-review --step config
security-review --step network
```

## 输出格式

```markdown
# 综合安全审查报告

## 执行摘要
- 目标：https://api.example.com
- 时间：2026-04-05
- 风险等级：🟡 中

## 详细结果

### 1. 静态分析
| 问题 | 文件 | 行号 | 严重性 |
|------|------|------|--------|
| SQL 注入 | user.go | 45 | 🔴 |

### 2. 依赖漏洞
| 依赖 | 版本 | CVE | 严重性 |
|------|------|-----|--------|
| lodash | 4.17.0 | CVE-2021-23337 | 🟡 |

### 3. 配置问题
| 问题 | 配置 | 建议 |
|------|------|------|
| DEBUG=true | .env | 生产设为 false |

## 建议修复计划
1. 🔴 紧急：修复 SQL 注入
2. 🟡 本周：升级 lodash
3. 🟢 月内：关闭 DEBUG 模式
```

---

## 5. 安全 Skills 最佳实践

### 5.1 设计原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **最小权限** | 只请求必要的权限 | 不需要文件系统访问时禁用 |
| **纵深防御** | 多层安全检查 | 依赖扫描 + 代码扫描 |
| **自动化优先** | 减少人工介入 | 集成到 CI/CD |
| **及时更新** | 跟踪最新威胁 | 定期更新规则库 |

### 5.2 误报处理

```yaml
# 允许标记误报
---
name: security-check
allow_false_positives:
  - pattern: "test_api_key"
    reason: "这是测试密钥，不是生产密钥"
    approved_by: "security-team"
---

## 误报管理

当检测到疑似问题但实际不是时：
1. 验证是否为真实问题
2. 如果是误报，添加到 allow_false_positives
3. 如果是真实问题，立即修复
```

### 5.3 告警分级

```yaml
alerts:
  critical:
    - type: "credentials_exposed"
      action: "立即告警 + 自动封禁"
    - type: "sql_injection"
      action: "立即告警"
      
  warning:
    - type: "outdated_dependency"
      action: "每日汇总"
    - type: "weak_encryption"
      action: "本周内处理"
      
  info:
    - type: "missing_logging"
      action: "月度审查"
```

---

## 6. 安全合规 Skill

### 6.1 GDPR 合规检查

```yaml
# skill: gdpr-compliance
---
name: gdpr-compliance
description: GDPR 合规检查技能
trigger: "当用户要求 GDPR 合规检查时触发"
---

## 检查清单

### 数据收集
- [ ] 明确告知用户数据收集目的
- [ ] 获得用户同意
- [ ] 提供选择退出机制

### 数据存储
- [ ] 加密存储个人数据
- [ ] 数据保留期限策略
- [ ] 删除权实现

### 数据传输
- [ ] 使用加密连接 (HTTPS)
- [ ] 跨境传输合规
- [ ] DPA 协议
```

### 6.2 PCI-DSS 合规

```yaml
# skill: pci-dss-compliance
---
name: pci-dss-compliance
description: PCI DSS 支付卡行业数据安全标准
trigger: "处理支付相关代码时触发"
---

## 12 项要求

1. 安装防火墙
2. 默认凭据修改
3. 保护存储的持卡人数据
4. 传输加密
5. 使用反病毒软件
6. 安全系统更新
7. 限制数据访问
8. 身份验证
9. 限制物理访问
10. 记录访问日志
11. 定期测试
12. 安全策略维护
```

---

## 7. 相关资源

- [OWASP Top 10](https://owasp.org/Top10/)
- [detect-secrets](https://github.com/Yelp/detect-secrets)
- [Semgrep](https://semgrep.dev/)
- [npm audit](https://docs.npmjs.com/cli/v8/commands/npm-audit)
- [PCI DSS 标准](https://www.pcisecuritystandards.org/)

---

## 下一步

- [ ] 为你的项目添加安全检查 Skill
- [ ] 集成到 CI/CD 流程
- [ ] 定期执行安全审查
- [ ] 培训团队安全意识

---

*整理：墨鉴 | 2026-04-05*
