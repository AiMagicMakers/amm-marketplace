---
name: amm-os-starter
description: This skill should be used when the user asks to "build my second brain", "set up my second brain", "set up AMM OS", or "create my AI memory folder", or wants to turn what they know about their business into Markdown files any AI can read. It interviews the user in three short rounds and writes a folder of notes. It also manages an existing Second Brain folder: "check my second brain", "add this document to my second brain", "show my second brain map", "update my second brain", "upgrade my second brain".
---

# AMM OS Starter

Build the user's "Second Brain": a folder of plain Markdown files holding who they are, what they sell, who their clients are, how they write and how they work. Any AI agent can read it (Claude Cowork project, Claude Code, or ChatGPT/Gemini through a one-page `brief.md`). It also opens in Obsidian if the user likes, but nothing depends on it.

All `references/` and `scripts/` paths in this file are relative to this skill's base directory (the folder that contains this SKILL.md), not to the user's folder.

The users are entrepreneurs, freelancers and SMB owners, mostly in Morocco, often non-technical. They are AMM (AI Magic Makers) participants. Keep every interaction simple and warm.

## Language and tone

- Everything is in English: your messages, the questions, the generated files, the file and folder names. Use plain words and short sentences. Address the user as "you". If you must use a technical term (Markdown, root folder), explain it in one short phrase the first time.
- Moroccan context: amounts in DH excl. VAT with 20% VAT added on top, cities like Casablanca, Rabat, Marrakech, Tangier, typical tools like WhatsApp Business, Instagram, Facebook, Google Business Profile, Excel, Sage/Ciel, Canva. Use these only as prompts to jog memory. Never assume the user uses them.
- Do not use US startup framing (funding rounds, OKR vocabulary, venture talk). Use "goals for the year", "clients", "quotes", "services".

## Hard rules for everything you write

1. **Never invent.** No prices, figures, results, client names, testimonials, dates or tools the user did not give. If a fact is missing, write `[TO COMPLETE]` in its place. Do not silently delete the section and do not guess.
2. **Fill templates with the user's own words.** The files in `references/` are scaffolds that show structure. Replace every `{{...}}` marker and every guidance sentence with real content from the interview. Keep their exact phrases, numbers and wording where possible.
3. **No em dashes and no en dashes, anywhere**, in chat or in files. Use a period, a comma, a colon or a normal hyphen. **No emojis.**
4. **Standard Markdown only**, plus YAML frontmatter and `[[wikilinks]]`. No callouts, no embeds, no app-specific syntax.
5. **Frontmatter on every note**: `type`, `updated` (today, `YYYY-MM-DD`), `tags` (2 or more specific tags). Every note in `Context/` (not its `CLAUDE.md`) also has `sources`: where its facts come from (`initial-interview`, plus the name of each document or link actually used). Never invent a source. Take today's date from the system (for example `date +%F`) or from the session.
6. **Wikilinks use the folder path** so they resolve when several files share a name: `[[Context/identity]]`, `[[Projects/project-name/README]]`. Weave them into sentences. Never use them to link to a `CLAUDE.md`. Catalogue lists (`index.md`, journal entries) may hold one link per line.
7. **File and folder names are lowercase with hyphens and no accents** (`offers-and-prices.md`), except the top folder, which is `Second Brain - {Name}`.
8. **Sensitive data stays out.** Never store a national ID (CIN), bank details (RIB), passwords, API keys, or personal data about the user's clients (names of private individuals, phones, emails, addresses). If the user pastes some, do not write it into any file, and tell them in one friendly sentence that you left it out and why. Use client types or anonymised cases instead ("a transport SMB in Casablanca").
9. **Legal**: `rules.md` carries a short reminder about Moroccan law 09-08 (protection of personal data, CNDP). It is a reminder, never legal advice.
10. **Never delete or overwrite** an existing file without showing the user and getting a yes.
11. **Originals are untouched.** Files in `Resources/sources/` are copies of documents the user provided. Never edit them. Summaries go in separate notes that cite them in `sources`.
12. **One marker per empty section.** If the person gave nothing for a whole section, or several details of one section are missing, write the gap once, on one line (`Missing: problem solved, payment terms [TO COMPLETE]`), not one marker per bullet or table cell. Never invent to avoid a marker.
13. **Answers cite their file.** When answering from the brain, name the file used and flag what is missing or stale (this rule is also written into the generated root `CLAUDE.md`).

