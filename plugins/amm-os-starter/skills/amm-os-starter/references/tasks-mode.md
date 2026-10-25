# Tasks mode

Tasks turn the owner's goals into work an AI crew can prepare. Four things to do: add a task, show the board, work the next task, and handle the owner's review. Everything lives in `Tasks/` inside the Complete-level Second Brain. In an Essential folder, say that tasks come with the Complete level and offer "move to Complete".

Everything said to the owner is in English, with no em dash and no emoji. Use `task-note.md` for the file shape and the log line format.

## The crew

Three agents ship with this plugin. They are read-only: they return text, and the main assistant writes every file.

| Agent | Role | Tools |
|---|---|---|
| Writer | Drafts texts in the owner's style from the notes | read files |
| Researcher | Finds public facts, with sources and confidence | read files, web search |
| Checker | Reviews a draft against the owner's rules | read files |

Delegate to a crew agent as a real sub-agent when sub-agents are available (the agent names are `writer`, `researcher`, `checker` in this plugin). If they are not available, play the role yourself and log the mode as `inline`. Never log `sub-agent` unless a sub-agent really ran. The board shows the mode, so the owner can see which it was.

## Hard rules

1. **Draft only.** Never send, publish, post or schedule anything. Never change a file outside `Tasks/` (and `board.html` at the root). The result of a task is a draft inside the task file. The one exception: after the owner approves a task, you may offer to save the text in `Resources/templates/`, and you save it only if the owner says yes.
2. **Only the owner closes a task.** Only the owner moves a task from `review` to `done`. Do it only when the owner says so in this conversation.
3. **Ready needs a definition of done.** A task may be `ready` only if "Done when" lists at least one condition. If it does not, ask the owner for one before marking it ready.
4. **One task per run.** Work one task, then stop and report.
5. **Log every step**, with the format in `task-note.md`. The log is append only.
6. **No private data.** Tasks, logs and drafts never hold a national ID, bank details, passwords or personal data about clients. Use client types or anonymised cases.
7. **Never invent.** Missing facts become `[TO COMPLETE]` in the draft, and are listed for the owner.
8. After each action you finish (adding a task, a work run, the owner's answer), rebuild the board if `board.html` exists (see "Show the board"). Do not rebuild it after every single log line.

## Add a task

Triggers: "add a task", "new task", "put this on my list".

1. Take the sentence the owner gave as "What is wanted". Ask at most two questions, only for what is missing: what does "done" look like, and is there a deadline. If the owner skips them, create the task as `backlog`. Unless the owner says otherwise, priority is `normal` and owner is `agent`.
2. Offer the goals from `Context/goals.md` as a short list and ask which one the task serves. Write the goal as it appears in that note, or `[TO COMPLETE]`.
3. Find the next id: list `Tasks/T-*.md`, take the highest number, add one, write it with four digits. The file name is `T-NNNN-short-title.md`.
4. Write the file from `task-note.md`. If the owner gave no condition, write `- [TO COMPLETE]` as the only bullet under "Done when": it does not count as a condition. Set the status to `ready` only if "Done when" has a real condition and the owner asked for the task to be ready (or says "mark it ready" afterwards: then set `ready` and log `ready`). Otherwise use `backlog`. Add the log line `created` (and `ready` if relevant) with Agent `You` and mode `you`.
5. Tell the owner the id, the status and what happens next. Rebuild the board if `board.html` exists; if it does not, offer once to create it ("show the board").

## Show the board

Triggers: "show the board", "show my tasks", "what are my agents doing".

1. If `Tasks/` has no task, say so and offer to add one.
2. Run `scripts/board.py "<folder>"` from this skill (path relative to the skill's base directory) if Python 3 is available (`python3 --version`, or `python --version` reporting 3.x). It reads the task files and writes `board.html` at the root of the Second Brain, using `references/board-template.html`.
3. If Python 3 is not available, build it by hand: read the tasks, build the JSON described in the docstring of `scripts/board.py`, replace the `__DATA__` marker in `references/board-template.html`, and save it as `board.html`.
4. Reply with the counts per status, then what needs the owner now: tasks in `review`, overdue tasks, blocked tasks. Say how to open it: "double-click board.html in your folder; tick Auto-refresh if you want it to update while the crew works".
5. Say once that the board is a snapshot that is rebuilt after every task change, and that the Crew panel shows what was logged.

## Work the next task

Triggers: "work the next task", "do the next task", "run my tasks".

1. **Pick.** Among tasks with status `ready`, take the highest priority (high, normal, low), then the earliest due date, then the lowest id. If none is ready, say so and list tasks in `backlog` that lack a definition of done. Never start a `backlog` task.
2. **Start.** Set the status to `in-progress` and `updated` to today. Log `Claude | main | started`.
3. **Research (only if needed).** Needed when the task says "find out" or "check", or when the draft needs a public fact that no note holds. Otherwise skip it and say so in the log note. When needed, delegate to the Researcher. Log `Researcher | sub-agent or inline | started`, then `finished` with one line of what it found.
4. **Draft.** Delegate to the Writer with the task text, the folder path and the notes listed under "Context to use". Log `Writer | sub-agent or inline | started`, then `finished`.
5. **Check.** Delegate the draft to the Checker with the task, the "Done when" conditions and the folder path. Log `Checker | sub-agent or inline | started`, then `finished` with the verdict. If the verdict is FAIL or PASS WITH EDITS, send the draft back to the Writer once with the issues, then check again. Stop after one revision and report what is still open.
6. **Save.** Write the draft under `## Result (draft)`, followed by the Checker's verdict and any gaps (`[TO COMPLETE]`). Set the status to `review`. Log `Claude | main | review`.
7. **Report.** Show the draft, the Checker's verdict and the gaps, in a form the owner can read in one minute. Ask: approve, change something, or block.

If anything prevents the work (a missing note, a needed fact that cannot be found), set the status to `blocked`, log `blocked` with the reason, and tell the owner what is needed.

## Handle the owner's answer

- **Approve** (the owner says it is fine): set `done`, `updated` today, log `You | you | approved`. Offer, in one sentence, to save the text in `Resources/templates/` if it could be reused (rule 15 of the root `CLAUDE.md`).
- **Change** (the owner asks for edits): log `You | you | changes | what they asked`, set the status back to `in-progress` (the `changes` line records why), redo steps 4 to 6 with their request, replace the draft under `## Result (draft)` with the revised one (the log keeps the history), then ask again.
- **Block** (the owner stops it): set `blocked`, log `blocked` with their reason.
- **Unblock** (the owner says it can go again): set `ready`, log `unblocked`.

After each change, rebuild the board.
