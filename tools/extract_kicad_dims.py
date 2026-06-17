#!/usr/bin/env python3
"""Extract Mini BLE main-board dimensions from minible_hw KiCad files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


def pcb_bounds(pcb_text: str) -> tuple[float, float, float, float]:
    lines = re.findall(
        r"\(gr_line \(start ([\d.]+) ([\d.]+)\) \(end ([\d.]+) ([\d.]+)\) \(layer Edge\.Cuts\)",
        pcb_text,
    )
    xs, ys = [], []
    for a, b, c, d in lines:
        xs += [float(a), float(c)]
        ys += [float(b), float(d)]
    for a, b in re.findall(
        r"\(gr_arc \(start ([\d.]+) ([\d.]+)\).*?\(layer Edge\.Cuts\)", pcb_text
    ):
        xs.append(float(a))
        ys.append(float(b))
    return min(xs), min(ys), max(xs), max(ys)


def module_at(pcb_text: str, footprint: str) -> tuple[float, float, float] | None:
    pattern = rf"\(module footprints:{re.escape(footprint)}[^\n]*\n\s+\(at ([\d.]+) ([\d.]+)(?: ([\d.]+))?\)"
    match = re.search(pattern, pcb_text)
    if not match:
        return None
    rot = float(match.group(3)) if match.group(3) else 0.0
    return float(match.group(1)), float(match.group(2)), rot


def main() -> int:
    default = Path(__file__).resolve().parents[1].parent / "minible_hw/main_board/mini_ble.kicad_pcb"
    pcb_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default
    pcb_path = pcb_path.resolve()
    if pcb_path.suffix != ".kicad_pcb" or not pcb_path.is_file():
        print(f"Expected an existing .kicad_pcb file, got: {pcb_path}", file=sys.stderr)
        return 1
    pcb = pcb_path.read_text()
    x0, y0, x1, y1 = pcb_bounds(pcb)
    pcb_l, pcb_w = x1 - x0, y1 - y0

    case_l, case_w, case_h = 89.0, 35.5, 12.5
    margin_x = (case_l - pcb_l) / 2
    margin_y = (case_w - pcb_w) / 2

    def case_xy(px: float, py: float) -> tuple[float, float]:
        return px - x0 + margin_x, py - y0 + margin_y

    features = {}
    for name, fp in [
        ("usb", "USB_C_Receptacle_GT-USB-7010"),
        ("wheel", "SRBE210200"),
        ("oled", "SCREEN_M01084"),
        ("smartcard", "CON_SMARTCARD_CLONE_91-90473-003A"),
        ("battery", "BAT_TWOTHIRD_AAA"),
        ("mount_j1", "FIX_M1.4"),
    ]:
        pos = module_at(pcb, fp)
        if pos:
            cx, cy = case_xy(pos[0], pos[1])
            features[name] = {"pcb_mm": [pos[0], pos[1]], "case_mm": [round(cx, 2), round(cy, 2)]}

    mounts: list[tuple[str, float, float]] = []
    for m in re.finditer(
        r"\(module footprints:FIX_M1\.4.*?\(at ([\d.]+) ([\d.]+).*?\(fp_text reference (J\d+)",
        pcb,
        re.S,
    ):
        px, py, ref = float(m.group(1)), float(m.group(2)), m.group(3)
        cx, cy = case_xy(px, py)
        mounts.append((ref, round(cx, 2), round(cy, 2)))

    for ref, cx, cy in mounts:
        features[ref.lower()] = {"pcb_mm": None, "case_mm": [cx, cy]}

    data = {
        "source": str(pcb_path),
        "pcb_mm": {"length": round(pcb_l, 2), "width": round(pcb_w, 2)},
        "case_mm": {"length": case_l, "width": case_w, "height": case_h},
        "pcb_margin_mm": {"x": round(margin_x, 2), "y": round(margin_y, 2)},
        "features": features,
    }
    print(json.dumps(data, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
