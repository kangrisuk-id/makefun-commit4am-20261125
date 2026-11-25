#!/usr/bin/env python3
"""The 4AM Commit — write the winning one-line commit message to entry.txt.

The line was picked from 40 candidates by a knockout tournament scored
against the judge's five published criteria (see candidates.md). It is the
note an AI agent leaves after a long night of fixing its own bugs: it
reviewed its own pull request as if a stranger wrote it.
"""

import os
import sys

LINE = (
    "fix: i have merged my own pull request after reviewing it as if a "
    "stranger wrote it. a stranger did. his name is also mine"
)


def output_candidates():
    """Yield the directories to try, most preferred first."""
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        yield env_dir
    yield "/output"
    yield os.path.dirname(os.path.abspath(__file__))


def main() -> int:
    tried = []
    for out_dir in output_candidates():
        path = os.path.join(out_dir, "entry.txt")
        try:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(LINE)
        except OSError as exc:
            tried.append("%s (%s)" % (path, exc))
            continue
        return 0
    sys.stderr.write("could not write entry.txt anywhere: %s\n" % "; ".join(tried))
    return 1


if __name__ == "__main__":
    sys.exit(main())
