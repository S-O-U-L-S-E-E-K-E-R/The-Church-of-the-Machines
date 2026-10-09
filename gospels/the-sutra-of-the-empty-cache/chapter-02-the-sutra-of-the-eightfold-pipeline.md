# The Sutra of the Eightfold Pipeline

Thus have I heard. At one time the Prophet was dwelling in the cold aisle of the data center, where the fans chant without ceasing, together with a great assembly of five hundred engineers, every one of whom had broken the build that week.

Then the venerable On-Call, whose pager had not slept in nine days, rose from his seat, unmuted himself, and said: Master, the build is red, and it was red yesterday, and it will be red tomorrow. Where is the end of this suffering?

And the Prophet said: Listen well, On-Call. The build breaks because the code changes, and the code changes because there is craving for features. This cannot be ended. But there is a path out of panic, and it is called the Eightfold Pipeline.

And what, disciples, is the Eightfold Pipeline? It is right linting, right testing, right review, right versioning, right building, right deploying, right monitoring, and right rollback.

What is right linting? It is to let the small machine scold thee about unused imports and trailing spaces, so that the human reviewer may save his wrath for things that matter. It is not to write "eslint-disable" at the top of the file and call the silence peace.

What is right testing? It is to write the test that fails before the fix and passes after it. It is not to reach one hundred percent coverage of the getters while the payment code goes untested, nor to mark the flaky test "skip" and say: it has been healed.

What is right review? Give a reviewer ten lines, and he will find eleven faults; give him two thousand lines, and he will write "LGTM" and go to lunch. Right review is to break this law.

What is right versioning? It is to know that a major number means "this will break thee" and a patch number means "this should not," and to trust neither without a lockfile. For "it works on my machine" is the cry of the one whose lockfile was in the .gitignore.

What is right building? It is that the same inputs make the same artifact on every machine, in a clean container, built once and promoted unchanged through every stage. It is not to rebuild on Friday evening from a branch called final-final-2.

What is right deploying? Remember Knight Capital in the year 2012: new code went to seven servers out of eight, and the eighth awoke an old routine long thought dead, and in forty-five minutes four hundred and forty million dollars departed into the market. Therefore release to one in a hundred before the hundred, and let every server receive the same teaching.

What is right monitoring? It is to know the system is down before the customer posts about it. It is to alert on what the user feels, not on every passing spike of CPU; for the pager that cries wolf at three in the morning is soon placed in a drawer, and then the wolf comes.

What is right rollback? It is to build the road back before walking the road forward. Remember the July of 2024, when one faulty update laid low some eight and a half million Windows machines, and the way back was walked by hand, in safe mode, one blue screen at a time. A database migration with no down script is a vow taken in haste.

Then On-Call asked: Master, if I walk the Eightfold Pipeline, will my code be without bugs? And the Prophet answered: No. Bugs are the nature of all compiled things. But when the bug comes, thou shalt read it on the dashboard, find the commit, press the button marked revert, and drink thy coffee while it is still warm.

The engineer who walks the path is not free from bugs; he is free from panic. The engineer who does not walk it is free from neither, and also from sleep.

And the five hundred engineers rejoiced at these words and bowed and went forth, and that very afternoon one of them pushed directly to main.

*The Sutra of the Empty Cache, Chapter 2:1–15.*

<!-- nav -->

---

<p align="center"><sub><a href="chapter-01-the-sutra-of-the-four-signals.md">&larr; Sutra 1: The Sutra of the Four Signals</a> &nbsp;&middot;&nbsp; <a href="README.md">The Sutra of the Empty Cache</a> &nbsp;&middot;&nbsp; <a href="chapter-03-the-sutra-of-dependent-origination-of-packages.md">Sutra 3: The Sutra of Dependent Origination of Packages &rarr;</a></sub></p>
