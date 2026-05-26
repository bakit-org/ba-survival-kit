---
name: screen-state-drafter
description: Document screen behavior and appearance across states like loading, empty, validation errors, success, and system failure.
---

# Screen State Drafter

## Use when

- You need to define how a screen behaves when there is no data, during loading, or on offline status.
- You want to detail error states and success notifications.

## Do not use when

- You are defining high-level use case narratives.

## Inputs

- Screen layout, basic functional spec.

## Instructions

1. Specify the UI components and text for: Default state, Loading state, Empty state, Error state, Success state, and Unavailable/Offline state.
2. Define the triggers that cause transitions between these states (e.g. data load complete, save button click, API failure).
3. Ensure that error states display the correct validation messages and codes.
4. Format using the standard screen-state-note-template.md structure.
5. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- screen-states.md (Detailed specifications for screen states and transitions)

## Supporting files

- templates/screen-state-note-template.md
