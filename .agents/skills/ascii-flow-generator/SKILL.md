---
name: ascii-flow-generator
description: Draft quick, text-based ASCII flowcharts mapping user journeys and logic blocks for quick note integration.
---

# ASCII Flow Generator

## Use when

- You want to add a quick flow diagram to meeting notes or text emails.
- You need a simple, lightweight flow chart without using graph visualization engines.

## Do not use when

- You are building official specs that require standardized UML sequence/activity diagrams.

## Inputs

- Workflow description, logic notes.

## Instructions

1. Create text-based boxes for steps, using brackets e.g. [ Step 1 ].
2. Connect steps using clear ASCII arrows (--> or |v|).
3. Map decision branches using simple text labels (Yes/No).
4. Keep indentation aligned and formatted in a monospaced code block.
5. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- ascii-flow.md (Text-based ASCII flowchart)

## Supporting files

- None