## Version

Current skill version: **2.1.0**. Write `skill_version: 2.1.0` in the frontmatter of the generated root `CLAUDE.md`. When a release changes what the skill generates, bump the number in all of these places: this section, `references/upgrade.md`, `references/root-claude-md.md`, `.claude-plugin/plugin.json` and `CHANGELOG.md`; then add an upgrade section to `references/upgrade.md`. If a folder's version is newer than the skill's, tell the user to update the skill and change nothing.

## Levels

| Level | What is created |
|---|---|
| **Essential** (default) | Root files (`CLAUDE.md`, `AGENTS.md`, `brief.md`, `.claudeignore`) + `Context/` (its `CLAUDE.md` + 8 context files) |
| **Complete** | Everything in Essential + `index.md` (catalogue of all notes) + `Projects/`, `Journal/`, `Decisions/`, `Resources/` (with `sources/`), `Skills/`, `Archive/` |

In Essential, current projects go into a section of `Context/goals.md` and drains go into `Context/processes.md`. In Complete, each project also gets its own folder with a `README.md`.

## Flow

### Step 0. Preflight

1. Work out the destination: the folder selected in Cowork, or the current directory in Claude Code. Look there (and in the current directory itself) for folders named `Second Brain - *`. If unclear, ask where to create it (one question).
2. The top folder is named `Second Brain - {Name}`.
3. If the user asked for Check, Add a document, Show the map, Update, Move to Complete or Upgrade and no `Second Brain - *` folder is found, say so and offer to build one. If several are found, ask which.
4. If that folder already exists, do not start over. Read its root `CLAUDE.md` (level and `skill_version`), then offer: **Update** and **Move to Complete** (see `references/update-and-complete.md`), **Check** (health report, see "Check mode"), **Add a document** (see "Add mode"), **Show the map** (see `references/map-mode.md`), **Upgrade** (only if its `skill_version` is older than the current one, see "Upgrade mode"), or **Cancel**. If the user's first message already names one of these, go straight to it.

### Step 1. Quick intake (one short exchange)

Ask in a single message, or with AskUserQuestion when available:

- The person's first name.
- Level: Essential (default, about 20 minutes) or Complete (about 40 minutes). If they hesitate, pick Essential and say they can upgrade later.
- Optional: do they have an existing document to start from, for example a sales brief, a presentation, a website, a LinkedIn or Instagram page? Accept paths and links.

Do not ask anything else before the interview.

### Step 2. The interview, 3 rounds

Read `references/interview-rounds.md` now. It holds the exact questions, the orienting message, the widget form and the plain-chat format.

- **Runtime check.** If the tool `mcp__visualize__show_widget` is available (Cowork), render each round as one form widget. Call `mcp__visualize__read_me` first and silently. If the widget call errors, or in Claude Code and other tools, post the same round as a plain chat block and wait for the reply.
- Send the orienting message first, then Round 1, then Round 2, then Round 3. One round at a time.
- Round 1: You and your business. Round 2: Clients and style. Round 3: How you work.
- The user may type, dictate (paste a voice transcript), paste links, or point to files. All of it is welcome. A blank category is a skip.
- **Do not drill down** between rounds. No follow-up questions, no commentary (the one exception: a kind one-sentence note when sensitive data was left out). Ingest and move on. If the user types "next", skip the current round. If they type "skip", stop asking and build with what you have.
- After Round 3, ask once, in one line, whether they want to add any other link or file. Then build.

### Step 3. Ingest

Build a working corpus tagged by target file (identity, offers, clients, style, processes, tools, goals, projects, drains).

