---
name: ba-parse-intake
description: Optional helper to parse highly chaotic, unstructured customer materials (large transcripts, disorganized notes) into a normalized intake brief. Use only when raw inputs are too complex or large to feed directly into generator skills.
---

# BA Parse Intake (Optional Helper)

## Use when

- The input materials are extremely large, unstructured, or disorganized.
- You want to reduce context size or summarize key points before running main generators.
- Multiple separate raw documents need to be normalized into a single concise brief.

## Do not use when

- The user already has a clean structured BA brief
- The task is code generation or implementation

## Inputs

- Transcript, notes, screenshots, raw requirements, or existing customer documents
- Optional domain context

## Instructions

1. Read the provided materials and extract the core request.
2. Identify business goals, users, scope, processes, constraints, and dependencies.
3. Separate known facts from assumptions.
4. Surface ambiguity under `Open Questions`.
5. Note major missing areas under `Source Gaps`.
6. Produce the result using `templates/intake-brief.md`.
7. Preserve customer terminology when it is clear and consistent.

## Output

- Structured intake brief
- Facts
- Assumptions
- Open Questions
- Source Gaps

## Supporting files

- `templates/intake-brief.md`
- `shared/extraction-rules.md`
- `shared/writing-rules.md`
- `shared/ambiguity-rules.md`
- `shared/quality-checklist.md`
