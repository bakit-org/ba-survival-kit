---
name: ba-generate-raci
description: Generate RACI matrices and Mermaid process workflow diagrams from messy customer materials such as transcripts, meeting notes, process descriptions, or project plans. Use to clarify roles, responsibilities, and task sequences.
---

# BA Generate RACI and Workflows

## Use when

- The input describes multiple actors, processes, tasks, or role allocations.
- The user wants a quick first-pass mapping of roles (RACI) or task flows (Mermaid flowchart) to resolve process ambiguity.

## Do not use when

- The task is software feature specification only (no human workflow involved).
- The input does not describe any human processes or roles.

## Inputs

- Transcript, notes, raw requirements, or intake briefs.
- Existing role lists or task lists (optional).

## Instructions

1. Identify all roles and key process tasks described in the raw inputs.
2. Construct a RACI matrix mapping tasks to roles: Responsible (R), Accountable (A), Consulted (C), Informed (I).
3. Generate a clean Mermaid flowchart diagram visualizing the sequence of tasks, branching conditions, and handoffs.
4. Separate known role assignments from assumptions.
5. Put missing roles, tasks, or sequence rules under `Open Questions`.
6. List poorly covered processes under `Source Gaps`.

## Output

- RACI Matrix table
- Mermaid workflow diagram code block
- Assumptions
- Open Questions
- Source Gaps

## Supporting files

- `shared/extraction-rules.md`
- `shared/writing-rules.md`
- `shared/ambiguity-rules.md`
- `shared/quality-checklist.md`
