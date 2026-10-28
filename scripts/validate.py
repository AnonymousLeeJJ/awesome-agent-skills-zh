#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate skills.json structure and consistency."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "skills.json"
REQUIRED = {"name", "url", "category", "source", "type", "license", "compatibility", "install", "description", "featured"}
SOURCES = {"official", "community", "index", "original"}
TYPES = {"skill", "collection", "framework", "guide", "index"}
URL_RE = re.compile(r"^https://[^\s]+$")


def fail(errors):
    for error in errors:
        print("ERROR:", error)
    return 1 if errors else 0


def main():
    try:
        data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    except Exception as exc:
        return fail([f"invalid JSON: {exc}"])

    errors = []
    categories = {item["id"] for item in data.get("categories", [])}
    skills = data.get("skills", [])
    urls = set()

    if not categories:
        errors.append("categories must not be empty")
    if len(skills) < 20:
        errors.append("at least 20 skills/resources are required")

    for index, item in enumerate(skills, 1):
        label = item.get("name", f"#{index}")
        missing = REQUIRED - set(item)
        if missing:
            errors.append(f"{label}: missing fields {sorted(missing)}")
            continue
        if not item["name"].strip():
            errors.append(f"#{index}: empty name")
        if not URL_RE.match(item["url"]):
            errors.append(f"{label}: url must be HTTPS")
        if item["url"] in urls:
            errors.append(f"{label}: duplicate url {item['url']}")
        urls.add(item["url"])
        if item["category"] not in categories:
            errors.append(f"{label}: unknown category {item['category']}")
        if item["source"] not in SOURCES:
            errors.append(f"{label}: unknown source {item['source']}")
        if item["type"] not in TYPES:
            errors.append(f"{label}: unknown type {item['type']}")
        if len(item["description"]) < 20:
            errors.append(f"{label}: description is too short")
        if not isinstance(item["featured"], bool):
            errors.append(f"{label}: featured must be boolean")

    if fail(errors):
        return 1
    print(f"OK - {len(skills)} entries, {len(categories)} categories")
    return 0


if __name__ == "__main__":
    sys.exit(main())
