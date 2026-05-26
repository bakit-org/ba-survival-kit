---
name: field-rules-generator
description: Generate detailed display, behavior, and validation rules for each input field on a screen to guide front-end and back-end developers.
---

# Field Rules Generator

## Use when

- You have a fields list and need to specify validation conditions (regex, limits, dependencies).
- You need to document how fields behave on user input (formatting, auto-complete).

## Do not use when

- You want to draw flowcharts or model multi-page sequence diagrams.

## Inputs

- Fields list, screen layout.

## Instructions

1. For each field, define rules under three categories:
2.   1. Display Rules: visibility conditions, formatting, masks.
3.   2. Behavior Rules: triggers (onchange, onblur), autocalculations, dependencies.
4.   3. Validation Rules: required checks, length limits, pattern/regex, range limits.
5. Reference specific error codes [MSG-XXX] when validation fails.
6. Compile these rules into a clean markdown table or structured sections.
7. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- field-rules.md (Detailed field-level rules spec)

## Supporting files

- None
