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
4. Use the exact layout in templates/ac-template.md.
5. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- acceptance-criteria.md (Testable Gherkin-style criteria)

## Supporting files

- templates/ac-template.md
