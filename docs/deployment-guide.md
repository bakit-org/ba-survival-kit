# Deployment and Setup Guide

This guide describes how to install and refresh the skills pack for Antigravity IDE.

## Prerequisites
- Antigravity IDE installed on your host system.
- Basic terminal utility access (`zsh` or `bash`).

## Installation Options

### 1. Workspace Level Sync
Use this option when you only want the skills to be active for the current repository workspace.
```bash
./scripts/install-antigravity-workspace.sh
```
This script copies skills to `.agents/skills/` and their runtime dependencies to `.agents/ba-survival-kit/`.

### 2. Global System Sync
Use this option when you want to load these skills across any project directory opened in your Antigravity IDE.
```bash
./scripts/install-antigravity-global.sh
```
This script copies skills to `~/.gemini/antigravity/skills/` and dependencies to `~/.gemini/antigravity/ba-survival-kit/`.

## Verifying Deployment
Run the following script to check the structure and yaml frontmatter compliance of all skills:
```bash
./scripts/validate-skill-tree.sh
```
If a skill is missing its frontmatter metadata (`name:` or `description:`), the validation script will fail.

After installation, verify the runtime payload:
```bash
test -f .agents/ba-survival-kit/scripts/validate-document-quality.py
test -d .agents/ba-survival-kit/templates
test -d .agents/ba-survival-kit/shared
```
