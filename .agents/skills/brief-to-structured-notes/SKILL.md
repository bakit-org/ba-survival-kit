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
3. Strictly follow the structure in templates/markdown-output-template.md.
4. Highlight any missing details under Open Questions and mark uncertainties as Assumptions.
5. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- brief-summary.md (Structured summary of the brief)
- working-notes.md (Detailed notes including assumptions, questions, and next steps)

## Supporting files

- templates/markdown-output-template.md
