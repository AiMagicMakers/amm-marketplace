Scaffold of `AGENTS.md` at the root. Short, identical for everyone. Replace only `{{Name}}` and `{{date}}`.

FILE START

---
type: guide
updated: {{date}}
tags: [second-brain, agents]
---

# For AI agents

This folder is {{Name}}'s Second Brain. The source of truth is the `CLAUDE.md` file at the root: read it first. It holds the routing table (which information lives in which file), the working rules and the permanent corrections.

In short:

- Files are in Markdown, in English.
- Never invent. Missing information is marked `[TO COMPLETE]`.
- Never record a national ID (CIN), bank details (RIB), a password or personal data about clients.
- Respect `.claudeignore`.
- If `index.md` exists (Complete level), read it before opening other files.
- Say which file was used to answer, and what is missing or looks outdated.
- For a tool without file access (ChatGPT, Gemini), use `brief.md`: it is the one-page summary to paste at the start of the conversation.

FILE END
