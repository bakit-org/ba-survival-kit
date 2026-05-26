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
4. Follow the layout in templates/user-story-template.md.
5. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- user-stories.md (Sprint-ready backlog stories)

## Supporting files

- templates/user-story-template.md
