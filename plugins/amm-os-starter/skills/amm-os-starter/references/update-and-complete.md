# Update and Move to Complete

Two modes for an existing folder. Both show their changes before touching anything and never delete or rewrite what the person wrote unless they approve it.

## Update (re-run the interview)

Use when the person wants to refresh their information ("update my second brain", "my offers changed").

1. Read the root `CLAUDE.md` and the `Context/` notes, so the questions only cover what is missing or what changed.
2. Run the interview from `interview-rounds.md`, but tell the person up front that their existing answers are kept: "I already have your answers. Tell me only what changed or what is missing."
3. For each note, compare the new answers with the current text. Show a short summary: what would be added, what would fill a `[TO COMPLETE]`, what would change (old value and new value side by side). Ask for a yes.
4. Apply only what is approved. Update `sources` (add `update-interview`), `updated` (only in notes whose content changed), `index.md` and the journal (Complete), then redo `brief.md`.

## Move to Complete

Use when an Essential folder should become Complete ("move to Complete", "add projects and a journal").

1. Announce in one short message what will be added: `index.md`, `Projects/`, `Journal/`, `Decisions/`, `Resources/` (with `sources/`), `Skills/`, `Archive/`. Ask for a yes.
2. Create the missing folders, each with its `CLAUDE.md` from `folder-claude-md.md`. `Archive/` is created empty.
3. Projects: if `Context/goals.md` has a "Current projects" table, create `Projects/{slug}/README.md` for each row from `project-readme.md`, using only what the table says. Then replace the table in `goals.md` with a list of `[[Projects/{slug}/README]]` links with one sentence each (as the Complete section of `context-goals.md` shows).
4. Root `CLAUDE.md`: restore the Complete-only lines that Essential removed (startup steps for `index.md` and the journal, the table rows, rules 13 to 15), remove the sentence saying the Complete level adds folders, and set `skill_version` to the current version.
5. `index.md`: write it from the notes that now exist (see `index-md.md`). `.claudeignore` and `AGENTS.md` already fit both levels; add to `AGENTS.md` the line about `index.md` if it is missing.
6. Documents the person provided earlier were only cited, not copied. If they are still available, offer to copy them into `Resources/sources/`. Do not copy any that hold sensitive data.
7. Journal: write today's note from `journal-note.md`, recording the move.
8. Run the checks of Step 5 in `SKILL.md` and report the result.
