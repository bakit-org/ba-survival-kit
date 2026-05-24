#!/bin/bash
# merge-srs.sh
# Combines main srs.md, all screen files under srs-screens/, and the message-registry.md into a single compiled spec.

set -e

WORKSPACE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRS_FILE="${WORKSPACE_DIR}/srs.md"
SCREENS_DIR="${WORKSPACE_DIR}/srs-screens"
OUTPUT_FILE="${WORKSPACE_DIR}/srs-compiled.md"

echo "=== Merging SRS Files ==="

if [ ! -f "${SRS_FILE}" ]; then
    # Try looking in current working directory if not found in root
    SRS_FILE="./srs.md"
    SCREENS_DIR="./srs-screens"
    OUTPUT_FILE="./srs-compiled.md"
fi

if [ ! -f "${SRS_FILE}" ]; then
    echo "Error: srs.md not found!"
    exit 1
fi

echo "Source: ${SRS_FILE}"
echo "Screens: ${SCREENS_DIR}"
echo "Output: ${OUTPUT_FILE}"

# 1. Copy main SRS content
cat "${SRS_FILE}" > "${OUTPUT_FILE}"
echo -e "\n\n" >> "${OUTPUT_FILE}"

# 2. Append all screen markdown files in alphabetical order
if [ -d "${SCREENS_DIR}" ]; then
    echo "Appending screen specs..."
    for screen_file in "${SCREENS_DIR}"/screen-*.md; do
        if [ -f "${screen_file}" ]; then
            echo "  Adding: $(basename "${screen_file}")"
            echo -e "\n---\n" >> "${OUTPUT_FILE}"
            cat "${screen_file}" >> "${OUTPUT_FILE}"
            echo -e "\n" >> "${OUTPUT_FILE}"
        fi
    done
    
    # 3. Append central message registry
    registry_file="${SCREENS_DIR}/message-registry.md"
    if [ -f "${registry_file}" ]; then
        echo "  Adding: message-registry.md"
        echo -e "\n---\n" >> "${OUTPUT_FILE}"
        cat "${registry_file}" >> "${OUTPUT_FILE}"
        echo -e "\n" >> "${OUTPUT_FILE}"
    fi
else
    echo "Warning: ${SCREENS_DIR} directory not found. No screen files appended."
fi

echo "=== Merge Complete: ${OUTPUT_FILE} ==="
exit 0
