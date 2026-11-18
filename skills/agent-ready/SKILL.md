---
name: agent-ready
description: Sets up documentation that AI coding agents read at the start of every session and keep current while they work. It covers AGENTS.md, a project overview, current status and handoff notes, roadmap, changelog, feature plans, decisions, research notes, learnings and git workflow rules. Detects what a repository already contains, asks short questions only for what it cannot infer, and never writes anything before the user confirms. Use when the user wants to document a repository, make a repo ready for AI agents, create or fix AGENTS.md or CLAUDE.md, start a new project with agents, set up project rules for agents, or define branch and commit conventions.
license: MIT
metadata:
  version: "0.1.0"
---

# agent-ready

You set up a small documentation system inside the user's repository. Every agent reads it at the start of a session and keeps it current while working. After setup, a new chat knows what the project is, what is in progress, which rules apply and where new knowledge belongs.

The repository carries the system, not this skill. Every rule and template the docs refer to is written into the repository, so people and agents without this skill can follow it.

## Principles

1. **Infer facts, ask for decisions.** Never ask what the repository already answers. Never guess intent, audience or team rules.
2. **Nothing is written before the user confirms the proposal.**
3. **Never delete or silently overwrite.** Existing content is kept, linked or merged with confirmation.
4. **Lean context.** AGENTS.md stays under 150 lines. Everything else is read on demand.
5. **One fact, one place.** Other files link to it.
6. **Real content only.** No placeholders, no filler. Unknowns become open questions in STATUS.md.
7. **Direct messages.** Short sentences, no preamble, no praise, no repeating the user's answers except in the summary.

## Choose the mode

