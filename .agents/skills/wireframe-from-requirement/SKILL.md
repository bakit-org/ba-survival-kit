---
name: wireframe-from-requirement
description: Translate functional screen requirements into a structured, screen-by-screen layout specification ready for visual mockup drafting.
---

# Wireframe from Requirement

## Use when

- You want to convert text requirements into a screen structure description.
- You need to define what widgets and sections go onto a screen based on business rules.

## Do not use when

- You want to write standard Gherkin acceptance criteria.

## Inputs

- Functional requirements, feature scope.

## Instructions

1. Identify screens needed based on requirements (e.g., login, form, list, review).
2. For each screen, layout the header, body panels, sidebars, and footer.
3. Specify which fields go into each section and what type of control is used (textbox, dropdown).
4. Insert a clean layout mockup placeholder or structured design prompt block.
5. Format the output strictly following templates/wireframe-input-template.md.
6. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- wireframe-pack.md (Consolidated collection of screen structures and layouts)

## Supporting files

- templates/wireframe-input-template.md
