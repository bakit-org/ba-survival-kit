#!/bin/bash
# validate-skill-tree.sh
# Checks that all skills in skills/ contain valid SKILL.md files and follow authoring standards

set -e

WORKSPACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_DIR="${WORKSPACE_DIR}/skills"

echo "=== Running Skill Tree Validation ==="
echo "Target directory: ${SKILLS_DIR}"

if [ ! -d "${SKILLS_DIR}" ]; then
    echo "Error: skills/ directory not found!"
    exit 1
fi

error_count=0
success_count=0

for skill_path in "${SKILLS_DIR}"/*; do
    if [ -d "${skill_path}" ]; then
        skill_name=$(basename "${skill_path}")
        echo -n "Checking skill [${skill_name}]... "
        
        # Check for SKILL.md existence
        skill_file="${skill_path}/SKILL.md"
        if [ ! -f "${skill_file}" ]; then
            echo -e "\033[31mFAILED (SKILL.md missing)\033[0m"
            error_count=$((error_count + 1))
            continue
        fi
        
        # Check for metadata name and description front-matter
        if ! grep -q "^name:" "${skill_file}"; then
            echo -e "\033[31mFAILED (name metadata missing in front-matter)\033[0m"
            error_count=$((error_count + 1))
            continue
        fi
        
        if ! grep -q "^description:" "${skill_file}"; then
            echo -e "\033[31mFAILED (description metadata missing in front-matter)\033[0m"
            error_count=$((error_count + 1))
            continue
        fi
        
        echo -e "\033[32mOK\033[0m"
        success_count=$((success_count + 1))
    fi
done

for required_dir in templates shared scripts; do
    if [ ! -d "${WORKSPACE_DIR}/${required_dir}" ]; then
        echo -e "\033[31mFAILED (${required_dir}/ runtime dependency missing)\033[0m"
        error_count=$((error_count + 1))
    fi
done

for stale_term in "Figma Make" "First Draft" "ba-generate-srs"; do
    if grep -Rqs "${stale_term}" "${WORKSPACE_DIR}/README.md" "${WORKSPACE_DIR}/docs" "${WORKSPACE_DIR}/skills" "${WORKSPACE_DIR}/templates" "${WORKSPACE_DIR}/shared" "${WORKSPACE_DIR}/resources" "${WORKSPACE_DIR}/.agents/skills"; then
        echo -e "\033[31mFAILED (stale Figma workflow term found: ${stale_term})\033[0m"
        error_count=$((error_count + 1))
    fi
done

echo ""
echo "=== Validation Summary ==="
echo "Valid Skills: ${success_count}"
echo "Failed Skills: ${error_count}"

if [ ${error_count} -gt 0 ]; then
    echo "Tree check failed!"
    exit 1
else
    echo "Tree check passed successfully!"
    exit 0
fi
