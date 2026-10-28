<div align="center">

# 🧩 Awesome Agent Skills 中文导航

**精选真实可用的 Agent Skills、技能合集与规范资源**  
中文解读 · 按场景分类 · 标注来源与安装方式

[![GitHub stars](https://img.shields.io/github/stars/AnonymousLeeJJ/awesome-agent-skills-zh?style=social)](https://github.com/AnonymousLeeJJ/awesome-agent-skills-zh/stargazers)
[![License: CC BY 4.0](https://img.shields.io/badge/Content-CC%20BY%204.0-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[English](README_EN.md) ｜ [在线导航](https://anonymousleejj.github.io/awesome-agent-skills-zh/) ｜ [提交 Skill](https://github.com/AnonymousLeeJJ/awesome-agent-skills-zh/issues/new?template=submit-skill.yml)

</div>

---

## 🤔 这是什么？

**Agent Skills** 是一种把专业知识、工作流程和辅助脚本打包给 AI Agent 的开放格式。一个 Skill 通常包含：

- `SKILL.md`：什么时候使用、如何执行、注意事项
- `references/`：参考文档、模板、案例
- `scripts/`：可选的辅助脚本

这个项目不是“复制一堆英文仓库链接”，而是一个面向中文开发者的 **Agent Skills 导航**：

- ✅ 只收录可核验的公开项目
- 🏷️ 标注官方 / 社区 / 索引 / 原创来源
- 📦 尽量给出明确安装方式
- 🧭 按文档、开发、设计、写作、研究等场景分类
- ⚠️ 明确提示脚本安全风险，不把“收录”包装成安全背书
- 📚 与 [书灵.skill](https://github.com/AnonymousLeeJJ/shuling-skill) 联动，支持蒸馏新的顾问技能

## 🌐 在线浏览

👉 **https://anonymousleejj.github.io/awesome-agent-skills-zh/**

支持搜索、分类筛选、来源筛选和一键复制安装命令。

## ⭐ 首批精选

| Skill / 资源 | 类型 | 适合场景 | 来源 |
| --- | --- | --- | --- |
| [Skill Creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | 单项 Skill | 学习如何创建高质量 SKILL.md | Anthropic 官方 |
| [PDF](https://github.com/anthropics/skills/tree/main/skills/pdf) / [DOCX](https://github.com/anthropics/skills/tree/main/skills/docx) / [PPTX](https://github.com/anthropics/skills/tree/main/skills/pptx) / [XLSX](https://github.com/anthropics/skills/tree/main/skills/xlsx) | 文档技能 | 文档读取、编辑和生成 | Anthropic 官方 |
| [MCP Builder](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | 单项 Skill | 创建 MCP Server、接入外部系统 | Anthropic 官方 |
| [Webapp Testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) | 单项 Skill | 用 Playwright 测试 Web 应用 | Anthropic 官方 |
| [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) | 技能合集 | React/Next.js 性能、Web 设计、部署 | Vercel Labs |
| [Stitch Skills](https://github.com/google-labs-code/stitch-skills) | 技能合集 | UI 生成、设计系统、React 组件转换 | Google Labs |
| [Agent Skills](https://github.com/addyosmani/agent-skills) | 技能合集 | 覆盖规格、计划、构建、测试、审查、发布 | Addy Osmani |
| [Superpowers](https://github.com/obra/superpowers) | 工程框架 | 头脑风暴、计划、执行、审查的长任务流程 | 社区 |
| [Planning with Files](https://github.com/OthmanAdi/planning-with-files) | 单项 Skill | 用文件保存长任务计划和进度 | 社区 |
| [书灵.skill](https://github.com/AnonymousLeeJJ/shuling-skill) | 原创 Skill | 把书、课程和资料蒸馏成 AI 顾问 | 本站原创 |

完整列表见 [在线导航](https://anonymousleejj.github.io/awesome-agent-skills-zh/) 或 [`skills.json`](skills.json)。

## 🚀 如何安装 Skill？

不同 Agent 的目录略有差异，核心都是“把包含 `SKILL.md` 的文件夹放到 skills 目录”。

### Claude Code

```bash
# 官方示例：先添加 Anthropic marketplace
/plugin marketplace add anthropics/skills

# 安装文档技能包
/plugin install document-skills@anthropic-agent-skills

# 安装示例技能包
/plugin install example-skills@anthropic-agent-skills
```

### 使用 skills CLI

```bash
# 安装 Vercel Labs 技能集
npx skills add vercel-labs/agent-skills

# 安装 Google Stitch 技能集
npx skills add google-labs-code/stitch-skills
```

### WorkBuddy / 其他支持 Agent Skills 的工具

把目标 Skill 文件夹复制到对应工具的 skills 目录。例如 WorkBuddy：

```text
~/.workbuddy/skills/<skill-name>/SKILL.md
```

> ⚠️ 安全提示：Skill 可以包含会在本机执行的脚本。安装前请阅读 `SKILL.md` 和脚本内容，谨慎授予文件、网络或终端权限。本站的“链接已核验”只表示链接存在，不代表安全审计。

## 🧭 分类

- 📄 **文档处理**：PDF、Word、PPT、Excel、协同写作
- 💻 **开发工程**：测试、部署、性能、工程流程
- 🎨 **设计创意**：前端设计、生成艺术、主题与视觉规范
- ✍️ **写作沟通**：品牌规范、内部沟通、顾问技能
- 🧩 **技能开发**：Skill Creator、MCP Builder、最佳实践
- 🔎 **研究规划**：长期规划、知识图谱、任务分解
- 📚 **合集索引**：大型英文索引和社区合集

## 📦 数据结构

所有条目维护在 [`skills.json`](skills.json)，字段包括：

```json
{
  "name": "Skill Creator",
  "url": "https://github.com/anthropics/skills/tree/main/skills/skill-creator",
  "category": "meta",
  "source": "official",
  "type": "skill",
  "license": "Apache-2.0",
  "compatibility": "Claude Code / Claude.ai / Claude API",
  "install": "/plugin install example-skills@anthropic-agent-skills",
  "description": "中文说明",
  "featured": true
}
```

本地校验和构建：

```bash
python scripts/validate.py
python build_site.py
```

## 🤝 贡献

欢迎提交：

- 新的 Agent Skill 或技能合集
- 更准确的安装方式、兼容性说明
- 失效链接修复
- 安全风险提示
- 你用书灵蒸馏出的顾问 Skill

提交前请阅读 [贡献指南](CONTRIBUTING.md)，也可以使用 [投稿模板](https://github.com/AnonymousLeeJJ/awesome-agent-skills-zh/issues/new?template=submit-skill.yml)。

## 🧾 收录原则

1. **真实存在**：必须有可访问的公开仓库或官方文档
2. **结构明确**：优先收录符合 SKILL.md / Agent Skills 规范的项目
3. **中文解读**：不是机翻简介，要说明它解决什么问题
4. **标注来源**：官方、社区、索引、原创必须分清
5. **不过度承诺**：收录不等于推荐生产使用，更不等于安全背书
6. **持续维护**：失效链接和更名仓库应定期修正

## 🙏 数据来源与致谢

首批条目参考并核验了以下来源：

- [anthropics/skills](https://github.com/anthropics/skills)
- [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)
- [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)
- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- [Sunnepah/awesome-agent-skills](https://github.com/Sunnepah/awesome-agent-skills)
- [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)
- [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)

## 🔗 我的其他项目

- 🎯 [Awesome AI Prompts](https://github.com/AnonymousLeeJJ/awesome-ai-prompts) — 48 条实战验证的中文 AI 提示词，即复制即用
- 🔌 [Free APIs 中文精选](https://github.com/AnonymousLeeJJ/free-apis-zh) — 真正可用的免费 API 大全，标注是否需 Key
- 🧭 [AI Tools 导航](https://github.com/AnonymousLeeJJ/ai-tools-nav) — 国内外好用的 AI 工具精选，标注免费情况
- 📄 [Awesome Resume 简历模板](https://github.com/AnonymousLeeJJ/awesome-resume-zh) — 免费中文简历模板，浏览器直接导出 PDF
- ⚡ [开发者速查表](https://github.com/AnonymousLeeJJ/cheatsheets-zh) — Git/Docker/Linux/Vim/正则/HTTP/SQL 高频命令随查随用
- ✨ [Pure CSS Effects](https://github.com/AnonymousLeeJJ/pure-css-effects) — 纯 CSS 特效库，实时预览一键复制
- 📘 [Awesome README 中文模板](https://github.com/AnonymousLeeJJ/awesome-readme-zh) — 让人 30 秒决定点 Star 的 README 模板与指南
- 📚 [书灵.skill](https://github.com/AnonymousLeeJJ/shuling-skill) — 把书、课程或资料蒸馏成可调用的 AI 顾问

## 📄 许可

- 数据、文案与文档：[CC BY 4.0](LICENSE) —— 可自由使用，但需署名
- 构建与校验脚本：[MIT](LICENSE-CODE)

---

<div align="center">

**如果这个项目帮你发现了好用的 Agent Skill，请点个 ⭐ Star！**

</div>
