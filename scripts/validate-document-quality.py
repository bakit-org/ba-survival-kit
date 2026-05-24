#!/usr/bin/env python3
# validate-document-quality.py
# Scans generated BA drafts for placeholders, template compliance, and broken error code references.

import os
import re
import sys
import argparse

# Define common placeholder patterns
PLACEHOLDER_PATTERNS = [
    r"\[Insert[^\]]*\]",
    r"\[e\.g\.[^\]]*\]",
    r"\[Field \d+[^\]]*\]",
    r"\[Action \d+[^\]]*\]",
    r"\[Goal \d+[^\]]*\]",
    r"\[Requirement \d+[^\]]*\]",
    r"\[Gap \d+[^\]]*\]",
    r"\[Question \d+[^\]]*\]",
]

def scan_placeholders(content, filepath):
    """Scans content for common BA placeholder markers."""
    findings = []
    lines = content.splitlines()
    for idx, line in enumerate(lines, 1):
        for pattern in PLACEHOLDER_PATTERNS:
            matches = re.findall(pattern, line, re.IGNORECASE)
            for match in matches:
                findings.append({
                    "file": os.path.basename(filepath),
                    "line": idx,
                    "type": "PLACEHOLDER",
                    "detail": f"Unfilled placeholder '{match}' found.",
                })
    return findings

def validate_srs_registry(screens_dir):
    """Verifies that all [MSG-XXX] codes referenced in screens exist in the message-registry."""
    findings = []
    registry_file = os.path.join(screens_dir, "message-registry.md")
    
    if not os.path.exists(registry_file):
        findings.append({
            "file": "message-registry.md",
            "line": 0,
            "type": "MISSING_REGISTRY",
            "detail": "Central message-registry.md file is missing.",
        })
        return findings, set()

    # 1. Read registered message codes
    with open(registry_file, "r", encoding="utf-8") as f:
        registry_content = f.read()
    
    # Match codes like MSG-001, MSG-002, etc. (case insensitive)
    registered_codes = set(re.findall(r"MSG-\d+", registry_content, re.IGNORECASE))
    # Normalize to uppercase
    registered_codes = {code.upper() for code in registered_codes}

    # 2. Scan all screens for referenced codes
    referenced_codes = {}
    for filename in os.listdir(screens_dir):
        if filename.startswith("screen-") and filename.endswith(".md"):
            filepath = os.path.join(screens_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Find references like [MSG-001]
            refs = re.findall(r"\[(MSG-\d+)\]", content, re.IGNORECASE)
            for ref in refs:
                ref_upper = ref.upper()
                if ref_upper not in referenced_codes:
                    referenced_codes[ref_upper] = []
                referenced_codes[ref_upper].append(filename)

    # 3. Compare references with registry
    for ref, files in referenced_codes.items():
        if ref not in registered_codes:
            findings.append({
                "file": ", ".join(files),
                "line": 0,
                "type": "ORPHANED_MESSAGE_CODE",
                "detail": f"Orphaned code '[{ref}]' referenced but not defined in message-registry.md.",
            })

    return findings, registered_codes

def main():
    parser = argparse.ArgumentParser(description="Validate BA document quality and compliance.")
    parser.add_argument("--srs-dir", help="Directory containing screens and message registry")
    parser.add_argument("--doc", help="Specific document file to scan for placeholders")
    args = parser.parse_args()

    errors = []
    
    # Validate individual file placeholders
    if args.doc:
        if os.path.exists(args.doc):
            with open(args.doc, "r", encoding="utf-8") as f:
                content = f.read()
            errors.extend(scan_placeholders(content, args.doc))
        else:
            print(f"Error: Document file '{args.doc}' not found.")
            sys.exit(1)

    # Validate SRS folder and registry integrity
    if args.srs_dir:
        if os.path.exists(args.srs_dir):
            # Scan placeholders in all files in the directory
            for root, _, files in os.walk(args.srs_dir):
                for file in files:
                    if file.endswith(".md"):
                        filepath = os.path.join(root, file)
                        with open(filepath, "r", encoding="utf-8") as f:
                            content = f.read()
                        errors.extend(scan_placeholders(content, filepath))
            
            # Check message codes compliance
            registry_errors, _ = validate_srs_registry(args.srs_dir)
            errors.extend(registry_errors)
        else:
            print(f"Error: SRS directory '{args.srs_dir}' not found.")
            sys.exit(1)

    # Print validation report
    print("=== BA Document Quality Validation Report ===")
    if not errors:
        print("\033[32m✔ PASS: Document is compliant. No placeholders or broken references found.\033[0m")
        sys.exit(0)
    
    print(f"\033[31m✘ FAIL: Found {len(errors)} compliance issue(s):\033[0m\n")
    for err in errors:
        print(f"  [{err['type']}] File: {err['file']}:{err['line']} - {err['detail']}")
    
    print("\nValidation failed! Please fix the errors before final submission.")
    sys.exit(1)

if __name__ == "__main__":
    main()
