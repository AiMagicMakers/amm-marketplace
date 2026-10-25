Scaffolds of the `CLAUDE.md` files of each folder. Each "## Section: X" becomes the `CLAUDE.md` of folder X. Do not copy the "## Section" title line. Each file starts with this frontmatter:

```
---
type: guide
updated: {{date}}
tags: [second-brain, routing, {{folder-in-lowercase}}]
---
```

Adapt the file table to what really exists in the folder. Replace `{{Name}}`.

## Section: Context

# Context

This folder is the foundation of {{Name}}'s Second Brain. These are the reference facts: who, what, for whom, how. All the other folders build on it.

## Files

| File | Content | Update it when |
|---|---|---|
| `identity.md` | Who {{Name}} is, story, conviction | The positioning changes |
| `offers-and-prices.md` | Offers, prices in DH excl. VAT, conditions | A price or an offer changes |
| `clients.md` | Typical client, their words, their problems | A client is better understood |
| `style.md` | Tone, forbidden words, example texts | A style instruction is given |
| `processes.md` | Ways of working, drains to automate | A way of doing things changes |
| `tools.md` | Tools and source of truth per subject | A tool is changed or added |
| `goals.md` | Goals for the year, current projects | A goal or a project moves |
| `rules.md` | Working rules with AI, confidentiality | A lasting rule is decided |

## Folder rules

- A fact lives in one place. Elsewhere, put a `[[link]]` to it.
- Each file in this folder says where its information comes from in the `sources` field of the frontmatter (for example `initial-interview` or the name of a provided document). If a source changes or disappears, the field is corrected.
- Never invent. Missing information is written `[TO COMPLETE]`.
- After any change here, update `updated` in the frontmatter and redo `brief.md` at the root.
- {{Name}}'s corrections about how to work go in the "User corrections" section of the root `CLAUDE.md`, not here.

## Section: Projects

# Projects

One folder per current project of {{Name}}. A project has a start, an end and an expected result (example: launch an offer, rebuild a website, prepare a training).

## Structure

```
Projects/
  project-name/
    README.md
```

The `README.md` is the front door: goal, status, deadline, people involved, next steps. When a project grows, add files next to it (notes, drafts, meeting notes) and link them from the `README.md`.

## Rules

- Folder name in lowercase with hyphens, no accents (example: `smb-offer-launch`).
- A new project starts with a `README.md` alone. No empty subfolders.
- In the frontmatter of each note of a project, add `project: project-name`.
- Every project should serve a goal in [[Context/goals]]. If none fits, flag it.
- A finished project goes to `Archive/` with a one-line summary of the outcome in its `README.md`.

## Section: Journal

# Journal

One note per meaningful working day, named `YYYY-MM-DD.md`. It records what was done, decided and left to do, so the next session starts without asking everything again.

## Shape of a note

Sections: What was done, Decisions made, What is left to do, Ideas to keep, and What worked or failed when there is a lesson (an exact fix, a message that got a reply, a mistake to avoid).

## Rules

- Write in the journal when real work took place, not for a quick question. After meaningful work, offer a short entry and save it only after {{Name}} says yes.
- If an important decision is made, also copy it to `Decisions/` and put a `[[link]]` in the journal.
- Stay concrete: project names, what was delivered, what blocks.
- At the start of a session, read the latest note.

## Section: Decisions

# Decisions

One note per important decision: a price changed, an offer stopped, a tool chosen, a client refused. The aim is to remember the why, six months later.

## Rules

- File name: `YYYY-MM-DD-short-topic.md`.
- Each note says: the context, the decision, the options rejected, the reason, when to review it.
- A decision is never erased. If it changes, write a new note that points to the old one with a `[[link]]`.
- Only record decisions that {{Name}} really made.

## Section: Resources

# Resources

The library of what gets reused: prompts, templates for messages and documents, examples that worked well.

## Layout

| Subfolder | Content |
|---|---|
| `prompts/` | Tested prompts for tasks that come back |
| `templates/` | Templates for quotes, WhatsApp messages, emails, posts |
| `examples/` | Successful texts, to imitate for the tone |
| `sources/` | The original documents provided by {{Name}} (sales brief, presentation, quote template). They are never modified |

Create a subfolder only when its first file arrives. `sources/` is the exception: it exists from the start, even empty.

When a note summarises a document in `sources/`, it cites it in its `sources` field. Every file in `Resources/`, including those in `sources/`, has its line in `index.md`.

## Rules

- Give the file a clear name (`follow-up-quote-no-reply.md`).
- Do not duplicate what already exists in a project: make a `[[link]]`.
- No name of a private client or personal data in the examples. Anonymise.
- Put nothing in `sources/` that contains a national ID, bank details, a password or contact details of private clients.

## Section: Tasks

# Tasks

The work that serves {{Name}}'s goals. One file per task, named `T-0001-short-title.md`. The AI crew (Writer, Researcher, Checker) prepares drafts; {{Name}} decides. The board, `board.html` at the root, shows every task by status and what the crew logged.

## Statuses

backlog, ready, in-progress, review, done, blocked. A task is `ready` only when its "Done when" section lists at least one condition. Only {{Name}} moves a task from `review` to `done`.

## Rules

- Draft only: never send, publish or schedule anything, and never change a file outside `Tasks/` (the board is an exception, and so is saving an approved text in `Resources/templates/`, which needs {{Name}}'s yes).
- Work one task at a time, and log every step in the task's Log.
- Log line format, one per event, append only: `- YYYY-MM-DD HH:MM | Agent | mode | event | note`. Agent is You, Claude, Writer, Researcher or Checker. Mode is you, main, sub-agent or inline. Event is created, ready, started, finished, review, approved, changes, blocked, unblocked or note. Write `sub-agent` only when a sub-agent really ran.
- No national ID, bank details, passwords or personal data about clients in tasks, logs or drafts.
- Link each task to a goal in [[Context/goals]].
- Say "show the board" to rebuild `board.html`. Never read that file: it is generated.

## Section: Skills

# Skills

A skill is a small ability that AI can reuse (example: "write a follow-up for a quote"). This folder keeps {{Name}}'s notes for their future skills: what the skill should do, what it should avoid, examples.

## Structure

```
Skills/
  skill-name/
    notes.md
```

`notes.md` states in a few lines the goal of the skill, when to use it, {{Name}}'s own rules and one or two examples. Create the folder when the idea of the skill appears.

## Rules

- One folder per skill, name in lowercase with hyphens.
- Do not copy the skill itself here: only {{Name}}'s preferences and examples.
- Link each skill to the process or drain it relates to in [[Context/processes]].
