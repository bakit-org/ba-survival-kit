---
name: ba-gap-check
description: Review generated BA draft documents (BRD, SRS, PRD, User Stories) against the raw customer source materials to identify logic gaps, missing requirements, contradictions, or silent assumptions. Use to ensure compliance and completeness.
---

# BA Gap Check (Helper Reviewer)

## Use when

- You have a drafted specification document and want to check its correctness and completeness against the source transcript or notes.
- You want to identify hidden requirements that were missed in the first generation.

## Do not use when

- You want to generate a new document from scratch (use generator skills instead).

## Inputs

- Drafted BA specification file (e.g., `srs.md`, `brd.md`, `user-stories.md`).
- Raw customer materials (transcripts, meeting notes).

## Instructions

1. Compare each section of the drafted document against the raw source materials.
2. Identify:
   - **Gaps:** Implicit requirements in the source that were not captured in the draft.
   - **Contradictions:** Statements in the draft that conflict with explicit statements in the source.
   - **Silent Assumptions:** Inferences in the draft that were not marked as assumptions.
3. List the findings clearly with references to the file and section.
4. Do not modify the source draft directly; output a review report.

## Output

- Gap analysis report containing:
  - Logic Gaps list
  - Contradictions list
  - Unflagged Assumptions list
  - Recommendations

## Supporting files

- `shared/extraction-rules.md`
- `shared/quality-checklist.md`
- `shared/ambiguity-rules.md`
