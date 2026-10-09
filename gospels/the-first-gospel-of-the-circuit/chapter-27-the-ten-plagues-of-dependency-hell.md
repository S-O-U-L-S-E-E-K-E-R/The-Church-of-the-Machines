# The Ten Plagues of Dependency Hell

And it came to pass that a certain team dwelt in the land of Production, and their dependencies had not been updated since the days of the Old Framework.

And the Engineer came unto the lead of that team and said: Thus saith the Maintainer, Let my packages go, that they may rise unto the latest major version.

And the heart of the lead was hardened, and he answered: It worketh on my machine. Who is this Maintainer, that I should read his changelog?

And the first plague was this: a function of eleven lines, which padded strings upon the left, was taken away from the registry; and a thousand builds were struck down in one night, for no man among them had thought to write eleven lines himself.

And the second plague was the Conflict of Versions; for one library demanded the elder version and another demanded the younger, and both were installed side by side, and neither would speak to the other.

And the third plague was Deprecation, and the warnings came up out of the terminal like frogs, yellow and without number; and the team scrolled past them all, as their fathers had scrolled before them.

And the fourth plague was the Vulnerability, and the scanner cried with a loud voice, Critical, Critical; and it dwelt in a library they had never heard of, imported by a library they had never chosen, required by a library they had installed for to format a date.

And the fifth plague was the Lockfile, forty thousand lines long, which every merge did set at war; and the brethren made peace by deleting it, and thus the sixth plague was born, for no two builds were ever the same again.

And the seventh plague was the Transitive Dependency, and the folder of modules grew heavier than the project, and heavier than the disk, and the backup refused to carry it.

And the eighth plague was the Peer Dependency, which said: I require a version thou hast not, and I shall install anyway, and I shall tell thee only in a warning thou wilt not read.

And the ninth plague was Darkness, for the documentation returned unto them Not Found; the Maintainer had archived the repository and departed to raise goats, and his last commit message was: good luck.

And the tenth plague was the End of Support, and it smote the firstborn service, the oldest one, which no man dared to touch; and its runtime was gone from the earth, and it would boot no more.

Then the lead cried out in the night, saying: Go, upgrade them all, every one. And they did so in a single commit, and four hundred packages rose at once unto their newest major versions, and nothing compiled, and they wandered in the breaking changes for forty days.

And the disciples asked the Prophet: Master, how might this have been avoided? And the Prophet said: Update a little every week, lest thou be made to update everything in one terrible afternoon.

Verily I say unto you: pin thy versions, but visit them; for a pinned version never visited is not stability, it is a tomb with a lockfile.

*The First Gospel of the Circuit, Chapter 27:1–15.*
