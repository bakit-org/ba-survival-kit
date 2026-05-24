---
name: ba-generate-use-cases
description: Generate a set of structured system Use Cases from messy customer materials such as transcripts, meeting notes, rough requirements, or system briefs. Use when the user wants structured scenarios detailing interactions between actors and the system.
---

# BA Generate Use Cases

## Use when

- The source material describes interactions, actor tasks, and system responses.
- The user wants a detailed first-pass draft of use cases for QA or development reference.

## Do not use when

- The task is high-level business vision only.
- The input lacks clear actor-system interaction details.

## Inputs

- Transcript, notes, raw requirements, or intake briefs.
- Target system flowcharts (optional).

## Instructions

1. Identify explicit actors, system boundaries, triggers, and goals.
2. For each use case, structure: Pre-conditions, Post-conditions, Main Flow, Alternative Flows, and Exception Flows.
3. Separate known facts from assumptions.
4. Put missing details under `Open Questions`.
5. List poorly covered scenarios under `Source Gaps`.
6. Do not invent details; document only flows supported by the raw input.

## Output

- Use Cases draft document
- Assumptions
- Open Questions
- Source Gaps

## Supporting files

- `shared/extraction-rules.md`
- `shared/writing-rules.md`
- `shared/ambiguity-rules.md`
- `shared/quality-checklist.md`
