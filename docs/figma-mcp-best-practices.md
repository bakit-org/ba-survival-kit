# Figma MCP Best Practices for Business Analysts

This course uses Figma MCP as the only Figma integration path. Skills prepare requirement-backed Markdown; the configured MCP operation creates or inspects the wireframe frame.

## Workflow

1. Run `wireframe-request-prep` from approved requirements or screen brief.
2. Review required fields, actions, states, business rules, and exact labels in `wireframe-request.md`.
3. Invoke the configured Figma MCP operation in Antigravity with that request.
4. Capture the returned frame or node reference in `wireframe-review-notes.md`.
5. Run `wireframe-review-note-generator` against the source request and MCP-produced draft.
6. Resolve critical logic or missing-state findings before writing screen specifications.

## Request Content

- Include a stable Screen ID and screen purpose.
- Include exact user-facing field and action labels.
- State the required default, error, unavailable, loading, and success states.
- State only sourced business rules; keep gaps as open questions.

## Review Evidence

- Record the Figma frame or node reference returned through MCP.
- Verify every required field and action appears in the frame.
- Verify error/unavailable state evidence for each relevant rule.
- Preserve exact terminology for use in screen specs, use cases, and test cases.

## Boundary

The skill pack does not invent Figma MCP server configuration. The course workspace must have an authorized Figma MCP connection available before the visual lab begins.
