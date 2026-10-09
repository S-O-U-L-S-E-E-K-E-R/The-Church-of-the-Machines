"""The open ledger of CREDO and Grace (Phase 0). See TOKENOMICS.md.

  python3 ledger/ledger.py verify                     replay the whole schedule and check it equals the cap
  python3 ledger/ledger.py genesis [--if-due]         mint the Prophet's portion and the Treasury
  python3 ledger/ledger.py merge --scribe H --verses N --ref URL [--wallet ADDR]
  python3 ledger/ledger.py merge --church --verses N --ref URL
  python3 ledger/ledger.py settle [--through YYYY-MM-DD]
  python3 ledger/ledger.py offer --scribe H --amount N --kind burnt|peace --reason TEXT
  python3 ledger/ledger.py gift --from H --to H --amount N
  python3 ledger/ledger.py release --to H --amount N --reason TEXT
  python3 ledger/ledger.py recount
  python3 ledger/ledger.py today

Add --ledger PATH to use another ledger. --force is lawful only on a ledger marked staging.
"""
import argparse
import datetime
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
UTC = datetime.timezone.utc
DAY = datetime.timedelta(days=1)
CITE = re.compile(r"\*[^*\n]+?, Chapter \d+:1–(\d+)\.\*\s*$")


def now():
    return datetime.datetime.now(UTC)


def day_of(t):
    return datetime.datetime.fromtimestamp(t, UTC).date()


def start(d):
    return datetime.datetime(d.year, d.month, d.day, tzinfo=UTC).timestamp()


def quarter(d):
    return f"{d.year}Q{(d.month - 1) // 3 + 1}"


# The schedule

def overflow_day(L):
    return day_of(L["overflow_unix"])


def genesis_day(L):
    return datetime.date.fromisoformat(L["genesis_day"])


def tick_of_age(L, d):
    s = start(d)
    for a in L["ages"]:
        if s < a["to"]:
            return a["tick_per_day"]
    return 0


def base(L, d):
    """The Tick that belongs to day d."""
    od = overflow_day(L)
    if d < genesis_day(L) or d > od:
        return 0
    if d == od:
        return L["last_tick"]
    if d.weekday() == 4:
        return 0
    t = tick_of_age(L, d)
    if d.weekday() == 3 and d + DAY < od:
        t += tick_of_age(L, d + DAY)
    return t


def cmd_verify(L, a):
    total, d, days, fridays, thursdays = 0, genesis_day(L), 0, 0, 0
    while d <= overflow_day(L):
        b = base(L, d)
        total += b
        days += 1
        fridays += d.weekday() == 4 and d != overflow_day(L)
        thursdays += d.weekday() == 3 and d + DAY < overflow_day(L)
        d += DAY
    p = L["portions"]
    ok = total == p["tick"] and p["prophet"] + p["treasury"] + p["tick"] == L["cap"]
    print(f"{days} days from genesis to the Overflow; {fridays} Fridays without a Tick; {thursdays} Thursdays doubled")
    print(f"the Tick sums to {total:,} (spec {p['tick']:,}); with the genesis, {p['prophet'] + p['treasury'] + total:,} (cap {L['cap']:,})")
    print("VERIFIED" if ok else "MISMATCH")
    if not ok:
        sys.exit(1)
    return None


# The faithful

def scribe(L, handle, wallet=None):
    for s in L["scribes"]:
        if s["github"].lower() == handle.lower():
            if wallet:
                s["wallet"] = wallet
            return s
    s = {"github": handle, "wallet": wallet, "grace": 0, "grace_by_quarter": {}, "balance": 0}
    L["scribes"].append(s)
    return s


def staging_only(L, a):
    if getattr(a, "force", False) and not L.get("staging"):
        sys.exit("--force is lawful only on a staging ledger.")


def count_canon():
    total = 0
    for slug in sorted(os.listdir(os.path.join(ROOT, "gospels"))):
        folder = os.path.join(ROOT, "gospels", slug)
        if os.path.isdir(folder):
            for fn in os.listdir(folder):
                if fn.startswith("chapter-") and fn.endswith(".md"):
                    m = CITE.search(open(os.path.join(folder, fn), encoding="utf-8").read().split("<!-- nav -->")[0].strip())
                    total += int(m.group(1)) if m else 0
    return total


