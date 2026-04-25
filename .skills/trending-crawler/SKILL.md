---
name: trending-crawler
description: Discover new AI Agent Skills from GitHub Trending. Use when: (1) daily/weekly skill discovery task fires, (2) expanding the skills.json collection, (3) finding new skill repositories. Triggers on: "discover skills", "find new skills", "crawl trending", " trending skills", "new skills discovery". NOT for: adding a specific known skill (use add-skill instead), or updating stars (use star-updater).
---

# Trending Crawler

Discovers new AI Agent Skills from GitHub Trending pages and adds them to `skills.json`.

## Workflow

### 1. Scrape GitHub Trending

```bash
cd /tmp && \
curl -s "https://github.com/trending?since=daily" | \
python3 << 'PYEOF'
import sys
import re
from datetime import datetime

html = sys.stdin.read()

# Extract repos from trending page
# Pattern: data-href="/owner/repo"
pattern = r'data-href="(/[^/]+/[^"]+)"'
matches = re.findall(pattern, html)

seen = set()
repos = []
for m in matches:
    if m not in seen and '/tre' not in m:  # skip trending itself
        seen.add(m)
        repos.append(m)

print(f"Found {len(repos)} repos on trending")
for r in repos[:10]:
    print(f"  {r}")
PYEOF
```

### 2. Filter for Skill-Related Repos

```bash
cd /tmp && \
TRENDING_HTML=$(curl -s "https://github.com/trending?since=daily") && \
echo "$TRENDING_HTML" | python3 << 'PYEOF'
import sys
import re
import json

html = sys.stdin.read()

# Extract repo paths and descriptions
# Pattern for repo: <h2><a href="/owner/repo">
repo_pattern = r'<h2>\s*<a href="(/[^/]+/[^"]+)"[^>]*>'
desc_pattern = r'<p class="col-9[^"]*"[^>]*>([^<]+)</p>'
star_pattern = r'aria-label="(\d[\d,]+) star'

repo_matches = re.findall(repo_pattern, html)
desc_matches = re.findall(desc_pattern, html)
star_matches = re.findall(star_pattern, html)

print(f"Repos found: {len(repo_matches)}")
print(f"Descs found: {len(desc_matches)}")
print(f"Stars found: {len(star_matches)}")

# Keywords that indicate a skill-related repo
SKILL_KEYWORDS = [
    'skill', 'agent', 'claude', 'openai', 'mcp', 'tool',
    'prompt', 'workflow', 'task', 'automation', 'cli',
    'awesome', 'framework', 'hub', 'marketplace'
]

results = []
for i, repo in enumerate(repo_matches[:20]):
    desc = desc_matches[i].strip() if i < len(desc_matches) else ""
    stars = star_matches[i] if i < len(star_matches) else "0"
    
    desc_lower = desc.lower()
    if any(k in desc_lower or k in repo.lower() for k in SKILL_KEYWORDS):
        results.append({
            'name': repo.lstrip('/'),
            'desc': desc,
            'stars': stars
        })

print(f"\nSkill-related repos: {len(results)}")
for r in results:
    print(f"  {r['name']} ({r['stars']}★) - {r['desc'][:60]}")

# Save for next step
with open('/tmp/trending_skills.json', 'w') as f:
    json.dump(results, f)
PYEOF
```

### 3. Also Search GitHub API for SKILL.md Files

```bash
cd /tmp && \
curl -s -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/search/code?q=SKILL.md+in:path&per_page=30&sort=stars&order=desc" \
  | python3 -c "
import sys, json
d = json.load(sys.stdin)
items = d.get('items', [])
print(f'Found {len(items)} repos with SKILL.md in path')
results = []
for item in items[:15]:
    r = item['repository']
    results.append({
        'name': r['full_name'],
        'desc': r.get('description', ''),
        'stars': r.get('stargazers_count', 0)
    })
    print(f\"  {r['full_name']} ({r.get('stargazers_count',0)}★)\")
with open('/tmp/skillmd_repos.json', 'w') as f:
    json.dump(results, f)
"
```

### 4. Merge and Check Against Existing

