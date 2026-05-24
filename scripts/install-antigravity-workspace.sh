#!/bin/bash
# install-antigravity-workspace.sh
# Syncs skills/ to the active workspace .agents/skills/ folder for Antigravity

set -e

WORKSPACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${WORKSPACE_DIR}/.agents/skills"

echo "=== Installing Antigravity Workspace Skills ==="
echo "Source: ${WORKSPACE_DIR}/skills"
echo "Target: ${TARGET_DIR}"

# Create target directory if it doesn't exist
mkdir -p "${TARGET_DIR}"

# Sync folders under skills/ into .agents/skills/
if [ -d "${WORKSPACE_DIR}/skills" ]; then
    for skill_path in "${WORKSPACE_DIR}/skills"/*; do
        if [ -d "${skill_path}" ]; then
            skill_name=$(basename "${skill_path}")
            echo "Installing workspace skill: ${skill_name}..."
            
            # Copy skill directory cleanly
            rm -rf "${TARGET_DIR}/${skill_name}"
            cp -R "${skill_path}" "${TARGET_DIR}/"
        fi
    done
    echo "Sync complete!"
else
    echo "Error: skills/ directory not found in workspace!"
    exit 1
fi

echo "=== Installation Successful ==="
echo "Antigravity will automatically load the new workspace skills next time you run a query."
