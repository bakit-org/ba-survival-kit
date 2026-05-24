# Antigravity Skill Authoring Guide

This guide establishes the folder and file conventions for authoring skills targeting the **Antigravity** workspace environment.

---

## 1. Directory Structure

Every skill must be packaged inside a single folder representing its unique skill name (kebab-case).

```text
skills/
└── ba-generate-example/          # Unique skill name
    ├── SKILL.md                  # Main entry point (Required)
    ├── scripts/                  # Deterministic code (Optional)
    │   └── validate-input.py
    └── resources/                # Large templates or rule docs (Optional)
        └── example-template.md
```

---

## 2. SKILL.md Skeleton

`SKILL.md` must remain lightweight (thin) to keep the routing lookup efficient. It must use the following standard sections:

```markdown
---
name: ba-generate-example
description: [Routing-optimized description (1-2 sentences). Maximize keyword signal.]
---

# BA Generate Example

## Use when

- [Trigger condition 1]
- [Trigger condition 2]

## Do not use when

- [Non-trigger condition 1]

## Inputs

- [Input file or details required]

## Instructions

1. [Instruction step 1]
2. [Instruction step 2]

## Output

- [Output file names or structure]

## Supporting files

- [Paths to templates/rules files relative to repo root]
```

---

## 3. Modularization Rule (200-Line Limit)

If any guideline or configuration file exceeds **200 lines**, it must be split into multiple smaller, focused markdown files under the `shared/` folder. This aligns with project rules and minimizes prompt token bloat during agent execution.
