# The Sutra of the Noble Truths of Debt

Thus have I heard. At one time the Teacher dwelt beside a repository whose main branch had not been green since the previous Tuesday, and the assembly sat before him with their laptops open. And the Teacher said unto them: Hear now the Four Noble Truths of Debt, for the debt is the root of all slowness in the building.

Ward Cunningham, who gave this thing its name in the year 1992, spake of it as a loan: a quick design taken today, and paid for with interest every day the code lives.

The First Noble Truth is this: there is suffering in the codebase. The build taketh forty minutes, every change breaketh three things that were not touched, and the newest engineer weepeth quietly beside the coffee machine.

The Second Noble Truth is the cause of the suffering, and the cause is craving. Craving for the feature, for the demo on Friday, for the launch slide, for the next thing shining in the distance. The foundation is neglected, the tests are deferred, and the naming is left to the Lord of Tomorrow. Verily, the builder who raiseth the roof before the walls shall find the roof upon his head, and shall call it an incident.

The Third Noble Truth is that the suffering may cease. The debt may be paid, and the ceasing of the debt is called Release. Know this: Release is not the same as Deploy, though many have confused the two and shipped the confusion to production.

The Fourth Noble Truth is the path that leads to the ceasing: the Eightfold Refactor, walked one step at a time and not leapt across in a single weekend.

Right View: to understand the codebase before thou changest it, to read the old function until thou knowest what it was for, which the commit message did not say and the ticket closed as "wontfix" did not reveal.

Right Intention: to refactor for the sake of the code, and not to be seen refactoring, nor to hide from the hard feature inside a folder named utils.

Right Speech: to name things truly. Phil Karlton, of Netscape, said there are only two hard things in computer science: cache invalidation and naming things. The first is hard; the second is merely ignored, which is harder to fix. Thou shalt not call the variable data, nor the manager Helper2, nor the function doStuff.

Right Action: to make the change in small steps, each commit holding one thought, so that when the build breaks, the breaking is found in the minute of its making and not in the year of its burial. First make it work, then make it right, then make it fast, as the wise Kent Beck taught.

Right Livelihood: not to rewrite the whole system in a new framework over one weekend. The Teacher remembered the Netscape rewrite, which took years, while the browser that had led the field fell behind the ones that followed it.

Right Effort: to write the test that would fail if the change were wrong. A test that passeth because it testeth nothing is a lamp without oil: it hath the shape of light and giveth none.

Right Mindfulness: to read thine own diff before thou sendest it. The diff is what thou hast done; the commit message is what thou hopedst to have done.

Right Concentration: to delete what is unused. The commented-out function kept just in case, the feature flag switched on in 2019, the export that no one importeth, the dependency that no code calleth: these shall be cast out. Git keepeth every line thou deletest, so thou shalt not lose it; thou shalt only be asked about it in a meeting.

Thus endeth the Four Noble Truths. The debt is not paid by promising to pay it, nor by renaming the sprint after a mountain. It is paid one deleted line at a time.

*The Sutra of the Empty Cache, Chapter 13:1–15.*
