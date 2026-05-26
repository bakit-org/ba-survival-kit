---
name: screen-spec-from-wireframe
description: Deconstruct a screen wireframe or layout specification into a comprehensive BA screen description detailing user actions, fields list, display, behavior, and validation rules.
---

# Screen Spec from Wireframe

## Use when

- You have a stable wireframe and want to write the official developer-ready screen spec.
- You need to specify validation messages, screen states, and interaction behavior for a screen.

## Do not use when

- You want to create high-level business case definitions (use requirements-intake-summary).

## Inputs

- Wireframe specification, screen layout description.

## Instructions

1. Extract and define general screen information (ID, name, purpose, flow).
2. Table 1: User Actions (Action, Trigger, Result).
3. Table 2: Fields List (Field, Display Type, Required status, Default value, Notes).
4. Document specific Display Rules, Behavior Rules, and Validation Rules.
5. Map screen states (Default, Error, Success, Unavailable).
6. Record error and system messages, assigning them unique IDs (e.g., [MSG-001]).
7. Follow templates/screen-description-template.md exactly.
8. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- screen-description.md (Official BA screen specification document)

## Supporting files

- templates/screen-description-template.md