- Links: fetch them (WebFetch or equivalent) and extract only what is relevant.
- Files: read `.md`, `.txt`, `.csv`, `.json` directly; `.pdf` with page ranges if long; `.docx`, `.pptx`, `.xlsx` with `pandoc` or `textutil` if available, otherwise ask for a PDF export; images by looking at them.
- Keep the user's exact words for style, client language, and "why clients choose me". These go in quotes in the files.
- Apply rule 8 (sensitive data) while ingesting.
- Complete level only: copy each local file the user provided into `Resources/sources/` unchanged (keep its name, lowercased with hyphens if needed). Skip, and say so in one sentence, any file that contains sensitive data under rule 8. Links are not copied: cite their address in `sources` instead. In Essential, nothing is copied, but documents used are still named in `sources`.
- Note, for each corpus fact, which document or link it came from, so the `sources` field of each `Context/` file is accurate.
- Tell the user in one line what you pulled ("I read 3 files and 2 links."), then build.

### Step 4. Build

Work silently, without narrating each file. Create folders first, then files, in this order. For every file, read its scaffold from `references/` and write only what lies between its `FILE START` and `FILE END` markers, filled in. `index.md` is written after all notes exist, and `brief.md` last.

| # | Path in `Second Brain - {Name}/` | Scaffold | Level |
|---|---|---|---|
| 1 | `Context/identity.md` | `context-identity.md` | both |
| 2 | `Context/offers-and-prices.md` | `context-offers-and-prices.md` | both |
| 3 | `Context/clients.md` | `context-clients.md` | both |
| 4 | `Context/style.md` | `context-style.md` | both |
| 5 | `Context/processes.md` | `context-processes.md` | both |
| 6 | `Context/tools.md` | `context-tools.md` | both |
| 7 | `Context/goals.md` | `context-goals.md` | both |
| 8 | `Context/rules.md` | `context-rules.md` | both |
| 9 | `Context/CLAUDE.md` | section "Context" in `folder-claude-md.md` | both |
| 10 | `CLAUDE.md` (root) | `root-claude-md.md` | both |
| 11 | `AGENTS.md` | `agents-md.md` | both |
| 12 | `.claudeignore` | `claudeignore.md` | both |
| 13 | `Projects/CLAUDE.md` and `Projects/{slug}/README.md` per project | section "Projects" + `project-readme.md` | Complete |
| 14 | `Journal/CLAUDE.md` and `Journal/{today}.md` | section "Journal" + `journal-note.md` | Complete |
| 15 | `Decisions/CLAUDE.md` | section "Decisions" + `decision-note.md` | Complete |
| 16 | `Resources/CLAUDE.md`, plus the folder `Resources/sources/` (filled in Step 3) | section "Resources" | Complete |
| 17 | `Skills/CLAUDE.md` | section "Skills" | Complete |
| 18 | `Archive/` (empty folder, no file) | none | Complete |
| 19 | `index.md` (written after all notes exist) | `index-md.md` | Complete |
| 20 | `brief.md` (written last) | `brief-md.md` | both |

Per-file notes:

- **Essential root `CLAUDE.md`**: keep only the routing rows and startup steps for folders that exist. Remove the Complete-only rows and add one line saying that the Complete level adds Projects, Journal, Decisions, Resources, Skills and Archive.
- **Projects**: one folder per project the user named, slug in lowercase hyphens. Create a `README.md` only. No empty subfolders.
- **Journal**: today's note records that the Second Brain was created, which files exist, and the list of `[TO COMPLETE]` to finish. Other days are created later by the assistant.
- **Drains** (Round 3): write each as the five-part template described in `context-processes.md`: When X happens, I do Y, it takes Z, the result is W, I want V. A missing part is `[TO COMPLETE]`. Do not propose automations the user did not ask for, but you may add one line "Idea" under a drain if it is obvious and clearly marked as a suggestion.
- **`brief.md`**: condense the filled Context files into one page of about 350 to 450 words, no wikilinks, ready to paste at the start of a ChatGPT or Gemini chat. Take facts only from the files you just wrote.
- **`index.md`**: one line per note, each line saying what question the note answers, drawn from the note's real content. Do not list `CLAUDE.md` files, `AGENTS.md`, `brief.md`, `graph.html` or the index itself.
- **`sources` field**: for each `Context/` file, list `initial-interview` plus only the documents or links that actually fed it. A file built only from the interview gets `[initial-interview]`.
- **`folder-claude-md.md`** contains one section per folder. Each `## Section: X` becomes that folder's `CLAUDE.md` (without the heading line, with frontmatter added). Update the file table to match the files that actually exist.
- **Corrections section**: the root `CLAUDE.md` always ends with the "User corrections (permanent rules)" section, empty at first. Keep it, never remove it.

