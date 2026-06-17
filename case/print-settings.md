# Print settings

## Recommended material

| Material | Notes |
|----------|-------|
| **PETG** | Good durability, moderate heat resistance — good default |
| **ASA** | Better heat resistance near USB-C port area |
| **PLA** | Acceptable for prototyping; may creep in warm environments |

## Suggested parameters (starting point)

| Setting | Value |
|---------|-------|
| Layer height | 0.2 mm |
| Perimeters | 3–4 |
| Infill | 20–25 % gyroid or grid |
| Horizontal expansion | 0 – 0.1 mm (tune fit) |
| Support | Usually none if printing shells upright |

## Orientation

Print each half **flat on the split face** so the mating flange is accurate.

## Post-processing

- Test-fit the PCB without the battery installed.
- Open the USB-C slot with a file if your printer tolerances are loose.
- Dry-fit the scroll wheel bore before gluing anything.

## Fit validation checklist

- [ ] PCB drops in without bowing
- [ ] USB-C plug inserts fully
- [ ] OLED window aligns with display active area
- [ ] Scroll wheel rotates without rubbing
- [ ] Halves close without flexing the PCB
- [ ] Smartcard inserts cleanly

Mark any parameter tweaks in a pull request with your measured values.
