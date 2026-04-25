---
name: link-doctor
description: Detect and repair broken links in the awesome-skills repository. Use when: (1) validating repository links, (2) fixing 404 errors, (3) checking link health. Triggers on: "fix links", "broken links", "link check", "validate links", "link doctor", "link health". NOT for: checking a single URL manually (just use curl), or updating star counts.
---

# Link Doctor

Detects broken links in README.md, tutorials, blogs, and papers, then attempts to repair them.

## Workflow

### 1. Scan All Markdown Files for Links

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos && \
find . -name "*.md" -not -path "./.git/*" | head -20 && \
echo "---" && \
# Extract all GitHub links
grep -rhops "https://github.com/" --include="*.md" . | \
grep -oE "https://github\.com/[a-zA-Z0-9_-]+/[a-zA-Z0-9_.-]+" | \
sort -u | head -50
```

### 2. Check Links with curl (Batch)

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos && \
python3 << 'PYEOF'
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

REPO_PATH = "/Volumes/waku/github-维护/awesome/awesome-skills-repos"

# Collect all GitHub URLs from markdown files
github_urls = set()
for ext in ['*.md']:
    result = subprocess.run(
        f'grep -rhops "https://github.com/" {REPO_PATH} --include="*.md" 2>/dev/null | grep -oE "https://github\.com/[^ )\"\\']+" | sort -u',
        shell=True, capture_output=True, text=True
    )
    for url in result.stdout.strip().split('\n'):
        if url:
            # Normalize - remove trailing slashes, .git, etc.
            url = url.rstrip('/').replace('.git', '')
            github_urls.add(url)

urls = list(github_urls)
print(f"Total unique GitHub URLs to check: {len(urls)}")

def check_url(url):
    """Check a URL and return status"""
    try:
        result = subprocess.run(
            ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', '-L', '--max-time', '10', url],
            capture_output=True, text=True, timeout=15
        )
        code = result.stdout.strip()
        return (url, code)
    except Exception as e:
        return (url, f"ERROR: {e}")

broken = []
working = []

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(check_url, url): url for url in urls[:100]}  # Check first 100
    
    for i, future in enumerate(as_completed(futures)):
        url, code = future.result()
        if code not in ['200', '301', '302']:
            broken.append((url, code))
            print(f"  BROKEN ({code}): {url}")
        else:
            working.append((url, code))
        
        if (i+1) % 20 == 0:
            print(f"Progress: {i+1}/{len(futures)}")

print(f"\n=== Results ===")
print(f"Working: {len(working)}")
print(f"Broken: {len(broken)}")

if broken:
    with open('/tmp/broken_links.json', 'w') as f:
        import json
        json.dump(broken, f, indent=2)
    print("Broken links saved to /tmp/broken_links.json")
PYEOF
```

### 3. Try to Repair Broken Links

```bash
python3 << 'PYEOF'
import subprocess
import json
import re

BROKEN_PATH = "/Volumes/waku/github-维护/awesome/awesome-skills-repos/.skills/link-doctor"

try:
    with open('/tmp/broken_links.json', 'r') as f:
        broken = json.load(f)
except:
    print("No broken links found or file not found")
    exit(0)

print(f"Attempting to repair {len(broken)} broken links...\n")

repaired = []
unrepairable = []

for url, code in broken:
    owner_repo = url.replace('https://github.com/', '')
    
    # Try 1: Check if repo was renamed (search API)
    try:
        search_result = subprocess.run(
            ['gh', 'api', f'/search/repositories?q={owner_repo.split("/")[-1]}+in:name&sort=stars&per_page=5'],
            capture_output=True, text=True, timeout=10
        )
        if search_result.returncode == 0:
            data = json.loads(search_result.stdout)
            items = data.get('items', [])
            if items:
                best = items[0]
                new_url = best['html_url']
                if new_url != url:
                    repaired.append({
                        'old': url,
                        'new': new_url,
                        'reason': f"Renamed/moved → {best['stargazers_count']}★"
                    })
                    print(f"  REPAIRED: {url}")
                    print(f"    -> {new_url} ({best['stargazers_count']}★)")
                    continue
    except:
        pass
    
    # Try 2: Wayback Machine
    try:
        wm_url = f"https://web.archive.org/web/2024/{url}"
        result = subprocess.run(
            ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', '--max-time', '5', wm_url],
            capture_output=True, text=True, timeout=8
        )
        if result.stdout.strip() == '200':
            repaired.append({
                'old': url,
                'new': wm_url,
                'reason': "Wayback Machine archive"
            })
            print(f"  ARCHIVED: {url}")
            print(f"    -> {wm_url}")
            continue
    except:
        pass
    
    # Unrepairable
    unrepairable.append({'url': url, 'code': code})
    print(f"  UNREPAIRABLE: {url} ({code})")

print(f"\n=== Summary ===")
print(f"Repaired: {len(repaired)}")
print(f"Unrepairable: {len(unrepairable)}")

if repaired:
    with open('/tmp/repaired_links.json', 'w') as f:
        json.dump(repaired, f, indent=2)

if unrepairable:
    with open('/tmp/unrepairable_links.json', 'w') as f:
        json.dump(unrepairable, f, indent=2)
PYEOF
```

### 4. Apply Repairs to Markdown Files

```bash
python3 << 'PYEOF'
import json
import subprocess
from pathlib import Path

REPO_PATH = Path("/Volumes/waku/github-维护/awesome/awesome-skills-repos")
REPAIRED_PATH = "/tmp/repaired_links.json"

try:
    with open(REPAIRED_PATH, 'r') as f:
        repaired = json.load(f)
except:
    print("No repairs to apply")
    exit(0)

print(f"Applying {len(repaired)} repairs...\n")

for item in repaired:
    old_url = item['old']
    new_url = item['new']
    
    # Find all markdown files containing this URL
    result = subprocess.run(
        ['grep', '-rl', old_url, str(REPO_PATH), '--include=*.md'],
        capture_output=True, text=True
    )
    
    files = result.stdout.strip().split('\n')
    
    for filepath in files:
        if not filepath:
            continue
        try:
            with open(filepath, 'r') as f:
                content = f.read()
            
            if old_url in content:
                new_content = content.replace(old_url, new_url)
                with open(filepath, 'w') as f:
                    f.write(new_content)
                print(f"  Fixed: {filepath}")
                print(f"    {old_url}")
                print(f"    -> {new_url}")
        except Exception as e:
            print(f"  Error fixing {filepath}: {e}")

print("\nAll repairs applied!")
PYEOF
```

### 5. Commit Changes

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos && \
git status && \
echo "---" && \
read -p "Commit and push repairs? (y/n) " ans && \
if [ "$ans" = "y" ]; then \
    git add -A && \
    git commit -m "fix: repair broken links $(date +%Y-%m-%d)" && \
    git push && \
    echo "Done!"; \
fi
```

## Notes

- Start with GitHub URLs (most common)
- Wayback Machine can rescue moved/deleted repos
- GitHub search API can find renamed repos
- Always review repairs before committing
- Run monthly to keep link health good
