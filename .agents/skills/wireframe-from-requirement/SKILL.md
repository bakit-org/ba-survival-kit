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
5. Format the output strictly following the installed `wireframe-input-template.md` supporting file listed below.
6. Preserve Screen IDs for use in the Figma MCP handoff and downstream specifications.
7. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- wireframe-pack.md (Consolidated collection of screen structures and layouts)

## Supporting files

- `.agents/ba-survival-kit/templates/wireframe-input-template.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/templates/wireframe-input-template.md` (global)
- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
