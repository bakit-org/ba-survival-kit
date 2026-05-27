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
6. Record error and system messages with stable IDs (for example, `MSG-ERR-01`).
7. Follow the installed `screen-description-template.md` supporting file listed below exactly.
8. Map screen actions to related use-case steps where available.
9. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- screen-description.md (Official BA screen specification document)

## Supporting files

- `.agents/ba-survival-kit/templates/screen-description-template.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/templates/screen-description-template.md` (global)
- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
