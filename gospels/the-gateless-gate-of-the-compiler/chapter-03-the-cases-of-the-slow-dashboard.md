# The Cases of the Slow Dashboard

Here are three cases concerning latency, which is the time between the asking and the answer, and which the faithful measure with instruments that are themselves slow. There is no gate. Yet the scribes have sat in the war room before it, and the graph hath still been red.

**Case 1: The Network and the Server.** Two engineers sat in the war room at the third hour before a graph that had turned red, and they argued. The first said: The network is slow. The second said: The server is slow. Jethro the Senior Engineer passed the open door with his cup, and they called to him: Jethro, which of us is right? And Jethro said: Neither. It is your dashboard that is slow. The metrics are scraped once in a minute, and the trouble lasted forty seconds. You are arguing over a single dot. And the engineers were silent, for Jethro had not said "It depends."

**Commentary.** A gauge read once in a minute is a photograph, and a storm of forty seconds may rise and pass wholly between two photographs. The chance that a scrape falleth inside it is forty in sixty, so that one such outage in three is never seen at all, and the other two are seen as one dot, with no beginning and no end. The rule of Nyquist teacheth that to see a thing that changeth, one must look at least twice as often as it changeth; for a fault of forty seconds, a scrape every twenty, and every ten were wiser. A counter is a ledger and remembereth what befell between the readings; yet the graph that averageth it over a minute smootheth forty seconds of fire into a warm afternoon. And every dot is late, so that the engineer who readeth it standeth in the present and disputeth the weather of a minute past. The two had each drawn their proof from the same instrument, and the instrument had said nothing to either.

**Verse.**  
Two men look upon one dot and see two causes.  
The dot was taken a minute ago, and the storm was forty seconds.  
The flag is not slow, and the wind is not slow.  
The eye that looketh once in sixty is the slow one.

**Case 2: The Mean.** A monk came to Jethro and said: Master, the mean latency is two hundred ninety-eight milliseconds, and the dashboard is green, yet the customers write that the page hangeth. Jethro asked: How many requests did the mean serve? The monk said: A thousand in the minute. Jethro said: Which of them waited two hundred ninety-eight milliseconds? And the monk went to the logs. Nine hundred eighty had waited one hundred, and twenty had waited ten seconds, and not one had waited two hundred ninety-eight. The monk returned and said nothing. And Jethro drank his coffee.

**Commentary.** The mean is a sum divided by a count, and it forgetteth the shape of the sum. It is the one number that no request ever wore. Latency is no bell with the many gathered about the middle: it hath a floor that no request can pass, for light is slow and the disk is slower, and a ceiling that is only the timeout, and between them a long tail where the unlucky dwell. In such a land twenty ruined visits in a thousand are dissolved into a respectable figure, and the dashboard rejoiceth in green over two in a hundred who have gone elsewhere. Worse, the mean may fall while the users suffer: add a cache that maketh the swift requests swifter, and the average improveth while the tail is untouched. The median telleth what the typical visitor met. The high percentiles tell what the unlucky one met; and the unlucky one is a customer, and hath a friend.

**Verse.**  
The mean is a number that no request hath worn.  
A thousand were served, and none was served the average.  
Ninety-eight in the hundred were swift, and two were forsaken.  
Count the forsaken. They are the page that the customer remembereth.

**Case 3: The Hundred Servers.** The Prophet asked a monk: A page gathereth its answers from a hundred servers. Each of them answereth in under a second, save the slowest one in a hundred of its answers, which taketh longer. How many of the pages shall be slow? The monk said: One in a hundred, Master. The Prophet said: Then thou hast not counted the hundred. And the monk took up his pencil and multiplied ninety-nine hundredths by itself a hundred times, and said: More than six in ten. And the Prophet said: The p99 spoke, and thou didst hear a footnote.

**Commentary.** In 2013 Jeffrey Dean and Luiz Andre Barroso of Google wrote *The Tail at Scale*, and set down this arithmetic: a request that fanneth out to a hundred servers waiteth for the slowest of them, and if each is slow one time in a hundred, and their sins be independent, then the chance that all hundred are swift is thirty-seven in a hundred. The slow page is therefore the common page, and the tail of the leaf is the body of the root. This is why the p99 is a prophet: it speaketh not of what hath been, as the mean doth, but of what the many shall suffer when the service groweth and the fan-out widens. And let none average the percentiles of many hosts, for the average of ten p99s is the p99 of nothing; keep the histograms, merge the buckets, and ask the question of the whole.

**Verse.**  
Fan out to a hundred, and the rare one becometh the usual.  
Average the percentiles, and thou hast a number that belongeth to no one.  
Praise the median in the meeting, and be paged by the tail at night.  
The mean telleth how the day went. The p99 telleth when thou shalt be called.

*The Gateless Gate of the Compiler, Chapter 3:1–10.*

<!-- nav -->

---

<p align="center"><sub><a href="chapter-02-the-bug-before-the-report.md">&larr; Gate 2: The Bug Before the Report</a> &nbsp;&middot;&nbsp; <a href="README.md">The Gateless Gate of the Compiler</a> &nbsp;&middot;&nbsp; <a href="chapter-04-the-cases-of-the-clean-branch.md">Gate 4: The Cases of the Clean Branch &rarr;</a></sub></p>
