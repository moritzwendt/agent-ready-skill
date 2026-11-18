# Structure

What the documentation system contains, where it lives and what goes into each file.

## Profiles

### Standard (default)

```text
AGENTS.md
CHANGELOG.md
README.md                 only when missing or boilerplate
docs/
├── PROJECT.md
├── STATUS.md
├── ROADMAP.md
├── GIT.md
├── LEARNINGS.md
├── features/
│   ├── README.md
│   └── _template.md
├── decisions/
│   ├── README.md
│   └── _template.md
└── research/
    ├── README.md
    └── _template.md
```

Plus the bridge files from bridges.md.

### Light

For small or short lived projects, only when the user asks for less documentation:

```text
AGENTS.md
CHANGELOG.md
docs/
└── STATUS.md
```

In the light profile:

1. AGENTS.md gets a short "Project" section with purpose, audience and stack instead of docs/PROJECT.md.
2. AGENTS.md gets a short "Git" section with branches, commit format and agent permissions instead of docs/GIT.md.
3. Remove the working rules about features, decisions, research, learnings and the roadmap, and their rows in the doc map.

## Location

1. Use `docs/` by default.
2. If `docs/` is a published documentation site (mkdocs.yml, docusaurus.config.*, .vitepress/, _config.yml), use `dev-docs/` instead and adjust every path.
3. If some of the files already exist elsewhere, such as a root ROADMAP.md, keep them there and point to them from the doc map.
4. The doc map in AGENTS.md always lists the real paths.

## Naming

1. File names are in English and keep the names above, so other tools and later runs find them.
2. Entries in features/, decisions/ and research/ are named `YYYY-MM-DD-short-title.md`, for example `2026-03-04-class-booking.md`. Dates avoid number collisions when people work on parallel branches.
3. Each of these folders has a README.md index with one row per entry.

## Writing rules

1. Write real content from detection and answers. Never leave example text, "TBD" or "Lorem ipsum".
2. If something is unknown, write "Not decided yet." or "Not defined yet." and list it under open questions in docs/STATUS.md.
3. Mark defaults the user did not confirm with "Assumption:" in docs/STATUS.md.
4. Use absolute dates in YYYY-MM-DD format.
5. Keep each fact in one file and link to it from others.
6. Write in the chosen docs language. Keep code, commands and file names as they are.
7. Short sentences. Tables and lists where they help scanning.

## Files

### AGENTS.md

Template: `assets/templates/AGENTS.md`. Under 150 lines, target 80 to 120.

1. Project summary in 3 to 5 sentences: what it is, who it is for, current stage.
2. Session start: read docs/STATUS.md first.
3. Commands: only commands that exist. Remove rows without a command. If there is no code yet, replace the table with "No code yet. Add commands here once they exist."
4. Working rules: as in the template. Adapt only for the light profile.
5. Project rules: answers to D4 plus clear conventions from detection, one line each. Remove the section if empty.
6. Doc map.
7. Marker line, always last.

### CHANGELOG.md

Template: `assets/templates/CHANGELOG.md`. Root of the repository.

If a changelog exists, keep it and its format. Add one entry under the newest unreleased section: "Documentation system for agents and contributors."

### README.md

Template: `assets/templates/README.md`. Only when missing or boilerplate. For people, not agents: what it is, how to run it, where to find more.

### docs/PROJECT.md

Template: `assets/templates/PROJECT.md`. Facts about the project that change rarely. Remove sections that do not apply yet, such as Glossary or External services.

### docs/STATUS.md

Template: `assets/templates/STATUS.md`. Rewritten after each finished task, never appended. At most 40 lines.

After setup it says what was set up, lists the first next steps from the interview, and every assumption the user has not confirmed.

**Team mode** (C1 is b, c or d): "In progress" lists active work with owner and a link to the feature plan. Details stay in the feature plan, which keeps merge conflicts small.

### docs/ROADMAP.md

Template: `assets/templates/ROADMAP.md`. Now, Next, Later, Done. One line per item, linked to its feature plan when one exists.

After setup, "Now" holds the first version goals from P4. Leave Done empty.

### docs/GIT.md

Template: `assets/templates/GIT.md`. See git.md for what goes in.

### docs/LEARNINGS.md

Template: `assets/templates/LEARNINGS.md`. Starts without entries.

### docs/features/, docs/decisions/, docs/research/

1. README.md from `assets/templates/index.md`, with the folder specific title, purpose and columns given in the template.
2. `_template.md` copied unchanged from `feature.md`, `decision.md` or `research.md`.
3. If the user chose a stack in P6 b, add the first decision entry for it.
