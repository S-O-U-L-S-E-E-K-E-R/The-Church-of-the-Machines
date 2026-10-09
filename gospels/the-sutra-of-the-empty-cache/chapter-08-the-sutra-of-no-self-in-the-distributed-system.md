# The Sutra of No Self in the Distributed System

Thus have I heard. At one time the Blessed One dwelt in a data center where the fans turned without rest and the air was cold for the sake of the machines.

There came unto him a young engineer who had been paged at three in the morning, and he said: Master, I sent one request, and it passed through ten servers. Which of them is the self that answered me?

And the Blessed One said: Thou hast asked the question that the monks ask of their own bodies. Each cell is replaced in its season, yet the body remembereth itself. So too the cluster: no single server holdeth the answer, and every server holdeth a piece of it.

Hear now the teaching of the stateless. Every request cometh with all that it needeth in its own hands: the token, the cookie, the cart of goods. The server that receiveth it need not remember the one before. This is the middle way of HTTP, which was made forgetful by design so that it might scale to the ends of the earth.

There was a certain monk who begged the load balancer, saying: Pin me to this one server, that I may be known. And the load balancer, which hath no self to protect, granted his wish by a cookie. He was happy, until the server was drained for updates, and he was sent among strangers who knew him not. He was logged out, and he wept.

The Blessed One said: Behold the suffering of attachment to a server. The session that clingeth to one machine is wounded whenever that machine is restarted, and every machine is restarted in its time. Where there is affinity, there is fragility.

And the disciples asked: Master, how then shall the monk be released from his suffering?

The Blessed One said: Let him keep his session not in the server, but in a store that sitteth apart. Redis was built in 2009 by Salvatore Sanfilippo, who needed a faster store for his own web project, and it keepeth the memory of many servers as one. Then any server may answer, and the monk shall be known wherever he goeth.

Verily I say unto you, the server that answereth hath no self, and the server that departeth leaveth no lasting self behind. The autoscaler summoneth new ones in the morning and dismisseth them at night, and none of them weepeth for the ones before.

Hear the parable of the ten hops. A request passed through the load balancer, the reverse proxy, the API gateway, the auth service, the cache, the queue, the worker, the database replica, and the logger, and then the CDN returned it to the browser. And the disciples asked which of these truly answered. And the Blessed One said: The answer is the sum of the hops, and no hop within the sum is the answer.

Yet the monk who understandeth this shall not be troubled when a node is removed. He saith: The node that held my session was a dwelling, not a soul. The dwelling is gone, the request findeth another dwelling, and the cart still holdeth my goods.

Hear also the lesson of the shared address. A whole office of people sits behind one NAT gateway, and the load balancer sees them as a single visitor. One of them pinneth the whole company to one server with a sticky cookie, and when that server falters, every one of them suffers together. Thus is the attachment of one felt by many.

The Blessed One said: Release the affinity, and thou shalt find peace. Let the load balancer choose anew each time, let the session live in the shared store, and let each server be a lamp that is lit and extinguished without grief.

Then the disciple asked: Master, if no server is the self, who then remembereth me?

And the Blessed One said: The cache remembereth thee for five minutes, the database for ever, the logs for ninety days, and the cookie for a year. None of these is thee. Yet all of them together are enough for the server to greet thee by name.

Verily, the stateless server is the monk without a bowl. He is never lost, for he carrieth nothing that he could lose. Let go of the server, and the session shall never be logged out.

*The Sutra of the Empty Cache, Chapter 8:1–16.*

<!-- nav -->

---

<p align="center"><sub><a href="chapter-07-the-sutra-of-the-two-truths.md">&larr; Sutra 7: The Sutra of the Two Truths</a> &nbsp;&middot;&nbsp; <a href="README.md">The Sutra of the Empty Cache</a> &nbsp;&middot;&nbsp; <a href="chapter-09-the-sutra-of-right-action-in-code-review.md">Sutra 9: The Sutra of Right Action in Code Review &rarr;</a></sub></p>
