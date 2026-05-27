---
name: ascii-flow-generator
description: Draft quick, text-based ASCII flowcharts mapping user journeys and logic blocks for quick note integration.
---

# ASCII Flow Generator

## Use when

- You want to add a quick flow diagram to meeting notes or text emails.
- You need a simple, lightweight flow chart without using graph visualization engines.

## Do not use when

- You are building official specs that require standardized UML sequence/activity diagrams.

## Inputs

- Workflow description, logic notes.

## Instructions

1. Create text-based boxes for steps, using brackets e.g. [ Step 1 ].
2. Connect steps using clear ASCII arrows (--> or |v|).
3. Map decision branches using simple text labels (Yes/No).
4. Keep indentation aligned and formatted in a monospaced code block.
5. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- ascii-flow.md (Text-based ASCII flowchart)

## Supporting files

- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
