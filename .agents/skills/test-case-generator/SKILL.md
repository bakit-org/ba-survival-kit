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
4. Map every test case to one or more `AC-*` identifiers and reuse applicable `MSG-*` text exactly.
5. Align output format with the installed `test-case-template.md` supporting file listed below.
6. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- test-cases.md (Functional test cases matrix)

## Supporting files

- `.agents/ba-survival-kit/templates/test-case-template.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/templates/test-case-template.md` (global)
- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
