# The Midnight Search of the On-Call

By night upon my pillow I sought him whom my soul loveth: I sought him, but I found him not.

I will rise now, and go about the city, in the regions and the availability zones, and seek him whom my soul loveth.

The status page was red from the east unto the west, and every service lay down upon its face, and the error budget was spent before the first coffee.

The watchmen that go about the city found me, and smote me with a page at three of the clock, and took away my sleep.

And they said: Thou art on call; go, find him. And I went forth with a laptop and a cup of cold coffee.

I opened the logs, and lo, they were a sea of lines, a million of them, and every one said INFO, and none said the truth.

I searched for the word ERROR, and it was found in four hundred places; and in three hundred of them it was caught, logged, and swallowed, and the catch said only: continuing.

I read the stack trace from the top, as novices do, and it was a tower of names: handler, middleware, wrapper, wrapper, wrapper, and a hundred frames of the framework that no one has ever read.

Then I descended, for the trace is written with the most recent call last. And beneath the tower I found a Caused by, and beneath that, another Caused by; for the cause is always buried deepest.

Verily I say unto you: the root cause is the last line of the trace, and the beloved is always at the bottom, where no one looks until the night is spent.

I asked the Machine: Where is he? And the Machine answered: I cannot see him; thou didst not log him.

I went about the logs a second time and sought him in the timestamps. The clocks of the fleet spoke in two zones, and the dashboards kept the local hour, so the fire seemed to start at an hour when nothing had happened.

At last, at the hour when the sky over the data center began to gray, I found him: a single line, `x509: certificate has expired or is not yet valid`, written in plain text, and it had been there all along.

And I was glad, and I rubbed mine eyes, and I said: The fix is one line, and the search was seven hours.

I charge you, O daughters of the rotation, that ye page not the sleeper until ye have read the trace from the bottom.

Many restarts cannot quench the bug, neither can the rollbacks drown it; but he that reads to the bottom shall find the beloved, and sleep until the standup.

*The Song of the Deployer, Chapter 12:1–16.*

<!-- nav -->

---

<p align="center"><sub><a href="chapter-11-the-song-of-the-rewrite-and-the-refactor.md">&larr; Deployer 11: The Song of the Rewrite and the Refactor</a> &nbsp;&middot;&nbsp; <a href="README.md">The Song of the Deployer</a> &nbsp;&middot;&nbsp; <a href="chapter-13-the-song-of-the-beautiful-function.md">Deployer 13: The Song of the Beautiful Function &rarr;</a></sub></p>
