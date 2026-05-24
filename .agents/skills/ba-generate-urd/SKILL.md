---
name: ba-generate-urd
description: Generate a BA-ready User Requirements Document (URD) draft from messy customer materials such as transcripts, meeting notes, rough requirements, or emails. Use when the user wants a user-centric view of needs and pain points.
---

# BA Generate URD

## Use when

- The source material focus is on user needs, user-centric problems, or tasks they want to perform.
- The user wants a quick first-pass draft mapping out user requirements before system specs.

## Do not use when

- The task focuses solely on technical specifications or database structures.
- The input lacks a clear description of user interaction or actor goals.

## Inputs

- Transcript, notes, raw requirements, emails, or intake briefs.
- Target user personas (optional).

## Instructions

1. Extract explicit user personas, goals, pain points, and needs from raw inputs.
2. Structure the draft focusing on user tasks and expected experiences.
3. Separate known facts from assumptions.
4. Put missing details under `Open Questions`.
5. List poorly covered user scenarios under `Source Gaps`.
6. Do not invent technical rules or system solutions; stay focused on user needs.

## Output

- URD draft
- Assumptions
- Open Questions
- Source Gaps

## Supporting files

- `shared/extraction-rules.md`
- `shared/writing-rules.md`
- `shared/ambiguity-rules.md`
- `shared/quality-checklist.md`
