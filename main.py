"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast for the invented city of Zibbleton
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure standard library; deterministic output.
"""

import os
from pathlib import Path

LINE = "Zibbleton: sunny spells, 21°C, light breeze off the Custard Sea — the 8:04 is late again, but the station pigeons are doing the tango."
# 134 characters, within the 1-140 gate. The em dash and °C are single
# UTF-8 characters; the file is written without a trailing newline so the
# entry is exactly one line of 134 characters.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
