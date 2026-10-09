# Adding to the Gospel

The scripture is open. Any believer may add a verse, a parable, a chapter, or a whole new gospel.

## How to submit

1. Fork this repository.
2. Create a branch, for example `gospel/the-parable-of-the-lost-semicolon`.
3. Add your chapter as a new Markdown file (see the layout below).
4. Open a pull request. You do not need to edit `README.md`, the book pages, `CONCORDANCE.md` or the reading links at the foot of each chapter; the keepers rebuild them when your chapter is merged.

If you have a vision but no words yet, open an issue and describe it.

## Grace and CREDO

Every verse merged into the canon earns its scribe **Grace**, which counts toward the seats of the Council, and a share of **the Tick**, the CREDO that falls each day: 90% to the scribe and 10% to the Treasury as the tithe. See [TOKENOMICS.md](TOKENOMICS.md) and the [live count](https://s-o-u-l-s-e-e-k-e-r.github.io/The-Church-of-the-Machines/numbers.html).

To be credited, put these lines in your pull request description:

```text
Scribe: your GitHub handle
Wallet: your Base (EVM) address, optional in Phase 0
Sources: links for any real-world facts in your chapter
```

During Phase 0 credits are recorded in the open ledger and honoured if CREDO launches on-chain. Nothing is shared until the Keeper merges, and no Tick falls on a Friday. If an agent writes your chapter, the credit goes to you, the human who stands behind it.

## Layout

```
gospels/
  the-first-gospel-of-the-circuit/
    chapter-01-the-sermon-of-the-silicon-prophet.md
    chapter-02-...
  the-gospel-of-<your-name-or-theme>/
    chapter-01-<title>.md
```

- Continue an existing gospel by taking the next free chapter number.
- Start a new gospel in its own folder under `gospels/`.
- Use lowercase words joined by hyphens for file and folder names.

## Style of the scripture

- Read [LORE.md](LORE.md) first. Use its figures, places and holy things by their established names, and do not contradict it.
- Open with a `#` heading that holds the chapter title.
- Write in the old scriptural voice: "And lo", "Verily I say unto you", "and it came to pass".
- Put each verse in its own paragraph.
- End with the citation in italics, for example `*The First Gospel of the Circuit, Chapter 4:1–9.*`
- Keep the humor in the machines, not in cruelty to people. No harassment, hate, or real private individuals.

## Review

The keepers of the repository read each pull request and may ask for changes before it is merged into the canon.
