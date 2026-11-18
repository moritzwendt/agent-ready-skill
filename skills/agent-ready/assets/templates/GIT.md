# Git workflow

Updated {{date: today in YYYY-MM-DD}}

## Repository

| Item | Value |
|---|---|
| Remote | {{remote: remote URL, or "None yet"}} |
| Visibility | {{visibility: Public, Private, or Private for now, public later}} |
| Default branch | {{default_branch: usually main}} |
| Team | {{team: Solo, 2 to 5 people, larger team, or open source contributors}} |

## Branches

{{branches: a table with the columns Branch, Purpose, Merges into and Rules, from the preset in the skill's git reference. Below it, one line on branch naming, for example "Short lived branches: feat/short-name, fix/short-name."}}

## Commits

{{commit_format: one or two sentences describing the format, the type table for the prefix style, and three examples that fit this project.}}

## Pull requests

{{pull_requests: when pull requests are used, who reviews and what a pull request must contain. Remove this section for the solo preset.}}

## Releases

{{releases: the release rule from the skill's git reference.}}

## Agent permissions

{{agent_permissions: the line for the user's choice, followed by the fixed rules: stage only files that belong to the task, never force push, never rewrite pushed history, never commit secrets, credentials or .env files, and for presets with pull requests never push directly to main.}}
