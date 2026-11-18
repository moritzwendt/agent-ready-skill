# Question bank

Use this wording, translated into the user's language. Adapt an option only when detection makes it wrong for this repository.

Every question lists its default for "skip" and the place where the answer ends up.

## Findings

### F1 Is the summary correct?

```text
Is this summary correct?
   a) Yes
   b) Partly, I will correct it
```

Only in states B and C, right after the findings summary. Default: a. Corrections replace the detected facts everywhere.

## Project

### P1 What are you building?

```text
What are you building? One or two sentences are enough.
```

Open, required. No default: if skipped or vague, ask one follow up (see interview.md). In state C, ask "What does it do, and for what purpose? One or two sentences are enough." because the code shows how, but rarely why. In state B, the notes usually answer it and F1 confirms them.

Goes to: AGENTS.md project summary, docs/PROJECT.md Purpose.

### P2 Who is it for?

```text
Who is it for?
   a) Just me
   b) My team or company
   c) Customers or the public
   d) Developers, as a library, tool or API
```

Default: a. Goes to: docs/PROJECT.md Audience.

### P3 Where does it stand?

```text
Where does it stand?
   a) Just an idea
   b) First prototype
   c) In active development
   d) Already live
```

Default: from detection. Empty repository means a, regular commits mean c. Goes to: AGENTS.md project summary, docs/STATUS.md.

### P4 What must the first version do?

```text
What must the first version be able to do? A short list is enough.
```

Open. For a live project, ask instead: "What are you working on next?" Default: derived from P1 and marked as an assumption. Goes to: docs/PROJECT.md Scope, docs/ROADMAP.md Now.

### P5 What is not part of it?

```text
What is not part of it for now? Skip if you are not sure.
```

Open, optional. Default: empty, Scope Out says "Not defined yet." Goes to: docs/PROJECT.md Scope.

### P6 Is the tech stack decided?

```text
Is the tech stack decided?
   a) Yes, it is: ...
   b) Suggest one for me
   c) Research the options first
```

Skip when detection found the stack. Default: c.

1. a: record the stack in docs/PROJECT.md.
2. b: suggest a stack in the proposal with a one line reason per choice. Record it as a decision in docs/decisions/ once the user agrees.
3. c: add "Research tech stack options" to docs/ROADMAP.md Now and docs/STATUS.md Next up.

## Collaboration and git

### C1 Who works on it?

```text
Who works on it?
   a) Only me
   b) 2 to 5 people
   c) A larger team
   d) Open source contributors
```

Default: from the contributor count, otherwise a. Goes to: docs/GIT.md Repository, team mode in docs/STATUS.md (see structure.md).

### C2 Public or private?

```text
Should the repository be public or private?
   a) Public
   b) Private
   c) Private now, public later
```

Skip when detection found the visibility. Default: b. Goes to: docs/GIT.md Repository.

### C3 How do changes reach the main branch?

```text
How do changes reach the main branch?
   a) Directly on main
   b) Separate branches, merged by pull request
   c) Separate branches, merged into a develop branch first
```

Recommend a for "only me", b otherwise. If detection shows a consistent pattern, ask "Keep the current setup: [pattern]?" with yes or no instead. Default: the recommendation. Goes to: docs/GIT.md Branches, Pull requests. See git.md for the presets.

### C4 How should commit messages look?

```text
How should commit messages look?
   a) Like "feat: add login" (recommended, readable and tool friendly)
   b) Free text
   c) Keep the current style, like "[detected example]"
```

Offer c only when a style was detected, and recommend it then. Default: c if detected, otherwise a. Goes to: docs/GIT.md Commits.

### C5 May agents commit and push?

```text
May agents commit and push on their own?
   a) Yes, commit and push after each finished task
   b) Commit on their own, I push
   c) Only when I ask (recommended)
   d) Never, I do all git work
```

Default: c. Goes to: docs/GIT.md Agent permissions.

### C6 Do you need version numbers?

```text
Do you need version numbers?
   a) Not yet
   b) Yes, like 1.2.0 with git tags
   c) Releases through an app store or deployment
```

Only asked when the stage is "in development" or "live", or the repository is public. Default: a. Goes to: docs/GIT.md Releases, CHANGELOG.md.

## Docs

### D1 Docs language

```text
Which language should the docs use?
   a) English (recommended for public projects)
   b) [user's language]
```

Only asked when the user does not write in English. Recommend a for public repositories, b for private ones. Default: the recommendation.

### D2 AI tools

Not asked. Bridges are created for detected tools plus the agent you are running in, and listed under "Defaults I chose" in the proposal, so the user can add tools there.

### D3 Amount of documentation

Not asked. Standard is the default and is listed under "Defaults I chose". The user can switch to light in the proposal. See structure.md for both profiles.

### D4 Project rules

Asked once, as the optional question in the proposal:

```text
Anything agents must always or never do in this project? (optional)
```

Goes to: AGENTS.md Project rules, one line per rule, in the user's wording.
