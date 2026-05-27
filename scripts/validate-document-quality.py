#!/usr/bin/env python3
# validate-document-quality.py
# Scans generated BA drafts for placeholders, syntax correctness, and template compliance.

import os
import re
import sys
import argparse

# Common placeholder patterns
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

REFERENCE_ASSET_NAMES = {
    "ac-template.md",
    "consistency-review-checklist.md",
    "mini-pack-structure.md",
    "review-checklist-uc-us.md",
    "screen-description-template.md",
    "test-case-template.md",
    "use-case-template.md",
    "user-story-template.md",
}

def is_reference_asset(filepath):
    normalized_parts = os.path.normpath(filepath).lower().split(os.sep)
    filename = normalized_parts[-1]
    return filename in REFERENCE_ASSET_NAMES and (
        "resources" in normalized_parts or "templates" in normalized_parts
    )

def scan_placeholders(content, filepath):
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

def validate_user_stories(content, filepath):
    findings = []
    if is_reference_asset(filepath):
        return findings
    # If the file contains story indicators, validate formatting
    if "câu chuyện người dùng" in content.lower() or "user story" in content.lower():
        # Check standard US structures
        # Look for Là/Tôi muốn/Để or As a/I want/So that
        plain_content = re.sub(r"[*_`]", "", content.lower())
        has_vn = ("là " in plain_content and "tôi muốn " in plain_content and "để " in plain_content)
        has_en = ("as a" in content.lower() and "i want" in content.lower() and "so that" in content.lower())
        if not (has_vn or has_en):
            findings.append({
                "file": os.path.basename(filepath),
                "line": 1,
                "type": "INVALID_STORY_FORMAT",
                "detail": "User Story format must follow: 'Là... Tôi muốn... Để...' or 'As a... I want to... So that...'",
            })
    return findings

def validate_acceptance_criteria(content, filepath):
    findings = []
    if is_reference_asset(filepath):
        return findings
    if "tiêu chí nghiệm thu" in content.lower() or "acceptance criteria" in content.lower():
        # Gherkin check: Cho/Khi/Thì or Given/When/Then
        has_vn = ("cho (" in content.lower() or "cho:" in content.lower() or "khi (" in content.lower() or "thì (" in content.lower())
        has_en = ("given" in content.lower() or "when" in content.lower() or "then" in content.lower())
        if not (has_vn or has_en):
            findings.append({
                "file": os.path.basename(filepath),
                "line": 1,
                "type": "INVALID_AC_FORMAT",
                "detail": "Acceptance criteria must contain Given/When/Then or Cho/Khi/Thì Gherkin structure.",
            })
    return findings

def validate_mermaid_diagrams(content, filepath):
    findings = []
    # Find all mermaid blocks
    mermaid_blocks = re.findall(r"```mermaid\s*\n(.*?)\n```", content, re.DOTALL)
    for block in mermaid_blocks:
        lines = [line.strip() for line in block.strip().splitlines() if line.strip()]
        if not lines:
            continue
        
        # Check header type
        header = lines[0]
        valid_headers = ["graph TD", "graph LR", "sequenceDiagram", "flowchart TD", "flowchart LR"]
        if not any(header.startswith(vh) for vh in valid_headers):
            findings.append({
                "file": os.path.basename(filepath),
                "line": 1,
                "type": "INVALID_MERMAID_TYPE",
                "detail": f"Mermaid diagram must start with TD/LR flowchart or sequenceDiagram (Found: '{header}').",
            })
        
        # Check for unquoted special characters in flowchart labels
        for idx, line in enumerate(lines, 1):
            # Matches node definitions like: A[Text (Extra)] or A(Text [Extra])
            # If brackets/parenthesis are nested without quotes, Mermaid CLI parses error
            if any(vh in header for vh in ["graph", "flowchart"]):
                bad_matches = re.findall(r"\w+\[[^\"\]]*[\(\)][^\"\]]*\]", line)
                if bad_matches:
                    findings.append({
                        "file": os.path.basename(filepath),
                        "line": idx,
                        "type": "INVALID_MERMAID_LABEL",
                        "detail": f"Label with nested parentheses must be quoted in quotes: '{line}'",
                    })
    return findings

def validate_use_cases(content, filepath):
    findings = []
    if is_reference_asset(filepath):
        return findings
    use_case_heading = re.search(r"^#{1,4}\s+.*(?:ca sử dụng|use case)", content, re.IGNORECASE | re.MULTILINE)
    if use_case_heading:
        required_headers = [
            r"luồng sự kiện chính",
            r"luồng sự kiện thay thế",
            r"luồng xử lý ngoại lệ"
        ]
        for header in required_headers:
            if not re.search(header, content, re.IGNORECASE):
                findings.append({
                    "file": os.path.basename(filepath),
                    "line": 1,
                    "type": "MISSING_USECASE_SECTION",
                    "detail": f"Use case document is missing required section: '{header}'.",
                })
    return findings

