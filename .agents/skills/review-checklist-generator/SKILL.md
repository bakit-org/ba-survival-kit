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
4. Include checks for stable ID mapping and exact screen/message terminology.
5. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- review-checklist.md (Spec review checklist)

## Supporting files

- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
