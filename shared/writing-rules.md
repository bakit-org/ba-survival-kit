---
title: BA Writing Rules
status: draft
updated: 2026-05-23
---

# BA Writing Rules

These rules keep generated BA documents readable and predictable.

## Tone

- Professional
- Direct
- Concise
- Neutral

## Style

1. Prefer short sentences.
2. Use one intent per bullet or sentence.
3. Avoid jargon unless it appears in the source or is standard for the domain.
4. Prefer concrete nouns and verbs over vague phrases.
5. Use parallel structure in lists.

## Terminology

1. Reuse the customer's business terms when clear.
2. If two terms appear to mean the same thing, pick one primary term and note the synonym if needed.
3. Do not rename core business entities casually.

## Document Structure

1. Follow the matching file in `templates/`.
2. Keep headings stable across drafts.
3. Use bullets for requirements, assumptions, and questions.
4. Use tables only when they make comparison clearer.

## Requirement Wording

Good pattern:

- "The system shall allow the user to submit a purchase request."
- "The business needs visibility into approval status by requester and date."

Avoid:

- "Maybe the app can..."
- "It should probably..."
- "Users somehow manage..."

## Uncertainty Labels

When content is not confirmed, label it directly:

- `Assumption:`
- `Open Question:`
- `Source Gap:`

Do not bury uncertainty inside normal prose.

## What to Avoid

- Long speculative paragraphs
- Hidden assumptions
- Mixed terminology
- Overly technical implementation detail
- Fake precision

## Preferred End State

A reader should be able to skim the draft and quickly see:

- what the client wants
- who is involved
- what the system or process must do
- what is still missing
