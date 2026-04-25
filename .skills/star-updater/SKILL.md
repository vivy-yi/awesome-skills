---
name: star-updater
description: Update GitHub star counts for all repositories in skills.json. Use when: (1) scheduled star update task fires, (2) manually refreshing star counts, (3) comparing star growth over time. Triggers on: "update stars", "refresh star counts", "sync stars", "star update". This skill updates ALL 337 repositories in skills.json using GitHub API with proper rate limiting. NOT for: updating a single repo (just use gh CLI manually), or checking stars for a new repo (use add-skill instead).
---

# Star Updater

Updates star counts for all repositories in `skills.json` using GitHub API with proper batching and rate limit handling.

## Workflow

### 1. Read current skills.json

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos
wc -l skills.json
jq length skills.json
```

### 2. Run the update script

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos
python3 << 'PYEOF'
import json
import subprocess
import time
from datetime import datetime

REPO_PATH = "/Volumes/waku/github-维护/awesome/awesome-skills-repos/skills.json"
OUTPUT_PATH = REPO_PATH

with open(REPO_PATH, 'r') as f:
    repos = json.load(f)

print(f"Total repos to check: {len(repos)}")

updated = 0
errors = 0
rate_limited = False

for i, repo in enumerate(repos):
    name = repo.get('name', '')
    if not name:
        continue
    
    # Progress indicator
    if i % 50 == 0:
        print(f"Progress: {i}/{len(repos)}...")
    
    try:
        result = subprocess.run(
            ['gh', 'api', f'/repos/{name}'],
            capture_output=True, text=True, timeout=10
        )
        
        if result.returncode == 0:
            data = json.loads(result.stdout)
            new_stars = data.get('stargazers_count', repo.get('stars', 0))
            old_stars = repo.get('stars', 0)
            
            if new_stars != old_stars:
                print(f"  {name}: {old_stars} -> {new_stars}")
                repo['stars'] = new_stars
                repo['last_updated'] = datetime.now().strftime('%Y-%m-%d')
                updated += 1
        elif 'rate limit' in result.stderr.lower() or result.returncode == 403:
            rate_limited = True
            print(f"  Rate limited at {i}/{len(repos)}, waiting 60s...")
            time.sleep(60)
        else:
            errors += 1
            
    except Exception as e:
        errors += 1
        if errors <= 5:
            print(f"  Error {name}: {e}")
    
    # Be nice to GitHub API - 3 req/sec max
    time.sleep(0.3)

# Save updated data
with open(OUTPUT_PATH, 'w') as f:
    json.dump(repos, f, f, indent=2, ensure_ascii=False)

print(f"\n=== Update Complete ===")
print(f"Total repos: {len(repos)}")
print(f"Updated: {updated}")
print(f"Errors: {errors}")

# Generate update summary for commit message
with open('/tmp/star_update_summary.txt', 'w') as f:
    f.write(f"Updated: {updated}, Errors: {errors}, Total: {len(repos)}\n")
PYEOF
```

### 3. Check what changed

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos
git diff --stat skills.json
```

### 4. Commit and push (only if changes exist)

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos
UPDATED=$(git diff --numstat skills.json | awk '{print $1}')
if [ "$UPDATED" != "0" ]; then
    git add skills.json
    git commit -m "chore: update stars $(date +%Y-%m-%d)"
    git push
    echo "Pushed star updates"
else
    echo "No changes to push"
fi
```

## Verification

After push, verify the update:
```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos
git log -1 --stat
```

## Notes

- Uses `gh api` (authenticated) for higher rate limits
- Sleeps 0.3s between requests to stay under 5000 req/hour limit
- Backs off 60s if rate limited
- Records `last_updated` timestamp per repo
- Safe to re-run - idempotent
