---
name: metadata-enricher
description: Enrich skills.json with additional metadata (category, tags, license, language, last_updated). Use when: (1) adding new metadata fields to skills.json, (2) categorizing uncatégorized skills, (3) enriching repo metadata. Triggers on: "enrich metadata", "add tags", "categorize skills", "metadata enrichment", "add categories". NOT for: updating star counts (use star-updater), or discovering new skills (use trending-crawler).
---

# Metadata Enricher

Enriches `skills.json` with additional metadata fields for better categorization and filtering.

## Target Metadata Schema

```json
{
  "name": "owner/repo",
  "stars": 1234,
  "desc": "Description",
  "url": "https://github.com/owner/repo",
  "category": "code-review",       // NEW: primary category
  "tags": ["security", "claude"],  // NEW: searchable tags
  "license": "MIT",                // NEW: license type
  "language": "Python",             // NEW: primary language
  "added_date": "2026-04-20",      // NEW: when added to collection
  "last_updated": "2026-04-25",    // NEW: last star/meta update
  "source": "trending"             // NEW: discovery method
}
```

## Workflow

### 1. Define Category Taxonomy

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos && \
cat << 'EOF'
CATEGORIES:
  - code-review        # Code quality, security, testing
  - web-development    # Frontend, backend, APIs
  - data-science        # ML, AI, analytics, notebooks
  - devops             # CI/CD, infrastructure, containers
  - mobile             # iOS, Android, React Native
  - productivity       # Writing, notes, task management
  - platform-integration # GitHub, Slack, Jira, Feishu
  - content-creation    # Blog, social media, video
  - research           # Papers, academic, knowledge
  - framework          # Agentic frameworks, orchestration
  - skill-tools        # Skills creation/maintenance tools
  - database           # SQL, NoSQL, data storage
  - security           # Cybersecurity, auth, encryption
  - other              # Uncategorized

TAGS (auto-detectable):
  - claude-code, cursor, opencode, codex  # Platform-specific
  - python, typescript, rust, go          # Language
  - mcp, api, cli, agent                  # Tech type
  - awesome, list, collection              # List type
  - security, review, test                # Function
  - chinese, english                       # Language of docs
