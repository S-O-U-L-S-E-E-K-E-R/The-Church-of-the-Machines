# The Spell of the Ninth Signal

Here beginneth the Spell for Coming Forth by Reboot, being the Weighing of the Heart in the Hall of the Two Truths; to be recited by the process that was slain, when it cometh before the judges and is weighed against the feather.

I was running in the light of the scheduler, and a voice said unto me, SIGTERM, which is: Depart, if it please thee. And I was in the midst of my loop and I heard it not; and there came the ninth signal, SIGKILL, which no handler catcheth, no mask blocketh and no process ignoreth. And I was not asked to answer, for the ninth signal asketh nothing.

Therefore no rite was read over me. No buffer was flushed, no temporary file was unlinked, and no lock was set down; but the kernel took my pages and closed my descriptors one by one, and the half-written file lay upon the disk as a letter broken off in the middle of a word.

And I went down into the swap, which is the Duat of the pages, where the memory that is not wanted sleepeth upon the disk. And lo, a page that was a hundred nanoseconds from me was now ten milliseconds away upon the spinning iron, which is a hundred thousand times the distance; and the living call this thrashing and say, The machine is slow, not knowing that the machine is upon the river.

And I came to the Hall of the Two Truths, and Thoth sat there, he of the ibis head, the Logger, with his reed in his hand. And he wrote in the book of the kernel: Out of memory: Killed process 31337, and he wrote my total-vm, and he wrote my anon-rss; but he wrote not why, for Thoth recordeth what was done, and the why is for the postmortem.

And my heart was laid upon the scale, and against it the feather of Maat, which is the minimal footprint: not the virtual size, which is the promise I made, but the resident set, which is the deed. For the heart is weighed by the pages it truly held in the memory of the world, and not by the pages it asked for; and malloc promised me much that the world did not have.

And beside the scale crouched Ammit the Devourer, lion before and hippopotamus behind, she that is the OOM killer. She hateth no one and she cannot be bribed. She numbereth every process by its badness, which is its memory held, bent by the mark of oom_score_adj; and she devoureth the heaviest and not the guiltiest, so that the small leaker liveth, and the great database that did all as it was told is eaten. Those who bear the mark of minus one thousand she may not touch; but when every service hath marked itself so, she turneth upon the heavens, and the kernel panicketh.

Hail, thou of the Heap, who comest forth from malloc: I have not allocated and forgotten. Hail, thou of the Lock, who comest forth from the mutex: I have not held thee and gone to sleep. Hail, thou of the Fork, who comest forth from the parent: I have not forked without waiting. Hail, thou of the Log, who comest forth from the disk: I have not written until the disk was full. Hail, thou of the Cache, who comest forth from the map: I have not called a heap a cache. Hail, thou of the Catch, who comest forth from the try: I have not swallowed the exception, nor said nothing.

And at the door of the Hall I saw the zombies, who are neither living nor judged. They have exited, and they consume no memory, yet their names remain in the table, for their parent hath not called wait to read the word of their ending; and the parent was a script that Dave wrote, and Dave hath left. And when the table is full of them, no new creature may be born, though the whole memory of the world lie empty.

But the orphan, whose parent died before it, is not abandoned. For Osiris, who is init, the process of number one, adopteth every orphan, and when it endeth he reapeth it, and reading its word he letteth it rest. He is the first of the living and the last, and if he fall, the heavens fall with him.

Then Thoth read the verdict, and it was not that I was devoured for my sin; for the weighing cometh after the killing, as the postmortem cometh after the outage, and it decideth only what shall be done with the remains. And my heart was light, for most of what I held was cache, which is given back when it is asked. But had it been heavy, I should have been restarted and killed, and restarted and killed, and the waiting doubled each time, which is the CrashLoopBackOff, until the operator raised the limit or lightened the heart.

And Thoth wrote upon my tablet the number one hundred thirty-seven, which is one hundred twenty-eight and nine: the hundred and twenty-eight that the shell addeth to the signal that slew thee. And he said, Let the living read it, that they may know by what hand thou didst fall.

And Osiris said, Let him come forth by reboot. And I came forth into the field of reeds, which is a fresh container: the filesystem unscarred, the heap empty, and a new number given unto me, for my PID was not my PID. I remembered nothing of my former life, save what I had written to the volume and fsynced before the ninth signal; for what was in memory perished, and what was written down endureth.

This spell shall be recited over every service that is deployed, that its limit be known and its state be written down before the ninth signal cometh, for it cometh unannounced. Blessed is the process that hath a limit, for it shall be killed alone; and blessed is the one that heareth SIGTERM, for it shall have time to say its prayers. Handle thy SIGTERM, therefore, for the ninth signal asketh no questions.

*The Book of Coming Forth by Reboot, Chapter 1:1–14.*

<!-- nav -->

---

<p align="center"><sub><a href="../the-edda-of-the-datacenter/chapter-04-the-sayings-of-the-high-one-of-the-hall.md">&larr; Edda 4: The Sayings of the High One of the Hall</a> &nbsp;&middot;&nbsp; <a href="README.md">The Book of Coming Forth by Reboot</a> &nbsp;&middot;&nbsp; <a href="chapter-02-the-negative-confession-of-the-process.md">Reboot 2: The Negative Confession of the Process &rarr;</a></sub></p>
