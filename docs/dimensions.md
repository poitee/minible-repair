# Mechanical dimensions

Values below are derived from [mooltipass/minible_hw](https://github.com/mooltipass/minible_hw) `main_board/mini_ble.kicad_pcb` and published retail specifications.

Regenerate `dimensions.json`:

```bash
python3 tools/update_dimensions.py
```

## Envelope

| Item | mm |
|------|-----|
| Retail case (L × W × H) | 89.0 × 35.5 × 12.5 |
| Main PCB (L × W) | 74.8 × 31.2 |
| PCB inset margin (X / Y) | 7.1 / 2.15 |

## Coordinate system (case)

- Origin: bottom-left-back corner
- **+X** → scroll wheel end
- **+Y** → smartcard edge
- **+Z** → display face

## Feature positions (case coordinates)

| Feature | X | Y | Notes |
|---------|---|---|-------|
| USB-C | 72.9 | 5.35 | GT-USB-7010 receptacle |
| Scroll wheel | 78.4 | 17.75 | SRBE210200 |
| OLED center | 41.4 | 17.75 | ~52 × 14 mm window (active area — verify) |
| Smartcard | 19.0 | 29.3 | Slot on +Y edge |
| Battery BT1 | 7.4 | 17.75 | 2/3 AAA NiMH, soldered |
| Mount J1 | 9.6 | 3.75 | M1.4 |
| Mount J2 | 9.6 | 31.75 | M1.4 |

## Battery cell

| Property | Value |
|----------|-------|
| Footprint | `BAT_TWOTHIRD_AAA` |
| Chemistry | NiMH |
| Capacity | ~300 mAh |
| Pad spacing | 20.6 mm center-to-center |

## Still verify on hardware

- PCB stack height (`pcb_h` in OpenSCAD, default 6.0 mm)
- OLED visible area vs. bezel overlap
- USB-C recess depth for your cable shell
- Factory aluminum shell internal ribs (not modeled in KiCad)

## References

- [FCC internal photos (MBLE1)](https://fccid.io/2AYPT-MBLE1/Internal-Photos/Internal-Photos-5088688)
- [minible_hw#4 — battery disconnect switch request](https://github.com/mooltipass/minible_hw/issues/4)
