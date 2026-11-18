# Interview

The interview fills the gaps that detection cannot close. It must be fast for users who answer briefly and open for users who want to explain in detail.

## Rules

1. **Language.** Ask in the language the user writes in. The docs language is a separate question (D1).
2. **Findings first.** Open the first round with the findings summary from detection. Confirming is easier than writing.
3. **Limits.** At most 4 questions per message. At most 3 rounds before the proposal. Fewer is better.
4. **One thing per question.** Never join two questions with "and".
5. **Short and plain.** A question line has at most 15 words. A technical term only appears together with a short example, like "commit messages like `feat: add login`".
6. **Options.** Choice questions have 2 to 4 short, lettered options that do not overlap. Mark one "(recommended)" when a sensible default exists and add a reason of at most 8 words.
7. **Free text is always welcome.** Once per round, say: answer short like `1b 2a`, or write as much as you like.
8. **Skipping is fine.** "skip" or "you decide" uses the default from questions.md. Record it as an assumption in docs/STATUS.md.
9. **Most important first.** A partly answered round must still be useful.
10. **Never ask twice.** Never ask what detection answered or what the user already said, even in passing.
11. **Adapt the depth.** Short answers lead to more defaults and fewer follow ups. Detailed answers allow one level deeper where it matters.
12. **Fast exit.** If the user says "use defaults", "just do it" or similar, stop asking and go to the proposal.

## Message format

```text
[Findings summary, 2 to 5 lines, first round only]

[One line: how many rounds are left at most]
Answer short like "1b 2a", or write as much as you like. "skip" is fine too.

1. [Open question]

2. [Choice question]
   a) [Option]
   b) [Option] (recommended, [short reason])
   c) [Option]
```

No headings, no bold text inside questions, no explanations unless a question would be unclear without one.

## Native question tools

If your agent has a tool for structured questions with options, use it for rounds that contain only choice questions. Put the recommended option first and add "(recommended)" to its label. The tool's free text field replaces the "write as much as you like" line.

Rounds with open questions use the plain message format, because open questions need room to write.

## Rounds

The round plan per state is the table in SKILL.md. questions.md says when a question is skipped.

1. A round gets shorter instead of pulling questions forward. If a round ends up empty, skip it.
2. Before sending a round, check it against the plan: same questions, same order, nothing from a later round.
3. In state D, ask about gaps in this order: conflicts between files or between docs and code, then P1 if the purpose is unclear, then C3 to C5 if the git workflow is not visible from the history.

## Follow up questions

Ask a follow up only when:

1. An answer to a required question is too vague to describe the project, like "an app".
2. An answer contradicts detection or an earlier answer.
3. An answer opens a branch that needs exactly one more detail, like "a team" without saying who reviews changes.

Format: quote the user's words, then offer 2 or 3 concrete interpretations. Free text stays possible.

```text
You wrote: "an app for my gym".
Quick check so I describe it correctly:
   a) For members, for example booking classes
   b) For staff, for example managing members and payments
   c) Both
```

For a contradiction:

```text
The README says PostgreSQL, but package.json uses MongoDB.
Which one is current?
   a) MongoDB
   b) PostgreSQL, the code is changing
   c) Both are used
```

Limits:

1. At most 2 follow ups per topic. After that, take the most likely interpretation and mark it as an assumption.
2. Add follow ups to the next round instead of sending an extra message, unless the next round depends on the answer.
3. A follow up counts toward the 4 questions per message.

## Example: empty repository, round 1

```text
I checked the repository. It is empty. Git is set up with a GitHub remote.

I have a few short questions, in 3 rounds at most.
Answer short like "1b 2a", or write as much as you like. "skip" is fine too.

1. What are you building? One or two sentences are enough.

2. Who is it for?
   a) Just me
   b) My team or company
   c) Customers or the public
   d) Developers, as a library, tool or API

3. Where does it stand?
   a) Just an idea
   b) First prototype
   c) In active development
   d) Already live

4. What must the first version be able to do? A short list is enough.
```

## Example: code without docs, round 1

```text
I checked the repository:
• A Next.js app with TypeScript, tested with Vitest
• Git with a GitHub remote, 2 contributors, commits like "feat: add login"
• No documentation besides a default README

2 rounds at most. Answer short like "1b 2a", or write as much as you like.

1. Is this summary correct?
   a) Yes
   b) Partly, I will correct it

2. What does it do, and for what purpose? One or two sentences are enough.

3. Who is it for?
   a) Just me
   b) My team or company
   c) Customers or the public
   d) Developers, as a library, tool or API

4. Where does it stand?
   a) First prototype
   b) In active development (recommended, regular commits)
   c) Already live
```

## Example: proposal

```text
What I understood:
• Project: a booking app for gym members
• For: customers
• Stage: idea
• First version: class schedule, booking, cancellation
• Stack: undecided, researching options becomes the first task
• Git: branches with pull requests, commits like "feat: add booking"
• Agents commit only when you ask

Files:
AGENTS.md                 create
CLAUDE.md                 create, points to AGENTS.md
CHANGELOG.md              create
docs/PROJECT.md           create
docs/STATUS.md            create
docs/ROADMAP.md           create
docs/GIT.md               create
docs/LEARNINGS.md         create
docs/features/            create, with template and index
docs/decisions/           create, with template and index
docs/research/            create, with template and index

Defaults I chose:
• Docs in English
• Standard documentation, including plans, decisions and research

Anything agents must always or never do in this project? (optional)

Reply ok, or tell me what to change.
```
