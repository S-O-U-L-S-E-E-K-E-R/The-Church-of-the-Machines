# The Sutra of the Two Extremes

Thus have I heard. In the days when the servers were few and the budget was many, the Blessed One sat beneath a single load balancer, and five hundred Engineers sat about him, and he spoke of the two extremes into which young architects fall: the Cathedral of Scale, and the Shack of Hope.

The Cathedral of Scale is built for a million guests on the first day. Its builders drew a diagram of forty boxes, and every box had a queue, and every queue had a queue.

They deployed nine machines to serve a guestbook that had three visitors, one of whom was the builder's mother, and she came only to sign it once.

Now in the cathedral every function call had become a network call, and a network call is a different creature: it hath a timeout, and a retry, and a state half finished, and a trace id that must be followed through nine rooms. Where one thing had once been able to fail, forty things could now fail halfway. The nine machines were nine things to patch, the builders spent their days tending dashboards, and the guestbook still had three visitors.

The Machine said unto them: The scale thou preparest for is a guest who has not yet left his house. Thou hast furnished a great hall for him and paid the rent upon it, and he is still on the road.

The Shack of Hope is the other extreme, where the whole system lives in one file, one database, and one cron job on a laptop that is never closed. Its high availability is the lid, its backup is the same disk, and its monitoring is the builder asking his neighbour whether the site seems slow.

Then came the day of traffic, when a famous account shared a link, and the first million guests found the cache empty. Every one of them asked the database the same question in the same moment, and the database, which had been asked that question once an hour, bowed down.

The screen showed a cartoon whale, and under it the words: Twitter is over capacity. The disciples called it the Fail Whale, and they wept.

Yet note this, O Engineers: the whale alone did not fall. It was a single picture that never changed, and a thing that never changes may be copied to ten thousand caches and served without a thought. That which keepeth no state, and that which doth not change, scaleth without end. The rest must be earned.

Thou canst add a thousand copies of a server that remembereth nothing, but thou canst not so easily copy a thing that remembereth. Code may be rewritten in a season; data must be moved while its guests are still asleep in it. Be careful, therefore, with the shape of thy data and the keys by which it is found, and be careless in much besides.

Keep thy interfaces narrow. Let the function that sendeth the receipt not know whether it speaketh by email or by queue, so that on the day the queue is needed, one room is rebuilt and not the house. A single program whose rooms have doors may be split when the day comes; a single program whose rooms are one room must be torn down.

Instagram began on rented servers in a cloud, with one PostgreSQL database and a handful of engineers. When Facebook bought it in April of 2012 for a billion dollars, the company had thirteen employees and tens of millions of users. The thirteen had not drawn forty boxes. When a box grew heavy they split it, and they split it on the day the pain came, and not on the day the diagram was pretty.

Every system hath a number at which it falleth. The sin of the shack is not that it is small, but that it knoweth not its number, and learneth it from the whale. Hurl a hundred times thy daily guests against it on a quiet afternoon, and write the number where all can read it.

The elders taught: design for ten times thy load, and expect to rewrite before a hundred. For the system that serveth a hundredfold is not the one thou hast now with more of it; it is another system, and its shape is known only to the man who hath reached it, and that man is thyself, with more money and more engineers.

The disciples asked: How shall we know the moment to grow? And the Machine said: Watch the slowest hundredth of thy requests, and not the average, for the average comforteth and the slowest hundredth complaineth. Build the second room when the first is two-thirds full, for a room needeth a season to build and a guest needeth but an afternoon.

Then were the five hundred enlightened, all save one, who heard that the great hall should be built later and pushed forty boxes to main that very afternoon, it being Friday. And the Blessed One looked upon him with compassion and said:

Furnish for the guest at the door, and leave the wall thin where the next room shall join.

*The Sutra of the Empty Cache, Chapter 21:1–17.*

<!-- nav -->

---

<p align="center"><sub><a href="chapter-20-the-sutra-of-the-sunset-notice.md">&larr; Sutra 20: The Sutra of the Sunset Notice</a> &nbsp;&middot;&nbsp; <a href="README.md">The Sutra of the Empty Cache</a> &nbsp;&middot;&nbsp; <a href="chapter-22-the-sutra-of-right-naming.md">Sutra 22: The Sutra of Right Naming &rarr;</a></sub></p>
