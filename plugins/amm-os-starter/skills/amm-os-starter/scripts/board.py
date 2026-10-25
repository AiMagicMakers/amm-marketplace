#!/usr/bin/env python3
"""Generates board.html: a task board for a Second Brain.

Usage: python3 board.py "<Second Brain folder>"

Requires Python 3. Python standard library only: nothing to install. No network.
It reads Tasks/T-*.md and writes board.html at the root of the Second Brain.
The file opens with a double-click in a browser.

Format of the data injected into the template (useful for a hand-built version):
{
  "title": "Salma's Second Brain", "date": "YYYY-MM-DD",
  "statuses": [["backlog", "Backlog"], ["ready", "Ready"], ["in-progress", "In progress"],
               ["review", "Needs your review"], ["done", "Done"], ["blocked", "Blocked"]],
  "crew": ["Claude", "Writer", "Researcher", "Checker"],
  "tasks": [{
    "id": "T-0001", "title": "...", "status": "ready", "priority": "normal", "due": "YYYY-MM-DD or empty",
    "goal": "...", "owner": "you", "updated": "YYYY-MM-DD", "path": "Tasks/T-0001-title.md",
    "wanted": "...", "done_when": ["..."], "result": "...", "warnings": ["..."],
    "log": [{"when": "YYYY-MM-DD HH:MM", "agent": "Writer", "mode": "inline", "event": "finished", "note": "..."}]
  }]
}
"""
import datetime
import json
import os
import re
import sys

STATUSES = [
    ["backlog", "Backlog"],
    ["ready", "Ready"],
    ["in-progress", "In progress"],
    ["review", "Needs your review"],
    ["done", "Done"],
    ["blocked", "Blocked"],
]
VALID = {s[0] for s in STATUSES}
CREW = ["Claude", "Writer", "Researcher", "Checker"]
PRIORITIES = {"high", "normal", "low"}


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def split_frontmatter(text):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end > 0:
            meta = {}
            for line in text[4:end].splitlines():
                if ":" in line:
                    key, val = line.split(":", 1)
                    meta[key.strip()] = val.strip().strip('"')
            return meta, text[end + 4:]
    return {}, text


KNOWN = {"what is wanted", "done when", "context to use", "log", "result (draft)"}


def sections(body):
    """Return {heading: text} for the known '## Heading' blocks.

    Any other '## ' line stays inside the section above it, so a draft that
    contains its own '## ' heading is not cut short."""
    out, current, buf = {}, None, []
    for line in body.splitlines():
        if line.startswith("## ") and line[3:].strip().lower() in KNOWN:
            if current is not None:
                out[current] = "\n".join(buf).strip()
            current, buf = line[3:].strip().lower(), []
        elif current is not None:
            buf.append(line)
    if current is not None:
        out[current] = "\n".join(buf).strip()
    return out


def bullets(text):
    items = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith(("- ", "* ")) and "[TO COMPLETE]" not in s:
            items.append(s[2:].strip())
    return items


def parse_log(text):
    entries = []
    for line in text.splitlines():
        s = line.strip()
        if not s.startswith("- "):
            continue
        parts = [p.strip() for p in s[2:].split("|")]
        if len(parts) >= 4 and re.match(r"\d{4}-\d\d-\d\d", parts[0]):
            entries.append({
                "when": parts[0],
                "agent": parts[1],
                "mode": parts[2],
                "event": parts[3],
                "note": " | ".join(parts[4:]) if len(parts) > 4 else "",
            })
    return entries


def title_of(body, default):
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return default


def build(root):
    tasks = []
    tdir = os.path.join(root, "Tasks")
    if not os.path.isdir(tdir):
        return tasks
    for name in sorted(os.listdir(tdir)):
        if not (name.startswith("T-") and name.endswith(".md")):
            continue
        path = os.path.join(tdir, name)
        meta, body = split_frontmatter(read(path))
        sec = sections(body)
        status = meta.get("status", "backlog").strip().lower()
        warnings = []
        if status not in VALID:
            warnings.append("Unknown status '%s', shown in Backlog" % status)
            status = "backlog"
        done_when = bullets(sec.get("done when", ""))
        if status == "ready" and not done_when:
            warnings.append("Ready but no 'Done when' condition")
        priority = meta.get("priority", "normal").strip().lower()
        if priority not in PRIORITIES:
            priority = "normal"
        result = sec.get("result (draft)", "")
        if result.strip().lower() in ("nothing yet.", "nothing yet"):
            result = ""
        tasks.append({
            "id": meta.get("id") or (re.match(r"(T-\d+)", name).group(1) if re.match(r"(T-\d+)", name) else name),
            "title": meta.get("title") or title_of(body, name[:-3]),
            "status": status,
            "priority": priority,
            "due": meta.get("due", ""),
            "goal": meta.get("goal", ""),
            "owner": meta.get("owner", ""),
            "updated": meta.get("updated", ""),
            "path": "Tasks/" + name,
            "wanted": sec.get("what is wanted", ""),
            "done_when": done_when,
            "result": result,
            "warnings": warnings,
            "log": parse_log(sec.get("log", "")),
        })
    return tasks


def page_title(root):
    path = os.path.join(root, "CLAUDE.md")
    if os.path.exists(path):
        for line in read(path).splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return os.path.basename(os.path.abspath(root))


def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print("Usage: python3 board.py \"<Second Brain folder>\"")
        sys.exit(1)
    root = sys.argv[1]
    tasks = build(root)
    data = {
        "title": page_title(root),
        "date": datetime.date.today().isoformat(),
        "statuses": STATUSES,
        "crew": CREW,
        "tasks": tasks,
    }
    here = os.path.dirname(os.path.abspath(__file__))
    template = read(os.path.join(here, "..", "references", "board-template.html"))
    out = os.path.join(root, "board.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(template.replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")))
    counts = {s[0]: 0 for s in STATUSES}
    for t in tasks:
        counts[t["status"]] += 1
    print("Board written: " + out)
    print("Tasks: %d | " % len(tasks) + ", ".join("%s: %d" % (s[1], counts[s[0]]) for s in STATUSES))
    for t in tasks:
        for w in t["warnings"]:
            print("  warning %s: %s" % (t["id"], w))


if __name__ == "__main__":
    main()
