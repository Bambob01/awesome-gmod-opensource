#!/usr/bin/env python3
"""Checks README.md entries for consistent formatting.

Runs automatically on every pull request. Run it yourself with:
    python3 scripts/check_format.py
"""
import re
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"

PROJECT_SECTIONS = {
    "Server Administration and Anti-Cheat",
    "Gamemodes and Frameworks",
    "Addon Development Tools",
    "Libraries and Binary Modules",
    "Client Fixes and Performance",
}
RESOURCE_SECTIONS = {"Learning Resources and Communities"}

# A license tag is an SPDX identifier (MIT, GPL-3.0, Apache-2.0, Unlicense...),
# a dual license such as MIT/Apache-2.0, or one of these special values.
SPECIAL_LICENSES = {"Custom", "No license"}
SPDX_LIKE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9.+-]*(/[A-Za-z0-9][A-Za-z0-9.+-]*)?$")
# Common mistakes: putting the language first, or using GitHub's placeholder values.
NOT_LICENSES = {
    "Lua", "C", "C++", "C#", "Rust", "Go", "Python", "JavaScript", "TypeScript",
    "Haskell", "Shell", "MoonScript", "None", "NOASSERTION", "Other", "Proprietary",
    "Commercial", "Paid",
}

HYPE_WORDS = re.compile(
    r"\b(best|greatest|amazing|awesome|revolutionary|incredible|ultimate|#1|number one)\b",
    re.IGNORECASE,
)

ENTRY = re.compile(
    r"^- \[(?P<name>[^\]]+)\]\((?P<url>https?://[^)\s]+)\) - "
    r"(?P<desc>[A-Z0-9\"'].*?[.!?])(?P<tags>(?: `[^`]+`)*)$"
)


def sort_key(name: str) -> str:
    return name.casefold()


def is_license(tag: str) -> bool:
    if tag in SPECIAL_LICENSES:
        return True
    return tag not in NOT_LICENSES and bool(SPDX_LIKE.match(tag))


def main() -> int:
    errors = []
    section = None
    names_in_block = []
    seen_urls = {}

    def check_order(block, sec):
        for (prev_line, prev), (line_no, cur) in zip(block, block[1:]):
            if sort_key(cur) < sort_key(prev):
                errors.append(
                    f"line {line_no}: '{cur}' should come before '{prev}' "
                    f"(entries in '{sec}' must be alphabetical)"
                )

    lines = README.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines, start=1):
        if line.startswith("## ") or line.startswith("### "):
            check_order(names_in_block, section)
            names_in_block = []
            if line.startswith("## "):
                section = line[3:].strip()
            continue

        if not line.startswith("- [") or section not in (PROJECT_SECTIONS | RESOURCE_SECTIONS):
            continue

        m = ENTRY.match(line)
        if not m:
            errors.append(
                f"line {i}: doesn't match the format "
                "'- [Name](https://link) - Sentence ending with a period. `License` `Language`'"
            )
            continue

        name, url, desc = m["name"], m["url"], m["desc"]
        tags = re.findall(r"`([^`]+)`", m["tags"])
        names_in_block.append((i, name))

        normalized = url.rstrip("/").lower()
        if normalized in seen_urls:
            errors.append(f"line {i}: duplicate link (also on line {seen_urls[normalized]})")
        seen_urls[normalized] = i

        if len(desc.split()) > 30:
            errors.append(f"line {i}: description is long; please keep it to one short sentence")
        if HYPE_WORDS.search(desc):
            errors.append(f"line {i}: please avoid hype words like 'best' or 'amazing' in descriptions")

        if section in PROJECT_SECTIONS:
            if len(tags) != 2:
                errors.append(f"line {i}: projects need exactly two tags: `License` `Language`")
            elif not is_license(tags[0]):
                errors.append(
                    f"line {i}: first tag '{tags[0]}' should be a license, e.g. `MIT`, "
                    "`GPL-3.0`, `Custom` or `No license` (see CONTRIBUTING.md)"
                )
        elif section in RESOURCE_SECTIONS:
            if tags:
                errors.append(f"line {i}: learning resources and communities don't need tags")

    check_order(names_in_block, section)

    if errors:
        print("Formatting problems found in README.md:\n")
        for e in errors:
            print("  - " + e)
        print("\nSee CONTRIBUTING.md for the format. Thanks for contributing!")
        return 1

    print(f"README.md looks good ({len(seen_urls)} entries checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
