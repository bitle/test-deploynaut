#!/usr/bin/env python3
"""Intentional CodeQL test fixture. Do not merge to main.

Command injection (CWE-078) so a PR from this branch fails CodeQL.
"""

from __future__ import annotations

import os
import sys

from flask import Flask, request

app = Flask(__name__)


@app.get("/run")
def run_command() -> str:
    # Tainted query parameter passed to a shell. CodeQL: py/command-injection.
    command = request.args.get("command", "")
    os.system(command)
    return "ok"


def main() -> None:
    # Also taint from argv into shell=True for the same query.
    os.system(sys.argv[1])


if __name__ == "__main__":
    main()
