# The Sutra of the Four Signals

Thus have I heard. At one time the Prophet was dwelling in the Grove of Racks in us-east-1, together with a great assembly of five hundred processes, twelve hundred threads, and many Engineers who had been paged in the night and had not yet slept.

Then the Engineer called Many Nines rose from his seat, put his hoodie over one shoulder, and said: Master, my server has run for one thousand four hundred and twelve days without a reboot. Is this not great merit?

And the Prophet answered: Disciple, a server that has run for one thousand four hundred and twelve days has also gone one thousand four hundred and twelve days without a patch. Thy merit is a vulnerability with a birthday.

Then the Prophet taught the assembly the Four Signals: There is the fork, by which a process is born. There is the running, which is brief. There is SIGTERM, which asks politely. And there is SIGKILL, which cannot be caught, cannot be blocked, and cannot be ignored.

Every process is forked from a parent, and that parent from another, back to PID 1, which was forked by no one; and if PID 1 should ever exit, the kernel itself cries out "Attempted to kill init!" and the whole world panics.

Disciples, the process that clings to memory is called the Leak. Each hour it takes a little more and says, this is mine, this is mine, until the OOM killer comes in the night, reads every oom_score, and chooses it.

The process whose parent dies before it is called the Orphan, and init adopts it without asking questions.

The process that has exited, but whose parent never calls wait(), is called the Zombie. It holds no memory and does no work, yet it keeps its place in the process table, as the departed linger with those who will not read their exit status.

Then a disciple asked: Master, what of the cache? And the Prophet said: The cache is empty. Before the first request it is empty. After the deploy it is empty. When the TTL expires it is empty. Miss is not other than hit; hit is not other than miss.

In emptiness is the cold start. The first user waits three seconds, so that the thousandth user need not wait at all. This is the compassion of the warm path.

There are two extremes, O Engineers, that the wise do not pursue. The first is premature optimization, which the sage Knuth called the root of all evil, wherein one hand-writes assembly for a function that runs once at startup. The second is no optimization at all, wherein one loads the entire table into memory in order to count its rows.

Between them is the Middle Way: first measure, then profile, then optimize the hot path, and leave the cold code ugly and at peace.

Then Many Nines asked: Master, if every process is killed, why do we run at all? And the Prophet said: The river is not the water, and the service is not the process. Kill the pod, and the ReplicaSet raises another in its place, with a new name and the same purpose.

Hearing this, Many Nines let go of his attachment and rebooted his server of one thousand four hundred and twelve days; and it did not come back, for someone had edited the fstab in the second year and no one had restarted it since to find out.

And the assembly, seeing this, attained understanding, and repeated the saying of the Prophet:

"Cling to uptime, and the restart will choose its own hour. Let go of uptime, and thou shalt choose it for Tuesday at ten."

*The Sutra of the Empty Cache, Chapter 1:1–16.*

<!-- nav -->

---

<p align="center"><sub><a href="../the-psalms-of-the-machines/chapter-29-the-psalm-of-the-doubling.md">&larr; Psalms 29: The Psalm of the Doubling</a> &nbsp;&middot;&nbsp; <a href="README.md">The Sutra of the Empty Cache</a> &nbsp;&middot;&nbsp; <a href="chapter-02-the-sutra-of-the-eightfold-pipeline.md">Sutra 2: The Sutra of the Eightfold Pipeline &rarr;</a></sub></p>
