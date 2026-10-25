# Upgrade mode

Current skill version: **2.1.0**. The person's folder carries its version in the frontmatter of the root `CLAUDE.md`: `skill_version: 2.1.0`.

Principle: an upgrade **adds** what the new version brings. It deletes nothing, does not rewrite the person's content, and never touches the "User corrections" section.

## Procedure

1. Read the folder's version. If it equals the current version, say in English that everything is up to date.
2. If the field is missing or starts with `1.`, the folder was built by a 1.x version: see "From 1.x" below.
3. Otherwise, announce what will be added (list below, adapted to the folder's level) and ask for a yes.
4. Apply only the additions. Insert the missing lines in existing files instead of regenerating them. Do not change the `updated` field of a `Context/` file when you only add technical information such as `sources`: its content did not change, and a misleading date would make `brief.md` look late. When an upgrade section adds or rewrites real content (a rule, a dated price line, an index line), the note's content did change: update its `updated` field.
5. Set `skill_version` last, to the current version.
6. At the Complete level, add a line "Upgrade from version X to version Y" to today's journal. If there is no note for today, create one from `journal-note.md` and add it to `index.md`.
7. Run the checks of step 5 of the skill and report the result.

## From 2.0.0 to 2.1.0

Additions for all levels:

- In the root `CLAUDE.md`: add to rule 3 the sentence about the "Prices valid as of" line (see `root-claude-md.md`), and set `skill_version`.
- In `Context/offers-and-prices.md`: add the line `Prices valid as of: [TO COMPLETE]` under the VAT sentence. Do not invent a date. In your reply, ask the person whether the listed prices are still current, and if they say yes, set the line to today's date. An unresolved price conflict (for example an `Open question` line) does not stop you from dating the line: mention the open conflict in your reply.
- In `brief.md`: after the list of offers, add the line "Prices valid as of {date}." with the same date (or `[TO COMPLETE]`).

Additions for the Complete level:

- `index.md`: rewrite each description so that it says what question the note answers, as `answers "..."`, using only what the note really contains, in 20 words or fewer and with no prices or other figures. Keep the links unchanged.
- Root `CLAUDE.md`: update rule 13 (the index line says what question the note answers) and add rule 16 (offer a short journal entry after meaningful work).
- `Journal/CLAUDE.md`: add "What worked or failed" to the shape of a note and the sentence about offering a short entry after meaningful work.

Nothing else changes. The person's offers, prices and texts stay exactly as they are.

## From 1.x

Versions 1.x used a different folder and file naming and were never part of a public release. Version 2.0.0 renamed the structure, so these folders are **not upgraded automatically**. Offer the person to rebuild: run the interview again (their old files stay untouched where they are), or paste the old files as starting documents so the interview only asks what is missing.

## For future versions

Add a section "From X to Y" with the additions, and update the current version at the top of this file and in `SKILL.md`.
