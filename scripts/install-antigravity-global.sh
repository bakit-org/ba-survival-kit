#!/bin/bash
# install-antigravity-global.sh
# Syncs skills/ to the user's global ~/.gemini/antigravity/skills/ folder

set -e

WORKSPACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${HOME}/.gemini/antigravity/skills"

echo "=== Installing Antigravity Global Skills ==="
echo "Source: ${WORKSPACE_DIR}/skills"
echo "Target: ${TARGET_DIR}"

# Create target directory if it doesn't exist
mkdir -p "${TARGET_DIR}"

# Sync folders under skills/ into ~/.gemini/antigravity/skills/
if [ -d "${WORKSPACE_DIR}/skills" ]; then
    for skill_path in "${WORKSPACE_DIR}/skills"/*; do
        if [ -d "${skill_path}" ]; then
            skill_name=$(basename "${skill_path}")
            echo "Installing global skill: ${skill_name}..."
            
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
echo "Antigravity will load these skills globally across all workspace directories."