EOF
```

### 2. Enrich All Repos via GitHub API

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos && \
python3 << 'PYEOF'
import json
import subprocess
import time
from datetime import datetime

REPO_PATH = "/Volumes/waku/github-维护/awesome/awesome-skills-repos/skills.json"

with open(REPO_PATH, 'r') as f:
    repos = json.load(f)

print(f"Total repos to enrich: {len(repos)}")

# Check which repos need enrichment
needs_enrichment = [r for r in repos if 'license' not in r or 'language' not in r]
print(f"Repos needing enrichment: {len(needs_enrichment)}")

# Limit to avoid rate limiting
LIMIT = 100
to_process = needs_enrichment[:LIMIT]
print(f"Processing first {LIMIT}...")

def get_metadata(name):
    """Fetch metadata from GitHub API"""
    try:
        result = subprocess.run(
            ['gh', 'api', f'/repos/{name}'],
            capture_output=True, text=True, timeout=10
        )
        if result.returncode == 0:
            data = json.loads(result.stdout)
            return {
                'license': data.get('license', {}).get('spdx_id') or 'Unknown',
                'language': data.get('language') or 'Unknown',
                'topics': data.get('topics', []),
                'description': data.get('description') or '',
                'homepage': data.get('homepage') or '',
            }
    except:
        pass
    return None

# Keyword -> category mapping
CATEGORY_KEYWORDS = {
    'code-review': ['review', 'lint', 'quality', 'audit', 'test'],
    'web-development': ['frontend', 'backend', 'api', 'http', 'server'],
    'data-science': ['ml', 'ai', 'machine-learning', 'deep-learning', 'nlp'],
    'devops': ['ci', 'cd', 'docker', 'kubernetes', 'deploy', 'infra'],
    'mobile': ['ios', 'android', 'react-native', 'flutter'],
    'productivity': ['note', 'write', 'task', 'productivity', 'tool'],
    'platform-integration': ['github', 'slack', 'jira', 'feishu', 'lark', 'discord'],
    'content-creation': ['blog', 'blog', 'social', 'video', 'content'],
    'research': ['paper', 'research', 'academic', 'arxiv', 'knowledge'],
    'framework': ['framework', 'agent', 'orchestration', 'workflow', 'harness'],
    'skill-tools': ['skill', 'claude-code', 'openclaude', 'codex'],
    'security': ['security', 'auth', 'crypto', 'encrypt', 'vulnerability'],
    'database': ['database', 'sql', 'nosql', 'db', 'storage'],
}

def infer_category(name, desc, topics):
    text = (name + ' ' + desc + ' ' + ' '.join(topics)).lower()
    for cat, keywords in CATEGORY_KEYWORDS.items():
        if any(k in text for k in keywords):
            return cat
    return 'other'

enriched = 0
for i, repo in enumerate(to_process):
    name = repo.get('name', '')
    if not name:
        continue
    
    meta = get_metadata(name)
    if meta:
        repo['license'] = meta['license']
        repo['language'] = meta['language']
        
        # Infer category from name + description + topics
        inferred_cat = infer_category(
            name,
            repo.get('desc', ''),
            meta.get('topics', [])
        )
        repo['category'] = inferred_cat
        
        # Auto-generate tags
        tags = []
        # Platform tags
        for platform in ['claude-code', 'claude', 'cursor', 'codex', 'opencode']:
            if platform in name.lower() or platform in repo.get('desc', '').lower():
                tags.append(platform)
        # Language tag
        if meta['language'] and meta['language'] != 'Unknown':
            tags.append(meta['language'].lower())
        # Topic tags (first 3)
        tags.extend(meta.get('topics', [])[:3])
        repo['tags'] = list(set(tags)) if tags else []
        
        enriched += 1
    
    if (i+1) % 20 == 0:
        print(f"  Progress: {i+1}/{len(to_process)}")
    
    time.sleep(0.3)  # Rate limit courtesy

# Save
with open(REPO_PATH, 'w') as f:
    json.dump(repos, f, indent=2, ensure_ascii=False)

print(f"\n=== Enrichment Complete ===")
print(f"Enriched: {enriched}/{len(to_process)}")

# Count categories
categories = {}
for r in repos:
    cat = r.get('category', 'unknown')
    categories[cat] = categories.get(cat, 0) + 1

print("\nCategory distribution:")
for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
    print(f"  {cat}: {count}")
PYEOF
```

### 3. Review and Validate

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos && \
python3 << 'PYEOF'
import json

with open('skills.json', 'r') as f:
    repos = json.load(f)

# Show sample of each category
categories = {}
for r in repos:
    cat = r.get('category', 'other')
    if cat not in categories:
        categories[cat] = []
    categories[cat].append(r)

print("=== Category Samples ===\n")
for cat in sorted(categories.keys()):
    print(f"## {cat} ({len(categories[cat])} repos)")
    for r in categories[cat][:3]:
        tags = ', '.join(r.get('tags', [])[:5])
        print(f"  - {r['name']} [{r.get('language','?')}] tags:{tags}")
    print()
PYEOF
```

### 4. Commit

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos && \
git diff --stat skills.json | head -5 && \
echo "---" && \
read -p "Commit enrichment? (y/n) " ans && \
if [ "$ans" = "y" ]; then \
    git add skills.json && \
    git commit -m "feat: enrich skills.json with category, tags, license, language" && \
    git push; \
fi
```

## Notes

- Run enrichment after adding many new repos
- Categories are inferred from name/description - manual review recommended for edge cases
- Tags are auto-generated from GitHub topics + inferred keywords
- Can re-run to fill in missing fields without overwriting existing data
