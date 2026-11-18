import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = ROOT / "skills" / "agent-ready"
SKILL_MD = SKILL_DIR / "SKILL.md"
TEMPLATES = SKILL_DIR / "assets" / "templates"
VERBATIM_TEMPLATES = ["feature.md", "decision.md", "research.md"]
MARKER_PREFIX = "Documentation system: [agent-ready]"
MAX_SKILL_LINES = 500
SKIPPED_FOLDERS = {".git", ".local", "node_modules"}
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)

errors = []


def fail(message):
    errors.append(message)


def read(path):
    return path.read_text(encoding="utf-8")


def links(path):
    text = FENCE.sub("", read(path))
    for target in LINK.findall(text):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        yield target.split("#", 1)[0]


def skill_version():
    parts = read(SKILL_MD).split("---", 2)
    if len(parts) < 3:
        fail("SKILL.md has no frontmatter")
        return None
    match = re.search(r'^\s+version:\s*"?([^"\n]+?)"?\s*$', parts[1], re.MULTILINE)
    return match.group(1) if match else None


def check_skill():
    lines = read(SKILL_MD).splitlines()
    if len(lines) >= MAX_SKILL_LINES:
        fail(f"SKILL.md has {len(lines)} lines, the limit is {MAX_SKILL_LINES}")
    linked = set(links(SKILL_MD))
    for reference in sorted((SKILL_DIR / "references").glob("*.md")):
        name = reference.relative_to(SKILL_DIR).as_posix()
        if name not in linked:
            fail(f"SKILL.md does not link {name}")


def check_templates():
    for name in VERBATIM_TEMPLATES:
        if "{{" in read(TEMPLATES / name):
            fail(f"templates/{name} is copied unchanged and must not contain markers")
    last_line = read(TEMPLATES / "AGENTS.md").rstrip().splitlines()[-1]
    if not last_line.startswith(MARKER_PREFIX):
        fail("templates/AGENTS.md must end with the marker line")


def check_versions():
    version = skill_version()
    manifest = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))
    versions = {
        "SKILL.md": version,
        "marketplace metadata": manifest.get("metadata", {}).get("version"),
    }
    for plugin in manifest.get("plugins", []):
        versions[f"plugin {plugin.get('name')}"] = plugin.get("version")
    if len(set(versions.values())) != 1:
        fail("versions differ: " + ", ".join(f"{key} {value}" for key, value in versions.items()))
    if version and f"## [{version}]" not in read(ROOT / "CHANGELOG.md"):
        fail(f"CHANGELOG.md has no heading for version {version}")


def check_links():
    for path in sorted(ROOT.rglob("*.md")):
        relative = path.relative_to(ROOT)
        if relative.parts[0] in SKIPPED_FOLDERS or TEMPLATES in path.parents:
            continue
        for target in links(path):
            if not (path.parent / target).exists():
                fail(f"{relative}: broken link to {target}")


def main():
    check_skill()
    check_templates()
    check_versions()
    check_links()
    for message in errors:
        print(f"error: {message}")
    if errors:
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
