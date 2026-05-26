# Design Guidelines for BA AI-Generated Artifacts

To deliver professional BA outcomes, AI-generated documents must conform to strict design standards.

## 1. Document Typography & Structure
- Every document must start with a single, clear `# H1` title.
- Keep subheadings nested hierarchically (`## H2`, `### H3`).
- Use Markdown tables for multi-dimensional data like field lists, test case matrices, and user action triggers.
- Monospaced blocks should only be used for code, configuration, Gherkin scenarios, or ASCII charts.

## 2. Formatting Conventions
- Avoid raw HTML tags.
- Highlight missing business rules or unresolved dependencies as `Assumptions` or `Open Questions`.
- Error registry codes must follow the `[MSG-XXX]` bracketed format, allowing regex validations.
- Action names should be structured as verbs (e.g. `Click COD option`, `Enter promotion code`).

## 3. Clarity & Concision
- Use standard business analysis terminology (e.g. *happy path*, *alternative flows*, *preconditions*).
- Keep descriptions concise and bulleted to avoid massive text paragraphs.
- Focus on logical rules rather than specific visual assets (font types, background shades), which belong to designers.
