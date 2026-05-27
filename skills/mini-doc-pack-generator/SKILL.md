---
name: mini-doc-pack-generator
description: Compile multiple BA artifacts into one complete, consistent, and traceable Mini BA documentation package.
---

# Mini Doc Pack Generator

## Use when

- You have created multiple BA files and want to pack them for handoff.
- You need one complete handoff document containing all deliverable content.

## Do not use when

- You are creating a single file from scratch without other artifacts.

## Inputs

- Collection of drafted BA files (brief, wireframes, specs, diagrams, stories, test cases).

## Instructions

1. Validate that terms, error codes, and flows are consistent across all files.
2. Compile full content for brief, wireframe evidence, screen specification, diagrams, use case, stories/criteria, checklist, and test cases into one document.
3. Preserve stable IDs and explicit traces across `CHK-*`, `UC-*`, `US-*`, `AC-*`, `TC-*`, and `MSG-*`.
4. Add source context, version history, open questions, and dependencies.
5. Follow the installed `mini-pack-structure.md` and `artifact-quality-contract.md` supporting files listed below.
6. Run the installed validator and resolve reported errors.

## Output

- mini-ba-pack.md (Complete merged BA handoff document)

## Supporting files

- `.agents/ba-survival-kit/templates/mini-pack-structure.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/templates/mini-pack-structure.md` (global)
- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
