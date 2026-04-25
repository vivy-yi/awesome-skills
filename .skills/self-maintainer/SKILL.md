---
name: self-maintainer
description: Self-maintaining skill that updates, improves, and audits the awesome-skills maintenance skill system. Use when: (1) updating skills to new patterns, (2) auditing skill health, (3) self-improvement. Triggers on: "self-maintain", "audit skills", "skill health", "improve skills", "skill maintenance", "maintain myself". This skill examines and updates the .skills/ directory itself.
---

# Self-Maintainer

Self-auditing and self-improving skill for the awesome-skills maintenance system.

## Core Principle

This skill follows the same patterns it maintains. When it improves itself, it uses these same instructions. This creates a positive feedback loop where the maintenance system gets better at maintaining itself.

## Workflow

### 1. Audit Current Skills Health

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos/.skills

echo "=== Skills Directory Health Check ===\n"

# Check all SKILL.md files exist and are valid
echo "Skill directories:"
for skill in */; do
    name=$(basename "$skill")
    if [ -f "$skill/SKILL.md" ]; then
        size=$(wc -c < "$skill/SKILL.md")
        lines=$(wc -l < "$skill/SKILL.md")
        echo "  ✅ $name - ${size}B, ${lines} lines"
    else
        echo "  ❌ $name - MISSING SKILL.md"
    fi
done

echo ""
echo "Total skills: $(ls -d */ | wc -l | tr -d ' ')"
echo "Total SKILL.md files: $(find . -name 'SKILL.md' | wc -l | tr -d ' ')"
```

### 2. Check for Skill Anti-Patterns

```bash
python3 << 'PYEOF'
import os
import re
from pathlib import Path

SKILLS_DIR = Path("/Volumes/waku/github-维护/awesome/awesome-skills-repos/.skills")
issues = []

for skill_dir in SKILLS_DIR.iterdir():
    if not skill_dir.is_dir():
        continue
    
    skill_name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    
    if not skill_md.exists():
        issues.append(f"❌ {skill_name}: SKILL.md missing")
        continue
    
    content = skill_md.read_text()
    
    # Check frontmatter
    if not content.startswith('---'):
        issues.append(f"❌ {skill_name}: Missing YAML frontmatter")
    
    # Check required fields
    if 'name:' not in content[:500]:
        issues.append(f"❌ {skill_name}: Missing 'name:' in frontmatter")
    if 'description:' not in content[:500]:
        issues.append(f"❌ {skill_name}: Missing 'description:' in frontmatter")
    
    # Check for common issues
    if len(content) < 500:
        issues.append(f"⚠️ {skill_name}: SKILL.md is very short ({len(content)} bytes)")
    
    # Check for README files (anti-pattern)
    for f in skill_dir.iterdir():
        if f.name.startswith('README') and f.suffix == '.md':
            issues.append(f"⚠️ {skill_name}: Has {f.name} (should be in SKILL.md or references/)")
    
    # Check for excessive nesting
    for root, dirs, files in os.walk(skill_dir):
        depth = root.replace(str(skill_dir), '').count(os.sep)
        if depth > 2:
            issues.append(f"⚠️ {skill_name}: Excessive nesting at depth {depth}")
    
    # Check description is comprehensive
    desc_match = re.search(r'description:\s*["\'](.+?)["\']', content[:1000], re.DOTALL)
    if desc_match:
        desc_len = len(desc_match.group(1))
        if desc_len < 50:
            issues.append(f"⚠️ {skill_name}: description is very short ({desc_len} chars)")

if issues:
    print("=== Issues Found ===")
    for issue in issues:
        print(f"  {issue}")
else:
    print("✅ All skills pass basic health checks!")
PYEOF
```

### 3. Check Consistency with Latest OpenClaw SKILL.md Spec

```bash
# Compare against OpenClaw's skill-creator spec
echo "=== OpenClaw SKILL.md Spec Compliance ==="
echo ""
echo "Checking against: /opt/homebrew/lib/node_modules/openclaw/skills/skill-creator/SKILL.md"
echo ""

# Key requirements from spec:
REQUIREMENTS=(
    "YAML frontmatter with name and description"
    "Anatomy: SKILL.md + optional scripts/ + optional references/ + optional assets/"
    "scripts/: executable code (Python/Bash)"
    "references/: documentation for loading as needed"
    "assets/: files used in output (templates, images)"
    "SKILL.md body: instructions under 500 lines preferred"
    "Progressive disclosure: metadata → SKILL.md body → references"
)

echo "Required patterns:"
for req in "${REQUIREMENTS[@]}"; do
    echo "  - $req"
done
```

### 4. Update Outdated Skills

```bash
# Check if skills use latest patterns
python3 << 'PYEOF'
import json
from pathlib import Path
from datetime import datetime

SKILLS_DIR = Path("/Volumes/waku/github-维护/awesome/awesome-skills-repos/.skills")

