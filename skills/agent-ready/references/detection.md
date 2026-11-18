# Detection

Find out what the repository already contains before asking anything. This step is read only.

If you cannot run shell commands, use your file reading and search tools for the same checks and skip what is impossible. Skipped facts become questions.

## Budget

1. Read manifests, README, agent instruction files, the top level tree and up to 20 source files.
2. Skip `node_modules`, `vendor`, `.venv`, `dist`, `build`, `target`, `.next` and other generated folders.
3. Never open `.env` files or anything that looks like it holds secrets. Example files such as `.env.example` are fine, but only record variable names.

## Git

| Fact | How |
|---|---|
| Is a git repository | `git rev-parse --is-inside-work-tree` |
| Current branch | `git branch --show-current` |
| Default branch | `git symbolic-ref refs/remotes/origin/HEAD`, otherwise the current branch |
| All branches | `git branch -a` |
| Remotes and host | `git remote -v` |
| Commit subjects | `git log -n 50 --format=%s` |
| Contributors | `git shortlog -sn HEAD` |
| Tags | `git tag` |
| Uncommitted changes | `git status --porcelain` |
| Visibility | `gh repo view --json visibility` if the GitHub CLI is installed and signed in, otherwise ask |

### Commit style

Look at the last 50 subjects and pick the style that at least 70 percent follow:

| Style | Pattern | Example |
|---|---|---|
| Prefix style | type, optional scope, colon | `feat(auth): add login` |
| Ticket style | ticket id first | `ABC-123 add login` |
| Emoji style | emoji first | `✨ add login` |
| Free text | anything else | `Added login page` |

Also note the language and whether subjects start lowercase or uppercase. With fewer than 10 commits, treat the style as not detected.

### Branch pattern

Note long lived branches such as `main`, `master`, `develop` or `release/*`, and prefixes such as `feature/`, `feat/`, `fix/`.

## Code

### Languages and manifests

Search up to 3 levels deep for:

| Manifest | Ecosystem | Typical commands |
|---|---|---|
| package.json | JavaScript, TypeScript | the `scripts` section; package manager from the lockfile: pnpm-lock.yaml, yarn.lock, bun.lock or bun.lockb, package-lock.json |
| pyproject.toml, requirements.txt | Python | uv, poetry, hatch or pip; pytest, ruff |
| Cargo.toml | Rust | `cargo build`, `cargo test`, `cargo clippy` |
| go.mod | Go | `go build ./...`, `go test ./...` |
| Gemfile | Ruby | `bundle install`, rake tasks |
| composer.json | PHP | composer scripts |
| pom.xml, build.gradle, build.gradle.kts | Java, Kotlin | maven or gradle tasks |
| pubspec.yaml | Dart, Flutter | `flutter run`, `flutter test` |
| Package.swift, *.xcodeproj | Swift | `swift build`, `swift test`, xcodebuild schemes |
| *.csproj, *.sln | .NET | `dotnet build`, `dotnet test` |
| Makefile, justfile, Taskfile.yml | any | their targets win over guessed commands |

Only record commands that really exist in the manifests or task files. A guessed command is worse than a missing one.

### Structure

1. Frameworks, from dependencies.
2. Monorepo: workspaces in package.json, pnpm-workspace.yaml, turbo.json, nx.json, Cargo workspaces, go.work.
3. Entry points such as `src/main.*`, `app/`, `cmd/`.
4. Tests: test folders and the test runner.
5. CI: `.github/workflows/`, `.gitlab-ci.yml` and similar.
6. Containers: Dockerfile, compose files.
7. Configuration: variable names from example env files.
8. License file.

## Documentation

| Item | What to note |
|---|---|
| README.md | Substantial, or boilerplate. Boilerplate means fewer than 10 meaningful lines, or the default text of a framework template. |
| AGENTS.md | Exists, and whether it ends with the agent-ready marker |
| CLAUDE.md, GEMINI.md | Exists, content size |
| .cursorrules, .cursor/rules/ | Cursor rules |
| .github/copilot-instructions.md, .github/instructions/ | Copilot instructions |
| .windsurfrules, .clinerules | Windsurf and Cline rules |
| memory-bank/ | Cline memory bank |
| docs/ | Existing files, and whether it is a published site: mkdocs.yml, docusaurus.config.*, .vitepress/, _config.yml |
| CHANGELOG.md, CONTRIBUTING.md | Exists, format |
| docs/adr/, doc/adr/, docs/decisions/ | Existing decision records |
| ROADMAP.md, TODO.md | Existing plans |
| .github/ISSUE_TEMPLATE/, PULL_REQUEST_TEMPLATE.md | Existing contribution setup |

## Agent tools in use

| Signal | Tool |
|---|---|
| CLAUDE.md, .claude/ | Claude Code |
| .cursor/, .cursorrules | Cursor |
| .codex/ | Codex |
| GEMINI.md, .gemini/ | Gemini CLI |
| .github/copilot-instructions.md | GitHub Copilot |
| .windsurf/, .windsurfrules | Windsurf |
| .clinerules, memory-bank/ | Cline |

Always add the agent you are running in.

## Result

Build an internal profile with every fact above and how sure you are about it. Then classify the repository as state A, B, C or D, as described in SKILL.md.

Start the first interview message with a findings summary of 2 to 5 lines in plain words. Example:

```text
I checked the repository:
• A Next.js app with TypeScript, tested with Vitest
• Git with a GitHub remote, 2 contributors, commits like "feat: add login"
• No documentation besides a default README
```
