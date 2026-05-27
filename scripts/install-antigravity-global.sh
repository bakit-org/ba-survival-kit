#!/bin/bash
# install-antigravity-global.sh
# Installs skills and their runtime dependencies into Antigravity global storage.

set -e

WORKSPACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET_DIR="${HOME}/.gemini/antigravity/skills"
RUNTIME_DIR="${HOME}/.gemini/antigravity/ba-survival-kit"
INSTALL_SUFFIX=".$$.install"

replace_directory() {
    local staged_dir="$1"
    local target_dir="$2"
    local backup_dir="${target_dir}${INSTALL_SUFFIX}.backup"

    rm -rf "${backup_dir}"
    if [ -d "${target_dir}" ]; then
        mv "${target_dir}" "${backup_dir}"
    fi
    if mv "${staged_dir}" "${target_dir}"; then
        rm -rf "${backup_dir}"
    else
        rm -rf "${target_dir}"
        if [ -d "${backup_dir}" ]; then
            mv "${backup_dir}" "${target_dir}"
        fi
        return 1
    fi
}

cleanup_staging() {
    rm -rf "${RUNTIME_DIR}${INSTALL_SUFFIX}" "${TARGET_DIR}${INSTALL_SUFFIX}"
}

trap cleanup_staging EXIT

echo "=== Installing Antigravity Global Skills ==="
echo "Source: ${WORKSPACE_DIR}/skills"
echo "Target: ${TARGET_DIR}"

# Create target directory if it doesn't exist
mkdir -p "${TARGET_DIR}"

if [ -d "${WORKSPACE_DIR}/skills" ]; then
    staged_skills="${TARGET_DIR}${INSTALL_SUFFIX}"
    staged_runtime="${RUNTIME_DIR}${INSTALL_SUFFIX}"
    rm -rf "${staged_skills}" "${staged_runtime}"
    mkdir -p "${staged_skills}" "${staged_runtime}"
    for skill_path in "${WORKSPACE_DIR}/skills"/*; do
        if [ -d "${skill_path}" ]; then
            skill_name=$(basename "${skill_path}")
            cp -R "${skill_path}" "${staged_skills}/"
            test -s "${staged_skills}/${skill_name}/SKILL.md"
        fi
    done
    cp -R "${WORKSPACE_DIR}/templates" "${WORKSPACE_DIR}/shared" "${WORKSPACE_DIR}/scripts" "${staged_runtime}/"
    test -f "${staged_runtime}/scripts/validate-document-quality.py"
    test -d "${staged_runtime}/templates"
    test -d "${staged_runtime}/shared"
    replace_directory "${staged_runtime}" "${RUNTIME_DIR}"
    for skill_path in "${staged_skills}"/*; do
        skill_name=$(basename "${skill_path}")
        echo "Installing global skill: ${skill_name}..."
        mkdir -p "${TARGET_DIR}/${skill_name}"
        mv "${skill_path}/SKILL.md" "${TARGET_DIR}/${skill_name}/SKILL.md"
    done
    rm -rf "${staged_skills}"
    echo "Sync complete!"
else
    echo "Error: skills/ directory not found in workspace!"
    exit 1
fi

echo "=== Installation Successful ==="
echo "Antigravity will load these skills globally across all workspace directories."
echo "Runtime dependencies installed at ${RUNTIME_DIR}."
