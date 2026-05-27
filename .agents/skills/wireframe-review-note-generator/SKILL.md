---
name: wireframe-review-note-generator
description: Review draft wireframes against original requirements to generate feedback notes, highlighting layout gaps, logic flaws, and missing controls.
---

# Wireframe Review Note Generator

## Use when

- You have a drafted wireframe and want to check if it covers all requirements.
- You need to document issues, missing fields, or navigation flaws in a design review.

## Do not use when

- You are generating the layout design from scratch.

## Inputs

- Original screen requirements, draft wireframe (description, layout, or screenshot).

## Instructions

1. Compare the fields, layout, and actions in the wireframe against the original requirements.
2. Record the Figma MCP frame or node reference and check for missing elements (e.g. error states, back buttons).
3. Generate structured review comments categorized by severity: Critical, Major, Minor.
4. Offer constructive feedback on how to fix each identified issue.
5. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- wireframe-review-notes.md (Detailed feedback and logic check report)

## Supporting files

- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
