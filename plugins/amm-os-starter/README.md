# AMM OS Starter: your Second Brain

## What it is

AMM OS Starter is a skill for Claude. It asks you questions in 3 short steps, then builds a folder of simple files for you: **your Second Brain**.

In that folder, AI finds what it needs to know about you: who you are, what you sell and at what price (in DH), who your clients are, how you write, how you work. Afterwards, when you ask for a quote, a WhatsApp message or a post, AI no longer starts from zero.

These are plain text files (Markdown format). Nothing else to install, nothing hidden, and everything stays on your computer.

## Two levels

| Level | What you get | Time |
|---|---|---|
| **Essential** (default) | The base files (`CLAUDE.md`, `AGENTS.md`, `brief.md`, `.claudeignore`) and the `Context/` folder with 8 notes | about 20 minutes |
| **Complete** | Essential, plus a catalogue of all your notes (`index.md`), `Projects/`, `Journal/`, `Decisions/`, `Resources/` (with your original documents), `Skills/` and `Archive/` | about 40 minutes |

You can start with Essential and move to Complete later, without losing anything.

## Installation

### Option 1: from the AMM marketplace (recommended)

In Claude Code:

```
/plugin marketplace add AiMagicMakers/amm-marketplace
/plugin install amm-os-starter@amm-marketplace
```

In the Claude desktop app or Cowork, open **Customize** and add the marketplace `AiMagicMakers/amm-marketplace` if your version offers it. The marketplace page has the details and the update steps.

### Option 2: upload the ZIP

1. Download `amm-os-starter-vX.Y.Z.zip` from the Releases page of the marketplace repository. Do not unzip it.
2. Open Claude (the app or claude.ai).
3. Go to **Customize** and add a plugin (or skill) with **Upload ZIP**. Select the ZIP.
4. Check that **amm-os-starter** appears in the list and is turned on.

The ZIP is a Claude plugin: it has a `.claude-plugin/plugin.json` file at its root and the skill inside `skills/amm-os-starter/`. Do not add a folder around it.

## First run

In a Claude conversation, simply write:

> Build my second brain

You can also write "AMM OS" or "set up my second brain". Claude asks for your first name, the level (Essential or Complete) and where to create the folder. Then it asks the questions in 3 steps:

1. **You and your business**: who you are, what you sell, your offers and prices, why people choose you.
2. **Your clients and your style**: your typical client, their words, their problems, your tone, words to avoid, example texts.
3. **How you work**: your processes, your tools, your projects, your goals for the year, 1 or 2 tasks that weigh on you and that you would like to automate.

To answer, do as you like:

- type;
- dictate with the microphone of your phone or computer and paste the text;
- paste links (website, Instagram page, online document);
- point to files (presentation, quote template, sales brief).

Cannot answer a question? Skip it. Claude will write `[TO COMPLETE]` at that spot and you can come back later. It invents nothing.

**Never give**: national ID number (CIN), bank details (RIB), passwords, your clients' contact details. If you paste them by mistake, Claude does not record them.

## What you get

```
Second Brain - YourName/
  CLAUDE.md       the map: where each piece of information goes, and the rules
  AGENTS.md       a pointer to CLAUDE.md for other AI tools
  brief.md        the one-page summary, to paste into ChatGPT or Gemini
  .claudeignore   the list of what AI must not read
  index.md        the catalogue of all your notes (Complete)
  graph.html      the map of your notes, created on request
  Context/        identity, offers-and-prices, clients, style, processes,
                  tools, goals, rules
  Projects/       one folder per project              (Complete)
  Journal/        one note per working day            (Complete)
  Decisions/      decisions and their reason          (Complete)
  Resources/      prompts, templates, examples, and
                  sources/: your original documents   (Complete)
  Skills/         notes for your future skills        (Complete)
  Archive/        what is finished                    (Complete)
```

## Adding a document later

Do you have a new quote template, a price list or a brief? Say: **"add this document to my second brain"** and give the file. Claude reads the document, keeps the original in `Resources/sources/` (Complete level), then tells you what it proposes to change, note by note. If the document says something different from what is already written (a different price, for example), it shows you both versions and you choose. Nothing is modified before you agree.

## Seeing your Second Brain as a map

Tell Claude: **"show my second brain map"**. It creates a `graph.html` file in your folder. Double-click it: it opens in your browser, with nothing to install and no internet connection needed.

