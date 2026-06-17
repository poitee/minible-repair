# Mini BLE replacement battery — BOM

## Required cell

| Property | Value | Source |
|----------|-------|--------|
| Chemistry | **NiMH** | [minible_hw](https://github.com/mooltipass/minible_hw) schematic (`BT1`) |
| Form factor | **2/3 AAA** | KiCad footprint `BAT_TWOTHIRD_AAA` |
| Nominal capacity | **~300 mAh** | [product specs](https://www.themooltipass.com) |
| Terminals | Solder tabs | Stock cell is through-hole soldered to PCB |

### Pad spacing (from KiCad footprint)

- Center-to-center between pads: **20.6 mm**
- Pad size: 4 × 3 mm oval holes

### Typical 2/3 AAA NiMH dimensions

| Dimension | Typical range |
|-----------|---------------|
| Diameter | 10.0 – 10.5 mm |
| Height (without tabs) | 30.0 – 31.0 mm |

Always measure your replacement cell before soldering.

## What **not** to use

- **LiPo / Li-ion cells** — charging circuitry implements a custom **NiMH** algorithm in firmware.
- **NiCd** — different charge profile; not validated on this hardware.
- Cells without reliable capacity ratings or unknown age (see [minible#422](https://github.com/mooltipass/minible/issues/422)).

## Example part categories

Search distributors for:

- `2/3 AAA NiMH 300mAh solder tabs`
- `2/3 AAA NiMH tagged`

Brands commonly used in tagged NiMH packs: Tenergy, Powerex, generic industrial tagged cells.

> Supplier links intentionally omitted — availability varies by region. Validate diameter and tab orientation against the original cell before ordering multiple units.

## Tools and consumables

- Temperature-controlled soldering iron (fine tip)
- Flux and lead-free solder
- Kapton tape
- ESD mat / wrist strap
- Plastic spudgers
- Multimeter (verify polarity and idle voltage after install)

## After installation

1. Inspect for solder bridges on battery pads.
2. Reassemble the device.
3. Connect USB and confirm the device boots.
4. In Moolticute, run **battery reconditioning** if available for your firmware bundle.
5. Disconnect USB and verify the device runs on battery power.

If the device only works on USB, the cell may be dead, reversed, or poorly soldered — not a firmware “security lock” ([#422](https://github.com/mooltipass/minible/issues/422)).

## Future hardware improvement

Upstream feature request: inline battery disconnect switch — [minible_hw#4](https://github.com/mooltipass/minible_hw/issues/4).
