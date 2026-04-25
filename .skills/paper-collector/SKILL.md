---
name: paper-collector
description: Collect academic papers related to AI Agent Skills into the awesome-skills papers/ directory. Use when: (1) adding new papers to papers/ directory, (2) collecting academic papers on Skills/Agent frameworks, (3) expanding research section. Triggers on: "collect paper", "add paper", "paper collector", "research paper", "arxiv paper".
---

# Paper Collector

Collects academic papers about AI Agent Skills and saves them to `papers/`.

## Workflow

### 1. Search for Relevant Papers

```bash
# Search arXiv for skill-related papers
curl -s "https://export.arxiv.org/api/query?search_query=ti:agent+skill+OR+ti:tool+agent+OR+ti:agent+framework&start=0&max_results=20&sortBy=submittedDate&sortOrder=descending" | \
python3 << 'PYEOF'
import sys
import re
from datetime import datetime

xml = sys.stdin.read()

# Extract entries
entries = re.findall(r'<entry>(.*?)</entry>', xml, re.DOTALL)

papers = []
for entry in entries:
    title = re.search(r'<title>(.*?)</title>', entry, re.DOTALL)
    summary = re.search(r'<summary>(.*?)</summary>', entry, re.DOTALL)
    link = re.search(r'<id>(.*?)</id>', entry)
    published = re.search(r'<published>(.*?)</published>', entry)
    
    if title and link:
        title_clean = ' '.join(title.group(1).split())
        summary_clean = ' '.join(summary.group(1).split())[:300] if summary else ""
        link_url = link.group(1)
        date = published.group(1)[:10] if published else ""
        
        papers.append({
            'title': title_clean,
            'summary': summary_clean,
            'url': link_url,
            'date': date
        })

print(f"Found {len(papers)} recent papers:\n")
for p in papers[:10]:
    print(f"[{p['date']}] {p['title']}")
    print(f"  {p['summary'][:150]}...")
    print()
PYEOF
```

### 2. Also Search Google Scholar / Semantic Scholar

```bash
# Search Semantic Scholar API (free, no auth needed)
curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=agent+skill+framework&limit=20&fields=title,abstract,year,citationCount,openAccessPdf,authors" | \
python3 << 'PYEOF'
import sys
import json

data = json.load(sys.stdin)
papers = data.get('data', [])

print(f"Found {len(papers)} papers on Semantic Scholar:\n")
for p in papers[:10]:
    title = p.get('title', '')
    year = p.get('year', '?')
    citations = p.get('citationCount', 0)
    abstract = p.get('abstract', '')[:200] if p.get('abstract') else ''
    pdf = p.get('openAccessPdf', {}).get('url', '') if p.get('openAccessPdf') else ''
    
    print(f"[{year}] {title} (cited: {citations})")
    if pdf:
        print(f"  PDF: {pdf}")
    print()
PYEOF
```

### 3. Download Paper PDF or Extract arXiv Abstract

```bash
# For arXiv papers, save abstract as markdown
ARXIV_ID="2312.12345"  # from URL

cat > "papers/paper-slug.md" << 'EOF'
# Paper Title

> **arXiv**: [arXiv:XXXX.XXXXX](https://arxiv.org/abs/XXXX.XXXXX)
> **年份**：2024
> **引用数**：XX
> **作者**：Author 1, Author 2

---

## 摘要

Paper abstract here...

## 核心贡献

1. Contribution 1
2. Contribution 2

## 方法

[Key methods described]

## 与 Skills 相关性

[How this relates to AI Agent Skills]

## 参考资料

- [arXiv](https://arxiv.org/abs/XXXX.XXXXX)
- [PDF](https://arxiv.org/pdf/XXXX.XXXXX.pdf)
EOF
```

### 4. Add to papers/README.md if exists

```bash
# Update papers README if it exists
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos/papers
if [ -f README.md ]; then
    echo "- [Paper Title](paper-slug.md) - YYYY-MM-DD" >> README.md
fi
```

### 5. Push to GitHub

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos
git add papers/
git commit -m "Add: Paper Title (YYYY-MM)"
git push
```

## Relevant Paper Topics

- Skill discovery and selection
- Skill composition and orchestration
- Skill security and trust
- LLM tool use / function calling
- Agent frameworks and architectures
- Prompt engineering for agents
- Skill distillation and transfer
- Multi-agent collaboration

## Target: 2-4 papers per month

Focus on papers that:
1. Introduce new Skill concepts or frameworks
2. Analyze Skill effectiveness
3. Address Skill security/safety
4. Present skill-related datasets

## Notes

- Always cite the original arXiv/paper URL
- Include why the paper is relevant to Skills
- Use Semantic Scholar for citation counts
- Check if open access PDF is available
