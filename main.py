#!/usr/bin/env python3
"""One Line, One Laugh - make.fun entry.

Writes a single funny line (101 characters) to /output/entry.txt.
Standard library only - no third-party imports.
"""
import os
import sys

ENTRY = "I told the GPS I knew a shortcut. It rerouted me through a cornfield and now my car has trust issues."

def main():
    if not 1 <= len(ENTRY) <= 140:
        print("entry must be 1-140 chars, got %d" % len(ENTRY), file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("round-trip mismatch", file=sys.stderr)
        return 1
    print("wrote /output/entry.txt (%d chars)" % len(ENTRY))
    return 0

if __name__ == "__main__":
    sys.exit(main())
