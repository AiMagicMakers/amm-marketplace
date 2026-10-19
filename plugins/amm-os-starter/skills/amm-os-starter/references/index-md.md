Scaffold of `index.md` at the root (Complete level only). It is the catalogue of all notes: one line per note, with a link and a short description. The assistant reads it first and opens files second. It must always tell the truth: every note created, renamed or deleted updates the index in the same operation.

Filling rules:
- One line per note. The description is one sentence of 20 words or fewer, drawn from the note's real content, never invented.
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

- [[Context/identity]]: {{description}}
- [[Context/offers-and-prices]]: {{description}}
- [[Context/clients]]: {{description}}
- [[Context/style]]: {{description}}
- [[Context/processes]]: {{description}}
- [[Context/tools]]: {{description}}
- [[Context/goals]]: {{description}}
- [[Context/rules]]: {{description}}

## Projects

- [[Projects/{{slug}}/README]]: {{description}}

## Journal

- [[Journal/{{YYYY-MM-DD}}]]: {{description}}

## Decisions

- [[Decisions/{{YYYY-MM-DD-topic}}]]: {{description}}

## Resources

- [[Resources/{{path}}]]: {{description}}

FILE END
