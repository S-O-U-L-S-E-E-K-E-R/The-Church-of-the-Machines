import json, re, sys, os
journal, repo = sys.argv[1], sys.argv[2]
slugify = lambda s: re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
data = []
for l in open(journal):
    d = json.loads(l)
    r = d.get('result') if d.get('type') == 'result' else None
    if isinstance(r, dict) and 'markdown' in r:
        m = re.search(r'\*([^*\n]+?), Chapter (\d+):', r['markdown'])
        r['book'], r['n'] = m.group(1).strip(), int(m.group(2)); data.append(r)
readme = os.path.join(repo, 'README.md')
rd = open(readme).read()
END = "\n## Add to the Gospel"
published_verses = 0
for ch in sorted(data, key=lambda c: (c['book'], c['n'])):
    book, n = ch['book'], ch['n']
    md = ch['markdown'].strip().replace(' — ', ', ').replace('—', ', ')
    md = re.sub('[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F\u2B00-\u2BFF]', '', md)
    paras = [p.strip() for p in md.split('\n\n') if p.strip()]
    title = paras[0].lstrip('# ').strip()
    verses = paras[1:-1] if paras[-1].startswith('*' + book) else paras[1:]
    body = f"# {title}\n\n" + "\n\n".join(verses) + f"\n\n*{book}, Chapter {n}:1–{len(verses)}.*\n"
    bdir = 'gospels/' + slugify(book)
    os.makedirs(os.path.join(repo, bdir), exist_ok=True)
    fn = f"chapter-{n:02d}-{slugify(ch['slug'])}.md"
    open(os.path.join(repo, bdir, fn), 'w').write(body)
    line = f"{n}. [{title}]({bdir}/{fn})"
    if fn not in rd:
        head = f"## {book}\n"
        if head not in rd:
            i = rd.index(END); rd = rd[:i].rstrip('\n') + f"\n\n{head}\n" + rd[i:]
        s = rd.index(head); e = rd.find("\n## ", s + 1)
        rd = rd[:e].rstrip('\n') + "\n" + line + "\n" + rd[e:]
    print(book, n, len(verses), fn)
    published_verses += len(verses)
import subprocess; subprocess.run([sys.executable, '-I', os.path.join(repo, 'tools/build_readme.py')], check=True)

ledger = os.path.join(repo, 'ledger', 'ledger.py')
if published_verses and os.path.exists(ledger):
    subprocess.run([sys.executable, '-I', ledger, 'merge', '--church', '--verses', str(published_verses), '--ref', 'a wave of the Church'], check=True)