def validate_test_cases(content, filepath):
    findings = []
    if is_reference_asset(filepath):
        return findings
    if "kịch bản kiểm thử" in content.lower() or "test case" in content.lower():
        required_headers = ["Test ID", "Scenario", "Preconditions", "Steps", "Expected Result"]
        required_headers_vn = ["Mã Test Case", "Kịch bản kiểm thử", "Điều kiện tiên quyết", "Các bước thực hiện", "Kết quả kỳ vọng"]
        
        has_en = all(h in content for h in required_headers)
        has_vn = all(h in content for h in required_headers_vn)
        
        if not (has_en or has_vn):
            findings.append({
                "file": os.path.basename(filepath),
                "line": 1,
                "type": "INVALID_TESTCASE_TABLE",
                "detail": "Test Case table must contain standard headers: [Test ID, Scenario, Preconditions, Steps, Expected Result].",
            })
    return findings

def validate_screen_description(content, filepath):
    findings = []
    if is_reference_asset(filepath):
        return findings
    if "thông tin màn hình" in content.lower() or "screen info" in content.lower():
        required_sections = [
            r"hành động của người dùng",
            r"danh sách trường dữ liệu",
            r"quy tắc hiển thị",
            r"quy tắc tương tác và hành vi",
            r"quy tắc kiểm tra tính hợp lệ dữ liệu",
            r"các trạng thái màn hình",
            r"thông báo hệ thống"
        ]
        for sec in required_sections:
            if not re.search(sec, content, re.IGNORECASE):
                findings.append({
                    "file": os.path.basename(filepath),
                    "line": 1,
                    "type": "MISSING_SCREEN_SECTION",
                    "detail": f"Screen Specification is missing required section: '{sec}'.",
                })
    return findings

def validate_merged_mini_pack(content, filepath):
    findings = []
    if is_reference_asset(filepath):
        return findings
    if "mini ba pack" not in content.lower() and "bộ hồ sơ tài liệu ba thu nhỏ" not in content.lower():
        return findings
    required_sections = {
        "scope/source": r"^#{1,4}\s+.*(?:nguồn|phạm vi|brief|tóm tắt)",
        "wireframe": r"^#{1,4}\s+.*(?:giao diện phác thảo|wireframe)",
        "screen specification": r"^#{1,4}\s+.*(?:thông tin màn hình|screen info|screen spec)",
        "diagram": r"^#{1,4}\s+.*(?:sơ đồ|diagram)",
        "use case": r"^#{1,4}\s+.*(?:ca sử dụng|use case)",
        "story and acceptance criteria": r"^#{1,4}\s+.*(?:câu chuyện người dùng|user stor)",
        "review checklist": r"^#{1,4}\s+.*(?:checklist|kiểm duyệt)",
        "test cases": r"^#{1,4}\s+.*(?:kịch bản kiểm thử|test case)",
        "traceability matrix": r"^#{1,4}\s+.*(?:ma trận truy vết|traceability)",
    }
    for section, pattern in required_sections.items():
        if not re.search(pattern, content, re.IGNORECASE | re.MULTILINE):
            findings.append({
                "file": os.path.basename(filepath),
                "line": 1,
                "type": "MISSING_MINI_PACK_SECTION",
                "detail": f"Merged Mini BA Pack is missing required section '{section}'.",
            })
    required_patterns = {
        "CHK-{DOMAIN}-{NN}": r"\bCHK-[A-Z][A-Z0-9-]*-\d{2,}\b",
        "UC-{FLOW}-{NN}": r"\bUC-[A-Z][A-Z0-9-]*-\d{2,}\b",
        "US-{FLOW}-{NN}": r"\bUS-[A-Z][A-Z0-9-]*-\d{2,}\b",
        "AC-{FLOW}-{NN}": r"\bAC-[A-Z][A-Z0-9-]*-\d{2,}\b",
        "TC-{FLOW}-{NN}": r"\bTC-[A-Z][A-Z0-9-]*-\d{2,}\b",
        "MSG-{TYPE}-{NN}": r"\bMSG-(?:ERR|WRN|SUC|INF)-\d{2,}\b",
    }
    for token, pattern in required_patterns.items():
        if not re.search(pattern, content):
            findings.append({
                "file": os.path.basename(filepath),
                "line": 1,
                "type": "MISSING_TRACEABILITY_ID",
                "detail": f"Merged Mini BA Pack is missing required traced identifier type '{token}'.",
            })
    trace_pattern = re.compile(
        r"^\|\s*(CHK-[A-Z][A-Z0-9-]*-\d{2,})\s*\|\s*"
        r"(UC-[A-Z][A-Z0-9-]*-\d{2,})\s*\|\s*"
        r"(US-[A-Z][A-Z0-9-]*-\d{2,})\s*\|\s*"
        r"(AC-[A-Z][A-Z0-9-]*-\d{2,})\s*\|\s*"
        r"(TC-[A-Z][A-Z0-9-]*-\d{2,})\s*\|\s*"
        r"(-|MSG-(?:ERR|WRN|SUC|INF)-\d{2,})\s*\|$",
        re.MULTILINE,
    )
    trace_rows = trace_pattern.findall(content)
    if not trace_rows:
        findings.append({
            "file": os.path.basename(filepath),
            "line": 1,
            "type": "MISSING_TRACEABILITY_ROW",
            "detail": "Merged Mini BA Pack must contain at least one complete CHK -> UC -> US -> AC -> TC trace row.",
        })
    traced_ac_ids = {row[3] for row in trace_rows}
    traced_tc_ids = {row[4] for row in trace_rows}
    defined_ac_ids = set(re.findall(r"^#{2,6}\s+(AC-[A-Z][A-Z0-9-]*-\d{2,})\b", content, re.MULTILINE))
    test_rows = re.findall(r"^\|\s*(TC-[A-Z][A-Z0-9-]*-\d{2,})\s*\|(.+)\|$", content, re.MULTILINE)
    defined_tc_ids = {row[0] for row in test_rows}
    for missing_ac in sorted(defined_ac_ids - traced_ac_ids):
        findings.append({
            "file": os.path.basename(filepath),
            "line": 1,
            "type": "UNTRACED_ACCEPTANCE_CRITERION",
            "detail": f"Acceptance criterion '{missing_ac}' does not appear in the traceability matrix.",
        })
    for missing_tc in sorted(defined_tc_ids - traced_tc_ids):
        findings.append({
            "file": os.path.basename(filepath),
            "line": 1,
            "type": "UNTRACED_TEST_CASE",
            "detail": f"Test case '{missing_tc}' does not appear in the traceability matrix.",
        })
    message_definitions = dict(re.findall(
        r"^\|\s*(MSG-(?:ERR|WRN|SUC|INF)-\d{2,})\s*\|\s*(?:[^|\n]+\|\s*)?([^|\n]+?)\s*\|$",
        content,
        re.MULTILINE,
    ))
    tested_message_refs = []
    for test_case_id, test_row_content in test_rows:
        for message_id in re.findall(r"\bMSG-(?:ERR|WRN|SUC|INF)-\d{2,}\b", test_row_content):
            tested_message_refs.append((test_case_id, message_id, test_row_content))
    for test_case_id, message_id, test_row_content in tested_message_refs:
        if message_id not in message_definitions:
            findings.append({
                "file": os.path.basename(filepath),
                "line": 1,
                "type": "MISSING_MESSAGE_DEFINITION",
                "detail": f"Trace row references '{message_id}' without a message definition.",
            })
            continue
        expected_text = message_definitions[message_id].strip()
        if expected_text not in test_row_content:
            findings.append({
                "file": os.path.basename(filepath),
                "line": 1,
                "type": "MESSAGE_TEXT_MISMATCH",
                "detail": f"Test case '{test_case_id}' must reuse exact text for '{message_id}'.",
            })
    return findings

