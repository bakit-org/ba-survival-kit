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
5. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- prototype-notes.md (Interactive flow and navigation specifications)

## Supporting files

- None
