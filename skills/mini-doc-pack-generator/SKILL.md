---
name: mini-doc-pack-generator
description: Assemble and cross-reference multiple BA artifacts into a cohesive, consistent, and traceable Mini BA documentation package.
---

# Mini Doc Pack Generator

## Use when

- You have created multiple BA files and want to pack them for handoff.
- You need a master index file to coordinate all sprint deliverables.

## Do not use when

- You are creating a single file from scratch without other artifacts.

## Inputs

- Collection of drafted BA files (brief, wireframes, specs, diagrams, stories, test cases).

## Instructions

1. Validate that terms, error codes, and flows are consistent across all files.
2. Create a master index markdown document tracing connections between files.
3. Add high-level context, version history, and dependencies list.
4. Follow the guidelines in templates/mini-pack-structure.md.
5. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- mini-ba-pack.md (Master index and documentation package overview)

## Supporting files

- templates/mini-pack-structure.md
