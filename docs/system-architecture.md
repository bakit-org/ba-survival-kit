# System Architecture & Routing

This document details the internal routing mechanism that allows Antigravity IDE to execute workspace skills.

## 1. Skill Execution Pipeline
When a user inputs a query or prompt inside the IDE, the Antigravity agent follows a multi-phase lifecycle to match and execute the command:

```text
  [ User Prompt ] ──> [ Routing Router ] ──> [ Select SKILL.md ]
                             │
                             ▼
                    [ Read File Context ]
                             │
                             ▼
                    [ Execute Guidelines ] ──> [ Generate Markdown ]
```

1. **Routing and Matching:** The router reads the metadata fields (`name` and `description`) defined in the yaml headers of each `SKILL.md` file. It computes a semantic match based on the user's intent.
2. **Context Resolution:** Once selected, the agent parses the "Inputs" and "Supporting files" paths to load templates or checklists relative to the workspace.
3. **Execution Instructions:** The agent executes the step-by-step instructions in `SKILL.md` using the gathered inputs, outputting the structured Markdown file.

## 2. MCP Layer Integration
For visual wireframing workflows (Module 3 and 4), the agent accesses the **Figma MCP** tool layer. This allows the agent to read current mockup structures, place visual layers on Figma, and generate interactive wireframe annotations directly inside the editor.
