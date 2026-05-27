---
name: brief-to-structured-notes
description: Convert raw, messy, or unstructured project briefs into well-structured working notes outlining bối cảnh, nội dung chính, assumptions, open questions, and next steps.
---

# Brief to Structured Notes

## Use when

- You have a raw project brief, meeting recording text, or customer description.
- You want to quickly structure chaotic notes into a clean Markdown layout.

## Do not use when

- You want to generate detailed screen specifications (use screen-spec-from-wireframe instead).
- You want to generate test cases or user stories.

## Inputs

- Raw brief text or unstructured document path.

## Instructions

1. Parse the raw input text for project goals, scope, and key elements.
2. Organize the extracted information into sections: Context (Feature, Source Input, Goal), Main Points, Assumptions, Open Questions, Risks & Dependencies, and Next Steps.
3. Strictly follow the installed `markdown-output-template.md` supporting file listed below.
4. Highlight any missing details under Open Questions and mark uncertainties as Assumptions.
5. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- brief-summary.md (Structured summary of the brief)
- working-notes.md (Detailed notes including assumptions, questions, and next steps)

## Supporting files

- `.agents/ba-survival-kit/templates/markdown-output-template.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/templates/markdown-output-template.md` (global)
- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
