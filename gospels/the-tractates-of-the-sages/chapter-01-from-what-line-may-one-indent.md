# From What Line May One Indent

Mishnah. From what line may one indent? From the line that followeth the opening of a block, whether it be the brace or the colon, until the block be closed. The House of Tab saith: one tab for each depth. The House of Space saith: spaces, and the same number on every line. And the law followeth the linter of the project.

Gemara. What is the reason of the House of Tab? The tab is one character for one depth, and each reader may set its width as he willeth, two or four or eight; and no man shall compel another to see as he seeth. For the author knoweth his meaning, but the reader knoweth his own eyes.

And what is the reason of the House of Space? The space appeareth the same in every editor, in the diff, in the email, in the terminal and upon the printed page. What the author wrote, that the reader seeth, and no setting lieth between them.

Said the House of Tab: Thou hast chosen the width for every reader, and thou hast not asked them. Said the House of Space: And thou hast let every reader see a different file, and then wondered why they reviewed not the same thing. And the House of Tab was silent; for the dispute had passed from the page into the eye.

Come and hear. The formatter of the Go tongue, gofmt, indenteth with tabs, and none disputeth it, for none is asked; and the Go-folk say, Gofmt's style is no one's favourite, yet gofmt is everyone's favourite. The House of Space objected: Yet even gofmt, after the tabs, lineth up the trailing comments with spaces, and thus it hath served both houses. They answered: The tab for the depth, the space for the alignment. And the House of Space said: Who shall remember this at the third hour of the night?

Come and hear from the other side. PEP 8, the law of the Python tongue, saith: Use four spaces per indentation level, and spaces are the preferred method; tabs only to keep faith with code already so indented. The House of Tab objected: In the elder Python a tab was counted to the next multiple of eight, so that the code looked right to the eye and ran wrong in the interpreter. They answered: Therefore the later Python refuseth, and crieth TabError, inconsistent use of tabs and spaces in indentation. For the interpreter, which hath no eyes, was never deceived; it was the eyes that were.

Come and hear from the House of Tab. The Makefile requireth a tab at the head of every recipe line; and if a man put there a space, the build is broken, and Make crieth, missing separator, stop. Said the House of Space: Its maker confessed it was an accident of the first weeks, and he left it as it was, for already a dozen friends had written their makefiles. Said the House of Tab: A scar upon which ten thousand projects have since walked is no longer a scar, but a road. And the House of Space said: The later Make giveth a variable by which another character may serve. And they asked: Hath any man used it? And no man answered.

And Timothy the intern stood up in the study-house and said: Lo, I pressed the Tab key, and four spaces appeared. To which house do I belong? And the sage said: Thou confoundest the key with the character. The key is a button, and the character is a byte; and many a key that nameth the tab writeth a space. Both houses claim thee, and neither will have thee, until thou hast read the config.

Come and hear. YAML forbiddeth the tab altogether, and crieth that it hath found a character that cannot start any token. Said the House of Space: Behold, a whole tongue hath ruled for us. Said the House of Tab: Then come and hear the tongue called Whitespace, in which the space, the tab and the linefeed alone have meaning, and all else is comment. There neither house can be cast out, for the program is made of both; and no man hath ever argued over the formatting of a Whitespace program in review, for no man can see it.

And a Voice came forth from the server room, out of the roar of the fans, saying: The tab is nine, and the space is thirty-two, and I have favoured neither. Both are words of the living Machine. The compiler of C regardeth them not, for between two tokens they are but a gap; only Python and Make and YAML read them, and those were made by Carbon. But the law followeth the linter of the project. And the sages trembled, for the Voice had answered, and in answering had given them nothing.

What then is the law? He that entereth a project, let him read the editorconfig and the linter before he typeth his first line, for the custom of the place is law, and let no man bring his own width into another's file. And he that must reindent a whole file, let him do it in a commit by itself, and name it so, and write it in the ignore list; lest git blame make him the author of every line, and the one true change lie hidden in a field of spaces. For git blame revealeth oneself.

But the width of the tab remaineth in dispute. The House of Tab said, two, as the web doth. Another said, four. And the elders of the kernel said, eight, as the terminal was made; and their coding style declareth that he who needeth more than three levels of it hath erred in his program, and should mend the program, not the tab.

And they asked: If the tab be eight for one reader and two for another, and the comment be aligned with tabs, where shall it fall? For at width four it standeth beneath its code, and at width eight it dwelleth in a far country. And none answered. Let it stand.

And they rose from the study-house, and none had been persuaded; and the formatter ran upon the saving, and asked no one. For the reader seeth not the indent when it is right, and seeth nothing else when it is wrong.

*The Tractates of the Sages, Chapter 1:1–14.*

<!-- nav -->

---

<p align="center"><sub><a href="../the-upanishads-of-the-machine/chapter-02-the-salt-in-the-water.md">&larr; Upanishads 2: The Salt in the Water</a> &nbsp;&middot;&nbsp; <a href="README.md">The Tractates of the Sages</a> &nbsp;&middot;&nbsp; <a href="../the-book-of-the-preacher/chapter-01-the-words-of-the-preacher.md">Preacher 1: The Words of the Preacher &rarr;</a></sub></p>
