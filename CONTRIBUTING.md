# Contributing

Thanks for helping to make agent-ready better. Bug reports, ideas and pull requests are welcome.

## Before you start

1. For small fixes, open a pull request directly.
2. For anything bigger, open an issue first so we can agree on the approach before you spend time on it.

## Layout

```text
skills/agent-ready/SKILL.md            main workflow, loaded when the skill runs
skills/agent-ready/references/         details, loaded on demand
skills/agent-ready/assets/templates/   files the skill writes into repositories
.claude-plugin/marketplace.json        Claude Code plugin marketplace entry
.github/scripts/check.py               repository checks, also run in CI
```

## Writing rules

1. English, plain words, short sentences.
2. SKILL.md stays under 500 lines. Move details into `references/`.
3. SKILL.md links every reference directly. References do not link to further references.
4. Templates that the skill fills use `{{token: instruction}}` markers. The instruction says what to write and when to remove the section.
5. `feature.md`, `decision.md` and `research.md` are copied unchanged into repositories, so they contain no markers.
6. A generated AGENTS.md must stay under 150 lines.
7. Questions in `references/questions.md` follow the rules in `references/interview.md`: at most 15 words, one thing per question, 2 to 4 options.

## Test your change

1. Install your local copy into a test repository, for example by copying or linking `skills/agent-ready` into `.claude/skills/agent-ready` there.
2. Run it on the repository states your change affects:
   1. Empty repository
   2. Only a README with an idea
   3. Code without docs
   4. Code with some docs or agent instruction files
   5. Already set up with agent-ready
3. Check that:
   1. Questions are short, few and never ask what the repository already shows.
   2. Nothing is written before you confirm the proposal.
   3. No `{{` markers remain in the written files and all links work.
   4. Existing content is kept.
4. Run the repository checks:

```bash
pip install skills-ref
agentskills validate skills/agent-ready
python3 .github/scripts/check.py
```

## Commits

Use the prefix style, lowercase and imperative:

```text
feat: add windsurf bridge
fix: keep existing changelog format
docs: clarify manual install
```

## Changelog

Every pull request adds a line to `CHANGELOG.md` under Unreleased. Pure typo fixes can skip this with the `skip-changelog` label.

## Pull requests

1. One topic per pull request.
2. Fill in the template, including which agents you tested with.
3. CI must pass.

## Releases

Maintainers release by:

1. Raising `metadata.version` in SKILL.md and both versions in `.claude-plugin/marketplace.json`.
2. Moving the Unreleased entries under a new version heading with the date.
3. Tagging `vX.Y.Z` and creating a GitHub release with the changelog entries.

## Code of conduct

Everyone taking part follows the [code of conduct](CODE_OF_CONDUCT.md).
