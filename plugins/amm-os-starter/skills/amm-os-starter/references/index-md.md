Scaffold of `index.md` at the root (Complete level only). It is the catalogue of all notes: one line per note, with a link and a short description. The assistant reads it first and opens files second. It must always tell the truth: every note created, renamed or deleted updates the index in the same operation.

Filling rules:
- One line per note. Each description says what question the note answers, written as `answers "..."`, in 20 words or fewer, drawn from the note's real content and never invented. Example: `- [[Context/offers-and-prices]]: answers "what do you charge, what is included, on what conditions?"`
- List the notes of `Context/`, `Projects/` (the README of each project), `Journal/`, `Decisions/`, `Resources/` (including the files in `Resources/sources/`).
- Do not list the `CLAUDE.md` files, `AGENTS.md`, `brief.md`, `graph.html` or the index itself.
- No prices or other figures in the descriptions: they go stale and can contradict the notes.
- A file that is not Markdown keeps its extension in the link (`[[Resources/sources/price-list.pdf]]`).
- An empty folder has no section.

FILE START

---
type: index
updated: {{date}}
tags: [second-brain, index]
---

# Index

Catalogue of all the notes in {{Name}}'s Second Brain. One line per note. Read this index first, open files second.

## Context

- [[Context/identity]]: answers "{{the question this note answers}}"
- [[Context/offers-and-prices]]: answers "{{the question this note answers}}"
- [[Context/clients]]: answers "{{the question this note answers}}"
- [[Context/style]]: answers "{{the question this note answers}}"
- [[Context/processes]]: answers "{{the question this note answers}}"
- [[Context/tools]]: answers "{{the question this note answers}}"
- [[Context/goals]]: answers "{{the question this note answers}}"
- [[Context/rules]]: answers "{{the question this note answers}}"

## Projects

- [[Projects/{{slug}}/README]]: answers "{{the question this note answers}}"

## Journal

- [[Journal/{{YYYY-MM-DD}}]]: answers "{{the question this note answers}}"

## Decisions

- [[Decisions/{{YYYY-MM-DD-topic}}]]: answers "{{the question this note answers}}"

## Resources

- [[Resources/{{path}}]]: answers "{{the question this note answers}}"

FILE END
