# Contributing to Claude Skillforge

Contributions are welcome. This repo is a library of production-tested Claude Skills, not a collection of demos.

## Adding a new skill

1. Fork the repo
2. Create a folder under the appropriate category (core, data-engineering, writing, career)
3. Include a `SKILL.md` with YAML frontmatter (`name` and `description` fields)
4. The skill should solve one specific problem well
5. Test the skill in at least 3 different scenarios before submitting
6. Submit a pull request with a brief description of what the skill does and how it was tested

## Skill quality bar

- The skill must be usable as-is, not a template or placeholder
- Description must be specific enough for Claude's skill router to trigger correctly
- Instructions must be concise (under 5K tokens for most skills)
- No hardcoded secrets, API keys, or personal data in skill files

## Modifying existing skills

- Open an issue first to discuss the change
- Keep changes focused: one improvement per PR
- Do not change skill names without updating the README skill table

## Reporting issues

- Use GitHub Issues
- Include the skill name, what you expected, and what happened
- Include Claude's response if relevant (redact any personal information)
