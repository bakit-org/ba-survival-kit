---
name: ba-generate-prd
description: Generate a BA-ready Product Requirements Document (PRD) draft from messy customer materials such as transcripts, meeting notes, rough requirements, or pitch decks. Use when the user wants a product-centric spec with vision, features, and success metrics.
---

# BA Generate PRD

## Use when

- The source material covers product vision, roadmap, primary features, and business metrics.
- The user wants a quick first-pass draft of product scope and feature definitions.

## Do not use when

- The task is functional detailed design (FRD/SRS).
- The input lacks a clear description of product features or product goals.

## Inputs

- Transcript, notes, raw requirements, pitch decks, or intake briefs.
- Target KPIs or release plans (optional).

## Instructions

1. Extract explicit product goals, feature definitions, release scope, and success metrics.
2. Structure the draft focusing on product value and feature high-level behaviors.
3. Separate known facts from assumptions.
4. Put missing details under `Open Questions`.
5. List poorly covered features under `Source Gaps`.
6. Do not invent details; describe features at a high functional level.

## Output

- PRD draft
- Assumptions
- Open Questions
- Source Gaps

## Supporting files

- `shared/extraction-rules.md`
- `shared/writing-rules.md`
- `shared/ambiguity-rules.md`
- `shared/quality-checklist.md`