### Step 5. Verify before reporting

Run these checks and fix what fails:

1. Search the new folder for the characters U+2014 and U+2013, excluding `Resources/sources/` (untouched originals) and `graph.html`: zero hits. Use the search tool, or read the files if no shell is available.
2. Search the same files for `{{` and for leftover `FILE START` or `FILE END` markers: zero hits.
3. Every `[[wikilink]]` outside inline code points to a file that exists. Example wikilinks inside backticks are fine.
4. Every `.md` file has frontmatter with `type`, `updated`, `tags`, and every note in `Context/` (not its `CLAUDE.md`) also has `sources`. The root `CLAUDE.md` has `skill_version: 2.1.0`. `.claudeignore` lists `graph.html`.
5. Complete only: every note appears in `index.md` and every index line points to an existing file.
6. No file contains a national ID, bank details, password or private client contact. Include `Resources/sources/` in this scan (a document that fails it must not be copied there), and skip `graph.html`.
7. Count the `[TO COMPLETE]` per file for the final report. Ignore the files where the marker only appears as a rule description (both `CLAUDE.md` levels, `AGENTS.md`, `Context/rules.md`) and the unfilled-journal mention.
8. No emoji (same files as check 1).

### Step 6. Final message (short)

Give:

- The tree of what was created (folders and files, one line each).
- How many `[TO COMPLETE]` remain and in which files, in plain words.
- How to use it, 4 lines: **Claude Cowork** (create a project, add this folder, say "read CLAUDE.md"), **Claude Code** (open a terminal in the folder, run `claude`), **Obsidian** (optional: "Open folder as vault"), **ChatGPT or Gemini** (paste `brief.md` at the start of the chat).
- One suggested next step, for example completing the most important `[TO COMPLETE]` or testing with a real task ("write me a follow-up message for a quote with no reply").
- If the level was Essential, one line: they can run the skill again later to move to Complete.
- One backup line: the folder lives only on their computer, so copy it now and then to a cloud drive or a USB key (a plain copy of the folder is enough).
- One line of later options: they can say "check my second brain" for a health report, "add this document to my second brain" for a new quote template, price list or brief, and "show my second brain map" for a clickable map of their notes.

## Check mode

Read `references/verify.md` and follow it. It is read-only until the user approves fixes. It checks links, index, missing information, contradictions (prices, offer names, tone), stale notes, sync between `brief.md` and `Context/`, privacy, form rules and version, then reports and proposes fixes.

## Add mode

Read `references/add-document.md` and follow it. It brings a new document into an existing folder: keep the original in `Resources/sources/` (Complete), propose the changes note by note, show both values when the document contradicts something already written, apply only what the user approves, then update `sources`, `index.md`, the journal and `brief.md`. Never guess a missing fact.

## Map mode

Read `references/map-mode.md` and follow it. It builds `graph.html` at the root of the user's folder: a self-contained, no-install map of the notes, their links, what is missing and what is unlinked. It is a generated file, listed in `.claudeignore`, and not a note.

## Upgrade mode

Read `references/upgrade.md` and follow it. It only adds what a newer version brings, after the user says yes, and never removes or rewrites their content or their corrections. It sets `skill_version` last.

## After setup

The day-to-day behaviours (saving corrections as permanent rules, updating the matching `Context/` note and `brief.md`, keeping `index.md` in sync, citing the file used) are written into the generated root `CLAUDE.md`. Do not repeat them here.
