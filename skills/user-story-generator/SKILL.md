---
name: user-story-generator
description: Draft agile-ready User Stories using the standard 'As a..., I want..., So that...' template and map them to priorities.
---

# User Story Generator

## Use when

- You are preparing stories for the product backlog.
- You want to partition a large requirement (epic) into smaller, user-centered increments.

## Do not use when

- You need detailed validation scripts or data schemas.

## Inputs

- Functional requirements, intake brief, or feature scope.

## Instructions

1. Write stories following: 'As a [role], I want to [action], so that [benefit].'
2. Include Story ID, Priority (High/Medium/Low), and Related Use Cases.
3. Ensure stories follow the INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable).
4. Assign stable `US-*` identifiers and link related `UC-*` and `AC-*` identifiers.
5. Follow the installed `user-story-template.md` supporting file listed below.
6. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- user-stories.md (Sprint-ready backlog stories)

## Supporting files

- `.agents/ba-survival-kit/templates/user-story-template.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/templates/user-story-template.md` (global)
- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