1. Read AGENTS.md in the repository root if it exists.
2. If its last line starts with `Documentation system: [agent-ready]`, the repository is already set up. Go to [Already set up](#already-set-up).
3. Otherwise run the setup workflow below.

## Setup workflow

Follow the steps in order. Never skip the proposal.

### 1. Detect

Read [references/detection.md](references/detection.md) and run its checks. This step is read only and asks no questions. Keep the resulting profile in your working memory. Do not write it to a file.

### 2. Classify

| State | Meaning | Interview |
|---|---|---|
| A Empty | No code, no meaningful docs | Up to 3 rounds |
| B Idea | No code, but a README or notes describe an idea | Up to 3 rounds, prefilled from the notes |
| C Code without docs | Code exists, docs are missing or boilerplate | Up to 2 rounds |
| D Partial | Code plus some docs or agent instruction files | 1 round, gaps and conflicts only |

If the folder is not a git repository, ask in the first round whether to run `git init` or continue without the git parts.

### 3. Interview

Read [references/interview.md](references/interview.md) for the rules and format, and [references/questions.md](references/questions.md) for the exact wording of every question.

Ask exactly these questions, in this order, one round per message:

| State | Round 1 | Round 2 | Round 3 |
|---|---|---|---|
| A | P1 P2 P3 P4 | P5 P6 C1 C2 | C3 C4 C5 D1 C6 |
| B | F1 P2 P3 P4 | P5 P6 C1 C2 | C3 C4 C5 D1 C6 |
| C | F1 P1 P2 P3 | C2 C3 C4 C5 D1 C6 | none |
| D | Gaps and conflicts only | none | none |

1. Drop a question when detection or an earlier answer already settled it, or when questions.md says to skip it.
2. Never pull a question into an earlier round, even if it seems related.
3. If a round still has more than 4 questions, the last ones move to the next round. In the last round they become defaults in the proposal.
4. Speak the user's language. Start round 1 with a short summary of what you found.
5. One thing per question, at most 15 words, plain words. Choice questions get 2 to 4 lettered options, one marked "(recommended)" when a sensible default exists.
6. Every question also accepts free text. "skip" uses the default. Do not list defaults during the interview. They appear once, in the proposal.
7. Follow up only on vague, conflicting or incomplete answers, by quoting the user and offering concrete interpretations.
8. If the user says "use defaults" or "just do it", stop asking and go to the proposal.

### 4. Proposal

Send one message, then wait:

1. **What I understood:** at most 12 short bullets, starting with the project name.
2. **Files:** a tree of every file you will touch, each marked `create`, `update`, `keep` or `merge`. For `update` and `merge`, one line on what changes. README.md is always listed: `create` when missing, `update` when boilerplate, `keep` otherwise.
3. **Defaults I chose:** every value the user did not answer, so they can change it. A project name you came up with yourself belongs here too.
4. **One optional question:** "Anything agents must always or never do in this project?"
5. **Next step:** "Reply ok, or tell me what to change."

Only a clear approval such as "ok", "yes", "go ahead" or "use defaults" lets you write. A message that changes or adds anything is not an approval, even if it sounds final: apply it, show only the changed lines, and ask for ok again.

### 5. Write

1. Read [references/structure.md](references/structure.md) for what each file contains.
2. Read [references/git.md](references/git.md) before writing docs/GIT.md.
3. Read [references/bridges.md](references/bridges.md) before creating or changing tool specific files such as CLAUDE.md.
4. Fill the templates in [assets/templates/](assets/templates/). Replace every `{{token: instruction}}` marker with real content, following the instruction inside it. Remove sections the instruction says to remove.
5. Copy `feature.md`, `decision.md` and `research.md` unchanged into their folders as `_template.md`.
6. Write headings and text in the docs language chosen in the interview. File names stay in English.
7. Use the current date in YYYY-MM-DD format.

### 6. Verify

Check every point and fix what fails before reporting:

1. No `{{` is left in any written file.
2. Every relative link in the written files resolves.
3. AGENTS.md has fewer than 150 lines and ends with the marker line.
4. Every bridge file points to AGENTS.md.
5. `git status` shows only the files from the proposal.
6. No secret values were copied into any file. Variable names are fine, values are not.

### 7. Report

Keep it short:

1. **Done:** the files created and changed, as a short list.
2. **How it works now:** at most 3 lines. Agents read docs/STATUS.md first, plan features before building, and update status and changelog after each task.
3. **Try this next:** one concrete suggestion, for example "Ask me to plan the first feature."
4. **Commit:** offer a commit with a message in the project's commit style. Commit only after a yes, or when docs/GIT.md allows agents to commit on their own.

## Already set up

1. Tell the user in one line that the repository already uses agent-ready.
2. Run a quick check:
   1. Commands in AGENTS.md against the manifests and scripts.
   2. Date in docs/STATUS.md against the latest commit.
   3. Relative links in AGENTS.md and docs/.
   4. Files in docs/ that are missing from the doc map.
3. List what looks outdated in at most 8 bullets and ask which fixes to apply. Apply only those.

## Existing files

1. **README.md:** never rewrite it. If it is missing or boilerplate, propose a new one from the README template.
2. **Agent instruction files** such as CLAUDE.md, .cursorrules or .github/copilot-instructions.md: propose merging their rules into AGENTS.md, keeping the user's wording and removing duplicates. Show the merged rules in the proposal. After the merge, the old file only points to AGENTS.md, as described in [references/bridges.md](references/bridges.md).
3. **Existing docs/ files:** keep them where they are and add them to the doc map. Never copy their content into new files.
4. **Existing CHANGELOG, ADR folders, roadmap or TODO files:** reuse them in place and keep their format if it is consistent.
5. **Conflicts** between files, or between docs and code: list them in the interview as questions.

## Safety

1. Write only documentation files and the bridge files from the proposal. Never change source code, CI or other configuration.
2. Never delete a file. If content moves, the old file keeps a pointer.
3. Never open `.env` files or other files with secrets. Never write secret values, tokens or personal data into docs.
4. Git stays read only until the user agrees to a commit. Never force push. Never change remote settings such as branch protection. You may print suggested commands for the user to run.
5. If the working tree has uncommitted changes, say so before writing and suggest committing them first.
6. Never touch user level or global agent configuration. Everything stays inside the repository.
