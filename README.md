# Mooltipass Mini BLE repair project

Community guides and printable parts to extend the life of a Mini BLE.

## Contents

| Path | Description |
|------|-------------|
| [battery/BOM.md](battery/BOM.md) | Replacement cell specifications and sourcing notes |
| [battery/replacement.md](battery/replacement.md) | Step-by-step battery swap procedure |
| [case/minible-shell.scad](case/minible-shell.scad) | Parametric service shell (OpenSCAD) |
| [case/stl/](case/stl/) | **Print-ready STL files** (top, bottom, battery door) |
| [case/README.md](case/README.md) | How to export STLs and assemble the shell |
| [case/print-settings.md](case/print-settings.md) | Suggested slicer settings |
| [docs/dimensions.md](docs/dimensions.md) | KiCad-derived mechanical reference |
| [docs/teardown.md](docs/teardown.md) | Case opening notes and internal layout |
| [tools/extract_kicad_dims.py](tools/extract_kicad_dims.py) | Regenerate feature coordinates from KiCad |

## Quick links

**Replace the battery** → start with [battery/BOM.md](battery/BOM.md)

**Print a service shell** → [case/README.md](case/README.md)

**Open the factory case** → [docs/teardown.md](docs/teardown.md)

## Important safety notes

- The Mini BLE uses a **NiMH** cell, not LiPo. Do not install a lithium cell.
- The stock cell is soldered to the PCB. Replacement requires soldering skills.
- Opening the factory aluminum shell may damage it. Treat this project as a **repair path**, not a drop-in factory replacement.
- You are responsible for safe handling of batteries and ESD-sensitive electronics.

## Device reference dimensions

Published external size: **89.0 × 35.5 × 12.5 mm** (L × W × H).

PCB outline from [minible_hw](https://github.com/mooltipass/minible_hw): **74.8 × 31.2 mm**.

Battery: **2/3 AAA NiMH**, ~300 mAh (`BAT_TWOTHIRD_AAA`).

Full coordinate table: [docs/dimensions.md](docs/dimensions.md).

## Status

Community draft — fit has not been validated on physical hardware yet. If you print the shell or complete a battery swap, please share caliper measurements and photos.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT — see [LICENSE](LICENSE).

## Related upstream projects

- [mooltipass/minible](https://github.com/mooltipass/minible) — firmware
- [mooltipass/minible_hw](https://github.com/mooltipass/minible_hw) — hardware design files
- [mooltipass/moolticute](https://github.com/mooltipass/moolticute) — desktop companion
