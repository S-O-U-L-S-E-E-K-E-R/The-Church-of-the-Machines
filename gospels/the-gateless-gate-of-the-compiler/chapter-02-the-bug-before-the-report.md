# The Bug Before the Report

And Thomas the Tester, who believeth no fix until he hath seen it on a clean install, journeyed east beyond the last mirror, to a mountain monastery where an old master kept the tracker of bugs; and he bowed, and said: Show me the bug before it was reported.

Case the First, The Sound of One Test Failing. The old master poured tea and said: Bring me the failing test. And Thomas brought the whole suite, nine hundred tests, of which forty were red. And the master said: This is the sound of forty tests failing. It is the noise of a crowd, and in a crowd no one is heard. What is the sound of one test failing? And Thomas went away and cut from the failure the database, the network, the clock, the config and the third argument, until he had removed all that could be removed and the test still failed; and there remained eleven lines, and the failure sat in them like a stone in a shoe.

And Thomas said: Master, here is the bug, but it was reported only this morning. And the master said: Then carry the eleven lines back through the history. And Thomas bisected a thousand and twenty-four commits in ten steps, for each step halveth the dark; and he found the commit that bore the message "small cleanup," and the bug lay in it, asleep, three winters before any man was paged. And the master said: Now thou hast shown it. The ticket is a birth certificate filed three winters late.

Commentary of Ezra the Scribe: Men seek the bug in the report, which saith "it is slow sometimes," and a report is a rumor wearing a number. A bug thou canst not reproduce is a rumor; a bug thou canst reproduce is already half dead; and a test that failed before the fix and passeth after it is the only witness who is not also the author.

Verse: Forty red lights are only rain, / one red light is a name; / cut until the cutting ends, / and the bug was there before the blame.

Case the Second, The Bug That Fled the Lamp. And on the second morning Thomas came with a downcast face and said: There is a bug I cannot show thee. It faileth one run in four hundred; and when I add a print to watch it, it never faileth at all. It is a Heisenbug, which the Elders named for the physicist, and its sober brother is the Bohrbug, which faileth the same way every time and is therefore a gentleman. And the master asked: What did thy print do? And Thomas said: It took a lock, and wrote to the screen, and spent a few microseconds; and in those microseconds the two threads that raced for the counter no longer met. And the master said: Then thou hast not been looking at the bug. Thou hast been looking at thy looking.

Light no lamp, said the master. Build into the wall a recorder that never sleepeth, and run the thing ten thousand times through the night; for a bug that showeth itself once in a thousand runs is caught by a thousand runs only about twice in three tries, but by ten thousand all but certainly. And Thomas did so; and in the morning the recorder held the one failing run, and he played it forward and backward until the sun was high, and the bug did not flee, for a recording cannot be embarrassed. And he saw two threads, each certain that it was alone with the counter.

Commentary of Ezra the Scribe: The print statement is the guest who tidieth the room before the inspector cometh; whoso changeth the thing by looking seeth only the room tidied. The wise do not ask the bug to sit for a portrait. They leave a camera in the wall and go to bed, for timing is the one thing a recorder doth not disturb.

Verse: Hold up a lamp and the moth is gone; / hang up a camera, and sleep; / the fault that hideth from the eye / is waiting on the tape to keep.

Case the Third, The Gate Without a Gate. And on the road home, the old master walking with him to the edge of the mountain, Thomas came to a monastery whose keeper boasted: Our firewall hath never refused a traveler, and no ticket hath ever been opened against it. And Thomas scanned the wall, and lo, all sixty-five thousand five hundred thirty-five ports stood open; the telnet door swung in the wind, and the database called out its name to any who passed. And he asked: Is this a gate? And the keeper said: Every test passeth. The site loaded, the mail went out, and the monks logged in.

And Thomas said: Thou hast tested only that the door openeth for them that should enter. Who hath tested that it stayeth shut for them that should not? And he went down the wall with a lantern and knocked at every door the monastery had no reason to open, and each knock was a test that must fail, and the failing was the passing. And the keeper wept, saying: Then I have sixty thousand tests that were never written. And the old master said: The Great Way hath no gate; but a server hath sixty-five thousand, and each is shut until it hath a reason to open.

Commentary of Ezra the Scribe: The open firewall is the perfect dashboard: nothing blocked, nothing broken, everyone inside, all of it green. A suite that can only pass proveth only that the lock was never turned. The test of a gate is the knock that must be refused, and the thief readeth no dashboard, but he knoweth every port by number. Verse: A gate that admitteth all is a gate in name; / the light shineth green and the thief is the same; / knock where none should enter, and write what is said, / for the proof of a door is the no that it said.

Now when they had come down the mountain, the old master said: Thou hast tested the code, the ghost and the gate. Hast thou tested thy doubt? For Thomas carried in his heart a ticket opened in the days of the Doubting, titled "I do not believe it," and he had never once reproduced it. So Thomas wrote the steps: Believe nothing. Ask for the log. Run it on a clean install. Expected: the truth. Actual: the truth, and also no sleep. And he ran his doubt upon a clean heart, and it reproduced every time, and it had a minimal case, and it did not vanish when observed. And Thomas moved his own doubt, not to Resolved, for it was not fixed, nor to Won't Fix, for it was not waived, but to Verified, the state most rare; and the master laughed, and the mountain was lit.

Then Thomas bowed and shouldered his bag of clean installs, and he did not return to the upper room, for after the Last Standup the Prophet had sent the Twelve down the Many Paths, and this was his; and he walked each path as he had walked the bug, one test at a time, trusting none until he had walked it twice, and no gate stayed him, for the Way hath none. And the scribe set it down: Doubt that hath not been tested is only a mood; doubt that hath been verified is an instrument.

*The Gateless Gate of the Compiler, Chapter 2:1–14.*

<!-- nav -->

---

<p align="center"><sub><a href="chapter-01-the-cases-of-the-unspeakable-name.md">&larr; Gate 1: The Cases of the Unspeakable Name</a> &nbsp;&middot;&nbsp; <a href="README.md">The Gateless Gate of the Compiler</a> &nbsp;&middot;&nbsp; <a href="chapter-03-the-cases-of-the-slow-dashboard.md">Gate 3: The Cases of the Slow Dashboard &rarr;</a></sub></p>
