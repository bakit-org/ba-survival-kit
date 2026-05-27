---
name: meeting-notes-summary
description: Distill unstructured meeting notes or transcripts into agreed-upon decisions, action items, assumptions, and open questions.
---

# Meeting Notes Summary

## Use when

- You have a raw meeting transcript or notes and want a concise summary.
- You need to track project decisions, action items, and open questions from a workshop or meeting.

## Do not use when

- You want to write a full SRS or functional requirement document.
- You want to create visual layouts or diagrams.

## Inputs

- Meeting notes or meeting transcript file.

## Instructions

1. Analyze the meeting notes/transcript to identify main discussion points.
2. Extract all decisions made (agreed-upon rules, flows, scopes).
3. Identify action items, attributing them to specific owners and deadlines if mentioned.
4. Extract open questions (unresolved issues) and assumptions (placeholder decisions).
5. Format the output using clear bullet points and header sections.
6. Apply the installed `artifact-quality-contract.md` supporting file listed below, then run its validator and resolve reported errors.

## Output

- meeting-notes-summary.md (Distilled meeting summary with decisions and action items)

## Supporting files

- `.agents/ba-survival-kit/shared/artifact-quality-contract.md` (workspace) or `~/.gemini/antigravity/ba-survival-kit/shared/artifact-quality-contract.md` (global)
