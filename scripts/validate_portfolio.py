#!/usr/bin/env python3
"""Check the public QA portfolio for basic integrity and safe structure.

This is intentionally a documentation/integrity check. It does not execute the
Restaurant Menu Manager or claim an end-to-end test result.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    "README.md",
    "api/restaurant-menu.postman_collection.json",
    "case-studies/README.md",
    "case-studies/bestys-request-to-retest.md",
    "case-studies/aman-ai-incident-validation.md",
    "case-studies/quiz-curriculum-transfer.md",
    "case-studies/anonymized-stale-notification-bug.md",
    "evidence/README.md",
    "known-limitations.md",
    "test-charters/restaurant-menu-exploratory-charter.md",
    "test-runs/README.md",
)

CASE_STUDY_SECTIONS = {
    "case-studies/bestys-request-to-retest.md": (
        "## Context and confidentiality",
        "## My role",
        "## How I worked with a request",
        "## Tools and methods",
        "## What is not published",
    ),
    "case-studies/aman-ai-incident-validation.md": (
        "## Context and confidentiality",
        "## My role",
        "## What I check",
        "## How I document a mismatch",
        "## Evidence boundary",
    ),
    "case-studies/quiz-curriculum-transfer.md": (
        "## Context and confidentiality",
        "## User problem",
        "## My role",
        "## Acceptance criteria used for QA discussion",
        "## Tools and boundaries",
    ),
    "case-studies/anonymized-stale-notification-bug.md": (
        "## Context and confidentiality",
        "## Steps to reproduce",
        "## Actual result",
        "## Expected result",
        "## Retest boundary",
    ),
}

MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)#]+)(?:#[^)]+)?\)")
TOKEN_PATTERNS = (
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._-]{20,}\b"),
)


def error(errors: list[str], message: str) -> None:
    errors.append(message)


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "tel:", "#"))


def validate_required_files(errors: list[str]) -> None:
    for relative_path in REQUIRED_FILES:
        path = ROOT / relative_path
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            error(errors, f"Required non-empty file is missing: {relative_path}")


def validate_postman_json(errors: list[str]) -> None:
    path = ROOT / "api/restaurant-menu.postman_collection.json"
    try:
        collection = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        error(errors, f"Postman collection is not valid JSON: {exc}")
        return

    if not collection.get("info", {}).get("schema"):
        error(errors, "Postman collection has no schema.")
    if len(collection.get("item", [])) < 10:
        error(errors, "Postman collection must include meaningful smoke coverage (at least 10 requests).")


def validate_case_studies(errors: list[str]) -> None:
    for relative_path, sections in CASE_STUDY_SECTIONS.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if "[SANITIZED WORK CASE]" not in text:
            error(errors, f"Missing sanitized-work label: {relative_path}")
        for section in sections:
            if section not in text:
                error(errors, f"Missing required case-study section '{section}' in {relative_path}")


def validate_local_markdown_links(errors: list[str]) -> None:
    for markdown_file in ROOT.rglob("*.md"):
        text = markdown_file.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip()
            if not target or is_external(target):
                continue
            target_path = (markdown_file.parent / target).resolve()
            if not target_path.is_file():
                relative_file = markdown_file.relative_to(ROOT)
                error(errors, f"Broken local link in {relative_file}: {target}")


def validate_token_patterns(errors: list[str]) -> None:
    public_files = [*ROOT.rglob("*.md"), ROOT / "api/restaurant-menu.postman_collection.json"]
    for path in public_files:
        text = path.read_text(encoding="utf-8")
        for pattern in TOKEN_PATTERNS:
            if pattern.search(text):
                error(errors, f"Potential credential/token pattern found in {path.relative_to(ROOT)}")
                break


def main() -> int:
    errors: list[str] = []
    validate_required_files(errors)
    validate_postman_json(errors)
    validate_case_studies(errors)
    validate_local_markdown_links(errors)
    validate_token_patterns(errors)

    if errors:
        print("Portfolio integrity check failed:", file=sys.stderr)
        for message in errors:
            print(f"- {message}", file=sys.stderr)
        return 1

    print("Portfolio integrity check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