You see each note as a point, and the links between notes as lines.

- Colours show the folder (Context, Projects, Journal...).
- A **red** ring marks a note that still contains `[TO COMPLETE]`.
- A **dashed** ring marks a note with no link to the others.
- Click a point to see the note, what it contains and the notes linked to it.
- The search bar finds a note even without accents.

The map is a snapshot. After changes, ask for it again to refresh it.

**For the more technical: Graphify.** A free tool, Graphify, also produces an interactive graph from a folder of notes. We tested it on a demo folder: it reads the `[[...]]` links correctly and needs no AI for Markdown files. However, it creates one point per section title (about twenty notes give over a hundred points), does not flag what is missing, and needs Python and a terminal. So it is optional. If you are comfortable with a terminal: install it with `uv tool install graphifyy`, run `graphify install`, then in Claude Code type `/graphify .` in your folder.

## How to use it afterwards

### In Claude Cowork

1. Create a project in Cowork.
2. Add the folder `Second Brain - YourName` to the project.
3. Start the conversation with: "Read CLAUDE.md, then help me with...".

Claude reads the map, then the useful notes, and answers with your tone and your prices.

### In Claude Code

1. Open a terminal in the folder `Second Brain - YourName`.
2. Run `claude`.

Claude Code reads `CLAUDE.md` automatically at startup.

### In Obsidian (optional)

Obsidian is a free app for reading and browsing notes. It is not required.

1. Install Obsidian.
2. Choose **Open folder as vault** and select `Second Brain - YourName`.

You will see your notes and the links between them. The files stay the same: Claude works with or without Obsidian.

### In ChatGPT or Gemini

These tools do not read your folder. Open `brief.md`, copy all of its content and paste it at the start of the conversation, then make your request. When you change your `Context/` notes, ask Claude to redo `brief.md`.

## Keeping your Second Brain alive

- **Correct the AI, once.** If it writes a phrase you do not like, say so ("never say that again"). It adds it to the "User corrections" section of `CLAUDE.md` and remembers it afterwards.
- **Update as soon as things change**: new price, new offer, new tool. Just ask Claude to modify the note concerned.
- **Fill in the `[TO COMPLETE]`** when you have the information.
- **Move to Complete** when you want to track your projects and your journal: run the skill again on the same folder.
- **Do a check-up from time to time.** Say "check my second brain". Claude checks broken links, missing information, prices that differ from one file to another, notes that are too old and confidentiality. It gives you a report and changes nothing without your agreement.
- **Ask where an answer comes from.** Claude must always say which file it used and what is missing. If it does not, remind it.

## Backup and updates

- **Back up your folder.** It exists only on your computer. From time to time, copy it to an online space (Google Drive, OneDrive) or a USB key. A simple copy of the folder is enough.
- **Updating the skill.** When a new version is published, download the new ZIP and upload it again in **Customize**. Your folder is not touched.
- **Upgrading your folder.** Then say "upgrade my second brain". Claude tells you what will be added, you answer yes, and it adds only what is new: your offers, prices and texts stay as they are.

## Confidentiality

- Your files stay on your computer. Content is sent to the AI you use only when you ask it to read it.
- Never record a national ID (CIN), bank details (RIB), passwords or personal data about clients (name of a private individual, phone, email, address). To talk about a client case, anonymise ("a transport SMB in Casablanca").
- The `.claudeignore` file lists what AI must not read. Not every tool respects it, so the rule is also written in `CLAUDE.md`.
- The file `Context/rules.md` contains a reminder about Moroccan law 09-08 (protection of personal data, CNDP). It is a reminder, not legal advice.

## Frequently asked questions

**Do I need to know how to code?** No. You answer questions, Claude writes the files.

**Can I edit the files myself?** Yes, they are text files. Open them with any editor.

**What happens if I run the skill again?** It deletes nothing. It offers to update, to move to the Complete level, to check, to add a document, to show the map or to upgrade, and it shows you the changes before modifying an existing file.

**Are my prices and figures invented?** Never. Claude writes only what you give. The rest stays `[TO COMPLETE]`.

**The plugin does not appear, or the upload fails.** Check that you uploaded the original ZIP without unzipping it, and that it is turned on in **Customize**. Inside the ZIP, `.claude-plugin/plugin.json` must be at the top level.

---

AMM, AI Magic Makers. AI training for entrepreneurs and SMBs in Morocco.
