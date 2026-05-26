---
name: activity-flow-generator
description: Generate process activity flows using Mermaid flowchart syntax, documenting branching logic, actor decisions, and exception paths.
---

# Activity Flow Generator

## Use when

- You need to model a step-by-step business process flow visually.
- You want to map the system decision logic for a transaction or checkout flow.

## Do not use when

- You need to document message calls between distinct service APIs (use sequence-diagram-generator).

## Inputs

- Process narrative, business flow notes.

## Instructions

1. Identify the starting point, steps, decision diamonds (if/else), and endpoints.
2. Trace both the happy path and any exception/error branching paths.
3. Format using Mermaid graph TD or graph LR syntax.
4. Double-check that node labels are enclosed in double quotes if they contain special characters.
5. Include a textual description of the process flow steps beneath the Mermaid block.
6. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- activity-flow.md (Activity flowchart in Mermaid format)

## Supporting files

- None
