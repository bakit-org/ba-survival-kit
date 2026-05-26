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
4. Specify visual or layout constraints (headers, sections, grids) following figma guidelines.
5. Verify the quality and compliance of the generated document by running the validation script: `python3 scripts/validate-document-quality.py --doc <output_file_name>` and resolve any reported errors.

## Output

- wireframe-request.md (Formal request package containing layout and field specifications)

## Supporting files

- shared/figma-layout-guidelines.md
