# Runtime Compatibility Matrix

This document maps out the support and behavior of the BA skills catalog across different AI agent runtime platforms.

---

## 1. Compatibility Overview

| Skill Feature | Antigravity (Google DeepMind) | OpenAI Codex | Claude Code (Anthropic) |
| :--- | :--- | :--- | :--- |
| **Workspace Skills** | Native (`.agents/skills/`) | Native (via Custom Tools) | Native (`~/.claude/skills/` or local config) |
| **Routing Mechanism** | Implicit (Description-matching) | Function/Tool calling signature | System prompt description matching |
| **Execution Scripts** | Native (venv execution) | Sandboxed API runs | Native (bash/python execution) |
| **Supporting Files** | Supported (dynamic relative loads) | Supported (via inline retrieval) | Supported (file system access) |

---

## 2. Platform-Specific Routing Optimization

### Antigravity & Claude Code
*   Both platforms scan the user query against the catalog of short skill descriptions.
*   **Best Practice:** Keep the `description` keyword-rich and concise. Avoid conversational language inside the front-matter.

### OpenAI Codex
*   Codex maps skills to JSON Schemas for tool calling.
*   **Best Practice:** When bridging, auto-generate a JSON schema from the inputs and outputs defined in `SKILL.md`.

---

## 3. Adapters for Tool Execution

For deterministic scripts (`scripts/`):
*   **Antigravity:** Use local shell/python executions running under the designated virtual environment.
*   **Claude:** Runs directly in terminal via bash/python tools.
*   **Codex:** Wrap scripts as HTTP endpoints or serverless functions to call from the Codex tool environment.
