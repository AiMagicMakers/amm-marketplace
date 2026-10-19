# Add mode

Bring new information into the Second Brain without damaging it. Triggers: "add this document to my second brain", "I have a new quote template", "update my prices with this file", "add this to my second brain". The person gives a file, a link or pasted text. Everything said to them is in English, with no em dash and no emoji.

## Steps

1. **Read the document.** File, link (fetch it) or pasted text. If the document contains a national ID, bank details, a password or contact details of private clients, do not copy or keep any of it and say so in one sentence.
2. **Keep the original (Complete level).** Copy the file as it is into `Resources/sources/`, without modifying it. A link or pasted text is not copied: cite its address or title in `sources`. In Essential, nothing is copied, but the document is cited in `sources`.
3. **Find where each piece of information goes.** For each useful fact, find the matching note in `Context/` (or the project) using the index or the `CLAUDE.md` table. Ignore what is not useful to the person's business.
4. **Propose before changing.** Present a short summary: for each note, what would be added, what would fill a `[TO COMPLETE]`, and what would be modified (old value and new value side by side). Ask for a yes.
   - If the document contradicts something already written (a different price, for example), do not choose: show both values and their sources, and let the person decide.
   - A value the person said is not set yet (for example "no fixed price yet") counts as missing, not as a contradiction: the document fills it.
   - Never guess information that is absent from the document.
5. **Apply only what is approved.**
   - Modify the notes as little as possible, using the document's words when they are good.
   - Add the document to the `sources` field of each note touched.
   - Update `updated` only in notes whose content changed.
   - Complete level: add the document's line to `index.md` (and the line of any new note), and a line to today's journal.
   - If a conflict stays unresolved, write one line `Open question: ...` next to the value in the note, naming both values and the source file, and record it in today's journal (Complete). Remove the line once the person decides.
   - If `Context/` changed, redo `brief.md`.
6. **Reply.** In a few lines: what was added and where, what remains to decide or complete. Suggest "check my second brain" if several notes changed.

## Rules

- A document that brings nothing new: say so, and change nothing.
- Several documents: handle them one by one, with one proposal per document.
- Never overwrite information the person gave themselves without their confirmation.
