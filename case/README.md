# Case parts

Parametric OpenSCAD shell for servicing a Mini BLE after the factory aluminum case is opened or damaged.

## Files

| File | Description |
|------|-------------|
| `minible-shell.scad` | Source model — edit parameters here |
| `export-stl.sh` | Headless STL export |
| `stl/` | Generated meshes (after export) |
| `print-settings.md` | Suggested slicer settings |

## Quick start

**Pre-built STLs** are in [`case/stl/`](stl/) — ready to slice.

To regenerate after editing `minible-shell.scad` or `tools/generate_stl.py`:

```bash
pip3 install -r tools/requirements.txt
./case/export-stl.sh
```

Or only:

```bash
python3 tools/generate_stl.py
```

OpenSCAD is optional (see `minible-shell.scad` for parametric edits); STL export uses Python + [trimesh](https://github.com/mikedh/trimesh).

This writes:

- `case/stl/minible-shell-top.stl` — display face + scroll wheel bore
- `case/stl/minible-shell-bottom.stl` — USB-C, smartcard slot, battery pocket
- `case/stl/minible-battery-door.stl` — optional cover for battery pocket

## Assembly

1. Print top and bottom shells (see `print-settings.md`).
2. Dry-fit the PCB without the battery.
3. Route the OLED flex cable before closing the shell.
4. Join halves with four M2 screws through J1/J2 standoff posts (length depends on print — start with 8–10 mm).
5. Optionally tape or screw the battery door over the access pocket.

## Tuning fit

Open `minible-shell.scad` and adjust:

- `clearance` — global PCB pocket tolerance (default 0.4 mm)
- `usb_open_*` — USB cutout size
- `wheel_bore_d` — scroll wheel clearance
- `battery_door_*` — under-cell access opening

After changing parameters tied to KiCad, update `docs/dimensions.md` and note your caliper measurements in the pull request.

## Orientation preview

In OpenSCAD, set `part = "both"` to preview top + bottom + battery door layouts side by side.
