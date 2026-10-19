# Upgrade mode

Current skill version: **2.0.0**. The person's folder carries its version in the frontmatter of the root `CLAUDE.md`: `skill_version: 2.0.0`.

Principle: an upgrade **adds** what the new version brings. It deletes nothing, does not rewrite the person's content, and never touches the "User corrections" section.

## Procedure

1. Read the folder's version. If it equals the current version, say in English that everything is up to date.
2. If the field is missing or starts with `1.`, the folder was built by a 1.x version: see "From 1.x" below.
3. Otherwise, announce what will be added (list below, adapted to the folder's level) and ask for a yes.
4. Apply only the additions. Insert the missing lines in existing files instead of regenerating them. Do not change the `updated` field of a `Context/` file when you only add technical information such as `sources`: its content did not change, and a misleading date would make `brief.md` look late.
5. Set `skill_version` last, to the current version.
6. At the Complete level, add a line to today's journal: "Upgrade from version X to version Y".
7. Run the checks of step 5 of the skill and report the result.

## From 1.x (French folders)

Versions 1.x used a different folder and file naming and were never part of a public release. Version 2.0.0 renamed the structure, so these folders are **not upgraded automatically**. Offer the person to rebuild: run the interview again (their old files stay untouched where they are), or paste the old files as starting documents so the interview only asks what is missing.

## For future versions

Add a section "From X to Y" with the additions, and update the current version at the top of this file and in `SKILL.md`.
