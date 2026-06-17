#!/usr/bin/env python3
"""Write docs/dimensions.json from minible_hw KiCad PCB."""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PCB = ROOT.parent / "minible_hw" / "main_board" / "mini_ble.kicad_pcb"
OUT = ROOT / "docs" / "dimensions.json"
SCRIPT = ROOT / "tools" / "extract_kicad_dims.py"


def main() -> int:
    if not PCB.exists():
        print(f"Missing KiCad PCB: {PCB}", file=sys.stderr)
        print("Clone minible_hw next to this repo or pass a PCB path.", file=sys.stderr)
        return 1
    raw = subprocess.check_output([sys.executable, str(SCRIPT), str(PCB)], text=True)
    OUT.write_text(raw)
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
