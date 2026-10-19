# Map mode

Builds `graph.html` at the root of the user's folder: one self-contained page (no install, no network, opens with a double-click) showing every note as a point, wikilinks as lines, folders in colours, a red ring on notes that still hold `[TO COMPLETE]`, a dashed ring on notes with no link, search, and a side list of what to look at. It works at both levels.

It is a generated file: it is listed in `.claudeignore` so assistants never read it, and it is not a note (not in `index.md`, not checked by Check mode). Originals in `Resources/sources/` are not shown as notes.

## Steps

1. Locate the folder (same way as Step 0 of `SKILL.md`). Ask nothing else.
2. If Python 3 is available (`python3 --version`, or `python --version` reporting 3.x), run `scripts/graph.py "<folder>"` from this skill (path relative to the skill's base directory). It reads the notes, resolves `[[wikilinks]]`, and writes `graph.html` using `references/graph-template.html`. Use the command that exists on the machine.
3. If Python 3 is not available, build it by hand: collect the notes (all `.md` files except `CLAUDE.md`, `AGENTS.md`, `brief.md`, `index.md` and anything under `Resources/sources/`), build the JSON described in the docstring of `scripts/graph.py`, replace the `__DATA__` marker in `references/graph-template.html` with that JSON, and save the result as `graph.html` in the user's folder.
4. Reply with one line of numbers (notes, links, to complete, unlinked), then how to open it ("double-click graph.html in your folder, it opens in your browser"), then what to look at first: the red rings (missing information) and any dashed note (no links), naming the two or three most important ones.
5. Mention once that the picture is a snapshot: to refresh it after changes, say "show my second brain map" again.

Never write the user's data anywhere except `graph.html` in their own folder. The page makes no network request.
