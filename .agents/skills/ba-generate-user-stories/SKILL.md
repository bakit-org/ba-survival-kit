---
name: ba-generate-user-stories
description: Generate BA-ready user stories and acceptance criteria from messy customer materials such as transcript, meeting notes, rough requirements, intake briefs, or existing specs. Use when the user wants quick agile-ready story drafts from unstructured input.
---

# BA Generate User Stories

## Use when

- The user wants user stories from raw requirements or customer materials
- The output should be ready for BA review before backlog grooming
- A fast first-pass of acceptance criteria is needed

## Do not use when

- The task is business-case writing only
- The source lacks enough user behavior or workflow detail

## Inputs

- Transcript, notes, intake brief, rough requirements, or existing specs
- Optional persona or priority hints

## Instructions

1. Identify actors, goals, and business value from the source.
2. Write stories in the form `As a / I want / so that` when appropriate.
3. Keep each story focused on one intent.
4. Add acceptance criteria only when the source supports them or they can be stated conservatively.
5. Mark uncertain story details as `Assumption`.
6. Put missing behavior, edge cases, and unresolved details under `Open Questions`.
7. Avoid inventing technical implementation tasks or hidden business rules.

## Output

- User story draft set
- Acceptance criteria draft
- Assumptions
- Open Questions
- Source Gaps

## Supporting files

- `templates/user-stories.md`
- `shared/extraction-rules.md`
- `shared/writing-rules.md`
- `shared/ambiguity-rules.md`
- `shared/quality-checklist.md`
