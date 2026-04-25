---
name: awesome-skills-maintenance
description: Main orchestrator for the awesome-skills repository maintenance system. Use when: (1) performing any maintenance task on the awesome-skills repo, (2) updating skills.json, (3) collecting content, (4) running scheduled maintenance, (5) asking about the maintenance system. Triggers on: "awesome skills maintenance", "maintain awesome skills", "run maintenance", "skills system", "awesome skills 维护", "run all maintenance", "check skills health". This is the entry point skill that delegates to sub-skills based on the task type. The sub-skills are: star-updater, trending-crawler, link-doctor, metadata-enricher, blog-collector, paper-collector, self-maintainer.
---

# Awesome Skills Maintenance System

Agent-centric maintenance system for the [awesome-skills](https://github.com/vivy-yi/awesome-skills) repository.

## Repository Overview

- **URL**: https://github.com/vivy-yi/awesome-skills
- **Local Path**: `/Volumes/waku/github-维护/awesome/awesome-skills-repos`
- **Skills**: 337 repositories in `skills.json`
- **Content**: 3 blog posts, 5 papers, 13 tutorials
- **Update Notes**: Daily reports in `update-notes/`

## Sub-Skills Architecture

```
awesome-skills-maintenance (this skill)
├── star-updater       → Update all star counts in skills.json
├── trending-crawler    → Discover new skills from GitHub Trending
├── link-doctor        → Fix broken links in markdown files
├── metadata-enricher  → Add category/tags/license to skills.json
├── blog-collector     → Collect blog articles into blogs/
├── paper-collector    → Collect papers into papers/
└── self-maintainer   → Audit and improve the maintenance system
```

## Quick Reference

| Task | Sub-Skill | Trigger Phrase |
|------|-----------|----------------|
| Update stars | `star-updater` | "update stars", "refresh stars" |
| Find new skills | `trending-crawler` | "discover skills", "find new skills" |
| Fix links | `link-doctor` | "fix links", "broken links" |
| Add metadata | `metadata-enricher` | "enrich metadata", "add categories" |
| Collect blog | `blog-collector` | "collect blog", "add article" |
| Collect paper | `paper-collector` | "collect paper", "add paper" |
| Self-audit | `self-maintainer` | "self-maintain", "audit skills" |
| Run all | (this skill) | "run maintenance", "full maintenance" |

## Running Full Maintenance

To run all maintenance tasks in sequence:

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos

echo "=== Awesome Skills Full Maintenance ==="
echo "Date: $(date)"
echo ""

# 1. Self-audit first
echo "Step 1: Self-audit..."
openclaw skills run self-maintainer

# 2. Update stars
echo "Step 2: Update stars..."
openclaw skills run star-updater

# 3. Discover new skills
echo "Step 3: Discover new skills..."
openclaw skills run trending-crawler

# 4. Fix broken links
echo "Step 4: Fix broken links..."
openclaw skills run link-doctor

# 5. Check metadata
echo "Step 5: Check metadata enrichment..."
openclaw skills run metadata-enricher

echo ""
echo "=== Maintenance Complete ==="
echo "Review .skills/HEALTH.md for system status"
```

## Running Individual Tasks

Each sub-skill can be triggered independently. See the sub-skill SKILL.md files for detailed instructions.

## Cron Schedule

Recommended maintenance schedule:

| Task | Frequency | Command |
|------|----------|---------|
| Star update | Weekly | `openclaw skills run star-updater` |
| Trending crawl | 2x/week | `openclaw skills run trending-crawler` |
| Link check | Weekly | `openclaw skills run link-doctor` |
| Metadata enrich | Monthly | `openclaw skills run metadata-enricher` |
| Self-maintain | Weekly | `openclaw skills run self-maintainer` |
| Blog collect | As needed | `openclaw skills run blog-collector` |
| Paper collect | As needed | `openclaw skills run paper-collector` |

## Cron Configuration

Add to crontab (`crontab -e`):

```cron
# Awesome Skills Maintenance
# Every Sunday 2AM: Full maintenance
0 2 * * 0 cd /Volumes/waku/github-维护/awesome/awesome-skills-repos && openclaw skills run star-updater && openclaw skills run self-maintainer

# Every Tuesday 2AM: Trending discovery
0 2 * * 2 cd /Volumes/waku/github-维护/awesome/awesome-skills-repos && openclaw skills run trending-crawler

# Every Friday 2AM: Link health check
0 2 * * 5 cd /Volumes/waku/github-维护/awesome/awesome-skills-repos && openclaw skills run link-doctor
```

## GitHub Actions (Optional)

The repo already has GitHub Actions. Update `.github/workflows/update-stars.yml` to trigger on this schedule instead:

```yaml
on:
  schedule:
    - cron: '0 2 * * 0'  # Weekly Sunday 2AM UTC
  workflow_dispatch:
```

## Maintenance Stats

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos

# Skills count
echo "Skills: $(jq length skills.json)"

# Blog posts
echo "Blog posts: $(ls blogs/*.md 2>/dev/null | wc -l | tr -d ' ')"

# Papers
echo "Papers: $(ls papers/*.md 2>/dev/null | wc -l | tr -d ' ')"

# Last update
echo "Last update: $(git log -1 --format='%ad' --date=short)"
```

## Sub-Skill Summary

### star-updater
Updates star counts for all 337 repos in skills.json using GitHub API. Handles rate limits, records timestamps.

### trending-crawler
Scrapes GitHub Trending and searches for SKILL.md files. Adds new repos to skills.json with source tracking.

### link-doctor
Scans all markdown files for broken links. Repairs via Wayback Machine or GitHub search for renamed repos.

### metadata-enricher
Adds category, tags, license, and language fields to skills.json entries via GitHub API.

### blog-collector
Collects blog articles from WeChat, Medium, Zhihu, etc. Saves to blogs/ with images.

### paper-collector
Collects academic papers from arXiv, Semantic Scholar. Saves to papers/ with citation info.

### self-maintainer
Audits the .skills/ directory health, fixes anti-patterns, extracts shared code, generates HEALTH.md.

## Health Report

After running, check `.skills/HEALTH.md` for system status.

Current sub-skills:
- `star-updater` — ✅
- `trending-crawler` — ✅
- `link-doctor` — ✅
- `metadata-enricher` — ✅
- `blog-collector` — ✅
- `paper-collector` — ✅
- `self-maintainer` — ✅

## Notes

- All skills follow OpenClaw SKILL.md specification
- Skills are stored in `.skills/` directory (travels with repo)
- Each skill is self-contained with embedded instructions
- Agent-centric: designed for OpenClaw/Claude Code to execute
- Self-maintaining: the self-maintainer skill keeps everything healthy
