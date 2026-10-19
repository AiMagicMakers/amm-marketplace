Scaffold of a `Decisions/` note (Complete level), named `YYYY-MM-DD-short-topic.md`. Create a note only for a decision the person really made. The skill does not create any by default: the folder is ready for later.

FILE START

---
type: decision
updated: {{date}}
tags: [decision, {{topic}}]
status: {{current or superseded}}
---

# {{Decision title}}

## Context

{{What happened, why a decision was needed.}}

## Decision

{{What was decided, in one or two sentences.}}

## Options rejected

- {{option}}: {{why not}}

## Reason

{{The why, in the person's words.}}

## To review

{{Date or condition to review it. Otherwise: [TO COMPLETE].}}

## Links

Concerns: {{[[Context/offers-and-prices]] or another note}}.

FILE END
