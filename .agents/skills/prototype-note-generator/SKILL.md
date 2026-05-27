---
name: prototype-note-generator
description: Document user interaction pathways, navigation transitions, button links, and dynamic states between prototype screens.
---

# Prototype Note Generator

## Use when

- You want to specify how screens link together in a flow.
- You need to document transition effects, modals, and dynamic changes.

## Do not use when

- You are defining data validation checks on specific fields.

## Inputs

- Wireframe layout spec, user journey path.

## Instructions

1. List all screens in the prototype flow.
2. For each interactive element, define: Source Screen -> User Action -> Trigger -> Transition -> Target Screen.
3. Describe the behavior of modals, tooltips, and collapsing panels.
4. Document the system response for dynamic transitions (e.g. ajax loading, slide-in).
5. For Figma-backed prototypes, record the MCP frame or node reference for each screen.
6. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- prototype-notes.md (Interactive flow and navigation specifications)

## Supporting files

- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
