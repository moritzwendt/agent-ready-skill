# {{project_name: the project name}}

{{project_summary: 3 to 5 sentences. What it is, who it is for, the current stage.}}

More: [README](README.md), [project overview](docs/PROJECT.md)

## Start of every session

1. Read [docs/STATUS.md](docs/STATUS.md) first. If your task relates to its handoff note, continue from there.
2. Read other docs only when your task needs them. The doc map below says which.

## Commands

{{commands: a table with the columns Task and Command. Rows for install, run, test, lint and build, only for commands that exist. Without code, write "No code yet. Add commands here once they exist."}}

## Working rules

### Before work

1. Plan non trivial features in [docs/features/](docs/features/) with the template there, and get the user's approval before building. A plan is needed when a change adds visible behavior, touches more than one area, changes data or APIs, or takes more than one session.
2. Before debugging, check [docs/LEARNINGS.md](docs/LEARNINGS.md).
3. Before researching, check [docs/research/](docs/research/).
4. Before any git operation, follow [docs/GIT.md](docs/GIT.md).

### During work

5. Record significant technical decisions in [docs/decisions/](docs/decisions/): choosing or replacing a library or service, changing the architecture or data model, or breaking a convention.
6. Save research results in [docs/research/](docs/research/) with sources and date.
7. When a code change makes docs wrong, fix the docs in the same change.

### After each finished task

8. Add notable changes to [CHANGELOG.md](CHANGELOG.md) under Unreleased.
9. Rewrite [docs/STATUS.md](docs/STATUS.md): focus, progress, next steps, open questions, handoff note.
10. Update [docs/ROADMAP.md](docs/ROADMAP.md) and the status of the feature plan.
11. Add problems that took real effort to solve to [docs/LEARNINGS.md](docs/LEARNINGS.md).

### Always

12. Keep each fact in one place and link to it from others.
13. Never write secrets or personal data into docs.
14. Use absolute dates in YYYY-MM-DD format.

## Project rules

{{project_rules: the user's own rules plus clear conventions from detection, one numbered line each. Remove this section if there are none.}}

## Doc map

| File | Read when | Update when |
|---|---|---|
| [docs/STATUS.md](docs/STATUS.md) | Every session, first | After each finished task |
| [docs/PROJECT.md](docs/PROJECT.md) | Working in a new area or on the architecture | Stack, structure or scope changes |
| [docs/ROADMAP.md](docs/ROADMAP.md) | Choosing the next task | Items finish or priorities change |
| [CHANGELOG.md](CHANGELOG.md) | Preparing a release | A notable change is finished |
| [docs/GIT.md](docs/GIT.md) | Before any git operation | The workflow changes |
| [docs/LEARNINGS.md](docs/LEARNINGS.md) | Before debugging | A problem took real effort to solve |
| [docs/features/](docs/features/) | Before building a feature | Plan approved, progress, done |
| [docs/decisions/](docs/decisions/) | Before changing architecture or dependencies | A significant decision is made |
| [docs/research/](docs/research/) | Before researching | Research is finished |
{{extra_doc_rows: rows for existing docs that stay where they are, such as an existing docs/architecture.md. Remove this line if there are none.}}

Documentation system: [agent-ready](https://github.com/moritzwendt/agent-ready-skill) v1
