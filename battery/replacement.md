# Battery replacement procedure

## Before you start

- Read [BOM.md](BOM.md) and confirm you have a **tagged 2/3 AAA NiMH** cell.
- Export your credentials from Moolticute if you have not recently backed up.
- Work on an ESD-safe surface.
- Expect to **open or replace the outer shell** — see [../docs/teardown.md](../docs/teardown.md).

## Discharge handling

If the old cell still holds charge, avoid shorting the tabs. Insulate removed cell terminals with tape.

## Removal

1. Open the device enclosure and expose the main PCB.
2. Note pad polarity — photograph the original orientation.
3. Apply flux to both battery pads.
4. Heat each pad in turn and lift the cell free with minimal force on the tabs.
5. Remove residual solder from pads if needed so the new tabs sit flat.

## Installation

1. Match the **positive tab** to the pad marked `BAT+` on the [PSU schematic](https://github.com/mooltipass/minible_hw/blob/master/main_board/mini_ble_psu.sch).
2. Tack one tab, verify alignment, then solder the second tab.
3. Avoid excessive heat — work quickly and let the cell cool between attempts.
4. Visually inspect joints under good light.

## Reassembly and validation

1. Route the OLED flex cable carefully — it is easy to damage ([minible_hw#4](https://github.com/mooltipass/minible_hw/issues/4)).
2. Reinstall the PCB in your shell (factory aluminum or [printed service shell](../case/minible-shell.scad)).
3. Connect USB:
   - Device should enumerate normally.
   - Leave on charge until the firmware reports a full state.
4. Unplug USB and confirm:
   - Power-on via scroll wheel click
   - Stable operation for at least several minutes
   - Reasonable battery indicator behavior

## Troubleshooting

| Symptom | Likely cause |
|---------|----------------|
| Works on USB only | Weak/counterfeit cell, cold solder joint, reversed polarity |
| Rapid shutdown after unplug | Cell not actually charged, high self-discharge cell |
| Overheating on charge | Wrong chemistry installed — **stop and disconnect** |

## Firmware notes

The Mini BLE firmware includes a custom NiMH charging routine. There is no documented “battery pairing” or anti-replacement lock — failures are almost always hardware-related.

For persistent issues after verifying a known-good cell, open a discussion in this repo with photos of the solder joints (not your credentials).
