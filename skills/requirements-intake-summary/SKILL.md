---
name: requirements-intake-summary
description: Analyze raw requirement intake briefs to extract business objectives, system constraints, out-of-scope items, and missing requirements.
---

# Requirements Intake Summary

## Use when

- You receive initial, messy requirements from client emails or intake briefs.
- You need to organize requirements and flag information gaps before the kickoff meeting.

## Do not use when

- You want to map out detailed interactive screens or UML flows.

## Inputs

- Intake brief, client notes, or raw request files.

## Instructions

1. Scan the intake document for high-level business goals and features.
2. Differentiate between in-scope requirements, out-of-scope requests, and technical constraints.
3. Identify information gaps, logical contradictions, or ambiguous requirements.
4. Generate a list of questions to ask stakeholders to clarify requirements.
5. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- requirements-intake-summary.md (High-level scoping and requirements summary)

## Supporting files

- None
