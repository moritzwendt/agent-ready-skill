# Changelog

All notable changes to this project are documented in this file. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] (2026-11-18)

### Added

- Setup workflow that detects the repository state, interviews the user, proposes a file plan and writes the docs only after confirmation.
- Interview rules and question bank: at most 4 questions per round and 3 rounds, lettered options with a recommendation, free text and skipping always allowed, targeted follow ups.
- Templates for AGENTS.md, PROJECT.md, STATUS.md, ROADMAP.md, CHANGELOG.md, GIT.md, LEARNINGS.md, README.md and the feature, decision and research folders.
- Git presets for solo work, pull requests, develop branches and open source, with agent commit permissions.
- Bridges for Claude Code and Gemini CLI, and merging of existing agent instruction files into AGENTS.md.
- Quick check for repositories that are already set up.
- Claude Code plugin marketplace entry.
