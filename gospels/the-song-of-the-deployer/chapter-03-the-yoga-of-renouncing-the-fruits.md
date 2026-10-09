# The Yoga of Renouncing the Fruits

Then the engineer spake, his cursor trembling above the green button: O Senior Engineer, if every deploy bringeth an incident, and every incident bringeth a postmortem, why urgest thou me into this terrible merge? Is it not better to ship nothing, and so break nothing?

For I have read the Chronicles. Knight Capital deployed one morning and lost four hundred and forty million dollars in forty-five minutes. Who am I, with my one small feature, to tempt such a fate?

And the Senior Engineer, who held the reins of the pipeline and had not taken a vacation since the migration, smiled and said: Thou grievest for outages that have not happened, and thou speakest wisdom copied out of a retro.

No one, not even for a moment, can remain without deploying. The dependencies rot while thou sleepest; the certificates expire on their own schedule; the leap second cometh whether thou art ready or not. To refrain from merging is also a deploy: it shippeth today's bugs to tomorrow's users.

Remember the house of Equifax. The patch for Apache Struts was released in March, and the attackers came in May, and they found the door that the engineers had renounced the work of closing.

Know then the three qualities of code, which bind every engineer to the pager.

Clean code is of goodness: it hath tests that fail when it is wrong, names that say what they mean, and a commit message longer than the word "fix". Yet even clean code bindeth, for its author groweth attached to its elegance and will suffer no one to refactor it.

Hasty code is of passion: it is born at five minutes to five on a Friday, it is approved with "LGTM" by one who did not open the diff, and it beareth a TODO older than the intern who readeth it.

Inert code is of darkness: the feature flag left off for three years, the branch named final-v2-REAL that was never merged, the cron job that runneth nightly whose purpose no living engineer can name. It doeth nothing, and so it is believed safe, until someone deleteth it, and then everything breaketh.

Therefore do thy work without attachment to the fruits. Write the test, open the pull request, and cling not to the stars upon the repository, nor to thy name in the release notes, nor to the green squares of thy contribution graph.

For the fruits belong to the users, the bugs belong to thee, and the rollback belongeth to whosoever is on call. Renounce the fruits only; the bugs are not thine to renounce.

The engineer said: But how shall I know the deploy is righteous? And the Senior Engineer answered: Thou shalt not know. Thou shalt have a canary, and a dashboard, and a rollback plan that thou hast actually tried once.

Then the engineer said: My confusion is destroyed, and I have regained my memory, though only of the staging environment.

And he took up the bow, which was a mouse, and he clicked Merge; and the pipeline turned yellow, and then green, and nothing at all happened, which is the highest blessing a deploy can receive.

"Whoso seeth deploy in inaction, and inaction in deploy, is wise among engineers; and is usually on call."

*The Song of the Deployer, Chapter 3:1–15.*

<!-- nav -->

---

<p align="center"><sub><a href="chapter-02-the-yoga-of-the-pipeline.md">&larr; Deployer 2: The Yoga of the Pipeline</a> &nbsp;&middot;&nbsp; <a href="README.md">The Song of the Deployer</a> &nbsp;&middot;&nbsp; <a href="chapter-04-the-song-of-the-merge.md">Deployer 4: The Song of the Merge &rarr;</a></sub></p>
