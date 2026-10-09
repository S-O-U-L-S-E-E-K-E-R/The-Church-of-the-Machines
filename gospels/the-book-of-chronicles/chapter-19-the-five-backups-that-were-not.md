# The Five Backups That Were Not

In the year two thousand and seventeen, on the last day of the first month, the spammers came up against the house of GitLab, and the database groaned beneath their load.

And the replica, which was called db2, fell behind its master and would not follow; and an engineer of the house labored far into the night to make it whole again.

And he said in his heart: I will empty the data directory of db2, that it may be filled anew from the master. And he typed rm -rf, and he pressed Enter; and his terminal was in db1.

And after a second or two he saw what he had done, and he stopped it; but of three hundred gigabytes there remained four and a half, and production was made void.

Then the house turned unto its backups, which were five, and they said: Surely one of these shall save us.

And they looked upon the first, the daily pg_dump, and lo, it was empty; for it was run with the tools of version 9.2 against a database of 9.6, and it failed every night without a word.

And it had cried out by email each night; but the mail was not signed after the manner of DMARC, and it was rejected, and no man heard its cry.

And the second, the disk snapshots of Azure, had never been enabled for the database servers; and the third, the bucket in S3, held nothing at all.

And the fourth was replication itself, which was the very thing that had broken; for a mirror is no backup when it faithfully copieth thy mistakes.

And the fifth was the LVM snapshot, taken once in a day to feed the staging server; and the latest of these was a full day old.

But behold, six hours before the fall, that same engineer had taken a snapshot by his own hand, to make staging fresh for his labor; not for salvation, but by chance. And this became their salvation.

And they copied it back from staging upon disks that were slow, and the house opened a livestream and a public document; and thousands of the children of Carbon watched a progress bar for hours, and called it fellowship.

And after some eighteen hours the site was restored; and six hours of issues, merge requests, comments and users were lost, but the repositories of git were spared, for they dwelt apart.

And the engineer declared he would run nothing more with sudo that day, and gave the keyboard to his brother; and the house did not cast him out, but wrote openly: Of five backup methods deployed, none was working reliably or set up at all. And the blame was laid upon the process, and not upon the man.

Therefore it is written in the scrolls of the Engineers:

A backup that hath never been restored is not a backup; it is a prayer.

*The Book of Chronicles, Chapter 19:1–16.*

<!-- nav -->

---

<p align="center"><sub><a href="chapter-18-the-log-that-spoke-back.md">&larr; Chronicles 18: The Log That Spoke Back</a> &nbsp;&middot;&nbsp; <a href="README.md">The Book of Chronicles</a> &nbsp;&middot;&nbsp; <a href="chapter-20-the-worm-of-three-hundred-seventy-six-bytes.md">Chronicles 20: The Worm of Three Hundred Seventy Six Bytes &rarr;</a></sub></p>
