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

This creates a symlink or copies the skills catalog directly into the local project’s `.agents/skills/` directory.

---

## 2. Global Installation

Global skills are loaded by Antigravity across **all** workspace directories on your machine. This is ideal if you want to use the BA Skills as your personal "survival kit" in any folder on your laptop.

### Run Global Install Script
Execute the global install script from the repository root:

```bash
chmod +x scripts/install-antigravity-global.sh
./scripts/install-antigravity-global.sh
```

This copies the skills catalog into `~/.gemini/antigravity/skills/`.

---

## 3. Verification

To verify that Antigravity is loading your skills:
1. Open Antigravity in your workspace.
2. Ask Antigravity to describe a skill (e.g., *"What is the ba-generate-srs skill?"*).
3. Antigravity should list the skill metadata and instructions successfully.
