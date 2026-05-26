---
name: review-checklist-generator
description: Create a customized quality review checklist to verify correctness, logic, completeness, and consistency of BA documents.
---

# Review Checklist Generator

## Use when

- You want to audit a set of specifications before presenting them to stakeholders.
- You need a systematic way to verify that a document matches original inputs.

## Do not use when

- You want to write functional use cases.

## Inputs

- Drafted BA specifications, design rules.

## Instructions

1. Analyze the drafted specification and generate relevant audit checks.
2. Group items into sections: Scope matching, Logical consistency, Data/Field completeness, State/Message verification.
3. Format as interactive Markdown checklists (- [ ]).
4. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- review-checklist.md (Spec review checklist)

## Supporting files

- None
