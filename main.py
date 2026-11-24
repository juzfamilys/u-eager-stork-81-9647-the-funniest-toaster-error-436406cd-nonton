"""The Funniest Toaster Error Message — make.fun entry (program/v1).

Writes one line, at most 120 characters — the funniest error message a
kitchen toaster would show its owner — to /output/entry.txt.

Pure Python standard library only. Deterministic: the same bytes every run.
"""

import os
import sys

# The entry: one deadpan line, no toast/burnt/pop-up puns.
# Fresh angle: the toaster meets a frozen slice and refuses the miracle.
ENTRY = "ERROR: BREAD STILL FROZEN. I AM A TOASTER, NOT A MIRACLE WORKER."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> int:
    line = ENTRY
    if not (1 <= len(line) <= 120):
        print(f"invalid entry length: {len(line)} chars", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("invalid entry: must be a single line", file=sys.stderr)
        return 1
    if line != line.strip():
        print("invalid entry: leading/trailing whitespace", file=sys.stderr)
        return 1
    # Voice guard: a real toaster error message, deadpan, in the appliance's
    # own voice — and the joke must not lean on the obvious toast puns.
    if not line.startswith("ERROR"):
        print("invalid entry: must read as a toaster error message", file=sys.stderr)
        return 1
    words = set(line.lower().replace(".", " ").replace(",", " ").split())
    for cliche in ("burnt", "toast", "pop-up", "crumb"):
        if cliche in words:
            print(f"invalid entry: leans on the obvious pun: {cliche}", file=sys.stderr)
            return 1
    data = line.encode("utf-8")
    # Round-trip check: valid UTF-8, same text back.
    if data.decode("utf-8") != line:
        print("invalid entry: not valid UTF-8", file=sys.stderr)
        return 1
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    print(line)
    print(f"chars: {len(line)}, bytes: {len(data)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
