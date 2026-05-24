---
title: BA Extraction Rules
status: draft
updated: 2026-05-23
---

# BA Extraction Rules

These rules apply to all BA skills in this repo.

## Goal

Convert messy client materials into BA-ready drafts without hiding uncertainty.

## Source Priority

Use sources in this order:

1. Explicit statements in customer materials
2. Repeated signals across multiple materials
3. Conservative inference from context
4. Structured placeholders for missing information

Do not treat weak inference as fact.

## Required Output Buckets

Every generation skill must separate content into:

- `Facts`: Explicitly supported by source material
- `Assumptions`: Reasonable but unconfirmed statements needed to complete the draft
- `Open Questions`: Missing information that affects quality or correctness
- `Source Gaps`: Important areas the source material does not cover well

## Extraction Rules

1. Extract business goals before features.
2. Extract actors and stakeholders before workflows.
3. Preserve customer terminology unless it is clearly inconsistent.
4. Normalize messy wording into professional BA wording without changing intent.
5. Pull out constraints, dependencies, timelines, and risks whenever present.
6. Record edge cases only when the source mentions them or strongly implies them.
7. Mark contradictions instead of resolving them silently.

## Do Not Invent

Do not invent any of the following unless strongly supported by source material:

- Additional actors or roles
- Business rules
- Validation rules
- Integration details
- Security controls
- Approval flows
- Error messages
- KPIs, SLAs, or timelines

## Ambiguity Handling

If the source is incomplete:

- Keep the document structure
- Fill only safe sections
- Add `Assumption` labels where needed
- Add unresolved items under `Open Questions`

## Multi-Source Handling

When multiple files or notes are provided:

1. Merge overlapping facts
2. Preserve the more specific statement
3. Flag contradictions explicitly
4. Note which parts appear to come from legacy material

## Minimum Quality Bar

A draft is acceptable when:

- Core sections are populated
- Terminology is consistent
- Uncertainty is visible
- The reader can see what is known versus guessed