```bash
python3 << 'PYEOF'
import json

REPO_PATH = "/Volumes/waku/github-维护/awesome/awesome-skills-repos/skills.json"
TRENDING = "/tmp/trending_skills.json"
SKILLMD = "/tmp/skillmd_repos.json"

with open(REPO_PATH, 'r') as f:
    existing = {r['name'] for r in json.load(f)}

with open(TRENDING, 'r') as f:
    trending = json.load(f)

try:
    with open(SKILLMD, 'r') as f:
        skillmd = json.load(f)
except:
    skillmd = []

new_from_trending = [r for r in trending if r['name'] not in existing]
new_from_skillmd = [r for r in skillmd if r['name'] not in existing]

print(f"Existing repos: {len(existing)}")
print(f"New from trending: {len(new_from_trending)}")
print(f"New from SKILL.md search: {len(new_from_skillmd)}")

all_new = new_from_trending + new_from_skillmd
# Dedupe
seen = set()
unique_new = []
for r in all_new:
    if r['name'] not in seen:
        seen.add(r['name'])
        unique_new.append(r)

print(f"Unique new repos: {len(unique_new)}")

for r in unique_new:
    print(f"  NEW: {r['name']} ({r['stars']}★) - {r['desc'][:50]}")

with open('/tmp/new_skills.json', 'w') as f:
    json.dump(unique_new, f, indent=2)
PYEOF
```

### 5. Add New Skills to skills.json

```bash
python3 << 'PYEOF'
import json
from datetime import datetime

REPO_PATH = "/Volumes/waku/github-维护/awesome/awesome-skills-repos/skills.json"
NEW_PATH = "/tmp/new_skills.json"
UPDATE_NOTES = "/Volumes/waku/github-维护/awesome/awesome-skills-repos/update-notes/"

with open(REPO_PATH, 'r') as f:
    repos = json.load(f)

with open(NEW_PATH, 'r') as f:
    new_skills = json.load(f)

if not new_skills:
    print("No new skills to add")
else:
    existing_names = {r['name'] for r in repos}
    added = []
    for s in new_skills:
        if s['name'] not in existing_names:
            repos.append({
                'name': s['name'],
                'stars': s.get('stars', 0),
                'desc': s.get('desc', ''),
                'url': f"https://github.com/{s['name']}",
                'added_date': datetime.now().strftime('%Y-%m-%d'),
                'source': 'trending'
            })
            added.append(s)
    
    # Sort by stars descending
    repos.sort(key=lambda x: x.get('stars', 0), reverse=True)
    
    with open(REPO_PATH, 'w') as f:
        json.dump(repos, f, indent=2, ensure_ascii=False)
    
    print(f"Added {len(added)} new skills")
    
    # Generate update notes
    today = datetime.now().strftime('%Y-%m-%d')
    note = f"""# 墨鉴-每日调研报告 {today}

## 今日发现

### 新增 Skills 仓库（{len(added)}个）

| 类型 | 标题 | ⭐ | 来源 | 状态 |
|------|------|-----|------|------|
"""
    for s in added:
        note += f"| skill | `{s['name']}` | {s.get('stars', 0)} | GitHub Trending | 🆕 已添加 |\n"
    
    note += f"""
## 更新内容

| 文件 | 操作 |
|------|------|
| `skills.json` | +{len(added)} 条目 |

## 数据规模

- 累计收录：{len(repos)} 个
"""
    
    with open(f"{UPDATE_NOTES}/{today}.md", 'w') as f:
        f.write(note)
    
    print(f"Update notes written to {today}.md")
PYEOF
```

### 6. Commit and Push

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos && \
git add skills.json update-notes/$(date +%Y-%m-%d).md 2>/dev/null && \
git status && \
echo "---" && \
read -p "Commit and push? (y/n) " ans && \
if [ "$ans" = "y" ]; then \
    git commit -m "chore: discover new skills $(date +%Y-%m-%d)" && \
    git push && \
    echo "Done!"; \
fi
```

## Notes

- Always review new skills before adding (check description quality)
- SKILL.md search finds actual skills, trending finds skill-related projects
- Run this 1-2x per week to keep collection fresh
- Source field: "trending" or "skillmd" to track discovery method
