# Contributing to Awesome AI Skills

Thank you for your interest in contributing to Awesome AI Skills! This document provides guidelines and instructions for contributing.

## How to Contribute

### Adding a New Skill

1. **Fork the Repository**
   ```bash
   git clone https://github.com/your-username/awesome-skills-repos.git
   cd awesome-skills-repos
   ```

2. **Create a Branch**
   ```bash
   git checkout -b add/skill-name
   ```

3. **Update README.md**
   - Add your skill to the appropriate category section
   - Follow this format:
     ```markdown
     - [repository-name](https://github.com/user/repo) - ⭐ 1,234 · Brief description
     ```

4. **Update JSON Data**
   - Add your entry to `skills.json`
   - Ensure all required fields are present:
     ```json
     {
       "name": "user/repo-name",
       "stars": 1234,
       "desc": "Brief description",
       "url": "https://github.com/user/repo-name"
     }
     ```

5. **Submit a Pull Request**
   - Push your changes
   - Create a descriptive pull request
   - Reference any related issues

## Inclusion Criteria

Skills should meet the following criteria:

### ✅ What We Include

- **AI Agent Skills**: Capabilities designed for AI agents (Claude, GPT, etc.)
- **Minimum Stars**: 100+ GitHub stars
- **Active Maintenance**: Repository updated within the last 6 months
- **Clear Documentation**: Has README with usage instructions
- **Relevance**: Related to AI agents, Claude Code, or agent frameworks

### ❌ What We Exclude

- **Human Learning Resources**: Tutorials, courses, coding challenges
- **Abandoned Projects**: No updates in 6+ months
- **Poor Documentation**: No clear usage instructions
- **Non-AI Skills**: Skills meant for human learning only

## Categories

Choose the most appropriate category for your contribution:

- **🌐 Skills Web** - Web platforms and marketplaces for AI agent skills
- **🤖 Claude Code 生态** - Claude Code ecosystem tools and configurations
- **📚 Awesome Lists & 资源集合** - Curated resource collections
- **🔧 Agent Skills & Tools** - Development utilities and tools
- **📝 内容创作 & 文档** - Content generation skills
- **🎨 UI/UX & 设计** - Design and frontend skills
- **🔌 MCP 服务器 & 集成** - API integrations and MCP servers
- **🤖 浏览器 & 自动化** - Web automation skills
- **🔬 科学 & 研究工具** - Scientific computing skills
- **🔒 安全 & 审计** - Security and audit tools
- **🌐 多智能体系统** - Multi-agent coordination
- **🤖 Bot Skills** - Bot framework skills (Moltbot, etc.)
- **🎯 特定领域工具** - Specialized domain skills

## Style Guidelines

### README Format

- Keep descriptions concise (one line)
- Use sentence case for descriptions
- Include star count with ⭐ emoji
- Use proper markdown linking

### Example

```markdown
- [username/skill-name](https://github.com/username/skill-name) - ⭐ 1,234 · Brief description of what the skill does
```

## Review Process

All submissions go through a review process:

1. **Automated Checks**
   - Minimum star count (100+)
   - Valid repository URL
   - Required JSON fields present

2. **Manual Review**
   - Relevance to AI agents
   - Documentation quality
   - Active maintenance check
   - Category appropriateness

3. **Decision**
   - ✅ Approved - Merged within 3-5 days
   - 🔄 Changes Requested - Feedback provided
   - ❌ Declined - Reason explained

## Getting Help

If you need help:

- **Open an Issue** - Ask questions or report problems
- **Start a Discussion** - Engage with the community
- **Check Existing Issues** - Your question may already be answered

## Code of Conduct

Be respectful and inclusive:

- Use welcoming and inclusive language
- Respect differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

## Recognition

Contributors are recognized in:

- **Contributors Section** - Listed in README
- **Release Notes** - Mentioned in changelog
- **Community Highlights** - Featured in announcements

Thank you for contributing to Awesome Agent Skills! 🎉
