---
name: use-case-generator
description: Create detailed Use Cases defining actors, preconditions, postconditions, happy path, alternative paths, and exception flows.
---

# Use Case Generator

## Use when

- You need to document standard functional scenarios for developers and testers.
- You want to specify detailed system behavior from an actor-system interaction standpoint.

## Do not use when

- You are writing code or test scripts.

## Inputs

- Business flow, functional rules.

## Instructions

1. Establish the Use Case ID, name, primary actor, and goal.
2. Define preconditions (what must be true before starting) and postconditions (state after success).
3. Write the Main Success Scenario (Happy Path) as numbered actor and system steps.
4. Document Alternative Flows (e.g. promo code applied) and Exception Flows (e.g. transaction fails) referencing main flow steps.
5. Include a Mermaid process flow or sequence diagram and link related Screen IDs and message IDs.
6. Align output format with the installed `use-case-template.md` supporting file listed below.
7. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- use-cases.md (Detailed use case documentation)

## Supporting files

- `.agents/ba-survival-kit/templates/use-case-template.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/templates/use-case-template.md` (global)
- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
