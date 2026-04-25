#!/usr/bin/env python3
"""
Shared utilities for awesome-skills maintenance system.
Common functions used across multiple skills.
"""

import json
import subprocess
import time
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional


REPO_PATH = Path("/Volumes/waku/github-维护/awesome/awesome-skills-repos")
SKILLS_JSON = REPO_PATH / "skills.json"
UPDATE_NOTES_DIR = REPO_PATH / "update-notes"


def load_skills_json() -> List[Dict[str, Any]]:
    """Load skills.json and return list of repo entries."""
    with open(SKILLS_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_skills_json(repos: List[Dict[str, Any]]) -> None:
    """Save repos list to skills.json, sorted by stars descending."""
    repos.sort(key=lambda x: x.get('stars', 0), reverse=True)
    with open(SKILLS_JSON, 'w', encoding='utf-8') as f:
        json.dump(repos, f, f, indent=2, ensure_ascii=False)


def gh_api(endpoint: str, timeout: int = 10) -> Optional[Dict]:
    """Call GitHub API via gh CLI, return JSON or None on error."""
    try:
        result = subprocess.run(
            ['gh', 'api', endpoint],
            capture_output=True, text=True, timeout=timeout
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except Exception:
        pass
    return None


def gh_repo_info(name: str) -> Optional[Dict[str, Any]]:
    """Get repository metadata from GitHub API."""
    return gh_api(f'/repos/{name}')


def rate_limit_wait(remaining: int, limit: int = 5000) -> bool:
    """Check rate limit and wait if approaching limit. Returns True if waited."""
    if remaining < 100:
        print(f"  Rate limit low ({remaining}), waiting 60s...")
        time.sleep(60)
        return True
    return False


def update_notes_path(date: Optional[str] = None) -> Path:
    """Get update notes path for a date."""
    if date is None:
        date = datetime.now().strftime('%Y-%m-%d')
    return UPDATE_NOTES_DIR / f"{date}.md"


def write_update_notes(date: Optional[str], new_count: int, total: int,
                       source: str = "") -> Path:
    """Write update notes for a day's changes."""
    if date is None:
        date = datetime.now().strftime('%Y-%m-%d')
    
    path = update_notes_path(date)
    
    content = f"""# 墨鉴-每日调研报告 {date}

## 今日发现

### 新增 Skills 仓库（{new_count}个）

来源: {source or 'Manual update'}

## 更新内容

| 文件 | 操作 |
|------|------|
| `skills.json` | +{new_count} 条目 |

## 数据规模

- 累计收录：{total} 个
"""
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return path


CATEGORY_KEYWORDS = {
    'code-review': ['review', 'lint', 'quality', 'audit', 'test', 'security'],
    'web-development': ['frontend', 'backend', 'api', 'http', 'server', 'web'],
    'data-science': ['ml', 'ai', 'machine-learning', 'deep-learning', 'nlp', 'data'],
    'devops': ['ci', 'cd', 'docker', 'kubernetes', 'deploy', 'infra', 'cloud'],
    'mobile': ['ios', 'android', 'react-native', 'flutter', 'mobile'],
    'productivity': ['note', 'write', 'task', 'productivity', 'tool', 'automation'],
    'platform-integration': ['github', 'slack', 'jira', 'feishu', 'lark', 'discord', 'telegram'],
    'content-creation': ['blog', 'social', 'video', 'content', 'writing', 'publish'],
    'research': ['paper', 'research', 'academic', 'arxiv', 'knowledge', 'study'],
    'framework': ['framework', 'agent', 'orchestration', 'workflow', 'harness'],
    'skill-tools': ['skill', 'claude-code', 'openclaude', 'codex', 'prompt'],
    'security': ['security', 'auth', 'crypto', 'encrypt', 'vulnerability', 'safe'],
    'database': ['database', 'sql', 'nosql', 'db', 'storage', 'data'],
}


def infer_category(name: str, desc: str, topics: List[str] = None) -> str:
    """Infer category from repo name, description, and topics."""
    text = f"{name} {desc} {' '.join(topics or [])}".lower()
    
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(k in text for k in keywords):
            return category
    
    return 'other'


def auto_tags(name: str, desc: str, language: str = None, 
              topics: List[str] = None) -> List[str]:
    """Generate auto tags for a repository."""
    tags = []
    
    # Platform detection
    platforms = {
        'claude-code': 'claude-code',
        'claude': 'claude',
        'cursor': 'cursor',
        'codex': 'codex',
        'opencode': 'opencode',
        'openclaw': 'openclaw',
    }
    name_lower = name.lower()
    for platform, tag in platforms.items():
        if platform in name_lower:
            tags.append(tag)
    
    # Language tag
    if language and language != 'Unknown':
        tags.append(language.lower())
    
    # Topic tags (first 3)
    if topics:
        tags.extend(topics[:3])
    
    return list(set(tags))


def check_github_url(url: str, timeout: int = 5) -> int:
    """Check if a GitHub URL returns 200. Returns HTTP status code."""
    try:
        result = subprocess.run(
            ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}',
             '-L', '--max-time', str(timeout), url],
            capture_output=True, text=True, timeout=timeout + 2
        )
        return int(result.stdout.strip())
    except:
        return 999


def find_markdown_files(repo_path: Path = None) -> List[Path]:
    """Find all markdown files in repo, excluding .git."""
    if repo_path is None:
        repo_path = REPO_PATH
    
    md_files = []
    for path in repo_path.rglob('*.md'):
        if '.git' not in str(path):
            md_files.append(path)
    return md_files


def extract_github_links(md_files: List[Path] = None) -> List[str]:
    """Extract all unique GitHub URLs from markdown files."""
    import re
    
    if md_files is None:
        md_files = find_markdown_files()
    
    urls = set()
    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
            matches = re.findall(
                r'https://github\.com/[a-zA-Z0-9_-]+/[a-zA-Z0-9_./-]+',
                content
            )
            for url in matches:
                # Normalize: remove trailing slashes, .git
                url = url.rstrip('/').replace('.git', '')
                urls.add(url)
        except:
            pass
    
    return sorted(urls)


if __name__ == '__main__':
    print("Awesome-Skills Maintenance Utilities")
    print(f"REPO_PATH: {REPO_PATH}")
    print(f"SKILLS_JSON: {SKILLS_JSON}")
    
    # Quick health check
    if SKILLS_JSON.exists():
        repos = load_skills_json()
        print(f"Skills loaded: {len(repos)}")
        
        needs_enrichment = [r for r in repos if 'license' not in r or 'language' not in r]
        print(f"Repos needing enrichment: {len(needs_enrichment)}")
    else:
        print("skills.json not found!")
