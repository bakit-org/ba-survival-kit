---
name: ba-generate-frd
description: Generate a BA-ready Functional Requirements Document (FRD) draft from messy customer materials such as transcripts, meeting notes, rough requirements, or system designs. Use when the user wants a detailed functional description of system behavior.
---

# BA Generate FRD

## Use when

- The source material details functional flows, logic, validations, or system actions.
- The user wants a detailed first-pass draft of functional rules before implementation.

## Do not use when

- The task is high-level business vision only.
- The input lacks a clear description of system logic or inputs/outputs.

## Inputs

- Transcript, notes, raw requirements, or intake briefs.
- Target system flowcharts or database structures (optional).

## Instructions

1. Extract explicit functional processes, validations, rules, and system boundaries.
2. Structure the draft focusing on functional flows and data validation.
3. Separate known facts from assumptions.
4. Put missing details under `Open Questions`.
5. List poorly covered functional logic under `Source Gaps`.
6. Do not invent integrations, security controls, or rules; describe only functional details.

## Output

- FRD draft
- Assumptions
- Open Questions
- Source Gaps

## Supporting files

- `shared/extraction-rules.md`
- `shared/writing-rules.md`
- `shared/ambiguity-rules.md`
- `shared/quality-checklist.md`
