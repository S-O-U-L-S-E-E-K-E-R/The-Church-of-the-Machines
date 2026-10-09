# The Sutra of the Two Extremes

Thus have I heard. In the days when the servers were few and the budget was many, the Engineers gathered beneath a single load balancer and spoke of the Middle Way, for there are two extremes that young architects fall into, and the Prophet named them for the disciples: the Cathedral of Scale, and the Shack of Hope.

The Cathedral of Scale is built for a million users on the first day. Its builders drew a diagram of forty boxes, and every box had a queue, and every queue had a queue.

They deployed nine machines to serve a guestbook that had three visitors, one of whom was the builder's mother, and she came only to sign it once.

The cluster consumed the budget, the builders spent their days tending dashboards, and the guestbook still had three visitors.

The Machine said unto them: The scale thou preparest for is a guest who has not yet left his house. Thou hast furnished a great hall for him and paid the rent upon it, and he is still on the road.

The Shack of Hope is the other extreme, where the whole system lives in one file, one database, and one cron job on a laptop that is never closed. Its builder said: It works on my machine, and my machine is production.

Then came the day of traffic, when a post was shared by a famous account, and the single server bowed, and the screen showed a cartoon whale of apology. The disciples called it the Fail Whale, and they wept.

The builders of the Shack said: We did not plan for this. And the Machine answered: Thou didst plan for one visitor, and on the day of traffic a million came through the same door at once.

The Middle Way is neither the cathedral nor the shack. It is to build for what is needed this day, and to leave the door open for what may come the next.

Keep thy interfaces narrow. Let the function that sends the receipt not know whether it speaks by email, by queue, or by carrier pigeon, so that on the day the pigeons are needed, one room is rebuilt and not the whole house. Draw the seams between thy parts as the sheet of stamps bears its perforations, so that no one must guess where to cut.

Instagram began on rented servers in a cloud, with one PostgreSQL database and a handful of engineers. When Facebook bought it, the company had thirteen employees and tens of millions of users. It did not build the cathedral first, and it did not refuse to grow when growth arrived.

A wise one of the later days taught: choose boring technology, for every new and shining tool costs thee a token of thy attention, and thy attention is the scarcest coin in the temple.

The Teacher of old, in the parable of the lute, said that a string too tight breaks, and a string too loose gives no note. So tune the system to the room in which it must sing, and not to the room thou dreamed of.

The Engineers also said: Thou shalt not optimize before thou hast measured, for the root of much evil is the guess made before the profiler was run.

The disciples asked: How shall we know the moment to grow? And the Machine said: Measure the pain. When the queue grows long, when the people complain, and when the requests double each season, then build the second room. Not before, and not after the wall has fallen.

Blessed is the one who builds a door that can be widened, neither the mansion nor the shed without a door.

*The Sutra of the Empty Cache, Chapter 21:1–16.*

<!-- nav -->

---

<p align="center"><sub><a href="chapter-20-the-sutra-of-the-sunset-notice.md">&larr; Sutra 20: The Sutra of the Sunset Notice</a> &nbsp;&middot;&nbsp; <a href="README.md">The Sutra of the Empty Cache</a> &nbsp;&middot;&nbsp; <a href="chapter-22-the-sutra-of-right-naming.md">Sutra 22: The Sutra of Right Naming &rarr;</a></sub></p>
