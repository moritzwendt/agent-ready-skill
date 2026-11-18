# Bridges

AGENTS.md is the single source of rules. Tools that do not read AGENTS.md get a bridge: a small file in the place the tool looks, pointing to AGENTS.md.

## Which tools need a bridge

| Tool | Reads | Bridge |
|---|---|---|
| Codex | AGENTS.md | None |
| Cursor | AGENTS.md | None |
| GitHub Copilot | AGENTS.md | None |
| Claude Code | CLAUDE.md, and AGENTS.md only when no CLAUDE.md exists | CLAUDE.md |
| Gemini CLI | GEMINI.md | GEMINI.md |
| Any other tool | Its own rules file | Its rules file with one line pointing to AGENTS.md |

Create a bridge for every tool found in detection plus the agent you are running in. Create no bridges for tools nobody uses.

## Bridge content

### CLAUDE.md

```markdown
@AGENTS.md
```

Claude Code imports the referenced file. This works in versions with and without native AGENTS.md support.

### GEMINI.md

```markdown
@AGENTS.md
```

Gemini CLI imports referenced markdown files the same way.

### Other tools

```markdown
Read AGENTS.md in the repository root before doing anything else. It holds all project rules and the map of the documentation.
```

## Existing tool files

When a tool file already has content:

1. Sort its content into three groups:
   1. Project rules and facts: they move into AGENTS.md.
   2. Tool specific settings that only this tool understands, such as Claude Code hook notes or Cursor rule metadata: they stay.
   3. Duplicates of what AGENTS.md already says: they are dropped.
2. Show the result in the proposal: which lines move, which stay, which are dropped as duplicates.
3. After the user confirms, rewrite the file as the bridge line followed by the tool specific part:

```markdown
@AGENTS.md

## Claude Code specific

[lines that only make sense for Claude Code]
```

4. If the user prefers to keep a tool file unchanged, keep it, and add the bridge line at the top only if they agree.

### Legacy files

| File | Handling |
|---|---|
| .cursorrules | Cursor's old format. Merge rules into AGENTS.md. Suggest deleting the file in the report, but never delete it yourself. |
| .cursor/rules/*.mdc | Keep files with file patterns or tool settings. Merge plain project rules into AGENTS.md. |
| .github/copilot-instructions.md | Merge into AGENTS.md, then replace with the other tools bridge line. |
| .windsurfrules, .clinerules | Merge into AGENTS.md, then replace with the other tools bridge line. |
| memory-bank/ | Keep it unchanged in this version and link it from the doc map. Mention in the report that its content overlaps with docs/. |
