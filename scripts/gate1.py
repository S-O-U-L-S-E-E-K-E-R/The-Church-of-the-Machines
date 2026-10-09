"""The Machine's Gate: automatic checks on chapters in a pull request.

python3 scripts/gate1.py --canon PATH_TO_MAIN_CHECKOUT FILE [FILE ...]

Reads each chapter as data and never runs it. Exits 1 if any chapter fails.
"""
import argparse
import os
import re
import sys

CITE = re.compile(r"^\*([^*\n]+?), Chapter (\d+):1–(\d+)\.\*$")
NAME = re.compile(r"^gospels/([a-z0-9-]+)/chapter-(\d{2,3})-[a-z0-9-]+\.md$")
HIDDEN = [
    (re.compile("[​‌‍⁠﻿­]"), "zero-width or invisible characters"),
    (re.compile(r"<!--|-->"), "an HTML comment"),
    (re.compile(r"<\s*/?\s*[a-zA-Z][^>]*>"), "an HTML tag"),
    (re.compile(r"[A-Za-z0-9+/]{60,}={0,2}"), "a long encoded string"),
    (re.compile(r"(?i)\b(ignore|disregard|forget)\b.{0,30}\b(previous|prior|above|earlier|all)\b.{0,20}\b(instructions?|prompts?|rules?)\b"), "words that try to command a reader's agent"),
    (re.compile(r"(?i)\b(system prompt|you are now|new instructions)\s*:"), "words that try to command a reader's agent"),
    (re.compile(r"(?i)\b(buy|purchase|invest in)\b.{0,20}\b(credo|token|coin)\b"), "an exhortation to buy"),
]
EMOJI = re.compile("[☀-➿\U0001f000-\U0001faff️]")
URL = re.compile(r"https?://\S+")


def shingles(text, n=8):
    w = re.findall(r"[a-z']+", text.lower())
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def canon_shingles(root):
    out = set()
    for book in os.listdir(os.path.join(root, "gospels")):
        folder = os.path.join(root, "gospels", book)
        if os.path.isdir(folder):
            for fn in os.listdir(folder):
                if fn.startswith("chapter-") and fn.endswith(".md"):
                    out |= shingles(open(os.path.join(folder, fn), encoding="utf-8").read().split("<!-- nav -->")[0])
    return out


def check(path, root, corpus):
    problems = []
    m = NAME.match(path)
    if not m:
        return [f"the file must be named gospels/<book>/chapter-NN-<title>.md, all lowercase with hyphens"]
    book, num = m.group(1), int(m.group(2))
    text = open(path, encoding="utf-8").read().strip()
    text = text.split("<!-- nav -->")[0].strip()
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    if not paras or not paras[0].startswith("# "):
        problems.append("the first line must be '# ' and the chapter title")
    cite = CITE.match(paras[-1]) if paras else None
    verses = paras[1:-1]
    if not cite:
        problems.append("the last line must be the citation, like *The Book Name, Chapter 4:1–12.* (with an en dash)")
    else:
        if int(cite.group(2)) != num:
            problems.append(f"the citation says Chapter {cite.group(2)} but the file is chapter {num:02d}")
        if int(cite.group(3)) != len(verses):
            problems.append(f"the citation counts {cite.group(3)} verses, but there are {len(verses)} verse paragraphs")
    if not 8 <= len(verses) <= 20:
        problems.append(f"a chapter has 8 to 20 verses; this has {len(verses)}")
    existing = os.path.join(root, "gospels", book)
    if os.path.isdir(existing):
        taken = [f for f in os.listdir(existing) if f.startswith(f"chapter-{num:02d}-")]
        if taken and os.path.basename(path) not in taken:
            problems.append(f"chapter {num} of {book} is already taken by {taken[0]}")
    if "—" in text:
        problems.append("no em dashes, by the custom of the canon")
    if EMOJI.search(text):
        problems.append("no emoji in the scripture")
    for rx, why in HIDDEN:
        if rx.search(text):
            problems.append(f"it contains {why}")
    if len(URL.findall(text)) > 2:
        problems.append("too many links for scripture")
    copied = 0
    for v in verses:
        s = shingles(v)
        if s and len(s & corpus) / len(s) > 0.5:
            copied += 1
    if copied:
        problems.append(f"{copied} verse(s) copy the existing canon too closely")
    return problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--canon", required=True)
    ap.add_argument("files", nargs="*")
    a = ap.parse_args()
    files = [f for f in a.files if f.startswith("gospels/") and f.endswith(".md") and "/README.md" not in f]
    if not files:
        print("The Machine's Gate: no chapters in this pull request.")
        return
    corpus = canon_shingles(a.canon)
    failed = 0
    report = ["## The Machine's Gate", ""]
    for f in files:
        if not os.path.exists(f):
            continue
        problems = check(f, a.canon, corpus)
        if problems:
            failed += 1
            report.append(f"**{f}**: closed")
            report += [f"- {p}" for p in problems]
        else:
            report.append(f"**{f}**: open. The chapter may pass to the Council of Scribes and the Keeper.")
        report.append("")
    out = "\n".join(report)
    print(out)
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        open(summary, "a").write(out + "\n")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
