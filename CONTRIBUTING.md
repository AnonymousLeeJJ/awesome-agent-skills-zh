# 贡献指南

感谢你为 Awesome Agent Skills 中文导航贡献内容。

## 可以贡献什么？

- 新的 Agent Skill、Skill 合集或规范资源
- 失效链接与仓库更名修复
- 更准确的安装方式、兼容性、许可证说明
- 中文描述优化
- 安全风险提示
- 使用 [书灵.skill](https://github.com/AnonymousLeeJJ/shuling-skill) 生成的原创顾问

## 收录标准

1. **公开可访问**：必须提供公开仓库、官方文档或演示地址
2. **真实可用**：不收录纯概念、空仓库或无法验证的项目
3. **结构清晰**：优先收录包含 `SKILL.md` 的技能
4. **描述具体**：说明它解决什么问题，避免“最强”“必备”等空泛宣传
5. **来源透明**：官方、社区、索引、原创必须明确标注
6. **安全提示**：包含脚本、网络请求或高权限需求的 Skill 必须主动说明

## 如何提交

### 方式一：Issue 投稿

使用 [投稿模板](https://github.com/AnonymousLeeJJ/awesome-agent-skills-zh/issues/new?template=submit-skill.yml)。

### 方式二：Pull Request

1. Fork 本仓库
2. 修改 `skills.json`
3. 运行：

```bash
python scripts/validate.py
python build_site.py
```

4. 提交 PR，并说明你验证过哪些信息

## 字段规范

- `source` 只能使用：`official`、`community`、`index`、`original`
- `type` 只能使用：`skill`、`collection`、`framework`、`guide`、`index`
- `category` 必须使用 `skills.json` 中已定义的分类
- `url` 必须使用 HTTPS
- `featured` 由维护者决定，投稿时请默认填 `false`

## 安全边界

收录不代表安全审计。请避免提交：

- 要求用户提供密钥但没有说明用途的 Skill
- 下载后执行远程脚本的 Skill
- 包含混淆代码或不明二进制的 Skill
- 过度申请文件、终端、网络权限的 Skill

发现安全风险时，请优先通过 Issue 说明，不要在公开评论中披露可被直接利用的细节。
