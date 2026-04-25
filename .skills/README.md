# .skills/ — Awesome-Skills 维护技能系统

> 本目录包含 awesome-skills 仓库的自动化维护技能

## 目录结构

```
.skills/
├── SKILL.md                    # ⭐ 主入口技能 (awesome-skills-maintenance)
├── README.md                   # 本文件
├── HEALTH.md                   # 系统健康报告 (自动生成)
├── star-updater/               # 更新所有 star 数量
│   └── SKILL.md
├── trending-crawler/           # 从 GitHub Trending 发现新技能
│   └── SKILL.md
├── link-doctor/                # 检测并修复损坏链接
│   └── SKILL.md
├── metadata-enricher/          # 为 skills.json 补充元数据
│   └── SKILL.md
├── blog-collector/             # 采集博客文章
│   └── SKILL.md
├── paper-collector/            # 采集学术论文
│   └── SKILL.md
└── self-maintainer/            # 系统自检和自我改进
    └── SKILL.md
```

## 使用方式

### 通过 OpenClaw Agent 执行

```
帮我运行 awesome-skills 的 star-updater
发现新的 skills 并添加到仓库
执行 awesome-skills 的完整维护
```

### 通过 GitHub Actions 自动执行

- 每周日: star-updater + self-maintainer
- 每周二: trending-crawler
- 每周五: link-doctor

### 手动执行

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos

# 读取并执行某个技能
# (由 OpenClaw Agent 读取 SKILL.md 后执行)
```

## 设计原则

1. **Agent-centric**: 所有技能都遵循 OpenClaw SKILL.md 规范
2. **Self-contained**: 每个技能是独立的，包含完整的执行说明
3. **Self-maintaining**: self-maintainer 技能定期审计系统健康
4. **Progressive disclosure**: 详细信息在参考文件中，按需加载

## 与 GitHub Actions 的关系

- GitHub Actions 处理定时自动化任务（定时触发）
- Skills 处理需要 Agent 判断的复杂任务（按需触发）
- 两者互补，确保维护系统全面覆盖

## 添加新技能

1. 在 `.skills/` 下创建新目录
2. 添加 `SKILL.md` 文件（遵循 OpenClaw 规范）
3. 在主 `SKILL.md` 的子技能表中注册
4. 运行 `self-maintainer` 进行自检

## 规范参考

- [OpenClaw SKILL.md 规范](https://docs.openclaw.ai/skills)
- [Skills.sh 规范](../docs/skills-sh-spec.md)
