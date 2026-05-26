# Coding and Authoring Standards

This document establishes development rules for maintaining and writing new skills in this repository.

## 1. Skill File Structure
Every skill must reside in its own folder under `skills/` using a lowercase, kebab-case directory name. The primary entry point must be `SKILL.md`.

```text
skills/
└── kebab-case-skill-name/
    └── SKILL.md
```

## 2. SKILL.md Conventions
`SKILL.md` must begin with YAML frontmatter containing:
- `name`: exact matching kebab-case name of the folder.
- `description`: A 1-2 sentence description optimized for Antigravity's routing selector (containing relevant keywords like "Mermaid", "Gherkin", "wireframe").

## 3. Formatting
The body of `SKILL.md` should use the following standard headers:
- `# [Skill Title]`
- `## Use when`
- `## Do not use when`
- `## Inputs`
- `## Instructions`
- `## Output`
- `## Supporting files`

## 4. 200-Line Modularization Rule
Guidelines, templates, or instructions that exceed **200 lines** of code/content must be modularized and broken down into smaller files placed under the `shared/` folder. This limits token bloat in agent routing cycles.
(Note: This rule does not apply to course markdown handouts, script configs, or compiled documentation files).
