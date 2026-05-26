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
This script copies all directories under `skills/` directly to `.agents/skills/`.

### 2. Global System Sync
Use this option when you want to load these skills across any project directory opened in your Antigravity IDE.
```bash
./scripts/install-antigravity-global.sh
```
This script copies the skills directory to `~/.gemini/antigravity/skills/` on macOS.

## Verifying Deployment
Run the following script to check the structure and yaml frontmatter compliance of all skills:
```bash
./scripts/validate-skill-tree.sh
```
If a skill is missing its frontmatter metadata (`name:` or `description:`), the validation script will fail.
