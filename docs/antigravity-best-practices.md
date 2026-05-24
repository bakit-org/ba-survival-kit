# Antigravity Skill Best Practices: Routing and Context Optimization

This guide documents the technical mechanics of how **Antigravity** executes workspace skills and how to design skills for optimal performance.

---

## 1. Description-Driven Routing

Antigravity uses the `description` header in `SKILL.md` to route user queries. 

*   **How it works:** When a user enters a query, Antigravity reads all available skill descriptions. It selects the skill that matches the intent best and imports its full `SKILL.md`.
*   **The Best Practice:** Write descriptions like a matching pattern, packed with nouns (the artifacts generated) and context trigger keywords.

### Good vs Bad Descriptions

*   ❌ **Bad:** `name: ba-generate-brd; description: A skill that lets you generate a Business Requirements Document from text.` (Too generic, weak keywords).
*   ✅ **Good:** `name: ba-generate-brd; description: Generate a BA-ready BRD draft from messy customer materials such as transcripts, meeting notes, rough requirements, or legacy specifications. Use when the user wants a fast business requirements document.` (Specific, matches typical raw inputs).

---

## 2. Progressive Disclosure (Context Budgeting)

Antigravity operates within strict token limitations. Bloating the agent's startup context causes failure or slow response.

*   **The Principle:** Do not put raw templates, massive styling guides, or exhaustive checklists directly in `SKILL.md`.
*   **The Practice:** Put them in `templates/` or `shared/` files, and reference them under the `## Supporting files` section in `SKILL.md`. Antigravity will only read these large files when the skill is actually selected for execution.

---

## 3. Tool-Enabled Skills

Whenever deterministic checking is required, combine instruction-based prompts with execution scripts under `scripts/`.
*   Scripts should run inside the workspace's designated virtual environment (`.venv`).
*   Example: Running structural tests or validating generated document formats before presenting them to the user.
