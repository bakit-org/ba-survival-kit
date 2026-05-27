---
name: acceptance-criteria-generator
description: Generate detailed, testable Acceptance Criteria using the Gherkin format (Given-When-Then) for user stories.
---

# Acceptance Criteria Generator

## Use when

- You have user stories and need to define clear boundaries of done.
- You want to establish criteria that QA and dev can use for testing verification.

## Do not use when

- You are writing high-level business goals or roadmaps.

## Inputs

- User stories, screen rules.

## Instructions

1. Review the user story and map out its conditions of acceptance.
2. Structure criteria using: 'Given [context], When [action], Then [outcome].'
3. Cover the primary success scenario, at least one alternate path, and failure/validation cases.
4. Use the exact layout in the installed `ac-template.md` supporting file listed below.
5. Assign stable `AC-*` identifiers, relate each criterion to its `US-*`, and preserve any `MSG-*` text used in validation outcomes.
6. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- acceptance-criteria.md (Testable Gherkin-style criteria)

## Supporting files

- `.agents/ba-survival-kit/templates/ac-template.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/templates/ac-template.md` (global)
- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
