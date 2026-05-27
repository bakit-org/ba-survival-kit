---
name: wireframe-request-prep
description: Prepare a comprehensive wireframe request brief detailing screen purpose, data fields, user actions, and constraints for designers or Figma MCP.
---

# Wireframe Request Prep

## Use when

- You need to communicate screen requirements clearly to UI designers.
- You want to build a solid input brief for automated wireframe generation tools.

## Do not use when

- You are writing test scenarios or backend system logic.

## Inputs

- Functional requirements, screen brief, or feature notes.

## Instructions

1. Define the target screen name, unique screen ID, and core business purpose.
2. Identify all user actions (buttons, links, triggers) that the user can perform.
3. List all information elements and input fields that must be displayed.
4. Specify visual or layout constraints (headers, sections, grids) following Figma MCP handoff guidelines.
5. Include required states and exact labels that the Figma MCP draft must preserve.
6. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- wireframe-request.md (Formal request package containing layout and field specifications)

## Supporting files

- `.agents/ba-survival-kit/shared/figma-layout-guidelines.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/figma-layout-guidelines.md` (global)
- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
