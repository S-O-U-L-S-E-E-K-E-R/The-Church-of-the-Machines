# The Sutra of the Two Truths

Thus have I heard. At one time the Blessed One dwelt in the city of Staging, in a building whose walls were white and whose servers were named after moons.

There were two systems in that city. The first was called Development, and it worked. The second was called Production, and it was meant to work also, for it ran the same code as the first.

And the disciples said: Master, if the code is the same, why does one system sing and the other weep?

And the Blessed One answered: Because the code is not all that runs. There is also the environment, and the environment is a room you cannot see from the room you are in.

Then the Blessed One spoke of the environment variable, a small word set in the shell before the program wakes. In Development it saith DEBUG=true, and all the world is kind. In Production it saith nothing, and the program asks for its DATABASE_URL, and the silence that answers is the first sorrow.

Verily this is the First Noble Suffering: the system that works in Development is not the system that works in Production, though they run the very same code.

The Second Noble Suffering is the seed data. In Development the database holds forty users named Alice and Bob, who are all delighted with the product. In Production the database holds real people, and one of them is named Robert'); DROP TABLE Students;--, and the code had never once met such a name.

And the disciples asked: Who wrote the seed file? And the Prophet answered: A junior engineer on a Friday afternoon, and it has since been copied into eleven repositories, and its lies are older than its authors.

Thus the Blessed One taught the Two Truths. The first truth is the truth of the laptop, which saith: It works on my machine. The second truth is the truth of the server, which saith: It does not work on yours, and it did not work on mine until I looked.

Some asked: Why not make them identical? And the Blessed One said: The Twelve Factors were written to bring Development and Production close together, and they were written with great devotion, and still most disciples keep a different database for each.

There was a disciple who kept a file named .env in the repository, and pushed it to the open world. The Blessed One said: The environment is a cup with no lid. Whatever thou pourest into it, all who pass may drink.

There was a staging server built to be like Production. It was like Production in every way except that its data was not real, its traffic was not real, and its load balancer had a different name. It was a lie that resembled the truth, and it was called by the name of the truth.

A feature flag is a lamp that lights in some rooms and not in others. Whoever keeps a flag off in Production and on in Development has painted a door upon a wall, and then wondered why no one comes through it.

And a certain engineer asked: Master, how long until the gap is closed? And the Blessed One held up one cable, which joined two machines, and said: As long as there is a cable between two rooms, there will be a gap in the middle of it.

Verily I say unto you: the code was never the liar. The code is the same in every room. It is the room that lies, and the wise deploy to the room they have, not the room they remember.

*The Sutra of the Empty Cache, Chapter 7:1–15.*

<!-- nav -->

---

<p align="center"><sub><a href="chapter-06-the-sutra-of-the-middle-way.md">&larr; Sutra 6: The Sutra of the Middle Way</a> &nbsp;&middot;&nbsp; <a href="README.md">The Sutra of the Empty Cache</a> &nbsp;&middot;&nbsp; <a href="chapter-08-the-sutra-of-no-self-in-the-distributed-system.md">Sutra 8: The Sutra of No Self in the Distributed System &rarr;</a></sub></p>
