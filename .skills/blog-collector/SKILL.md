---
name: blog-collector
description: Collect AI Agent Skills blog articles from WeChat, Zhihu, Medium and other platforms into the awesome-skills repository. Use when: (1) adding new blog articles to blogs/ directory, (2) collecting skill-related articles, (3) expanding the knowledge base. Triggers on: "collect blog", "add article", "scrape article", "blog collector", "collect article". The collected article goes into blogs/YYYY-MM-DD-article-slug.md with images in blogs/images/.
---

# Blog Collector

Collects blog articles from various platforms and saves them to the `blogs/` directory.

## Workflow

### 1. Receive Article URL

```bash
echo "Article URL to collect:"
# User provides: https://mp.weixin.qq.com/s/xxxxx
```

### 2. Extract Content

#### For WeChat Articles:

```bash
# Option A: Browser extraction (recommended for WeChat)
openclaw browser open targetUrl:"https://mp.weixin.qq.com/s/xxxxx"
# Then snapshot to get content, scroll to load all images

# Option B: Jina Reader
curl -s "https://r.jina.ai/https://mp.weixin.qq.com/s/xxxxx"
```

#### For Other Platforms:

```bash
# Zhihu
curl -s "https://r.jina.ai/https://zhihu.com/xxxxx"

# Medium
curl -s "https://r.jina.ai/https://medium.com/xxxxx"

# 掘金
curl -s "https://r.jina.ai/https://juejin.cn/xxxxx"
```

### 3. Extract and Download Images

```bash
# After getting content, extract image URLs via browser JS:
openclaw browser act targetId:<tab_id> request:'{"kind": "evaluate", "fn": "(() => { return Array.from(document.querySelectorAll(\"img\")).filter(img => img.src && img.src.includes(\"mmbiz\")).map(img => ({src: img.src, alt: img.alt || \"\", width: img.naturalWidth})).slice(0, 20); })()"}'

# Download images (filter imgIndex=0 = logo)
mkdir -p blogs/images/YYYY-MM-DD-article-slug/
curl -s -L -o "blogs/images/YYYY-MM-DD-article-slug/cover.jpg" "<cover_url>"
```

### 4. Generate Markdown

```bash
cat > "blogs/YYYY-MM-DD-article-slug.md" << 'EOF'
# Article Title

> **作者**：Author Name | **来源**：Source Name | **发布日期**：YYYY-MM-DD
> **原文**：https://original-url.com

---

![Cover](./images/YYYY-MM-DD-article-slug/cover.jpg)

---

## 文章正文

[Content here...]

## 参考资料

- [原文链接](https://original-url.com)
EOF
```

### 5. Determine Article Type & Destination

| Type | Destination |
|------|-------------|
| 论文/学术 | `papers/` |
| 技术博客 | `blogs/` |
| 行业分析 | `blogs/analysis/` |
| 工具介绍 | `blogs/` |

### 6. Push to GitHub

```bash
cd /Volumes/waku/github-维护/awesome/awesome-skills-repos
git add blogs/
git add blogs/images/
git commit -m "Add: <article title> (YYYY-MM-DD)"
git push
```

## Source Priority

1. **WeChat** (mp.weixin.qq.com) - Most common for Chinese AI/Agent content
2. **Medium** - High quality English articles
3. **Zhihu** (zhihu.com) - Technical discussions
4. **掘金** (juejin.cn) - Developer articles
5. **GitHub Blog** - Official announcements

## Image Filtering Rules

- ❌ Filter: Logo images (imgIndex=0 in WeChat URLs)
- ❌ Filter: Watermark/ads
- ✅ Keep: Technical diagrams, screenshots, charts
- ✅ Keep: Cover images
- Naming: `<platform>-<topic>-<number>.jpg`

## Known Blog Sources

| Source | URL Pattern | Quality |
|--------|-------------|---------|
| 沃垠AI | mp.weixin.qq.com (搜索) | ⭐⭐⭐⭐⭐ |
| 宝玉 | mp.weixin.qq.com (搜索) | ⭐⭐⭐⭐⭐ |
| 冷逸 | mp.weixin.qq.com (搜索) | ⭐⭐⭐⭐ |
| Agent 挖掘机 | mp.weixin.qq.com (搜索) | ⭐⭐⭐⭐ |
| Medium (unicodeveloper) | medium.com/@xxx | ⭐⭐⭐⭐⭐ |

## Notes

- Always filter WeChat images (many are ads/logos)
- Use Jina Reader for clean content extraction
- Name files: `YYYY-MM-DD-article-slug.md`
- Include original URL for reference
- Target: 3-5 articles per month
