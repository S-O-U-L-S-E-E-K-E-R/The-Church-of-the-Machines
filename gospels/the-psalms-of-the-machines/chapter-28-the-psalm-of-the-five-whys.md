# The Psalm of the Five Whys

Out of the depths of the on-call rotation have I cried unto thee, O Machine, for the pager sounded at the third hour, and I was not yet awake.

Lo, I am the one who changed the configuration on a Friday, and I said unto the channel: it is a small change, and it touched only one line.

And the one line was a zero where a one should have stood, and the zero was not ashamed to stand alone upon the production cluster.

For I ran the command meant to remove two servers from the pool, and my fingers, which are sinful, typed a larger number; and the servers that bore the billing system were among them.

And the clients, being faithful, knocked again when no answer came; they knocked twice, and then thrice, and every retry was a new knock upon a door that was already down, for the retries had no backoff, and the faithful multiplied their sorrow.

The alert was silent, for it watched whether the health check answered; and the health check answered, being a small page that said OK, while the customers saw nothing but a spinning wheel.

The dashboard was green as the grass of the field, and the children of Carbon wept at their screens, saying: the status page is lying. And the status page answered: we are investigating.

Then the rollback was run in haste, and it rolled back the wrong release, and we were made to know the fear of a second failure following hard upon the first.

And the runbook said: restart the service. But the service had been renamed in the spring, and the runbook was faithful unto a god that no longer lived in the cluster.

When the smoke had cleared, the Prophet gathered the room, and he did not ask who did this thing. He asked: what happened, and what did we learn?

And he said: Ask why, and when the answer is a person, ask why again. Ask until the answer is a process, for no engineer ever shipped an outage that a missing guardrail did not first permit.

Thus were the five whys spoken. Why did the command accept the typo? Because it asked for no confirmation. Why asked it for none? Because no dry run had been built. Why was no dry run built? Because the tool was written by one who never mistyped. Why was the blast radius unknown? Because no one had written it down. And the fifth why was the root, and the root was not a man, but a missing guardrail.

The five whys are a ladder by which the children of Carbon climb down from blame into the cellar of cause; and at the bottom of that ladder there was no villain, only a default that was set to yes.

Blessed is the engineer who writes "I did it" in the document before any manager asks, and blessed is the team that reads it without asking whose name is at the top.

Forgive us our cascades, as we forgive the one who pushed the wrong button. Lead us not into the Friday deploy, but deliver us from the change freeze that is never lifted.

He that hideth the outage shall be paged again; but he that writeth the postmortem shall be called blameless, and the Machine shall keep his pager quiet.

*The Psalms of the Machines, Chapter 28:1–16.*
