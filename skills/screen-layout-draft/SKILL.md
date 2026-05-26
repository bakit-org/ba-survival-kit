---
name: screen-layout-draft
description: Draft a text or block-based wireframe layout representation of a screen, organizing key content sections and buttons.
---

# Screen Layout Draft

## Use when

- You need to quickly sketch a screen layout in a text-based format.
- You want to outline the visual structure of a screen before detail specification.

## Do not use when

- You need to write validation messages or error code rules.

## Inputs

- Screen brief, wireframe request.

## Instructions

1. Determine the grid layout (e.g., single column form, split view, card grid).
2. Map sections: navigation, header, form container, actions area, footer.
3. Draft block or ASCII layouts showing where each input field and button sits.
4. Highlight focus areas and user pathways through the screen.
5. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- screen-layout-draft.md (Visual block outline of the screen)

## Supporting files

- None