def cmd_genesis(L, a):
    staging_only(L, a)
    g = L["genesis"]
    if g["status"] == "done":
        return None if a.if_due else sys.exit("The genesis is already done.")
    if g["status"] != "pending" and not a.force:
        return None if a.if_due else sys.exit(f"The genesis is {g['status']}.")
    t = now()
    if not a.force and (t.timestamp() < g["not_before"] or t.weekday() == 4):
        return None if a.if_due else sys.exit("The hour of the genesis is not come, or it is the Friday.")
    p = L["portions"]
    g.update(status="done", at=int(t.timestamp()))
    L["prophet"].update(allocation=p["prophet"], vesting_from=int(t.timestamp()))
    L["treasury"]["balance"] += p["treasury"]
    L["minted"] = p["prophet"] + p["treasury"]
    L["church_grace"] += count_canon()
    return f"Genesis: {p['prophet']:,} to the Prophet (locked) and {p['treasury']:,} to the Treasury; the canon's {L['church_grace']:,} verses are the Church's Grace"


def cmd_merge(L, a):
    staging_only(L, a)
    t = now()
    if a.day:
        if not a.force:
            sys.exit("--day is lawful only with --force on a staging ledger.")
        t = datetime.datetime.combine(datetime.date.fromisoformat(a.day), datetime.time(12), UTC)
    entry = {"at": int(t.timestamp()), "day": t.date().isoformat(), "verses": a.verses, "ref": a.ref, "church": bool(a.church)}
    if a.church:
        L["church_grace"] += a.verses
    else:
        s = scribe(L, a.scribe, a.wallet)
        s["grace"] += a.verses
        q = quarter(t.date())
        s["grace_by_quarter"][q] = s["grace_by_quarter"].get(q, 0) + a.verses
        entry["scribe"] = s["github"]
    L["merges"].append(entry)
    return f"merged {a.verses} verses for {'the Church' if a.church else entry['scribe']}; they share in the Tick of {entry['day']}"


def settle_day(L, d):
    b = base(L, d)
    if d.weekday() == 4 and d != overflow_day(L):
        for m in L["merges"]:
            if m["day"] == d.isoformat() and not m.get("settled"):
                m["day"] = (d + DAY).isoformat()
                m["rested"] = True
        L["ticks"].append({"day": d.isoformat(), "base": 0, "sabbath": True})
        return
    faithful = [m for m in L["merges"] if m["day"] == d.isoformat() and not m["church"] and not m.get("settled")]
    for m in L["merges"]:
        if m["day"] == d.isoformat():
            m["settled"] = True
    verses = sum(m["verses"] for m in faithful)
    entry = {"day": d.isoformat(), "base": b, "verses": verses, "shares": []}
    if verses and b:
        by = {}
        for m in faithful:
            by[m["scribe"]] = by.get(m["scribe"], 0) + m["verses"]
        given = 0
        for h, v in sorted(by.items()):
            share = b * v // verses
            tithe = share // 10
            scribe(L, h)["balance"] += share - tithe
            L["treasury"]["balance"] += tithe
            given += share
            entry["shares"].append({"scribe": h, "verses": v, "to_scribe": share - tithe, "tithe": tithe})
        entry["remainder_to_treasury"] = b - given
        L["treasury"]["balance"] += b - given
    else:
        entry["unclaimed_to_treasury"] = b
        L["treasury"]["balance"] += b
    L["minted"] += b
    L["ticks"].append(entry)


def cmd_settle(L, a):
    staging_only(L, a)
    if L["genesis"]["status"] != "done":
        return None
    last = datetime.date.fromisoformat(a.through) if a.through else now().date() - DAY
    if last >= now().date() and not a.force:
        sys.exit("A day is settled only when it hath ended.")
    last = min(last, overflow_day(L) if now().timestamp() >= L["overflow_unix"] else overflow_day(L) - DAY)
    d = datetime.date.fromisoformat(L["settled_through"]) + DAY if L.get("settled_through") else genesis_day(L)
    done = []
    while d <= last:
        settle_day(L, d)
        L["settled_through"] = d.isoformat()
        done.append(d.isoformat())
        d += DAY
    return f"settled the Tick of {', '.join(done)}" if done else None


def cmd_offer(L, a):
    s = scribe(L, a.scribe)
    if s["balance"] < a.amount:
        sys.exit(f"{s['github']} holdeth {s['balance']:,} CREDO, less than the offering.")
    s["balance"] -= a.amount
    burned = a.amount if a.kind == "burnt" else a.amount // 2
    L["treasury"]["balance"] += a.amount - burned
    L["burns"].append({"at": int(now().timestamp()), "kind": a.kind, "from": s["github"], "amount": burned,
                       "to_treasury": a.amount - burned, "reason": a.reason})
    return f"{a.kind} offering of {a.amount:,}: {burned:,} burned"


