Scaffold of a task in `Tasks/` (Complete level). One file per task, named `T-0001-short-title.md` (lowercase, hyphens). The next id is the highest existing id plus one, written with four digits.

Status values: backlog, ready, in-progress, review, done, blocked. A task may be `ready` only if the "Done when" section lists at least one real condition. If the owner gave none, the only bullet is `- [TO COMPLETE]`, which does not count. Defaults: priority `normal`, owner `agent`.

Log line format (one line per event, append only, never edited):
`- YYYY-MM-DD HH:MM | Agent | mode | event | note`
- Agent: You, Claude, Writer, Researcher, Checker.
- mode: you (the owner did it), main (the main assistant did it), sub-agent (a real sub-agent did it), inline (the main assistant played the role itself because no sub-agent was available).
- event: created, ready, started, finished, review, approved, changes, blocked, unblocked, note.
Get the date and time from the system (for example `date "+%Y-%m-%d %H:%M"`). Never invent a mode: write `sub-agent` only if a sub-agent really ran.

FILE START

---
type: task
id: {{T-0001}}
title: {{short title}}
status: {{backlog, ready, in-progress, review, done or blocked}}
priority: {{high, normal or low}}
due: "{{YYYY-MM-DD, or empty}}"
goal: "{{the goal this task serves, as written in Context/goals.md, or [TO COMPLETE]}}"
owner: {{you or agent}}
updated: {{date}}
tags: [task, {{topic}}]
---

# {{Title}}

## What is wanted

{{One to three sentences, in the person's words.}}

## Done when

- {{a condition that can be checked}}

## Context to use

- [[Context/style]]
- {{other notes that matter for this task}}

## Log

- {{YYYY-MM-DD HH:MM}} | You | you | created | {{how the task was created}}

## Result (draft)

Nothing yet.

FILE END
