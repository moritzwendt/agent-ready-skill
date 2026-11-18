# agent-ready

Make your repository agent ready.

agent-ready is an [Agent Skill](https://agentskills.io) that sets up documentation AI coding agents read at the start of every session and keep current while they work. Every new chat knows what the project is, what is in progress, which rules apply and where new knowledge belongs.

## What it does

1. Looks at what your repository already contains: code, docs, git history, agent instruction files.
2. Asks a few short questions, only about what it cannot find out itself.
3. Shows you exactly which files it will create or change, and waits for your ok.
4. Writes a documentation system that works for every agent and every person, with or without this skill installed.

## What you get

```text
AGENTS.md              entry point: project summary, commands, rules, doc map
CLAUDE.md              points to AGENTS.md, only if you use Claude Code
CHANGELOG.md           notable changes
docs/
├── PROJECT.md         what the project is and how it is built
├── STATUS.md          current focus and a handoff note for the next session
├── ROADMAP.md         now, next, later, done
├── GIT.md             branches, commit format, releases, what agents may do
├── LEARNINGS.md       hard problems with cause and fix
├── features/          a plan for each feature, approved before building
├── decisions/         why technical choices were made
└── research/          research results with sources and date
```

From then on, agents following AGENTS.md:

1. Read docs/STATUS.md at the start of every session.
2. Plan features and get your approval before building them.
3. Update status, changelog and roadmap after each finished task.
4. Write down decisions, research and hard bugs where the next session finds them.
5. Follow your branch and commit rules.

Prefer less? Ask for the light setup: AGENTS.md, CHANGELOG.md and docs/STATUS.md only.

## Install

### Skills CLI

Works with Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI and many more:

```bash
npx skills add moritzwendt/agent-ready-skill
```

### Claude Code plugin

```text
/plugin marketplace add moritzwendt/agent-ready-skill
/plugin install agent-ready@agent-ready-skill
```

### Manual

Copy the folder `skills/agent-ready` into your agent's skills folder. For Claude Code that is `.claude/skills/` in your project or `~/.claude/skills/` for all projects.

## Use

Open your repository with your agent and ask:

```text
Make this repo agent ready.
```

Other phrasings work too, such as "set up docs for this project" or "create an AGENTS.md".

The skill starts with what it found and a few questions:

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
```

## FAQ

**Does it change my code?** No. It only writes documentation files and small pointer files for agent tools.

**I already have docs. Will they be overwritten?** No. Existing files are kept and linked. Rules from files like CLAUDE.md or .cursorrules are merged into AGENTS.md only after you confirm.

**Which agents does it work with?** The skill runs in any agent that supports Agent Skills. The generated docs use AGENTS.md, which most coding agents read. Claude Code and Gemini CLI get a one line pointer file.

**Will it commit?** Only if you say yes. Afterwards, docs/GIT.md records whether agents may commit on their own.

**Can I run it again?** Yes. It notices an existing setup, checks it for outdated parts and asks before fixing anything.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)
