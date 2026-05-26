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
2. Check for usability flaws, logical flow issues, and missing elements (e.g. error states, back buttons).
3. Generate structured review comments categorized by severity: Critical, Major, Minor.
4. Offer constructive feedback on how to fix each identified issue.
5. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- wireframe-review-notes.md (Detailed feedback and logic check report)

## Supporting files

- None