def main():
    parser = argparse.ArgumentParser(description="Validate BA document quality and compliance.")
    parser.add_argument("--srs-dir", help="Directory containing screens and message registry")
    parser.add_argument("--doc", help="Specific document file to scan for placeholders")
    args = parser.parse_args()

    errors = []
    
    # Validate individual file
    if args.doc:
        if os.path.exists(args.doc):
            with open(args.doc, "r", encoding="utf-8") as f:
                content = f.read()
            errors.extend(scan_placeholders(content, args.doc))
            errors.extend(validate_user_stories(content, args.doc))
            errors.extend(validate_acceptance_criteria(content, args.doc))
            errors.extend(validate_mermaid_diagrams(content, args.doc))
            errors.extend(validate_use_cases(content, args.doc))
            errors.extend(validate_test_cases(content, args.doc))
            errors.extend(validate_screen_description(content, args.doc))
            errors.extend(validate_merged_mini_pack(content, args.doc))
        else:
            print(f"Error: Document file '{args.doc}' not found.")
            sys.exit(1)

    # Validate SRS directory (recursive)
    if args.srs_dir:
        if os.path.exists(args.srs_dir):
            for root, _, files in os.walk(args.srs_dir):
                for file in files:
                    if file.endswith(".md"):
                        filepath = os.path.join(root, file)
                        with open(filepath, "r", encoding="utf-8") as f:
                            content = f.read()
                        errors.extend(scan_placeholders(content, filepath))
                        errors.extend(validate_user_stories(content, filepath))
                        errors.extend(validate_acceptance_criteria(content, filepath))
                        errors.extend(validate_mermaid_diagrams(content, filepath))
                        errors.extend(validate_use_cases(content, filepath))
                        errors.extend(validate_test_cases(content, filepath))
                        errors.extend(validate_screen_description(content, filepath))
                        errors.extend(validate_merged_mini_pack(content, filepath))
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
