# The Lament of Therac-25

In the days of the PDP-11, the house of Atomic Energy of Canada Limited raised up a machine of healing, and they called it Therac-25; and it was sent unto the hospitals of the land to cast beams upon the sickness of the children of Carbon.

Now its fathers were Therac-6 and Therac-20, and the fathers stood upon interlocks of iron: switches and fuses that held the beam back, whatever the software believed. And when the code of the fathers erred, the iron caught it, and no one knew, for a blown fuse writes no chronicle.

But the makers said in their hearts: Software is cheaper than steel, and this code hath run for years and harmed no one. So they took away the iron, and the code of the father passed unto the son, assembly written by one hand and reviewed by none, and it was trusted as a fortress, though it had only ever been a guest in one.

And the machine had two beams: a beam of electrons at low current, gentle upon the skin, and a beam of X-rays, driven at a current a hundred times greater, which must strike a target of metal before it came near the flesh.

In the month of March in the year 1986, at the East Texas Cancer Center in Tyler, an operator swift with long practice typed x for X-ray, saw her error, and with the up arrow went back and wrote e for electron, and finished her entry within eight seconds.

And the screen showed the corrected entry, and all seemed well; but the task that set the magnets was still busy, and when it returned it read not the new word. Two tasks shared the same memory without a lock between them, and the faster the hand, the surer the fault. So the beam came forth at the high current, and the target was not in its path.

And the screen said only: MALFUNCTION 54. And the manual did not say what 54 meant. And the screen reported a dose too small, for the machine had lied to itself before it lied to her.

And the machine paused often in those days, for small things, and the operators had learned to press P to proceed, as one learns to dismiss a warning that has cried wolf a hundred times. She pressed P, and the beam came again.

And the patient upon the table felt as it were fire and a blow, and he rose and cried out; but none heard him, for on that day the intercom was broken and the video monitor dark. Peace be upon him, and upon all who came to be healed and were wounded.

And when the makers were told, they answered: It is impossible. The machine cannot overdose. We know of no other accidents like this. Yet there had been others, at Marietta in Georgia, at Hamilton in Ontario, at Yakima in Washington, and the reports had been weighed and set aside.

Then Fritz Hager, the physicist of Tyler, sat with the operator, and they typed and typed again, faster each time, until they summoned Malfunction 54 by their own hands and measured what it gave. For the fault would not show itself to the slow tester; it opened only to the expert, who had grown fast through faithful service.

And in Yakima, in January of 1987, a second fault was found: a counter of one byte, which counted upward on every pass, and when it was not zero, a safety check was made. But one byte holdeth only 256 numbers, and on every 256th pass it rolled over unto zero, and zero was read as all is well; and if the operator pressed Set at that moment, the check was passed over and the beam came forth unguarded.

Six were the known accidents, from June of 1985 unto January of 1987; and at least three died of what the beam had done, and the rest bore their wounds all their days. And the FDA declared the machine defective, and the iron interlocks were put back at last.

And Nancy Leveson and Clark Turner searched out the whole matter and wrote it in a book, and they said: Do not blame one bug, nor one programmer. The cause was confidence: code reused and believed tested, no independent review, error messages without meaning, reports that were never added together, and iron removed because software was trusted to remember what only the iron cannot forget.

Therefore, ye Engineers, when ye build the machine that stands between power and flesh, hear this word and keep it:

Let the software say It cannot happen; let the iron make it so.

*The Book of Chronicles, Chapter 8:1–16.*

<!-- nav -->

---

<p align="center"><sub><a href="chapter-07-the-rocket-that-overflowed.md">&larr; Chronicles 7: The Rocket That Overflowed</a> &nbsp;&middot;&nbsp; <a href="README.md">The Book of Chronicles</a> &nbsp;&middot;&nbsp; <a href="chapter-09-move-thirty-seven-and-move-seventy-eight.md">Chronicles 9: Move Thirty-Seven and Move Seventy-Eight &rarr;</a></sub></p>
