# Awesome Agent Skills Chinese Directory

A curated Chinese directory of real, publicly available **Agent Skills**, skill collections, and specification resources.

- Chinese explanations for developers
- Category and source filters
- Installation commands where available
- License and compatibility labels
- Clear safety warnings for script-bearing skills

## Website

https://anonymousleejj.github.io/awesome-agent-skills-zh/

## What is an Agent Skill?

An Agent Skill is a portable folder of instructions, references, and optional scripts that teaches an AI agent how to perform a specialized task. The core file is usually `SKILL.md`.

This repository curates:

- Official Anthropic skills
- Engineering, design, document, and research skills
- Community collections and indexes
- Original skills built with [shuling-skill](https://github.com/AnonymousLeeJJ/shuling-skill)

## Featured Entries

- [Anthropic Skills](https://github.com/anthropics/skills)
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)
- [Google Stitch Skills](https://github.com/google-labs-code/stitch-skills)
- [Agent Skills by Addy Osmani](https://github.com/addyosmani/agent-skills)
- [Superpowers](https://github.com/obra/superpowers)
- [Shuling Skill](https://github.com/AnonymousLeeJJ/shuling-skill)

## Data Format

All entries live in `skills.json` and are validated by `scripts/validate.py`.

```bash
python scripts/validate.py
python build_site.py
```

## Safety

Skills may include scripts that run locally. Read `SKILL.md` and all scripts before installing. Inclusion in this directory means the public link was checked; it is not a security audit or an official endorsement.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Chinese is the primary language, but bilingual submissions are welcome.

## License

- Data and documentation: [CC BY 4.0](LICENSE)
- Build and validation scripts: [MIT](LICENSE-CODE)
