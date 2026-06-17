# Contributing

Thank you for helping make the Mini BLE repairable.

## What we need most

1. **Teardown photos** with caliper measurements of the factory aluminum shell
2. **Print fit reports** — which parameters needed adjustment on your printer
3. **Validated battery suppliers** — tagged 2/3 AAA NiMH cells that fit and hold charge
4. **Opening technique** — repeatable steps to remove the stock shell without destroying the PCB

## Pull request checklist

- [ ] Measurements include units (mm) and photo of calipers where possible
- [ ] OpenSCAD changes note which parameter was tuned and why
- [ ] Battery-related changes confirm **NiMH only**
- [ ] No credentials, serial numbers, or smartcard photos in commits

## Regenerating dimensions

If `minible_hw` is checked out beside this repo:

```bash
git clone https://github.com/mooltipass/minible_hw.git ../minible_hw
python3 tools/update_dimensions.py
```

Update `case/minible-shell.scad` if feature coordinates change.

## Upstreaming

Hardware improvement ideas (battery disconnect switch, service-friendly enclosure) may also belong in [minible_hw issues](https://github.com/mooltipass/minible_hw/issues).
