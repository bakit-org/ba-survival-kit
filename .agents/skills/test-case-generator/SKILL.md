---
name: test-case-generator
description: Generate functional test cases with steps, test data, and expected results directly from user stories and acceptance criteria.
---

# Test Case Generator

## Use when

- You need to write functional test scenarios for UAT or QA.
- You want to verify that all Gherkin acceptance criteria are covered by tests.

## Do not use when

- You want to write automated testing code or scripts.

## Inputs

- User stories, acceptance criteria, screen spec.

## Instructions

1. Review user stories and Gherkin acceptance criteria.
2. Generate test cases specifying: Test ID, Scenario, Preconditions, Steps, Test Data, Expected Result, and Priority.
3. Ensure coverage of both happy paths (positive) and error flows (negative/validation).
4. Align output format with templates/test-case-template.md.
5. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- test-cases.md (Functional test cases matrix)

## Supporting files

- templates/test-case-template.md
