---
name: ba-polish-doc
description: Polish and format draft specifications into professional, structured documents. Supports --internal mode (keeps detailed gaps, assumptions, raw citations) and --client-ready mode (polishes tone, moves gaps to a meeting agenda).
---

# BA Polish Doc (Helper)

## Use when

- You have a raw or semi-polished draft document that needs formatting, tone refinement, or style cleanup.
- You need to prepare a document specifically for internal review or for a client meeting.

## Do not use when

- The document content is missing or incomplete (use generator or gap-check skills first).

## Inputs

- Generated draft document (e.g., `brd.md`, `srs.md`).
- Formatting flags: `--internal` (default) or `--client-ready`.

## Instructions

1. Read the draft document and clean up formatting, headings, lists, and markdown style.
2. Refine sentence structures for professional BA tone (concise, passive when formal, active when describing actions).
3. If `--internal` flag is active:
   - Preserve all detailed `Assumptions`, `Open Questions`, and `Source Gaps` sections.
   - Maintain any inline citations referencing lines in transcripts or notes.
4. If `--client-ready` flag is active:
   - Rewrite assumptions into polite, business-friendly statements (e.g., "The system is expected to..." instead of "We assume that...").
   - Compile raw `Open Questions` and `Source Gaps` into a structured, clean "Next Steps & Agenda" section suitable for a client review meeting. Remove raw developer-focused questions.

## Output

- Polished specification document

## Supporting files

- `shared/writing-rules.md`
- `shared/quality-checklist.md`
