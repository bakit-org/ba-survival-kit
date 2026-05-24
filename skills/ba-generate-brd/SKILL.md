---
name: ba-generate-brd
description: Generate a BA-ready BRD draft from messy customer materials such as transcript, meeting notes, rough requirements, intake briefs, or legacy documents. Use when the user wants a fast first-draft business requirements document.
---

# BA Generate BRD

## Use when

- The user wants a BRD draft from raw or semi-structured material
- The source focuses on business goals, stakeholders, scope, and outcomes
- A normalized intake brief already exists or can be derived safely

## Do not use when

- The task is technical solution design
- The source is too thin to support a meaningful business document

## Inputs

- Transcript, notes, customer documents, or intake brief
- Optional business context or formatting preference

## Instructions

1. Extract explicit business goals, stakeholders, scope, and outcomes first.
2. Organize the draft as a business-facing document.
3. Preserve client terminology where useful.
4. Mark uncertain statements as `Assumption`.
5. Add unresolved or blocking items under `Open Questions`.
6. List major missing information under `Source Gaps`.
7. Keep implementation detail out unless it materially affects business scope or feasibility.

## Output

- BRD draft
- Assumptions
- Open Questions
- Source Gaps

## Supporting files

- `templates/brd.md`
- `shared/extraction-rules.md`
- `shared/writing-rules.md`
- `shared/ambiguity-rules.md`
- `shared/quality-checklist.md`
