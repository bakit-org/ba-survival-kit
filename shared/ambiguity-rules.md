---
title: BA Ambiguity Rules
status: draft
updated: 2026-05-23
---

# BA Ambiguity Rules

This file defines how skills should behave when the source material is weak, conflicting, or incomplete.

## Core Rule

Prefer visible uncertainty over confident invention.

## Ambiguity Types

### Missing

The source does not provide enough information.

Action:

- Leave the section partially complete
- Add an `Open Question`
- Add a `Source Gap` note if the missing area is broad

### Conflicting

Two sources say different things.

Action:

- Preserve the conflict explicitly
- Do not choose a winner unless one source is clearly newer or more authoritative
- Add the conflict to `Open Questions`

### Weakly Implied

The source suggests something but does not say it clearly.

Action:

- Use `Assumption`
- Keep wording conservative

### Out of Scope

The source includes material that is unrelated to the requested document.

Action:

- Exclude it from the main draft
- Mention it only if it affects scope or downstream decisions

## Critical Unknowns

The following unknowns should almost always be surfaced:

- Primary business objective
- Main user or actor groups
- Scope boundaries
- Approval or decision ownership
- Required outputs or outcomes
- External dependencies
- Compliance or regulatory constraints

## Escalation Rule

If a missing detail would materially change the structure of the document, add it to `Open Questions` rather than guessing.

## Safe Inference Rule

Inference is acceptable only when:

- it helps organize known content
- it does not add new business behavior
- it can be described without sounding definitive

## Examples

- Safe: "Assumption: Managers review submissions before approval."
- Unsafe: "The system sends SMS OTP to all users during every approval."