# Check each skill for outdated patterns
for skill_dir in SKILLS_DIR.iterdir():
    if not skill_dir.is_dir():
        continue
    
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        continue
    
    content = skill_md.read_text()
    suggestions = []
    
    # Check for outdated patterns
    if 'python3 <<' in content and 'PYEOF' in content:
        suggestions.append("Uses inline Python heredoc - consider extracting to scripts/")
    
    if content.count('\n```\n') > 15:
        suggestions.append("Many code blocks - consider progressive disclosure")
    
    if len(content) > 10000:
        suggestions.append("SKILL.md is very long (>10k chars) - consider splitting")
    
    if suggestions:
        print(f"\n### {skill_dir.name}")
        for s in suggestions:
            print(f"  💡 {s}")
PYEOF
```

### 5. Extract Repeated Code to Shared Scripts

```bash
# Check if multiple skills have similar scripts
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos/.skills

echo "=== Checking for Shared Code Opportunities ==="

# Look for common patterns across skills
for skill in */SKILL.md; do
    name=$(basename $(dirname $skill))
    has_python=$(grep -c "python3" "$skill" 2>/dev/null || echo 0)
    has_curl=$(grep -c "curl" "$skill" 2>/dev/null || echo 0)
    has_github=$(grep -c "github" "$skill" 2>/dev/null || echo 0)
    
    if [ "$has_python" -gt 3 ] || [ "$has_curl" -gt 5 ] || [ "$has_github" -gt 5 ]; then
        echo "  $name: python=$has_python curl=$has_curl github=$has_github"
    fi
done

echo ""
echo "If a skill uses Python/curl extensively, consider extracting"
echo "reusable functions to .skills/scripts/shared.py"
```

### 6. Generate Maintenance Report

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos

python3 << 'PYEOF'
import json
from pathlib import Path
from datetime import datetime

repo = Path("/Volumes/waku/github-维护/awesome/awesome-skills-repos")
skills_dir = repo / ".skills"

report = f"""# 墨鉴-Skills维护系统健康报告 {datetime.now().strftime('%Y-%m-%d')}

## 系统概览

- 技能总数：{len(list(skills_dir.iterdir()))}
- skills.json 条目：{len(json.load(open(repo / 'skills.json')))}
- 仓库地址：https://github.com/vivy-yi/awesome-skills

## .skills/ 目录结构

"""

for skill_path in sorted(skills_dir.iterdir()):
    if not skill_path.is_dir():
        continue
    
    name = skill_path.name
    skill_md = skill_path / "SKILL.md"
    
    if skill_md.exists():
        size = skill_md.stat().st_size
        lines = len(skill_md.read_text().splitlines())
        report += f"- ✅ {name}/ — {size}B, {lines} 行\n"
    else:
        report += f"- ❌ {name}/ — SKILL.md 缺失\n"
    
    # List subdirectories
    for sub in ['scripts', 'references', 'assets']:
        sub_path = skill_path / sub
        if sub_path.exists() and any(sub_path.iterdir()):
            files = [f.name for f in sub_path.iterdir()]
            report += f"  - {sub}/: {', '.join(files)}\n"

report += f"""
## 最近更新

"""

# Check git log for recent changes
import subprocess
result = subprocess.run(
    ['git', 'log', '--oneline', '-10'],
    cwd=str(repo),
    capture_output=True, text=True
)
report += "```\n" + result.stdout + "```\n"

report += """
## 系统健康状态

- [ ] 所有 SKILL.md 文件存在且格式正确
- [ ] 无冗余 README 文件
- [ ] 嵌套深度 ≤ 2 层
- [ ] 重复代码已提取到 shared scripts
- [ ] 定时任务正常运行

## 待改进项

1. 定期运行 self-maintainer 检查健康状态
2. 提取通用代码到 shared utilities
3. 考虑添加 references/ 目录存储详细文档
"""

with open(repo / ".skills" / "HEALTH.md", 'w') as f:
    f.write(report)

print("Health report generated: .skills/HEALTH.md")
print(report)
PYEOF
```

### 7. Commit Self-Maintenance Changes

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos
git add .skills/
git status
echo "---"
read -p "Commit self-maintenance? (y/n) " ans
if [ "$ans" = "y" ]; then
    git commit -m "chore(self): skills system self-maintenance $(date +%Y-%m-%d)"
    git push
    echo "Self-maintenance complete!"
fi
```

## Self-Improvement Loop

```
┌─────────────────────────────────────┐
│  self-maintainer runs               │
│  (triggered by cron or agent)       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Audit: health check                │
│  - SKILL.md existence               │
│  - Frontmatter validity             │
│  - Anti-pattern detection           │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Analyze: find improvement areas    │
│  - Extract repeated code           │
│  - Split oversized SKILL.md         │
│  - Add missing metadata             │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Act: make improvements             │
│  - Update SKILL.md files           │
│  - Create shared scripts/           │
│  - Generate health report          │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Commit & push                      │
└─────────────────────────────────────┘
```

## Trigger Frequency

Run self-maintenance:
- **Weekly**: Via cron or agent trigger
- **After adding new skills**: Ensure quality
- **Before major updates**: Validate current state

## Notes

- This skill is the most meta — it maintains the maintenance system
- Creates HEALTH.md as a living status document
- Extracts reusable code to shared utilities when found
- Always commits with `chore(self):` prefix to distinguish from content updates
