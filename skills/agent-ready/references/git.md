# Git

What goes into docs/GIT.md. The skill documents the workflow. It never changes remote settings.

## Detected habits win

If detection found a consistent commit style or branch pattern, keep it and write it down. Suggest a change only when the user asks for one.

## Presets

Pick the preset from C1 and C3, then fill docs/GIT.md with it.

| Preset | When | Branches | Merging |
|---|---|---|---|
| Solo | C3 a | `main` | Commit directly to main |
| Pull requests | C3 b | `main`, plus short lived `feat/*`, `fix/*`, `docs/*`, `chore/*` | Pull request into main. With 2 or more people, someone else reviews |
| Develop branch | C3 c | `main`, `develop`, plus short lived `feat/*`, `fix/*` | Pull requests into develop. develop goes into main for a release |
| Open source | C1 d | Like pull requests. Outside contributors work from forks | Pull request with review by a maintainer |

Branch names use lowercase words joined by hyphens after the prefix, for example `feat/class-booking`.

## Commit format

### Prefix style (C4 a)

```text
<type>: <what changed, lowercase, imperative>
```

| Type | Use for |
|---|---|
| feat | New behavior |
| fix | Bug fixes |
| docs | Documentation only |
| style | Formatting, no behavior change |
| refactor | Code changes without new behavior or fixes |
| perf | Performance |
| test | Tests only |
| build | Build system, dependencies |
| ci | CI configuration |
| chore | Everything else |

Write three examples that fit the project, for example `feat: add class booking`, `fix: prevent double booking`, `docs: update roadmap`.

### Free text (C4 b)

One line, imperative, says what changed. Write three examples.

### Detected style (C4 c)

Describe the detected pattern in one sentence and copy three real subjects from the history as examples.

## Agent permissions

Map C5 to these lines:

| C5 | Agent permissions in docs/GIT.md |
|---|---|
| a | Commit after each finished task. Push the current branch after committing. |
| b | Commit after each finished task. Never push. |
| c | Commit or push only when the user asks. |
| d | Never commit or push. Leave all git work to the user. |

Always add these lines:

1. Stage only files that belong to the task.
2. Never force push.
3. Never rewrite history that has been pushed.
4. Never commit secrets, credentials or `.env` files.
5. With the pull requests, develop branch or open source preset: never push directly to `main`.

## Releases

| C6 | Releases in docs/GIT.md |
|---|---|
| a or not asked | No versioned releases yet. Changes are collected in CHANGELOG.md under Unreleased. |
| b | Semantic versioning. Move Unreleased entries to a new version heading with the date, then tag `vX.Y.Z`. |
| c | Describe the release channel the user named. Keep CHANGELOG.md entries per release. |

## Public repositories

If C2 is a or c and C1 is c or d, offer these in the proposal as optional extras. Create them only if the user agrees:

1. CONTRIBUTING.md: how to propose changes, branch and commit rules, link to docs/GIT.md.
2. `.github/PULL_REQUEST_TEMPLATE.md`: what changed, why, how it was tested, changelog checkbox.

## Branch protection

With the pull requests, develop branch or open source preset, mention in the report that `main` can be protected so that changes only arrive through pull requests. On GitHub this is a ruleset under Settings, Rules. On GitLab it is Settings, Repository, Protected branches. Never change these settings yourself.
