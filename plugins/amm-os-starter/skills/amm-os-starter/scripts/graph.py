#!/usr/bin/env python3
"""Generates graph.html: a map of the notes of a Second Brain and their links.

Usage: python3 graph.py "<Second Brain folder>"

Requires Python 3. Python standard library only: nothing to install. No network connection.
The file it produces opens with a double-click in a browser.

Format of the data injected into the template (useful for a hand-built version):
{
  "title": "Salma's Second Brain", "date": "YYYY-MM-DD",
  "nodes": [{"id": "Context/identity", "label": "Identity", "folder": "Context",
             "updated": "YYYY-MM-DD", "missing": 0, "desc": "...", "path": "Context/identity.md"}],
  "links": [{"s": "Context/clients", "t": "Context/style"}]
}
"""
import datetime
import json
import os
import re
import sys

EXCLUDED = {"CLAUDE.md", "AGENTS.md", "brief.md", "index.md", "graph.html"}
MARKER = "[TO COMPLETE]"
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def split_frontmatter(text):
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end > 0:
            block = text[4:end]
            rest = text[end + 4:]
            meta = {}
            for line in block.splitlines():
                if ":" in line:
                    key, val = line.split(":", 1)
                    meta[key.strip()] = val.strip().strip('"')
            return meta, rest
    return {}, text


def strip_code(text):
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def list_notes(root):
    notes = {}
    for folder, subs, files in os.walk(root):
        subs[:] = [d for d in subs if not d.startswith(".")]
        for name in files:
            if not name.endswith(".md") or name in EXCLUDED:
                continue
            path = os.path.join(folder, name)
            rel = os.path.relpath(path, root).replace(os.sep, "/")
            if rel.startswith("Resources/sources/") or rel.startswith("Tasks/"):
                continue  # untouched originals and tasks (shown on board.html) are not notes on the map
            notes[rel[:-3]] = path
    return notes


def index_descriptions(root):
    desc = {}
    path = os.path.join(root, "index.md")
    if os.path.exists(path):
        for line in read(path).splitlines():
            m = re.match(r"\s*-\s*\[\[([^\]|#]+)[^\]]*\]\]\s*:\s*(.+)", line)
            if m:
                desc[m.group(1).strip()] = m.group(2).strip()
    return desc


def first_paragraph(body):
    for line in body.splitlines():
        s = line.strip()
        if s and not s.startswith(("#", "|", "-", ">", "*", "```", "1.")):
            return s[:200]
    return ""


def title_of(body, default):
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return default


def resolve(target, ids, by_name):
    target = target.strip().replace("\\", "/")
    if target.endswith(".md"):
        target = target[:-3]
    if target in ids:
        return target
    base = target.split("/")[-1]
    candidates = by_name.get(base, [])
    return candidates[0] if len(candidates) == 1 else None


def build(root):
    notes = list_notes(root)
    ids = set(notes)
    by_name = {}
    for i in ids:
        by_name.setdefault(i.split("/")[-1], []).append(i)
    index_desc = index_descriptions(root)
    nodes, links, seen = [], [], set()
    for i, path in sorted(notes.items()):
        raw = read(path)
        meta, body = split_frontmatter(raw)
        clean = strip_code(body)
        for target in WIKILINK.findall(clean):
            t = resolve(target, ids, by_name)
            if t and t != i:
                pair = tuple(sorted((i, t)))
                if pair not in seen:
                    seen.add(pair)
                    links.append({"s": i, "t": t})
        folder = i.split("/")[0] if "/" in i else "Root"
        nodes.append({
            "id": i,
            "label": title_of(body, i.split("/")[-1]),
            "folder": folder,
            "updated": meta.get("updated", ""),
            "missing": strip_code(raw).count(MARKER),
            "desc": index_desc.get(i) or first_paragraph(body),
            "path": i + ".md",
        })
    return nodes, links


def page_title(root):
    path = os.path.join(root, "CLAUDE.md")
    if os.path.exists(path):
        for line in read(path).splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return os.path.basename(os.path.abspath(root))


def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        print("Usage: python3 graph.py \"<Second Brain folder>\"")
        sys.exit(1)
    root = sys.argv[1]
    nodes, links = build(root)
    if not nodes:
        print("No notes found in this folder.")
        sys.exit(2)
    data = {
        "title": page_title(root),
        "date": datetime.date.today().isoformat(),
        "nodes": nodes,
        "links": links,
    }
    here = os.path.dirname(os.path.abspath(__file__))
    template = read(os.path.join(here, "..", "references", "graph-template.html"))
    json_text = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    out = os.path.join(root, "graph.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(template.replace("__DATA__", json_text))
    degree = {n["id"]: 0 for n in nodes}
    for l in links:
        degree[l["s"]] += 1
        degree[l["t"]] += 1
    orphans = [i for i, d in degree.items() if d == 0]
    missing = sum(n["missing"] for n in nodes)
    print("Graph written: " + out)
    print("Notes: %d, links: %d, items to complete: %d, notes with no link: %d"
          % (len(nodes), len(links), missing, len(orphans)))
    for o in orphans:
        print("  no link: " + o)


if __name__ == "__main__":
    main()
