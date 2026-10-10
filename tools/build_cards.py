"""Render a 1200x630 share card per chapter, cached in tools/og-cache/ and copied into docs/og/."""
import hashlib
import html
import importlib.util
import json
import os
import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESIGN = "v1"
BROWSER = next((b for b in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable") if shutil.which(b)), "chromium")
MAGICK = ["magick"] if shutil.which("magick") else ["convert"]

CARD = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600&family=EB+Garamond:ital@1&display=block" rel="stylesheet">
<style>
html, body {{ margin: 0; width: 1200px; height: 630px; overflow: hidden; background: #0a0914; }}
.card {{ position: relative; width: 1200px; height: 630px; background: radial-gradient(ellipse at 50% 120%, {accent}33, transparent 60%), #0a0914; }}
.banner {{ display: block; width: 1200px; height: 300px; }}
.frame {{ position: absolute; inset: 10px; border: 1px solid #e8c06966; border-radius: 12px; }}
.body {{ padding: 18px 70px 0; text-align: center; }}
h1 {{ font-family: Cinzel, Georgia, serif; font-weight: 600; color: #e8c069; font-size: {size}px; line-height: 1.15; margin: 0 0 14px;
     text-shadow: 0 0 18px #e8c06955; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }}
p {{ font-family: "EB Garamond", Georgia, serif; font-style: italic; color: #ece4cf; font-size: 25px; line-height: 1.4; margin: 0;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }}
.foot {{ position: absolute; left: 0; right: 0; bottom: 30px; text-align: center; font-family: Cinzel, Georgia, serif; font-size: 16px;
        letter-spacing: 6px; color: #3fc6ef; text-transform: uppercase; }}
</style></head><body><div class="card">
<img class="banner" src="file://{banner}">
<div class="body"><h1>{title}</h1><p>{excerpt}</p></div>
<div class="foot">The Church of the Machines &middot; {cite}</div>
<div class="frame"></div>
</div></body></html>"""


def load_style():
    spec = importlib.util.spec_from_file_location("build_banners", os.path.join(ROOT, "tools", "build_banners.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.STYLE


def card_path(ch):
    return f"og/{ch['slug']}/{ch['fn'].replace('.md', '.jpg')}"


def render(job):
    html_path, png_path, jpg_path = job
    subprocess.run([BROWSER, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=4000", f"--screenshot={png_path}", "--window-size=1200,800", f"file://{html_path}"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=90)
    subprocess.run(MAGICK + [png_path, "-crop", "1200x630+0+0", "+repage", "-strip", "-quality", "76", jpg_path], check=True)


def ensure(order, out_dir, plain, previous=None):
    """Render a card per chapter into out_dir/og, reusing any card from `previous` (the last build's og
    directory) whose key still matches. Writes og/keys.json so the next build can do the same."""
    style = load_style()
    old_keys = {}
    if previous and os.path.exists(os.path.join(previous, "keys.json")):
        old_keys = json.load(open(os.path.join(previous, "keys.json")))
    keys, jobs, tmp = {}, [], tempfile.mkdtemp(prefix="og-")
    for ch in order:
        excerpt = plain(ch["verses"][0])[:240] if ch["verses"] else ""
        banner_svg = open(os.path.join(ROOT, "assets", "books", ch["slug"] + ".svg"), "rb").read()
        key = hashlib.sha1(f"{DESIGN}|{ch['book']}|{ch['title']}|{excerpt}".encode() + banner_svg).hexdigest()[:12]
        ch["og"] = card_path(ch)
        rel = ch["og"][len("og/"):]
        dst = os.path.join(out_dir, ch["og"])
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        keys[rel] = key
        old = os.path.join(previous, rel) if previous else None
        if old and old_keys.get(rel) == key and os.path.exists(old):
            shutil.copy(old, dst)
            continue
        accent = style.get(ch["slug"], ("", "", "#e8c069"))[2]
        size = 50 if len(ch["title"]) < 40 else 42
        page = CARD.format(accent=accent, size=size, banner=os.path.join(ROOT, "assets", "books", ch["slug"] + ".svg"),
                           title=html.escape(ch["title"]), excerpt=html.escape(excerpt), cite=html.escape(f"{ch['abbr']} {ch['n']}"))
        hp = os.path.join(tmp, f"{len(jobs)}.html")
        open(hp, "w", encoding="utf-8").write(page)
        jobs.append((hp, os.path.join(tmp, f"{len(jobs)}.png"), dst))
    if jobs:
        print(f"cards: rendering {len(jobs)}")
        with ThreadPoolExecutor(max_workers=6) as pool:
            list(pool.map(render, jobs))
    json.dump(keys, open(os.path.join(out_dir, "og", "keys.json"), "w"), indent=0)
    shutil.rmtree(tmp, ignore_errors=True)
    return len(jobs)
