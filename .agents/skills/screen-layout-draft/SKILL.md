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
5. Retain the stable Screen ID and state labels used by the originating request.
6. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- screen-layout-draft.md (Visual block outline of the screen)

## Supporting files

- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
