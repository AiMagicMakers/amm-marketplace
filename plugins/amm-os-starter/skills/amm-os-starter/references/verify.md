# Check mode

Health check of an existing Second Brain. Triggers: "check my second brain", "review my second brain", "how healthy is my second brain". It is read-only: nothing is modified before the person has said yes. Everything written to the person is in English, with no em dash and no emoji.

## Steps

1. Find the folder `Second Brain - {Name}` and read its root `CLAUDE.md` (level, `skill_version`).
2. Run the checks below with the search tool, `grep`/`find` if a shell is available, or by reading the files. Do not open the files listed in `.claudeignore`, and skip `graph.html`. Files in `Resources/sources/` are untouched originals: leave them out of checks 9 and 11 and of the notes and index checks, but keep them in check 10 (privacy).
3. Present the report (format below). Nothing is modified at this stage.
4. Ask which of the proposed fixes the person wants to apply.
5. Apply only those. Update `updated` in the files touched, the index (Complete) and `brief.md` if `Context/` changed. At the Complete level, if any fix was applied, note it in today's journal.

`graph.html` is a generated file, not a note: do not open it, do not count it in the checks. If it exists and notes are newer than it, offer to regenerate it ("show my second brain map").

## Checks

| # | Check | How | Level |
|---|---|---|---|
| 1 | Broken links | Every `[[link]]` outside code points to an existing file (for a link to a PDF or another file, with its extension, check the file itself) | all |
| 2 | Orphan notes | A note that neither the index nor any other note links to | Complete |
| 3 | Index up to date | Every note is in `index.md`, every index line points to an existing file, every line says what question the note answers, and no index description contains a price or other figure | Complete |
| 4 | Missing information | Number of `[TO COMPLETE]` per file, ranked by importance: offers-and-prices, identity, clients, style first | all |
| 5 | Contradictions | Prices in DH, offer names and tone (formal or friendly) are identical across `offers-and-prices.md`, `brief.md`, `style.md` and project notes. Also list every `Open question` line still left in a note | all |
| 6 | Stale notes | `updated` older than 90 days, especially `offers-and-prices.md` and `goals.md`; also a "Prices valid as of" date older than 90 days, in which case ask the person to confirm the prices are still current | all |
| 7 | Brief in sync | The facts in `brief.md` are the same as in `Context/`, and `brief.md` is not older than the most recent `Context/` file | all |
| 8 | Goals and projects | Every project serves a goal, every goal has at least one project | Complete |
| 9 | Frontmatter | `type`, `updated`, `tags` everywhere, and `sources` in every note of `Context/` (not its `CLAUDE.md`) | all |
| 10 | Confidentiality | No national ID, bank details, password, email or phone of a private individual. `.claudeignore` exists | all |
| 11 | Form rules | No em dash or emoji, no leftover `{{` | all |
| 12 | Version | The folder's `skill_version` compared with the current skill version (see `upgrade.md`) | all |

Hints for check 10 (clues, not proof: always confirm by reading the line; the CIN pattern is noisy and matches many harmless codes). Run them from the folder root, excluding `graph.html` and anything listed in `.claudeignore`:

```
grep -rnE '\b[0-9]{24}\b' .                          # possible RIB
grep -rnE '\b[A-Z]{1,2}[0-9]{5,6}\b' .               # possible CIN
grep -rnE '(\+212|0)[5-7][0-9]{8}' .                 # Moroccan phone number
grep -rnE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}' .   # email
grep -rniE 'password|passcode' .                     # password
```

Never copy the value found into the report: give only the file and the line.

## Report format

```
# Check of {Name}'s Second Brain, {date}

Overall state: {In good shape | Needs attention | Needs fixing}

| Check | Result | Detail |
|---|---|---|
| Links | {OK or N problems} | {files concerned} |
| ... | ... | ... |

## What I propose to fix

1. {Fix, in one plain sentence, with the file concerned}
2. ...

## What only you can complete

- {file}: {missing information}

Do you want me to apply fixes 1 to N, or only some of them?
```

Report rules:
- "In good shape": no confidentiality problem and no contradiction, fewer than 5 `[TO COMPLETE]`. "Needs fixing": at least one confidentiality problem, contradiction or broken link. Otherwise "Needs attention".
- A contradiction is presented with both values and their files, never with a choice made for the person.
- Missing information stays `[TO COMPLETE]`: it is not guessed.
- Never delete a rule from the "User corrections" section.
