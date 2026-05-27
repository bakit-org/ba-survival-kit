# Installing BA-skills in Antigravity

This guide explains how to install the generator-first BA skills library into your Antigravity environment.

---

## 1. Local Workspace Installation

Workspace-level skills are only loaded when Antigravity is opened within this specific project directory. This is the recommended choice for development or custom project extensions.

### Run Workspace Install Script
Execute the workspace install script from the repository root:

```bash
chmod +x scripts/install-antigravity-workspace.sh
./scripts/install-antigravity-workspace.sh
```

This copies the catalog into `.agents/skills/` and installs required templates, shared rules, and validator scripts under `.agents/ba-survival-kit/`.

---

## 2. Global Installation

Global skills are loaded by Antigravity across **all** workspace directories on your machine. This is ideal if you want to use the BA Skills as your personal "survival kit" in any folder on your laptop.

### Run Global Install Script
Execute the global install script from the repository root:

```bash
chmod +x scripts/install-antigravity-global.sh
./scripts/install-antigravity-global.sh
```

This copies skills into `~/.gemini/antigravity/skills/` and runtime dependencies into `~/.gemini/antigravity/ba-survival-kit/`.

---

## 3. Verification

To verify that Antigravity is loading your skills:
1. Open Antigravity in your workspace.
2. Ask Antigravity to describe a skill (e.g., *"What is the wireframe-request-prep skill?"*).
3. Antigravity should list the skill metadata and instructions successfully.
4. Check that the installed `ba-survival-kit` runtime directory contains `templates/`, `shared/`, and `scripts/validate-document-quality.py`.
