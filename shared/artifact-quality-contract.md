# BA Artifact Quality Contract

Apply this contract to every generated deliverable before handoff.

## Source Discipline

- Preserve the terminology in the approved source input.
- Separate confirmed facts from assumptions and open questions.
- Do not invent business rules, validation messages, integrations, or screen behavior.

## Traceability

- Use stable identifiers where the artifact supports them: `CHK-{DOMAIN}-{NN}` for screens, `UC-{FLOW}-{NN}` for use cases, `US-{FLOW}-{NN}` for stories, `AC-{FLOW}-{NN}` for acceptance criteria, `TC-{FLOW}-{NN}` for test cases, and `MSG-{TYPE}-{NN}` for messages (`TYPE` is `ERR`, `WRN`, `SUC`, or `INF`).
- Map screen actions to use-case steps using the same wording.
- Map acceptance criteria to user stories and test cases.
- Reuse the same message IDs and exact message text across screen specifications and test cases.

## Figma MCP Evidence

- For Figma-backed wireframes, retain the Screen ID and record the MCP-returned frame or node reference in review notes.
- A wireframe draft is not approved until required fields, actions, and relevant states have been reviewed against the request.

## Validation

Use the installed validator path available in the current Antigravity installation:

```bash
python3 .agents/ba-survival-kit/scripts/validate-document-quality.py --doc <output_file_name>
```

For global installations, use:

```bash
python3 ~/.gemini/antigravity/ba-survival-kit/scripts/validate-document-quality.py --doc <output_file_name>
```
