---
name: ba-generate-srs
description: Generate a BA-ready SRS draft from messy customer materials such as transcript, meeting notes, rough requirements, intake briefs, or legacy documents. Use when the user wants a fast first-draft software requirements specification from unstructured input.
---

# BA Generate SRS

## Use when

- The input is messy or semi-structured
- The user wants a quick first-draft SRS
- The source contains enough functional behavior to structure requirements safely

## Do not use when

- The user wants implementation code
- The source is too thin to support meaningful requirements

## Inputs

- Transcript, notes, raw requirements, intake brief, or existing documents
- Optional preferred structure or domain constraints

## Instructions

1. Extract explicit functional and non-functional requirements from the source.
2. Identify all user interfaces and screens mentioned or implied in the requirements.
3. Generate a central `srs-screens/message-registry.md` file following the layout in `templates/message-registry.md`. Extract all validation warnings and notification copy into this single file, assigned to unique codes (e.g. `[MSG-001]`).
4. For each screen identified, generate a separate screen specification file in the `srs-screens/` directory following `templates/srs-screen-figma.md`.
5. Under each screen's "UI Component Details", break down every field or control into explicit **Display Rules**, **Behaviour Rules**, and **Validation Rules** (referencing codes from the central registry, e.g. `[MSG-001]`).
6. Within each screen specification file, write a dedicated, detailed Figma Make Prompt block mapping to the layout and styling guidelines.
7. In the main `srs.md` draft, document high-level requirements and link the screen files.
8. If requested, compile all screens and registry files into a single master document by running `scripts/merge-srs.sh`.
9. Mark uncertain content as `Assumption`.
10. Put missing details under `Open Questions` and `Source Gaps`.
11. Do not invent integrations, business rules, validations, or security controls unless strongly supported by source material.

## Output

- `srs.md` (Main SRS document containing links to screens)
- `srs-screens/` (Folder containing individual `.md` screen files with Figma Make prompts)
- `srs-screens/message-registry.md` (Centralized index of all system message copy and error codes)
- Assumptions
- Open Questions
- Source Gaps

## Supporting files

- `templates/srs.md`
- `templates/srs-screen-figma.md`
- `templates/message-registry.md`
- `shared/extraction-rules.md`
- `shared/writing-rules.md`
- `shared/ambiguity-rules.md`
- `shared/quality-checklist.md`
- `scripts/merge-srs.sh`


