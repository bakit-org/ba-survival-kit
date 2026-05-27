---
name: sequence-diagram-generator
description: Generate a Mermaid sequence diagram representing chronological interactions, requests, and responses between actors and system components.
---

# Sequence Diagram Generator

## Use when

- You want to model API calls, page redirects, or backend interactions chronologically.
- You need to clarify system integrations and message exchanges between systems.

## Do not use when

- You are sketching visual wireframes or page grids.

## Inputs

- Integration flow, API requirements, or system interaction notes.

## Instructions

1. Identify all participating actors and systems (User, UI, API Gateway, Payment Portal, DB).
2. Write the message exchange chronologically from top to bottom.
3. Use Mermaid sequence diagram syntax (e.g. `sequenceDiagram`, `Actor->>System: Msg`).
4. Incorporate logic checks (alt/else) for success, error, and timeout flows.
5. Ensure all Mermaid syntax rules are followed, avoiding illegal characters in tags.
6. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- sequence-diagram.md (Sequence diagram in Mermaid format)

## Supporting files

- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