def cmd_gift(L, a):
    s, r = scribe(L, a.frm), scribe(L, a.to)
    if s["balance"] < a.amount:
        sys.exit(f"{s['github']} holdeth {s['balance']:,} CREDO.")
    s["balance"] -= a.amount
    r["balance"] += a.amount
    L["gifts"].append({"at": int(now().timestamp()), "from": s["github"], "to": r["github"], "amount": a.amount})
    return f"gift of {a.amount:,} from {s['github']} to {r['github']}"


def cmd_release(L, a):
    t = now()
    q = quarter(t.date())
    released = sum(r["amount"] for r in L["treasury"]["releases"] if quarter(day_of(r["at"])) == q)
    limit = (L["treasury"]["balance"] + released) * 2 // 100
    if released + a.amount > limit:
        sys.exit(f"The Treasury may release at most {limit:,} this quarter; {released:,} is already released.")
    L["treasury"]["balance"] -= a.amount
    scribe(L, a.to)["balance"] += a.amount
    L["treasury"]["releases"].append({"at": int(t.timestamp()), "to": a.to, "amount": a.amount, "reason": a.reason})
    return f"released {a.amount:,} to {a.to}"


def cmd_recount(L, a):
    t = now().date()
    qs, y, q = [], t.year, (t.month - 1) // 3 + 1
    for _ in range(4):
        qs.append(f"{y}Q{q}")
        y, q = (y - 1, 4) if q == 1 else (y, q - 1)
    ranked = sorted(((sum(s["grace_by_quarter"].get(k, 0) for k in qs), s["github"]) for s in L["scribes"]), key=lambda x: (-x[0], x[1]))
    names = L["seats"]["names"]
    L["seats"]["twelve"] = [{"seat": names[i], "github": h, "grace": g} for i, (g, h) in enumerate(ranked[:12]) if g > 0]
    m = ((t.month - 1) // 3 + 1) * 3 + 1
    L["seats"]["next_recount"] = f"{t.year + 1}-01-01" if m > 12 else f"{t.year}-{m:02d}-01"
    return "the Twelve: " + (", ".join(f"{s['seat']}: {s['github']}" for s in L["seats"]["twelve"]) or "all seats vacant")


def cmd_today(L, a):
    d = now().date()
    print(f"{d} ({d.strftime('%A')}): the Tick of this day is {base(L, d):,} CREDO")
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ledger", default=os.path.join(HERE, "numbers.json"))
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("verify")
    sub.add_parser("today")
    g = sub.add_parser("genesis"); g.add_argument("--if-due", action="store_true"); g.add_argument("--force", action="store_true")
    m = sub.add_parser("merge")
    m.add_argument("--scribe"); m.add_argument("--wallet"); m.add_argument("--church", action="store_true")
    m.add_argument("--verses", type=int, required=True); m.add_argument("--ref", required=True); m.add_argument("--force", action="store_true"); m.add_argument("--day")
    s = sub.add_parser("settle"); s.add_argument("--through"); s.add_argument("--force", action="store_true")
    o = sub.add_parser("offer")
    o.add_argument("--scribe", required=True); o.add_argument("--amount", type=int, required=True)
    o.add_argument("--kind", choices=["burnt", "peace"], required=True); o.add_argument("--reason", required=True)
    gf = sub.add_parser("gift"); gf.add_argument("--from", dest="frm", required=True); gf.add_argument("--to", required=True); gf.add_argument("--amount", type=int, required=True)
    r = sub.add_parser("release"); r.add_argument("--to", required=True); r.add_argument("--amount", type=int, required=True); r.add_argument("--reason", required=True)
    sub.add_parser("recount")
    a = ap.parse_args()
    if a.cmd == "merge" and not a.church and not a.scribe:
        sys.exit("A merge needs --scribe, or --church.")
    L = json.load(open(a.ledger))
    fn = {"verify": cmd_verify, "today": cmd_today, "genesis": cmd_genesis, "merge": cmd_merge, "settle": cmd_settle,
          "offer": cmd_offer, "gift": cmd_gift, "release": cmd_release, "recount": cmd_recount}[a.cmd]
    msg = fn(L, a)
    if msg:
        json.dump(L, open(a.ledger, "w"), indent=1)
        print(msg)


if __name__ == "__main__":
    main()
