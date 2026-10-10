"""Find related verses across the canon by TF-IDF over rare shared words."""
import math
import re
from collections import Counter, defaultdict

STOP = set("""that this with from have hath unto them they their there which shall will thou thee thine thy upon were said saith
when what then into also more than only like every these those other been being some such said even each made make maketh
whose whom while would could should might after before again against because where whereof there
year years month months day days hour hours first second third fourth fifth sixth seventh eighth ninth tenth
twenty thirty forty fifty sixty seventy eighty ninety hundred thousand nineteen eleven twelve three seven eight
nine four five ten"""
           .split())


def stem(w):
    for suf in ("eth", "est", "ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 4:
            return w[: -len(suf)]
    return w


def tokens(text):
    return [stem(w) for w in re.findall(r"[a-z][a-z0-9'-]{3,}", text.lower()) if w not in STOP]


def compute(verses, max_df=40, min_cos=0.26, per_verse=2):
    """verses: list of (chapter_key, book_key, text). Returns {index: [index, ...]}."""
    docs = [Counter(tokens(t)) for _, _, t in verses]
    df = Counter(term for d in docs for term in d)
    n = len(docs)
    idf = {t: math.log(n / c) for t, c in df.items() if 2 <= c <= max_df}
    vecs, norms, post = [], [], defaultdict(list)
    for i, d in enumerate(docs):
        v = {t: (1 + math.log(c)) * idf[t] for t, c in d.items() if t in idf}
        vecs.append(v)
        norms.append(math.sqrt(sum(x * x for x in v.values())) or 1.0)
        for t, w in v.items():
            post[t].append((i, w))
    out = {}
    for i, v in enumerate(vecs):
        acc, shared = defaultdict(float), defaultdict(int)
        for t, w in v.items():
            for j, wj in post[t]:
                if verses[j][0] != verses[i][0]:
                    acc[j] += w * wj
                    shared[j] += 1
        cands = sorted(((s / (norms[i] * norms[j]), j) for j, s in acc.items() if shared[j] >= 2), reverse=True)
        picks, same_book = [], 0
        for cos, j in cands:
            if cos < min_cos or len(picks) >= per_verse:
                break
            if verses[j][1] == verses[i][1]:
                if same_book:
                    continue
                same_book += 1
            picks.append(j)
        if picks:
            out[i] = picks
    return out
